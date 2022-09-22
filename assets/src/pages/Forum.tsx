import React from 'react'

import Grid from '@mui/material/Grid';

const Forum: React.FC = () => {
  return (
    <Grid container columns={6} spacing={3} justifyContent="sapce-between" alignItems="flex-start">
        <Grid item>
            <h1>This is Forum</h1>
        </Grid>
    </Grid>
  )
}

export default Forum
