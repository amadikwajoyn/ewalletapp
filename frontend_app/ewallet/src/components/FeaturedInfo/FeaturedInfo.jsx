import React from 'react'
import "./FeaturedInfo.css";
import {ArrowDownward, ArrowUpward} from "@material-ui/icons";

export default function FeaturedInfo() {
    return (
        <div className="featured">
            <div className="featuredItem">
                <span className="featuredTitle">Wallets</span>
                <div className="featuredMoneyContainer">
                <span className="featuredMoney">$3,454</span>
                    <span className="featuredMoneyRate">
                        -11.4<ArrowUpward className="featuredIcon negative" />
                    </span>
                </div>
                <span className="featuredSub">Available wallet Address</span>
            </div>

            <div className="featuredItem">
                <span className="featuredTitle">Transactions</span>
                <div className="featuredMoneyContainer">
                <span className="featuredMoney">$3,454</span>
                    <span className="featuredMoneyRate">-11.4<ArrowDownward /></span>
                </div>
                <span className="featuredSub">Total number of deposites</span>
            </div>

            <div className="featuredItem">
                <span className="featuredTitle">Notification</span>
                <div className="featuredMoneyContainer">
                <span className="featuredMoney">$3,454</span>
                    <span className="featuredMoneyRate">
                        11.4<ArrowDownward className="featuredIcon Negative" />
                    </span>
                </div>
                <span className="featuredSub">Latest notification</span>
            </div>
        </div>
    )
}
