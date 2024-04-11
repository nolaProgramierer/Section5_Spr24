import { useState } from 'react';
const Search3 = (props) => {
    // Destructuring props
    const { onSearch } = props;

    // Setting state variables
    const [searchTerm, setSearchTerm] = useState("");
    
    // Defining an event handler
    const handleChange = (e) => {
      setSearchTerm(e.target.value)
      onSearch(e)
    }
    return (
      <div style={searchStyle}>
        <h3>Basic Search Form 3</h3>
      <label htmlFor="search3">Search3: </label>
      <input id="search3" type="text" onChange={handleChange} />
      <p>Searching for: {searchTerm}</p>
    </div>
    )
  }
  const searchStyle = {
    borderBottom: '1px solid black', 
    paddingBottom: "30px"
  }

  export default Search3;
