import { Link } from "react-router-dom";
import "../style/NavBar.css";
function NavBar() {
  return (
    <nav className="navbar">
      <div className="navbar">
        <Link to="">Home</Link>
        <Link to="login">Login</Link>
        <Link to="admin">Admin</Link>
      </div>
    </nav>
  );
}

export default NavBar;
