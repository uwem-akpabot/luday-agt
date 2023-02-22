class Intros:

 intros = {}
 
 '''
 

 '''
 intro_1 ="""
import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import Slider from "react-slick";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import slick from 'slick-carousel/slick/slick';

/* Component requires 
    - react-router-dom
    - react-slick
    - slick-carousel
    - jquery

    - To install the packages needed to make this component fully functional and responsive, run the command below:
    
    npm install react-router-dom react-slick slick-carousel jquery  
*/


const images = [
    {
      id: 1,
      src:
        "https://luday.se/img/about.png",
      alt: "The world"
    },
    {
      id: 2,
      src:
        "https://luday.se/img/digital-marketing.png",
      alt: "Train"
    },
    {
      id: 3,
      src:
        "https://luday.se/img/project-manage.png",
      alt: "Laptop"
    },
    {
        id: 4,
        src:
          "https://luday.se/img/laravel-coding.png",
        alt: "Laptop"
      }
];

const imgNavigationStyle = {
    height: `120px`,
    width: `100%`
}


const settings = {
    customPaging: function (i) {
        return (
          <a>
            <img
              src={images[i].src} 
              className="rounded" style={imgNavigationStyle}
              alt={images[i].alt}
            />
          </a>
        );
    },
    infinite: true,
    dots: true,
    dotsClass: "slick-dots slick-thumb",
    slidesToShow: 1,
    autoplay: true,
    autoplaySpeed: 2000,
    cssEase: "linear",
    arrows: true,
    slidesToScroll: 1,
    lazyLoad: true
};

const Tabs = ({ color }) => {
    const [openTab, setOpenTab] = useState(1);
    return (
      <>
        <div className="flex">
          <div className="w-screen">
            <ul
              className="flex list-none pt-5 flex-row border-b border-gray-300"
              role="tablist"
            >
              <li className="-mb-px mr-2 last:mr-0 flex-auto text-center">
                <a
                  className={
                    "text-sm pb-2 font-bold uppercase block leading-normal " +
                    (openTab === 1
                      ? "text-" + color + "-600 border-b-4 border-" + color + "-600"
                      : "text-blue-900 bg-white")
                  }
                  onClick={e => {
                    e.preventDefault();
                    setOpenTab(1);
                  }}
                  data-toggle="tab"
                  href="#link1"
                  role="tablist"
                >
                  About Us
                </a>
              </li>
              <li className="-mb-px mr-2 last:mr-0 flex-auto text-center">
                <a
                  className={
                    "text-sm pb-2 font-bold uppercase block leading-normal " +
                    (openTab === 2
                      ? "text-" + color + "-600 border-b-4 border-" + color + "-600"
                      : "text-blue-900 bg-white")
                  }
                  onClick={e => {
                    e.preventDefault();
                    setOpenTab(2);
                  }}
                  data-toggle="tab"
                  href="#link2"
                  role="tablist"
                >
                   Our Mission
                </a>
              </li>
              <li className="-mb-px last:mr-0 flex-auto text-center">
                <a
                  className={
                    "text-sm pb-2 font-bold  uppercase block leading-normal " +
                    (openTab === 3
                      ? "text-" + color + "-600 border-b-4 border-" + color + "-600"
                      : "text-blue-900 bg-white")
                  }
                  onClick={e => {
                    e.preventDefault();
                    setOpenTab(3);
                  }}
                  data-toggle="tab"
                  href="#link3"
                  role="tablist"
                >
                   Our Vision
                </a>
              </li>
            </ul>
            <div className="relative flex flex-col min-w-full break-words bg-white w-full mb-6 text-blue-900 text-justify">
              <div className="px-4 py-5 flex-auto">
                <div className="tab-content tab-space">
                  <div className={openTab === 1 ? "block" : "hidden"} id="link1">
                    <p>
                        @@OurGoal@@
                    </p>
                  </div>
                  <div className={openTab === 2 ? "block" : "hidden"} id="link2">
                    <p>
                        @@OurMission@@
                    </p>
                  </div>
                  <div className={openTab === 3 ? "block" : "hidden"} id="link3">
                    <p>
                        @@OurVision@@
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </>
    );
  };

function Intro1() {
    return (
        <div className='mb-5 pb-5'>
            <div className="m-auto max-w-6xl p-4 h-4/5">

                <div className="flex flex-col-reverse lg:flex-row justify-between">
                  <div className="lg:w-3/5 mt-6 lg:max-w-xl hidden md:block flex flex-col justify-center">
                      <Slider {...settings}> 
                          {images.map((item) => (
                              <div key={item.id}>
                                  <img src={item.src} className='rounded-md h-72 md:h-96 w-full' alt={item.alt}/>
                              </div>
                          ))}
                      </Slider>
                      </div>
                      <div className="lg:w-2/5 lg:max-w-xl px-6 md:px-2 md:mr-6 text-center lg:text-justify">
                          <div>
                              <h2 className='uppercase text-blue-900 font-bold text-4xl md:text-5xl mb-6 tracking-tighter'>Who we are</h2>
                              <h5 className='text-blue-900 text-3xl my-8'>We are an innovation-driven ICT company committed to giving the best solution to any business need</h5>
                          </div>
                          <div>
                              <Tabs color="indigo" />
                          </div>
                          <div className='flex justify-center lg:justify-start'>
                            <Link to="/" className='bg-blue-700 mt-4 py-3 px-16 text-white rounded-md font-semibold text-md tracking-wide'>Read More</Link>
                          </div>
                          
                      </div> 
                  </div>
            </div>
        </div>
    )
}

export default Intro1;
 """
 intros["intro_1"] = intro_1

