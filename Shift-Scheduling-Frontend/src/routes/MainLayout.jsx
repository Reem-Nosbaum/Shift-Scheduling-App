import { Outlet } from "react-router-dom";
import NavBar from "../components/NavBar";
function MainLayout() {
  return (
    <div className="main-layout w-full h-full flex flex-col grow">
      <NavBar />
      <Outlet />
    </div>
  );
}
export default MainLayout;
