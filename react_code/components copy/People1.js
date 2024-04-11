// List of people using map
function People1(props) {
    return (
      <div>
        <h3>People example 1</h3>
        <ul>
      {props.persons.map((person, index) => {
        return <li key={index}>
          <span><a href={person.ip_address}>{person.ip_address}</a></span>
          <span>{person.email}</span>
          <span>{person.first_name}</span>
          <span>{person.last_name}</span>
          </li>
      })}
    </ul>
      </div>
    )
  }

  export default People1;