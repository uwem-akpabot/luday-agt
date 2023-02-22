class Sliders:

 sliders = {}


 """
 Slider 1 Component
 """
 slide_1 ="""
import React from 'react';
import slider1 from '../../images/sliders/bdn_banner_slider_shallyfat2.jpg';
import slider2 from '../../images/sliders/bdn_banner_slider_autodom.jpg';
import slider3 from '../../images/sliders/bdn_banner_slider_beschoice.jpg';
import * as ROUTE from '../../constants/routes'
import { Link } from 'react-router-dom';

const @@ComponentName@@ = () => {
  return (
    <div id="default-carousel" data-carousel="slide" className="relative">

      <div className="overflow-hidden relative h-screen wiw">

          <div className="hidden duration-700 ease-in-out md:grid justify-center items-center" data-carousel-item="active">
              <img src={slider1} className="block absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 luday_slider" alt="..." title="Slider 1" />
              <Link to={`${ROUTE.PRODUCTS}`} className="relative text-white px-8 py-3 rounded-md font-bold text-[13px]
                  tracking-wide bg-[#9c0]">@@cta@@</Link>
          </div>

          <div className="hidden duration-700 ease-in-out" data-carousel-item="">
              <img src={slider2} className="block absolute top-1/2 left-1/2 w-full -translate-x-1/2 -translate-y-1/2 luday_slider" alt="..." />
          </div>

          <div className="hidden duration-700 ease-in-out" data-carousel-item="">
              <img src={slider3} className="block absolute top-1/2 left-1/2 w-full -translate-x-1/2 -translate-y-1/2 luday_slider" alt="..." />
          </div>

      </div>

      <div className="flex absolute bottom-5 left-1/2 space-x-3 -translate-x-1/2">
          <button type="button" className="w-3 h-3 bg-white rounded-full dark:bg-gray-800" aria-current="true" aria-label="Slide 1" data-carousel-slide-to="0"></button>
          <button type="button" className="w-3 h-3 rounded-full bg-white/50 dark:bg-gray-800/50 hover:bg-white dark:hover:bg-gray-800" aria-current="false" aria-label="Slide 2" data-carousel-slide-to="1"></button>
          <button type="button" className="w-3 h-3 rounded-full bg-white/50 dark:bg-gray-800/50 hover:bg-white dark:hover:bg-gray-800" aria-current="false" aria-label="Slide 3" data-carousel-slide-to="2"></button>
      </div>

      <button type="button" className="flex absolute top-0 left-0 justify-center items-center px-4 h-full cursor-pointer group focus:outline-none" data-carousel-prev>
          <span className="inline-flex justify-center items-center w-8 h-8 rounded-full sm:w-10 sm:h-10 bg-white/30 dark:bg-gray-800/30 group-hover:bg-white/50 dark:group-hover:bg-gray-800/60 group-focus:ring-4 group-focus:ring-white dark:group-focus:ring-gray-800/70 group-focus:outline-none">
              <svg className="w-5 h-5 text-white sm:w-6 sm:h-6 dark:text-gray-800" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M15 19l-7-7 7-7"></path></svg>
              <span className="hidden">@@PreviousSliderText@@</span>
          </span>
      </button>
      <button type="button" className="flex absolute top-0 right-0 justify-center items-center px-4 h-full cursor-pointer group focus:outline-none" data-carousel-next>
          <span className="inline-flex justify-center items-center w-8 h-8 rounded-full sm:w-10 sm:h-10 bg-white/30 dark:bg-gray-800/30 group-hover:bg-white/50 dark:group-hover:bg-gray-800/60 group-focus:ring-4 group-focus:ring-white dark:group-focus:ring-gray-800/70 group-focus:outline-none">
              <svg className="w-5 h-5 text-white sm:w-6 sm:h-6 dark:text-gray-800" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 5l7 7-7 7"></path></svg>
              <span className="hidden">@@NextSliderText@@</span>
          </span>
      </button>
  </div>
  )
}

export default @@ComponentName@@
 """
 sliders["slide_1"] = slide_1
 
 
 """
 Slider 2 Component goes in here
 """
 slide_2 ="""

 """
 sliders["slide_2"] = slide_2
 '''
 

 '''
 