import { Routes, Route } from "react-router-dom";
import { HomePage } from "../pages/homepage";
import { Dashboard } from "../pages/dashboard";

const RouteData = () => {
    return (
      <Routes>
        <Route path="/" element={<HomePage /> } />
        <Route path="/dashboard" element={<Dashboard />} />
      </Routes>
    );
  };
  
  export default RouteData;