class Checkouts:

 checkouts = {}


 '''
 Checkout component 1
 '''
 checkout_1 ="""
import React from 'react';
import { Link } from 'react-router-dom';
import bdn_spa_beschoice from './images/products/bdn_spa_beschoice.jpg';


const Checkout1 = () => {
  return (
	<>
		<section className="mt-20 md:mt-40">
			<div className="">
				<div className="container">
					<div className="hero_inner">
						<div className="text-center">
							<p className="tracking-widest mb-2.5 text-xs">@@PreheaderText@@</p>
							<h1 className="text-6xl font-semibold tracking-tight">@@HeaderText@@</h1>
						</div>
					</div>
				</div>
			</div>
		</section>

		<div className="py-2 px-[10px] mt-10 md:px-[60px] lg:px-[90px]">                    
			<div className="flex flex-col-reverse md:flex-row py-[50px]">	
				<div className="w-full md:w-2/3 m-2 border border-black-600 drop-shadow-md p-5">
					<div className="">
						<h4 className="mb-2">Billing Details</h4>
						<hr/>
					</div>
					<div className="flex flex-col md:flex-row justify-between">
						<div className="mt-3 mb-3 w-auto md:w-[400px]">
							<label htmlFor="firstName">First name
							<span className="text-danger">*</span></label>
							<div className="">
								<input name="first_name" type="text" className="w-full text-black shadow-sm bg-white rounded" id="firstName" placeholder="Enter first-name" required/>
							</div>
						</div>
						<div className="mt-3 mb-3 w-auto md:w-[400px]">
							<label htmlFor="lastname">Last name
							<span className="text-danger">*</span></label>
							<div className="input-group">
								<input name="last_name" type="text" className="w-full text-black shadow-sm bg-white rounded" id="lastName" placeholder="Enter last-name" required/>
							</div>
						</div>
					</div>
					<div className="flex flex-col md:flex-row justify-between">
						<div className="mt-3 mb-3 w-auto md:w-[400px]">
							<label htmlFor="mobile">Phone
							<span className="text-danger">*</span></label>
							<div className="input-group">
							<input type="tel" name="mobile_number" className="w-full htm text-black shadow-sm bg-white rounded" id="mobile_number" autoComplete="bc-sharp" placeholder="Enter mobile" required/>
							</div>
						</div>
						<div className="mt-3 mb-3 w-auto md:w-[400px]">
							<label htmlFor="email">Email
							<span className="text-danger">*</span></label>
							<div className="input-group">
								<input name="email_name" type="email" className="w-full text-black shadow-sm bg-white rounded" id="email" placeholder="you@example.com" required/>
							</div>
						</div>
					</div>
					<div className="flex flex-col md:flex-row">
						<div className="mt-3 mb-3 w-auto md:w-full">
							<label htmlFor="address">Address
							<span className="text-danger">*</span></label>
							<div className="input-group">
								<textarea name="address" type="text" className="w-full text-black shadow-sm bg-white rounded" id="address" placeholder="Address line" row="3" required/>
							</div>
						</div>
					</div>
					<div className="flex flex-col md:flex-row justify-between">
						<div className="mt-3 mb-3 w-auto md:w-[400px]">
							<label htmlFor="postal">Postal code</label>
							<div className="input-group">
								<input name="postal_code" type="text" className="w-full text-black shadow-sm bg-white rounded" id="postal_code" placeholder="post code" required/>
							</div>
						</div>
						<div className="mt-3 mb-3 w-auto md:w-[400px]">
							<label htmlFor="postal">State
							<span className="text-danger">*</span></label>
							<div className="input-group">
							<input type="tel" name="mobile_number" className="w-full text-black shadow-sm bg-white rounded" id="mobile_number" autoComplete="bc-sharp" placeholder="Enter mobile" required/>
							</div>
						</div>
					</div>
					<div className="mt-10 flex justify-center">
						<Link to="/delivery" className="button button--theme overflow-hidden bg-[#9c0] 
						hover:bg-yellow-300 text-white text-sm transition-all ease-in-out duration-300 
						rounded py-3 px-5 m-2 flex items-center flex-nowrap w-80 justify-center">
						<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" className="fill-current mr-2" ><path d="M5 21h14a2 2 0 0 0 2-2V8a1 1 0 0 0-.29-.71l-4-4A1 1 0 0 0 16 3H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2zm10-2H9v-5h6zM13 7h-2V5h2zM5 5h2v4h8V5h.59L19 8.41V19h-2v-5a2 2 0 0 0-2-2H9a2 2 0 0 0-2 2v5H5z"></path></svg>
						<span>Save and Continue</span>
						</Link>
					</div>
					<p className="text-center">By clicking save and continue you agree to our <Link to="/terms-and-conditions" className="text-blue-300">Terms and Conditions</Link> and <Link to="/privacy-policy" className="text-blue-300">Privacy Policy</Link></p>
				</div>
				<div className="w-full md:w-1/3 m-2 border border-black-600 drop-shadow-md p-5 h-1/2">
					<h2 className="text-2xl mb-5">@@CartSummary@@</h2>
					<p>@@Vat@@ <span>₦0.00</span></p>
					<p className="mb-5">Subtotal <span>@@Cartprice@@</span></p>
					<hr/>
					<h2 className="text-2xl mt-5">Grand Total <span>@@Cartprice@@</span></h2>
					<div className="mt-10 flex flex-col">
						<Link to="/cart" className="button button--theme overflow-hidden border border-[#9c0]-600
						hover:bg-yellow-300 text-[#9c0] text-sm transition-all ease-in-out duration-300 
						rounded py-3 px-5 m-2 flex items-center flex-nowrap">
						<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" ><path d="M12.707 17.293 8.414 13H18v-2H8.414l4.293-4.293-1.414-1.414L4.586 12l6.707 6.707z"></path></svg>
						 <span>Back to Cart</span>
						</Link>
					</div>
				</div>
			</div>
		</div>
	</>
  );
}

export default @@PageName@@;
 """
 checkouts["checkout_1"] = checkout_1


 """
 Checkout payment method component 1
 """
 checkout_payment_methods_1 ="""
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

import { useFormikContext } from 'formik';
import PropType from 'prop-types';

import cardpay from '../../../images/payments/visamasterverve.png';
import paycom from '../../../images/payments/paystack-preview.png';
import paymoney from '../../../images/payments/money.png';
import PayWithPaystack from '../../../hooks/usePaystack';
import * as ROUTE from '../../../constants/routes';
import { calculateArrayTotal } from '../../../helpers/utils';

const @@PageName@@ = ({state}) => {
    const { values, setValues } = useFormikContext();
	const [paystackBtn, setPaystackBtn] = useState(false);
	const [cashBtn, setCashBtn] = useState(false);
	const navigate = useNavigate();

	const subtotal = calculateArrayTotal(
		state.cart.map((product) => 
			product?.sale_price ? product.sale_price * product.cart_quantity
			: product.price * product.cart_quantity
	));

	const onClickPrevious = () => {
		navigate(ROUTE.CHECKOUT);
	};
	const handlePaystackChange = (e) => {
		if (e.target.checked) {
			setValues({ payment_type: 'paystack' });
			setCashBtn(false);
			setPaystackBtn(!paystackBtn);
		}
	};
	const handleCashChange = (e) => {
		if (e.target.checked) {
			setValues({ payment_type: 'cash' });
			setPaystackBtn(false);
			setCashBtn(!cashBtn);
		}
	};

	return (
		<>
			<div className={`flex flex-col ${values.payment_type === 'paystack' ? 'is-selected-payment' : ''}`}>
				<p>@@SubHeadingParagraph1@@</p>
				<div className="mt-3 mb-1 w-full">
					<div className="flex flex-row itmes-center">
						<input 
							checked={values.payment_type === 'paystack'}
							type="radio" 
							name="payment_type" 
							className="text-black shadow-sm bg-white rounded mr-1" 
							id="paystack"
							onChange={handlePaystackChange} 
							required
						/>
						<img src={cardpay} alt="payment-method" className="h-6 mr-1"/>
						<p>@@paragraph2Span1@@</p>
					</div>
				</div>
			</div>
			<div className="flex flex-row">
				<div className="mt-1 mb-3 w-full">
					<img src={paycom} alt="payment-method" className="h-50 mr-1"/>
				</div>
			</div>
			<hr/>
			<div className={`mt-5 mb-3 w-full ${values.payment_type === 'cash' ? 'is-selected-payment' : ''}`}>
				<div className="flex flex-row itmes-center">
					<input 
						checked={values.payment_type === 'cash'}
						type="radio" 
						name="payment_type" 
						className="text-black shadow-sm bg-white rounded mr-1" 
						id="cash"
						onChange={handleCashChange}  
						required
					/>
					<img src={paymoney} alt="payment-method" className="h-10 mr-1"/>
					<span>@@Radio1SpanText@@</span>
				</div>
			</div>
			<hr/>
			<div className="mt-10 flex flex-col md:flex-row">
				<button 
					disabled={state.isLoading}
					type="button" 
					className="button button--theme overflow-hidden border border-[#9c0]-600
						hover:bg-yellow-300 text-[#9c0] text-sm transition-all ease-in-out duration-300 
						rounded py-3 px-5 m-2 flex items-center flex-nowrap w-full md:w-1/2"
					onClick={() => onClickPrevious()}
				>
					<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" ><path d="M12.707 17.293 8.414 13H18v-2H8.414l4.293-4.293-1.414-1.414L4.586 12l6.707 6.707z"></path></svg>
					<span>@@ProceedToPreviousPageText@@</span>
				</button>
				{(values.payment_type === 'paystack' || paystackBtn ) && 
					@@Pos1@@
				}
				{(values.payment_type === 'cash' || cashBtn) &&
					<button
						disabled={state.isLoading}
						className="button button--theme overflow-hidden bg-[#9c0] 
						hover:bg-yellow-300 text-white text-sm transition-all ease-in-out duration-300 
						rounded py-3 px-5 m-2 flex items-center flex-nowrap w-full md:w-1/2">
						<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" className="fill-current mr-1">
							<path d="M21 4H3a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h18a1 1 0 0 0 1-1V5a1 1 0 0 0-1-1zm-1 11a3 3 0 0 0-3 3H7a3 3 0 0 0-3-3V9a3 3 0 0 0 3-3h10a3 3 0 0 0 3 3v6z">
							</path>
							<path d="M12 8c-2.206 0-4 1.794-4 4s1.794 4 4 4 4-1.794 4-4-1.794-4-4-4zm0 6c-1.103 0-2-.897-2-2s.897-2 2-2 2 .897 2 2-.897 2-2 2z">
							</path>
						</svg> 
						<span>{state.isLoading ? '@@SubmitBtnOnLoadingText@@' : '@@SubmitBtnText@@'}</span>
					</button>
				}
			</div>
		</>
	);
};

@@PageName@@.propTypes = {
	state: PropType.object.isRequired
};

export default @@PageName@@;
 """
 checkouts["checkout_payment_methods_1"] = checkout_payment_methods_1


 """
 Checkout cash on delivery callback
 """
 checkout_cash_on_delivery_callback ="""
import React from 'react';
import { useDispatch, useSelector } from "react-redux";
import { Navigate } from 'react-router-dom';

import * as ROUTE from '../../../constants/routes';
import img from '../../../images/tradefair/tradefairbg.jpg';
import Banner  from '../../../components/default/Banner/index';
import { useDocumentTitle, useOrderById } from '../../../hooks';
import { clearCart } from '../../../redux/actions/cartActions';
import { OrderDetails } from '../components';

const @@PageName@@ = () => {
	useDocumentTitle('@@DocumentTitle@@');
    const { cart, billing } = useSelector((state) => ({
		cart: state.cart,
		billing: state.checkout.billing
	}));
	if (!billing) {
		return <Navigate to={ROUTE.CHECKOUT} />;
	}	

	const { order, isLoading } = useOrderById(billing.ref_order_id);
	const dispatch = useDispatch();

	if (cart.length) {
		dispatch(clearCart());
	}
	return (
		<>
			@@Pos1@@
			@@Pos2@@
		</>
	);
}
export default @@PageName@@;
 """
 checkouts["checkout_cash_on_delivery_callback"] = checkout_cash_on_delivery_callback


 """
 Checkout paystack callback
 """
 checkout_paystack_callback ="""
import React from 'react';
import { useDispatch, useSelector } from "react-redux";
import { Navigate, useSearchParams } from 'react-router-dom';

import * as ROUTE from '../../../constants/routes';
import img from '../../../images/tradefair/tradefairbg.jpg';
import Banner  from '../../../components/default/Banner/index';
import { useDocumentTitle, useOrderByRef } from '../../../hooks';
import { clearCart } from '../../../redux/actions/cartActions';
import { OrderDetails } from '../components';

const @@PageName@@ = () => {
	useDocumentTitle('@@DocumentTitle@@');
    const { cart } = useSelector((state) => ({
		cart: state.cart
	}));
	const [searchParams] = useSearchParams();
	const trxref = searchParams.get('trxref');
	const reference = searchParams.get('reference');

	if (!trxref && !reference) {
		return <Navigate to={ROUTE.CHECKOUT} />;
	}

	const { order, isLoading } = useOrderByRef(trxref, reference);
	const dispatch = useDispatch();

	if (cart.length) {
		dispatch(clearCart());
	}
	return (
		<>
			@@Pos1@@
			@@Pos2@@
		</>
	);
}
export default @@PageName@@;
 """
 checkouts["checkout_paystack_callback"] = checkout_paystack_callback

 """
 
 """
 checkout_2 ="""
const @@PageName@@ = () => {
	useDocumentTitle('@@DocumentTitle@@');
    
}
export default @@PageName@@;
 """
 checkouts["checkout_2"] = checkout_2
