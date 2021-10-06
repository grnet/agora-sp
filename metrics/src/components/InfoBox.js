import React from 'react';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import 'date-fns/format';
import useStyles from '../styles/AppStyles';

const InfoBox = (props) => {
  const classes = useStyles();
  return (
    <Grid container spacing={2} direction="row" alignItems="center">
      <Grid item key={'10'} xs={12} sm={12} md={2}>
        <Typography style={{ fontWeight: 600 }} variant="h5" color="textPrimary">
          {props.title}
        </Typography>
      </Grid>
      <Grid item xs={12} sm={12} md={3}>
        <Card>
          <CardContent>
            <div className={classes.cardPricing}>
              <Typography component="h2" variant="h3" color="textPrimary">
                {props.new}
              </Typography>
              <Typography variant="h6" color="textSecondary">
                new
              </Typography>
            </div>
          </CardContent>
        </Card>
      </Grid>
      <Grid item xs={12} sm={12} md={3}>
        <Card>
          <CardContent>
            <div className={classes.cardPricing}>
              <Typography component="h2" variant="h3" color="textPrimary">
                {props.updated}
              </Typography>
              <Typography variant="h6" color="textSecondary">
                updated
              </Typography>
            </div>
          </CardContent>
        </Card>
      </Grid>
      <Grid item xs={12} sm={12} md={3}>
        <Card>
          <CardContent>
            <div className={classes.cardPricing}>
              <Typography component="h2" variant="h3" color="textPrimary">
                {props.updated_total}
              </Typography>
              <Typography variant="h6" color="textSecondary">
                total updates
              </Typography>
            </div>
          </CardContent>
        </Card>
      </Grid>
    </Grid>
  );
};

export default InfoBox;
