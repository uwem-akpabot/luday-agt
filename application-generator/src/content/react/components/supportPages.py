class SupportPage:

 supports = {}
 
 '''
 

 '''
 support_1 ="""
import React from 'react';
import { Link } from 'react-router-dom';
import img from './images/tradefair/tradefairbg.jpg';
import image1 from './images/tradefair/image1.jpeg';
import image2 from './images/tradefair/image2.jpeg';
import image3 from './images/tradefair/image3.jpeg';
import image4 from './images/tradefair/image4.jpeg';
import image5 from './images/tradefair/image5.jpeg';

const Support1 = () => {
  return (
	<>
		<section className="trade_fair_bg ">
			<div className="bg_overlay">
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

		<div className="py-2 luday_wrap">                    
			<div class="grid grid-cols-1 md:grid-cols-2 gap-9 luday_grid_wrap">
				<div className="group px-2 py-[20px] md:pl-36 md:pr-[25px] md:py-[100px]">
					<p className="tracking-widest mb-2.5 text-xs ">@@InnerPreheaderText@@</p>
					<h4>@@InnerHeaderText@@</h4>
					<p className="my-4">@@Paragraph1@@</p>
					<p className="my-4">@@Paragraph2@@</p>		
				</div>
				<div className="group px-2 md:px-4">
					<div class="grid grid-cols-1 md:grid-cols-2 gap-2 py-1 luday_grid_wrap">
						<div className="group">
							<img className="lazy height_top" src={image1} alt="" />	
						</div>
						<div className="group">
							<img className="lazy height_top" src={image2} alt="" />	
						</div>
					</div>
					<div className="grid grid-cols-1 md:grid-cols-3 gap-2 py-1 luday_grid_wrap">
						<div className="group">
							<img className="lazy height_bottom" src={image3} alt="" />	
						</div>
						<div className="group">
							<img className="lazy height_bottom" src={image4} alt="" />	
						</div>
						<div className="group">
							<img className="lazy height_bottom" src={image5} alt="" />	
						</div>
					</div>
				</div>
			</div>
		</div>
	</>
  );
}

export default Support1;
 """
 supports["support_1"] = support_1

# Add page 2
 support_2 ="""

 """
 supports["support_2"] = support_2
