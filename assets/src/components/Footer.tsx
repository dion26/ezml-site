import React from 'react'
import Box from '@mui/material/Box';
import { useTheme } from "@mui/material/styles";
import Typography from '@mui/material/Typography';
import List from '@mui/material/List';
import ListItemText from '@mui/material/ListItemText';

const Footer = () => {
  const theme = useTheme();
  return (
    <footer>
      <Box sx={{
        backgroundColor: theme.palette.tertiaryContainer.main,
        color: theme.palette.onTertiaryContainer.main,
        borderRadius: "0 0 16px 16px",
      }}>
        <List sx={{
          display: 'flex',
          flexWrap: 'wrap',}}>
          <ListItemText><Typography>Contact</Typography></ListItemText>
          <ListItemText><Typography>Privacy</Typography></ListItemText>
          <ListItemText><Typography>© 2022 EZML. All rights reserved.</Typography></ListItemText>
          <ListItemText><Typography>Find us on:</Typography></ListItemText>
        </List>  
      </Box>
    </footer>
  )
}

export default Footer
