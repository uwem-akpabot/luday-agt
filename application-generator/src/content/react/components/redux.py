class Redux:

 redux = {}
 
 # Add redux authAction
 redux_actions_authActions ="""
import * as type from '../../constants/constants';

export const signIn = (email, password) => ({
  type: type.SIGNIN,
  payload: {
    email,
    password
  }
});

export const signInWithGoogle = () => ({
  type: type.SIGNIN_WITH_GOOGLE
});

export const signInWithFacebook = () => ({
  type: type.SIGNIN_WITH_FACEBOOK
});

export const signUp = (user) => ({
  type: type.SIGNUP,
  payload: user
});

export const signUpVendor = (vendor) => ({
  type: type.SIGNUP_VENDOR,
  payload: vendor
});

export const SignUpVendorDetails = (vendor) => ({
  type: type.SIGNUP_VENDOR_DETAILS,
  payload: vendor
});

export const signInSuccess = (auth) => ({
  type: type.SIGNIN_SUCCESS,
  payload: auth
});

export const setAuthPersistence = () => ({
  type: type.SET_AUTH_PERSISTENCE
});

export const signOut = () => ({
  type: type.SIGNOUT
});

export const signOutSuccess = () => ({
  type: type.SIGNOUT_SUCCESS
});

export const onAuthStateChanged = () => ({
  type: type.ON_AUTHSTATE_CHANGED
});

export const onAuthStateSuccess = (user) => ({
  type: type.ON_AUTHSTATE_SUCCESS,
  payload: user
});

export const onAuthStateFail = (error) => ({
  type: type.ON_AUTHSTATE_FAIL,
  payload: error
});

export const resetPassword = (payload) => ({
  type: type.RESET_PASSWORD,
  payload: payload
});

export const forgotPassword = (email) => ({
  type: type.FORGOT_PASSWORD,
  payload: {
    email
  }
});
 """
 redux["redux_actions_authActions"] = redux_actions_authActions


