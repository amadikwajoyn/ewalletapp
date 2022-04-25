import React from "react";
import Topbar from "../../components/Topbar/Topbar";
import SidebarPortal from "../../components/SidebarPortal/SidebarPortal";
import "./UserFundWallet.css";
import FundWallets from "../FundWallets/FundWallets";

function UserFundWallet() {
    return(
        <div>
            <Topbar />
                <div className="container">
                    <SidebarPortal />
                    <FundWallets />
                </div>
        </div>
    );
}

export default UserFundWallet;