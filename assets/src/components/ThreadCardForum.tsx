import {FC} from 'react';

import Box from '@mui/material/Box'
import Card from '@mui/material/Card';

import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardActionArea from '@mui/material/CardActionArea';
import Button from '@mui/material/Button';
import Chip from '@mui/material/Chip';
import {Typography} from '@mui/material';
import Stack from '@mui/material/Stack';
import IconButton from '@mui/material/IconButton'
import Link from '@mui/material/Link';

import KeyboardArrowUpIcon from '@mui/icons-material/KeyboardArrowUp';
import KeyboardArrowDownIcon from '@mui/icons-material/KeyboardArrowDown';
import SaveAltIcon from '@mui/icons-material/SaveAlt';
import ShareIcon from '@mui/icons-material/Share';
import ChatBubbleIcon from '@mui/icons-material/ChatBubble';
import {ThreadCard} from "./ThreadModel";

import { Link as RouterLink, NavLink } from 'react-router-dom';


function countdown(s:number) {
  const d = Math.floor(s / (3600 * 24));
  s  -= d * 3600 * 24;
  const h = Math.floor(s / 3600);
  s  -= h * 3600;
  const m = Math.floor(s / 60);
  s  -= m * 60;
  const tmp = [];
  
  (d) && tmp.push(d + 'd');
  (d || h) && tmp.push(h + 'h');
  (d || h || m) && tmp.push(m + 'm');
  tmp.push(Math.floor(s) + 's');
  if (tmp.length > 2){
    let tmpCompact = tmp.slice(0,2);
    return tmpCompact.join(' ');
  }
  return tmp.join(' ');
}

const ThreadCardForum: FC<ThreadCard> = (props) => {
    const handleClick = () => {
      console.info('You clicked the Chip.');
    };
  
    let upvote_var = ((props.user_upvote == true) ? 'primary' : 'default');
    let downvote_var = ((props.user_downvote == true) ? 'primary' : 'default');
    let for_url = "thread/" + props.slug;
    return (
      <Card variant="filled" sx={{borderRadius: 0, marginTop: "8px", width:"100%"}}>
        <CardActionArea component={RouterLink} exact to={`/${for_url}`}>
            <CardContent>
            <Box display="inline-flex" gap={1}>
                <Typography sx={{ fontSize: 12 }} color="text.secondary" gutterBottom>
                Posted by: 
                </Typography>
                <Link href="#" underline='hover' sx={{ fontSize: 12 }} 
                color="text.secondary" gutterBottom>/{props.host?.username}
                </Link>
                <Typography sx={{ fontSize: 12 }} color="text.secondary" gutterBottom>
                - {countdown(props.posted_since)} ago.
                </Typography>
            </Box>
            
            <Box>
                <Typography variant="h6" component="div">
                {props.name.substring(0,100) + '...'}
                </Typography>
            </Box>
            <Link href="#" underline='always' sx={{ fontSize: 12 }} 
                color="secondary" gutterBottom>twitter.com//asdfs
            </Link>
            <Typography variant="body2">
                {props.text_fill}
            </Typography>
            </CardContent>
        </CardActionArea>
        
        <CardActions>
          <IconButton edge="start" color={upvote_var} aria-label="upvote" component="label">
            <KeyboardArrowUpIcon />
          </IconButton>
          <Typography variant='subtitle2' color="primary">
            {props.get_top_score}
          </Typography>
          <IconButton color={downvote_var} aria-label="downvote" component="label">
            <KeyboardArrowDownIcon />
          </IconButton>
          <Stack spacing={1} direction="row" alignItems="center">
            <Button variant="outlined" color="secondary" startIcon={<ChatBubbleIcon />}>
              {props.total_comments} Comments
            </Button>
            <Button variant="outlined" color="secondary" startIcon={<SaveAltIcon />}>
              Save
            </Button>
            <Button variant="outlined" color="secondary" startIcon={<ShareIcon />}>
              Share
            </Button>
            
          </Stack>
          
          <Chip label={props.topics} onClick={handleClick}/>
          <Link href='#' gutterBottom>Delete</Link>
          
        </CardActions>
      </Card>
    )
  };

export default ThreadCardForum
