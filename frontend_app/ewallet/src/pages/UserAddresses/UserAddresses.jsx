import React from 'react'
import "./UserAddresses.css";
import Addresses from '../Addresses/Addresses';
import Topbar from '../../components/Topbar/Topbar';
import SidebarPortal from '../../components/SidebarPortal/SidebarPortal';

export default function Transactions() {
    return (
        <div>
            <br />
            <Topbar />
            <div className="homeTransactions">
                <SidebarPortal />
                <Addresses />
            </div>
        </div>
    )
}
