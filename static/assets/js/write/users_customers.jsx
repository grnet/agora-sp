
var formName = 'Users customers Form';

var serviceId;
var serviceName;
var opType;
var globalData;

var optionsData = [
  {id: 1, value: "Individual Researchers", text: "Individual Researchers"},
  {id: 2, value: "Community Manager", text: "Community Manager"},
  {id: 3, value: "Service Provider", text: "Service Provider"},
  {id: 4, value: "Data Project Principle Investigator (PI)", text: "Data Project Principle Investigator (PI)"}
];

var resourceObject = [
	{ tag: 'select', type: 'select', name: 'name', optionsData: optionsData, label: 'Name' },
	{ tag: 'input', type: 'text', name: 'role', placeholder: 'Enter user customer role', label: 'Role' },
	{ tag: 'input', type: 'text', name: 'service_id', placeholder: 'Enter service name', label: 'Service name' }
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
					<div className="form-group" key={i}>
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
		var name = $("#name").val();
		if(name == '' || name == null){
			validationMessage = "The name is required";
			validationObjects.push( { field: 'name', message: validationMessage } );
		}
		if(name.length > 255){
			validationMessage = "Content exceeds max length of 255 characters."
			validationObjects.push( { field: 'name', message: validationMessage } );			
		}
		var role = $("#role").val();
		if(role == '' || role == null){
			validationMessage = "The role is required";
			validationObjects.push( { field: 'role', message: validationMessage } );
		}
		if(role != null && role.length > 255){
			validationMessage = "Content exceeds max length of 255 characters."
			validationObjects.push( { field: 'role', message: validationMessage } );
		}

		var service = $("#service_id").val();
		if(service == '' || service == null){
			validationMessage = "The service is required";
			validationObjects.push( { field: 'service_id', message: validationMessage } );
		}
		if(service != null && service.length > 255){
			validationMessage = "Content exceeds max length of 255 characters."
			validationObjects.push( { field: 'service_id', message: validationMessage } );
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


			var service_id =  $("#service_id").val();

			if(serviceName != service_id){
				if(serviceName != null || service_id != "")
				{
					serviceName = null;
					serviceId = null;
					for(var i = 0; i < globalData.length; i++){
						if(service_id == globalData[i].name){
							serviceId = globalData[i].uuid;
							serviceName = service_id;
							break;
						}
					}
				}
			}

			var params = {};
			params["name"] = $("#name").val();
			params["role"] = $("#role").val();


			var parts = window.location.href.split("/");
			var host = "https://" + parts[2];
			var url = "";

			if(this.props.source != null && this.props.source != ""){
				params["uuid"] = parts[parts.length - 1];
				url = host + "/api/v1/services/" + serviceId + "/user_customer/edit";
				opType = "edit";
			}
			else {
				url = host + "/api/v1/services/" + serviceId + "/user_customer/add";
				opType = "add";
			}

			this.serverRequest = $.ajax({
				url: url,
				dataType: "json",
				crossDomain: true,
				type: "POST",
				contentType:"application/json",
				cache: false,
				data: JSON.stringify(params),
				success: function (data) {
					if(opType == "add")
						$("#modal-success-body").text("You have successfully inserted a new user customer");
					else
						$("#modal-success-body").text("You have successfully updated the user customer");
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
			user_customer: {
				name: "",
				role: "",
				service: {
					name: "",
					uuid: ""
				}
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
                this.setState({user_customer: data.data});
                $("#name").val(this.state.user_customer.name);
                $("#role").val(this.state.user_customer.role);
                $("#service_id").val(this.state.user_customer.service.name);
				serviceId = this.state.user_customer.service.uuid;
				serviceName = this.state.user_customer.service.name;
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
        if (!($(event.target).parents().andSelf().is('#service_id'))) {
			$(".ui-menu-item").remove();
		}});


	var getDataService = function(request, response){

        var url = window.location.href;
        var contents = url.split("/");
        var host = contents[0] + "//" + contents[2];

        $.getJSON(
            host + "/api/v1/services/all?search=" + request.term,
            function (data) {
				for(var i = 0; i < data.data.length; i++) {
					data.data[i].value = data.data[i].name;
					data.data[i].label = data.data[i].name;
                    data.data[i].index = i;
				}
				globalData = data.data;
                response(data.data);
            });
	};




    $( "#service_id" ).autocomplete({
      source: getDataService,
      minLength: 2,
      select: function( event, ui ) {
		this.value = ui.item.name;
		serviceId = ui.item.uuid;
		serviceName = ui.item.name;
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