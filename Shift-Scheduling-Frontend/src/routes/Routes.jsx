import { createBrowserRouter } from "react-router-dom";
import User from "../pages/User";
import Login from "../pages/Login";
import Admin from "../pages/Admin";
import MainLayout from "./MainLayout";

export const router = createBrowserRouter([
  {
    path: "/",
    element: <MainLayout />,
    children: [
      {
        path: "/",
        element: <User />,
      },
      {
        path: "/login",
        element: <Login />,
      },
      {
        path: "/admin",
        element: <Admin />,
      },
    ],
  },
]);
