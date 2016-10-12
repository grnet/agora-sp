
var formName = 'Service Component Implementation Detail Form';

var componentId = null;
var componentName = null;
var componentImplementationId = null;
var componentImplementationName = null;
var opType = "";
var globalComponentData;
var globalImplementationData;

var optionsData = [
  {id: 1, value: 1, text: "option 1"},
  {id: 2, value: 2, text: "option 2"},
	{id: 3, value: 3, text: "option 3"}
];

var resourceObject = [
	{ tag: 'input', type: 'text', name: 'version', placeholder: 'Enter version', label: 'Version' },
	{ tag: 'textarea', type: 'textarea', name: 'configuration_parameters', placeholder: "Enter configuration parameters", label: 'Configuration Parameters', onChange: 'textareaHTMLValidation' },
	{ tag: 'input', type: 'text', name: 'component_id', label: 'Component', placeholder: "Enter component name" },
	{ tag: 'input', type: 'text', name: 'component_implementation_id', label: 'Component implementation', placeholder: "Enter component implementation name" }
];

var OptionsComponent = React.createClass({
	render: function(){
		var htmlOptions = this.props.options.map(function(option) {
      return(
      	<option value={option.value} key={option.id}>{option.text}</option>
      );
		});		
		return (
			<select name={this.props.selectName} id={this.props.selectName} className="form-control">
				{htmlOptions}
		  </select>
		);
	}
});

