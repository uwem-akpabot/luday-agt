class Hooks:

 hooks = {}


 """
 Hook index
 """
 hooks_index ="""
export { default as useSetAuthPersistence } from './useSetAuthPersistence';
export { default as useDocumentTitle} from './useDocumentTitle';
export { default as useScrollTop } from './useScrollTop';
export { default as useProducts } from './useProducts';
export { default as useOrder } from './useOrder';
export { default as useOrders } from './useOrders';
export { default as useOrderById } from './useOrderById';
export { default as useOrderByRef } from './useOrderByRef';
export { default as useDidMount } from './useDidMount';
export { default as usePaystack } from './usePaystack';
export { default as Popup } from './Popup';
export { default as useFileHandler } from './useFileHandler';
export { default as useGuestOrders } from './useGuestOrders';
 """
 hooks["hooks_index"] = hooks_index


 """
 Hook useScrollTop
 """
 hooks_use_scroll_to_top ="""
import { useEffect } from 'react';

const useScrollTop = () => {
  useEffect(() => {
    window.scrollTo(0, 0);
  }, []);
};

export default useScrollTop;
 """
 hooks["hooks_use_scroll_to_top"] = hooks_use_scroll_to_top


 """
 Hook useDocumentTitle
 """
 hooks_use_document_title ="""
import { useLayoutEffect } from 'react';

const useDocumentTitle = (title) => {
  useLayoutEffect(() => {
    if (title) {
      document.title = title;
    } else {
      document.title = 'Best Deals in Nigeria | BestDealNaija';
    }
  }, [title]);
};

export default useDocumentTitle;
 """
 hooks["hooks_use_document_title"] = hooks_use_document_title


 """
 Hook useSetAuthPersistence
 """
 hooks_use_set_auth_persistence ="""
import { useEffect, useState } from 'react';

import { setAuthPersistence } from '../redux/actions/authActions';

const useSetAuthPersistence = (store) => {
    let [loading, setLoading] = useState(true);
	let auth_tokens = JSON.parse(localStorage.getItem('auth_tokens'));

    let setAuthPersist = ()=> {
        if (auth_tokens) {
            store.dispatch(setAuthPersistence())
            if(loading){
                setLoading(false)
            }
        }
    }

	useEffect(()=> {
        let _store = store.getState()
        let isAuthenticating = _store.app.isAuthenticating
        if (!isAuthenticating) {
            /*  if user is logged in and leaves the page
                set user token whenever access token expires 
            */
            if(loading){
                setAuthPersist()
            }

            let fourtyFourMinutes = 1000 * 60 * 44
            let interval =  setInterval(()=> {
                if(auth_tokens){
                    setAuthPersist()
                }
            }, fourtyFourMinutes)
            return () => clearInterval(interval)
        }

    }, [auth_tokens, loading])
};

export default useSetAuthPersistence;
 """
 hooks["hooks_use_set_auth_persistence"] = hooks_use_set_auth_persistence


 """
 Hook usePaystack
 """
 hooks_use_paystack ="""
import React from 'react';

import PropType from 'prop-types';
import { usePaystackPayment } from 'react-paystack';

import * as ROUTE from '../constants/routes';
import * as CONSTANT from '../constants/constants';

const updateOrder = async (ref) => {
	if (ref) {
		let status = CONSTANT.ORDER_PAYMENT_PENDING
		if (ref.status  && ref.status === 'success') {
			status = CONSTANT.ORDER_SUCCESS
		}
		if (ref.status  && ref.status === 'failed') {
			status = CONSTANT.ORDER_PAYMENT_FAILED
		}
		try {
			const requestOptions = {
				method: "PUT",
				headers: {
					'Accept': 'application/json',
					'Content-Type': 'application/json'
				},
				body: JSON.stringify(
					{
						"ref_transaction_id": ref.transaction,
						"ref_id": ref.trxref,
						"status": status
					}
				)
			}
			await fetch(`${ROUTE.PRODUCTS_API}/order/trxref`, requestOptions)
				.then(res => res.json())
				.then(data => {
					if(ref.redirecturl && data){
						window.location.href = `${process.env.REACT_APP_PAYSTACK_CALLBACK_URL}?trxref=${ref.transaction}&reference=${ref.trxref}`;// eslint-disable-line
					}
				})
				.catch(err=> {
                    console.error("Error:", err);
					location.reload()
                })
		} catch (e) {
			console.log(e)
		}	
	}
};

const handlePaystackSuccessAction = (reference) => {
	if (reference && reference.trxref) {
		updateOrder(reference)
	} else {
		console.log("No transaction reference:: Contact Admin")
	}
};

const handlePaystackCloseAction = () => {
	console.log('closed')
}

const PayWithPaystack = ({state, subTotal}) => {
	const config = {
		reference: state.billing.ref_id,
		email: state.profile.email,
		amount: subTotal * 100, // set in kobo!
		split_code: state.billing.split_code,
		metadata: {
			first_name: state.profile.first_name,
			last_name: state.profile.last_name,
			mobile_number: state.profile.mobile_number,
			custom_field: [{ profile_id: state.profile.id }]
		},
		publicKey: `${process.env.REACT_APP_PAYSTACK_PUBLIC_KEY}` // eslint-disable-line
	};

	const initializePayment = usePaystackPayment(config);
	return (
		<button onClick={() => {
			initializePayment(handlePaystackSuccessAction, handlePaystackCloseAction)
			}}
			className="button button--theme overflow-hidden bg-[#9c0] 
			hover:bg-yellow-300 text-white text-sm transition-all ease-in-out duration-300 
			rounded py-3 px-5 m-2 flex items-center flex-nowrap w-full md:w-1/2">
			<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" className="fill-current mr-1">
				<path d="M21 4H3a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h18a1 1 0 0 0 1-1V5a1 1 0 0 0-1-1zm-1 11a3 3 0 0 0-3 3H7a3 3 0 0 0-3-3V9a3 3 0 0 0 3-3h10a3 3 0 0 0 3 3v6z">
				</path>
				<path d="M12 8c-2.206 0-4 1.794-4 4s1.794 4 4 4 4-1.794 4-4-1.794-4-4-4zm0 6c-1.103 0-2-.897-2-2s.897-2 2-2 2 .897 2 2-.897 2-2 2z">
				</path>
			</svg> 
			<span>Pay & Complete Order</span>
		</button>
	);

};

PayWithPaystack.propTypes = {
	state: PropType.object.isRequired,
	subTotal: PropType.any.isRequired
};
export default PayWithPaystack;
 """
 hooks["hooks_use_paystack"] = hooks_use_paystack
 

 """
 Hook useProducts
 """
 hooks_use_products ="""
import { useCallback, useEffect, useState } from 'react';
import { useDispatch } from 'react-redux';

import { getProducts } from '../redux/actions/productActions'
import useDidMount from './useDidMount';
import * as ROUTE from '../constants/routes';

const useProducts = () => {      
	const [products, setProducts] = useState([]);
	const [isLoading, setLoading] = useState(false);
	const [error, setError] = useState('');
	const didMount = useDidMount(true);
	const dispatch = useDispatch();

	const fetchProducts = useCallback(async () => {
		try {
			setLoading(true);
			setError('');

			const requestOptions = {
				method: "GET",
				headers: {
					'content-type': 'application/json'
				}
			}
			const docs =  await fetch(`${ROUTE.PRODUCTS_API}/products/verified`, requestOptions)
				.then(res => res.json())
				.then(data =>{
					return data
				})
				.catch(err => console.log(err))

			if (docs.results.length == 0) {
				if (didMount) {
					setError('No products found.');
					setLoading(false);
				}
			} else {
				const data = docs.results;
				if (didMount) {
					setProducts(data);
					setLoading(false);
				}
			}
		} catch (e) {
			if (didMount) {
				setError('Failed to fetch products');
				setLoading(false);
			}
		}
	}, [didMount]);

	useEffect(() => {
		if (products.length === 0 && didMount) {
			fetchProducts();
			dispatch(getProducts());
		}
	}, []);


	return {
		products, fetchProducts, isLoading, error
	};
};

export default useProducts;
 """
 hooks["hooks_use_products"] = hooks_use_products


 """
 Hook useOrders
 """
 hooks_use_orders ="""
import { useCallback, useEffect, useState } from 'react';

import useDidMount from './useDidMount';
import * as ROUTE from '../constants/routes';

const useOrders = (token, isLoading) => {      
	const [orders, setOrders] = useState([]);
	const [error, setError] = useState('');
	const didMount = useDidMount(true);

	const fetchOrders = useCallback(async () => {
		try {
			setError('');
			const requestOptions = {
				method: "GET",
				headers: {
					'Content-Type': 'application/json',
					'Accept': 'application/json',
					'Authorization': `Bearer ${token}`
				}
			}
			const _orders =  await fetch(`${ROUTE.PRODUCTS_API}/order/user`, requestOptions)
				.then(res => res.json())
				.then(data =>{
					return data
				})
				.catch(err => console.log(err))

			if (_orders.length == 0) {
				if (didMount) {
					setError('No order for authenticated user.');
				}
			} else {
				const data = _orders;
				if (didMount) {
					setOrders(data);
				}
			}
		} catch (e) {
			if (didMount) {
				setError('Failed to fetch orders');
			}
		}
	}, [didMount]);

	useEffect(() => {
		if (orders.length === 0 && didMount) {
			fetchOrders();
		}
	}, []);


	return {
		orders, fetchOrders, isLoading, error
	};
};

export default useOrders;
 """
 hooks["hooks_use_orders"] = hooks_use_orders


 """
 Hook useOrderByRef
 """
 hooks_use_order_by_ref ="""
import { useCallback, useEffect, useState } from 'react';

import useDidMount from './useDidMount';
import * as ROUTE from '../constants/routes';

const useOrderByRef = (trxref, reference) => {      
	const [order, setOrder] = useState([]);
	const [error, setError] = useState('');
	const [isLoading, setLoading] = useState(false);
	const didMount = useDidMount(true);

	const fetchOrderByTrxref = useCallback(async () => {
		try {
			setError('');
			const requestOptions = {
				method: "GET",
				headers: {
					'Content-Type': 'application/json',
					'Accept': 'application/json'
				}
			}
			setLoading(true)
			const _order =  await fetch(`${ROUTE.PRODUCTS_API}/order/reference?trxref=${trxref}&reference=${reference}`, 
								requestOptions)
				.then(res => res.json())
				.then(data =>{
					return data
				})
				.catch(err => console.log(err))

			if (_order.length == 0) {
				if (didMount) {
					setError('No order found.');
					setLoading(false)
				}
			} else {
				const data = _order;
				if (didMount) {
					setOrder(data);
					setLoading(false)
				}
			}
		} catch (e) {
			if (didMount) {
				setError('Failed to fetch order');
			}
		}
	}, [didMount]);

	useEffect(() => {
		if (order.length === 0 && didMount) {
			fetchOrderByTrxref();
		}
	}, []);

	return {
		order, fetchOrderByTrxref, isLoading, error
	};
};

export default useOrderByRef;
 """
 hooks["hooks_use_order_by_ref"] = hooks_use_order_by_ref


 """
 Hook useOrderById
 """
 hooks_use_order_by_id ="""
import { useCallback, useEffect, useState } from 'react';

import useDidMount from './useDidMount';
import * as ROUTE from '../constants/routes';

const useOrderById = (order_id) => {      
	const [order, setOrder] = useState([]);
	const [error, setError] = useState('');
	const [isLoading, setLoading] = useState(false);
	const didMount = useDidMount(true);

	const fetchOrderById = useCallback(async () => {
		try {
			setError('');
			const requestOptions = {
				method: "GET",
				headers: {
					'Content-Type': 'application/json',
					'Accept': 'application/json'
				}
			}
			setLoading(true)
			const _order =  await fetch(`${ROUTE.PRODUCTS_API}/order/id?order_id=${order_id}`, 
								requestOptions)
				.then(res => res.json())
				.then(data =>{
					return data
				})
				.catch(err => console.log(err))

			if (_order.length == 0) {
				if (didMount) {
					setError('No order for guest user.');
					setLoading(false);
				}
			} else {
				const data = _order;
				if (didMount) {
					setLoading(false);
					setOrder(data);
				}
			}
		} catch (e) {
			if (didMount) {
				setError('Failed to fetch order');
			}
		}
	}, [didMount]);

	useEffect(() => {
		if (order.length === 0 && didMount) {
			fetchOrderById();
		}
	}, []);

	return {
		order, fetchOrderById, isLoading, error
	};
};

export default useOrderById;
 """
 hooks["hooks_use_order_by_id"] = hooks_use_order_by_id


 """
 Hook useOrder
 """
 hooks_use_order ="""
import { useEffect, useState } from 'react';

import useDidMount from './useDidMount';
import * as ROUTE from '../constants/routes';

const useOrder = (id, token) => {      
	const [order, setOrder] = useState([]);
	const [isLoading, setLoading] = useState(false);
	const [error, setError] = useState(null);
	const didMount = useDidMount(true);

	useEffect(() => {
		(async () => {
			try {
				const requestOptions = {
					method: "GET",
					headers: {
						'Content-Type': 'application/json',
						'Accept': 'application/json',
						'Authorization': `Bearer ${token}`
					}
				}
				if (!order || order.id !== id) {
					setLoading(true);
					const order_details = await fetch(`${ROUTE.PRODUCTS_API}/order/mapping/${id}`, requestOptions);

					if (order_details) {
					const data = order_details;

						if (didMount) {
							setOrder(data);
							setLoading(false);
						}
					} else {
					setError('Order not found.');
					}
				}
			} catch (err) {
				if (didMount) {
					setLoading(false);
					setError(err?.message || 'Something went wrong.');
				}
			}
		})();
	}, [id, token]);

	return { order, isLoading, error };
};

export default useOrder;
 """
 hooks["hooks_use_order"] = hooks_use_order


 """
 Hook useGuestOrders
 """
 hooks_use_guest_orders ="""
import { useCallback, useEffect, useState } from 'react';

import useDidMount from './useDidMount';
import * as ROUTE from '../constants/routes';

const useGuestOrders = (isLoading, kwargs) => {      
	const [orders, setOrders] = useState([]);
	const [error, setError] = useState('');
	const didMount = useDidMount(true);

	const fetchOrders = useCallback(async () => {
		try {
			setError('');
			const requestOptions = {
				method: "GET",
				headers: {
					'Content-Type': 'application/json',
					'Accept': 'application/json'
				}
			}
			const _orders =  await fetch(`${ROUTE.PRODUCTS_API}/order/mapping/${kwargs.ref_order_id}/${kwargs.email}`, 
								requestOptions)
				.then(res => res.json())
				.then(data =>{
					return data
				})
				.catch(err => console.log(err))

			if (_orders.length == 0) {
				if (didMount) {
					setError('No order for guest user.');
				}
			} else {
				const data = _orders;
				if (didMount) {
					setOrders(data);
				}
			}
		} catch (e) {
			if (didMount) {
				setError('Failed to fetch orders');
			}
		}
	}, [didMount]);

	useEffect(() => {
		if (orders.length === 0 && didMount) {
			fetchOrders();
		}
	}, []);

	return {
		orders, fetchOrders, isLoading, error
	};
};

export default useGuestOrders;
 """
 hooks["hooks_use_guest_orders"] = hooks_use_guest_orders


 """
 Hook useFileHandler
 """
 hooks_use_file_handler ="""
/* eslint-disable no-alert */
import { useState } from 'react';

const useFileHandler = (initState) => {
  const [imageFile, setImageFile] = useState(initState);
  const [isFileLoading, setFileLoading] = useState(false);

  const onFileChange = (event, { name }) => {
    const val = event.target.value;
    const img = event.target.files[0];
    const size = img.size / 1024 / 1024;
    const regex = /(\.jpg|\.jpeg|\.png)$/i;

    setFileLoading(true);
    if (!regex.exec(val)) {
      alert('File type must be JPEG or PNG', 'error');
      setFileLoading(false);
    } else if (size > 2) {
      alert('File size exceeded "2MB", consider optimizing your image', 'error');
      setFileLoading(false);
    } else {
      const reader = new FileReader();

      reader.addEventListener('load', (e) => {
        setImageFile({
          ...imageFile,
          [name]: { file: img, url: e.target.result }
        });
        setFileLoading(false);
      });
      reader.readAsDataURL(img);
    }
  };

  return {
    imageFile,
    setImageFile,
    isFileLoading,
    onFileChange
  };
};

export default useFileHandler;
 """
 hooks["hooks_use_file_handler"] = hooks_use_file_handler


 """
 Hook useDidMount
 """
 hooks_use_did_mount ="""
import { useEffect, useState } from 'react';

const useDidMount = (initState = false) => {
  const [didMount, setDidMount] = useState(initState);

  useEffect(() => {
    setDidMount(true);

    return () => {
      setDidMount(false);
    };
  }, []);

  return didMount;
};

export default useDidMount;
 """
 hooks["hooks_use_did_mount"] = hooks_use_did_mount


 """
 Hook ScrollToTop1
 """
 hooks_use_scroll_to_top_1 ="""
import React, { useEffect } from "react";
import { useLocation } from "react-router";
import PropType from 'prop-types';

const ScrollToTop1 = (props) => {
  const location = useLocation();
  useEffect(() => {
    window.scrollTo(0, 0);
  }, [location]);

  return <>{props.children}</>
};

ScrollToTop1.propTypes = {
  children: PropType.string
};

export default ScrollToTop1;
 """
 hooks["hooks_use_scroll_to_top_1"] = hooks_use_scroll_to_top_1


 """
 Hook Popup
 """
 hooks_use_pop_up ="""
import React from "react";
import PropType from 'prop-types';
import useDidMount from "./useDidMount";

const Popup = props => {
  const didMount = useDidMount(true);
  if (didMount) {
    return (
      <div className="fixed bg-[#00000050] w-full h-[100vh] top-0 left-0 z-10">
        <div className="relative w-[70%] my-0 mx-auto h-auto max-h-[70vh] mt-[calc(100vh - 85vh - 20px)] top-40 bg-white rounded-md p-10 border border-[#999] overflow-auto">
          <span className="absolute content-['X'] cursor-pointer  right-4 top-2  bg-[#ededed] w-[25px] h-[25px] rounded-lg leading-5 text-center border-[#999] text-xl" onClick={props.handleClose}>x</span>
          {props.content}
        </div>
      </div>
    );
  }
};

Popup.propTypes = {
    content: PropType.object,
    handleClose: PropType.func
};

 
export default Popup;
 """
 hooks["hooks_use_pop_up"] = hooks_use_pop_up


 """
 Hook useExample
 """
 hooks_use_example ="""

 """
 hooks["hooks_use_example"] = hooks_use_example

