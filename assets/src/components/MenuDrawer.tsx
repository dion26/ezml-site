
import Box from '@mui/material/Box';
import ScoreboardIcon from '@mui/icons-material/Scoreboard';
import EmojiEventsIcon from '@mui/icons-material/EmojiEvents';
import MilitaryTechIcon from '@mui/icons-material/MilitaryTech';
import BarChartIcon from '@mui/icons-material/BarChart';
import ForumIcon from '@mui/icons-material/Forum';
import ModeStandbyIcon from '@mui/icons-material/ModeStandby';
import AppRegistrationIcon from '@mui/icons-material/AppRegistration';

import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import Divider from '@mui/material/Divider';
import ListSubheader from '@mui/material/ListSubheader';
import { AppBar, Toolbar } from '@mui/material';

import { useTheme, styled } from "@mui/material/styles";
import logo from "../logo-large.svg"
import {Typography} from '@mui/material';

import { Link, NavLink } from 'react-router-dom';


const ActiveListItemButton = styled(ListItemButton)({
    '&.active .MuiTypography-root': {
      fontWeight: 'bold',
    },
  });

export default function PermanentDrawerLeft() {
    
    const theme = useTheme();
    const ActiveListItem = styled(ListItem)({
        "&.active": {
            background:theme.palette.primaryContainer.main,
            textDecoration: "none", 
            color: "inherit",
            borderRadius: "32px",
          },
        textDecoration: "none", 
        color: "inherit"
      });
    const competitiveCategory = [
        {
            id: 'Competitive',
            children: [
                {
                    id: 'Matches',
                    icon: <ScoreboardIcon />
                },
                {
                    id: 'Events',
                    icon: <EmojiEventsIcon />
                },
                {
                    id: 'Rankings',
                    icon: <MilitaryTechIcon />
                },
                {
                    id: 'Stats',
                    icon: <BarChartIcon />
                },
            ],
        },
    ];

    const communityCategory = [
        {
            id: 'Community',
            children: [
                {
                    id: 'Forums',
                    icon: <ForumIcon />
                },
                {
                    id: 'Pickems',
                    icon: <ModeStandbyIcon />
                },
            ],
        },
    ];

    const strategyCategory = [
        {
            id: 'Strategy',
            children: [
                {
                    id: 'Strategy Planner',
                    icon: <AppRegistrationIcon />
                },
            ],
        },
    ];
    

  return (
    <Box 
        sx={{ gap: 0,
            height: "100vh",
            bgcolor: theme.palette.background2.main,
            borderRadius: "16px"    
        }}>
        <AppBar color="default" elevation={0} position="static" sx={{display: 'flex-inline', borderRadius:"16px"}}>
            <Toolbar variant='regular' sx={{ borderRadius:"16px", gap: 3, marginTop: "16px"}}>
               <Link style={{textDecoration: "none", color: "inherit", 
                            display:"flex", gap:"16px", 
                            alignItems:"center"}} to={'/'}>
                <Box
                        component="img"
                        sx={{
                        width: 48,
                        maxWidth: { xs: 24, md: 48 },
                        }}
                        alt="EZML"
                        src={logo}
                    />
                    
                    <Typography variant='h5' fontWeight={"bold"}>EZML</Typography>
                </Link>
            </Toolbar>
        </AppBar>
            
        {competitiveCategory.map(({id, children}) => (
        <List key={id} subheader={
            <ListSubheader component="div">
                <Typography variant='button'>
                    {id}
                </Typography>
                
            </ListSubheader>}>
            {children.map(({id: childId, icon}) => (
                // <Link style={{textDecoration: "none", color: "inherit"}} to={`/${childId}`}>
                <ActiveListItem disablePadding key={childId} component={NavLink} exact to={`/${childId}`}>   
                        <ListItemButton>
                            <ListItemIcon>
                                {icon}
                            </ListItemIcon>
                            <ListItemText primary={childId} />
                        </ListItemButton>
                </ActiveListItem>
                // </Link>
            ))}
        </List>
        ))}
        <Divider variant='middle'/>
        {communityCategory.map(({id, children}) => (
        <List key={id} subheader={
            <ListSubheader component="div">
                <Typography variant='button'>
                    {id}
                </Typography>
            </ListSubheader>}>
            {children.map(({id: childId, icon}) => (
                    <ActiveListItem disablePadding key={childId} component={NavLink} exact to={`/${childId}`}>
                        <ListItemButton>
                            <ListItemIcon>
                                {icon}
                            </ListItemIcon>
                            <ListItemText primary={childId} />
                        </ListItemButton>
                    </ActiveListItem>

            ))}
        </List>
        ))}
        <Divider variant='middle'/>
        {strategyCategory.map(({id, children}) => (
        <List key={id} subheader={
            <ListSubheader component="div">
                <Typography variant='button'>
                    {id}
                </Typography>
            </ListSubheader>}>
            {children.map(({id: childId, icon}) => (
                <ActiveListItem disablePadding key={childId} component={NavLink} exact to={`/${childId}`}>
                    <ListItemButton>
                        <ListItemIcon>
                            {icon}
                        </ListItemIcon>
                        <ListItemText primary={childId} />
                    </ListItemButton>
                </ActiveListItem>
            ))}
        </List>
        ))}
        <Divider variant='middle'/>
    </Box>
  );
}
