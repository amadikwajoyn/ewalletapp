import React from 'react';
import "./ProfileSm.css"
import { Person, PhoneIphone, SupervisedUserCircle, Email } from '@material-ui/icons';


export default function ProfileSm() {
    return (
        <div className="ProfileSm">
            <span className="ProfileSmalltitle">
                <img src="https://images.pexels.com/photos/1526814/pexels-photo-1526814.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500" alt="Profile Avatar" className="topAvatar" />
                <h3>Joy Amadikwa</h3>
            </span>
            <ul className="ProfileSmallList">
                <h6>Account Detail</h6>
                <li className="ProfileSmallListItem">
                    <div className="ProfileSmWallet">
                        <span className="ProfileSmWalletdetail"><Person className="sidebarIcon"/> sweetjoyn</span>
                        <span className="ProfileSmWalletdetail"><PhoneIphone className="sidebarIcon"/> 0817623767</span>
                        <span className="ProfileSmWalletdetail"><Email className="sidebarIcon"/> amadikwajoyn@gmail.com</span>
                        <span className="ProfileSmWalletdetail"><SupervisedUserCircle className="sidebarIcon" /> Elite User</span>
                    </div>
                </li>

            </ul>
        </div>
    )
}
