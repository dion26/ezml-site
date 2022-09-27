import { TextField, InputAdornment, TextFieldProps } from '@mui/material';
import SearchIcon from '@mui/icons-material/Search';
import Autocomplete from '@mui/material/Autocomplete'
import { styled } from '@mui/material/styles';
import { PlayerModel } from './models/PlayerModel';
import { FC, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import * as _ from 'lodash';

const SearchBoxStyle = styled(TextField)(() => ({
    '& fieldset': {
      borderRadius: "30px",
    },
    width: "70%",
  }));

interface Props{
  search: string | undefined;
  setSearch: React.Dispatch<React.SetStateAction<string | undefined>>;
  options: PlayerModel[]
}

const SearchBox = ({search, setSearch, options}:Props) => {
  const [value, setValue] = useState<PlayerModel | null>(null);
  const navigate = useNavigate();

  const HandleEnter = () => {
    if (!_.isNull(value)) {
      const slug = value.slug
      const id = value.id
      console.log(value)
      navigate('/player/' + id.toString() + '/' + slug)
      setValue(null)
    } else if (!_.isEmpty(search)) {
      navigate('/search/' + search)
    }
  }

  return (
    <Autocomplete
      freeSolo
      id="search-combo"
      filterOptions={(x) => x}
      disableClearable
      options={options.map((option) => option.nickname)}
      renderInput={(params) => (
        <SearchBoxStyle
          {...params}
          placeholder="Search"
          InputProps={{
            ...params.InputProps,
            type: 'search',
            startAdornment: (
              <InputAdornment position="start">
                <SearchIcon />
              </InputAdornment>
            ),
          }}
          variant="outlined"
          margin="normal"
        />
      )}
      onKeyDown={(event:any) => {
        if (event.key === 'Enter') {
          // Prevent's default 'Enter' behavior.
          event.defaultMuiPrevented = false;
          
          HandleEnter()
          // your handler code
        }
      }}
      // inputValue={search}
      onInputChange = {(event, value) => {
        setSearch((event.target as HTMLTextAreaElement).value);
      }}
      onChange={(event: any, newValue: string | null) => {
        setValue(options.filter(obj => obj.nickname == newValue)[0]);
      }}
      sx={{width: "100%", padding:0, margin:0}}
    />
  )
}

export default SearchBox
