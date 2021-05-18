import React from 'react';
import CssBaseline from '@material-ui/core/CssBaseline';

import Footer from './components/Footer';
import NavBar from './components/NavBar';
import TopPage from './components/TopPage';
import PreviousMonths from './components/PreviousMonths';

const App = () => {
  return (
    <React.Fragment>
      <CssBaseline />
      <NavBar logo={'/logo.png'}/>
      <TopPage />
      <PreviousMonths />
      <Footer />
    </React.Fragment>
  );
};

export default App;
