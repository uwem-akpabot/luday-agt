class Constants:

 constants = {}

 constants_main ="""
export const GET_PRODUCTS = 'GET_PRODUCTS';
export const GET_CATEGORY_PRODUCTS = 'GET_CATEGORY_PRODUCTS';
export const SEARCH_PRODUCT = 'SEARCH_PRODUCT';
export const SEARCH_PRODUCT_SUCCESS = 'SEARCH_PRODUCT_SUCCESS';
export const GET_PRODUCTS_SUCCESS = 'GET_PRODUCTS_SUCCESS';
export const ADD_PRODUCT = 'ADD_PRODUCT';
export const ADD_PRODUCT_SUCCESS = 'ADD_PRODUCT_SUCCESS';
export const REMOVE_PRODUCT = 'REMOVE_PRODUCT';
export const REMOVE_PRODUCT_SUCCESS = 'REMOVE_PRODUCT_SUCCESS';
export const EDIT_PRODUCT = 'EDIT_PRODUCT';
export const EDIT_PRODUCT_SUCCESS = 'EDIT_PRODUCT_SUCCESS';
export const CANCEL_GET_PRODUCTS = 'CANCEL_GET_PRODUCTS';
export const CLEAR_SEARCH_STATE = 'CLEAR_SEARCH_STATE';
export const SET_LAST_REF_KEY = 'SET_LAST_REF_KEY';
export const EDIT_VENDOR = 'EDIT_VENDOR';

export const SET_CART_ITEMS = 'SET_CART_ITEMS';
export const ADD_TO_CART = 'ADD_TO_CART';
export const REMOVE_FROM_CART = 'REMOVE_FROM_CART';
export const CLEAR_CART = 'CLEAR_CART';
export const ADD_QTY_ITEM = 'ADD_QTY_ITEM';
export const MINUS_QTY_ITEM = 'MINUS_QTY_ITEM';

export const SET_CHECKOUT_BILLING_DETAILS = 'SET_CHECKOUT_BILLING_DETAILS';
export const ADD_ORDER = 'ADD_ORDER';
export const UPDATE_ORDER = 'UPDATE_ORDER';
export const UPDATE_ORDER_TRANSACTION = 'UPDATE_ORDER_TRANSACTION';
export const SET_CHECKOUT_PAYMENT_DETAILS = 'SET_CHECKOUT_PAYMENT_DETAILS';
export const RESET_CHECKOUT = 'RESET_CHECKOUT';

export const SIGNIN = 'SIGNIN';
export const SIGNIN_SUCCESS = 'SIGNIN_SUCCESS';
export const SIGNUP = 'SIGNUP';
export const SIGNUP_VENDOR = 'SIGNUP_VENDOR';
export const SIGNUP_VENDOR_DETAILS = 'SIGNUP_VENDOR_DETAILS';
export const SIGNUP_SUCCESS = 'SIGNUP_SUCCESS';
export const SIGNOUT = 'SIGNOUT';
export const SIGNOUT_SUCCESS = 'SIGNOUT_SUCCESS';
export const SET_AUTH_STATUS = 'SET_AUTH_STATUS';
export const SIGNIN_WITH_GOOGLE = 'SIGNIN_WITH_GOOGLE';
export const SIGNIN_WITH_FACEBOOK = 'SIGNIN_WITH_FACEBOOK';
export const ON_AUTHSTATE_CHANGED = 'ON_AUTHSTATE_CHANGED';
export const SET_AUTH_PERSISTENCE = 'SET_AUTH_PERSISTENCE';
export const ON_AUTHSTATE_SUCCESS = 'ON_AUTHSTATE_SUCCESS';
export const ON_AUTHSTATE_FAIL = 'ON_AUTHSTATE_FAIL';
export const RESET_PASSWORD = 'RESET_PASSWORD';
export const FORGOT_PASSWORD = 'FORGOT_PASSWORD';

export const UPDATE_EMAIL = 'UPDATE_EMAIL';
export const SET_PROFILE = 'SET_PROFILE';
export const UPDATE_PROFILE = 'UPDATE_PROFILE';
export const UPDATE_PROFILE_SUCCESS = 'UPDATE_PROFILE_SUCCESS';
export const UPDATE_PROFILE_ADDRESS_SUCCESS = 'UPDATE_PROFILE_ADDRESS_SUCCESS';
export const CLEAR_PROFILE = 'CLEAR_PROFILE';
export const SET_GUEST = 'SET_GUEST';

export const REGISTER_USER = 'REGISTER_USER';
export const GET_USER = 'GET_USER';
export const ADD_USER = 'ADD_USER';
export const DELETE_USER = 'DELETE_USER';
export const EDIT_USER = 'EDIT_USER';

export const LOADING = 'LOADING';
export const ORDER_LOADING = 'ORDER_LOADING';
export const IS_AUTHENTICATING = 'IS_AUTHENTICATING';
export const SET_REQUEST_STATUS = 'SET_REQUEST_STATUS';
export const SET_ORDER_STATUS = 'SET_ORDER_STATUS';

// Refernce: api/products/app/constants.py
export const ORDER_NEW = 'New';
export const ORDER_PAYMENT_PENDING = 'Pending';
export const ORDER_PAYMENT_FAILED = 'Failed';
export const ORDER_SUCCESS = 'Successful';

// Refernce: api/products/app/constants.py
export const DELIVERY_PENDING = 'Pending';
export const DELIVERY_PROCESSING = 'Shipped';
export const DELIVERY_COMPLETE = 'Delivered';

/* Production image store URL */
export const IMAGE_STORE = 'http://bestdealvps.luday.se';
/* Test image store URL should be the windows location of the folder */
// export const IMAGE_STORE = 'C:/react/bestdealnaija';

// Refernce: api/user/app/constants.py
export const USER_ROLE = 'user';
export const VENDOR_ROLE = 'vendor';
export const ADMIN_ROLE = 'super-admin';
export const SUB_ADMIN_ROLE = 'sub-admin';
 """
 constants["constants_main"] = constants_main


