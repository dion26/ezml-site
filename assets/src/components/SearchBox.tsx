import { TextField, InputAdornment, TextFieldProps } from '@mui/material';
import SearchIcon from '@mui/icons-material/Search';
import { styled } from '@mui/material/styles';
import { FC } from 'react';

const SearchBoxStyle = styled(TextField)(() => ({
    '& fieldset': {
      borderRadius: "30px",
    },
    width: "70%",
  }));

interface Props{
  search: string | number;
  setSearch: React.Dispatch<React.SetStateAction<string | number>>;
}

const SearchBox = ({search, setSearch}:Props) => {
    
  return (
    <SearchBoxStyle
        id="search-box"
        placeholder="Search"
        value={search}
        onChange={
          (e)=>setSearch(e.target.value)
        }
        InputProps={{
          startAdornment: (
            <InputAdornment position="start">
              <SearchIcon />
            </InputAdornment>
          ),
        }}
        variant="outlined"
        margin="normal"
      />
  )
}

export default SearchBox
