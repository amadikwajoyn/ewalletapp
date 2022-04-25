import React from 'react'
import "./Transactions.css";
import WidgetLg from '../../components/WidgetLg/WidgetLg';

export default function Transactions() {
    return (
        <div className="Transactions">
            <br />
            <h2>TRANSACTIONS HISTORY</h2>
            <br />
            <div className="homeTransactions">
                <WidgetLg />
            </div>
        </div>
    )
}
