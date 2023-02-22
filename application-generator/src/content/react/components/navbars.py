class Navbars:

 navbars = {}

 """
 Vendor Navigation index file
 """
 navbar_index_1 ="""
export { default as Sidebar } from './Sidebar';
export {default as Header } from './Header';
 """
 navbars["navbar_index_1"] = navbar_index_1
 
 '''

 '''
 navbar ="""
import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = ({ toggle }) => {
  return (
    <nav
      className='flex justify-between items-center h-16 bg-white text-black relative shadow-sm font-mono'
      role='navigation'
    >
      <Link to='/' className='pl-8'>
        EGG
      </Link>
      <div className='px-4 cursor-pointer md:hidden' onClick={toggle}>
        <svg
          className='w-8 h-8'
          fill='none'
          stroke='currentColor'
          viewBox='0 0 24 24'
          xmlns='http://www.w3.org/2000/svg'
        >
          <path
            strokeLinecap='round'
            strokeLinejoin='round'
            strokeWidth='2'
            d='M4 6h16M4 12h16M4 18h16'
          />
        </svg>
      </div>
      <div className='pr-8 md:block  hidden'>
        <Link to='/' className='p-4'>
          @@menu1@@
        </Link>
        <Link to='/menu' className='p-4'>
          @@menu2@@
        </Link>
        <Link to='/about' className='p-4'>
          @@menu3@@
        </Link>
        <Link to='/contact' className='p-4'>
          @@menu4@@
        </Link>
      </div>
    </nav>
  );
};

export default Navbar;

 """
 navbars["navbar"] = navbar

 '''
 

 '''
 navbar_1 ="""
import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';


function MenuItems() {
    return (
        // <div className="flex flex-row justify-center items-center text-center font-semibold">
        <>
                <Link className="px-4 font-bold text-blue-900 hover:text-blue-500" to="/">
                    @@menu1@@
                </Link>
                <Link className="px-4 font-bold text-blue-900 hover:text-blue-500" to="/">
                    @@menu3@@
                </Link>
                <Link className="px-4 font-bold text-blue-900 hover:text-blue-500" to="/">
                    @@menu3@@
                </Link>
                <Link className="px-4 font-bold text-blue-900 hover:text-blue-500" to="/">
                    @@menu4@@
                </Link>
                <Link className="px-4 font-bold text-blue-900 hover:text-blue-500" to="/contact">
                    @@menu5@@
                </Link>
        </>
        // </div>
    )
}
function Navbar1() {
    const [top, setTop] = useState(true);
    const [isOpen, setisOpen] = React.useState(false);
    function handleClick() {
        setisOpen(!isOpen);
      }

    // detect whether user has scrolled the page down by 10px 
    useEffect(() => {
      const scrollHandler = () => {
        window.pageYOffset > 10 ? setTop(false) : setTop(true)
      };
      window.addEventListener('scroll', scrollHandler);
      return () => window.removeEventListener('scroll', scrollHandler);
    }, [top]);
    return (
        // <nav className="bg-transparent md:px-12 md:mx-12 relative">
        <nav className={`fixed top-0 w-full z-30 transition duration-300 ease-in-out mb-16 ${!top && 'bg-white shadow-lg'}`}>
            <div className="flex flex-row justify-between items-center py-2">
                <div className="flex flex-row justify-center md:px-12 md:mx-12 items-center text-center font-semibold">
                    <Link to="/"><img src="https://luday.se/img/luday_logo.png" alt="Luday logo"/></Link>
                    <h1 className="font-bold text-3xl text-blue-900">Luday</h1>
                </div>
                <div className="group flex flex-col items-center">
                    <button className="p-2 rounded-lg lg:hidden " onClick={handleClick}>
                    {/* <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" className="h-10 fill-current text-blue-900" viewBox="0 0 16 16">
                        <path fill-rule="evenodd" d="M2.5 12a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5z" />
                    </svg> */}
                        <svg className="h-6 w-6 fill-current" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                            {isOpen && (
                            <path fillRule="evenodd" clipRule="evenodd" d="M18.278 16.864a1 1 0 0 1-1.414 1.414l-4.829-4.828-4.828 4.828a1 1 0 0 1-1.414-1.414l4.828-4.829-4.828-4.828a1 1 0 0 1 1.414-1.414l4.829 4.828 4.828-4.828a1 1 0 1 1 1.414 1.414l-4.828 4.829 4.828 4.828z" />
                            )}
                            {!isOpen && (
                            <path fillRule="evenodd" d="M4 5h16a1 1 0 0 1 0 2H4a1 1 0 1 1 0-2zm0 6h16a1 1 0 0 1 0 2H4a1 1 0 0 1 0-2zm0 6h16a1 1 0 0 1 0 2H4a1 1 0 0 1 0-2z" />
                            )}
                        </svg>
                    </button>
                    {/* <div className={`lg:flex hidden group-hover:block lg:block lg:static md:px-12 md:mx-12 inset-x-0 top-16 py-3 shadow-md lg:shadow-none text-blue-900 ${  isOpen ? "block" : "hidden" }`}>
                        <MenuItems />;
                    </div> */}
                    <div className='hidden space-x-6 lg:inline-block'>
                        <MenuItems />
                    </div>

                    <div className={`fixed transition-all duration-300 ease-in-out flex justify-center left-0 w-full h-auto rounded-md p-24 bg-white rounded-lg block lg:hidden shadow-xl top-16 ${  isOpen ? "block" : "hidden" } `}>
                        <div className='flex flex-col space-y-6'>
                            <MenuItems />
                        </div>                                                
                    </div>

                </div>
            </div>
        </nav>
    )
    
}


export default Navbar1;
"""
 navbars["navbar_1"] = navbar_1
 
 '''
 

 '''
 navbar_2 ="""
import React from 'react';
import { Link } from 'react-router-dom';

const Navbar= () => {
    return (
        <nav classNameName="bg-white shadow-lg">
            <div classNameName="md:flex items-center justify-between py-2 px-8 md:px-12">
                <div className="flex justify-between items-center">
                <div className="text-2xl font-bold text-gray-800 md:text-3xl">
                        <Link to="/">Brand</Link>
                </div>
                    <div className="md:hidden">
                        <button type="button" className="block text-gray-800 hover:text-gray-700 focus:text-gray-700 focus:outline-none">
                            <svg className="h-6 w-6 fill-current" viewBox="0 0 24 24">
                                <path className="hidden" d="M16.24 14.83a1 1 0 0 1-1.41 1.41L12 13.41l-2.83 2.83a1 1 0 0 1-1.41-1.41L10.59 12 7.76 9.17a1 1 0 0 1 1.41-1.41L12 10.59l2.83-2.83a1 1 0 0 1 1.41 1.41L13.41 12l2.83 2.83z"/>
                                <path d="M4 5h16a1 1 0 0 1 0 2H4a1 1 0 1 1 0-2zm0 6h16a1 1 0 0 1 0 2H4a1 1 0 0 1 0-2zm0 6h16a1 1 0 0 1 0 2H4a1 1 0 0 1 0-2z"/>
                            </svg>
                        </button>
                    </div>
                </div>
                <div className="flex flex-col md:flex-row hidden md:block -mx-2">
                    <Link to="/" className="text-gray-800 rounded hover:bg-gray-900 hover:text-gray-100 hover:font-medium py-2 px-2 md:mx-2">@@menu1@@
                    </Link>
                    <Link to="/" className="text-gray-800 rounded hover:bg-gray-900 hover:text-gray-100 hover:font-medium py-2 px-2 md:mx-2">@@menu2@@
                    </Link>
                    <Link to="/" className="text-gray-800 rounded hover:bg-gray-900 hover:text-gray-100 hover:font-medium py-2 px-2 md:mx-2">@@menu3@@</Link>
                </div>
            </div>
        </nav>
    );
  }
  export default Navbar;
 """
 navbars["navbar_2"] = navbar_2
 
 '''
 

 '''
 navbar_3 ="""
import React from 'react';
import { Link } from 'react-router-dom';

const Navbar3= () =>{
    return (
        <div className="bg-gray-100">
        <nav className="bg-white px-6 relative shadow-md">
            <div className="flex flex-row justify-between items-center py-2">
            <h3 className="font-semibold text-3xl text-gray-500">Webapp</h3>
            <div className="group flex flex-col items-center">
                <button className="p-2 rounded-lg md:hidden">
                <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" className="h-10 fill-current" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M2.5 12a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5z" /></svg>
                </button>
                <div className="hidden group-hover:block md:block absolute md:static bg-white inset-x-0 top-16 py-3 shadow-md md:shadow-none text-gray-600">
                <div className="flex flex-row justify-center items-center text-center font-semibold text-gray-500">
                    <Link className="px-6 py-1 flex flex-col md:flex-row md:items-center hover:bg-gray-700 hover:text-gray-100" to="/">
                    @@menu1@@ 
                    </Link>
                    <Link className="px-6 py-1 flex flex-col md:flex-row md:items-center hover:bg-gray-700 hover:text-gray-100" to="/">
                    @@menu2@@ 
                    </Link>
                    <Link className="px-6 py-1 flex flex-col md:flex-row md:items-center hover:bg-gray-700 hover:text-gray-100" to="/">
                    @@menu3@@ 
                    </Link>
                </div>
                </div>
            </div>
            </div>
        </nav>
        </div>
        );
    }

export default Navbar3;
 """
 navbars["navbar_3"] = navbar_3

 
 '''
 

 '''
 navbar_5 ="""
import React, {useState, useEffect} from 'react';
import Logo from './images/logo/logo.png';
import { Link } from "react-router-dom";

function Navbar5(){
  const [click, setClick] = useState(false);
  const [top, setTop] = useState(true);
  const handleClick = () => setClick(!click);
  const closeMobileMenu = () => setClick(false);

  useEffect(() => {
      const scrollHandler = () => {
        window.pageYOffset > 10 ? setTop(false) : setTop(true)
      };
      window.addEventListener('scroll', scrollHandler);
      return () => window.removeEventListener('scroll', scrollHandler);
    }, [top]);

    return (
        <nav className={`fixed z-30 w-full top-0 bg-white border-gray-200 px-2 sm:px-4 sm:py-2.5 dark:bg-gray-800 md:py-0 nav ${!top && 'bg-white shadow-lg'}`}>
          <div className="container flex flex-wrap justify-between items-center mx-auto">
          <a href="/" className="flex items-center w-[199px] md:w-60">
              <span className="self-center pl-4 font-semibold whitespace-nowrap dark:text-white">
              <img src={Logo} className="logo-img" /></span>
          </a>
          <Link to="/@@path6@@" onClick={closeMobileMenu} className="flex justify-center md:hidden lg:hidden">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24"><path d="M21 4H2v2h2.3l3.521 9.683A2.004 2.004 0 0 0 9.7 17H18v-2H9.7l-.728-2H18c.4 0 .762-.238.919-.606l3-7A.998.998 0 0 0 21 4z"></path><circle cx="10.5" cy="19.5" r="1.5"></circle><circle cx="16.5" cy="19.5" r="1.5"></circle></svg> <span className='bg-green-800 rounded-full text-white h-4 w-4 items-center pl-1 text-xs -ml-1.5'>0</span>
          </Link>
          <button data-collapse-toggle="mobile-menu" type="button" className="inline-flex items-center ml-3 text-sm text-gray-500 md:hidden  focus:outline-none transform-[translate(-60%, 70%)] duration-300 ease-out" aria-controls="mobile-menu-2" aria-expanded="false" onClick={handleClick}>
              <span className="sr-only">Open main menu</span>
              <svg xmlns="http://www.w3.org/2000/svg" className="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={3}>
              <path strokeLinecap="round" strokeLinejoin="round" d={click ? "M6 18L18 6M6 6l12 12" :"M4 6h16M4 12h8m-8 6h16" } />
              </svg>
          </button>
          <div className={click ? " w-full md:block md:w-auto mobile-menu" : " hidden w-full md:block md:w-auto mobile-menu"} id="mobile-menu">
            <ul className="flex flex-col mt-2 md:flex-row md:mt-0 md:text-sm md:font-medium nav">
            <Link to="/@@path1@@" onClick={closeMobileMenu}>
            <li className="pr-4 pl-4  rounded md:bg-transparent text-black dark:text-white hover:bg-gray-100 py-6 px-28">@@menu1@@</li>
            </Link>
            <Link to="/@@path2@@" onClick={closeMobileMenu}>
            <li className="pr-4 pl-4 rounded md:bg-transparent text-black dark:text-white hover:bg-gray-100 py-6 px-28">@@menu2@@</li>
            </Link>
            <Link to="/@@path3@@" onClick={closeMobileMenu}>
            <li className="pr-4 pl-4  rounded md:bg-transparent text-black dark:text-white hover:bg-gray-100 py-6 px-28">@@menu3@@</li>
            </Link>
            <Link to="/@@path4@@" onClick={closeMobileMenu} >
            <li className="pr-4 pl-4  rounded md:bg-transparent text-black dark:text-white hover:bg-gray-100 py-6 px-28">@@menu4@@</li>
            </Link>
            <Link to="/@@path5@@" onClick={closeMobileMenu}>
            <li className="pr-4 pl-4  rounded md:bg-transparent text-black dark:text-white hover:bg-gray-100 py-6 px-28">@@menu5@@</li>
            </Link>
            <li className="pr-4 pl-4  rounded md:bg-transparent text-black dark:text-white hover:bg-gray-100 py-6 px-28">
            <Link to="/@@path6@@" onClick={closeMobileMenu} className="hidden md:justify-center md:block">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" className='mr-6'><path d="M21 4H2v2h2.3l3.521 9.683A2.004 2.004 0 0 0 9.7 17H18v-2H9.7l-.728-2H18c.4 0 .762-.238.919-.606l3-7A.998.998 0 0 0 21 4z"></path><circle cx="10.5" cy="19.5" r="1.5"></circle><circle cx="16.5" cy="19.5" r="1.5"></circle></svg> <span className='bg-green-800 rounded-full text-white pt-0.5 pl-[6px] h-5 w-5 absolute md:bottom-[50px] lg:bottom-8 text-xs ml-4'>0</span>
            </Link>
            </li>
            </ul>
          </div>
        </div>
      </nav>
    )
}
export default Navbar5
 """
 navbars["navbar_5"] = navbar_5


 """
 Navigation component 6
 TODO: Replace dynamic text
 """
 navbar_6 ="""
import React, {
  useState, useEffect, 
  Fragment
} from 'react';
import { useDispatch, useSelector } from "react-redux";
import { NavLink, Link, useNavigate } from "react-router-dom";

import { 
  LogoutIcon, UserIcon,
  LoginIcon, UserAddIcon
} from '@heroicons/react/solid'
import { Menu, Transition } from '@headlessui/react'

import { signOut } from '../../../../redux/actions/authActions';
import * as ROUTE from '../../../../constants/routes';
import Logo from '../../../../images/logo/logo.png';
import Badge from '../../Badge';

function classNames(...classes) {
  return classes.filter(Boolean).join(' ')
}

const @@PageName@@ = () => {
  const [click, setClick] = useState(false);
  const [logout, setLogout] = useState(false);
  const [top, setTop] = useState(true);
  const handleClick = () => setClick(!click);
  const closeMobileMenu = () => setClick(false);

  const dispatch = useDispatch();
  const navigate = useNavigate();

  const store = useSelector((state) => ({
    cartTotalQuantity: state.cart.length,
    products: state.products,
    cart: state.cart,
    user: state.auth,
    profile: state.profile,
    isAuthenticating: state.app.isAuthenticating
  }));

  const handleLogout = () => {
    setLogout(true)
    dispatch(signOut())
  };

  useEffect(() => {
    if (logout) navigate(ROUTE.SIGNIN);
    setLogout(false);
  }, [logout]);

  useEffect(() => {
    const scrollHandler = () => {
      window.pageYOffset > 10 ? setTop(false) : setTop(true)
    };
    window.addEventListener('scroll', scrollHandler);
    return () => window.removeEventListener('scroll', scrollHandler);
  }, [top]);

    return (
      <>
      <nav className={`fixed z-30 w-full top-0 bg-white border-gray-200 sm:px-4 sm:py-2.5 md:py-0 nav ${!top && 'bg-white shadow-lg'}`}>
          <div className="container flex flex-wrap justify-between items-center mx-auto">
            <a href={ROUTE.HOME} className="flex items-center w-[159px] md:w-60 py-4 md:py-6">
                <span className="self-center pl-4 font-semibold whitespace-nowrap ">
                <img src={Logo} className="logo-img" /></span>
            </a>
            <NavLink to={ROUTE.CART} onClick={closeMobileMenu} className="flex justify-center lg:hidden">
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24">
                <path d="M21 4H2v2h2.3l3.521 9.683A2.004 2.004 0 0 0 9.7 17H18v-2H9.7l-.728-2H18c.4 0 .762-.238.919-.606l3-7A.998.998 0 0 0 21 4z"></path>
                <circle cx="10.5" cy="19.5" r="1.5"></circle>
                <circle cx="16.5" cy="19.5" r="1.5"></circle>
              </svg> 
              <Badge count={store.cartTotalQuantity}></Badge>
            </NavLink>
            <Link to='#' onClick={closeMobileMenu} className="flex justify-center lg:hidden dropdown-toggle" data-bs-toggle="dropdown">
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24">
                <path d="M7.5 6.5C7.5 8.981 9.519 11 12 11s4.5-2.019 4.5-4.5S14.481 2 12 2 7.5 4.019 7.5 6.5zM20 21h1v-1c0-3.859-3.141-7-7-7h-4c-3.86 0-7 3.141-7 7v1h17z"></path>
              </svg>
              <Menu as="div" className="relative inline-block text-left">
                <div>
                  <Menu.Button className="items-center rounded-full text-base text-gray-500 transition duration-75 group hover:bg-gray-100 font-medium">
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
                    {!store.user ? (
                      <>
                        <div className="py-1">
                          <Menu.Item>
                            {({ active }) => (
                              <NavLink
                                to={ROUTE.SIGNIN}
                                className={classNames(
                                  active ? 'bg-gray-100 text-gray-900' : 'text-gray-700',
                                  'inline-flex w-full text-left px-4 py-2 text-sm'
                                )}
                              >
                              <LoginIcon className="-ml-1 mr-2 h-5 w-5" aria-hidden="true" />
                                Sign In
                              </NavLink>
                            )}
                          </Menu.Item>
                        </div>
                        <hr />
                        <div className="py-1">
                          <Menu.Item>
                            {({ active }) => (
                              <NavLink
                                to={ROUTE.SIGNUP}
                                className={classNames(
                                  active ? 'bg-gray-100 text-gray-900' : 'text-gray-700',
                                  'inline-flex w-full text-left px-4 py-2 text-sm'
                                )}
                              >
                              <UserAddIcon className="-ml-1 mr-2 h-5 w-5" aria-hidden="true" />
                                Sign Up
                              </NavLink>
                            )}
                          </Menu.Item>
                        </div>
                      </>
                    ) : (
                      <>
                      {store.profile.user_type !== 'admin' && (
                        <>
                          <div className="py-1">
                            <Menu.Item>
                              {({ active }) => (
                                <NavLink
                                  to={ROUTE.PROFILE}
                                  className={classNames(
                                    active ? 'bg-gray-100 text-gray-900' : 'text-gray-700',
                                    'inline-flex w-full text-left px-4 py-2 text-sm'
                                  )}
                                >
                                <UserIcon className="-ml-1 mr-2 h-5 w-5" aria-hidden="true" />
                                  My Account
                                </NavLink>
                              )}
                            </Menu.Item>
                          </div>
                          <hr />
                          </>
                      )}
                        <div className="py-1">
                          <form method="POST" action="#">
                            <Menu.Item>
                              {({ active }) => (
                                <button
                                  type="submit"
                                  onClick={() => 
                                    handleLogout()
                                  }
                                  className={classNames(
                                    active ? 'bg-gray-100 text-gray-900' : 'text-gray-700',
                                    'inline-flex w-full text-left px-4 py-2 text-sm'
                                  )}
                                >
                                <LogoutIcon className="-ml-1 mr-2 h-5 w-5" aria-hidden="true" />
                                  Sign out
                                </button>
                              )}
                            </Menu.Item>
                          </form>
                        </div>
                      </>
                    )}
                  </Menu.Items>
                </Transition>
              </Menu>
            </Link>
          <button data-collapse-toggle="mobile-menu" type="button" className="inline-flex items-center ml-3 text-sm text-gray-500 lg:hidden  focus:outline-none transform-[translate(-60%, 70%)] duration-300 ease-out" aria-controls="mobile-menu-2" aria-expanded="false" onClick={handleClick}>
            <span className="sr-only">Open main menu</span>
            <svg xmlns="http://www.w3.org/2000/svg" className="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={3}>
              <path strokeLinecap="round" strokeLinejoin="round" d={click ? "M6 18L18 6M6 6l12 12" :"M4 6h16M4 12h8m-8 6h16" } />
            </svg>
        </button>
        <div className={click ? " w-full lg:block lg:w-auto mobile-menu" : " hidden w-full lg:block lg:w-auto mobile-menu"} id="mobile-menu">
          <ul className="flex flex-col mt-2 lg:flex-row lg:mt-0 lg:text-sm md:font-medium nav">
            <NavLink to={ROUTE.FIND_YOUR_DEAL} onClick={closeMobileMenu} className="border-t-2 md:border-none">
              <li className="border-t-2 pr-4 pl-6 pb-2 pt-2 font-medium rounded md:py-6 px-28 pb-2 pt-2 border-none font-normal bg-transparent text-black hover:bg-gray-100">Find your deal</li>
            </NavLink>
            <NavLink to={ROUTE.ABOUT_BEST_DEAL_NAIJA} onClick={closeMobileMenu} className="border-t-2 md:border-none">
              <li className="border-t-2 pr-4 pl-6 pb-2 pt-2 font-medium rounded md:py-6 px-28 pb-2 pt-2 border-none font-normal bg-transparent text-black hover:bg-gray-100 py-6 px-28">About BestDealNaija</li>
            </NavLink>
            <NavLink to={ROUTE.BLOG} onClick={closeMobileMenu} className="border-t-2 md:border-none">
              <li className="border-8 pr-4 pl-6 pb-2 pt-2 font-medium rounded md:py-6 px-28 pb-2 pt-2 border-none font-normal bg-transparent text-black hover:bg-gray-100 py-6 px-28">Blog</li>
            </NavLink>
            <NavLink to={ROUTE.CONTACT} onClick={closeMobileMenu} className="border-t-2 md:border-none">
              <li className="border-t-2 pr-4 pl-6 pb-2 pt-2 font-medium rounded md:py-6 px-28 pb-2 pt-2 border-none font-normal bg-transparent text-black hover:bg-gray-100 py-6 px-28">Contact</li>
            </NavLink>
            <NavLink to={ROUTE.BEST_DEAL_TRADE_FAIR} onClick={closeMobileMenu} className="border-t-2 md:border-none">
              <li className="border-t-2 pr-4 pl-6 pb-2 pt-2 font-medium rounded md:py-6 px-28 pb-2 pt-2 border-none font-normal bg-transparent text-black hover:bg-gray-100 py-6 px-28">BestDeal Trade Fair</li>
            </NavLink>
            <li className="flex flex-row whitespace-nowrap pr-4 pl-4 rounded md:bg-transparent text-black  py-6 px-28">
              <NavLink to={ROUTE.CART} onClick={closeMobileMenu} className="hidden lg:justify-center lg:block hover:bg-gray-100">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" className='mr-6'>
                  <path d="M21 4H2v2h2.3l3.521 9.683A2.004 2.004 0 0 0 9.7 17H18v-2H9.7l-.728-2H18c.4 0 .762-.238.919-.606l3-7A.998.998 0 0 0 21 4z"></path>
                  <circle cx="10.5" cy="19.5" r="1.5"></circle>
                  <circle cx="16.5" cy="19.5" r="1.5"></circle>
                </svg>
              <Badge count={store.cartTotalQuantity}></Badge>
              </NavLink>
            </li>
            <li className="flex flex-row whitespace-nowrap pr-4 pl-4  rounded md:bg-transparent text-black  py-6 px-28">
              <Menu as="div" className="relative inline-block text-left">
                <div>
                  <Menu.Button className="hidden md:flex items-center rounded-full text-base text-gray-500 transition duration-75 group hover:bg-gray-100 font-medium">
                  <Link to="#" data-bs-toggle="dropdown" 
                      className="hidden md:justify-center md:block dropdown-toggle">
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
                    {!store.user ? (
                      <>
                        <div className="py-1">
                          <Menu.Item>
                            {({ active }) => (
                              <NavLink
                                to={ROUTE.SIGNIN}
                                className={classNames(
                                  active ? 'bg-gray-100 text-gray-900' : 'text-gray-700',
                                  'inline-flex w-full text-left px-4 py-2 text-sm'
                                )}
                              >
                              <LoginIcon className="-ml-1 mr-2 h-5 w-5" aria-hidden="true" />
                                Sign In
                              </NavLink>
                            )}
                          </Menu.Item>
                        </div>
                        <hr />
                        <div className="py-1">
                          <Menu.Item>
                            {({ active }) => (
                              <NavLink
                                to={ROUTE.SIGNUP}
                                className={classNames(
                                  active ? 'bg-gray-100 text-gray-900' : 'text-gray-700',
                                  'inline-flex w-full text-left px-4 py-2 text-sm'
                                )}
                              >
                              <UserAddIcon className="-ml-1 mr-2 h-5 w-5" aria-hidden="true" />
                                Sign Up
                              </NavLink>
                            )}
                          </Menu.Item>
                        </div>
                      </>
                    ) : (
                      <>
                      {store.profile.user_type !== 'admin' && (
                        <>
                          <div className="py-1">
                            <Menu.Item>
                              {({ active }) => (
                                <NavLink
                                  to={ROUTE.PROFILE}
                                  className={classNames(
                                    active ? 'bg-gray-100 text-gray-900' : 'text-gray-700',
                                    'inline-flex w-full text-left px-4 py-2 text-sm'
                                  )}
                                >
                                <UserIcon className="-ml-1 mr-2 h-5 w-5" aria-hidden="true" />
                                  My Account
                                </NavLink>
                              )}
                            </Menu.Item>
                          </div>
                          <hr />
                          </>
                      )}
                        <div className="py-1">
                          <form method="POST" action="#">
                            <Menu.Item>
                              {({ active }) => (
                                <button
                                  type="submit"
                                  onClick={() => 
                                    handleLogout()
                                  }
                                  className={classNames(
                                    active ? 'bg-gray-100 text-gray-900' : 'text-gray-700',
                                    'inline-flex w-full text-left px-4 py-2 text-sm'
                                  )}
                                >
                                <LogoutIcon className="-ml-1 mr-2 h-5 w-5" aria-hidden="true" />
                                  Sign out
                                </button>
                              )}
                            </Menu.Item>
                          </form>
                        </div>
                      </>
                    )}
                  </Menu.Items>
                </Transition>
              </Menu>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    </>
  );
};

export default @@PageName@@;
 """
 navbars["navbar_6"] = navbar_6


 """
 Navigation Cart Badge component
 """
 navbar_cart_badge_1 ="""
import PropType from 'prop-types';
import React from 'react';

const @@PageName@@ = ({ count }) => (
  <>
    {count >= 1 &&
      (<span className='bg-[#98c01d] rounded-full text-white pt-0.5 pl-[6px] h-5 w-5 absolute md:bottom-[50px] lg:bottom-8 text-xs ml-4'>
        {count}
      </span>)
    }
  </>
);

@@PageName@@.propTypes = {
  count: PropType.number.isRequired
};

export default @@PageName@@;
 """
 navbars["navbar_cart_badge_1"] = navbar_cart_badge_1


 """
 Navigation component 7: Vendor Header
 TODO: Replace dynamic text
 """
 navbar_7 ="""
import React, { useEffect } from 'react';
import { Link } from "react-router-dom";
import { useDispatch } from "react-redux";

import $ from "jquery";
import { FaBars } from "react-icons/fa";

import { signOut } from '../../../redux/actions/authActions';

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
    <header className="w-full flex flex-wrap items-center justify-between p-2 bg-white min-h-min bg-whte border-b-2 border-[#4fa607]">
      <div>
        <button
            className="block lg:hidden"
            data-trigger="#offcanvas_aside"
          >
            <FaBars className="w-6 h-6 ml-2 text-gray-500"/>
          </button>
      </div>
      <div className="col-nav grow-0 flex flex-row items-center space-x-4">
        
        <ul className="flex flex-row items-center">
          <li>
            <button type="button" className="flex items-center p-2 rounded-full text-base font-normal text-gray-500 transition duration-75 group hover:bg-gray-100" aria-controls="dropdown-example" data-collapse-toggle="dropdown-example">
                <Link className="dropdown-toggle" data-bs-toggle="dropdown" to="#">
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 fill-current"><path d="M7.5 6.5C7.5 8.981 9.519 11 12 11s4.5-2.019 4.5-4.5S14.481 2 12 2 7.5 4.019 7.5 6.5zM20 21h1v-1c0-3.859-3.141-7-7-7h-4c-3.86 0-7 3.141-7 7v1h17z"></path></svg>
                </Link>
                  <svg className="w-4 h-4" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fillRule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clipRule="evenodd"></path></svg>
            </button>
            <ul id="dropdown-example" className="hidden absolute right-4 bg-white rounded shadow-md w-48 py-2 space-y-2">
              <li>
                <form method="POST" action="#">
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
                </form>
              </li>
            </ul>
          </li>
        </ul>
      </div>
    </header>
  )
};

export default @@PageName@@;
 """
 navbars["navbar_7"] = navbar_7
 
 # ludayab
 navbar_8 ="""
import React from 'react'
import logo from '../../../../images/luday-logo.png'
/* This example requires Tailwind CSS v3.0+ */
import { useState } from 'react';
import { Dialog } from '@headlessui/react';
import { Bars3Icon, XMarkIcon } from '@heroicons/react/24/outline';
import { NavLink } from "react-router-dom";
import * as ROUTE from '../../../../constants/routes'

const @@PageName@@ = () => {

const [mobileMenuOpen, setMobileMenuOpen] = useState(false)

  return (
    <div className="isolate bg-white">
      <div className="px-6 pt-4 lg:px-8">
        <nav className="flex items-center justify-between" aria-label="Global">
          <div className="flex lg:flex-1">
            <a href="#" className="-m-1.5 p-1.5">
              <span className="sr-only">Your Company</span>
              <img className="w-30" src={logo} alt="" />
            </a>
          </div>
          <div className="flex lg:hidden">
            <button
              type="button"
              className="-m-2.5 inline-flex items-center justify-center rounded-md p-2.5 text-gray-700"
              onClick={() => setMobileMenuOpen(true)}
            >
              <span className="sr-only">Open main menu</span>
              <Bars3Icon className="h-6 w-6" aria-hidden="true" />
            </button>
          </div>
          <div className="hidden lg:flex lg:gap-x-12">
            <NavLink to={ROUTE.HOME} className="text-sm font-semibold leading-6 text-gray-900">
              @@Nav1@@
            </NavLink>
            <NavLink to={ROUTE.ABOUT} className="text-sm font-semibold leading-6 text-gray-900">
              @@Nav2@@
            </NavLink>
            <NavLink to={ROUTE.SERVICES} className="text-sm font-semibold leading-6 text-gray-900">
              @@Nav3@@
            </NavLink>
            <NavLink to={ROUTE.PORTFOLIO} className="text-sm font-semibold leading-6 text-gray-900">
              @@Nav4@@
            </NavLink>
            <NavLink to={ROUTE.BLOG} className="text-sm font-semibold leading-6 text-gray-900">
              @@Nav5@@
            </NavLink>
            <NavLink to={ROUTE.CONTACT} className="text-sm font-semibold leading-6 text-gray-900">
              @@Nav6@@
            </NavLink>
          </div>
          <div className="hidden lg:flex lg:flex-1 lg:justify-end">
          <button className="flex items-center px-4 py-2 font-medium tracking-wide text-white capitalize transition-colors duration-300 transform bg-blue-600 rounded-lg hover:bg-blue-500 focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-80">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6">
            <path strokeLinecap="round" strokeLinejoin="round" d="M15.75 10.5V6a3.75 3.75 0 10-7.5 0v4.5m11.356-1.993l1.263 12c.07.665-.45 1.243-1.119 1.243H4.25a1.125 1.125 0 01-1.12-1.243l1.264-12A1.125 1.125 0 015.513 7.5h12.974c.576 0 1.059.435 1.119 1.007zM8.625 10.5a.375.375 0 11-.75 0 .375.375 0 01.75 0zm7.5 0a.375.375 0 11-.75 0 .375.375 0 01.75 0z" />
          </svg>

            <NavLink to={ROUTE.QUOTE} className="mx-1">Get a Quote</NavLink>
          </button>
          </div>
        </nav>
        <Dialog as="div" open={mobileMenuOpen} onClose={setMobileMenuOpen}>
          <Dialog.Panel focus="true" className="fixed inset-0 z-10 overflow-y-auto bg-white px-6 py-6 lg:hidden">
            <div className="flex items-center justify-between">
              <a href="#" className="-m-1.5 p-1.5">
                <span className="sr-only">Your Company</span>
                <img className="w-30" src={logo} alt="Luday AB logo" />
              </a>
              <button
                type="button"
                className="-m-2.5 rounded-md p-2.5 text-gray-700"
                onClick={() => setMobileMenuOpen(false)}
              >
                <span className="sr-only">Close menu</span>
                <XMarkIcon className="h-6 w-6" aria-hidden="true" />
              </button>
            </div>
            <div className="mt-6 flow-root">
              <div className="-my-6 divide-y divide-gray-500/10">
                <div className="space-y-2 py-6">
                  <NavLink to={ROUTE.HOME} className="-mx-3 block rounded-lg py-2 px-3 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-400/10" onClick={() => setMobileMenuOpen(false)}>
                    @@Nav1@@
                  </NavLink>
                  <NavLink to={ROUTE.ABOUT} className="-mx-3 block rounded-lg py-2 px-3 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-400/10" onClick={() => setMobileMenuOpen(false)}>
                    @@Nav2@@
                  </NavLink>
                  <NavLink to={ROUTE.SERVICES} className="-mx-3 block rounded-lg py-2 px-3 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-400/10" onClick={() => setMobileMenuOpen(false)}>
                    @@Nav3@@
                  </NavLink>
                  <NavLink to={ROUTE.PORTFOLIO} className="-mx-3 block rounded-lg py-2 px-3 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-400/10" onClick={() => setMobileMenuOpen(false)}>
                    @@Nav4@@
                  </NavLink>
                  <NavLink to={ROUTE.BLOG} className="-mx-3 block rounded-lg py-2 px-3 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-400/10" onClick={() => setMobileMenuOpen(false)}>
                    @@Nav5@@
                  </NavLink>
                  <NavLink to={ROUTE.CONTACT} className="-mx-3 block rounded-lg py-2 px-3 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-400/10" onClick={() => setMobileMenuOpen(false)}>
                    @@Nav6@@
                  </NavLink>
                </div>
                <div className="py-6">
                  <button className="flex items-center px-4 py-2 font-medium tracking-wide text-white capitalize transition-colors duration-300 transform bg-blue-900 rounded-lg hover:bg-blue-500 focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-80">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6">
                      <path strokeLinecap="round" strokeLinejoin="round" d="M15.75 10.5V6a3.75 3.75 0 10-7.5 0v4.5m11.356-1.993l1.263 12c.07.665-.45 1.243-1.119 1.243H4.25a1.125 1.125 0 01-1.12-1.243l1.264-12A1.125 1.125 0 015.513 7.5h12.974c.576 0 1.059.435 1.119 1.007zM8.625 10.5a.375.375 0 11-.75 0 .375.375 0 01.75 0zm7.5 0a.375.375 0 11-.75 0 .375.375 0 01.75 0z" />
                    </svg>

                      <NavLink to={ROUTE.QUOTE} className="mx-1" onClick={() => setMobileMenuOpen(false)}>Get a Quote</NavLink>
                  </button>
                </div>
              </div>
            </div>
          </Dialog.Panel>
        </Dialog>
      </div>
    </div>
  )
};

export default @@PageName@@;
 """
 navbars["navbar_8"] = navbar_8


 """
 Example component
 """
 example ="""
import React from 'react';
const @@PageName@@ = () => {

};

export default @@PageName@@;
 """
 navbars["example"] = example
 