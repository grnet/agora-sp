var ServiceHeadline = React.createClass({

    getInitialState: function () {
        return {
            title: "",
            serviceArea: "",
            shortDescription: "",
            logo: ""
        }
    },

    render: function () {

        var logo = "http://snf-715140.vm.okeanos.grnet.gr/static/img/logos/" + this.props.logo;

        return (
            <div className="col-lg-12 col-md-12 col-sm-12 col-xs-12" id="service-headline">
                <img
                    className="logo col-lg-2 col-md-2 col-sm-2 col-xs-6 col-xs-offset-3 col-sm-offset-0 col-md-offset-0 col-lg-offset-0"
                    src={logo} width="150"/>
                <div className="col-lg-10 col-md-10 col-sm-10 col-xs-12" id="service-name">
                    <h1 className="center-text-xs col-lg-12 col-md-12 col-sm-12 col-xs-8 col-sm-offset-0 col-xs-offset-2 col-md-offset-0 col-lg-offset-0">{this.props.title}</h1>
                    <h5 className="center-text-xs col-xs-8 col-xs-offset-2 col-lg-12 col-lg-offset-0 col-md-12 col-md-offset-0 col-sm-12 col-sm-offset-0"
                        id="service-area">{this.props.serviceArea}</h5>
                </div>

                <hr className="separator col-lg-12 col-md-12 col-sm-12 col-xs-12"/>
            </div>
        );
    }
});

var ServiceDescription = React.createClass({

    getInitialState: function () {
        return {
            descriptionExternal: ""
        }
    },

    render: function () {
        return (
            <div>
                <div className="col-lg-12" id="description"
                     dangerouslySetInnerHTML={{__html: this.props.descriptionExternal}}>
                </div>
                <hr className="separator col-lg-12 col-md-12 col-sm-12 col-xs-12"/>
            </div>

        );
    }
});

var Separator = React.createClass({
    render: function () {
        return (
            <div></div>
        );
    }
});


var ValueToCustomer = React.createClass({

    getInitialState: function () {
        return {
            valueToCustomer: ""
        }
    },

    render: function () {
        return (
            <div
                className={type == 'catalogue' && (this.props.valueToCustomer == null || this.props.valueToCustomer.length < 0) ? 'collapse' : ''}>
                <div className="col-lg-12 col-md-12 col-sm-12 col-xs-12">
                    <h2>Value to customers</h2>
                    <p className="paragraph">
                        {this.props.valueToCustomer}
                    </p>
                </div>

                <hr className="separator col-lg-12 col-md-12 col-sm-12 col-xs-12"/>
            </div>

        );
    }
});


var FeatureWrapper = React.createClass({
    render: function () {
        return (
            <div className="col-lg-3 col-md-4 col-sm-6 col-xs-12 center-features">
                <img src="/static/assets/images/logos/logo-b2safe.png" width="80"
                     className="col-lg-8 col-lg-offset-2 col-md-8 col-md-offset-2 col-sm-6 col-sm-offset-3 col-xs-6 col-xs-offset-3"/>
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
                <h4 className="col-lg-12 col-md-12 col-sm-12 col-xs-12">Status: <span
                    className='active-status'> {this.props.data.service_status} </span></h4>

                <div className="col-lg-12" id="description"
                     dangerouslySetInnerHTML={{__html: this.props.data.features_current}}>
                </div>

                {/*<div className="wrapper col-lg-12">
                 {this.props.data.features_list.map(function(feature){
                 return <FeatureWrapper data={feature} />
                 })}
                 </div> */}

                <div className="wrapper col-lg-12  col-md-12 links">
                    <div className="col-lg-12 col-md-12 col-sm-12 col-xs-12 evenAttribute"> Usage policy <a
                        target="blank" href={this.props.data.usage_policy_link.related.href}>here</a></div>
                    <div className="col-lg-12 col-md-12 col-sm-12 col-xs-12 oddAttribute"> User documentation <a
                        target="blank" href={this.props.data.user_documentation_link.related.href}>here</a></div>
                    <div className="col-lg-12 col-md-12 col-sm-12 col-xs-12 oddAttribute"> Privacy policy <a
                        target="blank" href={this.props.data.privacy_policy_link.related.href}>here</a></div>


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
                    {this.props.serviceDetails.map(function (serviceVersion) {
                        return <ServiceVersionWrapper key={serviceVersion.version} data={serviceVersion}
                                                      serviceName={name}/>
                    })}
                </div>

                <hr className="separator col-lg-12 col-md-12 col-sm-12 col-xs-12"/>
            </div>
        )
    }
});

