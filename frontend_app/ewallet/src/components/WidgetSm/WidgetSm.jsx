import React from 'react';
import "./WidgetSm.css"
import { Visibility } from '@material-ui/icons';

export default function WidgetSm() {
    return (
        <div className="widgetsm">
            <span className="widgetsmalltitle">Ewallet Address</span>
            <ul className="widgetsmallList">
                <li className="widgetsmallListItem">
                    <div className="widgetSmWallet">
                        <span className="widgetSmWalletCurrency">NGN</span>
                        <span className="widgetSmWalletAddress">sjdhjdf9f09fsdfkjfd90</span>
                    </div>
                    <button className="widgetSmButton">
                        <Visibility /> Display
                    </button>
                </li>

                <li className="widgetsmallListItem">
                    <div className="widgetSmWallet">
                        <span className="widgetSmWalletCurrency">USD</span>
                        <span className="widgetSmWalletAddress">KLKJfghgjjh878hjjKLLJjkhj</span>
                    </div>
                    <button className="widgetSmButton">
                        <Visibility /> Display
                    </button>
                </li>

            </ul>
        </div>
    )
}
