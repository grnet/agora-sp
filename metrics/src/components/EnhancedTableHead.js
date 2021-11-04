import React from 'react';
import 'date-fns/format';
import TableRow from '@material-ui/core/TableRow';

import StyledTableCell from './StyledTableCell';
import StyledTableSortLabel from './StyledTableSortLabel';
import TableHead from '@material-ui/core/TableHead';
import { Typography } from '@material-ui/core';

const EnhancedTableHead = (props) => {
  const {
    order,
    orderBy,
    onRequestSort,
    columns
  } = props;
  const createSortHandler = (property) => (event) => {
    onRequestSort(event, property);
  };

  return (
    <TableHead>
      <TableRow>
        {columns.map((headCell) => (
          <StyledTableCell
            key={headCell.id}
            align={headCell.numeric ? "right" : "left"}
            padding={headCell.disablePadding ? "none" : "default"}
            sortDirection={orderBy === headCell.id ? order : false}
          >
            { headCell.sortable ? (
              <StyledTableSortLabel
                active={orderBy === headCell.id}
                direction={orderBy === headCell.id ? order : "asc"}
                onClick={createSortHandler(headCell.id)}
              >
                <Typography>
                  {headCell.label}
                </Typography>
              </StyledTableSortLabel>
            ):(
              <Typography>
                {headCell.label}
              </Typography>
              )
            }
          </StyledTableCell>
        ))}
      </TableRow>
    </TableHead>
  );
}

export default EnhancedTableHead;
