import { Routes, Route } from "react-router-dom";
import { HomePage } from "../pages/homepage";
import { Dashboard } from "../pages/dashboard";
import { Pricing } from "../pages/pricing";


const RouteData = () => {
    return (
      <Routes>
        <Route path="/" element={<HomePage /> } />
        <Route path="/terminal" element={<Dashboard />} />
        <Route path="/pricing" element={<Pricing />} />
      </Routes>
    );
  };
  
  export default RouteData;