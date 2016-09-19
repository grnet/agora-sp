var formName = 'Service Form'

var optionsData = [
  {id: 1, value: 1, text: "option 1"},
  {id: 2, value: 2, text: "option 2"},
	{id: 3, value: 3, text: "option 3"}
];

var resourceObject = [
	{ tag: 'input', type: 'text', name: 'name', placeholder: 'Enter name', label: 'Name', required: true },
	{ tag: 'textarea', type: 'textarea', name: 'description_external', label: 'External Description', required: true, onChange: 'textareaHTMLValidation' },
	{ tag: 'textarea', type: 'textarea', name: 'description_internal', label: 'Internal Description', required: true, onChange: 'textareaHTMLValidation' },
	{ tag: 'input', type: 'text', name: 'service_area', placeholder: 'Enter service area', label: 'Service Area', required: true },
	{ tag: 'input', type: 'text', name: 'service_type', placeholder: 'Enter service type', label: 'Service Type', required: true },
	{ tag: 'textarea', type: 'textarea', name: 'request_procedures', label: 'Request Procedures', required: true, onChange: 'textareaHTMLValidation' },
	{ tag: 'textarea', type: 'textarea', name: 'funders_for_service', label: 'Funders for Service', required: true, onChange: 'textareaHTMLValidation' },
	{ tag: 'textarea', type: 'textarea', name: 'value_to_customer', label: 'Value to customer', required: true, onChange: 'textareaHTMLValidation' },
	{ tag: 'textarea', type: 'textarea', name: 'risks', label: 'Risks', required: true, onChange: 'textareaHTMLValidation' },
	{ tag: 'textarea', type: 'textarea', name: 'competitors', label: 'Competitors', required: true, onChange: 'textareaHTMLValidation' },
	// todo: how to fill the data for the options (should be done before rendering)
	{ tag: 'select', type: 'select', name: 'service_owner', label: 'Service Owner', required: true, optionsData: optionsData },
	{ tag: 'select', type: 'select', name: 'contact_information_external', label: 'Contact Information External', required: true, optionsData: optionsData },
	{ tag: 'select', type: 'select', name: 'contact_information_internal', label: 'Contact Information Internal', required: true, optionsData: optionsData }
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
		var formElements = resourceObject.map(function(field){
			if(field.tag == 'input'){
				if(field.type == 'text'){					
					return (
						<div className="form-group">
			      	        <label htmlFor={field.name}>{field.label}</label>			      	        
			      	        <input className="form-control" id={field.name} type={field.type} name={field.name} placeholder={field.placeholder} aria-describedby={field.name + '-error'} />
			      	        <span id={field.name + '-error'} className="validation-message sr-only"></span>
			      	    </div>
					);
				}
			}
			else if(field.tag == 'textarea'){
				return(
					<div className="form-group">
					    <label htmlFor={field.name}>{field.label}</label>
					    <textarea className="form-control" id={field.name} name={field.name} rows="6" onChange={this[field.onChange]}></textarea>
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
		console.log("Clearing the validations");
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
			validationMessage = "The name is required"
			validationObjects.push( { field: 'name', message: validationMessage } );
		}

		if($('#name').val().length > 255){
			validationMessage = "Content exceeds max length of 255 characters."
			validationObjects.push( { field: 'name', message: validationMessage } );			
		}

		if($('#service_area').val().length > 255){
			validationMessage = "Content exceeds max length of 255 characters."
			validationObjects.push( { field: 'service_area', message: validationMessage } );			
		}

		if($('#service_type').val().length > 255){
			validationMessage = "Content exceeds max length of 255 characters."
			validationObjects.push( { field: 'service_type', message: validationMessage } );
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
			var formValues = JSON.stringify($("#service-form").serializeJSON());
			console.log("The form values are ->", formValues);
		}
		else{			
			console.log("The form is not valid");
		}	
	},

	getInitialState: function () {
		return {
			service: {
				name: "",
				description_internal: ""
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
                this.setState({service: data.data});
                $("#name").val(this.state.service.name);
                $("#description_internal").val(this.state.service.description_internal);
                $("#description_external").val(this.state.service.description_external);
                $("#service_area").val(this.state.service.service_area);
                $("#service_type").val(this.state.service.service_type);
                $("#request_procedures").val(this.state.service.request_procedures);
                $("#funders_for_service").val(this.state.service.funders_for_service);
                $("#value_to_customer").val(this.state.service.value_to_customer);
                $("#risks").val(this.state.service.risks);
                $("#competitors").val(this.state.service.competitors);
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