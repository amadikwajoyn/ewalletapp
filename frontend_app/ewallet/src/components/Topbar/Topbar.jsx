import React from 'react'
import "./Topbar.css"
import logo from "../../images/logo.png";
import { NotificationsNone, Settings, Language } from '@material-ui/icons';


export default function Topbar() {
    return (
        <div className="topbar">
            <div className="topbarWrapper">
                <div className="topLeft">
                    <span className="logo"><img src={logo} alt="myewalletapp logo" width="50%" /></span>
                </div>
                <div className="topRight">
                    <div className="topbarIconContainer">
                        <NotificationsNone />
                        <span className="topIconBadge">2</span>
                    </div>
                    <div className="topbarIconContainer">
                        <Language />
                        <span className="topIconBadge">3</span>
                    </div>
                    <div className="topbarIconContainer">
                        <Settings />
                        <span className="topIconBadge">4</span>
                    </div>
                    <img src="https://images.pexels.com/photos/1526814/pexels-photo-1526814.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500" alt="Profile Avatar" className="topAvatar" />
                </div>
            </div>
        </div>
    )
}
