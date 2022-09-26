import React, {FC} from 'react'
import TwitterIcon from '@mui/icons-material/Twitter';
import GoogleIcon from '@mui/icons-material/Google';
import RedditIcon from '@mui/icons-material/Reddit';
import FacebookIcon from '@mui/icons-material/Facebook';
import IconButton from '@mui/material/IconButton';
import Stack from '@mui/material/Stack';
import Typography from '@mui/material/Typography';
import Grid from '@mui/material/Grid';

interface SignProps{
    method: string,
}

const SocialLogo: FC<SignProps> = (props) => {
  return (
    <Grid container marginTop={2}>
        <Grid item xs>
            <Typography justifyContent="center">Or {props.method} with: </Typography>
        </Grid>
        <Grid item>
            <Stack
            direction="row"
            justifyContent="center"
            alignItems="center"
            spacing={2}
            >
            <IconButton aria-label="twitter">
                <TwitterIcon/>
            </IconButton>
            <IconButton aria-label="google">
                <GoogleIcon/>
            </IconButton>
            <IconButton aria-label="reddit">
                <RedditIcon/>
            </IconButton>
            <IconButton aria-label="facebook">
                <FacebookIcon/>
            </IconButton>    
            </Stack>
        </Grid> 
    </Grid>
  )
}

export default SocialLogo
