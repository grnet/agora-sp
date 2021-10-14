

import React from 'react';
import Grid from '@material-ui/core/Grid';
import Container from '@material-ui/core/Container';
import 'date-fns/format';
import useStyles from '../styles/AppStyles';
import CONFIG from '../config';
import { Card, Typography, CardHeader, CardContent } from '@material-ui/core';

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
              <Typography component="h2" variant="h3" color="textPrimary">
                {props.new}
              </Typography>
              <Typography variant="body2" color="text.secondary">
                NEW
              </Typography>
            </Container>
            <Container maxWidth="xl" component="footer" className={classes.infoContent}>
              <Typography component="h2" variant="h3" color="textPrimary">
                {props.updated}
              </Typography>
              <Typography variant="body2" color="text.secondary">
                UPDATES
              </Typography>
            </Container>
            <Container maxWidth="xl" component="footer" className={classes.infoContent}>
              <Typography component="h2" variant="h3" color="textPrimary">
                {props.updated_total}
              </Typography>
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