
var OwnerTable = React.createClass({

	render: function () {
		return (
			<div>
				Service owners table
			</div>
		)
	}
});

ReactDOM.render(
  <OwnerTable  source={$("#source")[0].value}/>,
  document.getElementById('write-content')
);