var FormWrapper = React.createClass({

	generateFormElements: function(resourceObject){
		var formElements = resourceObject.map(function(field, i){
			if(field.tag == 'input'){
				if(field.type == 'text'){					
					return (
						<div className="form-group" key={i}>
			      	        <label htmlFor={field.name}>{field.label}</label>			      	        
			      	        <input className="form-control" id={field.name} type={field.type} name={field.name} placeholder={field.placeholder} aria-describedby={field.name + '-error'} />
			      	        <span id={field.name + '-error'} className="validation-message sr-only"></span>
			      	    </div>
					);
				}
			}
			else if(field.tag == 'textarea'){
				return(
					<div className="form-group" key={i}>
					    <label htmlFor={field.name}>{field.label}</label>
					    <textarea className="form-control" id={field.name} name={field.name} placeholder={field.placeholder} rows="6" onChange={this[field.onChange]}></textarea>
					    <span id={field.name + '-error'} className="validation-message sr-only"></span>
					</div>
				);				
			}
			else if(field.tag == 'select'){
				return(
					<div className="form-group">
					    <label htmlFor={field.name}>{field.label}</label>
					    <OptionsComponent options={field.optionsData} selectName={field.name}></OptionsComponent>
					    <span id={field.name + '-error'} className="validation-message sr-only"></span>
					</div>
				);				
			}
		}, this);
		return formElements;
	},

	markInvalid: function(elRef, message){

		$('#' + elRef).next().removeClass('sr-only');
		$('#' + elRef).next().html(message);
		$('#' + elRef).parent().addClass('has-error');
		$('html, body').animate({
        scrollTop: $('#' + elRef).offset().top
    	}, 800);
	},

	clearValidations: function(){
		$('body').find('.has-error').removeClass('has-error');
		$('body').find('.validation-message').addClass('sr-only');
	},

	textareaHTMLValidation: function(e){
		var div = document.createElement('div');
		div.innerHTML = $(e.target).val();
		if($(div).find('script').length > 0 || $(div).find('link').length){
			div = null;
			this.markInvalid($(e.target).attr('name'), 'This HTML content must not have script or css tags');
		}
		else{
			$(e.target).parent().removeClass('has-error');
			$(e.target).parent().find('.validation-message').addClass('sr-only');
		}
		div = null
	},

	validateForm: function(e){
		this.clearValidations();
		var validationObjects = [];
		var validationMessage = ''

		// --- validation code goes here ---
		if($('#version').val() == ''){
			validationMessage = "The version is required"
			validationObjects.push( { field: 'version', message: validationMessage } );
		}
		if($('#version').val().length > 255){
			validationMessage = "Content exceeds max length of 255 characters."
			validationObjects.push( { field: 'version', message: validationMessage } );			
		}
		var comp_id = $('#component_id').val();
		if(comp_id == null || comp_id == ""){
			validationMessage = "The component is required.";
			validationObjects.push( { field: 'component_id', message: validationMessage } );
		}
		var comp_imp_id = $('#component_implementation_id').val();
		if(comp_imp_id == null || comp_imp_id == ""){
			validationMessage = "The component is required.";
			validationObjects.push( { field: 'component_implementation_id', message: validationMessage } );
		}

		if(validationObjects.length > 0){
			var i = 0;
			for (i = 0; i < validationObjects.length; i++) {
			    this.markInvalid(validationObjects[i].field, validationObjects[i].message);
			}
			return false;
		}

		return true;
	},

	handleSubmit: function(e) {
		// some validation
		// ajax url call + redirect
		e.preventDefault();

		if(this.validateForm()){			
			//var formValues = JSON.stringify($("#service-form").serializeJSON());
			//console.log("The form values are ->", formValues);


			var component_id =  $("#component_id").val();

			if(componentName != component_id){
				if(componentName != null || component_id != "")
				{
					componentName = null;
					componentId = null;
					for(var i = 0; i < globalComponentData.length; i++){
						if(component_id == globalComponentData[i].name){
							componentId = globalComponentData[i].uuid;
							componentName = component_id;
							break;
						}
					}
				}
			}


			var component_implementation_id =  $("#component_implementation_id").val();

			if(componentImplementationName != component_implementation_id){
				if(componentImplementationName != null || component_implementation_id != "")
				{
					componentImplementationName = null;
					componentImplementationId = null;
					for(var i = 0; i < globalImplementationData.length; i++){
						if(component_implementation_id == globalImplementationData[i].name){
							componentImplementationId = globalImplementationData[i].uuid;
							componentImplementationName = component_implementation_id;
							break;
						}
					}
				}
			}

			var params = {};
			params["version"] = $("#version").val();
			params["configuration_parameters"] = $("#configuration_parameters").val();
			params["component_uuid"] = componentId;
			params["component_implementation_uuid"] = componentImplementationId;


			var parts = window.location.href.split("/");
			var host = "https://" + parts[2];
			var url = "";

			if(this.props.source != null && this.props.source != ""){
				params["uuid"] = parts[parts.length - 1];
				url = host + "/api/v1/component/service_component_implementation_detail/edit";
				opType = "edit";
			}
			else {
				url = host + "/api/v1/component/service_component_implementation_detail/add";
				opType = "add";
			}


			this.serverRequest = $.ajax({
				url: url,
				headers: {"X-CSRFToken": $("input[name=csrfmiddlewaretoken]")[0].value },
				dataType: "json",
				crossDomain: true,
				type: "POST",
				contentType:"application/json",
				cache: false,
				data: JSON.stringify(params),
				success: function (data) {
					if(opType == "add")
						$("#modal-success-body").text("You have successfully inserted a new component implementation detail");
					else
						$("#modal-success-body").text("You have successfully updated the component implementation detail");
					$("#modal-success").modal('show');
				}.bind(this),
				error: function (xhr, status, err) {
					var response = JSON.parse(xhr.responseText);
					$("#modal-body").text(response.errors.detail);
					$("#modal-danger").modal('show');
				}.bind(this)
			});

		}
		else{
		}
		
	},

	getInitialState: function () {
		return {
			component: {
				version: "",
				configuration_parameters: ""
			}
		}
	},

    componentDidMount: function () {

        if(this.props.source == null || this.props.source == "")
            return;

        jQuery.support.cors = true;
        this.serverRequest = $.ajax({
            url: this.props.source,
            dataType: "json",
            crossDomain: true,
            type: "GET",
            cache: false,
            success: function (data) {
                this.setState({component: data.data});
                $("#version").val(this.state.component.version);
                $("#configuration_parameters").val(this.state.component.configuration_parameters);
                $("#component_id").val(this.state.component.service_component.name);
                $("#component_implementation_id").val(this.state.component.service_component_implementation.name);
				componentId = this.state.component.service_component.uuid;
				componentName = this.state.component.service_component.name;
				componentImplementationId = this.state.component.service_component_implementation.uuid;
				componentImplementationName = this.state.component.service_component_implementation.name;
            }.bind(this),
            error: function (xhr, status, err) {
                console.log(this.props.source, status, err.toString());
            }.bind(this)
        });
    },

    componentWillUnmount: function () {
        this.serverRequest.abort();
    },

	render: function(){		
		var formElements = this.generateFormElements(this.props.resourceObject);
		return(
			<div className="widget">
					<div className="widget-header bordered-bottom bordered-blue">
			     	<span className="widget-caption">{this.props.formName}</span>
			    </div>
			    <div className="widget-body">
			    	<form role="form" onSubmit={this.handleSubmit} id="service-form">
			    		{formElements}
			    		<button type="submit" className="btn btn-blue">Submit</button>
			    	</form>
			   	</div>
			</div>
		);
	}
});

