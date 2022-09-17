
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

import { useTheme } from "@mui/material/styles";
import logo from "../logo-large.svg"
import CssBaseline from '@mui/material/CssBaseline';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import Typography from '@mui/material/Typography';
import DrawerComponent from './DrawerComponent';



export default function PermanentDrawerLeft() {
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
    const theme = useTheme();



  return (
    <Box 
        sx={{ gap: 0,
            height: "100vh",
            bgcolor: theme.palette.background2.main,
            borderRadius: "16px"    
        }}>
        <AppBar color="default" elevation={0} position="static" sx={{display: 'flex-inline', borderRadius:"16px"}}>
            <Toolbar variant='regular' sx={{ borderRadius:"16px", gap: 3, marginTop: "16px"}}>
                <Box
                    component="img"
                    sx={{
                    width: 48,
                    maxWidth: { xs: 24, md: 48 },
                    }}
                    alt="The house from the offer."
                    src={logo}
                />
                <Typography variant='h5' fontWeight={"bold"}>EZML</Typography>
            </Toolbar>
        </AppBar>
            
        {competitiveCategory.map(({id, children}) => (
        <List key={id} subheader={
            <ListSubheader component="div">
                {id}
            </ListSubheader>}>
            {children.map(({id: childId, icon}) => (
                <ListItem disablePadding key={childId}>
                    <ListItemButton>
                        <ListItemIcon>
                            {icon}
                        </ListItemIcon>
                        <ListItemText primary={childId} />
                    </ListItemButton>
                </ListItem>
            ))}
        </List>
        ))}
        <Divider variant='middle'/>
        {communityCategory.map(({id, children}) => (
        <List key={id} subheader={
            <ListSubheader component="div">
                {id}
            </ListSubheader>}>
            {children.map(({id: childId, icon}) => (
                <ListItem disablePadding key={childId}>
                    <ListItemButton>
                        <ListItemIcon>
                            {icon}
                        </ListItemIcon>
                        <ListItemText primary={childId} />
                    </ListItemButton>
                </ListItem>
            ))}
        </List>
        ))}
        <Divider variant='middle'/>
        {strategyCategory.map(({id, children}) => (
        <List key={id} subheader={
            <ListSubheader component="div">
                {id}
            </ListSubheader>}>
            {children.map(({id: childId, icon}) => (
                <ListItem disablePadding key={childId}>
                    <ListItemButton>
                        <ListItemIcon>
                            {icon}
                        </ListItemIcon>
                        <ListItemText primary={childId} />
                    </ListItemButton>
                </ListItem>
            ))}
        </List>
        ))}
        <Divider variant='middle'/>
    </Box>
  );
}
