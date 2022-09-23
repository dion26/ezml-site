import {FC} from 'react'
import Card from '@mui/material/Card';
import CardHeader from '@mui/material/CardHeader';
import CardMedia from '@mui/material/CardMedia';
import Avatar from '@mui/material/Avatar';
import IconButton from '@mui/material/IconButton';
import MoreVertIcon from '@mui/icons-material/MoreVert';
import CardContent from '@mui/material/CardContent';
import CardActions from '@mui/material/CardActions';
import FavoriteIcon from '@mui/icons-material/Favorite';
import ShareIcon from '@mui/icons-material/Share';
import Typography from '@mui/material/Typography';
import KeyboardArrowUpIcon from '@mui/icons-material/KeyboardArrowUp';
import KeyboardArrowDownIcon from '@mui/icons-material/KeyboardArrowDown';
import { Button } from '@mui/material';
import {ThreadCard} from "./ThreadModel";
import { styled } from '@mui/material/styles';


const MainCard: FC<ThreadCard> = (props) => {
    return (
    <Card sx={{ maxWidth: "100%", marginBottom: "16px"}} variant="filled">
        <CardHeader
        avatar={
            <Avatar sx={{ bgcolor: "red" }} aria-label="recipe">
            R
            </Avatar>
        }
        action={
            <IconButton aria-label="settings">
            <MoreVertIcon />
            </IconButton>
        }
        titleTypographyProps={{variant: "title" }}
        title={props.name.substring(0,60) + '...'}
        subheader="September 14, 2016"
        />

        <CardMedia
        component="img"
        height="194"
        image="/static/images/cards/paella.jpg"
        alt=""
        />
        
        <CardContent>
        <Typography variant="body2" color="text.secondary">
            {props.text_fill}
        </Typography>
        </CardContent>
        <CardActions disableSpacing>
            <Button variant="text" startIcon={<KeyboardArrowUpIcon />}>
            123
            </Button>
            <Button variant="text" startIcon={<KeyboardArrowDownIcon />}>
            123
            </Button>
            <Button variant="text">
            34 Comments
            </Button>
            <IconButton aria-label="share">
                <ShareIcon />
            </IconButton>
        </CardActions>
    </Card>
  )
}

export default MainCard
