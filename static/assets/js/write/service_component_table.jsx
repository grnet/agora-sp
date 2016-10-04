
var ComponentTable = React.createClass({

	getInitialState: function(){
		return {
			components: []
		}
	},

	componentDidMount: function () {
        this.serverRequest = $.ajax({
            url: this.props.source,
            dataType: "json",
            crossDomain: true,
            type: "GET",
            cache: false,
            success: function (data) {

                this.setState({
                    components: data.data
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
				<div className="col-xs-12">
					<div className="well with-header  with-footer">
						<div className="header bg-blue">
							Service components
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

							{this.state.components.map(function (component) {
								return (
									<tr>
										<td>{component.name}</td>
										<td>{component.description}</td>
										<td><a href={"/ui/component/" + component.uuid}>Edit</a></td>
									</tr>
								)
							})}

							</tbody>
						</table>

					</div>

				</div>

			</div>
		);
	}
});

ReactDOM.render(
  <ComponentTable  source={$("#source")[0].value}/>,
  document.getElementById('write-content')
);