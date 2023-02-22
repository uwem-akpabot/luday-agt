class FindDeals:

 find_deal = {}

 '''
 

 '''
 deal ="""
import React, { useEffect, useState }  from 'react';
import { Link } from 'react-router-dom';

import { useDocumentTitle, useScrollTop } from '../../hooks';
import * as ROUTE from '../../constants/routes';
import * as CONSTANT from '../../constants/constants';

const @@PageName@@ = () => {
  useDocumentTitle('Find your deals in Nigeria | BestDealNaija');
  useScrollTop();

  const [categories, fetchcategories] = useState([]);
  const getData = () => {
    fetch(`${ROUTE.PRODUCTS_API}/categories`)
      .then((res) => res.json())
      .then((res) => {
        fetchcategories(res.results)
      })
  }

  useEffect(() => {
      getData()
  }, [])

  return (
    <div className=''>
      <div className="px-10 luday_wrap mb-10 ">
          <div className="text-center py-7 mt-7 md:mt-30">
            <p className="tracking-widest text-xs text-gray-500">@@Preheadertext@@</p>
            <h3 className="text-6xl luday_deals">@@HeaderText@@</h3>
          </div>

          <div className="w-full grid grid-cols-1 gap-4 md:grid-cols-5 md:gap-7 ">
          {categories && (
              categories.map(category =>
              <div className="group" key={category.id}>
                  <div className='products'>
                      <Link to={`${ROUTE.CATEGORY_PRODUCTS}/${category.slug}`} className="luday_grid_links">
                      <h4 className="luday_grid_texts" >{category.name}</h4>
                      <div className='find_deal_bg'></div>
                      {/* <img src={slider2} className="luday_grid_images" /> */}
                      <img src={`${CONSTANT.IMAGE_STORE}/${category.image_path}`} className="luday_grid_images" />
                      </Link>
                      
                  </div> 
              </div>
            )
          )}
          </div>
      </div>
    </div>
  )
}
export default @@PageName@@;
 """
 find_deal["deal"] = deal
 
 '''
 

 '''
 # ludayab
 deal_1 ="""
import React  from 'react';
const @@PageName@@ = () => {
   return(
    <>
        <section className="overflow-hidden bg-gray-50 sm:grid sm:grid-cols-2 sm:items-center">
            <div className="p-8 md:p-12 lg:px-16 lg:py-24">
                <div className="mx-auto max-w-xl text-center sm:text-left">
                <h2 className="text-2xl font-bold text-gray-900 md:text-3xl">
                    Cant wait to build the next Big Thing?
                </h2>

                <p className="hidden text-gray-500 md:mt-4 md:block">
                We take responsibility for building customized software solutions to help transform your business activities and increase productivity
                </p>

                <div className="mt-4 md:mt-8">
                    <button className="px-8 py-4 font-medium tracking-wide text-white capitalize transition-colors duration-300 transform bg-blue-600 rounded-lg hover:bg-blue-500 focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-80">
                        Request a quote
                    </button>
                </div>
                </div>
            </div>

            <img
                alt="Violin"
                src="https://images.unsplash.com/photo-1610563166150-b34df4f3bcd6?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=776&q=80"
                className="h-full w-full object-cover sm:h-[calc(100%_-_2rem)] sm:self-end sm:rounded-tl-[30px] md:h-[calc(100%_-_4rem)] md:rounded-tl-[60px]"
            />
            </section>

        </>
  )
}
export default @@PageName@@;
 """
 find_deal["deal_1"] = deal_1
 