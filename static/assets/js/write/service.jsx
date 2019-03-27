var formName = 'Service Form';

var opType;
var serviceOwnerId;
var internalContactInformationId;
var externalContactInformationId;

var globalOwnerData;
var globalInternalContactData;
var globalExternalContactData;
var serviceId = null;

var fieldEdited = null;

var optionsOwnerData = [
  {id: 1, value: -1, text: "Select service owner"}
];

var optionsInternalContactData = [
  {id: 1, value: -1, text: "Select internal contact information"}
];

var optionsExternalContactData = [
  {id: 1, value: -1, text: "Select external contact information"}
];

var optionsArea = [
  {id: 1, value: -1, text: "Select service area"}
];

var optionsType = [
  {id: 1, value: -1, text: "Select service type"}
];

var resourceObject = [
	{ tag: 'input', type: 'text', name: 'name', placeholder: 'Enter name', label: 'Name', required: true },
	{ tag: 'textarea', type: 'textarea', name: 'description_external', placeholder: "Enter external description", label: 'External Description', required: true, onChange: 'textareaHTMLValidation' },
	{ tag: 'button', type: 'button', name: 'edit-description-external', label: 'Edit', value: "Edit"},
	{ tag: 'textarea', type: 'textarea', name: 'description_internal', placeholder: "Enter internal description", label: 'Internal Description', required: true, onChange: 'textareaHTMLValidation' },
	{ tag: 'button', type: 'button', name: 'edit-description-internal', label: 'Edit', value: "Edit"},
	{ tag: 'select', type: 'text', name: 'service_area', placeholder: 'Enter service area', label: 'Service Area', required: true, optionsData: optionsArea },
	{ tag: 'button', type: 'button', name: 'add-area', label: 'Add', value: "Add"},
	{ tag: 'select', type: 'text', name: 'service_type', placeholder: 'Enter service type', label: 'Service Type', required: true, optionsData: optionsType },
	{ tag: 'textarea', type: 'textarea', name: 'request_procedures', placeholder: "Enter request procedures", label: 'Request Procedures', required: true, onChange: 'textareaHTMLValidation' },
	{ tag: 'button', type: 'button', name: 'edit-request-procedures', label: 'Edit', value: "Edit"},
	{ tag: 'textarea', type: 'textarea', name: 'funders_for_service', placeholder: "Enter funders for service", label: 'Funders for Service', required: true, onChange: 'textareaHTMLValidation' },
	{ tag: 'button', type: 'button', name: 'edit-funders-for-service', label: 'Edit', value: "Edit"},
	{ tag: 'textarea', type: 'textarea', name: 'user_value', placeholder: "Enter value to customer", label: 'Value to customer', required: true, onChange: 'textareaHTMLValidation' },
	{ tag: 'button', type: 'button', name: 'edit-value-to-customer', label: 'Edit', value: "Edit"},
	{ tag: 'textarea', type: 'textarea', name: 'risks', placeholder: "Enter risks", label: 'Risks', required: true, onChange: 'textareaHTMLValidation' },
	{ tag: 'button', type: 'button', name: 'edit-risks', label: 'Edit', value: "Edit"},
	{ tag: 'textarea', type: 'textarea', name: 'competitors', placeholder: "Enter competitors", label: 'Competitors', required: true, onChange: 'textareaHTMLValidation' },
	{ tag: 'button', type: 'button', name: 'edit-competitors', label: 'Edit', value: "Edit"},
	// todo: how to fill the data for the options (should be done before rendering)
	{ tag: 'select', type: 'text', name: 'service_owner', label: 'Service Owner', placeholder: "Enter service owner name", optionsData: optionsOwnerData },
	{ tag: 'button', type: 'button', name: 'add-owner', label: 'Add', value: "Add"},
	{ tag: 'button', type: 'button', name: 'edit-owner', label: 'Add', value: "Edit"},
	{ tag: 'select', type: 'text', name: 'contact_information_external', label: 'Contact Information External', placeholder: "Enter external contact info", optionsData: optionsExternalContactData },
	{ tag: 'button', type: 'button', name: 'add-contact', label: 'Add', value: "Add"},
	{ tag: 'button', type: 'button', name: 'edit-external', label: 'Add', value: "Edit"},
	{ tag: 'select', type: 'text', name: 'contact_information_internal', label: 'Contact Information Internal', placeholder: "Enter internal contact info", optionsData: optionsInternalContactData },
	{ tag: 'button', type: 'button', name: 'add-int-contact', label: 'Add', value: "Add"},
	{ tag: 'button', type: 'button', name: 'edit-internal', label: 'Add', value: "Edit"}
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
		var validationMessage = '';

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
			//var formValues = JSON.stringify($("#service-form").serializeJSON());
			//console.log("The form values are ->", formValues);


			var service_owner_id =  $("#service_owner").val();

			if(service_owner_id != "")
			{
				serviceOwnerId = null;
				for(var i = 0; i < globalOwnerData.length; i++){
					if(service_owner_id == globalOwnerData[i].first_name + " " + globalOwnerData[i].last_name){
						serviceOwnerId = globalOwnerData[i].uuid;
						break;
					}
				}
			}


			var external_contact_information =  $("#contact_information_external").val();

			if(external_contact_information != "")
			{
				externalContactInformationId = null;
				for(var i = 0; i < globalExternalContactData.length; i++){
					if(external_contact_information == globalExternalContactData[i].internal_contact_information.internal_contact_information.first_name +
						" " + globalExternalContactData[i].internal_contact_information.internal_contact_information.last_name){
						externalContactInformationId = globalExternalContactData[i].internal_contact_information.internal_contact_information.uuid;
						break;
					}
				}
			}


			var internal_contact_information =  $("#contact_information_internal").val();

			if(internal_contact_information != "")
			{
				internalContactInformationId = null;
				for(var i = 0; i < globalInternalContactData.length; i++){
					if(internal_contact_information == globalInternalContactData[i].internal_contact_information.internal_contact_information.first_name + " "
						+ globalInternalContactData[i].internal_contact_information.internal_contact_information.last_name){
						internalContactInformationId = globalInternalContactData[i].internal_contact_information.internal_contact_information.uuid;
						break;
					}
				}
			}

			var area = $("#service_area").val();
			if(area == "-1" || area == -1)
				area = null;
			var type = $("#service_type").val();
			if(type == "-1" || type == -1)
				type = null;

			var params = {};
			params["name"] = $("#name").val();
			params["description_external"] = $("#description_external").val();
			params["description_internal"] = $("#description_internal").val();
			params["service_area"] = area;
			params["service_type"] = type;
			params["request_procedures"] = $("#request_procedures").val();
			params["funders_for_service"] = $("#funders_for_service").val();
			params["user_value"] = $("#user_value").val();
			params["risks"] = $("#risks").val();
			params["competitors"] = $("#competitors").val();


			if(serviceOwnerId != null)
				params["service_owner_uuid"] = serviceOwnerId;
			if(externalContactInformationId != null)
				params["service_contact_information_uuid"] = externalContactInformationId;
			if(internalContactInformationId != null)
				params["service_internal_contact_information_uuid"] = internalContactInformationId;


			var parts = window.location.href.split("/");
			var host = "https://" + parts[2];
			var url = "";

			if(this.props.source != null && this.props.source != ""){
				params["uuid"] = serviceId;
				url = host + "/api/v1/services/edit";
				opType = "edit";
			}
			else {
				url = host + "/api/v1/services/add";
				opType = "add";
			}

			this.serverRequest = $.ajax({
				url: url,
				headers: {
					"X-CSRFToken": $("input[name=csrfmiddlewaretoken]")[0].value,
					"AUTHTOKEN": localStorage.apiToken,
					"EMAIL": localStorage.apiEmail, "TEST-STH": "something"
				},
				dataType: "json",
				crossDomain: true,
				type: "POST",
				contentType:"application/json",
				cache: false,
				data: JSON.stringify(params),
				success: function (data) {
					if(opType == "add")
						$("#modal-success-body").text("You have successfully inserted a new service");
					else
						$("#modal-success-body").text("You have successfully updated the service");
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

var ServiceDetailsTable = React.createClass({


	getInitialState: function () {
		return {
			versions: [],
			count: 0,
			selected: 0,
			service_name: ""
		}
	},

	render: function() {

		var array = [];
		for(var i = 0; i < this.state.count; i++)
			array.push(i);

		var service_name = this.props.service_name;

		return (
			<div className="row">
				<div className="col-xs-12">
					<div className="well with-header  with-footer">
						<div className="form-group">
			      	        <button value="Add service version" id="add-version" className="btn btn-purple">Add service version</button>
			      	    </div>
						<table className="table table-hover">
							<thead className="bordered-darkorange">
								<tr>
									<th>
										Version
									</th>
									<th>
										Status
									</th>
									<th>
										In catalogue
									</th>

									<th>

									</th>
								</tr>
							</thead>
							<tbody>

							{this.props.versions.map(function (version) {
								var in_catalogue = "No";
								if(version.in_catalogue)
									in_catalogue = "Yes";
								return (
									<tr key={version.version}>
										<td>{version.version}</td>
										<td>{version.service_status}</td>
										<td>{in_catalogue}</td>
										<td><a href={"/ui/service/" + service_name + "/version/" + version.version}>Edit</a></td>
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


var ExternalServiceTable = React.createClass({


	getInitialState: function () {
		return {
			services: []
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
			      	        <button value="Add external service" id="add-external" className="btn btn-purple">Add external dependency</button>
			      	    </div>
						<table className="table table-hover">
							<thead className="bordered-darkorange">
								<tr>
									<th>
										Name
									</th>
									<th>

									</th>
								</tr>
							</thead>
							<tbody>

							{this.props.services.map(function (service) {
								return (
									<tr key={service.uuid}>
										<td>{service.name}</td>
										<td><a href={"/ui/service/external/" + service.uuid}>Edit</a></td>
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


var InternalServiceTable = React.createClass({


	getInitialState: function () {
		return {
			services: []
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
			      	        <button value="Add internal service" id="add-internal" className="btn btn-purple">Add internal dependency</button>
			      	    </div>
						<table className="table table-hover">
							<thead className="bordered-darkorange">
								<tr>
									<th>
										Name
									</th>
									<th>

									</th>
								</tr>
							</thead>
							<tbody>

							{this.props.services.map(function (service) {
								return (
									<tr key={service.uuid}>
										<td>{service.service.name}</td>
										<td><a href={"/ui/service/" + service.service.name}>Edit</a></td>
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

var UsersCustomersTable = React.createClass({


	getInitialState: function () {
		return {
			users: []
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
			      	        <button value="Add user customer" id="add-user" className="btn btn-purple">Add user customer</button>
			      	    </div>
						<table className="table table-hover">
							<thead className="bordered-darkorange">
								<tr>
									<th>
										Name
									</th>
									<th>
										Role
									</th>
									<th>

									</th>
								</tr>
							</thead>
							<tbody>

							{this.props.users.map(function (user) {
								return (
									<tr key={user.uuid}>
										<td>{user.name}</td>
										<td>{user.role}</td>
										<td><a href={"/ui/service/users_customers/" + user.uuid}>Edit</a></td>
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
			service: {
			},
			service_details: [],
			external_services: [],
			internal_services: [],
			users_customers: []
		}
	},

    componentDidMount: function () {


		jQuery.support.cors = true;
		var url = window.location.href;
        var contents = url.split("/");
        var host = contents[0] + "//" + contents[2];

		$.getJSON(
            host + "/api/v1/owner/all",
            function (data) {
				var service_owner = $("#service_owner");
				var current = service_owner.val();

				if(current != -1){
					$("#service_owner option[value='" + current + "']").remove();
				}
				for(var i = 0; i < data.data.length; i++) {
					var option = $('<option></option>').attr("value", data.data[i].first_name + " " + data.data[i].last_name )
						.text(data.data[i].first_name + " " + data.data[i].last_name);
					service_owner.append(option);

				}
				if(current != -1)
					service_owner.val(current).change();

				globalOwnerData = data.data;

            });


		$.getJSON(
            host + "/api/v1/owner/contact_information/all",
            function (data) {
				var contact_information_external = $("#contact_information_external");
				var current = contact_information_external.val();

				if(current != -1){
					$("#contact_information_external option[value='" + current + "']").remove();
				}
				for(var i = 0; i < data.data.length; i++) {
					var v = data.data[i].internal_contact_information.internal_contact_information.first_name + " "
						+ data.data[i].internal_contact_information.internal_contact_information.last_name;
					var option = $('<option></option>').attr("value",  v).text(v);
					contact_information_external.append(option);

				}
				if(current != -1)
					contact_information_external.val(current).change();

				globalExternalContactData = data.data;


				var contact_information_internal = $("#contact_information_internal");
				current = contact_information_internal.val();

				if(current != -1){
					$("#contact_information_internal option[value='" + current + "']").remove();
				}
				for(var i = 0; i < data.data.length; i++) {
					var v = data.data[i].internal_contact_information.internal_contact_information.first_name + " "
						+ data.data[i].internal_contact_information.internal_contact_information.last_name;
					var option = $('<option></option>').attr("value", v ).text(v);
					contact_information_internal.append(option);

				}
				if(current != -1)
					contact_information_internal.val(current).change();

				globalInternalContactData = data.data;

            });


		$.getJSON(
            host + "/api/v1/services/area/all",
            function (data) {
				var service_area = $("#service_area");
				var current = service_area.val();

				if(current != -1){
					$("#service_area option[value='" + current + "']").remove();
				}
				for(var i = 0; i < data.data.length; i++) {
					var option = $('<option></option>').attr("value", data.data[i].area).text(data.data[i].area);
					service_area.append(option);

				}
				if(current != -1)
					service_area.val(current).change();
            });

		$.getJSON(
            host + "/api/v1/services/type/all",
            function (data) {
				var type = $("#service_type");
				var current = type.val();

				if(current != -1){
					$("#service_type option[value='" + current + "']").remove();
				}
				for(var i = 0; i < data.data.length; i++) {
					var option = $('<option></option>').attr("value", data.data[i].type).text(data.data[i].type);
					type.append(option);

				}
				if(current != -1)
					type.val(current).change();

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
                this.setState({service: data.data});
                $("#name").val(this.state.service.name);
                $("#description_internal").val(this.state.service.description_internal);
                $("#description_external").val(this.state.service.description_external);
                $("#request_procedures").val(this.state.service.request_procedures);
                $("#funders_for_service").val(this.state.service.funders_for_service);
                $("#user_value").val(this.state.service.user_value);
                $("#risks").val(this.state.service.risks);
                $("#competitors").val(this.state.service.competitors);

				serviceId = this.state.service.uuid;

				var service_area = $("#service_area");
				var optionsCount = $("#service_area>option").length;
				var sa = this.state.service.service_area;
				if(optionsCount <= 1){
					var option = $('<option></option>').attr("value", sa).text(sa);
						service_area.append(option);
				}
				service_area.val(sa).change();

				var service_type = $("#service_type");
				optionsCount = $("#service_type>option").length;
				var st = this.state.service.service_type;
				if(optionsCount <= 1){
					var option = $('<option></option>').attr("value", st).text(st);
						service_type.append(option);
				}
				service_type.val(st).change();


				if(this.state.service.service_owner != null){
					var service_owner = $("#service_owner");
					optionsCount = $("#service_owner>option").length;
					var so = this.state.service.service_owner.first_name + " " + this.state.service.service_owner.last_name;
					if(optionsCount <= 1){
						var option = $('<option></option>').attr("value", so).text(so);
							service_owner.append(option);
					}
					service_owner.val(so).change();

					serviceOwnerId = this.state.service.service_owner.uuid;
				}



				if(this.state.service.contact_information.internal_contact_information != null){
					var contact_information_internal = $("#contact_information_internal");
					optionsCount = $("#contact_information_internal>option").length;
					var cii = this.state.service.contact_information.internal_contact_information
						.internal_contact_information.internal_contact_information.first_name + " " + this.state.service.contact_information.internal_contact_information
						.internal_contact_information.internal_contact_information.last_name;
					if(optionsCount <= 1){
						var option = $('<option></option>').attr("value", cii).text(cii);
							contact_information_internal.append(option);
					}
					contact_information_internal.val(cii).change();

					internalContactInformationId = this.state.service.contact_information.internal_contact_information.
						internal_contact_information.internal_contact_information.uuid;
				}

				if(this.state.service.contact_information.external_contact_information != null){
					var contact_information_external = $("#contact_information_external");
					optionsCount = $("#contact_information_external>option").length;
					var cie = this.state.service.contact_information.external_contact_information
						.internal_contact_information.internal_contact_information.first_name + " " + this.state.service.contact_information.external_contact_information
						.internal_contact_information.internal_contact_information.last_name;
					console.log(cie);
					if(optionsCount <= 1){
						var option = $('<option></option>').attr("value", cie).text(cie);
							contact_information_external.append(option);
					}
					contact_information_external.val(cie).change();

					externalContactInformationId = this.state.service.contact_information.external_contact_information.
						internal_contact_information.internal_contact_information.uuid;
				}


				this.setState({service_details: this.state.service.service_details_list.service_details});
				this.setState({external_services: this.state.service.external.external_services});
				this.setState({internal_services: this.state.service.dependencies_list.services});
				this.setState({users_customers: this.state.service.user_customers_list.user_customers})

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
							<span className="widget-caption">Service</span>
						</div>

						<div className="widget-body">
							<div className="widget-main ">
								<div className="tabbable">
									<ul className="nav nav-tabs tabs-flat" id="myTab11">
										<li className="active">
											<a data-toggle="tab" href="#home11">
												Service
											</a>
										</li>
										<li>
											<a data-toggle="tab" href="#profile11">
												Versions
											</a>
										</li>
										<li>
											<a data-toggle="tab" href="#profile12">
												Internal dependencies
											</a>
										</li>
										<li>
											<a data-toggle="tab" href="#profile13">
												External dependencies
											</a>
										</li>
										<li>
											<a data-toggle="tab" href="#profile14">
												Users customers
											</a>
										</li>
									</ul>
									<div className="tab-content tabs-flat">
										<div id="home11" className="tab-pane in active">
											<FormWrapper resourceObject={resourceObject} formName={formName} source={this.props.source} />
										</div>

										<div id="profile11" className="tab-pane">
											<ServiceDetailsTable service_name={this.state.service.name} versions={this.state.service_details} />
										</div>

										<div id="profile12" className="tab-pane">
											<InternalServiceTable services={this.state.internal_services} />
										</div>

										<div id="profile13" className="tab-pane">
											<ExternalServiceTable services={this.state.external_services} />
										</div>

										<div id="profile14" className="tab-pane">
											<UsersCustomersTable users={this.state.users_customers} />
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

$(function(){

	$("#add-version").click(function () {
		window.open("/ui/service/version?serviceId=" + serviceId, "_blank");
	});

	$("#add-external").click(function () {
		window.open("/ui/service/external_dependency?serviceId=" + serviceId, "_blank");
	});

	$("#add-internal").click(function () {
		window.open("/ui/service/internal_dependency?serviceId=" + serviceId, "_blank");
	});

	$("#add-user").click(function () {
		window.open("/ui/service/users_customers?serviceId=" + serviceId, "_blank");
	});

	$("#btn-add-area").click(function (e) {
		e.preventDefault();
		window.open("/ui/service/area", "_blank");
	});

	$("#btn-add-owner").click(function (e) {
		e.preventDefault();
		window.open("/ui/owner/", "_blank");
	});

	$("#btn-edit-owner").click(function (e) {
		e.preventDefault();
		window.open("/ui/owner/" + serviceOwnerId, "_blank");
	});

	$("#btn-add-contact").click(function (e) {
		e.preventDefault();
		window.open("/ui/owner/contact_information", "_blank");
	});

	$("#btn-add-int-contact").click(function (e) {
		e.preventDefault();
		window.open("/ui/owner/contact_information", "_blank");
	});

	$("#btn-edit-internal").click(function (e) {
		e.preventDefault();
		window.open("/ui/owner/contact_information/" + internalContactInformationId, "_blank");
	});

	$("#btn-edit-external").click(function (e) {
		e.preventDefault();
		window.open("/ui/owner/contact_information/" + externalContactInformationId, "_blank");
	});

	$("#btn-edit-description-external").click(function(e){
		e.preventDefault();
		tinymce.init({
			selector:'#rich-edit',
			height: 250,
			plugins: "advlist"
		});
		tinymce.get('rich-edit').setContent($("#description_external").val());
		$("#modal-rich-html").modal('show');
		fieldEdited = "description_external";
	});

	$("#btn-edit-description-internal").click(function(e){
		e.preventDefault();
		tinymce.init({
			selector:'#rich-edit',
			height: 250,
			plugins: "advlist"
		});
		tinymce.get('rich-edit').setContent($("#description_internal").val());
		$("#modal-rich-html").modal('show');
		fieldEdited = "description_internal";
	});

	$("#btn-edit-request-procedures").click(function(e){
		e.preventDefault();
		tinymce.init({
			selector:'#rich-edit',
			height: 250,
			plugins: "advlist"
		});
		tinymce.get('rich-edit').setContent($("#request_procedures").val());
		$("#modal-rich-html").modal('show');
		fieldEdited = "request_procedures";
	});

	$("#btn-edit-funders-for-service").click(function(e){
		e.preventDefault();
		tinymce.init({
			selector:'#rich-edit',
			height: 250,
			plugins: "advlist"
		});
		tinymce.get('rich-edit').setContent($("#funders_for_service").val());
		$("#modal-rich-html").modal('show');
		fieldEdited = "funders_for_service";
	});

	$("#btn-edit-value-to-customer").click(function(e){
		e.preventDefault();
		tinymce.init({
			selector:'#rich-edit',
			height: 250,
			plugins: "advlist"
		});
		tinymce.get('rich-edit').setContent($("#user_value").val());
		$("#modal-rich-html").modal('show');
		fieldEdited = "user_value";
	});

	$("#btn-edit-risks").click(function(e){
		e.preventDefault();
		tinymce.init({
			selector:'#rich-edit',
			height: 250,
			plugins: "advlist"
		});
		tinymce.get('rich-edit').setContent($("#risks").val());
		$("#modal-rich-html").modal('show');
		fieldEdited = "risks";
	});

	$("#btn-edit-competitors").click(function(e){
		e.preventDefault();
		tinymce.init({
			selector:'#rich-edit',
			height: 250,
			plugins: "advlist"
		});
		tinymce.get('rich-edit').setContent($("#competitors").val());
		$("#modal-rich-html").modal('show');
		fieldEdited = "competitors";
	});



	$("#confirm-edit").click(function () {

		if(fieldEdited == "description_external"){
			$("#description_external").val(tinymce.get('rich-edit').getContent());
		}
		else if(fieldEdited == "description_internal"){
			$("#description_internal").val(tinymce.get('rich-edit').getContent());
		}
		else if(fieldEdited == "request_procedures"){
			$("#request_procedures").val(tinymce.get('rich-edit').getContent());
		}
		else if(fieldEdited == "funders_for_service"){
			$("#funders_for_service").val(tinymce.get('rich-edit').getContent());
		}
		else if(fieldEdited == "user_value"){
			$("#user_value").val(tinymce.get('rich-edit').getContent());
		}
		else if(fieldEdited == "risks"){
			$("#risks").val(tinymce.get('rich-edit').getContent());
		}
		else if(fieldEdited == "competitors"){
			$("#competitors").val(tinymce.get('rich-edit').getContent());
		}

		fieldEdited = null;

	});

});
