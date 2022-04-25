import React from 'react'
import {LineStyle, TrendingUp} from '@material-ui/icons'
import CreditScoreIcon from '@mui/icons-material/CreditScore';
import "./SidebarPortal.css"
import { Link } from "react-router-dom";


export default function SidebarPortal() {
    return (
        <div className="sidebarportal">
            <div className="sidebarWrapper">
                <div className="sidebarMenu">
                    <h3 className="sidebarTitle">Dashboard</h3>
                    <ul className="sidebarList">
                        <Link to ='/userdashboard' className="Link">
                            <li className="sidebarListItem active">
                                <LineStyle className="sidebarIcon" />
                                Dashboard
                            </li>
                        </Link>
                    </ul>
                </div>
                <div className="sidebarMenu">
                    <h3 className="sidebarTitle">Ewallet</h3>
                    <ul className="sidebarList">
                        <Link to ='/usertransaction' className="Link">
                            <li className="sidebarListItem active">
                                <LineStyle className="sidebarIcon" />
                                Transaction
                            </li>
                        </Link>
                        <Link to='/userfundwallet' className="Link" >
                            <li className="sidebarListItem">
                                <CreditScoreIcon className="sidebarIcon"/>
                                Fund  Wallet
                            </li>
                        </Link>
                        <Link to='/userwithdrawfund' className="Link" >
                            <li className="sidebarListItem">
                                <TrendingUp className="sidebarIcon"/>
                                Withdraw Fund
                            </li>
                        </Link>
                    </ul>
                </div>
                <div className="sidebarMenu">
                    <h3 className="sidebarTitle">Wallet Setup</h3>
                    <ul className="sidebarList">
                        <Link to='/usercreateaddress' className="Link">
                            <li className="sidebarListItem active">
                                <LineStyle className="sidebarIcon" />
                                Create Address
                            </li>
                        </Link>
                        <Link to ='/viewaddresses' className="Link">
                            <li className="sidebarListItem">
                                <CreditScoreIcon className="sidebarIcon"/>
                                View Address
                            </li>
                        </Link>
                    </ul>
                </div>
                <div className="sidebarMenu">
                    <h3 className="sidebarTitle">Profile</h3>
                    <ul className="sidebarList">
                        <Link to ='/userprofile' className="Link">
                            <li className="sidebarListItem active">
                                <LineStyle className="sidebarIcon" />
                                Edit Account
                            </li>
                        </Link>
                        <Link to = '/' className="Link">
                            <li className="sidebarListItem">
                                <CreditScoreIcon className="sidebarIcon"/>
                                Signout
                            </li>
                        </Link>
                    </ul>
                </div>
            </div>
        </div>
    )
}
