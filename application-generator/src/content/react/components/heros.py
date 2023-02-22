class Heros:

 heros = {}
 
 '''
 

 '''
 hero_1 ="""
import React from 'react';
import { Link } from 'react-router-dom';

const Hero1 = () => {
    return (
    <section className="flex items-center justify-center h-20">
        <div className="text-center">
            <p className="text-xl font-medium tracking-wider text-gray-300">Lorem ipsum dolor</p>
            <h2 className="mt-6 text-3xl font-bold text-white md:text-5xl">Lorem ipsum dolor sit amet, consectetur
                adipiscing elit</h2>

            <div className="flex justify-center mt-8">
                <Link className="px-8 py-2 text-lg font-medium text-white transition-colors duration-300 transform bg-indigo-600 rounded hover:bg-indigo-500"
                    to="/">Get In Touch</Link>
            </div>
        </div>
    </section>
    );
}
export default Hero1;
 """
 heros["hero_1"] = hero_1
 
 '''
 

 '''
 hero_2 ="""
import React from 'react';
import { Link } from 'react-router-dom';

const Hero2 = () => {
    return (
        <section>
            <div className="bg-black text-white py-20">
                <div className="container mx-auto flex flex-col md:flex-row items-center my-12 md:my-24">
                    <div className="flex flex-col w-full lg:w-1/3 justify-center items-start p-8">
                        <h1 className="text-3xl md:text-5xl p-2 text-yellow-300 tracking-loose">TechFest</h1>
                        <h2 className="text-3xl md:text-5xl leading-relaxed md:leading-snug mb-2">Space : The Timeless Infinity
                        </h2>
                        <p className="text-sm md:text-base text-gray-50 mb-4">Explore your favourite events and
                            register now to showcase your talent and win exciting prizes.</p>
                        <a href="#"
                            className="bg-transparent hover:bg-yellow-300 text-yellow-300 hover:text-black rounded shadow hover:shadow-lg py-2 px-4 border border-yellow-300 hover:border-transparent">
                            @@CallToAction@@</a>
                    </div>
                    <div className="p-8 mt-12 mb-6 md:mb-0 md:mt-0 ml-0 md:ml-12 lg:w-2/3  justify-center">
                        <div className="h-48 flex flex-wrap content-center">
                            <div>
                                <img className="inline-block mt-28 hidden xl:block" src="https://user-images.githubusercontent.com/54521023/116969935-c13d5b00-acd4-11eb-82b1-5ad2ff10fb76.png" /></div>
                                <div>
                                    <img className="inline-block mt-24 md:mt-0 p-8 md:p-0"  src="https://user-images.githubusercontent.com/54521023/116969931-bedb0100-acd4-11eb-99a9-ff5e0ee9f31f.png" /></div>
                                    <div>
                                        <img className="inline-block mt-28 hidden lg:block" src="https://user-images.githubusercontent.com/54521023/116969939-c1d5f180-acd4-11eb-8ad4-9ab9143bdb50.png" /></div>
                                    </div>
                                </div>
                            </div>
            </div>
        </section>
    );
}
export default Hero2;
 """
 heros["hero_2"] = hero_2
 
 '''
 

 '''
 hero_3 ="""
import React from 'react';
import { Typewriter } from 'react-simple-typewriter';
import { Link } from 'react-router-dom';
@@importPackage@@

/*This Component requires react-simple-Typewriter, to install run the following command:
    - npm install react-simple-typewriter 

*/

const bgImg = {
    background: `url(https://luday.se/img/hero-bg.png) top center no-repeat`,
    backgroundSize: `cover`
};

const word = [
    'Developers',
    'Designers',
    'Digital Marketers',
    'Product Managers',
];

function Hero3() {
    return (
        <div>
            <div style={bgImg}>
                <div>
                    <Navbar1 />
                </div>
                
                <div className="m-auto max-w-6xl p-2 md:p-12 h-5/6">

                    <div className="flex flex-col lg:flex-row mt-16 py-12 justify-between text-center lg:text-left">
                        <div className="lg:w-1/2 flex flex-col justify-center">
                            <div className="mb-5 md:text-4xl text-3xl font-bold text-blue-900">We offer modern solutions for your business</div>
                            <div className="text-xl font-semibold tracking-tight mb-5 text-gray-500">We are a team of talented <br className="block lg:hidden" /><span className="text-blue-900">
                                <Typewriter
                                    words={word}
                                    loop = {0}
                                    cursor
                                    cursorStyle='|'
                                    typeSpeed={70}
                                    deleteSpeed={50}
                                    delaySpeed={1000}
                                    
                                />
                            </span></div>
                            <div className="my-8 h-16">
                            <Link to="/" className="shadow-2xl font-medium py-3 px-2 md:px-8 text-white cursor-pointer bg-blue-700 rounded-md text-lg text-center w-72"> 
                                <span>Discover our services </span> 
                            </Link>
                            </div>
                        </div>
                        <div className="flex lg:justify-end w-full lg:w-1/2 -mt-5">
                            <img alt="card img" className="rounded-t float-right" src="https://luday.se/img/luday-mockup.png" />

                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Hero3;
 """
 heros["hero_3"] = hero_3


 hero_4 ="""
import React from 'react'
import 'tw-elements';

const Slider = () => {
  return (
    <>
        <div id="carouselDarkVariant" className="carousel slide carousel-fade carousel-dark relative" data-bs-ride="carousel">
            <div className="carousel-indicators absolute right-0 bottom-0 left-0 flex justify-center p-0 mb-4">
                <button data-bs-target="#carouselDarkVariant" data-bs-slide-to="0" className="active" aria-current="true" aria-label="Slide 1"></button>
                <button data-bs-target="#carouselDarkVariant" data-bs-slide-to="1" aria-label="Slide 1"></button>
                <button data-bs-target="#carouselDarkVariant" data-bs-slide-to="2" aria-label="Slide 1"></button>
            </div>
            <div className="carousel-inner relative w-full overflow-hidden">
                <div className="carousel-item active relative float-left w-full">
                    <img src="https://mdbcdn.b-cdn.net/img/Photos/Slides/img%20(19).webp" className="block w-full" alt="Motorbike Smoke"/>
                    <div className="carousel-caption hidden md:block absolute text-center">
                        <h5 className="text-xl">First slide label</h5>
                        <p>Some representative placeholder content for the first slide.</p>
                    </div>
                </div>
                <div className="carousel-item relative float-left w-full">
                    <img src="https://mdbcdn.b-cdn.net/img/Photos/Slides/img%20(35).webp" className="block w-full" alt="Mountaintop"/>
                    <div className="carousel-caption hidden md:block absolute text-center">
                        <h5 className="text-xl">Second slide label</h5>
                        <p>Some representative placeholder content for the second slide.</p>
                    </div>
                </div>
                <div className="carousel-item relative float-left w-full">
                <img src="https://mdbcdn.b-cdn.net/img/Photos/Slides/img%20(40).webp" className="block w-full" alt="Woman Reading a Book"/>
                    <div className="carousel-caption hidden md:block absolute text-center">
                        <h5 className="text-xl">Third slide label</h5>
                        <p>Some representative placeholder content for the third slide.</p>
                    </div>
                </div>
            </div>
        
            {/* <button
                className="carousel-control-prev absolute top-0 bottom-0 flex items-center justify-center p-0 text-center border-0 hover:outline-none hover:no-underline focus:outline-none focus:no-underline left-0" type="button" data-bs-target="#carouselDarkVariant" data-bs-slide="prev">
                <span className="carousel-control-prev-icon inline-block bg-no-repeat" aria-hidden="true"></span>
                <span className="visually-hidden">Previous</span>
            </button>
            <button
                className="carousel-control-next absolute top-0 bottom-0 flex items-center justify-center p-0 text-center border-0 hover:outline-none hover:no-underline focus:outline-none focus:no-underline right-0" type="button" data-bs-target="#carouselDarkVariant" data-bs-slide="next">
                <span className="carousel-control-next-icon inline-block bg-no-repeat" aria-hidden="true"></span>
                <span className="visually-hidden">Next</span>
            </button> */}
        </div>
    </>
  )
}

export default Slider
 """
 heros["hero_4"] = hero_4


 hero_5 ="""
import React from 'react';
import Slider1 from './images/sliders/bdn_banner_slider_shallyfat2.jpg';
import Slider2 from './images/sliders/bdn_banner_slider_autodom.jpg';
import Slider3 from './images/sliders/bdn_banner_slider_beschoice.jpg';
import { Link } from 'react-router-dom';

function Hero5() {
  return (
    <div id="default-carousel" data-carousel="slide" className="relative">

      <div className="overflow-hidden relative h-screen wiw">

          <div className="hidden duration-700 ease-in-out grid justify-center items-center" data-carousel-item="active">
              <img src={Slider1} className="block absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 luday_slider" alt="..." title="Slider 1" />
              <Link to="/products" className="relative text-white px-8 py-3 rounded-md font-bold text-[13px]
                  tracking-wide bg-[#9c0]">@@sider1text1@@</Link>
          </div>

          <div className="hidden duration-700 ease-in-out" data-carousel-item="">
              <img src={Slider2} className="block absolute top-1/2 left-1/2 w-full -translate-x-1/2 -translate-y-1/2 luday_slider" alt="..." />
          </div>

          <div className="hidden duration-700 ease-in-out" data-carousel-item="">
              <img src={Slider3} className="block absolute top-1/2 left-1/2 w-full -translate-x-1/2 -translate-y-1/2 luday_slider" alt="..." />
          </div>

      </div>

      <div className="flex absolute bottom-5 left-1/2 space-x-3 -translate-x-1/2">
          <button type="button" className="w-3 h-3 bg-white rounded-full dark:bg-gray-800" aria-current="true" aria-label="Slide 1" data-carousel-slide-to="0"></button>
          <button type="button" className="w-3 h-3 rounded-full bg-white/50 dark:bg-gray-800/50 hover:bg-white dark:hover:bg-gray-800" aria-current="false" aria-label="Slide 2" data-carousel-slide-to="1"></button>
          <button type="button" className="w-3 h-3 rounded-full bg-white/50 dark:bg-gray-800/50 hover:bg-white dark:hover:bg-gray-800" aria-current="false" aria-label="Slide 3" data-carousel-slide-to="2"></button>
      </div>

      <button type="button" className="flex absolute top-0 left-0 justify-center items-center px-4 h-full cursor-pointer group focus:outline-none" data-carousel-prev>
          <span className="inline-flex justify-center items-center w-8 h-8 rounded-full sm:w-10 sm:h-10 bg-white/30 dark:bg-gray-800/30 group-hover:bg-white/50 dark:group-hover:bg-gray-800/60 group-focus:ring-4 group-focus:ring-white dark:group-focus:ring-gray-800/70 group-focus:outline-none">
              <svg className="w-5 h-5 text-white sm:w-6 sm:h-6 dark:text-gray-800" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path></svg>
              <span className="hidden">Previous</span>
          </span>
      </button>
      <button type="button" className="flex absolute top-0 right-0 justify-center items-center px-4 h-full cursor-pointer group focus:outline-none" data-carousel-next>
          <span className="inline-flex justify-center items-center w-8 h-8 rounded-full sm:w-10 sm:h-10 bg-white/30 dark:bg-gray-800/30 group-hover:bg-white/50 dark:group-hover:bg-gray-800/60 group-focus:ring-4 group-focus:ring-white dark:group-focus:ring-gray-800/70 group-focus:outline-none">
              <svg className="w-5 h-5 text-white sm:w-6 sm:h-6 dark:text-gray-800" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
              <span className="hidden">Next</span>
          </span>
      </button>
  </div>
  )
}

export default Hero5;
 """
 heros["hero_5"] = hero_5