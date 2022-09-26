import React from 'react'
import SplitPane from '../components/SplitPane'
import MainPlayerPane from './MainPlayerPane'
import SidePlayerPane from './SidePlayerPane'

const PlayerDetail = () => {
  return (
    <SplitPane
    pageFill={<MainPlayerPane/>}
    sideFill={<SidePlayerPane/>} 
    />
  )
}

export default PlayerDetail
