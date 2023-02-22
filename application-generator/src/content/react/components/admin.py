class Admin:

 admin = {}
 
 """
 Admin component index page
 """
 admin_index ="""
export { default as Sidebar } from './Sidebar';
export {default as Header } from './Header';
 """
 admin["admin_index"] = admin_index


 """
 Admin Sidebar component 1
 TODO: Replace dynamic text
 """
 admin_sidebar_1 ="""
import React, { Fragment } from "react";
import { useSelector } from "react-redux";
import { Link, NavLink } from "react-router-dom";
import { Menu, Transition } from "@headlessui/react";

import * as CONSTANT from '../../constants/constants'
import { FaStream, FaStoreAlt, FaHome, FaShoppingBag, FaList, FaUserAlt, FaCartPlus, FaBlog, FaPlusCircle } from "react-icons/fa";
import * as ROUTE from '../../constants/routes';
import { BsFillCartCheckFill, BsFillCartXFill } from "react-icons/bs";
import logo from '../../images/logo/logo.png';

const @@PageName@@ = () => {
    const { authUserType} = useSelector((state) => ({
        authUserType: state.auth.user_type
    }));
    
	return (
		<>
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
						to={ROUTE.ADMIN_DASHBOARD}
						>
						<FaHome className="text-gray-400 mr-3 w-6 h-6 inline-block" />
						<span className="text">Dashboard</span>
						</NavLink>
					</li>
					{authUserType === CONSTANT.ADMIN_ROLE && (
						<li className="menu-item">
						<Menu as="div">
							<Menu.Button className="menu-link w-full text-left">
							<FaUserAlt className="text-gray-400 mr-3 w-6 h-6 inline-block" />
							<span className="text">Users</span>
							<svg
								xmlns="http://www.w3.org/2000/svg"
								className="w-6 h-6 inline-block ml-3"
								fill="none"
								viewBox="0 0 24 24"
								stroke="currentColor"
								strokeWidth={2}
							>
								<path
									strokeLinecap="round"
									strokeLinejoin="round"
									d="M19 9l-7 7-7-7"
								/>
							</svg>
							</Menu.Button>
							<Transition
								as={Fragment}
								enter="transition ease-out duration-100"
								enterFrom="transform opacity-0 scale-95"
								enterTo="transform opacity-100 scale-100"
								leave="transition ease-in duration-75"
								leaveFrom="transform opacity-100 scale-100"
								leaveTo="transform opacity-0 scale-95"
							>
								<Menu.Items>
								<div className="py-1">
									<Menu.Item>
									<NavLink
										activeclassname="active"
										className="menu-link"
										to={ROUTE.ADMIN_CREATE_ADMIN}
									>
										<FaCartPlus className="text-gray-400 mr-3 w-6 h-6 inline-block" />
										<i className="icon fas fa-home"></i>
										<span className="text">Create Admin</span>
									</NavLink>
									</Menu.Item>
									<Menu.Item>
									<NavLink
										activeclassname="active"
										className="menu-link"
										to={ROUTE.ADMIN_MANAGE_ADMINS}
									>
										<FaCartPlus className="text-gray-400 mr-3 w-6 h-6 inline-block" />
										<i className="icon fas fa-home"></i>
										<span className="text">Manage Admins</span>
									</NavLink>
									</Menu.Item>
									<Menu.Item>
									<NavLink
										activeclassname="active"
										className="menu-link"
										to={ROUTE.ADMIN_USERS}
									>
										<BsFillCartCheckFill className="text-gray-400 mr-3 w-6 h-6 inline-block" />
										<i className="icon fas fa-home"></i>
										<span className="text">All Customers</span>
									</NavLink>
									</Menu.Item>
								</div>
								</Menu.Items>
							</Transition>
						</Menu>
						</li>
					)}
					<li className="menu-item">
						<NavLink
						activeclassname="active"
						className="menu-link"
						to={ROUTE.ADMIN_CATEGORIES}
						>
						<FaList className="text-gray-400 mr-3 w-6 h-6 inline-block" />
						<span className="text">Categories</span>
						</NavLink>
					</li>
					<li className="menu-item">
						<Menu as="div">
						<Menu.Button className="menu-link w-full text-left">
							<FaShoppingBag className="text-gray-400 mr-3 w-6 h-6 inline-block" />
							<span className="text">Products</span>
							<svg
								xmlns="http://www.w3.org/2000/svg"
								className="w-6 h-6 inline-block ml-3"
								fill="none"
								viewBox="0 0 24 24"
								stroke="currentColor"
								strokeWidth={2}
							>
							<path
								strokeLinecap="round"
								strokeLinejoin="round"
								d="M19 9l-7 7-7-7"
							/>
							</svg>
						</Menu.Button>
						<Transition
							as={Fragment}
							enter="transition ease-out duration-100"
							enterFrom="transform opacity-0 scale-95"
							enterTo="transform opacity-100 scale-100"
							leave="transition ease-in duration-75"
							leaveFrom="transform opacity-100 scale-100"
							leaveTo="transform opacity-0 scale-95"
						>
							<Menu.Items>
								<div className="py-1">
								<Menu.Item>
									<NavLink
									activeclassname="active"
									className="menu-link"
									to={ROUTE.ADMIN_PRODUCTS}
									>
									<BsFillCartCheckFill className="text-gray-400 mr-3 w-6 h-6 inline-block" />
									<i className="icon fas fa-cart-plus"></i>
									<span className="text">All products</span>
									</NavLink>
								</Menu.Item>
								<Menu.Item>
									<NavLink
									activeclassname="active"
									className="menu-link"
									to={ROUTE.ADMIN_VERIFY_PRODUCTS}
									>
									<BsFillCartXFill className="text-gray-400 mr-3 w-6 h-6 inline-block" />
									<i className="icon fas fa-cart-plus"></i>
									<span className="text">Unverified products</span>
									</NavLink>
								</Menu.Item>
								</div>
							</Menu.Items>
						</Transition>
						</Menu>
					</li>
					<li className="menu-item">
						<Menu as="div">
						<Menu.Button className="menu-link w-full text-left">
							<FaStoreAlt className="text-gray-400 mr-3 w-6 h-6 inline-block" />
							<span className="text">Vendors</span>
							<svg
								xmlns="http://www.w3.org/2000/svg"
								className="w-6 h-6 inline-block ml-3"
								fill="none"
								viewBox="0 0 24 24"
								stroke="currentColor"
								strokeWidth={2}
							>
							<path
								strokeLinecap="round"
								strokeLinejoin="round"
								d="M19 9l-7 7-7-7"
							/>
							</svg>
						</Menu.Button>
						<Transition
							as={Fragment}
							enter="transition ease-out duration-100"
							enterFrom="transform opacity-0 scale-95"
							enterTo="transform opacity-100 scale-100"
							leave="transition ease-in duration-75"
							leaveFrom="transform opacity-100 scale-100"
							leaveTo="transform opacity-0 scale-95"
						>
							<Menu.Items>
								<div className="py-1">
								<Menu.Item>
									<NavLink
									activeclassname="active"
									className="menu-link"
									to={ROUTE.ADMIN_VENDORS}
									>
									<BsFillCartCheckFill className="text-gray-400 mr-3 w-6 h-6 inline-block" />
									<i className="icon fas fa-home"></i>
									<span className="text">All vendors</span>
									</NavLink>
								</Menu.Item>
								<Menu.Item>
									<NavLink
									activeclassname="active"
									className="menu-link"
									to={ROUTE.ADMIN_VERIFY_VENDORS}
									>
									<BsFillCartCheckFill className="text-gray-400 mr-3 w-6 h-6 inline-block" />
									<i className="icon fas fa-home"></i>
									<span className="text">Unverified vendors</span>
									</NavLink>
								</Menu.Item>
								</div>
							</Menu.Items>
						</Transition>
						</Menu>
					</li>
					<li className="menu-item">
						<NavLink
						activeclassname="active"
						className="menu-link"
						to={ROUTE.ADMIN_ORDERS}
						>
						<FaShoppingBag className="text-gray-400 mr-3 w-6 h-6 inline-block" />
						<span className="text">Orders</span>
						</NavLink>
					</li>
					<li className="menu-item">
						<Menu as="div">
						<Menu.Button className="menu-link w-full text-left">
							<FaBlog className="text-gray-400 mr-3 w-6 h-6 inline-block" />
							<span className="text">Blogs</span>
							<svg
								xmlns="http://www.w3.org/2000/svg"
								className="w-6 h-6 inline-block ml-3"
								fill="none"
								viewBox="0 0 24 24"
								stroke="currentColor"
								strokeWidth={2}
							>
							<path
								strokeLinecap="round"
								strokeLinejoin="round"
								d="M19 9l-7 7-7-7"
							/>
							</svg>
						</Menu.Button>
						<Transition
							as={Fragment}
							enter="transition ease-out duration-100"
							enterFrom="transform opacity-0 scale-95"
							enterTo="transform opacity-100 scale-100"
							leave="transition ease-in duration-75"
							leaveFrom="transform opacity-100 scale-100"
							leaveTo="transform opacity-0 scale-95"
						>
							<Menu.Items>
								<div className="py-1">
								<Menu.Item>
									<NavLink
									activeclassname="active"
									className="menu-link"
									to={ROUTE.ADMIN_BLOGS}
									>
									<FaBlog className="text-gray-400 mr-3 w-6 h-6 inline-block" />
									<i className="icon fas fa-cart-plus"></i>
									<span className="text">All blogs</span>
									</NavLink>
								</Menu.Item>
								<Menu.Item>
									<NavLink
									activeclassname="active"
									className="menu-link"
									to={ROUTE.ADMIN_ADD_BLOGS}
									>
									<FaPlusCircle className="text-gray-400 mr-3 w-6 h-6 inline-block" />
									<i className="icon fas fa-cart-plus"></i>
									<span className="text">Post blog</span>
									</NavLink>
								</Menu.Item>
								</div>
							</Menu.Items>
						</Transition>
						</Menu>
					</li>
					</ul>
					<br />
					<br />
				</nav>
				</aside>
			</div>
		</>
	);
};

export default @@PageName@@;
 """
 admin["admin_sidebar_1"] = admin_sidebar_1


 """
 Admin Header component 1
 """
 admin_header_1 ="""
import React, { Fragment, useEffect } from 'react';
import { Link } from "react-router-dom";
import { useDispatch } from "react-redux";

import $ from "jquery";
import { Menu, Transition } from '@headlessui/react'
import { FaBars } from "react-icons/fa";

import { signOut } from '../../redux/actions/authActions';

const @@PageName@@ = () => {
    const dispatch = useDispatch();

    const handleLogout = () => {
        dispatch(signOut())
    };

    useEffect(() => {
        $("[data-trigger]").on("click", function (e) {
        e.preventDefault();
        e.stopPropagation();
        var offcanvas_id = $(this).attr("data-trigger");
        $(offcanvas_id).toggleClass("show");
        });

        $(".btn-aside-minimize").on("click", function () {
        if (window.innerWidth < 768) {
            $("body").removeClass("aside-mini");
            $(".navbar-aside").removeClass("show");
        } else {
            // minimize sidebar on desktop
            $("body").toggleClass("aside-mini");
        }
        });
    }, []);

    return (
        <>
            <nav className="w-full flex flex-wrap items-center justify-between bg-white min-h-min bg-whte border-b-2 border-[#4fa607]">
                <div>
                <button
                    className="block lg:hidden"
                    data-trigger="#offcanvas_aside"
                    >
                    <FaBars className="w-6 h-6 ml-2 text-gray-500"/>
                    </button>
                </div>
                <div className="flex flex-row items-center">
                    <ul className="flex flex-row items-center">
                        <li className="flex flex-row whitespace-nowrap pr-4 pl-4  rounded md:bg-transparent text-black  py-6 px-28">
                        <Menu as="div" className="relative inline-block text-left">
                            <div>
                            <Menu.Button className="flex items-center rounded-full text-base font-normal text-gray-500 transition duration-75 group hover:bg-gray-100">
                                <Link className="hidden md:justify-center md:block dropdown-toggle" data-bs-toggle="dropdown" to="#">
                                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24">
                                <path d="M7.5 6.5C7.5 8.981 9.519 11 12 11s4.5-2.019 4.5-4.5S14.481 2 12 2 7.5 4.019 7.5 6.5zM20 21h1v-1c0-3.859-3.141-7-7-7h-4c-3.86 0-7 3.141-7 7v1h17z"></path>
                                </svg>
                                </Link>
                                <svg 
                                className="w-4 h-4" 
                                fill="currentColor" 
                                viewBox="0 0 20 20" 
                                xmlns="http://www.w3.org/2000/svg">
                                    <path fillRule="evenodd" 
                                    d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" 
                                    clipRule="evenodd">
                                    </path>
                                </svg>
                            </Menu.Button>
                            </div>
                            <Transition
                            as={Fragment}
                            enter="transition ease-out duration-100"
                            enterFrom="transform opacity-0 scale-95"
                            enterTo="transform opacity-100 scale-100"
                            leave="transition ease-in duration-75"
                            leaveFrom="transform opacity-100 scale-100"
                            leaveTo="transform opacity-0 scale-95"
                            >
                            <Menu.Items className="origin-top-right absolute right-0 mt-2 w-56 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 focus:outline-none">
                                <>
                                <div className="py-1">
                                <form method="POST" action="#">
                                    <Menu.Item>
                                    <button 
                                        type="submit"
                                        className="flex items-center p-2 pl-11 w-full h-full text-base font-normal transition duration-75 group hover:bg-gray-100 text-red-500" 
                                        onClick={() => 
                                        handleLogout()
                                        }
                                    >
                                        <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 fill-current mr-4"><path d="m2 12 5 4v-3h9v-2H7V8z"></path><path d="M13.001 2.999a8.938 8.938 0 0 0-6.364 2.637L8.051 7.05c1.322-1.322 3.08-2.051 4.95-2.051s3.628.729 4.95 2.051 2.051 3.08 2.051 4.95-.729 3.628-2.051 4.95-3.08 2.051-4.95 2.051-3.628-.729-4.95-2.051l-1.414 1.414c1.699 1.7 3.959 2.637 6.364 2.637s4.665-.937 6.364-2.637c1.7-1.699 2.637-3.959 2.637-6.364s-.937-4.665-2.637-6.364a8.938 8.938 0 0 0-6.364-2.637z"></path></svg>
                                        Logout
                                    </button>
                                    </Menu.Item>
                                </form>
                                </div>
                                </>
                            </Menu.Items>
                            </Transition>
                        </Menu>
                        </li>
                    </ul>
                </div>
            </nav>
        </>
    )
};

export default @@PageName@@;
 """
 admin["admin_header_1"] = admin_header_1


 """
 Admin Dashboard component 1
 """
 dashboard_component_1 ="""
import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';

import PropType from 'prop-types';
import { FaShoppingBasket, FaExternalLinkAlt } from 'react-icons/fa';
import { BsShop } from "react-icons/bs";

import * as ROUTE from '../../../constants/routes'
import { useDidMount } from '../../../hooks';

const @@PageName@@ = () => {
  const [countOfProducts, setCountOfProducts] = useState([]);
  const [vendors, fetchVendors] = useState([]);
  const [users, fetchUsers] = useState([]);
  const [orders, fetchOrders] = useState([]);
  const didMount = useDidMount(true);
  
  const getCountOfProducts = () => {
    fetch(`${ROUTE.PRODUCTS_API}/products/count`)
      .then((res) => res.json())
      .then((res) => {
        setCountOfProducts(res.results) 
      })
  }
  const getVendors = () => {
    fetch(`${ROUTE.USER_API}/user/vendors`)
      .then((res) => res.json())
      .then((res) => {
          fetchVendors(res.results.length)
      })
  }
  const getCountOders = () => {
    fetch(`${ROUTE.PRODUCTS_API}/order/all`)
      .then((res) => res.json())
      .then((res) => {
          fetchOrders(res.data.length)
      })
  }
  const getUsers = () => {
		if (didMount) {
			let _tokens = JSON.parse(localStorage.getItem('auth_tokens'));
			fetch(`${ROUTE.USER_API}/users`, {
				headers:{
				'Content-Type':'application/json',
				'Authorization': 'Bearer ' + _tokens.access_token
				}
			})
			.then((res) => res.json())
			.then((res) => {
				fetchUsers(res.length)
			})  
		}
  }

  useEffect(() => {
    getCountOfProducts()
    getVendors()
    getUsers()
    getCountOders()
  }, [])

  return (
    <>   
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 p-4 mt-3 gap-4">
        <div className="bg-white shadow-lg rounded-md px-3 pt-3 border-b-4 border-green-600 text-green-600 font-medium group hover:scale-105 transition-all duration-400">
          <div className="flex items-center justify-between mb-3">
            <div className="flex justify-center items-center w-14 h-14 bg-gray-100 rounded-full transition-all duration-300 transform group-hover:rotate-12">
              <svg width="30" height="30" fill="none" viewBox="0 0 24 24" stroke="currentColor" className="stroke-current transform transition-transform duration-500 ease-in-out"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"></path></svg>
            </div>
            <div className="text-right">
              <p className="text-2xl">{ users > 0 ? users : 0 }</p>
              <p>@@Card1Title@@</p>
            </div>
          </div>
          <div className="flex items-center text-sm mb-1 justify-start text-green-700">
                <Link to={ROUTE.ADMIN_USERS}>@@Card1LinkDesc@@</Link> <span><FaExternalLinkAlt className="ml-1 h-3 w-3"/></span>
          </div>
        </div>

        <div className="bg-white shadow-lg rounded-md px-3 pt-3 border-b-4 border-green-600 text-green-600 font-medium group hover:scale-105 transition-all duration-400">
          <div className="flex items-center justify-between mb-3">
              <div className="flex justify-center items-center w-14 h-14 bg-gray-100 rounded-full transition-all duration-300 transform group-hover:rotate-12">
                <BsShop className="w-8 h-8"/>
              </div>
              <div className="text-right">
                <p className="text-2xl">{ vendors > 0 ? vendors : 0 }</p>
                <p>@@Card2Title@@</p>
              </div>
          </div>
          <div className="flex items-center text-sm mb-1 justify-start text-green-700">
                <Link to={ROUTE.ADMIN_VENDORS}>@@Card2LinkDesc@@</Link> <span><FaExternalLinkAlt className="ml-1 h-3 w-3"/></span>
          </div>
        </div>
        

        <div className="bg-white shadow-lg rounded-md px-3 pt-3 border-b-4 border-green-600 text-green-600 font-medium group hover:scale-105 transition-all duration-400">
          <div className="flex items-center justify-between mb-3">
            <div className="flex justify-center items-center w-14 h-14 bg-gray-100 rounded-full transition-all duration-300 transform group-hover:rotate-12">
            <svg width="30" height="30" fill="none" viewBox="0 0 24 24" stroke="currentColor" className="stroke-current transform transition-transform duration-500 ease-in-out"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"></path></svg>
            </div>
            <div className="text-right">
              <p className="text-2xl">{orders > 0 ? orders : 0}</p>
              <p>@@Card3Title@@</p>
            </div>
          </div>
          <div className="flex items-center text-sm mb-1 justify-start text-green-700">
              <Link to={ROUTE.ADMIN_ORDERS}>@@Card3LinkDesc@@</Link> <span><FaExternalLinkAlt className="ml-1 h-3 w-3"/></span>
          </div>
        </div>

        <div className="bg-white shadow-lg rounded-md px-3 pt-3 border-b-4 border-green-600 text-green-600 font-medium group hover:scale-105 transition-all duration-400 flex-col">
          <div className="flex items-center justify-between mb-3">
            <div className="flex justify-center items-center w-14 h-14 bg-gray-100 rounded-full transition-all duration-300 transform group-hover:rotate-12">
            <FaShoppingBasket className="w-8 h-8"/>
            </div>
            <div className="text-right">
              <p className="text-2xl">{countOfProducts > 0 ? countOfProducts : 0}</p>
              <p>@@Card4Title@@</p>
            </div>
          </div>
          <div className="flex items-center text-sm mb-1 justify-start text-green-700">
              <Link to={ROUTE.ADMIN_PRODUCTS}>@@Card4LinkDesc@@</Link> <span><FaExternalLinkAlt className="ml-1 h-3 w-3"/></span>
          </div>            
        </div>
      </div>
    </>
  )
}

@@PageName@@.propTypes = {
	isLoading: PropType.bool.isRequired
};

export default @@PageName@@;
 """
 admin["dashboard_component_1"] = dashboard_component_1

 """
 Example component
 """
 example ="""
import React from 'react';
const @@PageName@@ = () => {

};

export default @@PageName@@;
 """
 admin["example"] = example