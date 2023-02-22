class Deliverys:

 deliverys = {}
 
 '''
 

 '''
 delivery_1 ="""
import React from 'react';
import { Link } from 'react-router-dom';
import bdn_spa_beschoice from './images/products/bdn_spa_beschoice.jpg';


const Delivery1 = () => {
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
					<div className="">
						<h4 className="mb-2">Delivery Details</h4>
						<hr/>
					</div>
					<div className="flex flex-col md:flex-row">
						<div className="mt-3 mb-3 w-auto md:w-full">
							<label for="address">Delivery address
							<span class="text-danger">*</span></label>
							<div class="input-group">
								<textarea name="address" type="text" className="w-full text-black shadow-sm bg-white rounded" id="address" placeholder="Address line" row="3" required/>
							</div>
						</div>
					</div>
					<div className="flex flex-col md:flex-row justify-between">
						<div className="mt-3 mb-3 w-auto md:w-[400px]">
							<label for="postal">Postal code</label>
							<div class="input-group">
								<input name="postal_code" type="text" className="w-full text-black shadow-sm bg-white rounded" id="postal_code" placeholder="post code" required/>
							</div>
						</div>
						<div className="mt-3 mb-3 w-auto md:w-[400px]">
							<label for="postal">Delivery State
							<span class="text-danger">*</span></label>
							<div class="input-group">
							<input type="tel" name="mobile_number" class="w-full form-control text-black shadow-sm bg-white rounded" id="mobile_number" autocomplete="bc-sharp" placeholder="Enter mobile" required/>
							</div>
						</div>
					</div>
					<div className="mt-10 flex flex-col md:flex-row">
						<Link to="/checkout" className="button button--theme overflow-hidden border border-[#9c0]-600
						hover:bg-yellow-300 text-[#9c0] text-sm transition-all ease-in-out duration-300 
						rounded py-3 px-5 m-2 flex items-center flex-nowrap w-full md:w-1/2">
						<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" ><path d="M12.707 17.293 8.414 13H18v-2H8.414l4.293-4.293-1.414-1.414L4.586 12l6.707 6.707z"></path></svg>
						 <span>Previous</span>
						</Link>
						<Link to="/payment" className="button button--theme overflow-hidden bg-[#9c0] 
						hover:bg-yellow-300 text-white text-sm transition-all ease-in-out duration-300 
						rounded py-3 px-5 m-2 flex items-center flex-nowrap w-full md:w-1/2">
						<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" className="fill-current mr-2" ><path d="M5 21h14a2 2 0 0 0 2-2V8a1 1 0 0 0-.29-.71l-4-4A1 1 0 0 0 16 3H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2zm10-2H9v-5h6zM13 7h-2V5h2zM5 5h2v4h8V5h.59L19 8.41V19h-2v-5a2 2 0 0 0-2-2H9a2 2 0 0 0-2 2v5H5z"></path></svg>
						<span>Save and Continue</span>
						</Link>
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

export default Delivery1;
 """
 deliverys["delivery_1"] = delivery_1

# Add page 2
 delivery_2 ="""

 """
 deliverys["delivery_2"] = delivery_2
