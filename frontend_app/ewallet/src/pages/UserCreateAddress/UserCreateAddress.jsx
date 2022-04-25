import React from "react";
import Topbar from "../../components/Topbar/Topbar";
import SidebarPortal from "../../components/SidebarPortal/SidebarPortal";
import "./UserCreateAddress.css";
import CreateAddresses from "../CreateAddresses/CreateAddresses";

function UserCreateAddress() {
    return(
        <div>
            <Topbar />
                <div className="container">
                    <SidebarPortal />
                    <CreateAddresses />
                </div>
        </div>
    );
}

export default UserCreateAddress;