import React, { Component } from "react";
import Navbar from '../../components/Navbar/Navbar';
import Sidebar from '../../components/Sidebar/Sidebar';
import Hero from '../../components/Hero/Hero';
import SubMenu from '../../components/Submenu/Submenu';
import '../../../node_modules/bootstrap/dist/css/bootstrap.min.css';

export default class Home extends Component {
    render() {
        return (
            <>
            < Navbar />
            < Sidebar /> 
            < Hero />
            < SubMenu /> 
        </>
        );
    }
}