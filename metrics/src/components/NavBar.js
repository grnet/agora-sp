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
          Agora Metrics
        </Typography>
        <Link
          variant="button"
          color="textPrimary"
          href="#previous_months"
          className={classes.link}
        >
          Previous Months
        </Link>
        <Link
          variant="button"
          color="textPrimary"
          href={config.endpoint}
          className={classes.link}
          target="_blank"
        >
          Agora
        </Link>
        {!!config.catalogueUrl &&
          <Link
            variant="button"
            color="textPrimary"
            href={config.catalogueUrl}
            className={classes.link}
            target="_blank"
          >
            Catalogue
          </Link>
        }
        <Link
          variant="button"
          color="textPrimary"
          href={'mailto:' + config.supportMail}
          className={classes.link}
          target="_blank"
        >
          Support
        </Link>
      </Toolbar>
    </AppBar>
  );
};

export default NavBar;
