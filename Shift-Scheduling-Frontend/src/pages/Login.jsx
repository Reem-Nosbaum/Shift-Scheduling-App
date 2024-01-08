import { useState } from "react";
import "../style/Login.css";

// import { useNavigate } from "react-router-dom";

const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [usernameError, setUsernameError] = useState("");
  const [passwordError, setPasswordError] = useState("");
  const [loginError, setLoginError] = useState("");

  // const navigate = useNavigate();

  const onButtonClick = async () => {
    try {
      // Reset errors
      setUsernameError("");
      setPasswordError("");
      setLoginError("");

      // Validate inputs
      if (!username) {
        setUsernameError("Username is required");
        return;
      }

      if (!password) {
        setPasswordError("Password is required");
        return;
      }

      // Make API request to authenticate user
      const response = await fetch("http://127.0.0.1:5000/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          username,
          password,
        }),
      });

      if (!response.ok) {
        throw new Error("Authentication failed");
      }
      const data = await response.json();

      // Extract the token from the response
      const accessToken = data.access_token;

      // Store the token in localStorage or sessionStorage
      // You can use localStorage for a persistent token or sessionStorage for a session-based token
      localStorage.setItem("accessToken", accessToken);

      // Successful authentication, navigate to "/"
      console.log("Authentication successful");
    } catch (error) {
      // Handle authentication error
      console.error("Authentication error:", error);
      setLoginError("Invalid username or password");
    }
  };

  return (
    <div className={"mainContainer"}>
      <div className={"titleContainer"}>
        <div>Login</div>
      </div>
      <br />
      <div className={"inputContainer"}>
        <input
          value={username}
          placeholder="Enter your username here"
          onChange={(ev) => setUsername(ev.target.value)}
          className={"inputBox"}
        />
        <label className="errorLabel">{usernameError}</label>
      </div>
      <br />
      <div className={"inputContainer"}>
        <input
          value={password}
          placeholder="Enter your password here"
          onChange={(ev) => setPassword(ev.target.value)}
          className={"inputBox"}
        />
        <label className="errorLabel">{passwordError}</label>
        <label className="errorLabel">{loginError}</label>
      </div>
      <br />
      <div className={"inputContainer"}>
        <input
          className={"inputButton"}
          type="button"
          onClick={onButtonClick}
          value={"Log in"}
        />
      </div>
    </div>
  );
};

export default Login;
