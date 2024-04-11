// Login form using State
import { useState } from "react";

const LoginForm = () => {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
  
    function setEmailHandler(e) {
      setEmail(e.target.value);
    }
  
    function setPasswordHandler(e) {
      setPassword(e.target.value);
    }
  
    return (
      <div>
        <h3>Login form</h3>
        <form>
            <label htmlFor="email">Email:</label><br/>
            <input type="email" placeholder='Your email' onBlur={setEmailHandler} /><br/>
            <label htmlFor="password">Password:</label><br/>
            <input type="password" placeholder='Your password' onBlur={setPasswordHandler} />
        </form>
        <p>This is your email: {email}</p>
        <p>This is your password: {password}</p>
        
      </div>
    )
  }

  export default LoginForm;