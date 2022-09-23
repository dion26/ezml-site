import {useState, useEffect, FC} from 'react';
import React from 'react';

import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import Switch from '@mui/material/Switch';
import IconButton from '@mui/material/IconButton';
import { CircleFlag } from 'react-circle-flags';

import axios from 'axios';

import MenuDrawer from '../components/MenuDrawer';
import SearchBox from '../components/SearchBox';
import BadgeAvatar from '../components/BadgeAvatar';

interface MasterProps {
  pageFill?: React.ReactNode;
  sideFill?: React.ReactNode;
}

const Master: FC<MasterProps> = (props) => {
  const [search, setSearch] = useState<string | number>("");
  const { pageFill } = props

  return (
    <Grid container spacing={3} justifyContent="sapce-between" alignItems="flex-start"> 
        <Grid item xs={3} >
            <MenuDrawer/>
        </Grid>
        <Grid item xs={7}>
            <Box height="13vh">
                <SearchBox search={search} setSearch={setSearch}/>
                <Switch sx={{
                        marginTop: "24px",
                        float: "right"
                      }}/>
            </Box>
            <Box height="87vh" display="flex" flexDirection="column">
              {props.pageFill}
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
          <Box height="87vh">
            {props.sideFill}
          </Box>
        </Grid>
    </Grid>
  )
}

export default Master
