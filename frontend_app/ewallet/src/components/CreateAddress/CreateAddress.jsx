import React from 'react';
import "./CreateAddress.css";

export default function CreateAddress() {
    return (
        <div className="ProfileLg">
            <h3 className="ProfileLgTitle"> Create Ewallet Address </h3>
            <form action="" className="addressCreate">
                <div className="addressCreateLeft">
                    <div className="addressCreateitem">
                        <label>User Type</label>

                        <select id="addresstype" className ="addressCreateInput">
                            <option value="Elite">Elite</option>
                            <option value="Noobs">Noobs</option>
                        </select>
                    </div>

                    <div className="addressCreateitem">
                        <label>Currency Type</label>

                        <select id="addresstype" className ="addressCreateInput">
                            <option value="USD">USD</option>
                            <option value="NGN">NGN</option>
                            <option value="BTC">BTC</option>
                            
                        </select>
                    </div>
                    <br />
                    <button className="addressCreateButton">Create</button>

                </div>
            </form>
        </div>
    )
}
