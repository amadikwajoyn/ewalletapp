import React from 'react'
import Charts from '../../components/Charts/Charts'
import FeaturedInfo from '../../components/FeaturedInfo/FeaturedInfo'
import "./Dashboard.css";
import {userData} from "../../dummyData";
import WidgetSm from '../../components/WidgetSm/WidgetSm';
import WidgetLg from '../../components/WidgetLg/WidgetLg';

export default function Dashboard() {
    return (
        <div className="Dashboard">
            <FeaturedInfo />
            <Charts data={userData} title="User Transactions" grid dataKey="Active User" />
            <div className="homeTransactions">
                <WidgetSm />
                <WidgetLg />
            </div>
        </div>
    )
}
