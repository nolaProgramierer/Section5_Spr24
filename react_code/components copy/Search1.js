// A Form that console logs what is typed into the input form
export default function Search1() {
    
    const handleChange = (e) => {
      // Synthetic event
      console.log(e);
      // value of target (here: the element)
      console.log(e.target.value);
    }

    return (
      <div style={searchStyle}>
        <h3>Basic Search Form1</h3>
        <label htmlFor="search">Search1: </label>
        <input id="search1" type="text" onChange={handleChange} />
      </div>
      
    )
  }
  
  const searchStyle = {
    borderBottom: '1px solid black', 
    paddingBottom: "30px"
  }