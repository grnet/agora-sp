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

        var logo = host + "/static/img/logos/" + this.props.logo;

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


                    <div className={!this.props.data.usage_policy_has && type == 'catalogue' ? 'collapse' : ''}>
                        Usage policy
                        <a className={!this.props.data.usage_policy_has ? 'collapse' : ''} target="blank" href={this.props.data.usage_policy_link.related.href}> here</a>
                        <span className={this.props.data.usage_policy_has ? 'collapse' : ''}> not available</span>
                    </div>

                    <div className={!this.props.data.privacy_policy_has && type == 'catalogue' ? 'collapse' : ''}>
                        Privacy policy
                        <a className={!this.props.data.privacy_policy_has ? 'collapse' : ''} target="blank" href={this.props.data.privacy_policy_link.related.href}> here</a>
                        <span className={this.props.data.privacy_policy_has ? 'collapse' : ''}> not available</span>
                    </div>

                    <div className={!this.props.data.user_documentation_has && type == 'catalogue' ? 'collapse' : ''}>
                        User documentation
                        <a className={!this.props.data.user_documentation_has ? 'collapse' : ''} target="blank" href={this.props.data.user_documentation_link.related.href}> here</a>
                        <span className={this.props.data.user_documentation_has ? 'collapse' : ''}> not available</span>
                    </div>

                    <div className={!this.props.data.operations_documentation_has && type == 'catalogue' ? 'collapse' : ''}>
                        Operations documentation
                        <a className={!this.props.data.operations_documentation_has ? 'collapse' : ''} target="blank" href={this.props.data.operations_documentation_link.related.href}> here</a>
                        <span className={this.props.data.operations_documentation_has ? 'collapse' : ''}> not available</span>
                    </div>

                    <div className={!this.props.data.monitoring_has && type == 'catalogue' ? 'collapse' : ''}>
                        Monitoring
                        <a className={!this.props.data.monitoring_has ? 'collapse' : ''} target="blank" href={this.props.data.monitoring_link.related.href}> here</a>
                        <span className={this.props.data.monitoring_has ? 'collapse' : ''}> not available</span>
                    </div>

                    <div className={!this.props.data.accounting_has && type == 'catalogue' ? 'collapse' : ''}>
                        Accounting
                        <a className={!this.props.data.accounting_has ? 'collapse' : ''} target="blank" href={this.props.data.accounting_link.related.href}> here</a>
                        <span className={this.props.data.accounting_has ? 'collapse' : ''}> not available</span>
                    </div>

                    <div className={!this.props.data.business_continuity_plan_has && type == 'catalogue' ? 'collapse' : ''}>
                        Business continuity plan
                        <a className={!this.props.data.business_continuity_plan_has ? 'collapse' : ''} target="blank" href={this.props.data.business_continuity_plan_link.related.href}> here</a>
                        <span className={this.props.data.business_continuity_plan_has ? 'collapse' : ''}> not available</span>
                    </div>

                    <div className={!this.props.data.disaster_recovery_plan_has && type == 'catalogue' ? 'collapse' : ''}>
                        Disaster recovery plan
                        <a className={!this.props.data.disaster_recovery_plan_has ? 'collapse' : ''} target="blank" href={this.props.data.disaster_recovery_plan_link.related.href}> here</a>
                        <span className={this.props.data.disaster_recovery_plan_has ? 'collapse' : ''}> not available</span>
                    </div>

                    <div className={!this.props.data.decommissioning_procedure_has && type == 'catalogue' ? 'collapse' : ''}>
                        Decommissioning procedure
                        <a className={!this.props.data.decommissioning_procedure_has ? 'collapse' : ''} target="blank" href={this.props.data.decommissioning_procedure_link.related.href}> here</a>
                        <span className={this.props.data.decommissioning_procedure_has ? 'collapse' : ''}> not available</span>
                    </div>


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

        var logo = host + "/static/img/logos/" + this.props.data.service.logo;

        return (
            <div className="options col-lg-12 col-md-12 col-sm-12 col-xs-12">
                <img src={logo}
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

var Header = React.createClass({

    onLogoClick: function (event) {
        window.location.href =  window.location.href.split('#')[0];
        window.location.reload();
    },

    render: function () {

        var logoSrc;
        if(host.indexOf("sp.eudat.eu") <= -1)
            logoSrc = host + "/static/img/logos/logo_240p-84d8f1c276459514871468b2aab2d777.png";
        else
            logoSrc = "https://eudat.eu/sites/default/files/EUDAT-logo_3.png";

        return (
            <div>

                <nav id="nav_bar" className="navbar navbar-default navbar-fixed-top">
                    <div className="col-md-2">
                        <a href="" onClick={this.onLogoClick}>
                        <img src={logoSrc}
                                height="50"/>
                            </a>
                    </div>
                    <div className={type == 'catalogue' || window.location.href.indexOf("#") == -1 ? 'collapse' : ''}>
                        <ul className="service-header nav_links">
                            <li id="li-basic"><a>Basic Info</a></li>
                            <li id="li-versions"><a>Versions</a></li>
                            <li id="li-description"><a>Description</a></li>
                            {/* <li>SLA</li> */}
                            <li id="li-business"><a>Business Info</a></li>
                            <li id="li-extra"><a>Extra Info</a></li>
                        </ul>
                    </div>
                </nav>
            </div>
        )
    }
});

function toggleNavigationFocus(element){

    $("#li-basic").removeClass("nav-focus");
    $("#li-versions").removeClass("nav-focus");
    $("#li-description").removeClass("nav-focus");
    $("#li-business").removeClass("nav-focus");
    $("#li-extra").removeClass("nav-focus");

    if(element == "li-basic")
        $("#li-basic").addClass("nav-focus");
    else if(element == "li-versions")
        $("#li-versions").addClass("nav-focus");
    else if(element == "li-description")
        $("#li-description").addClass("nav-focus");
    else if(element == "li-business")
        $("#li-business").addClass("nav-focus");
    else if(element == "li-extra")
        $("#li-extra").addClass("nav-focus");
}

$(document).ready(function () {


    $("body").on("mouseover", "#basic-info-sect", function () {
        toggleNavigationFocus("li-basic");
    });

    $("body").on("mouseover", "#versions-sect", function () {
        toggleNavigationFocus("li-versions");
    });

    $("body").on("mouseover", "#description-sect", function () {
        toggleNavigationFocus("li-description");
    });

    $("body").on("mouseover", "#business-info-sect", function () {
        toggleNavigationFocus("li-business");
    });

    $("body").on("mouseover", "#extra-info-sect", function () {
        toggleNavigationFocus("li-extra");
    });


    var offset = 60;

    $("body").on("click", "#li-basic", function () {
        toggleNavigationFocus("li-basic");
        $('html, body').animate({
            scrollTop: $("#basic-info-sect").offset().top - offset - 60
        }, 2000);
    });

    $("body").on("click", "#li-versions", function () {
        toggleNavigationFocus("li-versions");
        $('html, body').animate({
            scrollTop: $("#versions-sect").offset().top - offset
        }, 2000);
    });

    $("body").on("click", "#li-description", function () {
        toggleNavigationFocus("li-description");
        $('html, body').animate({
            scrollTop: $("#description-sect").offset().top - offset
        }, 2000);
    });

    $("body").on("click", "#li-business", function () {
        toggleNavigationFocus("li-business");
        $('html, body').animate({
            scrollTop: $("#business-info-sect").offset().top - offset
        }, 2000);
    });

    $("body").on("click", "#li-extra", function () {
        toggleNavigationFocus("li-extra");
        $('html, body').animate({
            scrollTop: $("#extra-info-sect").offset().top - offset
        }, 2000);
    });

    $(window).scroll(function () {
        //if you hard code, then use console
        //.log to determine when you want the
        //nav bar to stick.
        //console.log($(window).scrollTop());
        if ($(window).scrollTop() > 120) {
            $('#nav_bar').addClass('navbar-shrink', 200);
        }
        if ($(window).scrollTop() < 121) {
            $('#nav_bar').removeClass('navbar-shrink', 200);
        }
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
                    <RequestProcedures requestProcedures={this.state.data.request_procedures}/>
                    <ValueToCustomer valueToCustomer={this.state.data.value_to_customer}/>
                    {/* <Separator /> */}
                    <ServiceVersions serviceDetails={this.state.data.service_details_list.service_details}
                                     serviceName={this.state.data.name}/>
                    {/*       <Separator /> */}
                    <Options source={this.props.source}/>
                    {/*       <Separator /> */}

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


                {/* BASIC */}
                <div id="basic-info-sect" className="col-xs-12">
                    <ServiceHeadline title={this.state.data.name} serviceArea={this.state.data.service_area}
                                     shortDescription="Sample short description" logo={this.state.data.logo}/>
                    <ServiceDescription descriptionExternal={this.state.data.description_external}/>
                    <UserCustomers userCustomers={this.state.data.user_customers_list.user_customers}/>
                    <ServiceOwner source={this.props.source}/>
                    <Contact source={this.props.source}/>
                </div>

                <div id="versions-sect" className="col-xs-12">
                    <ServiceVersions serviceDetails={this.state.data.service_details_list.service_details}
                                     serviceName={this.state.data.name}/>
                </div>

                {/* DETAIL */}
                <div id="description-sect" className="col-xs-12">
                    <ServiceComponents source={this.props.source}/>
                    <Options source={this.props.source}/>
                    <ServiceDependencies source={this.props.source}/>
                </div>

                {/* SLA */}


                {/* BUSINESS */}
                <div id="business-info-sect" className="col-xs-12">
                    <FundersForService fundersForService={this.state.data.funders_for_service}/>
                    <Risks risks={this.state.data.risks}/>
                    <Competitors competitors={this.state.data.competitors}/>
                    <ValueToCustomer valueToCustomer={this.state.data.value_to_customer}/>
                </div>

                {/* EXTRA */}
                <div id="extra-info-sect" className="col-xs-12">
                    <RequestProcedures requestProcedures={this.state.data.request_procedures}/>
                </div>


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

        //debugger;
        var newUrl = event.nativeEvent.target.id;
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
                        <img src={host + "/" + this.props.data.logo }
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
                                                 src={host + "/static/img/logos/" + this.props.service_area_icon}/>
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
        //console.log("dedae");
        window.location.href = "#" + this.props.name.split(" ").join("_");
        window.location.reload();
        //window.location = window.location.href;
        //document.location.reload();

    },

    render: function () {
        return (
            <a href={"#" + this.props.name.split(' ').join('_')} onClick={this.onMenuItemClick}>
                <img width="30" src={host + this.props.icon}/>
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
                <img width="30" src={host + "/static/img/logos/" + this.props.icon}/>
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
                <Header />
                <div className="wrapper area-content">
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
                <Header />
                <PageSidebar source={source_areas}/>
                <SideBar />
                <CatalogueServicePage source={source}/>
            </div>
        );
    }
});

var PortfolioPage = React.createClass({

    render: function () {
        return (
            <div>
                <Header />
                <PageSidebar source={source_areas}/>
                <SideBar />
                <PortfolioServicePage source={source}/>
            </div>
        );
    }
});


var host = "http://snf-715140.vm.okeanos.grnet.gr";
//var host = "http://sp.eudat.eu";

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


    var source = host + "/api/v1/" + type + "/services/" + service_name;
    var source_areas = host + "/api/v1/" + type + "/service_picker/";


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


    var source = host + "/api/v1/" + view_type + "/service_picker/";

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

//var source = "http://snf-715140.vm.okeanos.grnet.gr/api/v1/" + view_type + "/service_picker/";


//ReactDOM.render(
//        <PickerPage source={source} />,
//        document.getElementById('content')
//);
