class ProductDetails:

 productDetails = {}
 
 '''
 

 '''
 product_details_1 ="""
import React, {useState, useEffect} from 'react';
import { Link } from 'react-router-dom';
import bdn_spa_beschoice from './images/products/bdn_spa_beschoice.jpg';
import image1 from './images/tradefair/image1.jpeg';
import image2 from './images/tradefair/image2.jpeg';
import image3 from './images/tradefair/image3.jpeg';
import image4 from './images/tradefair/image4.jpeg';
import image5 from './images/tradefair/image5.jpeg';

const ProductDetails1 = () => {
	const [units, setUnits] = useState(0)
        useEffect(() => {
            {console.log(units)}
        })
        const countUp = () => {
            setUnits(units + 1)
        }
        const countDown = () => {
            if (units > 0){ setUnits(units - 1); }
        }
  return (
	<>
		<section className="trade_fair_bg " id="top">
			<div className="bg_overlay">
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

		<div className="py-2 px-[25px] md:px-[60px] lg:px-[140px]">                    
			<div className="grid grid-cols-1 md:grid-cols-2 luday_grid_wrap py-[100px]">				
				<div className="group md:gap-4">
					<img className="lazy w-full lg:w-3/4" src={bdn_spa_beschoice} alt="" />
					<div className="grid grid-cols-4 gap-4 pt-2">
                        <div className="group bg-white">
							<img className="lazy" src={bdn_spa_beschoice} alt="" />
                        </div>
                        <div className="group bg-white">
							<img className="lazy" src={bdn_spa_beschoice} alt="" />
                        </div>
                    </div>
				</div>
				<div className="group">
					<p className="tracking-widest mb-2.5 text-xs ">@@InnerPreheaderText@@</p>
					<h3>@@InnerHeaderText@@</h3>
					<div className="inline-grid grid-cols-3 gap-3 whitespace-nowrap">
					<p className="text-[#9c0] text-xl pb-2"><b>@@Pricename@@</b></p>
					<p className="text-[#9c0] text-xl pb-2"><b>&#8358;@@Price@@</b></p>
					<p className="text-gray-400 text-xl pb-2 line-through"><b>&#8358;@@Price2@@</b></p>
					</div>
					<p className="my-4">@@Paragraph1@@</p>
					<p className="my-4">@@Paragraph2@@</p>
					<p className="my-4">@@Paragraph2@@</p>
					<p className="my-4 pb-2"><Link to="/vendor-details" className="py-3 text-gray-500">Visit Vendors</Link></p>	
					<div className="row  m-5">
						<div className="custom-number-input h-10 w-32">
							<div className="flex flex-row h-10 w-full rounded-lg relative bg-transparent mt-1">
								<button onClick={countDown} className="bg-[#9c0] text-2xl border-[#9c0] hover:bg-[#9c0] text-white h-full w-32 rounded-l cursor-pointer outline-none">
								<span className="m-auto text-2xl font-thin">−</span>
								</button>
								<input type="number" value={units} className="border-[#9c0] text-center w-full bg-white font-semibold text-md hover:text-black focus:text-black md:text-basecursor-default flex items-center text-gray-700" name="custom-input-number" />
								<button onClick={countUp} className="bg-[#9c0] text-2xl border-[#9c0] hover:bg-[#9c0] text-white h-full w-32 rounded-r cursor-pointer">
									<span className="m-auto text-2xl font-thin">+</span>
								</button>
							</div>
						</div>
					</div>
					<div className="button-wrap">
						<Link to="/cart" className="button button--theme overflow-hidden bg-[#9c0] 
						hover:bg-yellow-300 text-white text-bold transition-all ease-in-out duration-300 
						rounded py-3 px-7">Proceed to cart</Link>
					</div>
				</div>
			</div>
		</div>
	</>
  );
}

export default ProductDetails1;
 """
 productDetails["product_details_1"] = product_details_1

# Add page 2
 product_details_2 ="""

 """
 productDetails["product_details_2"] = product_details_2
