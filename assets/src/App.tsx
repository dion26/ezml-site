
import { FC } from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';

import Master from './pages/Master';
import Home from './pages//Home';
// Auth
import SignIn from './pages/SignIn'
import SignUp from './pages/SignUp';
// Hidden Access
import PlayerDetail from './pages/PlayerDetail';

import Footer from './components/Footer'

const App: FC = () => {
  return (
    <BrowserRouter>
      <Master>
        <Routes>
            <Route path='/' element={<Home/>}></Route>
            <Route path='/signin' element={<SignIn/>}></Route>
            <Route path='/signup' element={<SignUp/>}></Route>
            <Route path='/player/:id/:slug' element={<PlayerDetail/>}></Route>
            {/* <Route path='/forums' element={<Master 
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
                                        /> }></Route> */}
                              
        </Routes>
      </Master>
    </BrowserRouter> 
  )
}

export default App