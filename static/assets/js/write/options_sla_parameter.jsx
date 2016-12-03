
var formName = 'Options SLA Parametar Form';

var parameterId = null;
var slaId = null;
var serviceOptionsId = null;
var newParameterId = null;
var newSlaId = null;
var newServiceOptionsId = null;
var opType = "";
var globalParameterData;
var globalSlaData;
var globalOptionsData;

var optionsParameterData = [
  {id: 1, value: -1, text: "Select parameter"}
];

var optionsSlaData = [
  {id: 1, value: -1, text: "Select SLA"}
];

var optionsData = [
  {id: 1, value: -1, text: "Select service options"}
];

var resourceObject = [
	{ tag: 'select', type: 'text', name: 'sla_id', placeholder: 'Enter SLA name', label: 'SLA', optionsData: optionsSlaData },
	{ tag: 'select', type: 'text', name: 'service_options_id', placeholder: 'Enter service option name', label: 'Service option', optionsData: optionsData },
	{ tag: 'select', type: 'text', name: 'parameter_id', placeholder: 'Enter parameter name', label: 'Parameter', optionsData: optionsParameterData },
	{ tag: 'button', type: 'button', name: 'add-param', label: 'Edit', value: "Add"}
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

var parameter = getParameterByName("slaId", window.location);
if(parameter != null) {
	slaId = parameter;
	newSlaId = parameter;
	jQuery.support.cors = true;
        $.ajax({
            url: $("#host")[0].value + "/api/v1/options/sla/" + slaId,
            dataType: "json",
            crossDomain: true,
            type: "GET",
            cache: false,
            success: function (response) {
				var name = response.data.name;
				var sla = $("#sla_id");
				var optionsCount = $("#sla_id>option").length;
				if(optionsCount <= 1){
					var option = $('<option></option>').attr("value", name)
							.text(name);
						sla.append(option);
				}
				sla.val(name).change();

				var opt_name = response.data.service_option.name;
				var options = $("#service_options_id");
				optionsCount = $("#service_options_id>option").length;
				if(optionsCount <= 1){
					var option = $('<option></option>').attr("value", opt_name)
							.text(opt_name);
						options.append(option);
				}
				options.val(opt_name).change();
				serviceOptionsId = response.data.service_option.uuid;
				newServiceOptionsId = response.data.service_option.uuid;
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
		var param = $('#parameter_id').val();
		if(param == '' || param == null || param == -1){
			validationMessage = "The parameter is required";
			validationObjects.push( { field: 'parameter_id', message: validationMessage } );
		}
		//if($('#name').val().length > 255){
		//	validationMessage = "Content exceeds max length of 255 characters."
		//	validationObjects.push( { field: 'name', message: validationMessage } );
		//}

		var sla = $('#sla_id').val();
		if(sla == null || sla == "" || sla == -1){
			validationMessage = "The SLA is required";
			validationObjects.push( { field: 'sla_id', message: validationMessage } );
		}

		var service_option = $('#service_options_id').val();
		if(service_option == null || service_option == "" || service_option == -1){
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

			if(parameter_id != "")
			{
				newParameterId = null;
				for(var i = 0; i < globalParameterData.length; i++){
					if(parameter_id == globalParameterData[i].name){
						newParameterId = globalParameterData[i].uuid;
						break;
					}
				}
			}


			var sla_id =  $("#sla_id").val();

			if(sla_id != "")
			{
				newSlaId = null;
				for(var i = 0; i < globalSlaData.length; i++){
					if(sla_id == globalSlaData[i].name){
						newSlaId = globalSlaData[i].id;
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


		jQuery.support.cors = true;
		var url = window.location.href;
        var contents = url.split("/");
        var host = contents[0] + "//" + contents[2];

		$.getJSON(
            host + "/api/v1/options/parameter/all",
            function (data) {
				var parameter = $("#parameter_id");
				var current = parameter.val();

				if(current != -1){
					$("#parameter_id option[value='" + current + "']").remove();
				}
				for(var i = 0; i < data.data.length; i++) {
					var option = $('<option></option>').attr("value", data.data[i].name).text(data.data[i].name);
					parameter.append(option);

				}
				if(current != -1)
					parameter.val(current).change();

				globalParameterData = data.data;

            });

		$.getJSON(
            host + "/api/v1/options/sla/all",
            function (data) {
				var sla = $("#sla_id");
				var current = sla.val();

				if(current != -1){
					$("#sla_id option[value='" + current + "']").remove();
				}
				for(var i = 0; i < data.data.length; i++) {
					var option = $('<option></option>').attr("value", data.data[i].name).text(data.data[i].name);
					sla.append(option);

				}
				if(current != -1)
					sla.val(current).change();

				globalSlaData = data.data;

            });

		$.getJSON(
            host + "/api/v1/options/service_options/all",
            function (data) {
				var service_options = $("#service_options_id");
				var current = service_options.val();

				if(current != -1){
					$("#service_options_id option[value='" + current + "']").remove();
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


				var parameter = $("#parameter_id");
				var optionsCount = $("#parameter_id>option").length;
				if(optionsCount <= 1){
					var option = $('<option></option>').attr("value", this.state.data.parameter.name)
							.text(this.state.data.parameter.name);
						parameter.append(option);
				}
				parameter.val(this.state.data.parameter.name).change();

				var sla = $("#sla_id");
				optionsCount = $("#sla_id>option").length;
				if(optionsCount <= 1){
					var option = $('<option></option>').attr("value", this.state.data.sla.name)
							.text(this.state.data.sla.name);
						sla.append(option);
				}
				sla.val(this.state.data.sla.name).change();

				var service_options = $("#service_options_id");
				optionsCount = $("#service_options_id>option").length;
				if(optionsCount <= 1){
					var option = $('<option></option>').attr("value", this.state.data.service_options.name)
							.text(this.state.data.service_options.name);
						service_options.append(option);
				}
				service_options.val(this.state.data.service_options.name).change();



				parameterId = this.state.data.parameter.uuid;
				slaId = this.state.data.sla.uuid;
				serviceOptionsId = this.state.data.service_options.uuid;
				newParameterId = parameterId;
				newSlaId = slaId;
				newServiceOptionsId = serviceOptionsId;
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

	$("#btn-add-param").click(function(e){
		e.preventDefault();
		window.open("/ui/options/parameter", "_blank");
	});

});