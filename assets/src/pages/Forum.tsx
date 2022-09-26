import {useState, useEffect, FC} from 'react';
import axios from 'axios';

import Box from '@mui/material/Box'
import Chip from '@mui/material/Chip';
import {Typography} from '@mui/material';
import Stack from '@mui/material/Stack';
import Divider from '@mui/material/Divider';
import Button from '@mui/material/Button';

import WhatshotIcon from '@mui/icons-material/Whatshot';
import VerticalAlignTopIcon from '@mui/icons-material/VerticalAlignTop';
import NewReleasesIcon from '@mui/icons-material/NewReleases';

import {ThreadCard} from "../components/ThreadModel";
import ThreadCardForum from '../components/ThreadCardForum';

const Forum: React.FC = () => {
  const handleClick = () => {
    console.info('You clicked the Chip.');
  };

  let [threads, setThreads] = useState<ThreadCard[]>([])

    useEffect(() => {
        getThreads();
    }, [])

    const apiUrl = '/api/forums/';

    let getThreads = async () => {
        let response = await axios.get(apiUrl)
        console.log(response)
        let data = response.data
        setThreads(data)
    }
    
  return (
    <Box flex={1} overflow="auto" sx={{gap: "16px"}}>
      <Stack spacing={1} direction="row" marginBottom={2}>
        <Chip icon={<NewReleasesIcon />} label="New" onClick={handleClick}/>
        <Chip icon={<WhatshotIcon />} label="Hot" onClick={handleClick}/>
        <Chip icon={<VerticalAlignTopIcon />} label="Top" onClick={handleClick}/>
        <Button>Post</Button>
      </Stack>
      <Divider/>
      <Box marginTop={2}>
      {threads.map((thread, index) => (
        <ThreadCardForum key={thread.id} 
                  name={thread.name} 
                  text_fill={thread.text_fill}
                  total_comments={thread.total_comments}
                  host={thread.host}
                  posted_since={thread.posted_since}
                  get_top_score={thread.get_top_score}
                  user_upvote={thread.user_upvote}
                  user_downvote = {thread.user_downvote}
                  topics = {thread.topics}
                  slug = {thread.slug}
                />
        ))}
      </Box>
    </Box>
  )
}

export default Forum
