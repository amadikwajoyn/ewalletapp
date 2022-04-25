import React from "react";
import Topbar from "../../components/Topbar/Topbar";
import SidebarPortal from "../../components/SidebarPortal/SidebarPortal";
import "./UserTransactions.css";
import Transactions from "../Transactions/Transactions"

function UserTransactions() {
    return(
        <div>
            <Topbar />
                <div className="container">
                    <SidebarPortal />
                    <Transactions/>
                </div>
        </div>
    );
}

export default UserTransactions;