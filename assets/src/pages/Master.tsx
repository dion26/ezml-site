import React, {FC} from 'react';
import Grid from '@mui/material/Grid';
import { Container } from '@mui/material';
import MenuDrawer from '../components/MenuDrawer';
import useTheme from "@mui/material/styles/useTheme";
import Footer from '../components/Footer'

interface MasterProps {
  children: JSX.Element,
}

const Master: FC<MasterProps> = (props) => {
  const { children } = props;
  const theme = useTheme();
  return (
    <Container maxWidth="lg" style={{backgroundColor: theme.palette.onPrimary.main, 
      borderRadius: "16px 16px 0 0 ", display: "flex", flexDirection: "column", 
      maxHeight: "100vh", paddingLeft: 0, paddingRight: 0}}>
      <Grid container spacing={3} justifyContent="sapce-between" alignItems="flex-start"> 
          <Grid item xs={3} >
              <MenuDrawer/>
          </Grid>
          {children}
      </Grid>
      <Footer />
    </Container>
  )
}

export default Master
