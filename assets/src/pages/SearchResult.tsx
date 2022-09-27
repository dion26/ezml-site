import React from 'react'
import {useParams} from 'react-router-dom'
import Typography from '@mui/material/Typography'
import Box from '@mui/material/Box'
import SplitPane from '../components/SplitPane'
import { useAxios } from '../components/useAxios';
import { PlayerModel } from '../components/models/PlayerModel'
import SimpleCardSearch from '../components/SimpleCardSearch'

const SearchResult = () => {
    const {qname} = useParams();
    let url = `/api/search/?q=${qname}`;

    console.log(url)
    const [loading, data, error, request] = useAxios<PlayerModel[]>({method: 'GET', url: url});
    if (loading) return <p>Loading</p>;
    if (error != '') return <p>Error Invalid Input</p>;
    if (!data) return <p>Nothing Found</p>;

    const result = data.map((element) => {
      return <SimpleCardSearch obj={element} />
    })
  return (
    <>
        <SplitPane 
            pageFill={<>
            <Typography variant='h6'>Search Result: "{qname}"</Typography>
            <Box sx={{display: "flex", gap: "32px", 
                      flexWrap: "wrap", overflow: "auto",
                      justifyContent: "flex-start",
                    }}>
              {result}
            </Box>
            </> 
          }
            sideFill={<></>}    
        />
    </>
  )
}

export default SearchResult
