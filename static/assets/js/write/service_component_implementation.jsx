
var formName = 'Service Component Implementation Form';

var componentId = null;
var opType = "";
var globalData;

var optionsData = [
  {id: 1, value: -1, text: "Select component"}
];

var resourceObject = [
	{ tag: 'input', type: 'text', name: 'name', placeholder: 'Enter name', label: 'Name' },
	{ tag: 'textarea', type: 'textarea', name: 'description', label: 'Description', placeholder: "Enter description", onChange: 'textareaHTMLValidation' },
	{ tag: 'select', type: 'text', name: 'component_id', label: 'Component', placeholder: "Enter component name", optionsData: optionsData }
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

//function getParameterByName(name, url) {
//    if (!url) url = window.location.href;
//    name = name.replace(/[\[\]]/g, "\\$&");
//    var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
//        results = regex.exec(url);
//    if (!results) return null;
//    if (!results[2]) return '';
//    return decodeURIComponent(results[2].replace(/\+/g, " "));
//}
//
//var parameter = getParameterByName("componentId", window.location);
//if(parameter != null) {
//	componentId = parameter;
//	console.log(componentId);
//	jQuery.support.cors = true;
//        $.ajax({
//            url: $("#host")[0].value + "/api/v1/component/" + componentId,
//            dataType: "json",
//            crossDomain: true,
//            type: "GET",
//            cache: false,
//            success: function (response) {
//				$("#component_id").val(response.data.name);
//				componentName = response.data.name;
//            },
//            error: function (xhr, status, err) {
//                console.log(this.props.source, status, err.toString());
//            }
//        });
//}
//
//var email;
//var token;
//
//function getCookie(cname) {
//    var name = cname + "=";
//    var ca = document.cookie.split(';');
//    for(var i = 0; i <ca.length; i++) {
//        var c = ca[i];
//        while (c.charAt(0)==' ') {
//            c = c.substring(1);
//        }
//        if (c.indexOf(name) == 0) {
//            return c.substring(name.length,c.length);
//        }
//    }
//    return "";
//}
//
//var t = getCookie("api-credentials");
//t = t.split("-");
//token = t[0];
//email = t[1];

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
					    <textarea className="form-control" id={field.name} name={field.name} placeholder={field.placeholder} rows="6" onChange={this[field.onChange]}></textarea>
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
			validationMessage = "The name is required";
			validationObjects.push( { field: 'name', message: validationMessage } );
		}
		if($('#name').val().length > 255){
			validationMessage = "Content exceeds max length of 255 characters.";
			validationObjects.push( { field: 'name', message: validationMessage } );			
		}

		var comp_id = $('#component_id').val();
		if(comp_id == null || comp_id == "" || comp_id == -1){
			validationMessage = "The component is required.";
			validationObjects.push( { field: 'component_id', message: validationMessage } );
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

			var component_id =  $("#component_id").val();

			if(component_id != "")
			{
				componentId = null;
				for(var i = 0; i < globalData.length; i++){
					if(component_id == globalData[i].name){
						componentId = globalData[i].uuid;
						break;
					}
				}
			}



			var params = {};
			params["name"] = $("#name").val();
			params["description"] = $("#description").val();
			params["component_uuid"] = componentId;


			var parts = window.location.href.split("/");
			var host = "http://" + parts[2];
			var url = "";

			if(this.props.source != null && this.props.source != ""){
				params["uuid"] = parts[parts.length - 1];
				url = host + "/api/v1/component/service_component_implementation/edit";
				opType = "edit";
			}
			else {
				url = host + "/api/v1/component/service_component_implementation/add";
				opType = "add";
			}

			this.serverRequest = $.ajax({
				url: url,
				headers: {
					"X-CSRFToken": $("input[name=csrfmiddlewaretoken]")[0].value,
					//"AUTH_TOKEN": token,
					//"EMAIL": email
				},
				dataType: "json",
				crossDomain: true,
				type: "POST",
				contentType:"application/json",
				cache: false,
				data: JSON.stringify(params),
				success: function (data) {
					if(opType == "add")
						$("#modal-success-body").text("You have successfully inserted a new component implementation");
					else
						$("#modal-success-body").text("You have successfully updated the component implementation");
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
			component: {
				name: "",
				description: ""
			}
		}
	},

    componentDidMount: function () {


		jQuery.support.cors = true;
		var url = window.location.href;
        var contents = url.split("/");
        var host = contents[0] + "//" + contents[2];

		$.getJSON(
            host + "/api/v1/component/all",
            function (data) {
				var component_id = $("#component_id");
				var current = component_id.val();

				if(current != -1){
					$("#component_id option[value='" + current + "']").remove();
				}
				for(var i = 0; i < data.data.length; i++) {
					var option = $('<option></option>').attr("value", data.data[i].name).text(data.data[i].name);
					component_id.append(option);

				}
				if(current != -1)
					component_id.val(current).change();

				globalData = data.data;

            });


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
                this.setState({component: data.data});
                $("#name").val(this.state.component.name);
                $("#description").val(this.state.component.description);

				var component = $("#component_id");
				var optionsCount = $("#component_id>option").length;
				if(optionsCount <= 1){
					var option = $('<option></option>').attr("value", this.state.component.component.name)
							.text(this.state.component.component.name);
						component.append(option);
				}
				component.val(this.state.component.component.name).change();
				componentId = this.state.component.component.uuid;
            }.bind(this),
            error: function (xhr, status, err) {
            }.bind(this)
        });

        //this.serverRequest = $.ajax({
        //    url: this.props.source,
        //    dataType: "json",
        //    crossDomain: true,
        //    type: "GET",
        //    cache: false,
        //    success: function (data) {
        //
        //    }.bind(this),
        //    error: function (xhr, status, err) {
        //        console.log(this.props.source, status, err.toString());
        //    }.bind(this)
        //});
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