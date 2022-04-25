import { Publish } from '@material-ui/icons';
import React from 'react';
import "./ProfileLg.css";

export default function ProfileLg() {
    return (
        <div className="ProfileLg">
            <h3 className="ProfileLgTitle"> Update Personal Info </h3>
            <form action="" className="userUpdate">
                <div className="userUpdateLeft">
                    <div className="userupdateitem">
                        <label>Username</label>
                        <input type="text" placeholder="Username" className="userUpdateInput" />
                    </div>

                    <div className="userupdateitem">
                        <label>Fullname</label>
                        <input type="text" placeholder="Fullname" className="userUpdateInput" />
                    </div>

                    <div className="userupdateitem">
                        <label>Phone</label>
                        <input type="text" placeholder="Phone" className="userUpdateInput" />
                    </div>

                    <div className="userupdateitem">
                        <label>Email</label>
                        <input type="text" placeholder="Email" className="userUpdateInput" />
                    </div>

                </div>
                <div className="userUpdateRight">
                    <div className="userUpdateUplaod">
                        <img src="https://images.pexels.com/photos/1526814/pexels-photo-1526814.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500" alt="Profile Avatar" className="userUpdateImg" />
                        <label htmlFor="file">
                            <Publish className="userUpdateIcon" />
                        </label>
                        <input type="file" id="file" style={{ display:"none" }} />
                    </div>
                    <button className="userUpdateButton">Update</button>
                </div>

                

            </form>
        </div>
    )
}
