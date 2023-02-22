class FeaturedProducts:

 featured_products = {}

 '''
 

 '''
 index ="""
import React, { useState, useEffect } from 'react';
// import bdn_spa_beschoice from '../../../images/products/bdn_spa_beschoice.jpg';
import * as ROUTE from '../../../constants/routes'
import { Link } from 'react-router-dom';
import SwiperCore, { Autoplay, Navigation } from 'swiper/core';
import { Swiper, SwiperSlide } from "swiper/react";
import 'swiper/css';
import 'swiper/css/navigation';
import './featuredCard.css';
import * as CONSTANT from '../../../constants/constants'
{/* @TODO: Make products image to be a slider  */} 

SwiperCore.use([Navigation, Autoplay]);
function @@ComponentName@@(){
    const [products, fetchProducts] = useState([]);
    const nf = new Intl.NumberFormat();
    const getData = () => {
        fetch(`${ROUTE.PRODUCTS_API}/products/featured`)
          .then((res) => res.json())
          .then((res) => {
            fetchProducts(res.results)
          })
      }
  
      useEffect(() => {
          getData()
      }, [])

    let featuredProducts;
    if (products.length > 0) {
        featuredProducts = <Swiper 
            breakpoints={{
                0: {
                    slidesPerView: 1
                },
                480: {
                    slidesPerView: 2
                },
                768: {
                    slidesPerView: 3
                },
                1024: {
                    slidesPerView: 4
                }
            }}
            tag="section"
            wrapperTag="ul"
            slidesPerView={4} 
            loop={true} autoplay={{delay: 3500, disableOnInteraction: false}} navigation={true} className="mx-auto ">
            { products?.map(product =>
                <SwiperSlide className="" key={product.id} tag="li">
                    <div className="group bg-white mx-auto px-0 py-2 shadow-md ">
                        <div className='products '>
                            <Link to={`${ROUTE.PRODUCT_DETAILS}/${product.slug}`} state={product}>
                                <div className="p-[10px] pb-[5px] ">
                                    <img className="lazy h-60 w-full" src={`${CONSTANT.IMAGE_STORE}/${product.image_path}`} alt="" />            
                                    <div className="gis-text text-center overflow-hidden w-full h-12 pt-4">
                                        <p className="text-lg md:text-xl lg:text-xl font-bold overflow-hidden text-ellipsis whitespace-nowrap px-3">{product.name}</p>
                                        <div className="row text-center">
                                            <p className="text-md font-medium order-first text-bold text-center">
                                                {product.sale_price ? (
                                                    <span>&#8358;{nf.format(product.sale_price)}</span>
                                                ) : (<span><br/></span>)
                                                } &nbsp;  
                                                <span className={
                                                product.sale_price ? "line-through font-light text-center text-sm mr-1 text-gray-500" : "" }>
                                                    &#8358;{nf.format(product.price)}
                                                </span>
                                            </p>
                                        </div>
                                    </div>
                                </div>
                            </Link>
                        </div> 
                    </div>
                </SwiperSlide>
            ) }
        </Swiper>
    }
    else {
        featuredProducts = (
            <h1 className="text-4xl">No featured products</h1>
        )
    }

    return (
      <>        
        <div className="px-10 luday_wrap">
            <div className="text-center py-10 pt-14">
            <p className="tracking-widest text-xs text-gray-500">@@Preheadertext@@</p>
            <h3 className="text-6xl luday_deals">@@HeaderText3@@</h3>
            </div>
        </div>
        <section className="bg-gray-50 ">
            <div className="px-3 md:px-10 lg:px-24 py-[30px] luday_wrap text-center">
                { featuredProducts }
            </div>
        </section>
        
    </>
    )
}
export default @@ComponentName@@
 """
 featured_products["index"] = index
 
 '''
 

 '''
 product ="""

 """
 featured_products["product"] = product
 '''
 

 '''
 