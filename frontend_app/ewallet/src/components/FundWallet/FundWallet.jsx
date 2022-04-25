import React, { useState } from 'react';
import "./FundWallet.css";
import axios from "axios";

export default function FundWallet() {
    const [wallet_address, setWallet_address] = useState("");
    const [currency_types, setCurrency_types] = useState("");
    const [amount, setAmount] = useState("");

    const handleSubmit = (event) => {
        event.preventDefault();
        console.log(wallet_address, currency_types, amount)

        axios.post("http://127.0.0.1:8000/api/fund/"+wallet_address, {
            wallet_address,
            currency_types,
            amount
        }).then(res => {
            console.log(res)
            console.log(res.data)
        }).catch(err => {
            console.log(err.response.data)
        })
    } 

    return (
        <div className="fundWallet">
            <h3 className="fundWalletTitle"> Fund Wallet </h3>
            <br /> 
            <form action="POST" className="fundWallet" onSubmit={handleSubmit}>
                <div className="fundWalletLeft">
                    <div className="fundWalletitem">
                    <br />
                        <label>Wallet Address</label>
                        <input 
                            type="text" 
                            placeholder="wallet address" 
                            className="fundWalletInput" 
                            name="wallet_address" 
                            value={wallet_address}
                            onChange={e => setWallet_address(e.target.value)}
                        />
                    </div>
                    <br />

                    <div className="fundWalletitem">
                        <label>Currency Type</label>

                        <select 
                            id="addresstype" 
                            className ="fundWalletInput" 
                            name="currency_types"  
                            value={currency_types}
                            onChange={e => setCurrency_types(e.target.value)}
                        >
                            <option value="USD">USD</option>
                            <option value="NGN">NGN</option>
                            <option value="BTC">BTC</option>
                            
                        </select>
                    </div>
                    <br />

                    <div className="fundWalletitem">
                        <label>Amount</label>
                        <input 
                            type="text" 
                            placeholder="Amount" 
                            className="fundWalletInput" 
                            name="amount" 
                            value={amount}
                            onChange={e => setAmount(e.target.value)}
                        />
                    </div>
                    <br />
                    <button className="fundWalletButton" onSubmit={handleSubmit}>Fund Wallet</button>

                </div>
            </form>
        </div>
    )
}
