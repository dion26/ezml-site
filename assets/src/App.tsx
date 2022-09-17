
import { FC } from 'react';
import { BrowserRouter, Route, Routes, Navigate } from 'react-router-dom';
import ColorSystem from './components/ColorSystem';

import Layout from './layout/Layout';
import ComponentPage from './pages/Components/Components';
import Home from './pages/Home/Home';
import {Container} from '@mui/material';
import { useTheme } from "@mui/material/styles";
import Master from './pages/Master/Master'



const App: FC = () => {
  const theme = useTheme();
  return (
    <Container maxWidth="lg" style={{backgroundColor: theme.palette.onPrimary.main, borderRadius: "16px", display: "flex", flexDirection: "column", maxHeight: "100vh", paddingLeft: 0, paddingRight: 0}}>
      <Master />
    </Container>
  )
}

export default App