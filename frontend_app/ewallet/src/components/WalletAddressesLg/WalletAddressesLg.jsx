import React from 'react';
import "./WalletAddressesLg.css";

export default function WalletAddressesLg() {
    return (
        <div className="WalletAddressesLg">
            <h3 className="WalletAddressesLgTitle"> Ewallet Address Info </h3> <br />
            <table className="WalletAddressesLgTable">
                <tr className="WalletAddressesLgTr">
                    <th className="WalletAddressesLgTh">Currency</th>
                    <th className="WalletAddressesLgTh">Total Deposites</th>
                    <th className="WalletAddressesLgTh">Ewallet Address</th>
                </tr> <br />
                <tr className="WalletAddressesLgTr"> 
                    <td className="WalletAddressesLgType">USD</td>
                    <td className="WalletAddressesLgType">5000</td>
                    <td className="WalletAddressesLgType">owkjd8d768JHisd7679kjd</td>

                </tr>

                <tr className="WalletAddressesLgTr"> 
                    <td className="WalletAddressesLgType">BTC</td>
                    <td className="WalletAddressesLgType">28000</td>
                    <td className="WalletAddressesLgType">ksdhad768JHisd7679kjd</td>

                </tr>

                <tr className="WalletAddressesLgTr"> 
                    <td className="WalletAddressesLgType">NGN</td>
                    <td className="WalletAddressesLgType">7000</td>
                    <td className="WalletAddressesLgType">iuisud768JHisd7679kjd</td>

                </tr>
            </table> 
            <br />
            <br />
            <h4>Total Balance : 40000</h4>
        </div>
    )
}
