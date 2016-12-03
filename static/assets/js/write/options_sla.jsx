
var formName = 'Options SLA Form';

var serviceOptionId = null;
var opType = "";
var slaId;
var globalData;

var optionsData = [
  {id: 1, value: -1, text: "Select service option"}
];

var resourceObject = [
	{ tag: 'input', type: 'text', name: 'name', placeholder: 'Enter name', label: 'Name' },	
	{ tag: 'select', type: 'text', name: 'service_option_id', label: 'Service Option', placeholder: "Enter service option name", optionsData: optionsData }
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

var parameter = getParameterByName("serviceOptionId", window.location);
if(parameter != null) {
	serviceOptionId = parameter;
	jQuery.support.cors = true;
        $.ajax({
            url: $("#host")[0].value + "/api/v1/options/service_options/" + serviceOptionId,
			headers: {
				"X-CSRFToken": $("input[name=csrfmiddlewaretoken]")[0].value,
				"AUTH_TOKEN": localStorage.apiToken,
				"EMAIL": localStorage.apiEmail
			},
            dataType: "json",
            crossDomain: true,
            type: "GET",
            cache: false,
            success: function (response) {
				var name = response.data.name;

				var options = $("#service_option_id");
				var optionsCount = $("#service_option_id>option").length;
				if(optionsCount <= 1){
					var option = $('<option></option>').attr("value", name)
							.text(name);
						options.append(option);
				}
				options.val(name).change();
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
		if($('#name').val() == ''){
			validationMessage = "The name is required"
			validationObjects.push( { field: 'name', message: validationMessage } );
		}
		if($('#name').val().length > 255){
			validationMessage = "Content exceeds max length of 255 characters."
			validationObjects.push( { field: 'name', message: validationMessage } );			
		}

		var serv_op_id = $("#service_option_id").val();
		if(serv_op_id == null || serv_op_id == "" || serv_op_id == -1){
			validationMessage = "The service option is required"
			validationObjects.push( { field: 'service_option_id', message: validationMessage } );
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

			var service_option_id =  $("#service_option_id").val();

			if(service_option_id != "")
			{
				serviceOptionId = null;
				for(var i = 0; i < globalData.length; i++){
					if(service_option_id == globalData[i].name){
						serviceOptionId = globalData[i].uuid;
						break;
					}
				}
			}



			var params = {};
			params["name"] = $("#name").val();
			params["service_option_uuid"] = serviceOptionId;


			var parts = window.location.href.split("/");
			var host = "http://" + parts[2];
			var url = "";

			if(this.props.source != null && this.props.source != ""){
				params["uuid"] = parts[parts.length - 1];
				url = host + "/api/v1/options/SLAs/edit";
				opType = "edit";
			}
			else {
				url = host + "/api/v1/options/SLAs/add";
				opType = "add";
			}

			this.serverRequest = $.ajax({
				url: url,
				headers: {
					"X-CSRFToken": $("input[name=csrfmiddlewaretoken]")[0].value,
					"AUTH_TOKEN": localStorage.apiToken,
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
						$("#modal-success-body").text("You have successfully inserted a new SLA");
					else
						$("#modal-success-body").text("You have successfully updated the SLA");
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

var ParametersTable = React.createClass({


	getInitialState: function () {
		return {
			parameters: [],
			count: 0,
			selected: 0
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
			      	        <button value="Add parameter" id="add-sla-param" className="btn btn-purple">Add SLA parameter</button>
			      	    </div>
						<table className="table table-hover">
							<thead className="bordered-darkorange">
								<tr>
									<th>
										Name
									</th>
									<th>
										Type
									</th>
									<th>
										Expression
									</th>

									<th>

									</th>
								</tr>
							</thead>
							<tbody>

							{this.props.parameters.map(function (parameter) {
								return (
									<tr key={parameter.uuid}>
										<td>{parameter.name}</td>
										<td>{parameter.type}</td>
										<td>{parameter.expression}</td>
										<td><a href={"/ui/options/parameter/" + parameter.uuid}>Edit</a></td>
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
			sla: {
				name: ""
			},
			parameters: []
		}
	},

    componentDidMount: function () {


		jQuery.support.cors = true;
		var url = window.location.href;
        var contents = url.split("/");
        var host = contents[0] + "//" + contents[2];

		$.getJSON(
            host + "/api/v1/options/service_options/all",
            function (data) {
				var serv_opt_id = $("#service_option_id");
				var current = serv_opt_id.val();

				if(current != -1){
					$("#service_option_id option[value='" + current + "']").remove();
				}
				for(var i = 0; i < data.data.length; i++) {
					var option = $('<option></option>').attr("value", data.data[i].name).text(data.data[i].name);
					serv_opt_id.append(option);

				}
				if(current != -1)
					serv_opt_id.val(current).change();

				globalData = data.data;

            });

        if(this.props.source == null || this.props.source == "")
            return;

        jQuery.support.cors = true;
        this.serverRequest = $.ajax({
            url: this.props.source,
			headers: {
				"X-CSRFToken": $("input[name=csrfmiddlewaretoken]")[0].value,
				"AUTH_TOKEN": localStorage.apiToken,
				"EMAIL": localStorage.apiEmail
			},
            dataType: "json",
            crossDomain: true,
            type: "GET",
            cache: false,
            success: function (data) {
                this.setState({sla: data.data});
                $("#name").val(this.state.sla.name);

				var service_option = $("#service_option_id");
				var optionsCount = $("#service_option_id>option").length;
				if(optionsCount <= 1){
					var option = $('<option></option>').attr("value", this.state.sla.service_option.name)
							.text(this.state.sla.service_option.name);
						service_option.append(option);
				}
				service_option.val(this.state.sla.service_option.name).change();

				serviceOptionId = this.state.sla.service_option.uuid;
				slaId = this.state.sla.id;

				var self = this;
				$.ajax({
					url: host + "/api/v1/options/parameters_for_sla/" + slaId,
					headers: {
						"X-CSRFToken": $("input[name=csrfmiddlewaretoken]")[0].value,
						"AUTH_TOKEN": localStorage.apiToken,
						"EMAIL": localStorage.apiEmail
					},
					dataType: "json",
					crossDomain: true,
					type: "GET",
					cache: false,
					success: function (data) {
						self.setState({parameters: data.data});
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
							<span className="widget-caption">SLA</span>
						</div>

						<div className="widget-body">
							<div className="widget-main ">
								<div className="tabbable">
									<ul className="nav nav-tabs tabs-flat" id="myTab11">
										<li className="active">
											<a data-toggle="tab" href="#home11">
												SLA
											</a>
										</li>
										<li>
											<a data-toggle="tab" href="#profile12">
												Parameters
											</a>
										</li>
									</ul>
									<div className="tab-content tabs-flat">
										<div id="home11" className="tab-pane in active">
											<FormWrapper resourceObject={resourceObject} formName={formName} source={this.props.source} />
										</div>

										<div id="profile12" className="tab-pane">
											<ParametersTable parameters={this.state.parameters} />
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

	$("#add-sla-param").click(function(){
		window.open("/ui/options/sla_parameter?slaId=" + slaId, "_blank");
	});

});
