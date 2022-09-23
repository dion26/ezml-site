import React from 'react'

import Box from '@mui/material/Box';
import Tabs from '@mui/material/Tabs';
import Tab from '@mui/material/Tab';
import {Typography} from '@mui/material';
import Divider from '@mui/material/Divider'

import MatchList from '../components/MatchList'

interface TabPanelProps {
  children?: React.ReactNode;
  index: number;
  value: number;
}

function TabPanel(props: TabPanelProps) {
  const { children, value, index, ...other } = props;

  return (
    <div
      role="tabpanel"
      hidden={value !== index}
      id={`simple-tabpanel-${index}`}
      aria-labelledby={`simple-tab-${index}`}
      {...other}
    >
      {value === index && (
        <Box sx={{ p: 3 }}>
          <Typography>{children}</Typography>
        </Box>
      )}
    </div>
  );
}

function a11yProps(index: number) {
  return {
    id: `simple-tab-${index}`,
    'aria-controls': `simple-tabpanel-${index}`,
  };
}

const MatchListPage = () => {
  const [value, setValue] = React.useState(0);

  const handleChange = (event: React.SyntheticEvent, newValue: number) => {
    setValue(newValue);
  };

  return (
    <Box flex={1} overflow="auto" sx={{gap: "16px"}}>
      <Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
        <Tabs value={value} onChange={handleChange} aria-label="basic tabs example">
          <Tab label="Schedule" {...a11yProps(0)} />
          <Tab label="Result" {...a11yProps(1)} />
        </Tabs>
      </Box>
      <TabPanel value={value} index={0}>
        <Typography>Mon, 12 September 2022</Typography>
        <Divider />
        <MatchList/>
        <MatchList/>
        <MatchList/>
        <MatchList/>
        <MatchList/>
        <MatchList/>
        <MatchList/>
        <MatchList/>
        <MatchList/>
      </TabPanel>
      <TabPanel value={value} index={1}>
        Item Two
      </TabPanel>
    </Box>
  )
}

export default MatchListPage
