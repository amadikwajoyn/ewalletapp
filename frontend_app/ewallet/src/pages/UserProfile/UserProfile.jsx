import React from "react";
import Topbar from "../../components/Topbar/Topbar";
import SidebarPortal from "../../components/SidebarPortal/SidebarPortal";
import "./UserProfile.css";
import Profile from "../Profile/Profile"

function UserProfile() {
    return(
        <div>
            <Topbar />
                <div className="container">
                    <SidebarPortal />
                    <Profile/>
                </div>
        </div>
    );
}

export default UserProfile;