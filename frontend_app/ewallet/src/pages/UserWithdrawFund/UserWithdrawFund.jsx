import React from "react";
import Topbar from "../../components/Topbar/Topbar";
import SidebarPortal from "../../components/SidebarPortal/SidebarPortal";
import "./UserWithdrawFund.css";
import WithdrawFunds from "../WithdrawFunds/WithdrawFunds";

function UserWithdrawFund() {
    return(
        <div>
            <Topbar />
                <div className="container">
                    <SidebarPortal />
                    <WithdrawFunds />
                </div>
        </div>
    );
}

export default UserWithdrawFund;