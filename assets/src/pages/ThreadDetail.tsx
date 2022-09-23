import {useState, useEffect} from 'react';

import Grid from '@mui/material/Grid';
import Card from '@mui/material/Card';
import CardHeader from '@mui/material/CardHeader';
import CardMedia from '@mui/material/CardMedia';
import CardContent from '@mui/material/CardContent';
import { useParams } from 'react-router-dom'
import ThreadCardForum from '../components/ThreadCardForum';

const ThreadDetail = () => {

  const { slug } = useParams()

  return (
    <Grid container columns={7} spacing={3} direction="row" 
          alignItems="stretch" overflow="auto">
      <ThreadCardForum key={1} 
                  name="This is title" 
                  text_fill="this is fill"
                  total_comments={2}
                  host={{"username" : "Dion"}}
                  posted_since={12344}
                  get_top_score={32}
                  user_upvote={true}
                  user_downvote = {false}
                  topics = "general"/>
      

      <Card sx={{width: 1, margin:"16px 16px 0 16px",}}>
        <CardHeader/>
        <CardMedia/>
        <CardContent>

        </CardContent>
      </Card>

    </Grid>
  )
}

export default ThreadDetail
