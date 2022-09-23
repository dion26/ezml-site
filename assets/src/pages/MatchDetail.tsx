import React from 'react'

import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import Tabs from '@mui/material/Tabs';
import Tab from '@mui/material/Tab';
import {Typography} from '@mui/material';
import Card from '@mui/material/Card';
import CardHeader from '@mui/material/CardHeader';
import CardActions from '@mui/material/CardActions';
import Avatar from '@mui/material/Avatar';
import Stack from '@mui/material/Stack';
import Paper from '@mui/material/Paper';
import {styled} from '@mui/material/styles';
import Divider from '@mui/material/Divider';
import DenseTable from '../components/DenseTable';

interface TabPanelProps {
    children?: React.ReactNode;
    index: number;
    value: number;
  }
  
function TabPanel(props: TabPanelProps) {
const { children, value, index, ...other } = props;

return (
    <div
    role="tabpanel"
    hidden={value !== index}
    id={`simple-tabpanel-${index}`}
    aria-labelledby={`simple-tab-${index}`}
    {...other}
    >
    {value === index && (
        <Box sx={{ p: 3 }}>
        <Typography>{children}</Typography>
        </Box>
    )}
    </div>
);
}

function a11yProps(index: number) {
return {
    id: `simple-tab-${index}`,
    'aria-controls': `simple-tabpanel-${index}`,
};
}



const PickBanLogo = () => {
  return (
    <Grid item container xs={1} alignItems="center" flexDirection="column" rowGap={0.5}> 
        <Avatar aria-label="team1" sx={{ width: 24, height: 24, marginTop:"8px" }}>
            R
        </Avatar>
        <Avatar aria-label="team1" sx={{ width: 16, height: 16, marginBottom:"8px" }}>
            R
        </Avatar>
    </Grid>
  )
}


const Item = styled(Box)(({ theme }) => ({
    ...theme.typography.body2,
    padding: theme.spacing(1),
    textAlign: 'center',
    color: theme.palette.text.secondary,
    display: "flex",
    gap: theme.spacing(1),
    alignItems: "center",
  }));

const MatchDetail = () => {
    const [value, setValue] = React.useState(0);

    const handleChange = (event: React.SyntheticEvent, newValue: number) => {
      setValue(newValue);
    };
  
    return (
      <Box flex={1} overflow="auto" sx={{gap: "16px"}}>
        <Card variant='elevation' sx={{minHeight: "256px"}}>
            <CardHeader
                avatar={
                <Avatar aria-label="event">
                    R
                </Avatar>
                }
                action={
                <Box display="flex" flexDirection="column" alignItems="flex-end">
                    <Typography>
                        Sunday
                    </Typography>
                    <Typography>
                        16 September 2022
                    </Typography>
                </Box>
                
                }
                title="Shrimp and Chorizo Paella"
                subheader="September 14, 2016"
            />
            <CardActions>
                <Stack
                    direction="row"
                    justifyContent="center"
                    alignItems="center"
                    spacing={2}
                    width="100%"
                    minHeight="128px"
                    >
                        <Item>
                            <Box>
                                <Typography variant='h5'> RRQ </Typography>
                                <Typography variant='caption'> [2109] </Typography>
                            </Box>
                            
                            <Avatar aria-label="team1">
                                R
                            </Avatar>
                            
                        </Item>
                        <Item>
                            <Typography variant='h5' color="green">2</Typography>
                            <Typography variant='h5'>:</Typography>
                            <Typography variant='h5'>1</Typography>
                        </Item>
                        <Item>
                            <Avatar aria-label="team1">
                                R
                            </Avatar>
                            <Box>
                                <Typography variant='h5'> RRQ </Typography>
                                <Typography variant='caption'> </Typography>
                            </Box>
                        </Item>
                        
                </Stack>
            </CardActions>
        </Card>
        <Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
          <Tabs value={value} onChange={handleChange} aria-label="basic tabs example">
            <Tab label="Overview" {...a11yProps(0)} />
            <Tab label="Performance" {...a11yProps(1)} />
            <Tab label="Economy" {...a11yProps(2)} />
          </Tabs>
        </Box>
        <TabPanel value={value} index={0}>
            <Paper variant='elevation'>
                <Grid container justifyContent="space-between" alignItems="center" height="64px">
                    <Grid container item xs={2} justifyContent="flex-start" overflow="hidden">
                        <Box>
                            <Typography variant='h4'>10</Typography>
                        </Box>
                        <Box>
                            <Typography variant='body2'>Evos</Typography>
                            <Typography variant='caption'>6</Typography>
                            <Typography variant='caption'> / </Typography>
                            <Typography variant='caption'>4</Typography>
                        </Box>
                    </Grid>

                    <Grid item xs={8}>
                        <Grid container columnGap={0.5} justifyContent="space-between" alignItems="center">
                            <PickBanLogo/>
                            <PickBanLogo/>
                            <PickBanLogo/>
                            <PickBanLogo/>
                            <PickBanLogo/>
                            <Typography variant="h4">:</Typography>
                            <PickBanLogo/>
                            <PickBanLogo/>
                            <PickBanLogo/>
                            <PickBanLogo/>
                            <PickBanLogo/>
                            {/* <Grid item xs={1}><Typography variant="h4">:</Typography></Grid> */}
                        </Grid>
                    </Grid>

                    <Grid container item xs={2} justifyContent="flex-end">
                        <Box>
                            <Typography variant='body2'>RRQ</Typography>
                            <Typography variant='caption'>6</Typography>
                            <Typography variant='caption'> / </Typography>
                            <Typography variant='caption'>4</Typography>
                        </Box>
                        <Box>
                            <Typography variant='h4'>10</Typography>
                        </Box>
                    </Grid>
                </Grid>
                <Divider/>
                <DenseTable/>
            </Paper>

        </TabPanel>
        <TabPanel value={value} index={1}>
          Item Two
        </TabPanel><TabPanel value={value} index={2}>
          Item Three
        </TabPanel>
      </Box>
    )
}

export default MatchDetail
