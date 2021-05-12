import TableCell from '@material-ui/core/TableCell';
import { withStyles } from '@material-ui/core/styles';

const StyledTableCell = withStyles((theme) => ({
  root: {
    backgroundColor: '#67729c',
    color: '#fff',
    fontSize: 14,
  },
}))(TableCell);

export default StyledTableCell;
