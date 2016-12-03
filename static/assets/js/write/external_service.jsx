var formName = 'External Service Form';

var opType;

var optionsData = [
  {id: 1, value: 1, text: "option 1"},
  {id: 2, value: 2, text: "option 2"},
	{id: 3, value: 3, text: "option 3"}
];

var resourceObject = [
	{ tag: 'input', type: 'text', name: 'name', placeholder: 'Enter name', label: 'Name' },
	{ tag: 'textarea', type: 'textarea', name: 'description', placeholder: 'Enter description', label: 'Description', onChange: 'textareaHTMLValidation' },
	{ tag: 'button', type: 'button', name: 'edit-description', label: 'Edit', value: "Edit"},
	{ tag: 'input', type: 'text', name: 'service', label: 'Service', placeholder: "Enter service" },
	{ tag: 'input', type: 'text', name: 'details', placeholder: 'Enter details', label: 'Details' }
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
					<div className="form-group" key={i}>
					    <label htmlFor={field.name}>{field.label}</label>
					    <OptionsComponent options={field.optionsData} selectName={field.name}></OptionsComponent>
					    <span id={field.name + '-error'} className="validation-message sr-only"></span>
					</div>
				);				
			}
			else if(field.tag == 'button'){
				return (
					<div className="form-group" key={i}>
			      	        <button value={field.value} className="btn btn-purple" id={"btn-" + field.name}>{field.value}</button>

			      	    </div>
				)
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
		if($('#name').val() == ''){
			validationMessage = "The name is required";
			validationObjects.push( { field: 'name', message: validationMessage } );
		}

		if($('#name').val().length > 255){
			validationMessage = "Content exceeds max length of 255 characters.";
			validationObjects.push( { field: 'name', message: validationMessage } );			
		}

		if($('#details').val().length > 255){
			validationMessage = "Content exceeds max length of 255 characters.";
			validationObjects.push( { field: 'details', message: validationMessage } );			
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
			this.clearValidations();
			//var formValues = JSON.stringify($("#service-form").serializeJSON());
			//console.log("The form values are ->", formValues);

			var params = {};
			params["name"] = $("#name").val();
			params["description"] = $("#description").val();
			params["service"] = $("#service").val();
			params["details"] = $("#details").val();


			var parts = window.location.href.split("/");
			var host = "https://" + parts[2];
			var url = "";

			if(this.props.source != null && this.props.source != ""){
				params["uuid"] = parts[parts.length - 1];
				url = host + "/api/v1/services/external_service/edit";
				opType = "edit";
			}
			else {
				url = host + "/api/v1/services/external_service/add";
				opType = "add";
			}

			this.serverRequest = $.ajax({
				url: url,
				headers: {
					"X-CSRFToken": $("input[name=csrfmiddlewaretoken]")[0].value,
					"AUTH_TOKEN": localStorage.apiToken,
					"EMAIL": localStorage.apiEmail
				},
				dataType: "json",
				crossDomain: true,
				type: "POST",
				contentType:"application/json",
				cache: false,
				data: JSON.stringify(params),
				success: function (data) {
					if(opType == "add")
						$("#modal-success-body").text("You have successfully inserted a new external service");
					else
						$("#modal-success-body").text("You have successfully updated the external service");
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
			external_service: {
				name: "",
				description: "",
				details: ""
			}
		}
	},

    componentDidMount: function () {

        if(this.props.source == null || this.props.source == "")
            return;

        jQuery.support.cors = true;
        this.serverRequest = $.ajax({
            url: this.props.source,
			headers: {
				"X-CSRFToken": $("input[name=csrfmiddlewaretoken]")[0].value,
				"AUTH_TOKEN": localStorage.apiToken,
				"EMAIL": localStorage.apiEmail
			},
            dataType: "json",
            crossDomain: true,
            type: "GET",
            cache: false,
            success: function (data) {
                this.setState({external_service: data.data});
                $("#name").val(this.state.external_service.name);
                $("#description").val(this.state.external_service.description);
                $("#service").val(this.state.external_service.service);
                $("#details").val(this.state.external_service.details);
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

$(function(){

	$("#btn-edit-description").click(function(e){
		e.preventDefault();
		tinymce.init({
			selector:'#rich-edit',
			height: 250
		});
		tinymce.get('rich-edit').setContent($("#description").val());
		$("#modal-rich-html").modal('show');
	});

	$("#confirm-edit").click(function () {
		$("#description").val(tinymce.get('rich-edit').getContent());
	});

});