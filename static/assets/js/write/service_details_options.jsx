
var formName = 'Service Details Options Form';


var serviceId = null;
var serviceDetailsId = null;
var serviceOptionsId = null;
var newServiceId = null;
var newServiceDetailsId = null;
var newServiceOptionsId = null;
var newServiceName = null;
var newServiceDetailsName = null;
var newServiceOptionsName = null;
var newServiceDetailsVersion = null;
var serviceDetailsVersion = null;
var opType = "";
var globalServiceData;
var globalServiceDetailsData;
var globalOptionsData;

var optionsData = [
  {id: 1, value: 1, text: "option 1"},
  {id: 2, value: 2, text: "option 2"},
	{id: 3, value: 3, text: "option 3"}
];

var resourceObject = [
	{ tag: 'input', type: 'text', name: 'service_id', placeholder: 'Enter service name', label: 'Service name' },
	{ tag: 'input', type: 'text', name: 'service_details_id', placeholder: 'Enter service version', label: 'Service version' },
	{ tag: 'input', type: 'text', name: 'service_options_id', placeholder: 'Enter service option name', label: 'Service option' }
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
		if (service == '' || service == null) {
			validationMessage = "The service is required";
			validationObjects.push({field: 'service_id', message: validationMessage});
		}

		var service_details = $('#service_details_id').val();
		if (service_details == null || service_details == "") {
			validationMessage = "The service version is required.";
			validationObjects.push({field: 'service_details_id', message: validationMessage});
		}

		var service_option = $("#service_options_id").val();
		if(service_option == null || service_option == ""){
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

			var service_options_id =  $("#service_options_id").val();

			if(newServiceOptionsName != service_options_id){
				if(newServiceOptionsName != null || service_options_id != "")
				{
					newServiceOptionsName = null;
					newServiceOptionsId = null;
					for(var i = 0; i < globalOptionsData.length; i++){
						if(service_options_id == globalOptionsData[i].name){
							newServiceOptionsId = globalOptionsData[i].uuid;
							newServiceOptionsName = service_options_id;
							break;
						}
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
                this.setState({data: data.data});
				$("#service_id").val(this.state.data.service.name);
				$("#service_details_id").val(this.state.data.service.name + " " + this.state.data.service_details.version);
				$("#service_options_id").val(this.state.data.service_options.name);

				serviceId = this.state.data.service.uuid;
				serviceDetailsId = this.state.data.service_details.uuid;
				serviceOptionsId = this.state.data.service_options.uuid;
				newServiceId = serviceId;
				newServiceDetailsId = serviceDetailsId;
				newServiceOptionsId = serviceOptionsId;
				newServiceName = this.state.data.service.name;
				newServiceDetailsName = this.state.data.service_details.service.name + " " + this.state.data.service_details.version;
				newServiceOptionsName = this.state.data.service_options.name;
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

		if (!($(event.target).parents().andSelf().is('#service_options_id'))) {
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

    var getDataServiceOptions = function(request, response){

        var url = window.location.href;
        var contents = url.split("/");
        var host = contents[0] + "//" + contents[2];

        $.getJSON(
            host + "/api/v1/options/service_options/all?search=" + request.term,
            function (data) {
				for(var i = 0; i < data.data.length; i++) {
					data.data[i].value = data.data[i].name;
					data.data[i].label = data.data[i].name;
                    data.data[i].index = i;
				}
				globalOptionsData = data.data;
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
		this.value = ui.item.name;
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

    $( "#service_options_id" ).autocomplete({
      source: getDataServiceOptions,
      minLength: 2,
      select: function( event, ui ) {
		this.value = ui.item.name;
		newServiceOptionsId = ui.item.uuid;
		newServiceOptionsName = ui.item.name;
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
        .append( item.name  )
        .appendTo( ul );
    };


  } );