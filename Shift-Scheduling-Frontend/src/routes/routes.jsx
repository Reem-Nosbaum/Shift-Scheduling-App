import { createBrowserRouter } from "react-router-dom";
import User from "../pages/User";
import Login from "../pages/Login";
import Admin from "../pages/Admin";

const routes = [
  {
    path: "/",
    element: <Login />,
  },
  {
    path: "/user",
    element: <User />,
  },
  {
    path: "/admin",
    element: <Admin />,
  },
];

const router = createBrowserRouter(routes);

export default router;
