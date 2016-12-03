
var formName = 'Service Details Options Form';


var serviceId = null;
var serviceDetailsId = null;
var serviceOptionsId = null;
var newServiceId = null;
var newServiceDetailsId = null;
var newServiceOptionsId = null;
var newServiceDetailsVersion = null;
var serviceDetailsVersion = null;
var opType = "";
var globalServiceData;
var globalServiceDetailsData;
var globalOptionsData;


var optionsServiceData = [
  {id: 1, value: -1, text: "Select service"}
];

var optionsServiceDetailsData = [
  {id: 1, value: -1, text: "Select service version"}
];

var optionsData = [
  {id: 1, value: -1, text: "Select service option"}
];

var resourceObject = [
	{ tag: 'select', type: 'text', name: 'service_id', placeholder: 'Enter service name', label: 'Service name', optionsData: optionsServiceData },
	{ tag: 'select', type: 'text', name: 'service_details_id', placeholder: 'Enter service version', label: 'Service version', optionsData: optionsServiceDetailsData },
	{ tag: 'select', type: 'text', name: 'service_options_id', placeholder: 'Enter service option name', label: 'Service option', optionsData: optionsData },
	{ tag: 'button', type: 'button', name: 'add-service-option', label: 'Edit', value: "Add"}
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
	newServiceId = parameter;
	jQuery.support.cors = true;
        $.ajax({
            url: $("#host")[0].value + "/api/v1/portfolio/services/" + serviceId,
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


				parameter = getParameterByName("serviceVersion", window.location);
				if(parameter != null) {
					serviceDetailsId = parameter;
					newServiceDetailsId = parameter;
					jQuery.support.cors = true;
						$.ajax({
							url: $("#host")[0].value + "/api/v1/portfolio/services/" + serviceId + "/service_details/" + serviceDetailsId,
							dataType: "json",
							crossDomain: true,
							type: "GET",
							cache: false,
							success: function (response) {
								console.log(response);
								var version = response.data.version;

								var service_details = $("#service_details_id");
								var optionsCount = $("#service_details_id>option").length;
								var v = name + " " + version;
								if(optionsCount <= 1){
									var option = $('<option></option>').attr("value", v)
											.text(v);
										service_details.append(option);
								}
								service_details.val(v).change();
							},
							error: function (xhr, status, err) {
							}
							});
				}

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

	validateForm: function(e){
		this.clearValidations();
		var validationObjects = [];
		var validationMessage = ''

		// --- validation code goes here ---
		var service = $('#service_id').val();
		if (service == '' || service == null || service == -1) {
			validationMessage = "The service is required";
			validationObjects.push({field: 'service_id', message: validationMessage});
		}

		var service_details = $('#service_details_id').val();
		if (service_details == null || service_details == "" || service_details == -1) {
			validationMessage = "The service version is required.";
			validationObjects.push({field: 'service_details_id', message: validationMessage});
		}

		var service_option = $("#service_options_id").val();
		if(service_option == null || service_option == "" || service_option == -1){
			validationMessage = "The service option is required.";
			validationObjects.push({field: 'service_options_id', message: validationMessage});
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

			if(service_id != "")
			{
				newServiceId = null;
				for(var i = 0; i < globalServiceData.length; i++){
					if(service_id == globalServiceData[i].name){
						newServiceId = globalServiceData[i].uuid;
						break;
					}
				}
			}


			var service_details_id =  $("#service_details_id").val();

			if(service_details_id != "")
			{
				newServiceDetailsId = null;
				newServiceDetailsVersion = null;
				for(var i = 0; i < globalServiceDetailsData.length; i++){
					if(service_details_id == globalServiceDetailsData[i].service.name + " " + globalServiceDetailsData[i].version){
						newServiceDetailsId = globalServiceDetailsData[i].uuid;
						newServiceDetailsVersion = globalServiceDetailsData[i].version;
						break;
					}
				}
			}


			var service_options_id =  $("#service_options_id").val();

			if(service_options_id != "")
			{
				newServiceOptionsId = null;
				for(var i = 0; i < globalOptionsData.length; i++){
					if(service_options_id == globalOptionsData[i].name){
						newServiceOptionsId = globalOptionsData[i].uuid;
						break;
					}
				}
			}



			var params = {};

			var parts = window.location.href.split("/");
			var host = "http://" + parts[2];
			var url = "";

			if (this.props.source != null && this.props.source != "") {

				params["service_options_uuid"] = serviceOptionsId;
				params["new_service_options_uuid"] = newServiceOptionsId;
				params["service_uuid"] = serviceId;
				params["new_service_uuid"] = newServiceId;
				params["service_details_uuid"] = serviceDetailsId;
				params["new_service_details_uuid"] = newServiceDetailsId;

				url = host + "/api/v1/options/service_details_option/edit";
				opType = "edit";
			}
			else {

				params["service_options_uuid"] = newServiceOptionsId;
				params["service_uuid"] = newServiceId;
				params["service_details_uuid"] = newServiceDetailsId;

				url = host + "/api/v1/options/service_details_option/add";
				opType = "add";
			}

			console.log(params);

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
						$("#modal-success-body").text("You have successfully inserted a new service details options relationship");
					else {
						serviceId = newServiceId;
						serviceDetailsId = newServiceDetailsId;
						serviceOptionsId = newServiceOptionsId;
						$("#modal-success-body").text("You have successfully updated the service details options relationship");
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

		jQuery.support.cors = true;
		var url = window.location.href;
        var contents = url.split("/");
        var host = contents[0] + "//" + contents[2];

		$.getJSON(
            host + "/api/v1/services/all",
            function (data) {
				var service = $("#service_id");
				var current = service.val();

				if(current != -1){
					$("#service_id option[value='" + current + "']").remove();
				}
				for(var i = 0; i < data.data.length; i++) {
					var option = $('<option></option>').attr("value", data.data[i].name).text(data.data[i].name);
					service.append(option);

				}
				if(current != -1)
					service.val(current).change();

				globalServiceData = data.data;

            });

		$.getJSON(
            host + "/api/v1/services/version/all",
            function (data) {
				var service_details = $("#service_details_id");
				var current = service_details.val();

				if(current != -1){
					$("#service_details_id option[value='" + current + "']").remove();
				}
				for(var i = 0; i < data.data.length; i++) {
					var v = data.data[i].service.name + " " + data.data[i].version;
					var option = $('<option></option>').attr("value", v).text(v);
					service_details.append(option);

				}
				if(current != -1)
					service_details.val(current).change();

				globalServiceDetailsData = data.data;

            });

		$.getJSON(
            host + "/api/v1/options/service_options/all",
            function (data) {
				var service_options = $("#service_options_id");
				var current = service_options.val();

				if(current != -1){
					$("#service_details_id option[value='" + current + "']").remove();
				}
				for(var i = 0; i < data.data.length; i++) {
					var option = $('<option></option>').attr("value", data.data[i].name).text(data.data[i].name);
					service_options.append(option);

				}
				if(current != -1)
					service_options.val(current).change();

				globalOptionsData = data.data;

            });

        if(this.props.source == null || this.props.source == "")
            return;

        this.serverRequest = $.ajax({
            url: this.props.source,
            dataType: "json",
            crossDomain: true,
            type: "GET",
            cache: false,
            success: function (data) {
                this.setState({data: data.data});

				var service = $("#service_id");
				var optionsCount = $("#service_id>option").length;
				if(optionsCount <= 1){
					var option = $('<option></option>').attr("value", this.state.data.service.name)
							.text(this.state.data.service.name);
						service.append(option);
				}
				service.val(this.state.data.service.name).change();


				var service_details = $("#service_details_id");
				optionsCount = $("#service_details_id>option").length;
				var v = this.state.data.service_details.service.name + " " + this.state.data.service_details.version;
				if(optionsCount <= 1){
					var option = $('<option></option>').attr("value", v).text(v);
						service_details.append(option);
				}
				service_details.val(v).change();


				var service_options = $("#service_options_id");
				optionsCount = $("#service_options_id>option").length;
				if(optionsCount <= 1){
					var option = $('<option></option>').attr("value", this.state.data.service_options.name).text(this.state.data.service_options.name);
						service_options.append(option);
				}
				service_options.val(this.state.data.service_options.name).change();


				serviceId = this.state.data.service.uuid;
				serviceDetailsId = this.state.data.service_details.uuid;
				serviceOptionsId = this.state.data.service_options.uuid;
				newServiceId = serviceId;
				newServiceDetailsId = serviceDetailsId;
				newServiceOptionsId = serviceOptionsId;
				serviceDetailsVersion = this.state.data.service_details.version;
				newServiceDetailsVersion = serviceDetailsVersion;

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

	$("#btn-add-service-option").click(function(e){
		e.preventDefault();
		window.open("/ui/options/service_options", "_blank");
	});

});