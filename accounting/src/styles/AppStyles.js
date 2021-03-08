import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles((theme) => ({
    '@global': {
      ul: {
        margin: 0,
        padding: 0,
        listStyle: 'none',
      },
    },
    root: {
      width: '100%',
    },
    container: {
      maxHeight: 440,
    },
    table: {
      minWidth: 650,
    },
    appBar: {
      borderBottom: `1px solid ${theme.palette.divider}`,
    },
    toolbar: {
      flexWrap: 'wrap',
    },
    toolbarTitle: {
      flexGrow: 1,
    },
    link: {
      margin: theme.spacing(1, 1.5),
    },
    heroContent: {
      padding: theme.spacing(14, 0, 5),
    },
    cardHeader: {
      backgroundColor:
        theme.palette.type === 'light' ? theme.palette.grey[200] : theme.palette.grey[700],
    },
    cardPricing: {
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'baseline',
    },
    card: {
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'baseline',
      marginBottom: theme.spacing(2),
    },
    cardDouble: {
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center',
      marginBottom: theme.spacing(2),
      width: 500,
      height: 100,
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
    logo: {
      height: 45,
    },
    logoPadding: {
      flexGrow: 1,
    },
    mainBoard: {
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center',
      margin: theme.spacing(5)
    },
    row: {
      flexGrow: 1,
      flexDirection: 'row'
    },
    tableBody: {
  
      overflow: 'auto',
    },
    nav: {
      flexGrow: 1,
      position: 'relative',
      marginLeft: 0,
      width: '100%',
      padding: theme.spacing(0, 2),
      height: '100%',
      position: 'absolute',
      pointerEvents: 'none',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'flex-end',
    },
    title: {
      flexGrow: 1,
      display: 'none',
    } 
}));


export default useStyles;  