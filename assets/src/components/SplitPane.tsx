import React, {FC, useEffect, useState} from 'react'
import SearchBox from '../components/SearchBox';
import BadgeAvatar from '../components/BadgeAvatar';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import Switch from '@mui/material/Switch';
import IconButton from '@mui/material/IconButton';
import Button from '@mui/material/Button';
import { CircleFlag } from 'react-circle-flags';
import { Link } from 'react-router-dom';
import axios from 'axios'

interface PaneProps {
    pageFill: JSX.Element,
    sideFill: JSX.Element,
}

function Avatar(isLogIn:boolean) {
  if (isLogIn){
  return (<IconButton>
    <BadgeAvatar />
  </IconButton>);
} else {
  return (<Button color="success" component={Link} to="/signin">Sign In</Button>);
}}

const SplitPane: FC<PaneProps> = (props) => {
    const [search, setSearch] = useState<string | undefined>("");
    const [options, setOptions] = useState([]);
    const {pageFill, sideFill} = props
    let url = `/api/search/?q=${search}`;

    useEffect(() => {
      const timer = setTimeout(() => {
        axios({method: 'GET', url: url, headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
        },})
        .then(response => {
            setOptions(response.data);
        })
        .catch(error => {
            console.log('error geting search API call');
        });
      }, 700);
      return () => clearTimeout(timer);
    }, [search]);

    const isLogIn = false
    let avatar = Avatar(isLogIn)

  return (
    <>
      <Grid item xs={7}>
        <Box height="13vh" display="flex">
            <SearchBox search={search} setSearch={setSearch} options={options}/>
            <Switch sx={{
                    marginTop: "24px",
                    float: "right"
                }}/>
        </Box>
        <Box height="87vh" display="flex" flexDirection="column">
        {pageFill}
        </Box>
    </Grid>
    <Grid item xs={2}>
    <Box height="13vh">
        <IconButton sx={{margin: "14px"}}>
          <CircleFlag countryCode="id" height="32px"/>
        </IconButton>
        
        {avatar}
        
    </Box>
    <Box height="87vh">
        {sideFill}
    </Box>
    </Grid>
    </>
  )
}

export default SplitPane
