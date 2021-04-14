import React from 'react';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Link from '@material-ui/core/Link';

import useStyles from '../styles/AppStyles';
import config from '../config';

const NavBar = (props) => {
  const classes = useStyles();
  return (
    <AppBar
      position="fixed"
      color="default"
      elevation={0}
      className={classes.appBar}
    >
      <Toolbar>
        <img src={props.logo} className={classes.logo} alt="Logo" />
        <Typography
          component="h6"
          variant="h6"
          color="textPrimary"
          noWrap
          className={classes.toolbarTitle}
        >
          Agora Accounting
        </Typography>
        <Link
          variant="button"
          color="textPrimary"
          href={config.endpoint}
          className={classes.link}
        >
          Agora
        </Link>
        <Link
          variant="button"
          color="textPrimary"
          href={config.endpoint + '/catalogue'}
          className={classes.link}
        >
          Catalogue
        </Link>
        <Link
          variant="button"
          color="textPrimary"
          href={'mailto:' + config.supportMail}
          className={classes.link}
        >
          Support
        </Link>
      </Toolbar>
    </AppBar>
  );
};

export default NavBar;
