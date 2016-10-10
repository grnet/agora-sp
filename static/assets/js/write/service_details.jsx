
var formName = 'Service Details Form';

var opType;
var serviceId;
var serviceName;
var globalData;

var optionsData = [
  {id: 1, value: 1, text: "option 1"},
  {id: 2, value: 2, text: "option 2"},
	{id: 3, value: 3, text: "option 3"}
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
	{ tag: 'textarea', type: 'textarea', name: 'features_future', placeholder: "Enter future features", label: 'Features Future', onChange: 'textareaHTMLValidation' },
	// todo: how to fill the data for the options (should be done before rendering)
	{ tag: 'select', type: 'select', name: 'usage_policy_has', label: 'Has Usage Policy', required: true, optionsData: booleanData },
	{ tag: 'input', type: 'text', name: 'usage_policy_url', placeholder: 'Enter Usage Policy URL', label: 'Usage Policy URL', onChange: 'urlContentChanged' },

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
	{ tag: 'select', type: 'select', name: 'is_in_catalog', label: 'Is in catalog', required: true, optionsData: booleanData },
	{ tag: 'input', type: 'text', name: 'service_id', label: 'Service', required: true, placeholder: "Enter service name" }

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
		if(service == '' || service == null){
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

		var usage_policy_has = $("#usage_policy_has").val();
		var usage_policy_url = $("#usage_policy_url").val();

		if(usage_policy_has == "false" && usage_policy_url != null && usage_policy_url != ""){
			validationMessage = "Usage policy URL cannot be filled without checking the select box";
			validationObjects.push( { field: 'usage_policy_url', message: validationMessage } );
		}

		if(usage_policy_has == "true" && (usage_policy_url == null || usage_policy_url == "")){
			validationMessage = "Usage policy URL cannot be empty with the select box checked";
			validationObjects.push( { field: 'usage_policy_url', message: validationMessage } );
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
			params["version"] = $("#version").val();
			params["status"] = $("#status").val();
			params["features_current"] = $("#features_current").val();
			params["features_future"] = $("#features_future").val();
			params["usage_policy_has"] = $("#usage_policy_has").val();
			params["usage_policy_url"] = $("#usage_policy_url").val();
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
			params["is_in_catalog"] = $("#is_in_catalog").val();
			params["service_id"] = serviceId;


			var parts = window.location.href.split("/");
			var host = "https://" + parts[2];
			var url = "";

			if(this.props.source != null && this.props.source != ""){
				params["uuid"] = parts[parts.length - 1];
				url = host + "/api/v1/services/" + serviceId + "/service_details/edit";
				opType = "edit";
			}
			else {
				url = host + "/api/v1/services/" + serviceId + "/service_details/add";
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

	getInitialState: function () {
		return {
			service_details: {
				version: ""
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
                this.setState({service_details: data.data});
                $("#version").val(this.state.service_details.version);
                $("#status").val(this.state.service_details.status);
                $("#features_current").val(this.state.service_details.features_current);
                $("#features_future").val(this.state.service_details.features_future);
                $("#usage_policy_has").val(this.state.service_details.usage_policy_has.toString());
                $("#usage_policy_url").val(this.state.service_details.usage_policy_link.related.href);
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
                $("#is_in_catalog").val(this.state.service_details.is_in_catalog);
                $("#service_id").val(this.state.service_details.service.name);
				serviceId = this.state.service_details.service.uuid;
				serviceName = this.state.service_details.service.name;
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
		}
    });

	var getData = function(request, response){

        var url = window.location.href;
        var contents = url.split("/");
        var host = contents[0] + "//" + contents[2];

		$.getJSON(
            host + "/api/v1/services/all?search=" + request.term,
            function (data) {
				for(var i = 0; i < data.data.length; i++) {
					data.data[i].value = data.data[i].name;
					data.data[i].index = i;
				}
				globalData = data.data;
                response(data.data);
            });
	};

    $( "#service_id" ).autocomplete({
      source: getData,
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