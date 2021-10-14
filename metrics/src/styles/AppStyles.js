import { makeStyles } from '@material-ui/core/styles';
import config from '../config';

const useStyles = makeStyles((theme) => ({
  '@global': {
    ul: {
      margin: 0,
      padding: 0,
      listStyle: 'none',
    },
  },
  PrevMonthsTable: {
    width: '100%',
    borderRadius: '10px',
  },
  backgroundTheme: {
    backgroundColor: '#f1f1f1',
    width: '100%',
    height: '100%',
  },
  boldHeader: {
    fontWeight: 600,
  },
  appBar: {
    borderBottom: `1px solid ${theme.palette.divider}`,
    backgroundColor: config.colors.navbar,
  },
  date: {
    marginLeft: theme.spacing(4),
    width: '90%',
  },
  toolbarTitle: {
    flexGrow: 1,
    color: config.colors.navbarText
  },
  link: {
    margin: theme.spacing(1, 1.5),
    color: config.colors.navbarText
  },
  heroContent: {
    marginBottom: theme.spacing(5),
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
  },
  footer: {
    borderTop: `1px solid ${theme.palette.divider}`,
    marginTop: theme.spacing(8),
    paddingTop: theme.spacing(3),
    paddingBottom: theme.spacing(3),
    [theme.breakpoints.up('sm')]: {
      paddingTop: theme.spacing(6),
      paddingBottom: theme.spacing(6),
    },
  },
  infoContent: {
    borderTop: `1px solid ${theme.palette.divider}`,
    paddingTop: theme.spacing(3),
    paddingBottom: theme.spacing(3),
  },
  infoContentTop: {
    paddingTop: theme.spacing(3),
    paddingBottom: theme.spacing(3),
  },
  logo: {
    height: 40,
    marginRight: 15,
  },
  tableBody: {
    overflow: 'auto',
    borderRadius: '10px',
  },
  title: {
    paddingTop: theme.spacing(16),
    paddingBottom: theme.spacing(6),
    color: '#323232',
    display: 'flex',
    justifyContent: 'center',
  },
}));

export default useStyles;
