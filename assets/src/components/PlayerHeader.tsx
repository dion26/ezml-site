import React from 'react';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';

import { CircleFlag } from 'react-circle-flags';
import logo from "../Logo_MPL.png";
import { useParams } from 'react-router-dom';
import { PlayerModel } from './models/PlayerModel';
import { useAxios } from './useAxios';

const PlayerHeader = () => {
  const {id, slug} = useParams()
  
  let url = `/api/players/${id?.toString()}/${slug}/`;
  
  const [loading, data, error, request] = useAxios<PlayerModel>({method: 'GET', url: url});
  if (loading) return <p>Loading</p>;
  if (error != '') return <p>Error: Invalid Input</p>;
  if (!data) return <p>Data was null</p>;

  return (
    <Box >
      <Card variant='outlined' sx={{border: "none", padding:"0", 
                                    paddingRight: "16px",
                                    display: "flex", 
                                    justifyContent: "flex-start",
                                    borderRadius: "16px 16px 0 0",
                                    gap: "16px"}}>
        <CardMedia 
        component="img"
        image={data.image}
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
                    <CircleFlag countryCode={data.country.toLowerCase()} height="32px"/>
                </IconButton>
                <Typography variant='h6'>{data.nickname}</Typography>
            </Box>
            
            <CardContent sx={{margin:0, padding: 0}}>

                <Typography>{data.fullname}</Typography>
                    
                
                <Typography>Age: {data.get_age}</Typography>
                <Typography>{data.status}</Typography>
                <Typography>{data.alternate_ids}</Typography>
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
