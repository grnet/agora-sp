var ServiceWrapper = React.createClass({
    getInitialState: function(){

        return {
            data: []

        }},
    render: function () {

        console.log("Datata e tuka...");
        return (
                <a href={"http://localhost/ui/portfolio/services/"+ this.props.data.name.split(' ').join('_')}> <div className="service-pick col-lg-12 col-md-12 col-sm-12 col-xs-12">
                    <div className="service-tile col-lg-12 col-md-12 col-sm-12 col-xs-12 center-text-xs">
                         <img src= { this.props.data.logo }  className="service-logo col-lg-1 col-md-1 col-sm-2 col-xs-2" />
                        <h3 className="col-lg-8 col-md-8 col-sm-8 col-xs-8 col-xs-offset-1">{this.props.data.name}</h3>
                    </div>
                </div> </a>
        )
    }
});

var ServiceAreas = React.createClass({
    getInitialState: function(){
        return {
            service_area: "",
            services: [   ]
        }

    },

    componentDidMount: function(){


    },

    componentWillUnmount: function(){

    },


    render: function () {

        return (
                <div className="col-lg-12 col-md-12 col-sm-12 col-xs-12">
                    <h2 className="area-header"><span className="glyphicon glyphicon-adjust" aria-hidden="true"></span> <span >{this.props.service_area}</span> </h2>
                    <div className="wrapper">


                        {  this.props.services.map(function(service){

                            return <ServiceWrapper  data={service}/>
                        })}
                    </div>
                </div>
        )


    }
});

var PickerPage = React.createClass({

    getInitialState: function(){
        return {

                    data: [ ],

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
                this.setState({data: data.data.areas});
                console.log(this.state.data);
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
                    <div className="wrapper">
                        {this.state.data.map(function(servicesInArea){
                                 return <ServiceAreas services={servicesInArea} service_area={servicesInArea[0].service_area}/>
                            })}
                    </div>
                </div>
        );
   }
});


ReactDOM.render(
        <PickerPage source="http://localhost/api/v1/{{ view_type }}/service_picker/" />,
        document.getElementById('content')
);