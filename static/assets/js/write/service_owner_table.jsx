
var OwnerTable = React.createClass({

	getInitialState: function(){
		return {
			owners: []
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
                    owners: data.data
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
							Service owners
						</div>
						<table className="table table-hover">
							<thead className="bordered-darkorange">
								<tr>
									<th>
										First name
									</th>
									<th>
										Last name
									</th>
									<th>
										Email
									</th>
									<th>
										Phone
									</th>
								</tr>
							</thead>
							<tbody>

							{this.state.owners.map(function (owner, i) {
								return (
									<tr key={i}>
										<td>{owner.first_name}</td>
										<td>{owner.last_name}</td>
										<td>{owner.email}</td>
										<td>{owner.phone}</td>
										<td><a href={"/ui/owner/" + owner.uuid}>Edit</a></td>
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
  <OwnerTable  source={$("#source")[0].value}/>,
  document.getElementById('write-content')
);