import {useState, useEffect} from 'react';

import axios from 'axios';

import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import Switch from '@mui/material/Switch';
import IconButton from '@mui/material/IconButton';

import MenuDrawer from '../components/MenuDrawer';
import SearchBox from '../components/SearchBox';
import MainCard from '../components/MainCard';
import {ThreadCard} from "../components/ThreadModel";

import { CircleFlag } from 'react-circle-flags';
import BadgeAvatar from '../components/BadgeAvatar';

const Home = () => {
    const [search, setSearch] = useState<string | number>("");

    let [threads, setThreads] = useState<ThreadCard[]>([])

    useEffect(() => {
        getThreads();
    }, [])

    const apiUrl = '/api/forums/';

    let getThreads = async () => {
        let response = await axios.get(apiUrl);
        let data = response.data
        setThreads(data)
    }
  return (
    <Grid container spacing={3} justifyContent="sapce-between" alignItems="flex-start"> 
        <Grid item xs={3} >
            <MenuDrawer/>
        </Grid>
        <Grid item xs={4}>
            <Box height="13vh">
                <SearchBox search={search} setSearch={setSearch}/>
            </Box>
            <Box height="87vh" display="flex" flexDirection="column">
                <Box flex={1} overflow="auto">
                    {threads.map((thread, index) => (
                        <MainCard name={thread.name} text_fill={thread.text_fill}/>
                    ))}
 
                </Box>
            </Box>
        </Grid>
        <Grid item xs={3}>
          <Box height="13vh">
            <Switch sx={{
              marginTop: "24px",
              float: "right"
            }}/>
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
        </Grid>
    </Grid>
  )
}

export default Home
