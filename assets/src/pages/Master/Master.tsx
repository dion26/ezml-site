import SearchBox from '../../components/SearchBox';
import MenuDrawer from '../../components/MenuDrawer';
import MainCard from '../../components/MainCard';
import Grid from '@mui/material/Grid';
import { styled } from '@mui/material/styles';
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import { FC, useState } from 'react';
import Switch from '@mui/material/Switch';
import MatchList from '../../components/MatchList';
import { Typography, Divider } from '@mui/material';
import { CircleFlag } from 'react-circle-flags';
import IconButton from '@mui/material/IconButton';
import BadgeAvatar from '../../components/BadgeAvatar';
import RecentActivities from '../../components/RecentActivities';

const label = { inputProps: { 'aria-label': 'Switch demo' } };

const Master = () => {
    const [search, setSearch] = useState<string | number>("");
    console.log(search)

  return (
    // <Box sx={{ flexGrow: 2 }}>
      <Grid container spacing={3} justifyContent="sapce-between" >
        <Grid item xs={3} >
            <MenuDrawer/>
        </Grid>
        <Grid item xs={4}>
          <Box height="13vh">
            <SearchBox search={search} setSearch={setSearch}/>
          </Box>
          
          <Box height="87vh" display="flex" flexDirection="column">
            <Box flex={1} overflow="auto">

            </Box>
          </Box>
        </Grid>

        <Grid item xs={3}>
          <Box height="13vh">
            <Switch {...label} sx={{
              marginTop: "24px",
              float: "right"
            }}/>
          </Box>
          <Box height="87vh" display="flex" flexDirection="column">
            <Box flex={1} overflow="auto">
              <Typography variant='button'>
                Upcoming Matches
              </Typography>
              <Divider variant='fullWidth'/>
              <MatchList />
              <MatchList />
              <MatchList />
              <MatchList />
              <MatchList />
              <Typography variant='button'>
                Recent Result
              </Typography>
              <Divider variant='fullWidth'/>
              <MatchList />
              <MatchList />
              <MatchList />
              <MatchList />
              <MatchList />
            </Box>
          </Box>
        </Grid>

        <Grid item xs={2}>
          <Box height="13vh">
            <IconButton sx={{margin: "14px"}}>
              <CircleFlag countryCode="id" height="32px"/>
            </IconButton>
            <IconButton>
              <BadgeAvatar />
            </IconButton>
          </Box>
          <Box height="87vh" display="flex" flexDirection="column">
            <Typography variant='button' sx={{marginTop: "8px"}}>
              Ongoing Events
            </Typography>
            <Divider variant='fullWidth' sx={{marginBottom: "8px"}}/>
            <RecentActivities/>
            <RecentActivities/>
            <RecentActivities/>
            <Typography variant='button' sx={{marginTop: "8px"}}>
              Upcoming Events
            </Typography>
            <Divider variant='fullWidth' sx={{marginBottom: "8px"}}/>
            <RecentActivities/>
            <RecentActivities/>
            <RecentActivities/>
            <Typography variant='button' sx={{marginTop: "8px"}}>
              Recent Activities
            </Typography>
            <Divider variant='fullWidth' sx={{marginBottom: "8px"}}/>
            <RecentActivities/>
            <RecentActivities/>
            <RecentActivities/>
            <RecentActivities/>
            <RecentActivities/>
          </Box>
        </Grid>
      </Grid>
    // </Box>
  )
}

export default Master