# Add Constant Index
 constants_index ="""
export * as constant from './constants';
export * as route from './routes';
 """
 constants["constants_index"] = constants_index


 # Add Constant routes
 constants_routes ="""
/* API routes */
export const CONTACT_API = process.env.REACT_APP_CONTACT_API; // eslint-disable-line
export const USER_API = process.env.REACT_APP_USER_API; // eslint-disable-line
export const PRODUCTS_API = process.env.REACT_APP_PRODUCTS_API; // eslint-disable-line
export const BLOGS_API = process.env.REACT_APP_BLOGS_API; // eslint-disable-line

/* public routes */
export const HOME = '/';
export const FIND_YOUR_DEAL = '/find-your-deal';
export const ABOUT_BEST_DEAL_NAIJA = '/about-bestdealnaija';
export const BLOG = '/blog';
export const BLOG_DETAILS = '/blog-details';
export const CONTACT = '/contact';
export const CART = '/cart';
export const VENDORS = '/vendors';
export const VENDORDETAILS = '/vendor-details';
export const PRODUCTS = '/products';
export const SEARCH = '/search/:searchQuery';
export const VENDOR_PRODUCTS_VIEW = '/vendor-products';
export const CATEGORY_PRODUCTS = '/category';
export const PRODUCT_DETAILS = '/product-details';
export const CHECKOUT = '/checkout';
export const DELIVERY = '/delivery';
export const PAYMENT = '/payment';
export const TEST = '/test';
export const BEST_DEAL_TRADE_FAIR = '/best-deal-trade-fair';
export const USERS_GUIDE = '/users-guide';
export const OWNERS_GUIDE = '/owners-guide';

/* Vendor routes */
export const VENDOR_DASHBOARD = '/vendor';
export const ADD_PRODUCT = '/vendor/add';
export const EDIT_PRODUCT = '/vendor/edit';
export const VENDOR_ADD_PRODUCTS = '/vendor/addproducts';
export const VENDOR_EDIT_PRODUCTS = '/vendor/editproducts';
export const VENDOR_PRODUCTS = '/vendor/products';
export const VENDOR_ORDERS = '/vendor/order';

/* Auth routes */
export const SIGNIN = '/signin';
export const SIGNOUT = '/logout';
export const SIGNUP = '/signup';
export const SIGNUP_VENDOR = '/vendor/signup';
export const SIGNUP_VENDOR_DETAILS = '/vendor/signup/details';
export const SIGNUP_VENDOR_COMPLETE = '/vendor/signup/complete';
export const FORGOT_PASSWORD = '/forgot_password';
export const RESET_PASSWORD = '/reset_password/:token';

export const CHECKOUT_STEP_1 = '/checkout/step1';
export const CHECKOUT_STEP_2 = '/checkout/step2';
export const CHECKOUT_STEP_3 = '/checkout/step3';
export const VIEW_PRODUCT = '/product/:id';

/* Admin routes */
export const ADMIN_DASHBOARD = '/admin/home';
export const ADMIN_CATEGORIES = '/admin/categories';
export const ADMIN_EDIT_CATEGORIES = '/admin/edit-categories';
export const ADMIN_PRODUCTS = '/admin/products';
export const ADMIN_VERIFY_PRODUCTS = '/admin/verifyproducts';
export const ADMIN_VIEW_PRODUCT = '/admin/viewproduct';
export const ADMIN_EDIT_PRODUCTS = '/admin/editproducts';
export const ADMIN_ORDERS = '/admin/orders';
export const VIEW_ORDERS = '/admin/vieworders';
export const ADMIN_ADD_VENDORS = '/admin/addvendors';
export const ADMIN_EDIT_VENDORS = '/admin/editvendors';
export const ADMIN_VIEW_VENDORS = '/admin/viewvendors';
export const ADMIN_VERIFY_VENDORS = '/admin/verifyvendors';
export const ADMIN_VENDORS = '/admin/vendors';
export const ADMIN_BLOGS = '/admin/blogs';
export const ADMIN_ADD_BLOGS = '/admin/addblogs';
export const ADMIN_EDIT_BLOGS = '/admin/editblogs';
export const ADMIN_USERS = '/admin/users';
export const ADMIN_CREATE_ADMIN = '/admin/create-admin';
export const ADMIN_MANAGE_ADMINS = '/admin/manage-admins';
export const ADMIN_EDIT_ADMINS = '/admin/edit-admins';

/* protected user routes */
export const PROFILE = '/profile';
export const CHANGEPASSWORD = '/change-password';
export const ORDER_HISTORY = '/order-history';
export const ORDER_DETAILS = '/order-details';
export const ORDER_CALLBACK = '/order/callback';
export const CASH_ORDER_CALLBACK = '/order/cash-callback';
export const VIEW_ORDER = '/order/:id';
 """
 constants["constants_routes"] = constants_routes


# ludayab
 constants_routes_2 ="""
/* public routes */
export const HOME = '/';
export const ABOUT = '/about';
export const BLOG = '/blog';
export const BLOG_DETAILS = '/blog-details';
export const SERVICES = '/services';
export const SERVICE_DETAILS = '/service-details';
export const CONTACT = '/contact';
export const QUOTE = '/quote';
export const PORTFOLIO = '/portfolio';
 """
 constants["constants_routes_2"] = constants_routes_2
