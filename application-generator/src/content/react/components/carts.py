class Carts:

 carts = {}
 

 '''
Cart summary index
 '''
 cart_summary_index ="""
export { default as CartSummary } from './CartSummary';
 """
 carts["cart_summary_index"] = cart_summary_index


 '''
Cart Summary component
 '''
 cart_summary ="""
import React from 'react';
import { useLocation, Link } from 'react-router-dom';
import { useSelector } from "react-redux";

import * as ROUTE from '../../constants/routes'
import { displayMoney, calculateArrayTotal } from '../../helpers/utils';
const @@PageName@@ = () => {
	const { cart } = useSelector((state) => ({
		cart: state.cart
	}));
	const { pathname } = useLocation();

	return (
		<div className="w-full md:w-1/4 m-2 border border-black-600 drop-shadow-md p-5 h-1/2">
			<h2 className="text-2xl mb-5">@@PageTitleHeading2@@</h2>
			<p>VAT <span>&#8358;0.00</span></p>
			<p className="mb-5">@@SubtotalParagraphText@@ <br />
				<span>
					&#8358;{displayMoney(calculateArrayTotal(cart.map((product) => 
							product?.sale_price ? product.sale_price * product.cart_quantity
								: product.price * product.cart_quantity
						))
					)}
				</span>
			</p>
			<hr/>
			<h2 className="text-2xl mt-5">@@GrandTotalHeading2Text@@</h2>
			<h2 className="text-3xl mt-5 font-bold">
				&#8358;{displayMoney(calculateArrayTotal(cart.map((product) => 
						product?.sale_price ? product.sale_price * product.cart_quantity
							: product.price * product.cart_quantity
					))
				)}
			</h2>
			<div className="mt-4 mx-0">
				{pathname == ROUTE.CART ? (
					<Link to={ROUTE.PRODUCTS} className="button button--theme overflow-hidden [#490] border border-[#9c0]-600
						text-[#98c01d] text-sm transition-all ease-in-out duration-300 
						rounded py-3 px-5 my-2 flex items-center flex-nowrap">
					<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" ><path d="M12.707 17.293 8.414 13H18v-2H8.414l4.293-4.293-1.414-1.414L4.586 12l6.707 6.707z"></path></svg>
					<span>@@ContinueShoppingText@@</span>
					</Link>
					) :(
					<Link to={ROUTE.CART} className="button button--theme overflow-hidden [#490] border border-[#9c0]-600
						text-[#98c01d] text-sm transition-all ease-in-out duration-300 
						rounded py-3 px-5 my-2 flex items-center flex-nowrap">
						<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" ><path d="M12.707 17.293 8.414 13H18v-2H8.414l4.293-4.293-1.414-1.414L4.586 12l6.707 6.707z"></path></svg>
						<span>@@ProceedToPreviousPageText@@</span>
					</Link>
				)}
				{pathname == ROUTE.CART && (
					<Link to={ROUTE.CHECKOUT} className="button button--theme overflow-hidden bg-[#98c01d] 
							text-white transition-all ease-in-out duration-300 
							rounded py-3 px-5 my-2 flex items-center flex-nowrap">
						<span>@@ProceedToNextPageText@@</span>
						<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" className="fill-current">
							<path d="m11.293 17.293 1.414 1.414L19.414 12l-6.707-6.707-1.414 1.414L15.586 11H6v2h9.586z"></path>
						</svg>
					</Link>
				)}
			</div>
		</div>
	)
}
export default @@PageName@@;
 """
 carts["cart_summary"] = cart_summary


 '''
Cart 1
 '''
 cart_1 ="""
import React from 'react';
import { Link } from 'react-router-dom';
import bdn_spa_beschoice from './images/products/bdn_spa_beschoice.jpg';


const Cart1 = () => {
  return (
	<>
		<section className="mt-20 md:mt-40">
			<div className="">
				<div class="container">
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
			<div class="flex flex-col md:flex-row py-[50px]">	
				<div className="w-full md:w-2/3 m-2 border border-black-600 drop-shadow-md p-5">
					<div className="overflow-x-auto">
						<table className="divide-y divide-gray-300 md:w-full">
							<thead className="bg-gray-50" >
								<tr>
									<th className="px-6 py-2 text-left">@@Product@@</th>
									<th className="px-6 py-2 ">@@Quantity@@</th>
									<th className="px-6 py-2 ">@@Price@@</th>
									<th className="px-6 py-2 text-right">@@Remove@@</th>
								</tr>
							</thead>
							<tbody>
								<tr className="border border-black-600 whitespace-nowrap">
									<td className="flex flex-col flex-nowrap items-left p-2 w-[100px]">
										<div className="m-2">
											<img class="lazy" src={bdn_spa_beschoice} className="w-[90px]" alt="" />
										</div>
										<p className="text-sm">@@Productname@@</p>
									</td>
									<td className="text-center">
										6
									</td>
									<td className="text-center">@@Amount@@</td>
									<td className="float-right mr-10"><Link to="#" className="text-red-900"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" className="text-red-900" ><path d="M5 20a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8h2V6h-4V4a2 2 0 0 0-2-2H9a2 2 0 0 0-2 2v2H3v2h2zM9 4h6v2H9zM8 8h9v12H7V8z"></path><path d="M9 10h2v8H9zm4 0h2v8h-2z"></path></svg></Link></td>
								</tr>
								<tr className="border border-black-600 whitespace-nowrap">
									<td className="flex flex-col flex-nowrap items-left p-2 w-[100px]">
										<div className="m-2">
											<img class="lazy" src={bdn_spa_beschoice} className="w-[90px]" alt="" />
										</div>
										<p className="text-sm">@@Productname@@</p>
									</td>
									<td className="text-center">
										6
									</td>
									<td className="text-center">@@Amount@@</td>
									<td className="float-right mr-10"><Link to="#" className="text-red-900"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" className="text-red-900" ><path d="M5 20a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8h2V6h-4V4a2 2 0 0 0-2-2H9a2 2 0 0 0-2 2v2H3v2h2zM9 4h6v2H9zM8 8h9v12H7V8z"></path><path d="M9 10h2v8H9zm4 0h2v8h-2z"></path></svg></Link></td>
								</tr>
								<tr className="border border-black-600 whitespace-nowrap">
									<td className="flex flex-col flex-nowrap items-left p-2 w-[100px]">
										<div className="m-2">
											<img class="lazy" src={bdn_spa_beschoice} className="w-[90px]" alt="" />
										</div>
										<p className="text-sm">@@Productname@@</p>
									</td>
									<td className="text-center">
										6
									</td>
									<td className="text-center">@@Amount@@</td>
									<td className="float-right mr-10"><Link to="#" className="text-red-900"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" className="text-red-900" ><path d="M5 20a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8h2V6h-4V4a2 2 0 0 0-2-2H9a2 2 0 0 0-2 2v2H3v2h2zM9 4h6v2H9zM8 8h9v12H7V8z"></path><path d="M9 10h2v8H9zm4 0h2v8h-2z"></path></svg></Link></td>
								</tr>
								<tr className="border border-black-600 whitespace-nowrap">
									<td className="flex flex-col flex-nowrap items-left p-2 w-[100px]">
										<div className="m-2">
											<img class="lazy" src={bdn_spa_beschoice} className="w-[90px]" alt="" />
										</div>
										<p className="text-sm">@@Productname@@</p>
									</td>
									<td className="text-center">
										6
									</td>
									<td className="text-center">@@Amount@@</td>
									<td className="float-right mr-10"><Link to="#" className="text-red-900"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" className="text-red-900" ><path d="M5 20a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8h2V6h-4V4a2 2 0 0 0-2-2H9a2 2 0 0 0-2 2v2H3v2h2zM9 4h6v2H9zM8 8h9v12H7V8z"></path><path d="M9 10h2v8H9zm4 0h2v8h-2z"></path></svg></Link></td>
								</tr>
							</tbody>
						</table>
					</div>
				</div>
				<div className="w-full md:w-1/3 m-2 border border-black-600 drop-shadow-md p-5 h-1/2">
					<h2 className="text-2xl mb-5">@@CartSummary@@</h2>
					<p>@@Vat@@ <span>₦0.00</span></p>
					<p className="mb-5">Subtotal <span>@@Cartprice@@</span></p>
					<hr/>
					<h2 className="text-2xl mt-5">Grand Total <span>@@Cartprice@@</span></h2>
					<div className="mt-10 flex flex-col">
						<Link to="/products" className="button button--theme overflow-hidden border border-[#9c0]-600
						hover:bg-yellow-300 text-[#9c0] text-sm transition-all ease-in-out duration-300 
						rounded py-3 px-5 m-2 flex items-center flex-nowrap">
						<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" ><path d="M12.707 17.293 8.414 13H18v-2H8.414l4.293-4.293-1.414-1.414L4.586 12l6.707 6.707z"></path></svg>
						 <span>Continue Shopping</span>
						</Link>
						<Link to="/checkout" className="button button--theme overflow-hidden bg-[#9c0] 
						hover:bg-yellow-300 text-white text-sm transition-all ease-in-out duration-300 
						rounded py-3 px-5 m-2 flex items-center flex-nowrap">
						<span>Proceed to Checkout</span>
						<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" className="fill-current"><path d="m11.293 17.293 1.414 1.414L19.414 12l-6.707-6.707-1.414 1.414L15.586 11H6v2h9.586z"></path></svg>
						</Link>
					</div>
				</div>
				
			</div>
		</div>
	</>
  );
}

export default Cart1;
 """
 carts["cart_1"] = cart_1

# Add page 2
 '''
Cart 2
 '''
 cart_2 ="""
import React from 'react';
const @@PageName@@ = () => {

}
export default @@PageName@@;
 """
 carts["cart_2"] = cart_2
