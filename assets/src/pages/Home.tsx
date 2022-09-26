import React from 'react'
import SplitPane from '../components/SplitPane'
import MainFeeds from '../components/MainFeeds'
import RecentActivities from '../components/RecentActivities'

const Home = () => {
  return (
   <SplitPane
      pageFill={<MainFeeds/>}
      sideFill={<RecentActivities/>}
    /> 
  )
}

export default Home
