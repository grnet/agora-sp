

var ServiceTable = React.createClass({

    render: function(){
        return (
            <div>
                Services table
            </div>
        )
    }
});

ReactDOM.render(
  <ServiceTable  source={$("#source")[0].value}/>,
  document.getElementById('write-content')
);