# Add intro ludayab
 intro_2 ="""
import {React, useState} from 'react'
import { Link } from 'react-router-dom'
import {  BookOpenIcon, LightBulbIcon, ArrowRightIcon } from '@heroicons/react/20/solid'


const About = (color) => {
  const [openTab, setOpenTab] = useState(1);
  return (
    <div className="overflow-hidden bg-white py-24 sm:py-32">
      <div className="mx-auto max-w-7xl px-6 lg:px-8">
        <div className="mx-auto grid max-w-2xl grid-cols-1 gap-y-16 gap-x-8 sm:gap-y-20 lg:mx-0 lg:max-w-none lg:grid-cols-2">
          <div className="lg:pr-8 lg:pt-4">
            <div className="lg:max-w-lg">
              <h2 className="text-lg font-semibold leading-8 tracking-tight text-blue-600">@@Heading1@@</h2>
              <p className="mt-2 text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">@@Heading2@@</p>
              <p className="my-6 text-lg leading-8 text-gray-600">
               @@Paragraph1@@
              </p>
              <div className="flex">
                <div className="w-screen">
                  <ul className="flex list-none pt-5 flex-row border-b border-gray-300"role="tablist">
                    <li className="-mb-px mr-2 last:mr-0 flex-auto text-center">
                      <a className={"text-sm pb-2 font-bold uppercase leading-normal flex items-center " +
                          (openTab === 1
                            ? "text-" + color + "-600 border-b-4 border-" + color + "-600"
                            : "text-blue-900 bg-white")
                        }
                        onClick={e => {
                          e.preventDefault();
                          setOpenTab(1);
                        }}
                        data-toggle="tab"
                        href="#link1"
                        role="tablist"
                      >
                        <BookOpenIcon className="h-5 w-5 text-blue-600" aria-hidden="true" />@@Heading3@@
                      </a>
                    </li>
                    <li className="-mb-px mr-2 last:mr-0 flex-auto text-center">
                      <a
                        className={"text-sm pb-2 font-bold uppercase  leading-normal flex items-center " +
                          (openTab === 2
                            ? "text-" + color + "-600 border-b-4 border-" + color + "-600"
                            : "text-blue-900 bg-white")
                        }
                        onClick={e => {
                          e.preventDefault();
                          setOpenTab(2);
                        }}
                        data-toggle="tab"
                        href="#link2"
                        role="tablist"
                      >
                        <LightBulbIcon className="h-5 w-5 text-blue-600" aria-hidden="true" />
                        @@Heading4@@
                      </a>
                    </li>
                    
                  </ul>
                  <div className="relative flex flex-col min-w-full break-words bg-white w-full mb-6 text-blue-900 text-justify">
                    <div className="px-4 py-5 flex-auto">
                      <div className="tab-content tab-space">
                        <div className={openTab === 1 ? "block" : "hidden"} id="link1">
                          <p>
                              @@Paragraph2@@
                          </p>
                        </div>
                        <div className={openTab === 2 ? "block" : "hidden"} id="link2">
                          <p>
                              @@Paragraph3@@
                          </p>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div className='flex justify-center lg:justify-start'>
                <Link to="/" className='bg-blue-700 mt-4 py-3 px-16 text-white rounded-md font-semibold text-md tracking-wide flex items-center' > @@CallToAction1@@ <ArrowRightIcon className="h-5 w-5 text-white" aria-hidden="true" /></Link>
              </div>
            </div>
          </div>
          <img src="https://tailwindui.com/img/component-images/dark-project-app-screenshot.png" alt="Product screenshot" className="h-[28rem] md:h-[48rem] rounded-xl shadow-xl ring-1 ring-gray-400/10"/>
        </div>
        <div className='-mt-40 mr-5 md:mr-0 flex flex-col md:flex-row'>
          <div className='ml-5 md:ml-5 lg:-ml-10 w-full md:w-2/5 m-5 bg-white h-auto shadow-md'>
            <div className='bg-blue-400 h-3'></div>
              <h3 className="p-6 text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">@@Heading5@@</h3>
              <p className='px-5'>@@Paragraph4@@</p>
              <div className='m-5 flex justify-center lg:justify-start'>
                <Link to="/" className='bg-blue-700 mt-4 py-3 px-16 text-white rounded-md font-semibold text-md tracking-wide flex items-center' > @@CallToAction2@@ <ArrowRightIcon className="h-5 w-5 text-white" aria-hidden="true" /></Link>
              </div>
          </div>
          <div className='w-full md:w-3/5 m-5  bg-white h-auto shadow-md'>
            <div className='bg-blue-400 h-3'></div>
            <h3 className="p-6 text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">@@Heading6@@</h3>
              <p className='px-5'>@@Paragraph5@@<br/><br/></p>
              <div className='m-5 flex justify-center lg:justify-start'>
                <Link to="/" className='bg-blue-700 mt-4 py-3 px-16 text-white rounded-md font-semibold text-md tracking-wide flex items-center' > @@CallToAction3@@ <ArrowRightIcon className="h-5 w-5 text-white" aria-hidden="true" /></Link>
              </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default About
 """
 intros["intro_2"] = intro_2

