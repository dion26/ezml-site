import {useState, useEffect} from 'react';

import Grid from '@mui/material/Grid';
import Card from '@mui/material/Card';
import CardHeader from '@mui/material/CardHeader';
import CardMedia from '@mui/material/CardMedia';
import CardContent from '@mui/material/CardContent';
import { useParams } from 'react-router-dom'

const ThreadDetail = () => {

  const { threadId } = useParams()

  return (
    <Grid container columns={7} spacing={3} direction="row" 
          alignItems="stretch" overflow="auto">
    
      <Card sx={{
          margin:"16px 16px 0 16px",
          width: 1
      }}>
        <p>234 Likes</p>
        <a>Forum Room</a>
        <p>Posted by User 18 hours ago</p>
        <h1>Title {threadId}</h1>
        <p>Tag</p>
        <p>Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.</p>
        <h6>Comments | Share | Save</h6>
        <CardHeader/>
        <CardMedia/>
        <CardContent>
        </CardContent>
      </Card>

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
