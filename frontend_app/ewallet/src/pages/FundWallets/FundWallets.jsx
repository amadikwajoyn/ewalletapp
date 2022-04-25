import React from 'react'
import "./FundWallets.css";
import FundWallet from '../../components/FundWallet/FundWallet';


export default function FundWallets() {
    return (
        <div className="FundWallets">
            <div className="homeFundWallets">
                <FundWallet />
            </div>
        </div>
    )
}
