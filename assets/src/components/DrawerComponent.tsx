import React, { FC } from 'react'
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import ListSubheader from '@mui/material/ListSubheader';
import SvgIcon from '@mui/material/SvgIcon';

interface Children {
    id: string;
    icon: JSX.Element;
}

interface Category {
    id: string;
    children: Children[]
}

const DrawerComponent: FC<Category[]> = (category) => {
  return (
    <>
      {category.map(({id, children}) => (
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
    </>
  )
}

export default DrawerComponent
