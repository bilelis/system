import React from "react";
import { Box, Typography, Paper, Button, Table, TableBody, TableCell, TableContainer, TableHead, TableRow } from "@mui/material";

const mockBills = [
  { id: 1, guest: "John Doe", room: "101", amount: 250, status: "Paid" },
  { id: 2, guest: "Jane Smith", room: "202", amount: 400, status: "Unpaid" },
];

const Billing: React.FC = () => {
  return (
    <Box p={3}>
      <Typography variant="h4" gutterBottom>
        Billing
      </Typography>
      <TableContainer component={Paper}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Bill ID</TableCell>
              <TableCell>Guest</TableCell>
              <TableCell>Room</TableCell>
              <TableCell>Amount</TableCell>
              <TableCell>Status</TableCell>
              <TableCell>Action</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {mockBills.map((bill) => (
              <TableRow key={bill.id}>
                <TableCell>{bill.id}</TableCell>
                <TableCell>{bill.guest}</TableCell>
                <TableCell>{bill.room}</TableCell>
                <TableCell>${bill.amount}</TableCell>
                <TableCell>{bill.status}</TableCell>
                <TableCell>
                  {bill.status === "Unpaid" && (
                    <Button variant="contained" color="primary">Pay</Button>
                  )}
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </Box>
  );
};

export default Billing;
