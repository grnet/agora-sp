
var formName = 'Service Details Form';

var opType;
var serviceId;
var serviceDetailsId;
var serviceVersion;
var globalData;

var fieldEdited = null;

var optionsData = [
  {id: 1, value: -1, text: "Select service"}
];

var booleanData = [
  {id: 0, value: "false", text: "no"},
  {id: 1, value: "true", text: "yes"}
];

var statusData = [
  {id: 0, value: 0, text: "Inactive"},
  {id: 1, value: 1, text: "Active"}
];

var resourceObject = [
	{ tag: 'input', type: 'text', name: 'version', placeholder: 'Enter version', label: 'Version' },	
	{ tag: 'input', type: 'text', name: 'status', label: 'Enter status', required: true, placeholder: "Enter status" },
	{ tag: 'textarea', type: 'textarea', name: 'features_current', placeholder: "Enter current features", label: 'Features Current', onChange: 'textareaHTMLValidation' },
	{ tag: 'button', type: 'button', name: 'edit-features-current', label: 'Edit', value: "Edit"},
	{ tag: 'textarea', type: 'textarea', name: 'features_future', placeholder: "Enter future features", label: 'Features Future', onChange: 'textareaHTMLValidation' },
	{ tag: 'button', type: 'button', name: 'edit-features-future', label: 'Edit', value: "Edit"},
	// todo: how to fill the data for the options (should be done before rendering)
	{ tag: 'select', type: 'select', name: 'terms_of_use_has', label: 'Has Usage Policy', required: true, optionsData: booleanData },
	{ tag: 'input', type: 'text', name: 'terms_of_use_url', placeholder: 'Enter Usage Policy URL', label: 'Usage Policy URL', onChange: 'urlContentChanged' },

	{ tag: 'select', type: 'select', name: 'privacy_policy_has', label: 'Has Privacy Policy', required: true, optionsData: booleanData },
	{ tag: 'input', type: 'text', name: 'privacy_policy_url', placeholder: 'Enter Privacy Policy URL', label: 'Privacy Policy URL', onChange: 'urlContentChanged' },

	{ tag: 'select', type: 'select', name: 'user_documentation_has', label: 'Has Usage Documentation', required: true, optionsData: booleanData },
	{ tag: 'input', type: 'text', name: 'user_documentation_url', placeholder: 'Enter Usage Documentation URL', label: 'Usage Documentation URL', onChange: 'urlContentChanged' },

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
	{ tag: 'textarea', type: 'textarea', name: 'use_cases', placeholder: "Enter use cases", label: 'Use Cases', onChange: 'textareaHTMLValidation' },
	{ tag: 'button', type: 'button', name: 'edit-use-cases', label: 'Edit', value: "Edit"},
	{ tag: 'select', type: 'select', name: 'is_in_catalog', label: 'Is in catalog', required: true, optionsData: booleanData },
	{ tag: 'select', type: 'text', name: 'service_id', label: 'Service', required: true, placeholder: "Enter service name", optionsData: optionsData }

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

var parameter = getParameterByName("serviceId", window.location);
if(parameter != null) {
	serviceId = parameter;
	jQuery.support.cors = true;
        $.ajax({
            url: $("#host")[0].value + "/api/v1/portfolio/services/" + serviceId,
			headers: {
				"X-CSRFToken": $("input[name=csrfmiddlewaretoken]")[0].value,
				"AUTHTOKEN": localStorage.apiToken,
				"EMAIL": localStorage.apiEmail
			},
            dataType: "json",
            crossDomain: true,
            type: "GET",
            cache: false,
            success: function (response) {

				var name = response.data.name;

				var service = $("#service_id");
				var optionsCount = $("#service_id>option").length;
				if(optionsCount <= 1){
					var option = $('<option></option>').attr("value", name)
							.text(name);
						service.append(option);
				}
				service.val(name).change();
            },
            error: function (xhr, status, err) {
            }
        });
}

var FormWrapper = React.createClass({

	generateFormElements: function(resourceObject){
		var formElements = resourceObject.map(function(field, i){
			if(field.tag == 'input'){
				if(field.type == 'text'){					
					return (
						<div className="form-group" key={i}>
			      	        <label htmlFor={field.name}>{field.label}</label>
			      	        <input className="form-control" id={field.name} type={field.type} name={field.name} placeholder={field.placeholder} onChange={this[field.onChange]} aria-describedby={field.name + '-error'} />
			      	        <span id={field.name + '-error'} className="validation-message sr-only"></span>
			      	    </div>
					);
				}
			}
			else if(field.tag == 'textarea'){
				return(
					<div className="form-group" key={i}>
					    <label htmlFor={field.name}>{field.label}</label>
					    <textarea className="form-control" id={field.name} placeholder={field.placeholder} name={field.name} rows="6" onChange={this[field.onChange]}></textarea>
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

	urlContentChanged: function(e){
		//var value = $(e.target).val();
		//var nameParts = e.target.name.split("_");
		//nameParts[nameParts.length - 1] = "has";
		//var optionsField = nameParts.join('_');
        //
		//if(value != ''){
		//	$('#' + optionsField).val("yes");
		//}
		//else{
		//	$('#' + optionsField).val("no");
		//}
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
		var version = $("#version").val();
		if(version == '' || version == null){
			validationMessage = "The version is required";
			validationObjects.push( { field: 'version', message: validationMessage } );
		}

		var service = $("#service_id").val();
		if(service == '' || service == null || service == -1){
			validationMessage = "The service is required";
			validationObjects.push( { field: 'service_id', message: validationMessage } );
		}

		if(version != null && version.length > 255){
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

		var privacy_policy_has = $("#privacy_policy_has").val();
		var privacy_policy_url = $("#privacy_policy_url").val();

		if(privacy_policy_has == "false" && privacy_policy_url != null && privacy_policy_url != ""){
			validationMessage = "Privacy policy URL cannot be filled without checking the select box";
			validationObjects.push( { field: 'privacy_policy_url', message: validationMessage } );
		}

		if(privacy_policy_has == "true" && (privacy_policy_url == null || privacy_policy_url == "")){
			validationMessage = "Privacy policy URL cannot be empty with the select box checked";
			validationObjects.push( { field: 'privacy_policy_url', message: validationMessage } );
		}

		var terms_of_use_has = $("#terms_of_use_has").val();
		var terms_of_use_url = $("#terms_of_use_url").val();

		if(terms_of_use_has == "false" && terms_of_use_url != null && terms_of_use_url != ""){
			validationMessage = "Usage policy URL cannot be filled without checking the select box";
			validationObjects.push( { field: 'terms_of_use_url', message: validationMessage } );
		}

		if(terms_of_use_has == "true" && (terms_of_use_url == null || terms_of_use_url == "")){
			validationMessage = "Usage policy URL cannot be empty with the select box checked";
			validationObjects.push( { field: 'terms_of_use_url', message: validationMessage } );
		}

		var user_documentation_has = $("#user_documentation_has").val();
		var user_documentation_url = $("#user_documentation_url").val();

		if(user_documentation_has == "false" && user_documentation_url != null && user_documentation_url != ""){
			validationMessage = "User documentation URL cannot be filled without checking the select box";
			validationObjects.push( { field: 'user_documentation_url', message: validationMessage } );
		}

		if(user_documentation_has == "true" && (user_documentation_url == null || user_documentation_url == "")){
			validationMessage = "User documentation URL cannot be empty with the select box checked";
			validationObjects.push( { field: 'user_documentation_url', message: validationMessage } );
		}

		var operations_documentation_has = $("#operations_documentation_has").val();
		var operations_documentation_url = $("#operations_documentation_url").val();

		if(operations_documentation_has == "false" && operations_documentation_url != null && operations_documentation_url != ""){
			validationMessage = "Operations documentation URL cannot be filled without checking the select box";
			validationObjects.push( { field: 'operations_documentation_url', message: validationMessage } );
		}

		if(operations_documentation_has == "true" && (operations_documentation_url == null || operations_documentation_url == "")){
			validationMessage = "Operations documentation URL cannot be empty with the select box checked";
			validationObjects.push( { field: 'operations_documentation_url', message: validationMessage } );
		}

		var monitoring_has = $("#monitoring_has").val();
		var monitoring_url = $("#monitoring_url").val();

		if(monitoring_has == "false" && monitoring_url != null && monitoring_url != ""){
			validationMessage = "Monitoring URL cannot be filled without checking the select box";
			validationObjects.push( { field: 'monitoring_url', message: validationMessage } );
		}

		if(monitoring_has == "true" && (monitoring_url == null || monitoring_url == "")){
			validationMessage = "Monitoring URL cannot be empty with the select box checked";
			validationObjects.push( { field: 'monitoring_url', message: validationMessage } );
		}

		var accounting_has = $("#accounting_has").val();
		var accounting_url = $("#accounting_url").val();

		if(accounting_has == "false" && accounting_url != null && accounting_url != ""){
			validationMessage = "Accounting URL cannot be filled without checking the select box";
			validationObjects.push( { field: 'accounting_url', message: validationMessage } );
		}

		if(accounting_has == "true" && (accounting_url == null || accounting_url == "")){
			validationMessage = "Accounting URL cannot be empty with the select box checked";
			validationObjects.push( { field: 'accounting_url', message: validationMessage } );
		}

		var business_continuity_plan_has = $("#business_continuity_plan_has").val();
		var business_continuity_plan_url = $("#business_continuity_plan_url").val();

		if(business_continuity_plan_has == "false" && business_continuity_plan_url != null && business_continuity_plan_url != ""){
			validationMessage = "Business continuity plan URL cannot be filled without checking the select box";
			validationObjects.push( { field: 'business_continuity_plan_url', message: validationMessage } );
		}

		if(business_continuity_plan_has == "true" && (business_continuity_plan_url == null || business_continuity_plan_url == "")){
			validationMessage = "Business continuity plan URL cannot be empty with the select box checked";
			validationObjects.push( { field: 'business_continuity_plan_url', message: validationMessage } );
		}

		var disaster_recovery_plan_has = $("#disaster_recovery_plan_has").val();
		var disaster_recovery_plan_url = $("#disaster_recovery_plan_url").val();

		if(disaster_recovery_plan_has == "false" && disaster_recovery_plan_url != null && disaster_recovery_plan_url != ""){
			validationMessage = "Disaster recovery plan URL cannot be filled without checking the select box";
			validationObjects.push( { field: 'disaster_recovery_plan_url', message: validationMessage } );
		}

		if(disaster_recovery_plan_has == "true" && (disaster_recovery_plan_url == null || disaster_recovery_plan_url == "")){
			validationMessage = "Disaster recovery plan URL cannot be empty with the select box checked";
			validationObjects.push( { field: 'disaster_recovery_plan_url', message: validationMessage } );
		}

		var decommissioning_procedure_has = $("#decommissioning_procedure_has").val();
		var decommissioning_procedure_url = $("#decommissioning_procedure_url").val();

		if(decommissioning_procedure_has == "false" && decommissioning_procedure_url != null && decommissioning_procedure_url != ""){
			validationMessage = "Decommissioning procedure URL cannot be filled without checking the select box";
			validationObjects.push( { field: 'decommissioning_procedure_url', message: validationMessage } );
		}

		if(decommissioning_procedure_has == "true" && (decommissioning_procedure_url == null || decommissioning_procedure_url == "")){
			validationMessage = "Decommissioning procedure URL cannot be empty with the select box checked";
			validationObjects.push( { field: 'decommissioning_procedure_url', message: validationMessage } );
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


			var service_id =  $("#service_id").val();

			if(service_id != "")
			{
				serviceId = null;
				for(var i = 0; i < globalData.length; i++){
					if(service_id == globalData[i].name){
						serviceId = globalData[i].uuid;
						break;
					}
				}
			}


			var params = {};
			params["version"] = $("#version").val();
			params["status"] = $("#status").val();
			params["features_current"] = $("#features_current").val();
			params["features_future"] = $("#features_future").val();
			params["terms_of_use_has"] = $("#terms_of_use_has").val();
			params["terms_of_use_url"] = $("#terms_of_use_url").val();
			params["privacy_policy_has"] = $("#privacy_policy_has").val();
			params["privacy_policy_url"] = $("#privacy_policy_url").val();
			params["user_documentation_has"] = $("#user_documentation_has").val();
			params["user_documentation_url"] = $("#user_documentation_url").val();
			params["operations_documentation_has"] = $("#operations_documentation_has").val();
			params["operations_documentation_url"] = $("#operations_documentation_url").val();
			params["monitoring_has"] = $("#monitoring_has").val();
			params["monitoring_url"] = $("#monitoring_url").val();
			params["accounting_has"] = $("#accounting_has").val();
			params["accounting_url"] = $("#accounting_url").val();
			params["business_continuity_plan_has"] = $("#business_continuity_plan_has").val();
			params["business_continuity_plan_url"] = $("#business_continuity_plan_url").val();
			params["disaster_recovery_plan_has"] = $("#disaster_recovery_plan_has").val();
			params["disaster_recovery_plan_url"] = $("#disaster_recovery_plan_url").val();
			params["decommissioning_procedure_has"] = $("#decommissioning_procedure_has").val();
			params["decommissioning_procedure_url"] = $("#decommissioning_procedure_url").val();
			params["cost_to_run"] = $("#cost_to_run").val();
			params["cost_to_build"] = $("#cost_to_build").val();
			params["use_cases"] = $("#use_cases").val();
			params["service_id"] = serviceId;

			if($("#is_in_catalog").val() == true)
				params["is_in_catalogue"] = true;
			else
				params["is_in_catalogue"] = false;



			var parts = window.location.href.split("/");
			var host = "https://" + parts[2];
			var url = "";

			if(this.props.source != null && this.props.source != ""){
				params["uuid"] = serviceDetailsId;
				url = host + "/api/v1/services/" + serviceId + "/service_details/edit";
				opType = "edit";
			}
			else {
				url = host + "/api/v1/services/" + serviceId + "/service_details/add";
				opType = "add";
			}

			this.serverRequest = $.ajax({
				url: url,
				headers: {
					"X-CSRFToken": $("input[name=csrfmiddlewaretoken]")[0].value,
					"AUTHTOKEN": localStorage.apiToken,
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
						$("#modal-success-body").text("You have successfully inserted a new service version");
					else
						$("#modal-success-body").text("You have successfully updated the service version");
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

	render: function(){		
		var formElements = this.generateFormElements(this.props.resourceObject);
		return(
			<div className="widget">
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

var ComponentsTable = React.createClass({


	getInitialState: function () {
		return {
			components: []
		}
	},

	render: function() {

		var array = [];
		for(var i = 0; i < this.state.count; i++)
			array.push(i);

		return (
			<div className="row">
				<div className="col-xs-12">
					<div className="well with-header  with-footer">
						<div className="form-group">
			      	        <button value="Add user customer" id="add-component-detail" className="btn btn-purple">Match related component implementation detail</button>
			      	    </div>
						<table className="table table-hover">
							<thead className="bordered-darkorange">
								<tr>
									<th>
										Version
									</th>
									<th>
										Configuration parameters
									</th>
									<th>

									</th>
								</tr>
							</thead>
							<tbody>

							{this.props.components.map(function (component) {
								return (
									<tr key={component.uuid}>
										<td>{component.version}</td>
										<td>{component.configuration_parameters}</td>
										<td><a href={"/ui/component/implementation_detail/" + component.uuid}>Edit</a></td>
									</tr>
								)
							})}

							</tbody>

						</table>

						<div className="col-xs-hidden col-sm-6"></div>
							<div className="col-xs-12 col-sm-6">
								<div className="dataTables_paginate paging_bootstrap" id="simpledatatable_paginate">

								</div>
							</div>

					</div>

				</div>

			</div>
		);
	}
});

var ServiceOptionsTable = React.createClass({


	getInitialState: function () {
		return {
			options: []
		}
	},

	render: function() {

		var array = [];
		for(var i = 0; i < this.state.count; i++)
			array.push(i);

		return (
			<div className="row">
				<div className="col-xs-12">
					<div className="well with-header  with-footer">
						<div className="form-group">
			      	        <button value="Add user customer" id="add-options" className="btn btn-purple">Match related service options</button>
			      	    </div>
						<table className="table table-hover">
							<thead className="bordered-darkorange">
								<tr>
									<th>
										Name
									</th>
									<th>
										Description
									</th>
									<th>
										Pricing
									</th>
									<th>

									</th>
								</tr>
							</thead>
							<tbody>

							{this.props.options.map(function (option) {
								return (
									<tr key={option.uuid}>
										<td>{option.name}</td>
										<td>{option.description}</td>
										<td>{option.pricing}</td>
										<td><a href={"/ui/options/service_options/" + option.uuid}>Edit</a></td>
									</tr>
								)
							})}

							</tbody>

						</table>

						<div className="col-xs-hidden col-sm-6"></div>
							<div className="col-xs-12 col-sm-6">
								<div className="dataTables_paginate paging_bootstrap" id="simpledatatable_paginate">

								</div>
							</div>

					</div>

				</div>

			</div>
		);
	}
});

var Tabs = React.createClass({

	getInitialState: function () {
		return {
			service_details: {
				version: ""
			},
			components: [],
			options: []
		}
	},

    componentDidMount: function () {


		jQuery.support.cors = true;
		var url = window.location.href;
        var contents = url.split("/");
        var host = contents[0] + "//" + contents[2];

		$.getJSON(
            host + "/api/v1/services/all",
            function (data) {
				var service_id = $("#service_id");
				var current = service_id.val();

				if(current != -1){
					$("#service_id option[value='" + current + "']").remove();
				}
				for(var i = 0; i < data.data.length; i++) {
					var option = $('<option></option>').attr("value", data.data[i].name).text(data.data[i].name);
					service_id.append(option);

				}
				if(current != -1)
					service_id.val(current).change();

				globalData = data.data;

            });


        if(this.props.source == null || this.props.source == "")
            return;

        this.serverRequest = $.ajax({
            url: this.props.source,
			headers: {
				"X-CSRFToken": $("input[name=csrfmiddlewaretoken]")[0].value,
				"AUTHTOKEN": localStorage.apiToken,
				"EMAIL": localStorage.apiEmail
			},
            dataType: "json",
            crossDomain: true,
            type: "GET",
            cache: false,
            success: function (data) {
                this.setState({service_details: data.data});
                $("#version").val(this.state.service_details.version);
                $("#status").val(this.state.service_details.service_status);
                $("#features_current").val(this.state.service_details.features_current);
                $("#features_future").val(this.state.service_details.features_future);
                $("#terms_of_use_has").val(this.state.service_details.terms_of_use_has.toString());
                $("#terms_of_use_url").val(this.state.service_details.usage_policy_link.related.href);
                $("#privacy_policy_has").val(this.state.service_details.privacy_policy_has.toString());
                $("#privacy_policy_url").val(this.state.service_details.privacy_policy_link.related.href);
                $("#user_documentation_has").val(this.state.service_details.user_documentation_has.toString());
                $("#user_documentation_url").val(this.state.service_details.user_documentation_link.related.href);
                $("#operations_documentation_has").val(this.state.service_details.operations_documentation_has.toString());
                $("#operations_documentation_url").val(this.state.service_details.operations_documentation_link.related.href);
                $("#monitoring_has").val(this.state.service_details.monitoring_has.toString());
                $("#monitoring_url").val(this.state.service_details.monitoring_link.related.href);
                $("#accounting_has").val(this.state.service_details.accounting_has.toString());
                $("#accounting_url").val(this.state.service_details.accounting_link.related.href);
                $("#business_continuity_plan_has").val(this.state.service_details.business_continuity_plan_has.toString());
                $("#business_continuity_plan_url").val(this.state.service_details.business_continuity_plan_link.related.href);
                $("#disaster_recovery_plan_has").val(this.state.service_details.disaster_recovery_plan_has.toString());
                $("#disaster_recovery_plan_url").val(this.state.service_details.disaster_recovery_plan_link.related.href);
                $("#decommissioning_procedure_has").val(this.state.service_details.decommissioning_procedure_has.toString());
                $("#decommissioning_procedure_url").val(this.state.service_details.decommissioning_procedure_link.related.href);
                $("#cost_to_run").val(this.state.service_details.cost_to_run);
                $("#cost_to_build").val(this.state.service_details.cost_to_build);
                $("#use_cases").val(this.state.service_details.use_cases);
                $("#is_in_catalog").val(this.state.service_details.in_catalogue.toString());

				var service = $("#service_id");
				var optionsCount = $("#service_id>option").length;
				if(optionsCount <= 1){
					var option = $('<option></option>').attr("value", this.state.service_details.service.name)
							.text(this.state.service_details.service.name);
						service.append(option);
				}
				service.val(this.state.service_details.service.name).change();
				serviceId = this.state.service_details.service.uuid;
				serviceDetailsId = this.state.service_details.uuid;
				serviceVersion = this.state.service_details.version;

				var self = this;
				$.ajax({
					url: host + "/api/v1/component/service_details_components/" + serviceDetailsId,
					headers: {
						"X-CSRFToken": $("input[name=csrfmiddlewaretoken]")[0].value,
						"AUTHTOKEN": localStorage.apiToken,
						"EMAIL": localStorage.apiEmail
					},
					dataType: "json",
					crossDomain: true,
					type: "GET",
					cache: false,
					success: function (data) {
						self.setState({components: data.data});
					}
				});

				$.ajax({
					url: host + "/api/v1/options/options_for_service_details/" + serviceDetailsId,
					headers: {
						"X-CSRFToken": $("input[name=csrfmiddlewaretoken]")[0].value,
						"AUTHTOKEN": localStorage.apiToken,
						"EMAIL": localStorage.apiEmail
					},
					dataType: "json",
					crossDomain: true,
					type: "GET",
					cache: false,
					success: function (data) {
						self.setState({options: data.data});
					}
				});


            }.bind(this),
            error: function (xhr, status, err) {
                console.log(this.props.source, status, err.toString());
            }.bind(this)
        });
    },

    componentWillUnmount: function () {
        this.serverRequest.abort();
    },

	render: function() {
		return (
			<div className="row">
				<div>
					<div className="widget flat radius-bordered">
						<div className="widget-header bg-themeprimary">
							<span className="widget-caption">Service Version</span>
						</div>

						<div className="widget-body">
							<div className="widget-main ">
								<div className="tabbable">
									<ul className="nav nav-tabs tabs-flat" id="myTab11">
										<li className="active">
											<a data-toggle="tab" href="#home11">
												Service Version
											</a>
										</li>
										<li>
											<a data-toggle="tab" href="#profile11">
												Components
											</a>
										</li>
										<li>
											<a data-toggle="tab" href="#profile12">
												Options
											</a>
										</li>
									</ul>
									<div className="tab-content tabs-flat">
										<div id="home11" className="tab-pane in active">
											<FormWrapper resourceObject={resourceObject} formName={formName} source={this.props.source} />
										</div>

										<div id="profile11" className="tab-pane">
											<ComponentsTable components={this.state.components} />
										</div>

										<div id="profile12" className="tab-pane">
											<ServiceOptionsTable options={this.state.options} />
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
				<div className="col-lg-6 col-sm-6 col-xs-12">
				</div>
			</div>
		);
	}
});


ReactDOM.render(
  <Tabs source={$("#source")[0].value} />,
  document.getElementById('write-content')
);


$(function() {

	$("#add-component-detail").click(function(){
		window.open("/ui/component/service_details_component?serviceId=" + serviceId + "&serviceVersion=" + serviceVersion, "_blank")
	});

	$("#add-options").click(function(){
		window.open("/ui/options/service_details_options?serviceId=" + serviceId + "&serviceVersion=" + serviceVersion, "_blank")
	});

	$("#btn-edit-features-current").click(function (e) {
		e.preventDefault();
		tinymce.init({
			selector: '#rich-edit',
			height: 250,
			plugins: "advlist"
		});
		tinymce.get('rich-edit').setContent($("#features_current").val());
		$("#modal-rich-html").modal('show');
		fieldEdited = "features_current";
	});

	$("#btn-edit-features-future").click(function (e) {
		e.preventDefault();
		tinymce.init({
			selector: '#rich-edit',
			height: 250,
			plugins: "advlist"
		});
		tinymce.get('rich-edit').setContent($("#features_future").val());
		$("#modal-rich-html").modal('show');
		fieldEdited = "features_future";
	});

	$("#btn-edit-use-cases").click(function (e) {
		e.preventDefault();
		tinymce.init({
			selector: '#rich-edit',
			height: 250,
			plugins: "advlist"
		});
		tinymce.get('rich-edit').setContent($("#use_cases").val());
		$("#modal-rich-html").modal('show');
		fieldEdited = "use_cases";
	});

	$("#confirm-edit").click(function () {

		if(fieldEdited == "features_current"){
			$("#features_current").val(tinymce.get('rich-edit').getContent());
		}
		else if(fieldEdited == "features_future"){
			$("#features_future").val(tinymce.get('rich-edit').getContent());
		}
		else if(fieldEdited == "use_cases"){
			$("#use_cases").val(tinymce.get('rich-edit').getContent());
		}

		fieldEdited = null;

	});

});


