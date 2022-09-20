import {useState, useEffect} from 'react';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import Switch from '@mui/material/Switch';
import IconButton from '@mui/material/IconButton';

import BadgeAvatar from './BadgeAvatar';
import MenuDrawer from './MenuDrawer';
import SearchBox from './SearchBox';

import { CircleFlag } from 'react-circle-flags';

const Header = () => {
    const [search, setSearch] = useState<string | number>("");

  return (
    <Grid container spacing={3} justifyContent="sapce-between" alignItems="flex-start"> 
        <Grid item xs={3} >
            <MenuDrawer/>
        </Grid>
        <Grid item xs={4} bgcolor="red">
            <Box height="13vh">
                <SearchBox search={search} setSearch={setSearch}/>
            </Box>
        </Grid>
        <Grid item xs={3}>
          <Box height="13vh">
            <Switch sx={{
              marginTop: "24px",
              float: "right"
            }}/>
          </Box>
        </Grid>
        <Grid item xs={2}>
          <Box height="13vh">
            <IconButton sx={{margin: "14px"}}>
              <CircleFlag countryCode="id" height="32px"/>
            </IconButton>
            <IconButton>
              <BadgeAvatar />
            </IconButton>
          </Box>
        </Grid>
    </Grid>
  )
}

export default Header
