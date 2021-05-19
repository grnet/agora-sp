import React from 'react';
import Grid from '@material-ui/core/Grid';
import Container from '@material-ui/core/Container';
import Box from '@material-ui/core/Box';
import { format } from 'date-fns';
import DateFnsUtils from '@date-io/date-fns';
import Button from '@material-ui/core/Button';
import {
  MuiPickersUtilsProvider,
  KeyboardDatePicker,
} from '@material-ui/pickers';
import 'date-fns/format';
import useStyles from '../styles/AppStyles';
import InfoBox from './InfoBox';
import InfoBoxUsers from './InfoBoxUsers';
import CONFIG from '../config';
import { Typography, withStyles } from '@material-ui/core';
import { get_month } from '../utils/Month';

const initData = {
  newProviders: 0,
  updatedProviders: 0,
  newResources: 0,
  updatedResources: 0,
  newUsers: 0,
};

const TopPage = () => {
  const classes = useStyles();
  const [accData, setAccData] = React.useState(initData);
  const [currentDate, setCurrentDate] = React.useState(new Date());
  const [monthStart, setMonthStart] = React.useState(new Date().setDate(1));
  const [titleMonth, setTitleMonth] = React.useState(
    get_month(new Date().getMonth() + 1) + ' ' + new Date().getFullYear()
  );

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
      newResources: data.resources.new_resources,
      updatedResources: data.resources.updated_resources,
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
        setTitleMonth('Custom date range');
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
        <Typography component="h4" variant="h4" color="textPrimary">
          {titleMonth}
        </Typography>
      </Container>
      <Container maxWidth="md" className={classes.heroContent}>
        <MuiPickersUtilsProvider utils={DateFnsUtils}>
          <Grid container md={9} justify="flex-end" alignItems="center">
            <Grid item xs={12} sm={4}>
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
            <Grid item xs={12} sm={4}>
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
            <Grid item xs={12} sm={4} align="center">
              <Box mt={3}>
                <ColorButton
                  variant="contained"
                  color="primary"
                  onClick={searchHandle}
                  aria-label="delete"
                >
                  Apply filter
                </ColorButton>
              </Box>
            </Grid>
          </Grid>
        </MuiPickersUtilsProvider>
      </Container>

      <Container maxWidth="md" component="main">
        <InfoBox
          title="Providers"
          new={accData.newProviders}
          updated={accData.updatedProviders}
        />
        <InfoBox
          title="Resources"
          new={accData.newResources}
          updated={accData.updatedResources}
        />
        <InfoBoxUsers title="Users" new={accData.newUsers} />
      </Container>
    </>
  );
};

export default TopPage;