ReactDOM.render(
  <FormWrapper resourceObject={resourceObject} formName={formName} source={$("#source")[0].value}/>,
  document.getElementById('write-content')
);


$( function() {

	var temp = null;
	$(document).bind('click', function (event) {
        // Check if we have not clicked on the search box
        if (!($(event.target).parents().andSelf().is('#component_id'))) {
			$(".ui-menu-item").remove();
		}

		if (!($(event.target).parents().andSelf().is('#component_implementation_id'))) {
			$(".ui-menu-item").remove();
		}});


	var getDataComponent = function(request, response){

        var url = window.location.href;
        var contents = url.split("/");
        var host = contents[0] + "//" + contents[2];

        $.getJSON(
            host + "/api/v1/component/all?search=" + request.term,
            function (data) {
				for(var i = 0; i < data.data.length; i++) {
					data.data[i].value = data.data[i].name;
					data.data[i].label = data.data[i].name;
                    data.data[i].index = i;
				}
				globalComponentData = data.data;
                response(data.data);
            });
	};

    var getDataComponentImplementation = function(request, response){

        var url = window.location.href;
        var contents = url.split("/");
        var host = contents[0] + "//" + contents[2];

        $.getJSON(
            host + "/api/v1/component/implementation/all?search=" + request.term,
            function (data) {
				for(var i = 0; i < data.data.length; i++) {
					data.data[i].value = data.data[i].name;
					data.data[i].label = data.data[i].name;
                    data.data[i].index = i;
				}
				globalImplementationData = data.data;
                response(data.data);
            });
	};


    $( "#component_id" ).autocomplete({
      source: getDataComponent,
      minLength: 2,
      select: function( event, ui ) {
		this.value = ui.item.name;
		componentId = ui.item.uuid;
		componentName = ui.item.name;
		$(".ui-autocomplete").hide();
		$(".ui-menu-item").remove();
      },
	  focus: function(event, ui){
          var items = $(".ui-menu-item");
		  items.removeClass("ui-menu-item-hover");
		  $(items[ui.item.index]).addClass("ui-menu-item-hover");
	  }
    }).autocomplete( "instance" )._renderItem = function( ul, item ) {
		return $( "<li>" )
        .append( item.name )
        .appendTo( ul );
    };

    $( "#component_implementation_id" ).autocomplete({
      source: getDataComponentImplementation,
      minLength: 2,
      select: function( event, ui ) {
		this.value = ui.item.name;
		componentImplementationId = ui.item.uuid;
		componentImplementationName = ui.item.name;
		$(".ui-autocomplete").hide();
		$(".ui-menu-item").remove();
      },
	  focus: function(event, ui){
          var items = $(".ui-menu-item");
		  items.removeClass("ui-menu-item-hover");
		  $(items[ui.item.index]).addClass("ui-menu-item-hover");
	  }
    }).autocomplete( "instance" )._renderItem = function( ul, item ) {
		return $( "<li>" )
        .append( item.name )
        .appendTo( ul );
    };


  } );