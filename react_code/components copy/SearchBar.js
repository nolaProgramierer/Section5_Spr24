// Two sibling components with props passed between them
const SearchBar = (props) => {

    return (
      <div>
        <h3>Sibling Search Bar</h3>
        <input type="search" onChange={props.onUpdateSearch} />
      </div>
    ) 
  }

export default SearchBar;