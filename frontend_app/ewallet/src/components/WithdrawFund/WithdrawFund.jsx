import React from 'react';
import "./WithdrawFund.css";

export default function WithdrawFund() {
    return (
        <div className="WithdrawFund">
            <h3 className="WithdrawFundTitle"> Withdraw Fund </h3>
            <br /> 
            <form action="" className="WithdrawFund">
                <div className="WithdrawFundLeft">
                    <div className="WithdrawFunditem">
                    <br />
                        <label>Wallet Address</label>
                        <input type="text" placeholder="wallet address" className="WithdrawFundInput" />
                    </div>
                    <br />

                    <div className="WithdrawFunditem">
                        <label>Currency Type</label>

                        <select id="addresstype" className ="WithdrawFundInput">
                            <option value="USD">USD</option>
                            <option value="NGN">NGN</option>
                            <option value="BTC">BTC</option>
                            
                        </select>
                    </div>
                    <br />

                    <div className="WithdrawFunditem">
                        <label>Amount</label>
                        <input type="text" placeholder="Amount" className="WithdrawFundInput" />
                    </div>
                    <br />
                    <button className="WithdrawFundButton">Fund Wallet</button>

                </div>
            </form>
        </div>
    )
}
