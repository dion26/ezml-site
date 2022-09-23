import {useState, useEffect} from 'react';

import axios from 'axios';

import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import Divider from '@mui/material/Divider';
import {Typography} from '@mui/material'

import MainCard from '../components/MainCard';
import {ThreadCard} from "../components/ThreadModel";
import MatchList from '../components/MatchList';

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
      <Grid container columns={7}>
        <Grid item xs={4}>
            <Box height="87vh" display="flex" flexDirection="column">
                <Box flex={1} overflow="auto">
                    {threads.map((thread, index) => (
                        <MainCard key={index} 
                                    name={thread.name} 
                                    text_fill={thread.text_fill}
                                    posted_since={thread.posted_since}
                                    get_top_score={thread.get_top_score}
                                    user_upvote={thread.user_upvote}
                                    user_downvote={thread.user_downvote}
                                    />
                    ))}
 
                </Box>
            </Box>
        </Grid>
        <Grid item xs={3}>
          <Box margin={1}>
            <Typography>
              Upcoming Matches
            </Typography>
            <Divider/>
            <MatchList/>
          </Box>
          <Box margin={1}>
            <Typography>
              Upcoming Matches
            </Typography>
            <Divider/>
            <MatchList/>
          </Box>
        </Grid>
      </Grid>
  )
}

export default Home
