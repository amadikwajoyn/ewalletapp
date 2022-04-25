import React from 'react';
import "./WidgetLg.css";

export default function WidgetLg() {
    return (
        <div className="widgetlg">
            <h3 className="widgetLgTitle"> Latest Transactions </h3>
            <table className="widgetLgTable">
                <tr className="widgetLgTr">
                    <th className="widgetLgTh">Type</th>
                    <th className="widgetLgTh">Currency</th>
                    <th className="widgetLgTh">Amount</th>
                    <th className="widgetLgTh">Address</th>
                    <th className="widgetLgTh">Date</th>
                </tr>
                <tr className="widgetLgTr"> 
                    <td className="widgetLgType">Debit</td>
                    <td className="widgetLgType">USD</td>
                    <td className="widgetLgType">9000</td>
                    <td className="widgetLgType">owkjd8d768JHisd7679kjd</td>
                    <td className="widgetLgType">2/3/2021</td>

                </tr>

                <tr className="widgetLgTr"> 
                    <td className="widgetLgType">Credit</td>
                    <td className="widgetLgType">BTC</td>
                    <td className="widgetLgType">300</td>
                    <td className="widgetLgType">ksdhad768JHisd7679kjd</td>
                    <td className="widgetLgType">12/5/2021</td>

                </tr>

                <tr className="widgetLgTr"> 
                    <td className="widgetLgType">Debit</td>
                    <td className="widgetLgType">NGN</td>
                    <td className="widgetLgType">29000</td>
                    <td className="widgetLgType">iuisud768JHisd7679kjd</td>
                    <td className="widgetLgType">20/6/2021</td>

                </tr>
            </table>
        </div>
    )
}
