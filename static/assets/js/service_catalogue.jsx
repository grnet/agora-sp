var ServiceHeadline = React.createClass({

        	getInitialState: function(){
        		return {
        			title: "",
        			serviceArea: "",
        			shortDescription: "",
                    logo: ""
        		}
        	},

            render: function(){

                var logo = "/static/img/logos/" + this.props.logo;

                return (
                        <div className="col-lg-12 col-md-12 col-sm-12 col-xs-12">
                            <img className="logo col-lg-2 col-md-2 col-sm-2 col-xs-6 col-xs-offset-3 col-sm-offset-0 col-md-offset-0 col-lg-offset-0" src={logo} width="150" />
                            <div className="col-lg-10 col-md-10 col-sm-10 col-xs-12" id="service-name">
                                <h1 className="center-text-xs col-lg-12 col-md-12 col-sm-12 col-xs-8 col-sm-offset-0 col-xs-offset-2 col-md-offset-0 col-lg-offset-0">{this.props.title}</h1>
                                <h5 className="center-text-xs col-xs-8 col-xs-offset-2 col-lg-12 col-lg-offset-0 col-md-12 col-md-offset-0 col-sm-12 col-sm-offset-0" id="service-area">{this.props.serviceArea}</h5>
                            </div>
                        </div>
                );
            }
        });

        var ServiceDescription = React.createClass({

        	getInitialState: function(){
        		return {
        			descriptionExternal: ""
        		}
        	},

           render: function () {
               return (

                    <div className="col-lg-12" id="description" dangerouslySetInnerHTML={{__html: this.props.descriptionExternal}}>
                    </div>

               );
           }
        });

        var Separator = React.createClass({
           render: function () {
               return (
                 <hr className="separator col-lg-12 col-md-12 col-sm-12 col-xs-12" />
               );
           }
        });

        var ValueToCustomer = React.createClass({

        	getInitialState: function(){
        		return {
        			valueToCustomer: ""
        		}
        	},

           render: function () {
               return (
                    <div className="col-lg-12 col-md-12 col-sm-12 col-xs-12">
                        <h2>Value to customers</h2>
                        <p className="paragraph">
                            {this.props.valueToCustomer}
                        </p>
                    </div>
               );
           }
        });

        var FeatureWrapper = React.createClass({
            render: function () {
                return (
                        <div className="col-lg-3 col-md-4 col-sm-6 col-xs-12 center-features">
                            <img src="/static/assets/images/logos/logo-b2safe.png" width="80" className="col-lg-8 col-lg-offset-2 col-md-8 col-md-offset-2 col-sm-6 col-sm-offset-3 col-xs-6 col-xs-offset-3" />
                            <p className="col-lg-12 col-md-12 col-sm-12 col-xs-12 features">{this.props.data}</p>
                        </div>
                )
            }
        });


        var ServiceVersionWrapper = React.createClass({
           render: function () {
               return (
                   <div className="col-lg-12">
                       <h3 className="col-lg-12 col-md-12 col-sm-12 col-xs-12">{this.props.data.serviceName} {this.props.data.version}</h3>
                       <h4 className="col-lg-12 col-md-12 col-sm-12 col-xs-12">Status: <span className='active-status'> {this.props.data.service_status} </span></h4>

                       <div className="col-lg-12" id="description" dangerouslySetInnerHTML={{__html: this.props.data.features_current}}>
                       </div>

                        {/*<div className="wrapper col-lg-12">
                           {this.props.data.features_list.map(function(feature){
                               return <FeatureWrapper data={feature} />
                           })}
                       </div> */}

                       <div className="wrapper col-lg-12  col-md-12 links">
                           <div className="col-lg-12 col-md-12 col-sm-12 col-xs-12 evenAttribute"> Usage policy <a target="blank" href={this.props.data.usage_policy_link.related.href}>here</a> </div>
                           <div className="col-lg-12 col-md-12 col-sm-12 col-xs-12 oddAttribute"> User documentation  <a target="blank" href={this.props.data.user_documentation_link.related.href}>here</a> </div>
                           <div className="col-lg-12 col-md-12 col-sm-12 col-xs-12 oddAttribute"> Privacy policy <a target="blank" href={this.props.data.privacy_policy_link.related.href}>here</a> </div>



                            {/* <div className="col-lg-12 col-md-12 col-sm-12 col-xs-12 evenAttribute"> Monitoring link  <a target="blank" href={this.props.data.monitoring}>here</a></div>
                           <div className="col-lg-12 col-md-12 col-sm-12 col-xs-12 oddAttribute"> Operations documentaion link  <a target="blank" href={this.props.data.usage_policy}>here</a></div>*/}
                       </div>
                   </div>
               )
           }
        });

        var ServiceVersions = React.createClass({

            getInitialState: function () {
                return {
                    serviceDetails: [],
                    serviceName: ""
                }
            },

            render: function () {

            	var name = this.props.serviceName;
                return (
                    <div className="col-lg-12 col-md-12 col-sm-12 col-xs-12">
                        <h2>Service versions</h2>
                        <div id="versions">
                            {this.props.serviceDetails.map(function(serviceVersion){
                                return <ServiceVersionWrapper key={serviceVersion.version} data={serviceVersion} serviceName={name} />
                            })}
                        </div>
                    </div>
                )
            }
        });

        var RequestProcedures = React.createClass({

        	getInitialState: function(){
        		return {
        			requestProcedures: ""
        		}
        	},

            render: function () {
                return (
                        <div className="col-lg-12 col-md-12 col-sm-12 col-xs-12">
                            <h2>Request procedures</h2>
                            <p className="paragraph">{this.props.requestProcedures}</p>
                        </div>
                )
            }
        });

        var Contact = React.createClass({

        	getInitialState: function(){
        		return {
        			url: "",
        			email: ""
        		}
        	},

        	componentDidMount: function(){
        		this.serverRequest = $.ajax({
					url: this.props.source + "/contact_information",
					dataType: "json",
					crossDomain: true,
					type: "GET",
					cache: false,
					success: function(data){
						this.setState({url: data.data.external_contact_information.url, email: data.data.external_contact_information.email});

					}.bind(this),
					error: function(xhr, status, err){
						console.log(this.props.source, status, err.toString());
					}.bind(this)
				});
        	},

        	componentWillUnmount: function(){
				this.serverRequest.abort();
			},

           render: function () {
               return (
                   <div className="col-lg-12 col-md-12 col-sm-12 col-xs-12">
                        <h2>Contact information</h2>
                        <div className="wrapper">
                            <span>URL: <a target="blank" href={this.state.url}>{this.state.url}</a></span><br/>
                            <span>Email: {this.state.email}</span>
                        </div>
                   </div>
               )
           }
        });


        var UserCustomerWrapper = React.createClass({
           render: function () {
               return (
               		<div>
                   		<span className="col-lg-6 col-xs-6 oddAttribute">{this.props.data.name}</span> <span className="col-lg-6 col-xs-6 evenAttribute">{this.props.data.role}</span>
                   	</div>
               )
           }
        });

        var UserCustomers = React.createClass({

        	getInitialState: function(){
        		return {
        			userCustomers: []
        		}
        	},

            render: function () {

                return (
                        <div className="col-lg-12 col-md-12 col-sm-12 col-xs-12">
                            <h2>User Customers</h2>
                            <div className="wrapper">
                                <span className="col-lg-6 col-xs-6 oddAttribute"> Name</span>   <span className="col-lg-6 col-xs-6 evenAttribute">Role </span> <br />
                                {this.props.userCustomers.map(function(userCustomer){
                                	return <UserCustomerWrapper key={userCustomer.name} data={userCustomer} />
                                })}
                            </div>
                        </div>
                )
            }
        });


        var ServiceOwner = React.createClass({
            render: function () {
                return (
                        <div className="col-lg-12 col-md-12 col-sm-12 col-xs-12">
                            <h2>Service Owner</h2>
                            <div className="wrapper">
                                <span>Name: Ioannis Liabotis</span><br/>
                                <span>Email: iliaboti@grnet.gr</span>
                            </div>
                        </div>
                )
            }
        });



        var FundersForService = React.createClass({
            render: function () {
                return (
                        <div className="col-lg-12 col-md-12 col-sm-12 col-xs-12">
                            <h2>Funders for Service</h2>
                            <div className="wrapper">
                                <span>At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga.</span><br/>
                            </div>
                        </div>
                )
            }
        });

        var Risks = React.createClass({
            render: function () {
                return (
                        <div className="col-lg-12 col-md-12 col-sm-12 col-xs-12">
                            <h2>Risks</h2>
                            <div className="wrapper">
                                <span>At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga.</span><br/>
                            </div>
                        </div>
                )
            }
        });

        var Competitors = React.createClass({
            render: function () {
                return (
                        <div className="col-lg-12">
                            <h2>Competitors</h2>
                            <div className="wrapper">
                                <span>At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga.</span><br/>
                            </div>
                        </div>
                )
            }
        });

        var OptionWrapper = React.createClass({

            getInitialState: function(){
                return {
                    data: {
                        name: "",
                        description: ""
                    }
                }
            },

           render: function () {

               return (
                   <div className="options col-lg-12 col-md-12 col-sm-12 col-xs-12">
                       <img src="/static/assets/images/logos/logo-b2safe.png" className="col-lg-1 col-md-1 col-sm-1 col-xs-6 col-xs-offset-3 col-sm-offset-0" />
                       <div className="col-lg-11 col-md-11 col-sm-11 col-xs-12 center-text-xs">
                           <h3 className="col-lg-12 option-name">{this.props.data.name}</h3>
                           <div className="features col-xs-12">
                               <p className="col-lg-9 col-md-9 col-sm-9 center-text-xs padding-left-0">{this.props.data.description}</p>
                           </div>
                       </div>
                   </div>
               )
           }
        });

        var Options = React.createClass({
           getInitialState: function () {
               return {
                       serviceOptions: [

                       ]

               }
           },

            componentDidMount: function(){
        		this.serverRequest = $.ajax({
					url: this.props.source + "/service_options",
					dataType: "json",
					crossDomain: true,
					type: "GET",
					cache: false,
					success: function(data){

						this.setState({serviceOptions: data.data.options});

					}.bind(this),
					error: function(xhr, status, err){
						console.log(this.props.source, status, err.toString());
					}.bind(this)
				});
        	},

        	componentWillUnmount: function(){
				this.serverRequest.abort();
			},

            render: function () {
                return (
                    <div className="col-lg-12 col-md-12 col-sm-12 col-xs-12">
                        <h2>Service options</h2>
                        <div className="wrapper">
                            {this.state.serviceOptions.map(function(option){
                                return <OptionWrapper key={option.name} data={option} />
                            })}
                        </div>
                    </div>
                )
            }
        });


        var ServicePage = React.createClass({

			getInitialState: function(){
				return {
					data: {
						name: "",
						service_area: "",
						description_external: "",
						user_customers_list: {
							user_customers: []
						},
						value_to_customer: "",
						request_procedures: "",
						service_details_list: {
							service_details: []
						}
					}
				};
			},

			componentDidMount: function(){
				jQuery.support.cors = true;
				this.serverRequest = $.ajax({
					url: this.props.source,
					dataType: "json",
					crossDomain: true,
					type: "GET",
					cache: false,
					success: function(data){
						this.setState({data: data.data});
					}.bind(this),
					error: function(xhr, status, err){
						console.log(this.props.source, status, err.toString());
					}.bind(this)
				});
			},

			componentWillUnmount: function(){
				this.serverRequest.abort();
			},

           render: function () {
                return (
                        <div>
                            <ServiceHeadline title={this.state.data.name} serviceArea={this.state.data.service_area} shortDescription="Sample short description" logo={this.state.data.logo} />
                            <ServiceDescription descriptionExternal={this.state.data.description_external} />
                            <Separator />
                            <UserCustomers userCustomers={this.state.data.user_customers_list.user_customers} />
                            <Separator />
                            <ValueToCustomer valueToCustomer={this.state.data.value_to_customer} />
                            <Separator />
                            <ServiceVersions serviceDetails={this.state.data.service_details_list.service_details} serviceName={this.state.data.name} />
                            <Separator />
                            <Options source={this.props.source} />
                            <Separator />
                            <RequestProcedures requestProcedures={this.state.data.request_procedures} />
                            <Separator />
                            <Contact source={this.props.source} />
                            <Separator />
                        </div>
                );
           }
        });


        var service_name = window.location.href.split("/");

        if(service_name[service_name.length - 1] == "")
            service_name = service_name[service_name.length - 2];
        else
            service_name = service_name[service_name.length - 1];

        var source = "http://localhost/api/v1/portfolio/services/" + service_name;

        ReactDOM.render(
                <ServicePage source={source} />,
                document.getElementById('content')
        );