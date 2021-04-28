import TableSortLabel from '@material-ui/core/TableSortLabel';
import { withStyles } from '@material-ui/core/styles';

const StyledTableSortLabel = withStyles((theme) => ({
  root: {
    color: 'white',
    "&:hover": {
      color: 'white',
    },
    '&$active': {
      color: 'white',
    },
    '&:visited': {
      color: 'white',
    },
  },
  active: {},
  icon: {
    color: 'inherit !important'
  },
}))(TableSortLabel);

export default StyledTableSortLabel;
