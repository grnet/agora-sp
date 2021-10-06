import React from 'react';
import Paper from '@material-ui/core/Paper';
import Container from '@material-ui/core/Container';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableRow from '@material-ui/core/TableRow';
import TablePagination from '@material-ui/core/TablePagination';
import { Typography } from '@material-ui/core';

import EnhancedTableHead from './EnhancedTableHead';
import useStyles from '../styles/AppStyles';
import CONFIG from '../config';
import { get_month } from '../utils/Month';

const columns = [
  { id: 'year', label: 'Year', minWidth: 170, sortable: true},
  { id: 'month', label: 'Month', minWidth: 170, sortable: false},
  { id: 'new_providers', label: 'New providers', minWidth: 170,sortable: true },
  { id: 'updated_providers', label: 'Updated providers', minWidth: 170, sortable: true },
  { id: 'updated_providers_total', label: 'Total provider updates', minWidth: 170, sortable: true },
  { id: 'new_resources', label: 'New resources', minWidth: 170,sortable: true },
  { id: 'updated_resources', label: 'Updated resources', minWidth: 170, sortable: true },
  { id: 'updated_resources_total', label: 'Total resource updates', minWidth: 170, sortable: true },
  { id: 'new_users', label: 'New users', minWidth: 170, sortable: true },
];

const descendingComparator = (a, b, orderBy) => {
  if (b[orderBy] < a[orderBy]) {
    return -1;
  }
  if (b[orderBy] > a[orderBy]) {
    return 1;
  }
  return 0;
}

const getComparator = (order, orderBy) => {
  return order === "desc"
    ? (a, b) => descendingComparator(a, b, orderBy)
    : (a, b) => -descendingComparator(a, b, orderBy);
}


const createData = (
  month,
  year,
  new_providers,
  updated_providers,
  updated_providers_total,
  new_resources,
  updated_resources,
  updated_resources_total,
  new_users
) => {
  return {
    month: get_month(month),
    month_num: month,
    year,
    new_providers,
    updated_providers,
    updated_providers_total,
    new_resources,
    updated_resources,
    updated_resources_total,
    new_users,
  };
};

const compare_date = (a, b) => {
  if (a.year > b.year) {
    return -1;
  } else if (b.year > a.year) {
    return 1;
  } else {
    if (a.month_num > b.month_num) return -1;
    else return 1;
  }
};

const sortByField = (array, comparator) => {
  const stabilizedThis = array.map((el, index) => [el, index]);
  stabilizedThis.sort((a, b) => {
    const order = comparator(a[0], b[0]);
    if (order !== 0) return order;
    return a[1] - b[1];
  });
  return stabilizedThis.map((el) => el[0]);
}

const NumberContainer = (props) => {
  const value = props.value;
  let objValue =  <Typography>{value}</Typography>
  if (typeof value === 'number'){
    if ( value === 0 ) {
      objValue = <Typography style={{color: 'grey'}}>{value}</Typography>
    }
  }
  return (
    <>
      {objValue}
    </>
  );
}

const PreviousMonths = () => {
  const classes = useStyles();
  const [page, setPage] = React.useState(0);
  const [rowsPerPage, setRowsPerPage] = React.useState(10);
  const [rows, setRows] = React.useState([]);
  const [order, setOrder] = React.useState("asc");
  const [orderBy, setOrderBy] = React.useState("date");

  const handleChangePage = (event, newPage) => {
    setPage(newPage);
  };

  const handleChangeRowsPerPage = (event) => {
    setRowsPerPage(+event.target.value);
    setPage(0);
  };
  React.useEffect(() => {
    fetch(`${CONFIG.endpoint}/api/v2/monthly_stats`)
      .then((res) => res.json())
      .then((result) => {
        setRows(
          result
            .map((entry) =>
              createData(
                entry.month,
                entry.year,
                entry.new_providers,
                entry.updated_providers,
                entry.updated_providers_total,
                entry.new_resources,
                entry.updated_resources,
                entry.updated_resources_total,
                entry.new_users
              )
            )
            .sort(compare_date)
        );
      });
  }, []);

  const handleRequestSort = (event, property) => {
    const isAsc = orderBy === property && order === "asc";
    setOrder(isAsc ? "desc" : "asc");
    setOrderBy(property);
  };

  return (
    <>
      <Container maxWidth="sm" component="main" className={classes.title}>
        <Typography style={{ fontWeight: 600}} component="h1" variant="h4" color="textPrimary">
          Previous Months
        </Typography>
      </Container>

      <Container maxWidth="lg" className={classes.heroContent}>
        <Paper className={classes.root} style={{ borderRadius: '20px'}}>
          <TableContainer className={classes.tableBody} style={{ borderRadius: '20px'}}>
            <Table stickyHeader aria-label="sticky table">
              <EnhancedTableHead
                columns={columns}
                order={order}
                orderBy={orderBy}
                onRequestSort={handleRequestSort}
              />
              <TableBody>
                {sortByField(rows,getComparator(order, orderBy))
                  .slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage)
                  .map((row) => {
                    return (
                      <TableRow
                        hover
                        tabIndex={-1}
                        key={row.year.toString().concat(row.month)}
                      >
                        {columns.map((column) => {
                          const value = row[column.id];
                          return (
                            <TableCell key={column.id} align={column.align}>
                                <NumberContainer value={value} />
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
    </>
  );
};

export default PreviousMonths;
