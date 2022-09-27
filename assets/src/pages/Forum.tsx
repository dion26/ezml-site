import React from 'react'
import SplitPane from '../components/SplitPane'
import ForumPane from './ForumPane'

const Forum = () => {
  return (
    <>
      <SplitPane 
        pageFill={<ForumPane/>}
        sideFill={<></>}
      />
    </>
  )
}

export default Forum
