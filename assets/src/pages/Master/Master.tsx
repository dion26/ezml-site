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

const label = { inputProps: { 'aria-label': 'Switch demo' } };

const Master = () => {
    const [search, setSearch] = useState<string | number>("")
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
                <MainCard/>
                <MainCard/>
                <MainCard/>
                <MainCard/>
                <MainCard/>
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
        </Grid>
      </Grid>
    // </Box>
  )
}

export default Master