var RequestProcedures = React.createClass({

    getInitialState: function () {
        return {
            requestProcedures: ""
        }
    },

    render: function () {
        return (
            <div
                className={type == 'catalogue' && (this.props.requestProcedures == null || this.props.requestProcedures.length < 0) ? 'collapse' : ''}>
                <div id="service-request" className="col-lg-12 col-md-12 col-sm-12 col-xs-12">
                    <h2>Request procedures</h2>
                    <p className="paragraph">{this.props.requestProcedures}</p>
                </div>

                <hr className="separator col-lg-12 col-md-12 col-sm-12 col-xs-12"/>
            </div>

        )
    }
});

var Contact = React.createClass({

    getInitialState: function () {
        return {
            url: "",
            email: ""
        }
    },

    componentDidMount: function () {
        this.serverRequest = $.ajax({
            url: this.props.source + "/contact_information",
            dataType: "json",
            crossDomain: true,
            type: "GET",
            cache: false,
            success: function (data) {
                this.setState({
                    url: data.data.external_contact_information.url,
                    email: data.data.external_contact_information.email
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

    render: function () {
        return (
            <div className="col-lg-12 col-md-12 col-sm-12 col-xs-12">
                <h2>Contact information</h2>
                <div className="wrapper">
                    <span
                        className={type == 'catalogue' && (this.state.url == null || this.state.url.length) < 0 ? 'collapse' : ''}>URL: <a
                        target="blank" href={this.state.url}>{this.state.url}</a></span><br/>
                    <span
                        className={type == 'catalogue' && (this.state.email == null || this.state.email.length < 0) ? 'collapse' : ''}>Email: {this.state.email}</span>
                </div>
                <hr className="separator col-lg-12 col-md-12 col-sm-12 col-xs-12"/>
            </div>
        )
    }
});


var UserCustomerWrapper = React.createClass({
    render: function () {
        return (
            <div>
                <span className="col-lg-6 col-xs-6 oddAttribute">{this.props.data.name}</span> <span
                className="col-lg-6 col-xs-6 evenAttribute">{this.props.data.role}</span>
            </div>
        )
    }
});
var UserCustomers = React.createClass({

    getInitialState: function () {
        return {
            userCustomers: []
        }
    },

    render: function () {

        return (
            <div className="col-lg-12 col-md-12 col-sm-12 col-xs-12">
                <h2>User Customers</h2>
                <div className="wrapper">
                    <span className="col-lg-6 col-xs-6 oddAttribute"> Name</span> <span
                    className="col-lg-6 col-xs-6 evenAttribute">Role </span> <br />
                    {this.props.userCustomers.map(function (userCustomer) {
                        return <UserCustomerWrapper key={userCustomer.name} data={userCustomer}/>
                    })}
                </div>
                <hr className="separator col-lg-12 col-md-12 col-sm-12 col-xs-12"/>
            </div>
        )
    }
});
var ServiceOwner = React.createClass({
    getInitialState: function () {
        return {
            url: "",
            email: ""
        }
    },

    componentDidMount: function () {
        this.serverRequest = $.ajax({
            url: this.props.source + "/service_owner",
            dataType: "json",
            crossDomain: true,
            type: "GET",
            cache: false,
            success: function (data) {
                this.setState({
                    first_name: data.data.first_name,
                    last_name: data.data.last_name,
                    email: data.data.email
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
    render: function () {
        return (
            <div className="col-lg-12 col-md-12 col-sm-12 col-xs-12">
                <h2>Service Owner</h2>
                <div className="wrapper">
                    <span>Name: {this.state.first_name} {this.state.last_name}</span><br/>
                    <span>Email: {this.state.email}</span>
                </div>
                <hr className="separator col-lg-12 col-md-12 col-sm-12 col-xs-12"/>
            </div>
        )
    }
});


var FundersForService = React.createClass({
    render: function () {
        return (
            <div className="col-lg-12 col-md-12 col-sm-12 col-xs-12" id="service-funders">
                <h2>Funders for Service</h2>
                <div className="wrapper">
                    <span>{this.props.funders_for_service}</span>
                </div>
                <hr className="separator col-lg-12 col-md-12 col-sm-12 col-xs-12"/>
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
                    <span>{this.props.risks}</span>
                </div>
                <hr className="separator col-lg-12 col-md-12 col-sm-12 col-xs-12"/>
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
                    <span>{this.props.competitors}</span>
                </div>
                <hr className="separator col-lg-12 col-md-12 col-sm-12 col-xs-12"/>
            </div>
        )
    }
});
var OptionWrapper = React.createClass({

    getInitialState: function () {
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
                <img src="/static/assets/images/logos/logo-b2safe.png"
                     className="col-lg-1 col-md-1 col-sm-1 col-xs-6 col-xs-offset-3 col-sm-offset-0"/>
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
            serviceOptions: []

        }
    },

    componentDidMount: function () {
        this.serverRequest = $.ajax({
            url: this.props.source + "/service_options",
            dataType: "json",
            crossDomain: true,
            type: "GET",
            cache: false,
            success: function (data) {

                this.setState({serviceOptions: data.data.options});

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
        return (
            <div className={type == 'catalogue' && (this.state.serviceOptions.length == 0) ? 'collapse' : ''}>
                <div className="col-lg-12 col-md-12 col-sm-12 col-xs-12">
                    <h2>Service options</h2>
                    <div className="wrapper">
                        {this.state.serviceOptions.map(function (option) {
                            return <OptionWrapper key={option.name} data={option}/>
                        })}
                    </div>
                </div>
                <hr className="separator col-lg-12 col-md-12 col-sm-12 col-xs-12"/>
            </div>
        )
    }
});


var ServiceDependencies = React.createClass({

    getInitialState: function () {
        return {
            dependencies: []
        }

    },

    componentDidMount: function () {
        this.serverRequest = $.ajax({
            url: this.props.source + "/service_dependencies_with_graphics",
            dataType: "json",
            crossDomain: true,
            type: "GET",
            cache: false,
            success: function (data) {

                this.setState({
                    dependencies: data.data.dependencies
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

    render: function () {
        return (
            <div className="col-lg-12 col-md-12 col-sm-12 col-xs-12">
                <h2>Service dependencies</h2>
                <div className="wrapper">
                    {this.state.dependencies.map(function (service) {
                        return <DependencyWrapper key={service.name} data={service}/>
                    })}
                </div>
                <hr className="separator col-lg-12 col-md-12 col-sm-12 col-xs-12"/>
            </div>
        )
    }
});


var DependencyWrapper = React.createClass({
    getInitialState: function () {

        return {
            data: {
                name: "",
                logo: "",
                description: ""
            }

        }
    },

    render: function () {

        return (
            <div className="options col-lg-12 col-md-12 col-sm-12 col-xs-12">
                <img src={ this.props.data.service.logo}
                     className="col-lg-1 col-md-1 col-sm-1 col-xs-6 col-xs-offset-3 col-sm-offset-0"/>
                <div className="col-lg-11 col-md-11 col-sm-11 col-xs-12 center-text-xs">
                    <h3 className="col-lg-12 option-name">{this.props.data.service.name}</h3>
                    <div className="features col-xs-12">
                        <p className="col-lg-9 col-md-9 col-sm-9 center-text-xs padding-left-0">{this.props.data.service.description}</p>
                    </div>
                </div>
            </div>
        )
    }
});


var ComponentWrapper = React.createClass({
    getInitialState: function () {

        return {
            data: {
                name: "",
                description: "",
                version: ""
            }

        }
    },
    render: function () {


        return (
            <div className="options col-lg-12 col-md-12 col-sm-12 col-xs-12">
                <img src={ this.props.data.component.logo }
                     className="col-lg-1 col-md-1 col-sm-1 col-xs-6 col-xs-offset-3 col-sm-offset-0"/>
                <div className="col-lg-11 col-md-11 col-sm-11 col-xs-12 center-text-xs">
                    <h3 className="col-lg-12 option-name">{this.props.data.component.name}</h3>
                    <div className="features col-xs-12">
                        <p className="col-lg-9 col-md-9 col-sm-9 center-text-xs padding-left-0">Service
                            version: {this.props.data.component.version}</p>
                        <p className="col-lg-9 col-md-9 col-sm-9 center-text-xs padding-left-0">{this.props.data.component.description}</p>
                    </div>
                </div>

            </div>
        )
    }
});

var ServiceComponents = React.createClass({
    getInitialState: function () {
        return {
            service_components: []
        }

    },

    componentDidMount: function () {
        this.serverRequest = $.ajax({
            url: this.props.source + "/service_components",
            dataType: "json",
            crossDomain: true,
            type: "GET",
            cache: false,
            success: function (data) {

                this.setState({
                    service_components: data.data.service_components_list.service_components
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


    render: function () {

        return (
            <div className="col-lg-12 col-md-12 col-sm-12 col-xs-12" id="service-components">
                <h2>Service components</h2>
                <div className="wrapper">
                    {this.state.service_components.map(function (component) {
                        return <ComponentWrapper key={component.name} data={component}/>
                    })}
                </div>
                <hr className="separator col-lg-12 col-md-12 col-sm-12 col-xs-12"/>
            </div>
        )


    }
});

var PortfolioHeader = React.createClass({

    render: function(){
        return (
            <div>
                <ul className="service-header">
                    <li id="li-basic"><a>Basic</a></li>
                    <li id="li-description"><a>Description</a></li>
                    {/* <li>SLA</li> */}
                    <li id="li-business"><a>Business</a></li>
                    <li id="li-extra"><a>Extra</a></li>
                </ul>
            </div>
        )
    }
});


$(document).ready(function(){
    console.log("deaeageag");
    $("body").on("click", "#li-basic", function(){

        console.log("deadaef");
        $('html, body').animate({
            scrollTop: $("#service-headline").offset().top
        }, 2000);
    });
    $("body").on("click", "#li-description", function(){
        $('html, body').animate({
            scrollTop: $("#service-components").offset().top
        }, 2000);
    });

    $("body").on("click", "#li-business", function(){
        $('html, body').animate({
            scrollTop: $("#service-funders").offset().top
        }, 2000);
    });

    $("body").on("click", "#li-extra", function(){
        console.log("da");
        $('html, body').animate({
            scrollTop: $("#service-request").offset().top
        }, 2000);
    });
});


var CatalogueServicePage = React.createClass({

        getInitialState: function () {
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

        componentDidMount: function () {
            jQuery.support.cors = true;
            this.serverRequest = $.ajax({
                url: this.props.source,
                dataType: "json",
                crossDomain: true,
                type: "GET",
                cache: false,
                success: function (data) {
                    this.setState({data: data.data});
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


            return (
                <div className="col-md-10 col-lg-8" id="service-content">

                    <ServiceHeadline title={this.state.data.name} serviceArea={this.state.data.service_area}
                                     shortDescription="Sample short description" logo={this.state.data.logo}/>

                    <ServiceDescription descriptionExternal={this.state.data.description_external}/>
                    {/* <Separator /> */}
                    {/*  <UserCustomers userCustomers={this.state.data.user_customers_list.user_customers} /> */}
                    {/*    <Separator /> */}
                    <ValueToCustomer valueToCustomer={this.state.data.value_to_customer}/>
                    {/* <Separator /> */}
                    <ServiceVersions serviceDetails={this.state.data.service_details_list.service_details}
                                     serviceName={this.state.data.name}/>
                    {/*       <Separator /> */}
                    <Options source={this.props.source}/>
                    {/*       <Separator /> */}
                    <RequestProcedures requestProcedures={this.state.data.request_procedures}/>
                    {/*  <Separator /> */}
                    <Contact source={this.props.source}/>
                    {/*       <Separator /> */}
                </div>
            );
        }
    }
);


var PortfolioServicePage = React.createClass({

    getInitialState: function () {
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
                },
                risks: "",
                funders_for_service: "",
                competitors: ""
            }
        };
    },

    componentDidMount: function () {
        jQuery.support.cors = true;
        this.serverRequest = $.ajax({
            url: this.props.source,
            dataType: "json",
            crossDomain: true,
            type: "GET",
            cache: false,
            success: function (data) {
                this.setState({data: data.data});
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
        return (
            <div className="col-md-10 col-lg-8" id="service-content">
                <PortfolioHeader />

                {/* BASIC */}
                <ServiceHeadline title={this.state.data.name} serviceArea={this.state.data.service_area}
                                 shortDescription="Sample short description" logo={this.state.data.logo}/>
                <ServiceDescription descriptionExternal={this.state.data.description_external}/>
                <UserCustomers userCustomers={this.state.data.user_customers_list.user_customers}/>
                <ServiceVersions serviceDetails={this.state.data.service_details_list.service_details}
                                 serviceName={this.state.data.name}/>
                <ServiceOwner source={this.props.source}/>
                <Contact source={this.props.source}/>


                {/* DETAIL */}
                <ServiceComponents source={this.props.source}/>
                <Options source={this.props.source}/>
                <ServiceDependencies source={this.props.source}/>


                {/* SLA */}



                {/* BUSINESS */}
                <FundersForService fundersForService={this.state.data.funders_for_service}/>
                <Risks risks={this.state.data.risks}/>
                <Competitors competitors={this.state.data.competitors}/>
                <ValueToCustomer valueToCustomer={this.state.data.value_to_customer}/>


                {/* EXTRA */}
                <RequestProcedures requestProcedures={this.state.data.request_procedures}/>






            </div>
        );
    }
});


var ServiceWrapper = React.createClass({
    getInitialState: function () {

        return {
            data: []

        }
    },
    onServiceClick: function (event) {


        var newUrl = event.nativeEvent.srcElement.id;
        window.location.hash += newUrl;
        window.location.reload();

    },

    render: function () {

        return (
            <a href={"#"+ this.props.data.name.split(' ').join('_')} id={this.props.data.name.split(' ').join('_')}
               onClick={this.onServiceClick}>
                <div className="service-pick col-lg-12 col-md-12 col-sm-12 col-xs-12">
                    <div className="service-tile col-lg-12 col-md-12 col-sm-12 col-xs-12 center-text-xs"
                         id={this.props.data.name.split(' ').join('_')}>
                        <img src={"http://snf-715140.vm.okeanos.grnet.gr/" + this.props.data.logo }
                             className="service-logo col-lg-1 col-md-1 col-sm-2 col-xs-2"
                             id={this.props.data.name.split(' ').join('_')}/>
                        <h3 className="col-lg-8 col-md-8 col-sm-8 col-xs-8 col-xs-offset-1"
                            id={this.props.data.name.split(' ').join('_')}>{this.props.data.name}</h3>
                    </div>
                </div>
            </a>
        )
    }
});

var ServiceAreas = React.createClass({
    getInitialState: function () {
        return {
            service_area: "",
            service_area_icon: "",
            services: []
        }

    },

    componentDidMount: function () {


    },

    componentWillUnmount: function () {

    },


    render: function () {

        return (
            <div className="col-lg-12 col-md-12 col-sm-12 col-xs-12">
                <h2 className="area-header"><img width="40"
                                                 src={"http://snf-715140.vm.okeanos.grnet.gr/static/img/logos/" + this.props.service_area_icon}/>
                    <span >{this.props.service_area}</span></h2>
                <div className="wrapper">


                    {  this.props.services.map(function (service) {

                        return <ServiceWrapper data={service}/>
                    })}
                </div>
            </div>
        )


    }
});


var MenuItemIcon = React.createClass({

    onMenuItemClick: function (event) {
        console.log("dedae");
        window.location.reload();

    },

    render: function () {
        return (
            <a href={"#" + this.props.name.split(' ').join('_')} onClick={this.onMenuItemClick}>
                <img width="30" src={"http://snf-715140.vm.okeanos.grnet.gr" + this.props.icon}/>
                <span className="menu-text">{this.props.name}</span>
            </a>
        );
    }
});

var MenuItem = React.createClass({
    render: function () {
        return (
            <a href="{this.props.href}">
                <span className="menu-text">{this.props.text}</span>
            </a>
        );
    }
});

var ParentMenuIcon = React.createClass({
    render: function () {
        return (
            <a className="menu-dropdown">
                <img width="30" src={"http://snf-715140.vm.okeanos.grnet.gr/static/img/logos/" + this.props.icon}/>
                <span className="menu-text">{this.props.name}</span>
                <i className="menu-expand"></i>
            </a>
        );
    }
});

var ParentMenu = React.createClass({
    render: function () {
        return (
            <a href="#" className="menu-dropdown">
                <span className="menu-text">{this.props.text}</span>
                <i className="menu-expand"></i>
            </a>
        );
    }
});


var NavbarBrand = React.createClass({
    render: function () {
        return (
            <div className="navbar-header pull-left">
                <a href="#" className="navbar-brand">
                    <small>
                        <img src="assets/img/logo.png" alt=""/>
                    </small>
                </a>
            </div>
        );
    }
});

var SideBar = React.createClass({
    handleClick: function (e) {

        var b = $("#sidebar").hasClass("menu-compact");
        //if (!$('#sidebar').is(':visible'))
        //    $("#sidebar").toggleClass("hide");
        $("#sidebar").toggleClass("menu-compact");
        $("#service-content").toggleClass("col-lg-offset-2");
        $(".sidebar-collapse").toggleClass("active");
        b = $("#sidebar").hasClass("menu-compact");

        if ($(".sidebar-menu").closest("div").hasClass("slimScrollDiv")) {
            $(".sidebar-menu").slimScroll({destroy: true});
            $(".sidebar-menu").attr('style', '');
        }
        if (b) {
            $(".open > .submenu").removeClass("open");
        } else {
            if ($('.page-sidebar').hasClass('sidebar-fixed')) {
                var position = (readCookie("rtl-support") || location.pathname == "/index-rtl-fa.html" || location.pathname == "/index-rtl-ar.html") ? 'right' : 'left';
                $('.sidebar-menu').slimscroll({
                    height: 'auto',
                    position: position,
                    size: '3px',
                    color: themeprimary
                });
            }
        }
    },
    render: function () {
        return (
            <div className="sidebar-collapse hidden-md hidden-lg" id="sidebar-collapse" onClick={this.handleClick}>
                <i className="collapse-icon fa fa-bars"></i>
            </div>
        );
    }
});


var PageSidebar = React.createClass({
    bodyClickHandler: function (e) {

        var b = $("#sidebar").hasClass(".page-sidebar");
        var menuLink = $(e.target).closest("a");
        if (!menuLink || menuLink.length == 0)
            return;
        if (!menuLink.hasClass("menu-dropdown")) {
            if (b && menuLink.get(0).parentNode.parentNode == this) {
                var menuText = menuLink.find(".menu-text").get(0);
                if (e.target != menuText && !$.contains(menuText, e.target)) {
                    return false;
                }
            }
            return;
        }
        var submenu = menuLink.next().get(0);
        if (!$(submenu).is(":visible")) {
            var c = $(submenu.parentNode).closest("ul");
            if (b && c.hasClass("sidebar-menu"))
                return;
            c.find("> .open > .submenu")
                .each(function () {
                    if (this != submenu && !$(this.parentNode).hasClass("active"))
                        $(this).slideUp(200).parent().removeClass("open");
                });
        }
        if (b && $(submenu.parentNode.parentNode).hasClass("sidebar-menu"))
            return false;
        $(submenu).slideToggle(200).parent().toggleClass("open");
        return false;
    },
    getInitialState: function () {
        return {
            areas: []
        }
    },

    componentDidMount: function () {
        jQuery.support.cors = true;
        this.serverRequest = $.ajax({
            url: this.props.source,
            dataType: "json",
            crossDomain: true,
            type: "GET",
            cache: false,
            success: function (data) {
                this.setState({areas: data.data.areas});
            }.bind(this),
            error: function (xhr, status, err) {
            }.bind(this)
        });
    },
    componentWillUnmount: function () {
        this.serverRequest.abort();
    },

    render: function () {
        return (
            <div className="page-sidebar col-md-2 hidden-sm hidden-xs" id="sidebar">

                <ul className="nav sidebar-menu" onClick={this.bodyClickHandler}>

                    {this.state.areas.map(function (area) {
                        if (area[1] == null)
                            area[1] = "service.png";
                        return (
                            <li>
                                <ParentMenuIcon name={area[0][0].service_area} icon={area[1]}/>
                                <ul className="submenu">
                                    {area[0].map(function (service) {
                                        return <li><MenuItemIcon name={service.name} icon={service.logo}/></li>
                                    })}
                                </ul>
                            </li> )
                    })}
                </ul>
            </div>
        );
    }
});


var PickerPage = React.createClass({

    getInitialState: function () {
        return {
            data: []
        };
    },

    componentDidMount: function () {
        jQuery.support.cors = true;
        this.serverRequest = $.ajax({
            url: this.props.source,
            dataType: "json",
            crossDomain: true,
            type: "GET",
            cache: false,
            success: function (data) {
                this.setState({data: data.data.areas});
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

        return (
            <div className="col-xs-12 col-md-8 col-md-offset-2">
                <div className="wrapper">
                    {this.state.data.map(function (servicesInArea) {
                        if (servicesInArea[1] == null)
                            servicesInArea[1] = "service.png";
                        return <ServiceAreas services={servicesInArea[0]} service_area_icon={servicesInArea[1]}
                                             service_area={servicesInArea[0][0].service_area}/>
                    })}
                </div>
            </div>
        );
    }
});

var CataloguePage = React.createClass({

    render: function () {
        return (
            <div>
                <div className="col-md-2 hidden-sm hidden-xs"></div>
                <CatalogueServicePage source={source}/>
            </div>
        );
    }
});

var PortfolioPage = React.createClass({

    render: function () {
        return (
            <div>
                <PageSidebar source={source_areas}/>
                <SideBar />
                <PortfolioServicePage source={source}/>
            </div>
        );
    }
});


var view_type = window.location.href.split("/");

if (window.location.href.indexOf("#") > -1) {


    var url_parts = window.location.href.split("/");


    if (view_type[view_type.length - 1] == "")

        url_parts.splice(-1, 1);


    if (view_type[view_type.length - 3] == "wordpress")

        url_parts = view_type[view_type.length - 2];

    else

        url_parts = view_type[view_type.length - 3];


    var url_parts2 = window.location.href.split("#");

    var service_name = url_parts2[1];

    var type = url_parts;


    var source = "http://snf-715140.vm.okeanos.grnet.gr/api/v1/" + type + "/services/" + service_name;
    var source_areas = "http://snf-715140.vm.okeanos.grnet.gr/api/v1/" + type + "/service_picker/";


    if (type == "catalogue") {
        ReactDOM.render(
            <CataloguePage />,
            document.getElementById('content')
        );
    }
    else {
        ReactDOM.render(
            <PortfolioPage />,
            document.getElementById('content')
        );
    }


}

else {


    var view_type = window.location.href.split("/");


    if (view_type[view_type.length - 1] == "")

        view_type.splice(-1, 1);


    if (view_type[view_type.length - 2] == "wordpress")

        view_type = view_type[view_type.length - 1];

    else

        view_type = view_type[view_type.length - 2];


    var source = "http://snf-715140.vm.okeanos.grnet.gr/api/v1/" + view_type + "/service_picker/";

    ReactDOM.render(
        <PickerPage source={source}/>,
        document.getElementById('content')
    );
}


var view_type = window.location.href.split("/");

//if(view_type[view_type.length - 1] == "")
//  view_type.splice(-1,1);

//if(view_type[view_type.length - 2] == "wordpress")
//    view_type = view_type[view_type.length - 1];
//else
//    view_type = view_type[view_type.length - 2];

//debugger;


//if(view_type[view_type.length - 2] != "catalogue" || view_type[view_type.length - 2] != "portfolio")
//    view_type = view_type[view_type.length - 3];
//else
//    view_type = view_type[view_type.length - 2];

//var source = "http://agora-dev.vi-seem.eu/api/v1/" + view_type + "/service_picker/";


//ReactDOM.render(
//        <PickerPage source={source} />,
//        document.getElementById('content')
//);