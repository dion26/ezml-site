import {useState, useEffect} from 'react';

import Grid from '@mui/material/Grid';
import Card from '@mui/material/Card';
import CardHeader from '@mui/material/CardHeader';
import CardMedia from '@mui/material/CardMedia';
import CardContent from '@mui/material/CardContent';
import { useParams } from 'react-router-dom'
import ThreadCardForum from '../components/ThreadCardForum';
import { ThreadCard } from "../components/ThreadModel";
import { useAxios } from '../components/useAxios';

type SlugParam = {
  slug: string;
};

const ThreadDetail = () => {
  let param = useParams<SlugParam>();
  let slug = param.slug;
  let url = `/api/forums/thread/${slug}/`;
  
  const [loading, data, error, request] = useAxios<ThreadCard>({method: 'GET', url: url});
  if (loading) return <p>Loading</p>;
  if (error != '') return <p>{url}</p>;
  if (!data) return <p>Data was null</p>;

  return (
    <Grid container columns={7} spacing={3} direction="row" 
          alignItems="stretch" overflow="auto">
      <ThreadCardForum key={data?.id} 
                        name={data?.name} 
                        text_fill={data?.text_fill}
                        total_comments={data?.total_comments}
                        host={data?.host}
                        posted_since={data?.posted_since}
                        get_top_score={data?.get_top_score}
                        user_upvote={data?.user_upvote}
                        user_downvote = {data?.user_downvote}
                        topics = {data?.topics}
                        slug = {data?.slug}
                  />

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
