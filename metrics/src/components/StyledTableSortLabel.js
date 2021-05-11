import TableSortLabel from '@material-ui/core/TableSortLabel';
import { withStyles } from '@material-ui/core/styles';
import config from '../config';

const StyledTableSortLabel = withStyles((theme) => ({
  root: {
    color: config.colors.previousMonthsHeaderText,
    "&:hover": {
      color: config.colors.previousMonthsHeaderText,
    },
    '&$active': {
      color: config.colors.previousMonthsHeaderText,
    },
    '&:visited': {
      color: config.colors.previousMonthsHeaderText,
    },
  },
  active: {},
  icon: {
    color: 'inherit !important'
  },
}))(TableSortLabel);

export default StyledTableSortLabel;