# Add Redux cartActions
 redux_actions_cartActions ="""
import {
  ADD_QTY_ITEM, ADD_TO_CART,
  CLEAR_CART,
  MINUS_QTY_ITEM, REMOVE_FROM_CART,
  SET_CART_ITEMS
} from '../../constants/constants';

export const setCartItems = (items = []) => ({
  type: SET_CART_ITEMS,
  payload: items
});

export const addToCart = (product) => ({
  type: ADD_TO_CART,
  payload: product
});

export const removeFromCart = (id) => ({
  type: REMOVE_FROM_CART,
  payload: id
});

export const clearCart = () => ({
  type: CLEAR_CART
});

export const addQtyItem = (id) => ({
  type: ADD_QTY_ITEM,
  payload: id
});

export const minusQtyItem = (id) => ({
  type: MINUS_QTY_ITEM,
  payload: id
});
 """
 redux["redux_actions_cartActions"] = redux_actions_cartActions


 # Add Redux checkoutActions
 redux_actions_checkoutActions ="""
import {
  RESET_CHECKOUT, 
  SET_CHECKOUT_PAYMENT_DETAILS, 
  SET_CHECKOUT_BILLING_DETAILS,
  ADD_ORDER, UPDATE_ORDER,
  UPDATE_ORDER_TRANSACTION
} from '../../constants/constants';

export const setBillingDetails = (details) => ({
  type: SET_CHECKOUT_BILLING_DETAILS,
  payload: details
});

export const addOrder = (details) => ({
  type: ADD_ORDER,
  payload: {
    user: details.user,
    guest: details.guest,
    type: details.type
  }
});

export const updateOrder = (details) => ({
  type: UPDATE_ORDER,
  payload: {
    order: details.order,
    type: details.type
  }
});

export const updateOrderTransaction = (payload) => ({
  type: UPDATE_ORDER_TRANSACTION,
  payload: payload
});

export const setPaymentDetails = (details) => ({
  type: SET_CHECKOUT_PAYMENT_DETAILS,
  payload: details
});

export const resetCheckout = () => ({
  type: RESET_CHECKOUT
});
 """
 redux["redux_actions_checkoutActions"] = redux_actions_checkoutActions

 # Add Redux Actions index
 redux_actions_index ="""
export * as authActions from './authActions';
export * as cartActions from './cartActions';
export * as checkoutActions from './checkoutActions';
export * as miscActions from './miscActions';
export * as productActions from './productActions';
export * as profileActions from './profileActions';
export * as userActions from './userActions';
 """
 redux["redux_actions_index"] = redux_actions_index


 # Add Redux miscActions
 redux_actions_miscActions ="""
import {
  IS_AUTHENTICATING, LOADING, SET_AUTH_STATUS, 
  SET_REQUEST_STATUS, SET_ORDER_STATUS, ORDER_LOADING
} from '../../constants/constants';

export const setLoading = (bool = true) => ({
  type: LOADING,
  payload: bool
});

export const setOrderLoading = (bool = true) => ({
  type: ORDER_LOADING,
  payload: bool
});

export const setAuthenticating = (bool = true) => ({
  type: IS_AUTHENTICATING,
  payload: bool
});

export const setRequestStatus = (status) => ({
  type: SET_REQUEST_STATUS,
  payload: status
});


export const setAuthStatus = (status = null) => ({
  type: SET_AUTH_STATUS,
  payload: status
});

export const setOrderStatus = (status = null) => ({
  type: SET_ORDER_STATUS,
  payload: status
});
 """
 redux["redux_actions_miscActions"] = redux_actions_miscActions


 # Add Redux productActions
 redux_actions_productActions ="""
import {
  ADD_PRODUCT,
  ADD_PRODUCT_SUCCESS,
  CANCEL_GET_PRODUCTS,
  CLEAR_SEARCH_STATE,
  EDIT_PRODUCT,
  EDIT_PRODUCT_SUCCESS,
  GET_PRODUCTS,
  GET_CATEGORY_PRODUCTS,
  GET_PRODUCTS_SUCCESS,
  REMOVE_PRODUCT,
  REMOVE_PRODUCT_SUCCESS,
  SEARCH_PRODUCT,
  SEARCH_PRODUCT_SUCCESS
} from '../../constants/constants';

export const getProducts = (lastRef) => ({
  type: GET_PRODUCTS,
  payload: lastRef
});

export const getCategoryProducts = (categoryId) => ({
  type: GET_CATEGORY_PRODUCTS,
  payload: categoryId
});

export const getProductsSuccess = (products) => ({
  type: GET_PRODUCTS_SUCCESS,
  payload: products
});

export const cancelGetProducts = () => ({
  type: CANCEL_GET_PRODUCTS
});

export const addProduct = (product) => ({
  type: ADD_PRODUCT,
  payload: product
});

export const searchProduct = (searchKey, lastRefKey=null) => ({
  type: SEARCH_PRODUCT,
  payload: {
    searchKey,
    lastRefKey
  }
});

export const searchProductSuccess = (products) => ({
  type: SEARCH_PRODUCT_SUCCESS,
  payload: products
});

export const clearSearchState = () => ({
  type: CLEAR_SEARCH_STATE
});

export const addProductSuccess = (product) => ({
  type: ADD_PRODUCT_SUCCESS,
  payload: product
});

export const removeProduct = (id) => ({
  type: REMOVE_PRODUCT,
  payload: id
});

export const removeProductSuccess = (id) => ({
  type: REMOVE_PRODUCT_SUCCESS,
  payload: id
});

export const editProduct = (id, updates) => ({
  type: EDIT_PRODUCT,
  payload: {
    id,
    updates
  }
});

export const editProductSuccess = (updates) => ({
  type: EDIT_PRODUCT_SUCCESS,
  payload: updates
});
 """
 redux["redux_actions_productActions"] = redux_actions_productActions


 # Add Redux profileActions
 redux_actions_profileActions ="""
import {
  CLEAR_PROFILE,
  SET_PROFILE,
  UPDATE_EMAIL,
  UPDATE_PROFILE,
  UPDATE_PROFILE_SUCCESS,
  UPDATE_PROFILE_ADDRESS_SUCCESS
} from '../../constants/constants';

export const clearProfile = () => ({
  type: CLEAR_PROFILE
});

export const setProfile = (user, token) => ({
  type: SET_PROFILE,
  payload: user,
  token: token
});

export const updateEmail = (password, newEmail) => ({
  type: UPDATE_EMAIL,
  payload: {
    password,
    newEmail
  }
});

export const updateProfile = (newProfile) => ({
  type: UPDATE_PROFILE,
  payload: {
    updates: newProfile.updates,
    address: newProfile.address,
    credentials: newProfile.credentials
  }
});

export const updateProfileSuccess = (updates) => ({
  type: UPDATE_PROFILE_SUCCESS,
  payload: updates
});

export const updateProfileAddressSuccess = (profile, address) => ({
  type: UPDATE_PROFILE_ADDRESS_SUCCESS,
  payload: {
    user: profile,
    address: address
  }
});
 """
 redux["redux_actions_profileActions"] = redux_actions_profileActions


 # Add Redux userActions
 redux_actions_userActions ="""
import {
  ADD_USER,
  DELETE_USER, EDIT_USER, GET_USER, REGISTER_USER
} from '../../constants/constants';

// insert in profile array
export const registerUser = (user) => ({
  type: REGISTER_USER,
  payload: user
});

export const getUser = (uid) => ({
  type: GET_USER,
  payload: uid
});

// different from registerUser -- only inserted in admins' users array not in profile array
export const addUser = (user) => ({
  type: ADD_USER,
  payload: user
});

export const editUser = (updates) => ({
  type: EDIT_USER,
  payload: updates
});

export const deleteUser = (id) => ({
  type: DELETE_USER,
  payload: id
});
 """
 redux["redux_actions_userActions"] = redux_actions_userActions


 """
Redux Reducer
"""
# Add Redux authReducer
 redux_reducers_authReducer ="""
import { SIGNIN_SUCCESS, SIGNOUT_SUCCESS } from '../../constants/constants';

const initState = null;

export default (state = initState, action) => {
  switch (action.type) {
    case SIGNIN_SUCCESS:
      return {
        id: action.payload.id,
        user_type: action.payload.user_type,
        is_active: action.payload.is_active,
        provider: action.payload.provider
      };
    case SIGNOUT_SUCCESS:
      return null;
    default:
      return state;
  }
};
 """
 redux["redux_reducers_authReducer"] = redux_reducers_authReducer


 # Add Redux cartReducer
 redux_reducers_cartReducer ="""
import {
  ADD_QTY_ITEM, ADD_TO_CART,
  CLEAR_CART,
  MINUS_QTY_ITEM, REMOVE_FROM_CART,
  SET_CART_ITEMS
} from '../../constants/constants';

export default (state = [], action) => {
  switch (action.type) {
    case SET_CART_ITEMS:
      return action.payload;
    case ADD_TO_CART:
      return state.some((product) => product.id === action.payload.id)
        ? state
        : [action.payload, ...state];
    case REMOVE_FROM_CART:
      return state.filter((product) => product.id !== action.payload);
    case CLEAR_CART:
      return [];
    case ADD_QTY_ITEM:
      return state.map((product) => {
        if (product.id === action.payload) {
          return {
            ...product,
            cart_quantity: product.cart_quantity + 1
          };
        }
        return product;
      });
    case MINUS_QTY_ITEM:
      return state.map((product) => {
        if (product.id === action.payload) {
          return {
            ...product,
            cart_quantity: product.cart_quantity - 1
          };
        }
        return product;
      });
    default:
      return state;
  }
};
 """
 redux["redux_reducers_cartReducer"] = redux_reducers_cartReducer


 # Add Redux checkoutReducer
 redux_reducers_checkoutReducer ="""
import {
  RESET_CHECKOUT, 
  SET_CHECKOUT_PAYMENT_DETAILS, 
  SET_CHECKOUT_BILLING_DETAILS
} from '../../constants/constants';

const defaultState = {
  billing: {},
  payment: {
    type: 'paystack',
    name: ''
  }
};

export default (state = defaultState, action) => {
  switch (action.type) {
    case SET_CHECKOUT_BILLING_DETAILS:
      return {
        ...state,
        billing: action.payload
      };
    case SET_CHECKOUT_PAYMENT_DETAILS:
      return {
        ...state,
        payment: action.payload
      };
    case RESET_CHECKOUT:
      return defaultState;
    default:
      return state;
  }
};
 """
 redux["redux_reducers_checkoutReducer"] = redux_reducers_checkoutReducer


 # Add Redux index
 redux_reducers_index ="""
import authReducer from './authReducer';
import cartReducer from './cartReducer';
import checkoutReducer from './checkoutReducer';
import miscReducer from './miscReducer';
import productReducer from './productReducer';
import profileReducer from './profileReducer';
import userReducer from './userReducer';

const rootReducer = {
  products: productReducer,
  cart: cartReducer,
  auth: authReducer,
  profile: profileReducer,
  users: userReducer,
  checkout: checkoutReducer,
  app: miscReducer
};

export default rootReducer;
 """
 redux["redux_reducers_index"] = redux_reducers_index


 # Add Redux miscReducer
 redux_reducers_miscReducer ="""
import {
  IS_AUTHENTICATING, LOADING,
  SET_AUTH_STATUS,
  SET_REQUEST_STATUS,
  SET_GUEST, SET_ORDER_STATUS, ORDER_LOADING
} from '../../constants/constants';

const initState = {
  loading: false,
  orderLoading: false,
  isAuthenticating: false,
  authStatus: null,
  orderStatus: null,
  requestStatus: null,
  guest: {}
};

export default (state = initState, action) => {
  switch (action.type) {
    case LOADING:
      return {
        ...state,
        loading: action.payload
      };
    case ORDER_LOADING:
        return {
          ...state,
          orderLoading: action.payload
        };
    case IS_AUTHENTICATING:
      return {
        ...state,
        isAuthenticating: action.payload
      };
    case SET_REQUEST_STATUS:
      return {
        ...state,
        requestStatus: action.payload
      };
    case SET_AUTH_STATUS:
      return {
        ...state,
        authStatus: action.payload
      };
    case SET_ORDER_STATUS:
        return {
          ...state,
          orderStatus: action.payload
        };
    case SET_GUEST:
      return {
        ...state,
        guest: action.payload
      };
    default:
      return state;
  }
};
 """
 redux["redux_reducers_miscReducer"] = redux_reducers_miscReducer


 # Add Redux productReducer
 redux_reducers_productReducer ="""
import {
  ADD_PRODUCT_SUCCESS,
  CLEAR_SEARCH_STATE, EDIT_PRODUCT_SUCCESS,
  GET_PRODUCTS_SUCCESS, REMOVE_PRODUCT_SUCCESS,
  SEARCH_PRODUCT_SUCCESS
} from '../../constants/constants';

const initState = {
  lastRefKey: null,
  nextPage: null,
  prevPage: null,
  items: []
};

export default (state = {
  lastRefKey: null,
  nextPage: null,
  prevPage: null,
  items: [],
  searchedProducts: initState
}, action) => {
  switch (action.type) {
    case GET_PRODUCTS_SUCCESS:
      return {
        ...state,
        lastRefKey: action.payload.lastKey,
        nextPage: action.payload.nextPage,
        prevPage: action.payload.prevPage,
        items: [...state.items, ...action.payload.products]
      };
    case ADD_PRODUCT_SUCCESS:
      return {
        ...state,
        items: [...state.items, action.payload.products]
      };
    case SEARCH_PRODUCT_SUCCESS:
      return {
        ...state,
        searchedProducts: {
          lastRefKey: action.payload.lastKey,
          nextPage: action.payload.nextPage,
          prevPage: action.payload.prevPage,
          items: [...state.searchedProducts.items, ...action.payload.products]
        }
      };
    case CLEAR_SEARCH_STATE:
      return {
        ...state,
        searchedProducts: initState
      };
    case REMOVE_PRODUCT_SUCCESS:
      return {
        ...state,
        items: state.items.filter((product) => product.id !== action.payload)
      };
    case EDIT_PRODUCT_SUCCESS:
      return {
        ...state,
        items: state.items.map((product) => {
          if (product.id === action.payload.id) {
            return {
              ...product,
              ...action.payload.updates
            };
          }
          return product;
        })
      };
    default:
      return state;
  }
};
 """
 redux["redux_reducers_productReducer"] = redux_reducers_productReducer


 # Add Redux profileReducer
 redux_reducers_profileReducer ="""
import { 
  CLEAR_PROFILE, SET_PROFILE, 
  UPDATE_PROFILE_SUCCESS,UPDATE_PROFILE_ADDRESS_SUCCESS
} from '../../constants/constants';

export default (state = {}, action) => {
  switch (action.type) {
    case SET_PROFILE:
      return {
        ...state,
        ...action.token,
        ...action.payload
      };
    case UPDATE_PROFILE_SUCCESS:
      return {
        ...state,
        ...action.payload
      };
    case UPDATE_PROFILE_ADDRESS_SUCCESS:
      return {
        ...state,
        ...action.payload.user,
        ...action.payload.address
      };
    case CLEAR_PROFILE:
      return {};
    default:
      return state;
  }
};
 """
 redux["redux_reducers_profileReducer"] = redux_reducers_profileReducer


 # Add Redux userReducer
 redux_reducers_userReducer ="""
import { ADD_USER, DELETE_USER, EDIT_USER } from '../../constants/constants';

export default (state = {}, action) => {
  switch (action.type) {
    case ADD_USER:
      return [...state, action.payload];
    case EDIT_USER:
      return state.map((user) => {
        if (user.id === action.payload.id) {
          return {
            ...user,
            ...action.payload
          };
        }
        return user;
      });
    case DELETE_USER:
      return state.filter((user) => user.id !== action.payload);
    default:
      return state;
  }
};
 """
 redux["redux_reducers_userReducer"] = redux_reducers_userReducer


 # Add Redux authSaga
 redux_sagas_authSaga ="""
import {
  ON_AUTHSTATE_FAIL,
  SET_AUTH_PERSISTENCE,
  ON_AUTHSTATE_SUCCESS,
  SIGNIN, SIGNOUT, SIGNUP, 
  SIGNUP_VENDOR, SIGNUP_VENDOR_DETAILS,
  VENDOR_ROLE, USER_ROLE, FORGOT_PASSWORD, RESET_PASSWORD
} from '../../constants/constants';
import { USER_API } from '../../services';
import { call, put } from 'redux-saga/effects';
import { signInSuccess, signOutSuccess } from '../actions/authActions';
import { clearCart } from '../actions/cartActions';
import { resetCheckout } from '../actions/checkoutActions';
import { setAuthenticating, setAuthStatus, setLoading} from '../actions/miscActions';
import { clearProfile, setProfile } from '../actions/profileActions';

function* handleError(e) {
  const obj = { success: false, type: 'auth', isError: true };
  yield put(setAuthenticating(false));

  if (e.json?.email) {
    yield put(setAuthStatus({ ...obj, status: 'error', message: 'Email is already in use. Please use another email' }));
  }
}

function* initRequest() {
  yield put(setAuthenticating());
  yield put(setAuthStatus({}));
}

function* authSaga({ type, payload }) {
  switch (type) {
    case SIGNIN:
      try {
        yield initRequest();

        const auth = {
          email: payload.email,
          password: payload.password
        };
        const auth_user = yield call(USER_API.signIn, auth);
        const user_snapshot = yield call(USER_API.getAuthenticatedUser, {token: auth_user.access_token});
        if (user_snapshot) { 
          const user = user_snapshot;
          localStorage.setItem('user', JSON.stringify(user));
          localStorage.setItem('auth_tokens', JSON.stringify(auth_user));

          yield put(setProfile(user, auth_user));

          yield put(signInSuccess({
            id: user_snapshot.id,
            user_type: user_snapshot.user_type,
            is_active: user_snapshot.is_active,
            provider: user_snapshot.provider
          }));
  
          yield put(setAuthStatus({
            success: true,
            type: 'auth',
            isError: false,
            message: 'Successfully signed in. Redirecting...'
          }));
        }

      } catch (e) {
        console.log(e)
        yield put(setAuthenticating(false));
        yield put(setAuthStatus({ 
          success: false, 
          type: 'auth', 
          isError: true, 
          status: 'error', 
          message: 'Incorrect email or password' 
        }));
      }
      break;
      
    case SIGNUP:
      try {
        yield initRequest();
        const user = {
            first_name: payload.first_name,
            last_name: payload.last_name,
            email: payload.email,
            password: payload.password,
            gender: payload.gender,
            user_type: USER_ROLE,
            is_active: payload.is_active
          };
        
        const auth = {
          email: payload.email,
          password: payload.password
        };
        const ref_user = yield call(USER_API.signUp, user);
        const auth_token = yield call(USER_API.signIn, auth);
        localStorage.setItem('user', JSON.stringify(ref_user));
        localStorage.setItem('auth_tokens', JSON.stringify(auth_token));

        yield put(setProfile(ref_user, auth_token));

        yield put(signInSuccess({
          id: ref_user.id,
          user_type: user.user_type,
          is_active: user.is_active,          
          provider: user.provider
        }));

        yield put(setAuthStatus({
          success: true,
          type: 'auth',
          isError: false,
          message: 'Successfully signed up. Redirecting...'
        }));

        yield put(setAuthenticating(false));
      } catch (e) {
        yield handleError(e);
      }
    break;

    case SIGNUP_VENDOR:
      try {
        yield initRequest();
        
        const vendor = {
          first_name: payload.first_name,
          last_name: payload.last_name,
          email: payload.email,
          password: payload.password,
          gender: payload.gender,
          user_type: VENDOR_ROLE,
          is_active: payload.is_active
        };
        const auth = {
          email: payload.email,
          password: payload.password
        };
        const ref_vendor = yield call(USER_API.signUp, vendor);
        const auth_token = yield call(USER_API.signIn, auth);
        localStorage.setItem('user', JSON.stringify(ref_vendor));
        localStorage.setItem('auth_tokens', JSON.stringify(auth_token));

        yield put(setProfile(ref_vendor, auth_token));

        yield put(signInSuccess({
          id: ref_vendor.id,
          user_type: vendor.user_type,
          is_active: vendor.is_active,
          provider: vendor.provider
        }));

        yield put(setAuthStatus({
          success: true,
          type: 'auth',
          isError: false,
          message: 'Successfully signed up. Redirecting...'
        }));

        yield put(setAuthenticating(false));
      } catch (e) {
        yield handleError(e);
      }
    break;
    
    case SIGNUP_VENDOR_DETAILS: {
      try {
        yield initRequest();

        let auth_tokens = JSON.parse(localStorage.getItem('auth_tokens'));
        yield call(USER_API.signUpVendorDetails, payload, {token: auth_tokens.access_token});

        yield put(setAuthStatus({
          success: true,
          type: 'auth',
          isError: false,
          message: 'Successfully signed details.'
        }));
        yield put(setAuthenticating(false));
      } catch (e) {
        console.log(e)
        yield handleError(e);
      }
      break;
    }

    case SIGNOUT: {
      try {
        yield initRequest();

        localStorage.removeItem('user');
        let auth_tokens = JSON.parse(localStorage.getItem('auth_tokens'));
        localStorage.removeItem('auth_tokens');

        yield put(clearCart());
        yield put(clearProfile());
        yield put(resetCheckout());
        yield put(signOutSuccess());
        yield put(setAuthenticating(false));
        yield call(USER_API.signOut, {token: auth_tokens.access_token});
      } catch (e) {
        console.log(e);
      }
      break;
    }

    case FORGOT_PASSWORD: {
      try {
        yield initRequest();

        yield call(USER_API.forgotUserPassword, payload);
        yield put(setAuthStatus({
          success: true,
          type: 'reset',
          status: 'success',
          message: 'Password reset email has been sent to your provided email.'
        }));
        yield put(setAuthenticating(false));
      } catch (e) {
        console.log(e);
      }
      break;
    }

    case RESET_PASSWORD: {
      try {
        yield initRequest();

        const data = {
          token: payload.token,
          new_password: payload.new_password
        };
        yield call(USER_API.resetUserPassword, data);
        yield put(setAuthStatus({
          success: true,
          type: 'reset',
          status: 'success',
          message: 'Password reset was successful.'
        }));
        yield put(setAuthenticating(false));
      } catch (e) {
        console.log(e)
        yield put(setAuthenticating(false));
        yield put(setAuthStatus({ 
          success: false, 
          type: 'auth', 
          isError: true, 
          status: 'error', 
          message: 'Expired or invalid reset token' 
        }));
      }
      break;
    }

    case ON_AUTHSTATE_SUCCESS: {
      let auth_tokens = JSON.parse(localStorage.getItem('auth_tokens'));
      const user_shot = yield call(USER_API.getAuthenticatedUser, {token: auth_tokens.access_token});
      console.log(user_shot)
      if (user_shot) { 
        const user = user_shot;

        yield put(setProfile(user, auth_tokens));
        yield put(signInSuccess({
          id: payload.id,
          user_type: user.user_type,
          is_active: user.is_active,
          provider: user.provider
        }));
      }

      yield put(setAuthStatus({
        success: true,
        type: 'auth',
        isError: false,
        message: 'Successfully signed in. Redirecting...'
      }));
      yield put(setAuthenticating(false));
      break;
    }
  
    case ON_AUTHSTATE_FAIL: {
      localStorage.removeItem('user');
      localStorage.removeItem('auth_tokens');
      yield put(clearProfile());
      yield put(signOutSuccess());
      break;
    }

    case SET_AUTH_PERSISTENCE: {
      yield put(setLoading(true));
      try {
        let auth_tokens = JSON.parse(localStorage.getItem('auth_tokens'));
        let set_auth_persistence = yield call(USER_API.getRefreshToken, auth_tokens);

        if (set_auth_persistence) {
          localStorage.setItem('auth_tokens', JSON.stringify(set_auth_persistence));

          let refresh_auth_tokens = JSON.parse(localStorage.getItem('auth_tokens'));
          const user_shot = yield call(USER_API.getAuthenticatedUser, {token: refresh_auth_tokens?.access_token});
          
          if (user_shot) { 
            const user = user_shot;
            yield put(setProfile(user, refresh_auth_tokens));
          }
          yield put(setLoading(false));
        }        
      } catch (e) {
        yield put(setLoading(false));
        console.log(e);
      }
      break;
    }
    default: {
      throw new Error('Unexpected Action Type.');
    }
  }
}

export default authSaga;
 """
 redux["redux_sagas_authSaga"] = redux_sagas_authSaga


 # Add Redux checkoutSaga
 redux_sagas_checkoutSaga ="""
import { call, put } from 'redux-saga/effects';

import {ADD_ORDER, UPDATE_ORDER } from '../../constants/constants';
import { setBillingDetails } from '../actions/checkoutActions';
import { PRODUCT_API } from '../../services';
import { setOrderLoading, setOrderStatus, setRequestStatus } from '../actions/miscActions';
import { clearCart } from '../actions/cartActions';
import { clearProfile } from '../actions/profileActions';

function* initRequest() {
	yield put(setRequestStatus(null));
	yield put(setOrderLoading(true));
}

function* checkoutSaga({type, payload}) {
	switch (type) {
		case ADD_ORDER:
			try {
				yield initRequest();
				yield put(setOrderStatus({}));
				if (Object.keys(payload.guest).length) {
					const ref_add_order = yield call(PRODUCT_API.addGuestOrder, 
					payload.guest);
					const set_billing_details = yield put(setBillingDetails({...ref_add_order, isDone: true}));
					if (set_billing_details) {
						yield put(setOrderStatus({
							success: true,
							type: 'order',
							isError: false,
							status: 'success',
							message: 'Order added.'
						}));
						yield put(setOrderLoading(false));
					}
				}
				if (Object.keys(payload.user).length) {
					let auth_tokens = JSON.parse(localStorage.getItem('auth_tokens'));
					if (auth_tokens) {
						const ref_add_order = yield call(PRODUCT_API.addOrder, 
							payload.user,
							{token: auth_tokens.access_token}
						);
						const set_billing_details = yield put(setBillingDetails({...ref_add_order, isDone: true}));
						if (set_billing_details) {
							yield put(setOrderStatus({
								success: true,
								type: 'order',
								isError: false,
								status: 'success',
								message: 'Order added.'
							}));
							yield put(setOrderLoading(false));
						}
					}
				}
			} catch (e) {
				if(e.message === "FORBIDDEN") {
					yield put(setOrderStatus({ 
						success: false,
						type: 'order', 
						isError: true, 
						status: 'error', 
						message: 'Some cart items are out of stock!' 
					}));
					yield put(setOrderLoading(false));
				}
				if(e.message === "UNAUTHORIZED") {
					yield put(setOrderStatus({ 
						success: false,
						type: 'order', 
						isError: true, 
						status: 'error', 
						message: 'Unauthorized! Kindly login again...' 
					}));
					yield put(setOrderLoading(false));
				}
				else {
					yield put(setOrderStatus({ 
						success: false,
						type: 'support', 
						isError: true, 
						status: 'error', 
						message: 'Something went wrong.'
					}));
					yield put(setOrderLoading(false));
				}
			}
		break;

		case UPDATE_ORDER:
			try {
				yield initRequest();

				const order = yield call(PRODUCT_API.updateOrderBillingAddressIdByRefId, 
					payload.order);
				yield put(setBillingDetails({...order, isDone: true}));
				
				if (payload.type === 'cash') {
					yield put(setRequestStatus(true));
					yield put(clearCart())
				}
				let auth_tokens = JSON.parse(localStorage.getItem('auth_tokens'));
				// Clear guest user profile to avoid state persistence if the guest signs up.
				if (!auth_tokens) {
					yield put(clearProfile());
				}
				yield put(setOrderLoading(false));
			} catch (e) {
				console.log(e);
				yield put(setOrderLoading(false));
			}
		break;

		default: {
			throw new Error('Unexpected action type.');
		}
	}
}

export default checkoutSaga;
 """
 redux["redux_sagas_checkoutSaga"] = redux_sagas_checkoutSaga


 # Add Redux productSaga
 redux_sagas_productSaga ="""
/* eslint-disable indent */
import {
	call, put, select
  } from 'redux-saga/effects';
import {
	GET_CATEGORY_PRODUCTS,
	REMOVE_PRODUCT, GET_PRODUCTS, SEARCH_PRODUCT
} from '../../constants/constants';
import { PRODUCT_API } from '../../services';
import { getProductsSuccess, removeProductSuccess, searchProductSuccess } from '../actions/productActions';
import { setLoading, setRequestStatus} from '../actions/miscActions';

function* initRequest() {
	yield put(setLoading(true));
	yield put(setRequestStatus(null));
}

function* handleError(e) {
	yield put(setLoading(false));
	yield put(setRequestStatus(e?.message || 'Failed to fetch products'));
	console.log('ERROR: ', e);
}

function* productSaga({type, payload}) {
	switch (type) {
    case GET_CATEGORY_PRODUCTS:
      try {
        yield initRequest();
        const response = yield call(PRODUCT_API.getCategoryProducts, payload);
        if (response.results.length === 0) {
          handleError('No items found.');
        } else {
          yield put(getProductsSuccess({
            products: response.results
          }));
          yield put(setRequestStatus(''));
        }
        yield put(setLoading(false));
      } catch (e) {
        console.log(e);
        yield handleError(e);
      }
	break;
	case GET_PRODUCTS: {
		try {
			yield initRequest();
			const state = yield select();
			const response = yield call(PRODUCT_API.getProducts, payload);

			if (response.results.length === 0) {
				handleError('No items found.');
			} else {
				yield put(getProductsSuccess({
					products: response.results,
					nextPage: response.next_page,
					prevPage: response.prev_page,
					lastKey: response.last_product_id ? response.last_product_id : state.products.lastRefKey
				}));
				yield put(setRequestStatus(''));
			}
			yield put(setLoading(false));
		} catch (e) {
			console.log(e);
			yield handleError(e);
		}
		break;
	}
	case REMOVE_PRODUCT: {
		try {
			yield initRequest();
			yield put(removeProductSuccess(payload));
			yield put(setLoading(false));
		} catch (e) {
			yield handleError(e);
		}
		break;
	}
	case SEARCH_PRODUCT: {
		try {
			yield initRequest();
			const state = yield select();
			const response = yield call(PRODUCT_API.searchProducts, payload.searchKey, payload.lastRefKey);
			if (response) {
				yield put(searchProductSuccess({
					products: response.results,
					nextPage: response.next_page,
					prevPage: response.prev_page,
					lastKey: response.last_product_id ? response.last_product_id : state.products.lastRefKey
				}));
				yield put(setRequestStatus(''));
			}
			yield put(setLoading(false));
		} catch (e) {
			yield handleError(e);
		}
		break;
	}
    default: {
      throw new Error(`Unexpected action type ${type}`);
    }
  }
}

export default productSaga;
 """
 redux["redux_sagas_productSaga"] = redux_sagas_productSaga


 # Add Redux profileSaga
 redux_sagas_profileSaga ="""
import { call, put } from 'redux-saga/effects';

import {UPDATE_PROFILE } from '../../constants/constants';
import { USER_API } from '../../services';
import { 
	updateProfileSuccess,
	updateProfileAddressSuccess
} from '../actions/profileActions';
import { setLoading } from '../actions/miscActions';

function* profileSaga({type, payload}) {
	switch (type) {
		case UPDATE_PROFILE: {
			try {
				const { password, old_password } = payload.credentials;
		
				yield put(setLoading(true));
		
				let auth_tokens = JSON.parse(localStorage.getItem('auth_tokens'));
				if (auth_tokens) {
					if (password && old_password) {
						yield call(USER_API.updateUserDetails, 
							{...payload.updates, password, old_password}, 
							{token: auth_tokens.access_token});
						yield put(updateProfileSuccess(payload.updates));
					} else {
						yield call(USER_API.updateUserDetails, 
							payload.updates, 
							{token: auth_tokens.access_token});
						if (payload.address) {
							const address_response = yield call(USER_API.addOrUpdateAuthenticatedUserAddress, 
								payload.address, 
								{token: auth_tokens.access_token});
							yield put(updateProfileAddressSuccess(payload.updates, address_response));
						}
					}
				} else {
					if (payload.address) {
						const address_response = yield call(USER_API.addOrUpdateGuestUserAddress, 
							payload.address);
						yield put(updateProfileAddressSuccess(payload.updates, address_response));

					}
				}
		
				yield put(setLoading(false));

			} catch (e) {
				console.log(e);
				yield put(setLoading(false));
			}
			break;
		}
		default: {
			throw new Error('Unexpected action type.');
		}
	}
}

export default profileSaga;
 """
 redux["redux_sagas_profileSaga"] = redux_sagas_profileSaga


 # Add Redux rootSaga
 redux_sagas_rootSaga ="""
import * as ACTION from '../../constants/constants';
import { takeLatest } from 'redux-saga/effects';
import authSaga from './authSaga';
import profileSaga from './profileSaga';
import productSaga from './productSaga';
import checkoutSaga from './checkoutSaga';

function* rootSaga() {
  yield takeLatest([
    ACTION.SIGNIN,
    ACTION.SIGNUP,
    ACTION.SIGNUP_VENDOR,
    ACTION.SIGNUP_VENDOR_DETAILS,
    ACTION.SIGNOUT,
    ACTION.SIGNIN_WITH_GOOGLE,
    ACTION.SIGNIN_WITH_FACEBOOK,
    ACTION.ON_AUTHSTATE_CHANGED,
    ACTION.ON_AUTHSTATE_SUCCESS,
    ACTION.ON_AUTHSTATE_FAIL,
    ACTION.SET_AUTH_PERSISTENCE,
    ACTION.FORGOT_PASSWORD,
    ACTION.RESET_PASSWORD
  ], authSaga);
  yield takeLatest([
    ACTION.ADD_PRODUCT,
    ACTION.SEARCH_PRODUCT,
    ACTION.REMOVE_PRODUCT,
    ACTION.EDIT_PRODUCT,
    ACTION.GET_PRODUCTS,
    ACTION.GET_CATEGORY_PRODUCTS
  ], productSaga);
  yield takeLatest([
    ACTION.UPDATE_EMAIL,
    ACTION.UPDATE_PROFILE
  ], profileSaga);
  yield takeLatest([
    ACTION.ADD_ORDER,
    ACTION.UPDATE_ORDER,
    ACTION.UPDATE_ORDER_TRANSACTION
  ], checkoutSaga);
}

export default rootSaga;
 """
 redux["redux_sagas_rootSaga"] = redux_sagas_rootSaga


 # Add Redux store
 redux_store ="""
import {
	applyMiddleware,
	compose, createStore
  } from 'redux';
import { persistCombineReducers, persistStore } from 'redux-persist';
import storage from 'redux-persist/lib/storage';
import createSagaMiddleware from 'redux-saga';
import rootReducer from '../reducers';
import rootSaga from '../sagas/rootSaga';
  
const sagaMiddleware = createSagaMiddleware();
const composeEnhancer = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
  
const authPersistConfig = {
	key: 'root',
	storage,
	whitelist: ['auth', 'profile', 'cart', 'checkout'] // only auth, profile, cart, checkout will be persisted
};
  
export default () => {
	const store = createStore(
		persistCombineReducers(authPersistConfig, rootReducer),
		composeEnhancer(applyMiddleware(sagaMiddleware))
	);
	const persistor = persistStore(store);
	sagaMiddleware.run(rootSaga);
	return { store, persistor };
};
 """
 redux["redux_store"] = redux_store