var formName = 'Service Form'

var optionsData = [
  {id: 1, value: 1, text: "option 1"},
  {id: 2, value: 2, text: "option 2"},
	{id: 3, value: 3, text: "option 3"}
];

var resourceObject = [
	{ tag: 'input', type: 'text', name: 'name', placeholder: 'Enter name', label: 'Name', required: true },
	{ tag: 'textarea', type: 'textarea', name: 'description_external', label: 'External Description', required: true },
	{ tag: 'textarea', type: 'textarea', name: 'description_internal', label: 'Internal Description', required: true },
	{ tag: 'input', type: 'text', name: 'service_area', placeholder: 'Enter service area', label: 'Service Area', required: true },
	{ tag: 'input', type: 'text', name: 'service_type', placeholder: 'Enter service type', label: 'Service Type', required: true },
	{ tag: 'textarea', type: 'textarea', name: 'request_procedures', label: 'Request Procedures', required: true },
	{ tag: 'textarea', type: 'textarea', name: 'funders_for_service', label: 'Funders for Service', required: true },
	{ tag: 'textarea', type: 'textarea', name: 'value_to_customer', label: 'Value to customer', required: true },
	{ tag: 'textarea', type: 'textarea', name: 'risks', label: 'Risks', required: true },
	{ tag: 'textarea', type: 'textarea', name: 'competitors', label: 'Competitors', required: true },

	{ tag: 'select', type: 'select', name: 'service_owner', label: 'Service Owner', required: true, optionsData: optionsData },
	{ tag: 'select', type: 'select', name: 'contact_information', label: 'Contact Information', required: true, optionsData: optionsData }
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
			      	        <span id={field.name + '-error'} className="validation-message" className="sr-only">There was an error</span>
			      	    </div>
					);
				}
			}
			else if(field.tag == 'textarea'){
				return(
					<div className="form-group">
					    <label htmlFor={field.name}>{field.label}</label>
					    <textarea className="form-control" id={field.name} name={field.name} rows="6"></textarea>
					</div>
				);				
			}
			else if(field.tag == 'select'){
				return(
					<div className="form-group">
					    <label htmlFor={field.name}>{field.label}</label>
					    <OptionsComponent options={field.optionsData} selectName={field.name}></OptionsComponent>
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

	validateForm: function(e){
		// method that marks what is not valid and navigates to the top of the form
		// separate implementation for each view
		if($('#name').val() == ''){
			var validationMessage = "The name is required"
			this.markInvalid('name', validationMessage);
			return false;
		}
		return true;
	},

	handleSubmit: function(e) {
		// some validation
		// ajax url call + redirect
		e.preventDefault();

		if(this.validateForm()){
			var formValues = JSON.stringify($("#service-form").serializeJSON());
			console.log("The form values are ->", formValues);
		}
		else{
			console.log("The form is not valid");
		}		
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
  <FormWrapper resourceObject={resourceObject} formName={formName}/>,
  document.getElementById('content')
);