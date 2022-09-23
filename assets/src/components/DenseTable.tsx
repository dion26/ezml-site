import * as React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';

import AcUnitIcon from '@mui/icons-material/AcUnit';

function createData(
  name: string,
  acs: number,
  fat: number,
  carbs: number,
  protein: number,
  icon?: any,
) {
  return { name, icon, acs, fat, carbs, protein };
}

const rows = [
  createData('Player 1',159, 6.0, 24, 4.0,  <AcUnitIcon/>),
  // createData('Player 2', 237, 9.0, 37, 4.3),
  // createData('Player 3', 262, 16.0, 24, 6.0),
  // createData('Player 4', 305, 3.7, 67, 4.3),
  // createData('Player 5', 356, 16.0, 49, 3.9),
];

export default function DenseTable() {
  return (
    <TableContainer component={Paper}>
      <Table sx={{ minWidth: 800, padding: 0 }} size="small" aria-label="a dense table">
        <TableHead>
          <TableRow>
            <TableCell width="30%"></TableCell>
            <TableCell align="right" width="5%">ACS</TableCell>
            <TableCell align="right" width="5%">K</TableCell>
            <TableCell align="right" width="5%">D</TableCell>
            <TableCell align="right" width="5%">A</TableCell>
            <TableCell align="right" width="5%">+/-</TableCell>
            <TableCell align="right" width="5%">DG</TableCell>
            <TableCell align="right" width="5%">DT</TableCell>
            <TableCell align="right" width="5%">TG</TableCell>
            <TableCell align="right" width="5%">DGM</TableCell>
            <TableCell align="right" width="5%">DTM</TableCell>
            <TableCell align="right" width="5%">GPM</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <TableRow
              key={row.name}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              <TableCell component="th" scope="row">
                {row.name}
              </TableCell>
              <TableCell align="right">{row.icon}</TableCell>
              <TableCell align="right">{row.acs}</TableCell>
              <TableCell align="right">{row.fat}</TableCell>
              <TableCell align="right">{row.carbs}</TableCell>
              <TableCell align="right">{row.protein}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}