# Add intro 3
 intro_3 ="""

 """
 intros["intro_3"] = intro_3

# Add intro 4
 intro_4 ="""

 """
 intros["intro_4"] = intro_4

# Bestdealnaija
 intro_5 ="""
import React from 'react';
import { Link } from 'react-router-dom';
import Spa_image from './images/deals/bdn_spa.jpg';
import Entertainment_image from './images/deals/img_0079.jpg';
import Fashion_image from './images/deals/ankara-fabric.jpg';
import Fragrance_image from './images/deals/antonin-fels-726121-unsplash.jpg';
import Hotels_image from './images/deals/bdn_hotels2.jpg';
import Restaurants_image from './images/deals/bdn_restaurant.jpg';
import Education_image from './images/deals/bdn_education.jpg';
import Travels_image from './images/deals/bdn_travels.jpg';
import RealEstate_image from './images/deals/bdn_real_estate.jpg';
import FoodStores_image from './images/deals/bdn_food_stores.jpg';
import Electronic_image from './images/deals/bdn_electronic_gadgets.jpg';
import Home_image from './images/deals/bdn_homes.jpg';
import Automobiles_image from './images/deals/bdn_automobile2.jpg';

function Intro5(){
    return (
      <div className="px-10 luday_wrap">

        <div className="text-center py-10 mt-20 md:mt-40">
          <p className="tracking-widest text-xs text-gray-500">@@PreheaderText@@</p>
          <h3 className="text-6xl luday_deals">@@HeaderText@@</h3>
        </div>

        <div className="grid grid-cols-1 gap-4 md:grid-cols-5 md:gap-9 ">
          <div className="group">
            <Link to="/products" className="luday_grid_links">
              <h4 className="luday_grid_texts">@@DealsHeader1@@</h4>
              <img src={Spa_image} className="luday_grid_images" />
            </Link>
          </div>
          <div className="group">
            <Link to="/products" className="luday_grid_links">
              <h4 className="luday_grid_texts">@@DealsHeader2@@</h4>
              <img src={Entertainment_image} className="luday_grid_images" />
            </Link>
          </div>
          <div className="group">
            <Link to="/products" className="luday_grid_links">
              <h4 className="luday_grid_texts">@@DealsHeader3@@</h4>
              <img src={Fashion_image} className="luday_grid_images" />
            </Link>
          </div>
          <div className="group">
            <Link to="/products" className="luday_grid_links">
              <h4 className="luday_grid_texts">@@DealsHeader4@@</h4>
              <img src={Fragrance_image} className="luday_grid_images" />
            </Link>
          </div>
          <div className="group">
            <Link to="/products" className="luday_grid_links">
              <h4 className="luday_grid_texts">@@DealsHeader5@@</h4>
              <img src={Hotels_image} className="luday_grid_images" />
            </Link>
          </div>
          <div className="group">
            <Link to="/products" className="luday_grid_links">
              <h4 className="luday_grid_texts">@@DealsHeader6@@</h4>
              <img src={Restaurants_image} className="luday_grid_images" />
            </Link>
          </div>
          <div className="group">
            <Link to="/products" className="luday_grid_links">
              <h4 className="luday_grid_texts">@@DealsHeader7@@</h4>
              <img src={Education_image} className="luday_grid_images" />
            </Link>
          </div>
          <div className="group">
            <Link to="/products" className="luday_grid_links">
              <h4 className="luday_grid_texts">@@DealsHeader8@@</h4>
              <img src={Travels_image} className="luday_grid_images" />
            </Link>
          </div>
          <div className="group">
            <Link to="/products" className="luday_grid_links">
              <h4 className="luday_grid_texts">@@DealsHeader9@@</h4>
              <img src={RealEstate_image} className="luday_grid_images" />
            </Link>
          </div>
          <div className="group">
            <Link to="/products" className="luday_grid_links">
              <h4 className="luday_grid_texts">@@DealsHeader10@@</h4>
              <img src={FoodStores_image} className="luday_grid_images" />
            </Link>
          </div>
          <div className="group">
            <Link to="/products" className="luday_grid_links">
              <h4 className="luday_grid_texts">@@DealsHeader11@@</h4>
              <img src={Electronic_image} className="luday_grid_images" />
            </Link>
          </div>
          <div className="group">
            <Link to="/products" className="luday_grid_links">
              <h4 className="luday_grid_texts">@@DealsHeader12@@</h4>
              <img src={Home_image} className="luday_grid_images" />
            </Link>
          </div>
          <div className="group">
            <Link to="/products" className="luday_grid_links">
              <h4 className="luday_grid_texts">@@DealsHeader13@@</h4>
              <img src={Automobiles_image} className="luday_grid_images" />
            </Link>
          </div>

        </div>
        </div>
    )
}
export default Intro5

 """
 intros["intro_5"] = intro_5 # Bestdealnaija

