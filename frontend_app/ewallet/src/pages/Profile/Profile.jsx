import React from 'react'
import "./Profile.css";
import ProfileLg from '../../components/ProfileLg/ProfileLg';
import ProfileSm from '../../components/ProfileSm/ProfileSm';

export default function Profile() {
    return (
        <div className="Profile">
            <br />
            <h2>Profile setup</h2>
            <br />
            <div className="homeProfile">
                <ProfileSm />
                <ProfileLg />
            </div>
        </div>
    )
}
