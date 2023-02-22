class Payments:

 payments = {}
 
 '''
 

 '''
 payment_1 ="""
import React from 'react';
import { Link } from 'react-router-dom';
import cardpay from './images/payments/visamasterverve.png';
import paycom from './images/payments/paystack-preview.png';
import paymoney from './images/payments/money.png';


const Payment = () => {
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
			<div class="flex flex-col-reverse md:flex-row py-[50px]">	
				<div className="w-full md:w-2/3 m-2 border border-black-600 drop-shadow-md p-5">
					<div>
						<h4 className="mb-2" >Payment Method</h4>
						<hr/>
					</div>
					<div className="flex flex-col">
						<p>How do you want to pay for your order?</p>
                        <div className="mt-3 mb-1 w-full">
							<div className="flex flex-row itmes-center">
							<input type="radio" name="mobile_number" className="text-black shadow-sm bg-white rounded mr-1" id="mobile_number" autocomplete="bc-sharp" required/>
                            <img src={cardpay} alt="payment-method" className="h-6 mr-1"/>
                            <p>Stay Safe, go cashless with card</p>
							</div>
						</div>
					</div>
					<div className="flex flex-row">
						<div className="mt-1 mb-3 w-full">
							<img src={paycom} alt="payment-method" className="h-50 mr-1"/>
						</div>
					</div>
                    <hr/>
                    <div className="mt-5 mb-3 w-full">
                        <div className="flex flex-row itmes-center ">
                        <input type="radio" name="mobile_number" class="text-black shadow-sm bg-white rounded mr-1" id="mobile_number" autocomplete="bc-sharp" required/>
                        <img src={paymoney} alt="payment-method" className="h-10 mr-1"/>
                        <span>Cash on Delivery</span>
                        </div>
					</div>
					 <hr/>
					<div className="mt-10 flex flex-col md:flex-row">
						<Link to="/delivery" className="button button--theme overflow-hidden border border-[#9c0]-600
						hover:bg-yellow-300 text-[#9c0] text-sm transition-all ease-in-out duration-300 
						rounded py-3 px-5 m-2 flex items-center flex-nowrap w-full md:w-1/2">
						<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" ><path d="M12.707 17.293 8.414 13H18v-2H8.414l4.293-4.293-1.414-1.414L4.586 12l6.707 6.707z"></path></svg>
						 <span>Previous</span>
						</Link>
						<button className="button button--theme overflow-hidden bg-[#9c0] 
						hover:bg-yellow-300 text-white text-sm transition-all ease-in-out duration-300 
						rounded py-3 px-5 m-2 flex items-center flex-nowrap w-full md:w-1/2">
						<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" className="fill-current mr-1"><path d="M21 4H3a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h18a1 1 0 0 0 1-1V5a1 1 0 0 0-1-1zm-1 11a3 3 0 0 0-3 3H7a3 3 0 0 0-3-3V9a3 3 0 0 0 3-3h10a3 3 0 0 0 3 3v6z"></path><path d="M12 8c-2.206 0-4 1.794-4 4s1.794 4 4 4 4-1.794 4-4-1.794-4-4-4zm0 6c-1.103 0-2-.897-2-2s.897-2 2-2 2 .897 2 2-.897 2-2 2z"></path></svg> 
						<span>Pay and Complete Order</span>
						</button>
					</div>
					


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

export default Payment;
 """
 payments["payment_1"] = payment_1

# Add page 2
 payment_2 ="""

 """
 payments["payment_2"] = payment_2
