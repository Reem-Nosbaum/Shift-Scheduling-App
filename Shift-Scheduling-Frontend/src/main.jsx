import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.jsx";
import "./index.css";
import User from "./pages/User.jsx";

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <User />
  </React.StrictMode>
);
