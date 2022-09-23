
import { FC } from 'react';
import { BrowserRouter, Route, Routes, Navigate } from 'react-router-dom';
import Home from './pages//Home';
import {Container} from '@mui/material';
import useTheme from "@mui/material/styles/useTheme";
import Master from './pages/Master'
import Header from './components/Header'
import Footer from './components/Footer'
import ThreadDetail from './pages/ThreadDetail'
import Forum from './pages/Forum';
import MatchListPage from './pages/MatchListPage';
import MatchDetail from './pages/MatchDetail';
import RecentActivities from './components/RecentActivities';


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
            <Route path='/' element={<Master 
                                        pageFill={<Home/>}
                                        sideFill={<RecentActivities />}
                                        /> }></Route>
            <Route path='/forums' element={<Master 
                                              pageFill={<Forum/>}
                                              sideFill={<RecentActivities />}
                                              />}></Route>
            <Route path='/thread/:slug' element={<Master 
                                            pageFill={<ThreadDetail/>} 
                                            sideFill={<RecentActivities />}
                                            />}></Route>
            <Route path='/matches' element={<Master 
                                            pageFill={<MatchListPage/>} 
                                            sideFill={<RecentActivities />}
                                            />}></Route>
            <Route path='/matches/:id/:slug' element={<Master 
                                            pageFill={<MatchDetail/>} 
                                            sideFill={<RecentActivities />}
                                            />}></Route>
            <Route path='*' element={<Master 
                                        pageFill={<Home/>}
                                        sideFill={<RecentActivities />}
                                        /> }></Route>
                              
        </Routes>
        <Footer/>
      </Container>
    </BrowserRouter> 
  )
}

export default App