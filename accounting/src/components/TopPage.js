import React from 'react';
import Grid from '@material-ui/core/Grid';
import Container from '@material-ui/core/Container';
import { format } from 'date-fns';
import DateFnsUtils from '@date-io/date-fns';
import IconButton from '@material-ui/core/IconButton';
import {
  MuiPickersUtilsProvider,
  KeyboardDatePicker,
} from '@material-ui/pickers';
import 'date-fns/format';
import SearchIcon from '@material-ui/icons/Search';
import useStyles from '../styles/AppStyles';
import InfoBox from './InfoBox';
import InfoBoxUsers from './InfoBoxUsers';
import CONFIG from '../config';

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
      });
  };

  return (
    <>
      <Container maxWidth="md" className={classes.heroContent}>
        <Grid container md={9} justify="space-between">
          <MuiPickersUtilsProvider utils={DateFnsUtils}>
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
          </MuiPickersUtilsProvider>
          <IconButton
            className={classes.search}
            variant="outlined"
            color="primary"
            onClick={searchHandle}
            aria-label="delete"
          >
            <SearchIcon />
          </IconButton>
        </Grid>
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
          updated={accData.newResources}
        />
        <InfoBoxUsers title="Users" new={accData.newUsers} />
      </Container>
    </>
  );
};

export default TopPage;
