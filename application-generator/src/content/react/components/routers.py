class Routers:

 routers = {}
 
 # Add Admin route
 routers_adminRoute ="""
/* eslint-disable react/forbid-prop-types */
/* eslint-disable react/jsx-props-no-spreading */
import React from 'react';
import { connect } from 'react-redux';
import { Navigate } from 'react-router-dom';

import PropType from 'prop-types';

import { Sidebar, Header } from '../components/admin';
import * as CONSTANT from '../constants/constants';
import './styles/admin_route.css';

/**
 * Authentication guard for routes
 * 
 * @param {PropTypes.bool} isAuth element/bool
 * @param {PropTypes.string} user_type element/string
 * @param {PropTypes.func} component element/func
 * 
 */

const AdminRoute = ({ isAuth, user_type, component: Component }) => {

	if(isAuth && user_type === CONSTANT.ADMIN_ROLE || isAuth && user_type === CONSTANT.SUB_ADMIN_ROLE) {
    return (
      <>
        <Sidebar />
        <main className="main-wrap bg-gray-100 h-screen overflow-y-auto">
          <Header />
          <Component />
        </main>
      </>
    );
  }
  return (
    <Navigate to="/" />
  );
  
}

AdminRoute.defaultProps = {
  isAuth: false,
  user_type: CONSTANT.USER_ROLE
};

AdminRoute.propTypes = {
  isAuth: PropType.bool,
  user_type: PropType.string,
  component: PropType.func.isRequired
};

const mapStateToProps = ({ auth }) => ({
  isAuth: !!auth,
  user_type: auth?.user_type || ''
});

export default connect(mapStateToProps)(AdminRoute);
 """
 routers["routers_adminRoute"] = routers_adminRoute


 # Add AppRouter
 routers_appRouter ="""
import React from 'react';
import { 
	BrowserRouter as Router,
	// unstable_HistoryRouter as HistoryRouter,
	Routes, 
	Route
} from 'react-router-dom';

import { createBrowserHistory } from 'history';

import { 
	Home, About, FindDeal, 
	Contact, Blog, TradeFair, 
	AdminDashboard, Categories, 
	EditCategories, AllProducts, Products, 
	EditProduct, VerifyProduct, 
	ViewProductDetails, Orders, ViewOrder, 
	VendorAddProduct, VendorProducts, VendorEditProduct,
	ProductDetails, Cart, VendorDetails, 
	Checkout, Delivery, Paymemt, Profile, 
	ChangePassword, OrderHistory, 
	CategoryProducts, SearchProducts, SignUp, 
	SignIn, SignUpVendor,
	AllBlogs, AddBlog, EditBlog, BlogDetails,
	AddVendor, EditVendor, AllVendors, Vendors, VendorOrder,
	VendorDasboard, PaystackCallback,
	CashOnDeliveryCallback,
	Users, SignUpVendorComplete, 
	ViewVendor, VerifyVendors, CreateAdmin, ManageAdmins, EditAdmins, VendorProduct, SignUpVendorsDetails,
	UsersGuide, OwnersGuide
 }  from '../pages';

import * as ROUTES from '../constants/routes';
import PublicRoute from './PublicRoute';
import StaticRoute from './StaticRoute';
import ClientRoute from './ClientRoute';
import AdminRoute from './AdminRoute';
import VendorRoute from './VendorRoute';
// import NotFound from '../components/default/NotFound';

export const history = createBrowserHistory();

const AppRouter = () => (
	<Router history={history}>
		<>
			<Routes>
				<Route element={<StaticRoute />}>
					<Route
						element={<SearchProducts />}
						exact
						path={ROUTES.SEARCH}
					/>
					<Route
						element={<Home />}
						path={ROUTES.HOME}
					/>
					<Route
						element={<FindDeal />}
						path={ROUTES.FIND_YOUR_DEAL}
					/>
					<Route
						element={<About />}
						path={ROUTES.ABOUT_BEST_DEAL_NAIJA}
					/>
					<Route
						element={<Blog />}
						path={ROUTES.BLOG}
					/>
					<Route
						element={<BlogDetails />}
						path={`${ROUTES.BLOG_DETAILS}/:slug`}
					/>
					<Route
						element={<Contact />}
						path={ROUTES.CONTACT}
					/>
					<Route
						element={<TradeFair />}
						path={ROUTES.BEST_DEAL_TRADE_FAIR}
					/>
					<Route
						element={<Products />}
						path={ROUTES.PRODUCTS}
					/>	
					<Route
						element={<CategoryProducts />}
						path={`${ROUTES.CATEGORY_PRODUCTS}/:slug`}
					/>					
					<Route
						element={<VendorProduct />}
						path={`${ROUTES.VENDOR_PRODUCTS_VIEW}/:slug`}
					/>				
					<Route
						element={<ProductDetails />}
						path={`${ROUTES.PRODUCT_DETAILS}/:slug`}
					/>					
					<Route
						element={<Cart />}
						path={ROUTES.CART}
					/>					
					<Route
						element={<Vendors />}
						path={ROUTES.VENDORS}
					/>			
					<Route
						element={<VendorDetails />}
						path={`${ROUTES.VENDORDETAILS}/:slug`}
					/>					
					<Route
						element={<Checkout />}
						path={ROUTES.CHECKOUT}
					/>
					<Route
						element={<Delivery />}
						path={ROUTES.DELIVERY}
					/>
					<Route
						element={<Paymemt />}
						path={ROUTES.PAYMENT}
					/>
					<Route
						element={<PaystackCallback />}
						path={ROUTES.ORDER_CALLBACK}
					/>
					<Route
						element={<CashOnDeliveryCallback />}
						path={ROUTES.CASH_ORDER_CALLBACK}
					/>	
					<Route
						element={<UsersGuide />}
						path={ROUTES.USERS_GUIDE}
					/>
					<Route
						element={<OwnersGuide />}
						path={ROUTES.OWNERS_GUIDE}
					/>
				</Route>
				<Route
					path={ROUTES.SIGNUP}
					element={
						<PublicRoute 
							component={SignUp} 
							path={ROUTES.SIGNUP}
						/>
					}
				/>
				<Route
					path={ROUTES.SIGNUP_VENDOR}
					element={
						<PublicRoute 
							component={SignUpVendor} 
							path={ROUTES.SIGNUP_VENDOR} 
						/>
					}
				/>
				<Route
					path={ROUTES.SIGNIN}
					element={
						<PublicRoute 
							component={SignIn} 
							path={ROUTES.SIGNIN} 
						/>
					}
				/>
				<Route
					path={ROUTES.FORGOT_PASSWORD}
					element={
						<PublicRoute 
							path={ROUTES.SIGNIN} 
						/>
					}
				/>
				<Route
					path={ROUTES.RESET_PASSWORD}
					element={
						<PublicRoute 
							path={ROUTES.RESET_PASSWORD} 
						/>
					}
				/>
				<Route
					path={ROUTES.PROFILE}
					element={
						<ClientRoute 
							component={Profile} 
							path={ROUTES.PROFILE} 
						/>
					}
				/>
				<Route
					path={ROUTES.CHANGEPASSWORD}
					element={
						<ClientRoute 
							component={ChangePassword} 
							path={ROUTES.CHANGEPASSWORD} 
						/>
					}
				/>
				<Route
					path={ROUTES.ORDER_HISTORY}
					element={
						<ClientRoute 
							component={OrderHistory} 
							path={ROUTES.ORDER_HISTORY} 
						/>
					}
				/>
				<Route
					path={`${ROUTES.ORDER_DETAILS}/:id/:ref`}
					element={
						<ClientRoute 
							path={`${ROUTES.ORDER_DETAILS}/:id/:ref`} 
						/>
					}
				/>
				<Route
					path={ROUTES.VIEW_ORDER}
					element={
						<ClientRoute 
							component={OrderHistory} 
							path={ROUTES.VIEW_ORDER} 
						/>
					}
				/>
				<Route
					path={ROUTES.SIGNUP_VENDOR_DETAILS}
					element={
						<VendorRoute 
							component={SignUpVendorsDetails} 
							path={ROUTES.SIGNUP_VENDOR_DETAILS} 
						/>
					}
				/>				
				<Route
					path={ROUTES.SIGNUP_VENDOR_COMPLETE}
					element={
						<VendorRoute 
							component={SignUpVendorComplete} 
							path={ROUTES.SIGNUP_VENDOR_COMPLETE} 
						/>
					}
				/>				
				<Route
					path={ROUTES.VENDOR_DASHBOARD}
					element={
						<VendorRoute 
							component={VendorDasboard} 
							path={ROUTES.VENDOR_DASHBOARD} 
						/>
					}
				/>
				<Route
					path={ROUTES.ADMIN_DASHBOARD}
					element={
						<AdminRoute 
							component={AdminDashboard} 
							path={ROUTES.ADMIN_DASHBOARD} 
						/>
					}
				/>
				<Route
					path={ROUTES.ADMIN_CATEGORIES}
					element={
						<AdminRoute 
							component={Categories} 
							path={ROUTES.ADMIN_CATEGORIES} 
						/>
					}
				/>
				<Route
					path={`${ROUTES.ADMIN_EDIT_CATEGORIES}/:id`}
					element={
						<AdminRoute 
							component={EditCategories} 
							path={`${ROUTES.ADMIN_EDIT_CATEGORIES}/:id`} 
						/>
					}
				/>
				<Route
					path={ROUTES.ADMIN_PRODUCTS}
					element={
						<AdminRoute 
							component={AllProducts} 
							path={ROUTES.ADMIN_PRODUCTS} 
						/>
					}
				/>
				<Route
					path={ROUTES.VENDOR_ADD_PRODUCTS}
					element={
						<VendorRoute 
							component={VendorAddProduct} 
							path={ROUTES.VENDOR_ADD_PRODUCTS} 
						/>
					}
				/>
				<Route
					path={`${ROUTES.VENDOR_EDIT_PRODUCTS}/:id`}
					element={
						<VendorRoute 
							component={VendorEditProduct} 
							path={`${ROUTES.VENDOR_EDIT_PRODUCTS}/:id`} 
						/>
					}
				/>
				<Route
					path={ROUTES.VENDOR_PRODUCTS}
					element={
						<VendorRoute 
							component={VendorProducts} 
							path={ROUTES.VENDOR_PRODUCTS} 
						/>
					}
				/>
				<Route
					path={ROUTES.VENDOR_ORDERS}
					element={
						<VendorRoute 
							component={VendorOrder} 
							path={ROUTES.VENDOR_ORDERS} 
						/>
					}
				/>
				<Route
					path={ROUTES.ADMIN_VERIFY_PRODUCTS}
					element={
						<AdminRoute 
							component={VerifyProduct} 
							path={ROUTES.ADMIN_VERIFY_PRODUCTS} 
						/>
					}
				/>
				<Route
					path={`${ROUTES.ADMIN_VIEW_PRODUCT}/:id`} 
					element={
						<AdminRoute 
							component={ViewProductDetails} 
							path={`${ROUTES.ADMIN_VIEW_PRODUCT}/:id`} 
						/>
					}
				/>
				<Route
					path={`${ROUTES.ADMIN_EDIT_PRODUCTS}/:id`}
					element={
						<AdminRoute 
							component={EditProduct} 
							path={`${ROUTES.ADMIN_EDIT_PRODUCTS}/:id`} 
						/>
					}
				/>
				<Route
					path={ROUTES.ADMIN_VENDORS}
					element={
						<AdminRoute 
							component={AllVendors} 
							path={ROUTES.ADMIN_VENDORS} 
						/>
					}
				/>
				<Route
					path={ROUTES.ADMIN_VERIFY_VENDORS}
					element={
						<AdminRoute 
							component={VerifyVendors} 
							path={ROUTES.ADMIN_VERIFY_VENDORS} 
						/>
					}
				/>
				<Route
					path={ROUTES.ADMIN_ADD_VENDORS}
					element={
						<AdminRoute 
							component={AddVendor} 
							path={ROUTES.ADMIN_ADD_VENDORS} 
						/>
					}
				/>
				<Route
					path={`${ROUTES.ADMIN_EDIT_VENDORS}/:id/:slug`}
					element={
						<AdminRoute 
							component={EditVendor} 
							path={ROUTES.ADMIN_EDIT_VENDORS} 
						/>
					}
				/>
				<Route
					path={`${ROUTES.ADMIN_VIEW_VENDORS}/:id/:slug`}
					element={
						<AdminRoute 
							component={ViewVendor} 
							path={ROUTES.ADMIN_VIEW_VENDORS} 
						/>
					}
				/>
				<Route
					path={ROUTES.ADMIN_ORDERS}
					element={
						<AdminRoute 
							component={Orders} 
							path={ROUTES.ADMIN_ORDERS} 
						/>
					}
				/>
				<Route
					path={`${ROUTES.VIEW_ORDERS}/:id/:trans_id`}
					element={
						<AdminRoute 
							component={ViewOrder} 
							path={ROUTES.VIEW_ORDERS} 
						/>
					}
				/>
				<Route
					path={ROUTES.ADMIN_BLOGS}
					element={
						<AdminRoute 
							component={AllBlogs} 
							path={ROUTES.ADMIN_BLOGS} 
						/>
					}
				/>
				<Route
					path={ROUTES.ADMIN_ADD_BLOGS}
					element={
						<AdminRoute 
							component={AddBlog} 
							path={ROUTES.ADMIN_ADD_BLOGS} 
						/>
					}
				/>
				<Route
					path={`${ROUTES.ADMIN_EDIT_BLOGS}/:id`}
					element={
						<AdminRoute 
							component={EditBlog} 
							path={`${ROUTES.ADMIN_EDIT_BLOGS}/:id`} 
						/>
					}
				/>
				<Route
					path={ROUTES.ADMIN_USERS}
					element={
						<AdminRoute 
							component={Users} 
							path={ROUTES.ADMIN_USERS} 
						/>
					}
				/>	
				<Route
					path={ROUTES.ADMIN_CREATE_ADMIN}
					element={
						<AdminRoute 
							component={CreateAdmin} 
							path={ROUTES.ADMIN_CREATE_ADMIN} 
						/>
					}
				/>
				<Route
					path={ROUTES.ADMIN_MANAGE_ADMINS}
					element={
						<AdminRoute 
							component={ManageAdmins} 
							path={ROUTES.ADMIN_MANAGE_ADMINS} 
						/>
					}
				/>
				<Route
					path={`${ROUTES.ADMIN_EDIT_ADMINS}/:id`}
					element={
						<AdminRoute 
							component={EditAdmins} 
							path={`${ROUTES.ADMIN_EDIT_ADMINS}/:id`} 
						/>
					}
				/>
			</Routes>
		</>
	</Router>	
);
  
export default AppRouter;
 """
 routers["routers_appRouter"] = routers_appRouter


