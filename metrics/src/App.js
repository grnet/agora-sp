import React from 'react';
import CssBaseline from '@material-ui/core/CssBaseline';

import Footer from './components/Footer';
import NavBar from './components/NavBar';
import TopPage from './components/TopPage';
import PreviousMonths from './components/PreviousMonths';
import useStyles from './styles/AppStyles';

const App = () => {
  const classes = useStyles();
  return (
    <div className={classes.backgroundTheme}>
      <CssBaseline />
      <NavBar logo={'logo.png'}/>
      <TopPage />
      <PreviousMonths />
      <Footer />
    </div>
  );
};

export default App;
