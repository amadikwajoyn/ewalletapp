import React from 'react'
import "./Addresses.css";
import WalletAddressesLg from '../../components/WalletAddressesLg/WalletAddressesLg';

export default function Addresses() {
    return (
        <div className="Addresses">
            <div className="homeTransactions">
                <WalletAddressesLg />
            </div>
        </div>
    )
}
