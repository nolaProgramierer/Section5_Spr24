// Special children props
// Defines any content that you want between the opening and closing tags
const Children = (props) => {
    return (
      <div>
        <h3>Children Example</h3>
        <li>{props.children} (ID: {props.id})</li>
      </div>
    ) 
  }

  export default Children;