// A basic HTML form which doesn't do anything other than render the form
export default function Search0() {
    return (
      <div style={{ borderBottom: '1px solid black', paddingBottom: "30px"}}>
        <h3>Basic Search Form0</h3>
          <label htmlFor="search">Search: </label>
          <input id="search" type="text" />
      </div>
    )
  }
  