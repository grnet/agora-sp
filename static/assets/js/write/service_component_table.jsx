
var ComponentTable = React.createClass({

	render: function () {
		return (
			<div>
				Service components table
			</div>
		)
	}
});

ReactDOM.render(
  <ComponentTable  source={$("#source")[0].value}/>,
  document.getElementById('write-content')
);