# ludayab
 routers_appRouter_2 ="""
import React from 'react';
import { 
	BrowserRouter as Router,
	// unstable_HistoryRouter as HistoryRouter,
	Routes, 
	Route
} from 'react-router-dom';

import { createBrowserHistory } from 'history';

import { 
	Home, About, Blog, BlogDetails, Contact,
	Quote, Services, ServiceDetails, Portfolio 
 }  from '../pages';

import * as ROUTES from '../constants/routes';
import StaticRoute from './StaticRoute';

export const history = createBrowserHistory();

const AppRouter = () => (
	<Router history={history}>
		<>
			<Routes>
				<Route  element={<StaticRoute />} >
					<Route
						element={<Home />}
						path={ROUTES.HOME}
					/>
					<Route
						element={<About />}
						path={ROUTES.ABOUT}
					/>
					<Route
						element={<Blog />}
						path={ROUTES.BLOG}
					/>
					<Route
						element={<BlogDetails />}
						path={ROUTES.BLOG_DETAILS}
					/>
					<Route
						element={<Services />}
						path={ROUTES.SERVICES}
					/>
					<Route
						element={<Portfolio />}
						path={ROUTES.PORTFOLIO}
					/>
					<Route
						element={<ServiceDetails />}
						path={ROUTES.SERVICES}
					/>
					<Route
						element={<Quote />}
						path={ROUTES.QUOTE}
					/>
					<Route
						element={<Contact />}
						path={ROUTES.CONTACT}
					/>
					
				</Route>
			</Routes>
		</>
	</Router>	
);
  
export default AppRouter;
 """
 routers["routers_appRouter_2"] = routers_appRouter_2


 # Add Client route
 routers_clientRoute ="""
/* eslint-disable react/forbid-prop-types */
/* eslint-disable react/jsx-props-no-spreading */
import React from 'react';
import {  connect } from 'react-redux';
import { useLocation, Navigate } from 'react-router-dom';

import PropType from 'prop-types';

import { 
	ADMIN_DASHBOARD, SIGNIN 
} from '../constants/routes';
import { Footer, Navigation } from '../components/default';

/**
 * Authentication guard for routes
 * 
 * @param {PropTypes.bool} isAuth element/bool
 * @param {PropTypes.string} user_type element/string
 * @param {PropTypes.func} component element/func
 * 
 */

const ClientRoute = ({ 
	isAuth, user_type, component: Component
 }) => {
	let location = useLocation();
	let _from = location.state?.from?.pathname || "/";

	if (isAuth && user_type === 'user') {
		return (
			<>
				<Navigation />
					<Component />
				<Footer />
			</>
		);
	}
	if (isAuth && user_type === 'super-admin') {
		return <Navigate to={ADMIN_DASHBOARD} replace state={{ location }} />;
	}

	return (
		<Navigate 
			to={SIGNIN} 
			replace 
			state={{from: _from }} />
	);
}

ClientRoute.defaultProps = {
  isAuth: false,
  user_type: 'user',
  is_active: false
};

ClientRoute.propTypes = {
  isAuth: PropType.bool,
  user_type: PropType.string,
//   is_active: PropType.bool,
  component: PropType.func.isRequired
};

const mapStateToProps = ({ auth }) => ({
  isAuth: !!auth,
  user_type: auth?.user_type || ''
//   is_active: auth?.is_active || false
});

export default connect(mapStateToProps)(ClientRoute);
 """
 routers["routers_clientRoute"] = routers_clientRoute


 # Add Public route
 routers_publicRoute ="""
/* eslint-disable react/forbid-prop-types */
/* eslint-disable react/jsx-props-no-spreading */
import React from 'react';
import {  connect, useSelector } from 'react-redux';
import { useLocation, Navigate } from 'react-router-dom';
import PropType from 'prop-types';

import { ADMIN_DASHBOARD, VENDOR_DASHBOARD,
  SIGNIN, SIGNUP, SIGNUP_VENDOR_DETAILS
} from '../constants/routes';
import * as ROUTE from '../constants/routes';
import * as CONSTANT from '../constants/constants';
import { Footer, Navigation } from '../components/default';
import { useDidMount } from '../hooks';
import Alert from '../helpers/Alert';

/**
 * Authentication guard for routes
 * 
 * @param {PropTypes.bool} isAuth element/bool
 * @param {PropTypes.string} user_type element/string
 * @param {PropTypes.func} component element/func
 * @param {PropTypes.string} path element/string
 * 
 */

const PublicRoute = ({ isAuth, user_type, is_active, component: Component, path }) => {
  
  let location = useLocation();
  const didMount = useDidMount(true);
  let from = location.state?.from?.pathname || ROUTE.PROFILE;
  const { authStatus } = useSelector((state) => ({
    authStatus: state.app.authStatus
  }));

  if (isAuth && user_type === CONSTANT.ADMIN_ROLE || isAuth && user_type === CONSTANT.SUB_ADMIN_ROLE) {
    if (didMount) {
      return <Navigate to={ADMIN_DASHBOARD} replace state={{ location }} />;
    }
  }
  if (isAuth && !is_active && user_type === CONSTANT.VENDOR_ROLE) {
    if (didMount) {
      return <Navigate to={SIGNUP_VENDOR_DETAILS} replace state={{ location }} />;
    }
  }
  if (isAuth && is_active && user_type === CONSTANT.VENDOR_ROLE) {
    if (didMount) {
      return <Navigate to={VENDOR_DASHBOARD} replace state={{ location }} />;
    }
  }
  if ((isAuth && user_type === CONSTANT.USER_ROLE) && (path === SIGNIN || path === SIGNUP)) {
    if (didMount) {
      return <Navigate to={from} replace state={{ location }} />;
    }
  }

  if (didMount) {
    return (
      <>
        <Navigation />
          {authStatus?.message && (
            <nav className='fixed z-20 w-full top-0 bg-white border-gray-200'>
              <Alert
                status={authStatus.status}
                mssg={authStatus.message}
                type={authStatus.type}
            />
            </nav>
          )}
          <Component />
        <Footer />
      </>
    );
  }
}

PublicRoute.defaultProps = {
  isAuth: false,
  user_type: CONSTANT.USER_ROLE,
  is_active: false,
  path: '/'
};

PublicRoute.propTypes = {
  isAuth: PropType.bool,
  user_type: PropType.string,
  is_active: PropType.bool,
  component: PropType.func.isRequired,
  path: PropType.string
};

const mapStateToProps = ({ auth }) => ({
  isAuth: !!auth,
  user_type: auth?.user_type || '',
  is_active: auth?.is_active || false
});

export default connect(mapStateToProps)(PublicRoute);
 """
 routers["routers_publicRoute"] = routers_publicRoute


 # Add Static route
 routers_staticRoute ="""
import React from 'react';
import { Outlet } from 'react-router-dom';
import { Navigation, Footer } from '../components/default';
{/* import { useSelector } from 'react-redux'; */}
@@Imports@@
const StaticRoute = () => {
  {/* 
  const { isOrderStatus, requestStatus } = useSelector((store) => ({
    isOrderStatus: store?.app?.orderStatus,
    requestStatus: store?.app?.requestStatus
  })); */}

  return (
    <>
      <Navigation />
        {/* 
		{isOrderStatus?.message && (  */}
          <nav className='fixed z-20 w-full top-0 bg-white border-gray-200'>
            {/* <Alert
              status={isOrderStatus.status}
              mssg={isOrderStatus.message}
              type={isOrderStatus.type}
            /> */}
          </nav>
		{/* )} */}
        {/*
		{requestStatus?.message && ( */}
          <nav className='fixed z-20 w-full top-0 bg-white border-gray-200'>
            {/* <Alert
              status={requestStatus.status}
              mssg={requestStatus.message}
              type={requestStatus.type}
            /> */}
          </nav>
		{/* )} */}
        <Outlet />
      <Footer />
    </>
  )
};

export default StaticRoute;
 """
 routers["routers_staticRoute"] = routers_staticRoute

 routers_staticRoute_2 ="""
import React from 'react';
import { Outlet } from 'react-router-dom';

import { Navigation, Footer } from '../components/default';
@@Imports@@

const StaticRoute = () => {

  return (
    <>
      <Navigation />
        <Outlet />
      <Footer />
    </>
  )
};

export default StaticRoute;
 """
 routers["routers_staticRoute_2"] = routers_staticRoute_2


 # Add Vendor route
 routers_vendorRoute ="""
/* eslint-disable react/forbid-prop-types */
/* eslint-disable react/jsx-props-no-spreading */
import React from 'react';
import {  connect } from 'react-redux';
import { useLocation, Navigate } from 'react-router-dom';

import PropType from 'prop-types';

import { 
	ADMIN_DASHBOARD, SIGNIN 
} from '../constants/routes';
import * as CONSTANT from '../constants/constants'
import { Sidebar, Header } from '../components/default/Vendor';
import { Footer, Navigation } from '../components/default';
import './styles/admin_route.css'

/**
 * Authentication guard for routes
 * 
 * @param {PropTypes.bool} isAuth element/bool
 * @param {PropTypes.string} user_type element/string
 * @param {PropTypes.func} component element/func
 * 
 */

const VendorRoute = ({ 
	isAuth, user_type, is_active,
	component: Component
 }) => {
	let location = useLocation();
	let _from = location.state?.from?.pathname || "/";
	if (isAuth && is_active && user_type === CONSTANT.VENDOR_ROLE) {
		return (
			<>
				<Sidebar />
				<main className="main-wrap bg-gray-100 h-screen overflow-y-auto">
					<Header />
					<Component />
				</main>
			</>
		);
	}
	if (isAuth && !is_active && user_type === CONSTANT.VENDOR_ROLE) {
		return (
			<>
				<Navigation />
					<Component />
				<Footer />
			</>
		);
	}
	if (isAuth && user_type === CONSTANT.ADMIN_ROLE) {
		return <Navigate to={ADMIN_DASHBOARD} replace state={{ location }} />;
	}

	return (
		<Navigate 
			to={SIGNIN} 
			replace 
			state={{from: _from }} />
	);
}

VendorRoute.defaultProps = {
  isAuth: false,
  user_type: CONSTANT.USER_ROLE,
  is_active: false
};

VendorRoute.propTypes = {
  isAuth: PropType.bool,
  user_type: PropType.string,
  is_active: PropType.bool,
  component: PropType.func.isRequired
};

const mapStateToProps = ({ auth }) => ({
  isAuth: !!auth,
  user_type: auth?.user_type || '',
  is_active: auth?.is_active || false
});

export default connect(mapStateToProps)(VendorRoute);
 """
 routers["routers_vendorRoute"] = routers_vendorRoute

