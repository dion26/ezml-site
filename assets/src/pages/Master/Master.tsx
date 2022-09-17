import SearchBox from '../../components/SearchBox';
import MenuDrawer from '../../components/MenuDrawer';
import MainCard from '../../components/MainCard';
import Grid from '@mui/material/Grid';
import { styled } from '@mui/material/styles';
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import { FC, useState } from 'react';
import Switch from '@mui/material/Switch';

const Item = styled(Paper)(({ theme }) => ({
    backgroundColor: theme.palette.mode === 'dark' ? theme.palette.background2.main : theme.palette.background2.dark,
    ...theme.typography.body2,
    padding: theme.spacing(1),
    textAlign: 'center',
    color: theme.palette.text.secondary,
  }));

const label = { inputProps: { 'aria-label': 'Switch demo' } };

const Master = () => {
    const [search, setSearch] = useState<string | number>("")
    console.log(search)

  return (
    // <Box sx={{ flexGrow: 2 }}>
      <Grid container spacing={3} justifyContent="sapce-between" >
        <Grid item xs={3} >
            <MenuDrawer/>
        </Grid>
        <Grid item xs={4}>
          <SearchBox search={search} setSearch={setSearch}/>
          <Box height="85vh" display="flex" flexDirection="column">
            <Box flex={1} overflow="auto">
                <MainCard/>
                <MainCard/>
                <MainCard/>
                <MainCard/>
                <MainCard/>
            </Box>
          </Box>
        </Grid>
        <Grid item xs={3}>
        <Switch {...label} />
        </Grid>
        <Grid item xs={2}>
          <Item>Recent</Item>
        </Grid>
      </Grid>
    // </Box>
  )
}

export default Master
