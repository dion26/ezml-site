import React from 'react'
import Card from '@mui/material/Card'
import CardActionArea from '@mui/material/CardActionArea'
import CardMedia from '@mui/material/CardMedia'
import Typography from '@mui/material/Typography'
import CardContent from '@mui/material/CardContent'
import {Link} from 'react-router-dom'

const SimpleCardSearch = (props) => {
    const {obj} = props;
    const url = 'player/' + obj.id.toString() + '/' + obj.slug 
    return (
    <Card sx={{ maxWidth: 256, flex: 1, minWidth: 256 }}>
        <CardActionArea component={Link} exact to={`/${url}`}>
            <CardMedia
                component="img"
                height="140"
                image={obj.image}
                alt={obj.nickname}
            />
            <CardContent>
                <Typography gutterBottom variant="h5" component="div">
                {obj.nickname}
                </Typography>
                <Typography variant="body2" color="text.secondary">
                {obj.fullname}
                </Typography>
            </CardContent>
        </CardActionArea>
    </Card>
  )
}

export default SimpleCardSearch
