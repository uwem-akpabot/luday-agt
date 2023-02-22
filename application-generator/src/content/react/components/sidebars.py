class Sidebars:

 sidebars = {}
 
 """
 Sidebar component 1: Vendor Sidebar
 TODO: Replace dynamic text
 """
 sidebar_1 ="""
import React from "react";
import { Link, NavLink } from "react-router-dom";

import { 
	FaStream, FaHome, 
	FaShoppingBag, FaCartPlus
} from "react-icons/fa";

import * as ROUTE from '../../../constants/routes';
import { BsFillCartCheckFill } from "react-icons/bs";
import logo from '../../../images/logo/logo.png';


const @@PageName@@ = () => {
	return (
		<div>
			<aside className="navbar-aside" id="offcanvas_aside">
				<div className="aside-top">
					<Link to={ROUTE.ADMIN_DASHBOARD} className="brand-wrap">
					<img
						src={logo}
						style={{ height: "40", maxWidth: "150px" }}
						alt="Bestdealnaija dashboard"
					/>
					</Link>
					<div>
					<button className="btn-aside-minimize">
						<FaStream className="w-5 h-5 text-gray-500"/>
					</button>
					</div>
				</div>
				<nav>
					<ul className="menu-aside">
						<li className="menu-item">
						<NavLink
							className="menu-link"
							to={ROUTE.VENDOR_DASHBOARD}
						>
							<FaHome className="text-gray-400 mr-3 w-6 h-6 inline-block" />
							<span className="text">Dashboard</span>
						</NavLink>
						</li>
						<li className="menu-item cursor-pointer" data-collapse-toggle="aside-dropdown1">
							<div className="menu-link">
								<FaShoppingBag className="text-gray-400 mr-3 w-6 h-6 inline-block" />
								<span className="text">Products</span>
								<svg className="w-6 h-6 inline-block ml-3" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fillRule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clipRule="evenodd"></path></svg>
							</div>
							<ul id="aside-dropdown1" className="ml-5 hidden">
								<li>
									<NavLink
										activeclassname="active"
										className="menu-link"
										to={ROUTE.VENDOR_PRODUCTS}
									>
										<BsFillCartCheckFill className="text-gray-400 mr-3 w-6 h-6 inline-block" />
										<i className="icon fas fa-cart-plus"></i>
										<span className="text">All products</span>
									</NavLink>
								</li>
								<li>
								<NavLink
									activeclassname="active"
									className="menu-link"
									to={ROUTE.VENDOR_ADD_PRODUCTS}
								>
									<FaCartPlus className="text-gray-400 mr-3 w-6 h-6 inline-block" />
									<i className="icon fas fa-cart-plus"></i>
									<span className="text">Add product</span>
								</NavLink>
								</li>
							</ul>
						</li>
						<li className="menu-item">
							<NavLink
								activeclassname="active"
								className="menu-link"
								to={ROUTE.VENDOR_ORDERS}
							>
								<FaShoppingBag className="text-gray-400 mr-3 w-6 h-6 inline-block" />
								<span className="text">Orders</span>
							</NavLink>
						</li>

						{/* <li className="menu-item">
							<NavLink
								activeclassname="active"
								className="menu-link disabled"
								to="#"
							>
								<FaMoneyBillAlt className="text-gray-400 mr-3 w-6 h-6 inline-block" />
								<span className="text">Transactions</span>
							</NavLink>
						</li> */}
					</ul>
					<br />
					<br />
				</nav>
			</aside>
		</div>
	);
};

export default @@PageName@@;
 """
 sidebars["sidebar_1"] = sidebar_1


 """
 Example component
 """
 example ="""
import React from 'react';
const @@PageName@@ = () => {

};

export default @@PageName@@;
 """
 sidebars["example"] = example