const List = ( {persons }) => {
    return (
      <div>
        <h3>List example using map method</h3>
         <ul>
          {persons.map((item) => (
            <Item key={item.id} item={item} />
          ))}
      </ul>
      </div>
     
    )
  }

  const Item = (props) => {
    const { item } = props;
    return (
      <li>
        <span><a href={item.ip_address}>{item.ip_address}</a></span>
        <span>{item.first_last}</span>
        <span>{item.last_last}</span>
        <span>{item.email}</span>
      </li>
    )
  }

  export default List;