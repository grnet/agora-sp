import React, { Component } from 'react';
import AppBar from '@material-ui/core/AppBar';
import Button from '@material-ui/core/Button';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import CardHeader from '@material-ui/core/CardHeader';
import CssBaseline from '@material-ui/core/CssBaseline';
import Grid from '@material-ui/core/Grid';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Paper from '@material-ui/core/Paper';
import Link from '@material-ui/core/Link';
import { makeStyles, withStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import Box from '@material-ui/core/Box';
import logo from './assets/agora.png';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import TablePagination from '@material-ui/core/TablePagination';

import useStyles from './styles/AppStyles'
import Copyright from './components/Copyright'
import StyledTableCell from './components/StyledTableCell'


const columns = [
  { id: 'year', label: 'Year', minWidth: 170 },
  { id: 'month', label: 'Month', minWidth: 170 },
  { id: 'new_providers', label: 'New providers', minWidth: 170 },
  { id: 'updated_providers', label: 'Updated providers', minWidth: 170 },
  { id: 'new_resources', label: 'New resources', minWidth: 170 },
  { id: 'updated_resources', label: 'Updated resources', minWidth: 170 },
  { id: 'new_users', label: 'New users', minWidth: 170 },
];

function createData(month, year, new_providers, updated_providers, new_resources, updated_resources, new_users) {
  return { month, year, new_providers, updated_providers, new_resources, updated_resources, new_users };
}

const rows = [
  createData('February', 2021, 2, 15, 12, 3,22),
  createData('January', 2021, 20, 125, 1, 32,24),
  createData('December', 2020, 2, 15, 12, 3,22),
  createData('November', 2020, 20, 125, 1, 32,24),
  createData('Octomber', 2020, 2, 15, 12, 3,22),
  createData('September', 2020, 20, 125, 1, 32,24),
  createData('August', 2020, 2, 15, 12, 3,22),
  createData('July', 2020, 20, 125, 1, 32,24),
  createData('June', 2020, 2, 15, 12, 3,22),
  createData('May', 2020, 20, 125, 1, 32,24),
  createData('April', 2020, 2, 15, 12, 3,22),
  createData('March', 2020, 20, 125, 1, 32,24),

];

export default function App() {
  const classes = useStyles();
  const [page, setPage] = React.useState(0);
  const [rowsPerPage, setRowsPerPage] = React.useState(10);

  const handleChangePage = (event, newPage) => {
    setPage(newPage);
  };

  const handleChangeRowsPerPage = (event) => {
    setRowsPerPage(+event.target.value);
    setPage(0);
  };

  return (
    <React.Fragment>
      <CssBaseline />
      <AppBar position="fixed" color="default" elevation={0} className={classes.appBar}>
        <Toolbar>
            <img src={logo} className={classes.logo} alt="Logo"/>
            <Typography  component="h6" variant="h6" color="textPrimary" noWrap>
              Agora Accounting
            </Typography>
          <div className={classes.nav}>
            <Link variant="button" color="textPrimary" href="#" className={classes.link}>
              Agora
            </Link>
            <Link variant="button" color="textPrimary" href="#" className={classes.link}>
              Catalogue
            </Link>
            <Link variant="button" color="textPrimary" href="#" className={classes.link}>
              Support
            </Link>
          </div>
        </Toolbar>
      </AppBar>
      {/* Hero unit */}
      <Container maxWidth="md" component="main" className={classes.heroContent}>
        <Typography component="h1" variant="h2" align="center" color="textPrimary">
          This Month
        </Typography>
        <Typography variant="h5" align="center" color="textSecondary" component="p" className={classes.date}>
          March 2021
        </Typography>
      </Container>

      <Container maxWidth="md" component="main">

      <Grid container spacing={2} direction="row" alignItems="center">
          <Grid item key={'10'} xs={12} sm={12} md={2}>
            <Typography component="h5" variant="h5" color="textPrimary">
              Providers
            </Typography>
          </Grid>
            <Grid item xs={12} sm={12} md={4}>
              <Card>
                <CardContent>
                  <div className={classes.cardPricing}>
                    <Typography component="h2" variant="h3" color="textPrimary">
                      10
                    </Typography>
                    <Typography variant="h6" color="textSecondary">
                      /new
                    </Typography>
                  </div>
                </CardContent>
              </Card>
            </Grid>
            <Grid item xs={12} sm={12} md={4}>
              <Card>
                <CardContent>
                  <div className={classes.cardPricing}>
                    <Typography component="h2" variant="h3" color="textPrimary">
                      14
                    </Typography>
                    <Typography variant="h6" color="textSecondary">
                      /updated
                    </Typography>
                  </div>
                </CardContent>
              </Card>
            </Grid>
        </Grid>


        <Grid container spacing={1} alignItems="center">
          <Grid item key={'10'} xs={12} sm={12} md={2}>
            <Typography component="h5" variant="h5" color="textPrimary">
              Resources
            </Typography>
          </Grid>
            <Grid item xs={12} sm={12} md={4}>
              <Card>
                <CardContent>
                  <div className={classes.cardPricing}>
                    <Typography component="h2" variant="h3" color="textPrimary">
                      4
                    </Typography>
                    <Typography variant="h6" color="textSecondary">
                      /new
                    </Typography>
                  </div>
                </CardContent>
              </Card>
            </Grid>
            <Grid item xs={12} sm={12} md={4}>
              <Card>
                <CardContent>
                  <div className={classes.cardPricing}>
                    <Typography component="h2" variant="h3" color="textPrimary">
                      11
                    </Typography>
                    <Typography variant="h6" color="textSecondary">
                      /updated
                    </Typography>
                  </div>
                </CardContent>
              </Card>
            </Grid>
        </Grid>

        <Grid container spacing={1} alignItems="center">
          <Grid item key={'10'} xs={12} sm={12} md={2}>
            <Typography component="h5" variant="h5" color="textPrimary">
              Users
            </Typography>
          </Grid>
            <Grid item xs={12} sm={12} md={8}>
              <Card>
                <CardContent>
                  <div className={classes.cardPricing}>
                    <Typography component="h2" variant="h3" color="textPrimary">
                      21
                    </Typography>
                    <Typography variant="h6" color="textSecondary">
                      /new
                    </Typography>
                  </div>
                </CardContent>
              </Card>
            </Grid>
        </Grid>
      </Container>

      <Container maxWidth="lg" className={classes.heroContent}>
      <Paper className={classes.root}>
      <TableContainer className={classes.container} className={classes.tableBody}>
        <Table stickyHeader aria-label="sticky table">
          <TableHead>
            <TableRow>
              {columns.map((column) => (
                <StyledTableCell
                  key={column.id}
                  align={column.align}
                >
                  {column.label}
                </StyledTableCell>
              ))}
            </TableRow>
          </TableHead>
          <TableBody>
            {rows.slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage).map((row) => {
              return (
                <TableRow hover role="checkbox" tabIndex={-1} key={row.code}>
                  {columns.map((column) => {
                    const value = row[column.id];
                    return (
                      <TableCell key={column.id} align={column.align}>
                        {column.format && typeof value === 'number' ? column.format(value) : value}
                      </TableCell>
                    );
                  })}
                </TableRow>
              );
            })}
          </TableBody>
        </Table>
      </TableContainer>
      <TablePagination
        rowsPerPageOptions={[10, 25, 100]}
        component="div"
        count={rows.length}
        rowsPerPage={rowsPerPage}
        page={page}
        onChangePage={handleChangePage}
        onChangeRowsPerPage={handleChangeRowsPerPage}
      />
    </Paper>
    </Container>
      {/* Footer */}
      <Container maxWidth="md" component="footer" className={classes.footer}>
        <Box mt={5}>
          <Copyright />
        </Box>
      </Container>
      {/* End footer */}
    </React.Fragment>
  );
}