# Bestdealnaija
 intro_6 ="""
import React from 'react';
import bdn_spa_beschoice from './images/products/bdn_spa_beschoice.jpg';
import { Link } from 'react-router-dom';



function Intro6(){
    return (
      <>
      <div className="px-10 luday_wrap">
        <div className="text-center py-10 pt-20">
          <p className="tracking-widest text-xs text-gray-500">@@Preheadertext@@</p>
          <h3 className="text-6xl luday_deals">@@HeaderText@@</h3>
        </div>
      </div>
      <section className="bg-gray-100">
                    <div className="px-3 md:px-10 lg:px-36 py-[80px] pb-[80px] luday_wrap" >                    
                        <div class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-9" >
                            <div className="group bg-white">
                                <article>
                                    <div>
                                        <Link to="/product-details"><img className="lazy" src={bdn_spa_beschoice} alt="" /></Link>
                                    </div>
                                    <div className="p-[30px]">
                                        <div className="gis-text">
                                            <Link to="/product-details"><h2 className="text-2xl font-semibold">@@ProductTitle@@</h2></Link>
                                          </div>
                                    </div>
                                </article>
                            </div>
                            <div className="group bg-white">
                                <article>
                                    <div>
                                        <Link to="/product-details"><img className="lazy" src={bdn_spa_beschoice} alt="" /></Link>
                                    </div>
                                    <div className="p-[30px]">
                                        <div className="gis-text">
                                            <Link to="/product-details"><h2 className="text-2xl font-semibold">@@ProductTitle@@</h2></Link>
                                          </div>
                                    </div>
                                </article>
                            </div>
                            <div className="group bg-white">
                                <article>
                                    <div>
                                        <Link to="/product-details"><img className="lazy" src={bdn_spa_beschoice} alt="" /></Link>
                                    </div>
                                    <div className="p-[30px]">
                                        <div className="gis-text">
                                          <Link to="/product-details"><h2 className="text-2xl font-semibold">@@ProductTitle@@</h2></Link>
                                       </div>
                                    </div>
                                </article>
                            </div>
                            <div className="group bg-white">
                                <article>
                                    <div>
                                        <Link to="/product-details"><img className="lazy" src={bdn_spa_beschoice} alt="" /></Link>
                                    </div>
                                    <div className="p-[30px] flex flex-center">
                                        <div className="gis-text">
                                          <Link to="/product-details"><h2 className="text-2xl font-semibold">@@ProductTitle@@</h2></Link>
                                        </div>
                                    </div>
                                </article>
                            </div>
                        </div>
                    </div>
                </section>
        </>
    )
}
export default Intro6

 """
 intros["intro_6"] = intro_6 # Bestdealnaija
 