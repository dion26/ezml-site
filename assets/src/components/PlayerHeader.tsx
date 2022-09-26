import React from 'react';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';

import { CircleFlag } from 'react-circle-flags';
import logo from "../Logo_MPL.png";

const PlayerHeader = () => {
  return (
    <Box >
      <Card variant='outlined' sx={{border: "none", padding:"0", 
                                    paddingRight: "16px",
                                    display: "flex", 
                                    justifyContent: "space-between",
                                    borderRadius: "16px 16px 0 0"}}>
        <CardMedia 
        component="img"
        image={logo}
        alt="Name"
        sx={{width: 198, 
            height: 198,
            backgroundColor: "white",
            marginLeft: 0,
            marginTop: 0,
            }}
        />
        <Box sx={{ display: 'flex', flexDirection: 'column', alignItems: "flex-start" }}>
            <Box sx={{display: 'flex', alignItems: "center"}}>
                <IconButton sx={{margin: "16px"}}>
                    <CircleFlag countryCode="id" height="32px"/>
                </IconButton>
                <Typography variant='h6'>ALBERTTT</Typography>
            </Box>
            
            <CardContent sx={{margin:0, padding: 0}}>

                <Typography>Albert Neilsen Iskandar</Typography>
                    
                
                <Typography>Age: 20</Typography>
                <Typography>@rrq_alberttt</Typography>
                <Typography>RRQ ALBERTTT</Typography>
            </CardContent>
        </Box>
        <Box sx={{ display: 'flex', flexDirection: 'column', 
                    alignItems: "flex-start",
                    justifyContent: "center" }}>
            <Typography>Current Team: </Typography>
        </Box>
      </Card>
      <Card variant="outlined" sx={{borderRadius: "0 0 16px 16px"}}>Trophy</Card>
    </Box>
  )
}

export default PlayerHeader
