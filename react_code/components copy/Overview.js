const Overview = (props) => {
    const { currentTerm1 } = props;
    return (
      <div>
        <h4>Showing results from the state change in Sibling Search Bar</h4>
        <p>Currently searching for {currentTerm1}</p>
      </div>
    )
    
  }

  export default Overview;