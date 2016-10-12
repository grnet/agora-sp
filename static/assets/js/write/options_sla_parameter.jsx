
var formName = 'Options SLA Parametar Form';

var parameterId = null;
var slaId = null;
var serviceOptionsId = null;
var newParameterId = null;
var newSlaId = null;
var newServiceOptionsId = null;
var parameterName;
var newParameterName;
var slaName;
var newSlaName;
var serviceOptionsName;
var newServiceOptionsName;
var opType = "";
var globalParameterData;
var globalSlaData;
var globalOptionsData;

var optionsData = [
  {id: 1, value: 1, text: "option 1"},
  {id: 2, value: 2, text: "option 2"},
	{id: 3, value: 3, text: "option 3"}
];

var resourceObject = [
	{ tag: 'input', type: 'text', name: 'parameter_id', placeholder: 'Enter parameter name', label: 'Parameter' },
	{ tag: 'input', type: 'text', name: 'sla_id', placeholder: 'Enter SLA name', label: 'SLA' },
	{ tag: 'input', type: 'text', name: 'service_options_id', placeholder: 'Enter service option name', label: 'Service option' }
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
					    <textarea className="form-control" id={field.name} name={field.name} rows="6"></textarea>
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

	validateForm: function(e){
		this.clearValidations();
		var validationObjects = [];
		var validationMessage = ''

		// --- validation code goes here ---
		var param = $('#parameter_id').val();
		if(param == '' || param == null){
			validationMessage = "The parameter is required";
			validationObjects.push( { field: 'parameter_id', message: validationMessage } );
		}
		//if($('#name').val().length > 255){
		//	validationMessage = "Content exceeds max length of 255 characters."
		//	validationObjects.push( { field: 'name', message: validationMessage } );
		//}

		var sla = $('#sla_id').val();
		if(sla == null || sla == ""){
			validationMessage = "The SLA is required";
			validationObjects.push( { field: 'sla_id', message: validationMessage } );
		}

		var service_option = $('#service_options_id').val();
		if(service_option == null || service_option == ""){
			validationMessage = "The service options are required";
			validationObjects.push( { field: 'service_options_id', message: validationMessage } )
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

			var parameter_id =  $("#parameter_id").val();

			if(newParameterName != parameter_id){
				if(newParameterName != null || parameter_id != "")
				{
					newParameterName = null;
					newParameterId = null;
					for(var i = 0; i < globalParameterData.length; i++){
						if(parameter_id == globalParameterData[i].name){
							newParameterId = globalParameterData[i].uuid;
							newParameterName = parameter_id;
							break;
						}
					}
				}
			}

			var sla_id =  $("#sla_id").val();

			if(newSlaName != sla_id){
				if(newSlaName != null || sla_id != "")
				{
					newSlaName = null;
					newSlaId = null;
					for(var i = 0; i < globalSlaData.length; i++){
						if(sla_id == globalSlaData[i].name){
							newSlaId = globalSlaData[i].id;
							newSlaName = sla_id;
							break;
						}
					}
				}
			}

			var service_options_id =  $("#service_options_id").val();

			if(newServiceOptionsName != service_options_id){
				if(newServiceOptionsName != null || service_options_id != "")
				{
					newServiceOptionsName = null;
					newServiceOptionsId = null;
					for(var i = 0; i < globalOptionsData.length; i++){
						if(service_options_id == globalOptionsData[i].name){
							newServiceOptionsId = globalOptionsData[i].uuid;
							newServiceOptionsName = service_options_id;
							break;
						}
					}
				}
			}


			var params = {};


			var parts = window.location.href.split("/");
			var host = "https://" + parts[2];
			var url = "";

			if (this.props.source != null && this.props.source != "") {

				params["parameter_uuid"] = parameterId;
				params["new_parameter_uuid"] = newParameterId;
				params["sla_uuid"] = slaId;
				params["new_sla_uuid"] = newSlaId;
				params["service_options_uuid"] = serviceOptionsId;
				params["new_service_options_uuid"] = newServiceOptionsId;


				url = host + "/api/v1/options/SLA_paramters/edit";
				opType = "edit";
			}
			else {

				params["parameter_uuid"] = newParameterId;
				params["sla_uuid"] = newSlaId;
				params["service_options_uuid"] = newServiceOptionsId;

				url = host + "/api/v1/options/SLA_paramters/add";
				opType = "add";
			}


			this.serverRequest = $.ajax({
				url: url,
				headers: {"X-CSRFToken": $("input[name=csrfmiddlewaretoken]")[0].value },
				dataType: "json",
				crossDomain: true,
				type: "POST",
				contentType: "application/json",
				cache: false,
				data: JSON.stringify(params),
				success: function (data) {
					if (opType == "add")
						$("#modal-success-body").text("You have successfully inserted a new SLA parameter");
					else {
						parameterId = newParameterId;
						slaId = newSlaId;
						serviceOptionsId = newServiceOptionsId;
						$("#modal-success-body").text("You have successfully updated the SLA parameter");
					}
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
			data: {
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
                this.setState({data: data.data});

				$("#parameter_id").val(this.state.data.parameter.name);
				$("#sla_id").val(this.state.data.sla.name);
				$("#service_options_id").val(this.state.data.service_options.name);

				parameterId = this.state.data.parameter.uuid;
				slaId = this.state.data.sla.uuid;
				serviceOptionsId = this.state.data.service_options.uuid;
				newParameterId = parameterId;
				newSlaId = slaId;
				newServiceOptionsId = serviceOptionsId;
				parameterName = this.state.data.parameter.name;
				slaName = this.state.data.sla.name;
				serviceOptionsName = this.state.data.service_options.name;
				newParameterName = parameterName;
				newSlaName = slaName;
				newServiceOptionsName = serviceOptionsName;
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
        if (!($(event.target).parents().andSelf().is('#parameter_id'))) {
			$(".ui-menu-item").remove();
		}

		if (!($(event.target).parents().andSelf().is('#sla_id'))) {
			$(".ui-menu-item").remove();
		}

		if (!($(event.target).parents().andSelf().is('#service_option_id'))) {
			$(".ui-menu-item").remove();
		}});


	var getDataParameter = function(request, response){

        var url = window.location.href;
        var contents = url.split("/");
        var host = contents[0] + "//" + contents[2];

        $.getJSON(
            host + "/api/v1/options/parameter/all?search=" + request.term,
            function (data) {
				for(var i = 0; i < data.data.length; i++) {
					data.data[i].value = data.data[i].name;
					data.data[i].label = data.data[i].name;
                    data.data[i].index = i;
				}
				globalParameterData = data.data;
                response(data.data);
            });
	};

	var getDataSla = function(request, response){

        var url = window.location.href;
        var contents = url.split("/");
        var host = contents[0] + "//" + contents[2];


        $.getJSON(
            host + "/api/v1/options/sla/all?search=" + request.term,
            function (data) {
				for(var i = 0; i < data.data.length; i++) {
					data.data[i].value = data.data[i].name;
					data.data[i].label = data.data[i].name;
                    data.data[i].index = i;
				}
				globalSlaData = data.data;
                response(data.data);
            });
	};

    var getDataServiceOptions = function(request, response){

        var url = window.location.href;
        var contents = url.split("/");
        var host = contents[0] + "//" + contents[2];

        $.getJSON(
            host + "/api/v1/options/service_options/all?search=" + request.term,
            function (data) {
				for(var i = 0; i < data.data.length; i++) {
					data.data[i].value = data.data[i].name;
					data.data[i].label = data.data[i].name;
                    data.data[i].index = i;
				}
				globalOptionsData = data.data;
                response(data.data);
            });
	};


    $( "#parameter_id" ).autocomplete({
      source: getDataParameter,
      minLength: 2,
      select: function( event, ui ) {
		this.value = ui.item.name;
		  newParameterId = ui.item.uuid;
		  newParameterName = ui.item.name;
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

	$( "#sla_id" ).autocomplete({
      source: getDataSla,
      minLength: 2,
      select: function( event, ui ) {
		this.value = ui.item.name;
		newSlaId = ui.item.id;
		newSlaName = ui.item.name;
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

    $( "#service_options_id" ).autocomplete({
      source: getDataServiceOptions,
      minLength: 2,
      select: function( event, ui ) {
		this.value = ui.item.name;
		newServiceOptionsId = ui.item.uuid;
		newServiceOptionsName = ui.item.name;
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