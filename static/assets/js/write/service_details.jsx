
var formName = 'Service Details Form'
var optionsData = [
  {id: 1, value: 1, text: "option 1"},
  {id: 2, value: 2, text: "option 2"},
	{id: 3, value: 3, text: "option 3"}
];

var booleanData = [
  {id: 0, value: 0, text: "no"},
  {id: 1, value: 1, text: "yes"}  
];

var statusData = [
  {id: 0, value: 0, text: "Inactive"},
  {id: 1, value: 1, text: "Active"}
];

var resourceObject = [
	{ tag: 'input', type: 'text', name: 'version', placeholder: 'Enter version', label: 'Version' },	
	{ tag: 'select', type: 'select', name: 'status', label: 'Enter status', required: true, optionsData: statusData },
	{ tag: 'textarea', type: 'textarea', name: 'features_current', label: 'Features Current', onChange: 'textareaHTMLValidation' },
	{ tag: 'textarea', type: 'textarea', name: 'features_future', label: 'Features Future', onChange: 'textareaHTMLValidation' },
	// todo: how to fill the data for the options (should be done before rendering)
	{ tag: 'select', type: 'select', name: 'usage_policy_has', label: 'Has Usage Policy', required: true, optionsData: booleanData },
	{ tag: 'input', type: 'text', name: 'usage_policy_url', placeholder: 'Enter Usage Policy URL', label: 'Usage Policy URL', onChange: 'urlContentChanged' },

	{ tag: 'select', type: 'select', name: 'usage_documentation_has', label: 'Has Usage Documentation', required: true, optionsData: booleanData },
	{ tag: 'input', type: 'text', name: 'usage_documentation_url', placeholder: 'Enter Usage Documentation URL', label: 'Usage Documentation URL', onChange: 'urlContentChanged' },

	{ tag: 'select', type: 'select', name: 'operations_documentation_has', label: 'Has Operation Documentation', required: true, optionsData: booleanData },
	{ tag: 'input', type: 'text', name: 'operations_documentation_url', placeholder: 'Enter Operation Documentation URL', label: 'Operation Documentation URL', onChange: 'urlContentChanged' },

	{ tag: 'select', type: 'select', name: 'monitoring_has', label: 'Has Monitoring', required: true, optionsData: booleanData },
	{ tag: 'input', type: 'text', name: 'monitoring_url', placeholder: 'Enter Monitoring URL', label: 'Monitoring URL', onChange: 'urlContentChanged' },

	{ tag: 'select', type: 'select', name: 'accounting_has', label: 'Has Accounting', required: true, optionsData: booleanData },
	{ tag: 'input', type: 'text', name: 'accounting_url', placeholder: 'Enter Accounting URL', label: 'Accounting URL', onChange: 'urlContentChanged' },

	{ tag: 'select', type: 'select', name: 'business_continuity_plan_has', label: 'Has Business Continuity Plan', required: true, optionsData: booleanData },
	{ tag: 'input', type: 'text', name: 'business_continuity_plan_url', placeholder: 'Enter Business Continuity Plan URL', label: 'Business Continuity Plan URL', onChange: 'urlContentChanged' },

	{ tag: 'select', type: 'select', name: 'disaster_recovery_plan_has', label: 'Has Disaster Recovery Plan', required: true, optionsData: booleanData },
	{ tag: 'input', type: 'text', name: 'disaster_recovery_plan_url', placeholder: 'Enter Disaster Recovery Plan URL', label: 'Disaster Recovery Plan URL', onChange: 'urlContentChanged' },

	{ tag: 'select', type: 'select', name: 'decommissioning_procedure_has', label: 'Has Decommissioning Procedure', required: true, optionsData: booleanData },
	{ tag: 'input', type: 'text', name: 'decommissioning_procedure_url', placeholder: 'Enter Decommissioning Procedure URL', label: 'Decommissioning Procedure URL', onChange: 'urlContentChanged' },

	{ tag: 'input', type: 'text', name: 'cost_to_run', placeholder: 'Enter cost to run', label: 'Cost to run' },
	{ tag: 'input', type: 'text', name: 'cost_to_build', placeholder: 'Enter cost to build', label: 'Cost to build' },
	{ tag: 'textarea', type: 'textarea', name: 'use_cases', label: 'Use Cases', onChange: 'textareaHTMLValidation' },
	{ tag: 'select', type: 'select', name: 'is_in_catalog', label: 'Is in catalog', required: true, optionsData: booleanData },
	{ tag: 'select', type: 'select', name: 'is_service_id', label: 'Service', required: true, optionsData: optionsData }

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
			      	        <input className="form-control" id={field.name} type={field.type} name={field.name} placeholder={field.placeholder} onChange={this[field.onChange]} aria-describedby={field.name + '-error'} />
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
		$('body').find('.has-error').removeClass('has-error');
		$('body').find('.validation-message').addClass('sr-only');
	},

	urlContentChanged: function(e){
		var value = $(e.target).val();
		var nameParts = e.target.name.split("_");
		nameParts[nameParts.length - 1] = "has";
		var optionsField = nameParts.join('_');

		if(value != ''){
			$('#' + optionsField).val(1);
		}
		else{
			$('#' + optionsField).val(0);
		}
	},

	textareaHTMLValidation: function(e){
		var div = document.createElement('div');
		div.innerHTML = $(e.target).val();
		if($(div).find('script').length > 0 || $(div).find('link').length){
			div = null;
			this.markInvalid($(e.target).attr('name'), 'This HTML content must not have script or css tags');
		}
		else{
			console.log("all is good now");
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
			validationMessage = "The name is required"
			validationObjects.push( { field: 'version', message: validationMessage } );
		}

		if($('#version').val().length > 255){
			validationMessage = "Content exceeds max length of 255 characters."
			validationObjects.push( { field: 'version', message: validationMessage } );			
		}

		if($('#cost_to_run').val().length > 255){
			validationMessage = "Content exceeds max length of 255 characters."
			validationObjects.push( { field: 'cost_to_run', message: validationMessage } );			
		}

		if($('#cost_to_build').val().length > 255){
			validationMessage = "Content exceeds max length of 255 characters."
			validationObjects.push( { field: 'cost_to_build', message: validationMessage } );
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
  document.getElementById('write-content')
);