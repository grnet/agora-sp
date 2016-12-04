
var formName = 'Service Component Form';
var opType = "";
var componentId;
var implementations;

var optionsData = [
  {id: 1, value: 1, text: "option 1"},
  {id: 2, value: 2, text: "option 2"},
	{id: 3, value: 3, text: "option 3"}
];

var resourceObject = [
	{ tag: 'input', type: 'text', name: 'name', placeholder: 'Enter name', label: 'Name' },
	{ tag: 'textarea', type: 'textarea', name: 'description', label: 'Description', placeholder: 'Enter description',
        onChange: 'textareaHTMLValidation' },
	{tag: 'button', type: 'button', name: 'edit-description', label: 'Edit', value: "Edit"}
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
		var validationMessage = ''
		if($('#name').val() == ''){
			validationMessage = "The name is required"
			validationObjects.push( { field: 'name', message: validationMessage } );
		}
		if($('#name').val().length > 255){
			validationMessage = "Content exceeds max length of 255 characters."
			validationObjects.push( { field: 'name', message: validationMessage } );			
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

			var params = {};
			params["name"] = $("#name").val();
			params["description"] = $("#description").val();


			var parts = window.location.href.split("/");
			var host = "https://" + parts[2];
			var url = "";

			if(this.props.source != null && this.props.source != ""){
				params["uuid"] = parts[parts.length - 1];
				url = host + "/api/v1/component/edit";
				opType = "edit";
			}
			else {
				url = host + "/api/v1/component/add";
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
						$("#modal-success-body").text("You have successfully inserted a new component");
					else
						$("#modal-success-body").text("You have successfully updated the component");
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


var ImplementationTable = React.createClass({


	getInitialState: function () {
		return {
			implementations: [],
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
			      	        <button value="Add component implementation" id="add-imp" className="btn btn-purple">Add component implementation</button>
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

									</th>
								</tr>
							</thead>
							<tbody>

							{this.props.implementations.map(function (implementation) {
								return (
									<tr key={implementation.name}>
										<td>{implementation.name}</td>
										<td>{implementation.description}</td>
										<td><a href={"/ui/component/implementation/" + implementation.uuid}>Edit</a></td>
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


var ImplementationDetailsTable = React.createClass({


	getInitialState: function () {
		return {
			implementationsDetails: [],
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
			      	        <button value="Add component implementation details" id="add-imp-det" className="btn btn-purple">Add component implementation details</button>
			      	    </div>
						<table className="table table-hover">
							<thead className="bordered-darkorange">
								<tr>
									<th>
										Version
									</th>
									<th>
										Configuration Parameters
									</th>

									<th>

									</th>
								</tr>
							</thead>
							<tbody>

							{this.props.implementationsDetails.map(function (implementation) {
								return (
									<tr key={implementation.version}>
										<td>{implementation.version}</td>
										<td>{implementation.configuration_parameters}</td>
										<td><a href={"/ui/component/implementation_detail/" + implementation.uuid}>Edit</a></td>
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
			component: {
				name: "",
				description: ""
			},
			implementations: [],
			implementationsDetails: []
		}
	},

    componentDidMount: function () {

        if(this.props.source == null || this.props.source == "")
            return;

        jQuery.support.cors = true;
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
                this.setState({component: data.data});
                $("#name").val(this.state.component.name);
                $("#description").val(this.state.component.description);
				componentId = this.state.component.uuid;
				this.setState({implementations: this.state.component.component_implementations_list.component_implementations});

				var seen = {};
				var details = [];
				for(var i = 0; i < this.state.component.component_implementations_list.count; i++){
					var imp = this.state.component.component_implementations_list.component_implementations[i];

					for(var j = 0; j < imp.component_implementation_details_list.count; j++){
						var imp_det = imp.component_implementation_details_list.component_implementation_details[j];

						if(seen[imp_det.uuid])
							continue;

						seen[imp_det.uuid] = true;
						details.push(imp_det);
					}
				}

				this.setState({implementationsDetails: details});

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
							<span className="widget-caption">Component</span>
						</div>

						<div className="widget-body">
							<div className="widget-main ">
								<div className="tabbable">
									<ul className="nav nav-tabs tabs-flat" id="myTab11">
										<li className="active">
											<a data-toggle="tab" href="#home11">
												Component
											</a>
										</li>
										<li>
											<a data-toggle="tab" href="#profile11">
												Implementations
											</a>
										</li>
										<li>
											<a data-toggle="tab" href="#profile12">
												Implementations Details
											</a>
										</li>
									</ul>
									<div className="tab-content tabs-flat">
										<div id="home11" className="tab-pane in active">
											<FormWrapper resourceObject={resourceObject} formName={formName} source={this.props.source} />
										</div>

										<div id="profile11" className="tab-pane">
											<ImplementationTable implementations={this.state.implementations} />
										</div>

										<div id="profile12" className="tab-pane">
											<ImplementationDetailsTable implementationsDetails={this.state.implementationsDetails} />
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

	$("#add-imp").click(function () {
		//window.location = "/ui/component/implementation?componentId=" + componentId;
		window.open("/ui/component/implementation?componentId=" + componentId, "_blank");
	});

	$("#add-imp-det").click(function () {
		window.open("/ui/component/implementation_detail?componentId=" + componentId, "_blank");
	});

	$("#btn-edit-description").click(function(e){
		e.preventDefault();
		tinymce.init({
			selector:'#rich-edit',
			height: 250
		});
		tinymce.get('rich-edit').setContent($("#description").val());
		$("#modal-rich-html").modal('show');
	});

	$("#confirm-edit").click(function () {
		$("#description").val(tinymce.get('rich-edit').getContent());
	});

});