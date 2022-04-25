import React from "react";
import Topbar from "../../components/Topbar/Topbar";
import SidebarPortal from "../../components/SidebarPortal/SidebarPortal";
import Dashboard from "../Dashboard/Dashboard";
import "./UserDashboard.css";

function UserDashboard() {
    return(
        <div>
            <Topbar />
                <div className="container">
                    <SidebarPortal />
                    <Dashboard/>
                
                </div>
        </div>
    );
}

export default UserDashboard;