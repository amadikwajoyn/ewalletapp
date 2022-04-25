import './App.css';
import React from 'react';
import SignUp from './pages/Signup/Signup';
import Login from './pages/Signin/Signin';
import Home from './pages/Home/Home'; 
import {BrowserRouter as Router,  Route, Routes} from "react-router-dom";
import UserDashboard from './pages/UserDashboard/UserDashboard';
import UserTransactions from './pages/UserTransactions/UserTransactions';
import UserProfile from './pages/UserProfile/UserProfile';
import UserAddresses from './pages/UserAddresses/UserAddresses';
import UserCreateAddress from './pages/UserCreateAddress/UserCreateAddress';
import UserFundWallet from './pages/UserFundWallet/UserFundWallet';
import UserWithdrawFund from './pages/UserWithdrawFund/UserWithdrawFund';

function App() {
  return (
    <Router>
      <>
      <Routes>
        <Route path = "/" element={<Home/>}/>
      </Routes>
      <Routes>
        <Route path = "/signup" element = {<SignUp/>}/>
      </Routes>
      <Routes>
        <Route path = "/signin" element = {<Login/>}/>
      </Routes>

      <Routes>
        <Route path = "/userdashboard" element = {<UserDashboard/>}/>
      </Routes>
      <Routes>
        <Route path = "/usertransaction" element = {<UserTransactions />} />
      </Routes>
      <Routes>
        <Route path = "/userprofile" element = {<UserProfile />} />
      </Routes>
      <Routes>
        <Route path = "/viewaddresses" element = {<UserAddresses />} />
      </Routes>

      <Routes>
        <Route path = "/usercreateaddress" element = {<UserCreateAddress />} />
      </Routes>

      <Routes>
        <Route path = "/userfundwallet" element = {<UserFundWallet />} />
      </Routes>

      <Routes>
        <Route path = "/userwithdrawfund" element = {<UserWithdrawFund />} />
      </Routes>
      
      </>
    </Router>
  );
}

export default App;
