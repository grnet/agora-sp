

import React from 'react';
import Grid from '@material-ui/core/Grid';
import Container from '@material-ui/core/Container';
import 'date-fns/format';
import useStyles from '../styles/AppStyles';
import CONFIG from '../config';
import { Card, Typography, CardHeader, CardContent } from '@material-ui/core';

const isZero = (number) => {
  if (number > 0) {
    return (
      <Typography component="h2" variant="h3" color="textPrimary">
      {number}
    </Typography>)
  } else {
    return (
      <Typography component="h2" variant="h3" style={{color: 'grey'}}>
        {number}
      </Typography>
    )
  }
}

const InfoCard = (props) => {
  const classes = useStyles();
  return (
    <Grid container spacing={4} xs={12} sm={12} md={4} direction="row" alignItems="center">
      <Grid item>
        <Card alignItems="center" style={{ borderRadius: '10px', minHeight: '500px', minWidth: '270px', textAlign: 'center'}}>
          <CardHeader style={{ backgroundColor: CONFIG.colors.ColorA}}
            title={
              <Typography component="h5" variant="h5" style={{ fontWeight: 600, color: '#fff'}}>
                {props.title}
              </Typography>
            }
          />
          <CardContent align="center">
            <Container maxWidth="xl" component="footer" className={classes.infoContentTop}>
              {isZero(props.new)}
              <Typography variant="body2" color="text.secondary">
                NEW
              </Typography>
            </Container>
            <Container maxWidth="xl" component="footer" className={classes.infoContent}>
              {isZero(props.updated)}
              <Typography variant="body2" color="text.secondary">
                UPDATES
              </Typography>
            </Container>
            <Container maxWidth="xl" component="footer" className={classes.infoContent}>
              {isZero(props.updated_total)}
              <Typography variant="body2" color="text.secondary">
                TOTAL UPDATES
              </Typography>
            </Container>
          </CardContent>
        </Card>
      </Grid>
    </Grid>
  );
};

export default InfoCard;