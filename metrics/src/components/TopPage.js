import React from 'react';
import Grid from '@material-ui/core/Grid';
import Container from '@material-ui/core/Container';
import { format } from 'date-fns';
import DateFnsUtils from '@date-io/date-fns';
import Button from '@material-ui/core/Button';
import {
  MuiPickersUtilsProvider,
  KeyboardDatePicker,
} from '@material-ui/pickers';
import 'date-fns/format';
import useStyles from '../styles/AppStyles';
import InfoCard from './InfoCard';
import CONFIG from '../config';
import { Card, Typography, withStyles} from '@material-ui/core';
import SearchIcon from '@material-ui/icons/Search';
import BusinessIcon from '@material-ui/icons/Business';
import SettingsIcon from '@material-ui/icons/Settings';
import PersonIcon from '@material-ui/icons/Person';

const initData = {
  newProviders: 0,
  updatedProviders: 0,
  updatedProvidersTotal: 0,
  newResources: 0,
  updatedResources: 0,
  updatedResourcesTotal: 0,
  newUsers: 0,
};

const TopPage = () => {
  const classes = useStyles();
  const [accData, setAccData] = React.useState(initData);
  const [currentDate, setCurrentDate] = React.useState(new Date());
  const [monthStart, setMonthStart] = React.useState(new Date().setDate(1));

  const handleStartDateChange = (date) => {
    setMonthStart(date);
  };

  const handleEndDateChange = (date) => {
    setCurrentDate(date);
  };

  const getDate = (date) => {
    return format(date, 'dd-MM-yyyy');
  };

  const getAccountingData = (data) => {
    return {
      newProviders: data.providers.new_providers,
      updatedProviders: data.providers.updated_providers,
      updatedProvidersTotal: data.providers.total_updated_providers,
      newResources: data.resources.new_resources,
      updatedResources: data.resources.updated_resources,
      updatedResourcesTotal: data.resources.total_updated_resources,
      newUsers: data.users.new_users,
    };
  };

  React.useEffect(() => {
    const fromDate = getDate(new Date().setDate(1));
    const toDate = getDate(new Date());
    fetch(`${CONFIG.endpoint}/api/v2/accounting?from=${fromDate}&to=${toDate}`)
      .then((res) => res.json())
      .then((result) => {
        setAccData(getAccountingData(result));
      });
  }, []);

  const searchHandle = () => {
    const fromDate = getDate(monthStart);
    const toDate = getDate(currentDate);
    fetch(`${CONFIG.endpoint}/api/v2/accounting?from=${fromDate}&to=${toDate}`)
      .then((res) => res.json())
      .then((result) => {
        setAccData(getAccountingData(result));
      });
  };

  const ColorButton = withStyles((theme) => ({
    root: {
      color: theme.palette.getContrastText(CONFIG.colors.searchButton),
      backgroundColor: CONFIG.colors.searchButton,
      '&:hover': {
        backgroundColor: CONFIG.colors.searchButton,
      },
    },
  }))(Button);

  return (
    <>
      <Container maxWidth="sm" component="main" className={classes.title}>
        <Typography component="h4" variant="h4" className={classes.boldHeader}>
          Latest Usage
        </Typography>
      </Container>
      <Container maxWidth="md">
        <Card style={{backgroundColor: 'white', borderRadius: '100px'}} className={classes.heroContent}>
          <MuiPickersUtilsProvider utils={DateFnsUtils}>
            <Grid container xs={12} style={{justifyContent: 'space-between'}}>
              <Grid item xs={12} sm={5} style={{marginLeft: '30px', paddingLeft:'30px'}}>
                <KeyboardDatePicker
                  margin="normal"
                  className={classes.date}
                  disableToolbar
                  variant="inline"
                  format="dd/MM/yyyy"
                  id="date-picker-inline1"
                  label="From"
                  value={monthStart}
                  onChange={handleStartDateChange}
                />
              </Grid>
              <Grid item xs={12} sm={5} style={{marginLeft: '30px', paddingLeft:'30px'}}>
                <KeyboardDatePicker
                  margin="normal"
                  className={classes.date}
                  disableToolbar
                  variant="inline"
                  format="dd/MM/yyyy"
                  id="date-picker-inline2"
                  label="To"
                  value={currentDate}
                  onChange={handleEndDateChange}
                />
              </Grid>
              <Grid item xs={12} sm={1} style={{padding: '10px 10px 10px 0px'}}>
                  <ColorButton
                    variant="contained"
                    color="primary"
                    onClick={searchHandle}
                    aria-label="delete"
                    style={{borderRadius: '50px', height: '65px', width: '65px'}}
                  >
                    <SearchIcon/>
                  </ColorButton>
              </Grid>
            </Grid>
          </MuiPickersUtilsProvider>
        </Card>
      </Container>



        <Grid container  maxWidth="lg" spacing={8} direction="row" alignItems="center"  justify="center" style={{paddingTop: '20px'}}>
          <Grid item>
            <InfoCard
              title="Providers"
              new={accData.newProviders}
              updated={accData.updatedProviders}
              updated_total={accData.updatedProvidersTotal}
              logo={BusinessIcon}
            />
          </Grid>
          <Grid item>
            <InfoCard
              title="Resources"
              new={accData.newResources}
              updated={accData.updatedResources}
              updated_total={accData.updatedResourcesTotal}
              logo={SettingsIcon}
            />
          </Grid>
          <Grid item>
            <InfoCard
              title="Users"
              new={accData.newUsers}
              updated={'-'}
              updated_total={'-'}
              logo={PersonIcon}
            />
          </Grid>
        </Grid>
    </>
  );
};

export default TopPage;
