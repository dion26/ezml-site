
import { FC } from 'react';
import { BrowserRouter, Route, Routes, Navigate } from 'react-router-dom';
import Home from './pages//Home';
import {Container} from '@mui/material';
import { useTheme } from "@mui/material/styles";
import Master from './pages/Master'
import Header from './components/Header'
import Footer from './components/Footer'
import ThreadDetail from './pages/ThreadDetail'
import Forum from './pages/Forum';


const App: FC = () => {
  const theme = useTheme();
  return (
    <BrowserRouter>
      <Container maxWidth="lg" style={{backgroundColor: theme.palette.onPrimary.main, 
            borderRadius: "16px 16px 0 0 ", display: "flex", flexDirection: "column", 
            maxHeight: "100vh", paddingLeft: 0, paddingRight: 0}}>
        {/* <Header /> */}
        <Routes>
            {/* <Master /> */}
            <Route path='/' element={<Home/>}></Route>
            <Route path='/thread/:threadId/:slug' element={<Master pageFill={<ThreadDetail/>}/>}></Route>
        </Routes>
        <Footer/>
      </Container>
    </BrowserRouter> 
  )
}

export default App