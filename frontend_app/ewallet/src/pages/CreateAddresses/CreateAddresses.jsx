import React from 'react'
import "./CreateAddresses.css";
import CreateAddress from '../../components/CreateAddress/CreateAddress';


export default function CreateAddresses() {
    return (
        <div className="CreateAddresses">
            <div className="homeCreateAddresses">
                <CreateAddress />
            </div>
        </div>
    )
}
