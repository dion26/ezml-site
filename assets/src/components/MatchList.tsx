import React from 'react'
import { Card, CardActionArea, CardMedia, Typography, Box, CardActions } from '@mui/material';
import { CircleFlag } from 'react-circle-flags';
import { height } from '@mui/system';
import tourLogo from "../Logo_MPL.png"
import { styled } from '@mui/material/styles';

const StyledCardActionArea = styled(CardActionArea)(({theme}) => `
    .MuiCardActionArea-focusHighlight {
        background: transparent;
    }
`);

const MatchList = () => {
    const Team1Flag = () => <CircleFlag countryCode="es" height="16px"/>
    const Team2Flag = () => <CircleFlag countryCode="id" height="16px"/>
    let team1Name = "RRQ"
    let team2Name = "Evos"
    let team1Score = 1
    let team2Score = 0
    let status = "01d23h"
    let tournament = "../Logo_MPL.png"

  return (
    <Card variant='filled' sx={{marginTop: "8px"}}>
        <Box display="flex" alignItems="center" justifyContent="space-between">
          <StyledCardActionArea sx={{height:"56px"}}> 
             <Box display="flex" alignItems="center" justifyContent="space-between">
                <Box sx={{width: "80%"}}>
                    <Box display="grid" gridTemplateColumns="1fr 3fr 1fr" >
                        <Box marginTop="4px">
                            <Team1Flag />
                        </Box>
                        <Typography>
                            {team1Name}
                        </Typography>
                        <Typography visibility="visible">
                            {team1Score}
                        </Typography>
                    </Box>
                    <Box display="grid" gridTemplateColumns="1fr 3fr 1fr">
                        <Box marginTop="4px">
                            <Team2Flag />
                        </Box>
                        <Typography>
                            {team2Name}
                        </Typography>
                        <Typography>
                            {team2Score}
                        </Typography>
                    </Box>
                </Box>
            
                <Typography display="inline-block">
                    {status}
                </Typography>
            </Box>
        </StyledCardActionArea>
        <StyledCardActionArea sx={{width: "auto"}}>
            <CardMedia
                        component="img"
                        sx={{ width: "56px", height: "56px" }}
                        image={tourLogo}
                        alt=""
                    />
        </StyledCardActionArea>
        </Box>
    </Card>
  )
}

export default MatchList
