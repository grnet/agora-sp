
var formName = 'Service Owner Form';

var institutionId = null;
var institutionName = null;
var opType = "";
var globalData;

var optionsData = [
  {id: 1, value: 1, text: "option 1"},
  {id: 2, value: 2, text: "option 2"},
	{id: 3, value: 3, text: "option 3"}
];

var booleanData = [
  {id: 1, value: 1, text: "yes"},
  {id: 0, value: 0, text: "no"}
];

var resourceObject = [
	{ tag: 'input', type: 'text', name: 'first_name', placeholder: 'Enter first name', label: 'First Name' },
	{ tag: 'input', type: 'text', name: 'last_name', placeholder: 'Enter last name', label: 'Last Name' },
	{ tag: 'input', type: 'text', name: 'email', placeholder: 'Enter email', label: 'Email' },
	{ tag: 'input', type: 'text', name: 'phone', placeholder: 'Enter phone', label: 'Phone' },
	{ tag: 'input', type: 'text', name: 'institution_id', placeholder: 'Enter institution', label: 'Institution' }
	//{ tag: 'select', type: 'select', name: 'account_id', label: 'Account', optionsData: optionsData }
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

	validateEmail: function(email) {
	    var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
	    return re.test(email);
	},

	validatePhone: function(phone) {
		var re = /^\d+$/
		return re.test(phone)
	},

	validateForm: function(e){
		this.clearValidations();
		var validationObjects = [];
		var validationMessage = ''

		// --- validation code goes here ---
		if($('#email').val() == ''){
			validationMessage = "The email is required"
			validationObjects.push( { field: 'email', message: validationMessage } );
		}
		if(!this.validateEmail($('#email').val())){
			validationMessage = "Content is not a valid email"
			validationObjects.push( { field: 'email', message: validationMessage } );
		}
		if($('#first_name').val().length > 255){
			validationMessage = "Content exceeds max length of 255 characters."
			validationObjects.push( { field: 'first_name', message: validationMessage } );			
		}
		if($('#last_name').val().length > 255){
			validationMessage = "Content exceeds max length of 255 characters."
			validationObjects.push( { field: 'last_name', message: validationMessage } );
		}


		var phone = $("#phone").val();
		if(phone != null && phone != "" && !this.validatePhone(phone)){
			validationMessage = "Phone field must contain numbers only."
			validationObjects.push( { field: 'phone', message: validationMessage } );
		}

		if(phone.length > 255){
			validationMessage = "Content exceeds max length of 255 characters."
			validationObjects.push( { field: 'phone', message: validationMessage } );
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


			var institution_id =  $("#institution_id").val();

			if(institutionName != institution_id){
				if(institutionName != null || institution_id != "")
				{
					institutionName = null;
					institutionId = null;
					for(var i = 0; i < globalData.length; i++){
						if(institution_id == globalData[i].name){
							institutionId = globalData[i].uuid;
							institutionName = institution_id;
							break;
						}
					}
				}
			}

			var params = {};
			params["first_name"] = $("#first_name").val();
			params["last_name"] = $("#last_name").val();
			params["email"] = $("#email").val();
			params["phone"] = $("#phone").val();
			params["institution_uuid"] = institutionId;



			var parts = window.location.href.split("/");
			var host = "http://" + parts[2];
			var url = "";

			if(this.props.source != null && this.props.source != ""){
				params["uuid"] = parts[parts.length - 1];
				url = host + "/api/v1/owner/edit";
				opType = "edit";
			}
			else {
				url = host + "/api/v1/owner/add";
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
						$("#modal-success-body").text("You have successfully inserted a new service owner");
					else
						$("#modal-success-body").text("You have successfully updated the service owner");
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
			service_owner: {
				first_name: "",
				last_name: "",
				email: "",
				phone: ""
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
                this.setState({service_owner: data.data});
                $("#first_name").val(this.state.service_owner.first_name);
                $("#last_name").val(this.state.service_owner.last_name);
                $("#email").val(this.state.service_owner.email);
                $("#phone").val(this.state.service_owner.phone);
				$("#institution_id").val(this.state.service_owner.institution.name);
				institutionId = this.state.service_owner.institution.uuid;
				institutionName = this.state.service_owner.institution.name;
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
        if (!($(event.target).parents().andSelf().is('#institution_id'))) {
			$(".ui-menu-item").remove();
		}});




	var getData = function(request, response){

        var url = window.location.href;
        var contents = url.split("/");
        var host = contents[0] + "//" + contents[2];

		$.getJSON(
            host + "/api/v1/owner/institution/all?search=" + request.term,
            function (data) {
				for(var i = 0; i < data.data.length; i++) {
					data.data[i].value = data.data[i].name;
					data.data[i].label = data.data[i].name;
                    data.data[i].index = i;
				}
				globalData = data.data;
                response(data.data);
            });
	};


    $( "#institution_id" ).autocomplete({
      source: getData,
      minLength: 2,
      select: function( event, ui ) {
		this.value = ui.item.name;
		institutionId = ui.item.uuid;
		institutionName = ui.item.name;
		$(".ui-autocomplete").hide();
		$(".ui-menu-item").remove();
      },
	  change: function(event, ui){
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