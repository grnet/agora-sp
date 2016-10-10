
var formName = 'Service Component Implementation Detail Form';

var serviceId = null;
var serviceDetailsId = null;
var componentImplementationDetailId = null;
var newServiceId = null;
var newServiceDetailsId = null;
var newComponentImplementationDetailId = null;
var newServiceName = null;
var newServiceDetailsName = null;
var newComponentImplementationDetailName = null;
var newServiceDetailsVersion = null;
var serviceDetailsVersion = null;
var opType = "";
var globalServiceData;
var globalServiceDetailsData;
var globalComponentData;

var optionsData = [
  {id: 1, value: 1, text: "option 1"},
  {id: 2, value: 2, text: "option 2"},
	{id: 3, value: 3, text: "option 3"}
];

var resourceObject = [
	{ tag: 'input', type: 'text', name: 'service_id', placeholder: 'Enter service name', label: 'Service' },
	{ tag: 'input', type: 'text', name: 'service_details_id', label: 'Service details', placeholder: "Enter service version" },
	{ tag: 'input', type: 'text', name: 'component_implementation_detail_id', label: 'Component implementation detail', placeholder: "Enter component implementation detail version" }
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

var FormWrapper;
FormWrapper = React.createClass({

	generateFormElements: function (resourceObject) {
		var formElements = resourceObject.map(function (field, i) {
			if (field.tag == 'input') {
				if (field.type == 'text') {
					return (
						<div className="form-group" key={i}>
							<label htmlFor={field.name}>{field.label}</label>
							<input className="form-control" id={field.name} type={field.type} name={field.name}
								   placeholder={field.placeholder} aria-describedby={field.name + '-error'}/>
							<span id={field.name + '-error'} className="validation-message sr-only"></span>
						</div>
					);
				}
			}
			else if (field.tag == 'textarea') {
				return (
					<div className="form-group" key={i}>
						<label htmlFor={field.name}>{field.label}</label>
						<textarea className="form-control" id={field.name} name={field.name}
								  placeholder={field.placeholder} rows="6" onChange={this[field.onChange]}></textarea>
						<span id={field.name + '-error'} className="validation-message sr-only"></span>
					</div>
				);
			}
			else if (field.tag == 'select') {
				return (
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

	markInvalid: function (elRef, message) {
		$('#' + elRef).next().removeClass('sr-only');
		$('#' + elRef).next().html(message);
		$('#' + elRef).parent().addClass('has-error');
		$('html, body').animate({
			scrollTop: $('#' + elRef).offset().top
		}, 800);
	},

	clearValidations: function () {
		$('body').find('.has-error').removeClass('has-error');
		$('body').find('.validation-message').addClass('sr-only');
	},

	textareaHTMLValidation: function (e) {
		var div = document.createElement('div');
		div.innerHTML = $(e.target).val();
		if ($(div).find('script').length > 0 || $(div).find('link').length) {
			div = null;
			this.markInvalid($(e.target).attr('name'), 'This HTML content must not have script or css tags');
		}
		else {
			$(e.target).parent().removeClass('has-error');
			$(e.target).parent().find('.validation-message').addClass('sr-only');
		}
		div = null
	},

	validateForm: function (e) {
		this.clearValidations();
		var validationObjects = [];
		var validationMessage = ''

		// --- validation code goes here ---
		var service = $('#service_id').val();
		if (service == '' || service == null) {
			validationMessage = "The service is required";
			validationObjects.push({field: 'service_id', message: validationMessage});
		}

		var service_details = $('#service_details_id').val();
		if (service_details == null || service_details == "") {
			validationMessage = "The service version is required.";
			validationObjects.push({field: 'service_details_id', message: validationMessage});
		}

		var comp_imp_det = $('#component_implementation_detail_id').val();
		if (comp_imp_det == null || comp_imp_det == "") {
			validationMessage = "The component implementation details are required.";
			validationObjects.push({field: 'component_implementation_detail_id', message: validationMessage});
		}

		if (validationObjects.length > 0) {
			var i = 0;
			for (i = 0; i < validationObjects.length; i++) {
				this.markInvalid(validationObjects[i].field, validationObjects[i].message);
			}
			return false;
		}

		return true;
	},

	handleSubmit: function (e) {
		// some validation
		// ajax url call + redirect
		e.preventDefault();

		if (this.validateForm()) {
			//var formValues = JSON.stringify($("#service-form").serializeJSON());
			//console.log("The form values are ->", formValues);

			var service_id =  $("#service_id").val();

			if(newServiceName != service_id){
				if(newServiceName != null || service_id != "")
				{
					newServiceName = null;
					newServiceId = null;
					for(var i = 0; i < globalServiceData.length; i++){
						if(service_id == globalServiceData[i].name){
							newServiceId = globalServiceData[i].uuid;
							newServiceName = service_id;
							break;
						}
					}
				}
			}

			var service_details_id =  $("#service_details_id").val();

			if(newServiceDetailsName != service_details_id){
				if(newServiceDetailsName != null || service_details_id != "")
				{
					newServiceDetailsName = null;
					newServiceDetailsId = null;
					newServiceDetailsVersion = null;
					for(var i = 0; i < globalServiceDetailsData.length; i++){
						if(service_details_id == globalServiceDetailsData[i].service.name + " " + globalServiceDetailsData[i].version){
							newServiceDetailsId = globalServiceDetailsData[i].uuid;
							newServiceDetailsName = service_details_id;
							newServiceDetailsVersion = globalServiceDetailsData[i].version;
							break;
						}
					}
				}
			}

			var component_implementation_detail_id =  $("#component_implementation_detail_id").val();

			if(newComponentImplementationDetailName != component_implementation_detail_id){
				if(newComponentImplementationDetailName != null || component_implementation_detail_id != "")
				{
					newComponentImplementationDetailName = null;
					newComponentImplementationDetailId = null;
					for(var i = 0; i < globalComponentData.length; i++){
						if(component_implementation_detail_id == globalComponentData[i].service_component.name + " " +
						globalComponentData[i].service_component_implementation.name + " " + globalComponentData[i].version){
							newComponentImplementationDetailId = globalComponentData[i].uuid;
							newComponentImplementationDetailName = component_implementation_detail_id;
							break;
						}
					}
				}
			}


			var params = {};

			var parts = window.location.href.split("/");
			var host = "https://" + parts[2];
			var url = "";

			if (this.props.source != null && this.props.source != "") {

				params["component_implementation_details_uuid"] = componentImplementationDetailId;
				params["new_component_implementation_details_uuid"] = newComponentImplementationDetailId;
				params["service_id"] = serviceId;
				params["new_service_id"] = newServiceId;
				params["service_version"] = serviceDetailsVersion;
				params["new_service_version"] = newServiceDetailsVersion;

				url = host + "/api/v1/component/service_details_component_implementation_details/edit";
				opType = "edit";
			}
			else {

				params["component_implementation_details_uuid"] = newComponentImplementationDetailId;
				params["service_id"] = newServiceId;
				params["service_version"] = newServiceDetailsVersion;

				url = host + "/api/v1/component/service_details_component_implementation_details/add";
				opType = "add";
			}


			this.serverRequest = $.ajax({
				url: url,
				dataType: "json",
				crossDomain: true,
				type: "POST",
				contentType: "application/json",
				cache: false,
				data: JSON.stringify(params),
				success: function (data) {
					if (opType == "add")
						$("#modal-success-body").text("You have successfully inserted a new service details component relationship");
					else {
						serviceId = newServiceId;
						serviceDetailsId = newServiceDetailsId;
						serviceDetailsVersion = newServiceDetailsVersion;
						componentImplementationDetailId = newComponentImplementationDetailId;
						$("#modal-success-body").text("You have successfully updated the service details component relationship");
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
		else {
		}

	},

	getInitialState: function () {
		return {
			data: {

			}
		}
	},

	componentDidMount: function () {

		if (this.props.source == null || this.props.source == "")
			return;

		jQuery.support.cors = true;
		this.serverRequest = $.ajax({
			url: this.props.source,
			dataType: "json",
			crossDomain: true,
			type: "GET",
			cache: false,
			success: function (data) {
				this.setState({data: data.data});
				$("#service_id").val(this.state.data.service.name);
				$("#service_details_id").val(this.state.data.service_details.service.name + " " + this.state.data.service_details.version);
				$("#component_implementation_detail_id").val(this.state.data.component_implementation_details.component.name +
				 " " + this.state.data.component_implementation_details.component_implementation.name + " " +
				this.state.data.component_implementation_details.version);

				serviceId = this.state.data.service.uuid;
				serviceDetailsId = this.state.data.service_details.uuid;
				componentImplementationDetailId = this.state.data.component_implementation_details.uuid;
				newServiceId = serviceId;
				newServiceDetailsId = serviceDetailsId;
				newComponentImplementationDetailId = componentImplementationDetailId;
				newServiceName = this.state.data.service.name;
				newServiceDetailsName = this.state.data.service_details.service.name + " " + this.state.data.service_details.version;
				newComponentImplementationDetailName = this.state.data.component_implementation_details.component.name +
				 " " + this.state.data.component_implementation_details.component_implementation.name + " " +
				this.state.data.component_implementation_details.version;
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

	render: function () {
		var formElements = this.generateFormElements(this.props.resourceObject);
		return (
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

		if (!($(event.target).parents().andSelf().is('#service_details_id'))) {
			$(".ui-menu-item").remove();
		}

		if (!($(event.target).parents().andSelf().is('#component_implementation_detail_id'))) {
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
				globalServiceData = data.data;
                response(data.data);
            });
	};

	var getDataServiceDetails = function(request, response){

        var url = window.location.href;
        var contents = url.split("/");
        var host = contents[0] + "//" + contents[2];


		var service = $("#service_id").val();
		if(service == null)
			service = "";

        $.getJSON(
            host + "/api/v1/services/version/all?search=" + request.term + "&service=" + service,
            function (data) {
				for(var i = 0; i < data.data.length; i++) {
					data.data[i].value = data.data[i].service.name + " " + data.data[i].version;
					data.data[i].label = data.data[i].version;
                    data.data[i].index = i;
				}
				globalServiceDetailsData = data.data;
                response(data.data);
            });
	};

    var getDataComponentImplementationDetail = function(request, response){

        var url = window.location.href;
        var contents = url.split("/");
        var host = contents[0] + "//" + contents[2];

        $.getJSON(
            host + "/api/v1/component/implementation_detail/all?search=" + request.term,
            function (data) {
				for(var i = 0; i < data.data.length; i++) {
					data.data[i].value = data.data[i].service_component.name + " " +
						data.data[i].service_component_implementation.name + " " + data.data[i].version;
					data.data[i].label = data.data[i].version;
                    data.data[i].index = i;
				}
				globalComponentData = data.data;
                response(data.data);
            });
	};


    $( "#service_id" ).autocomplete({
      source: getDataService,
      minLength: 2,
      select: function( event, ui ) {
		this.value = ui.item.name;
		newServiceId = ui.item.uuid;
		newServiceName = ui.item.name;
		$("#service_details_id").val(null);
		$(".ui-autocomplete").hide();
		$(".ui-menu-item").remove();
      },
	  change: function(event, ui){
		$("#service_details_id").val(null);
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

	$( "#service_details_id" ).autocomplete({
      source: getDataServiceDetails,
      minLength: 2,
      select: function( event, ui ) {
		this.value = ui.item.service.name + " " + ui.item.version;
		newServiceDetailsId = ui.item.uuid;
		newServiceDetailsName = ui.item.service.name + " " + ui.item.version;
		newServiceDetailsVersion = ui.item.version;
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
        .append( item.service.name + " " + item.version )
        .appendTo( ul );
    };

    $( "#component_implementation_detail_id" ).autocomplete({
      source: getDataComponentImplementationDetail,
      minLength: 2,
      select: function( event, ui ) {
		this.value = ui.item.service_component.name + " " + ui.item.service_component_implementation.name + " "
			+ ui.item.version;
		newComponentImplementationDetailId = ui.item.uuid;
		newComponentImplementationDetailName = ui.item.service_component.name + " " +
			ui.item.service_component_implementation.name + " " + ui.item.version;
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
        .append( item.service_component.name + " " + item.service_component_implementation.name + " " + item.version )
        .appendTo( ul );
    };


  } );