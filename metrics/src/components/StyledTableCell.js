import TableCell from '@material-ui/core/TableCell';
import { withStyles } from '@material-ui/core/styles';
import CONFIG from '../config';

const StyledTableCell = withStyles((theme) => ({
  root: {
    backgroundColor: CONFIG.colors.previousMonthsHeader,
    color: CONFIG.colors.previousMonthsHeaderText,
    fontSize: 14,
  },
}))(TableCell);

export default StyledTableCell;
