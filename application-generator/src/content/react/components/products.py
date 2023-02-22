class Products:

 products = {}
 
 '''
 

 '''
 product_1 ="""
    import React, {useState, useEffect} from 'react';
    import { Link } from 'react-router-dom';
    import bdn_spa_beschoice from './images/products/bdn_spa_beschoice.jpg';
    
    const Product1 = () => {
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

                <section className="bg-gray-100">
                    {units}
                </section>

                <section className="bg-gray-100">
                    <div className="px-3 md:px-10 lg:px-36 py-[50px] pb-[80px] luday_wrap">  
                        <div className="mb-5">
                            <form id="submitForm">
                                <div className="input-group flex items-center flex-nowrap">
                                    <input name="product_name" id="productName" type="search" className="form-control rounded w-full md:w-1/2 lg:w-1/3" placeholder="Search" aria-label="Search"
                                    aria-describedby="search-addon" />
                                    <button name="searchBtn" value="1" type="submit" className="bg-transparent hover:bg-yellow-500 text-green-700 font-semibold hover:text-white py-2 px-2 border border-green-500 hover:border-transparent rounded"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24"><path d="M19.023 16.977a35.13 35.13 0 0 1-1.367-1.384c-.372-.378-.596-.653-.596-.653l-2.8-1.337A6.962 6.962 0 0 0 16 9c0-3.859-3.14-7-7-7S2 5.141 2 9s3.14 7 7 7c1.763 0 3.37-.66 4.603-1.739l1.337 2.8s.275.224.653.596c.387.363.896.854 1.384 1.367l1.358 1.392.604.646 2.121-2.121-.646-.604c-.379-.372-.885-.866-1.391-1.36zM9 14c-2.757 0-5-2.243-5-5s2.243-5 5-5 5 2.243 5 5-2.243 5-5 5z"></path></svg></button>
                                </div>
                            </form>
                        </div>               
                        <hr className="text-sm pt-2" />
                        <div className="grid grid-cols-1 gap-4 md:grid-cols-4 lg:grid-cols-4">
                            <div className="group bg-white border-r-2 border-b-2 mx-0 px-0 py-2">
                               <Link to="/product-details">
                                <article className="p-[10px] pb-[5px]">
                                    <img className="lazy" src={bdn_spa_beschoice} alt="" />                                    
                                    <div className="gis-text pt-4">
                                        <p className="text-xl font-bold">@@ProductTitle@@</p>
                                        <p className="pb-2 text-base">&#8358;@@Price@@</p>
                                    </div>
                                </article>
                                </Link>
                                <div className="row px-[10px]">
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
                            </div>
                            <div className="group bg-white border-r-2 border-b-2 mx-0 px-0 py-2">
                                <Link to="/product-details">
                                <article className="p-[10px] pb-[5px]">
                                    <img className="lazy" src={bdn_spa_beschoice} alt="" />                                    
                                    <div className="gis-text pt-4">
                                        <p className="text-xl font-bold">@@ProductTitle@@</p>
                                        <p className="pb-2">&#8358;@@Price@@</p>
                                    </div>
                                </article>
                                </Link>
                                <div className="row px-[10px]">
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
                            </div>
                            <div className="group bg-white border-r-2 border-b-2 mx-0 px-0 py-2">
                               <Link to="/product-details">
                                <article className="p-[10px] pb-[5px]">
                                    <img className="lazy" src={bdn_spa_beschoice} alt="" />                                    
                                    <div className="gis-text pt-4">
                                        <p className="text-xl font-bold">@@ProductTitle@@</p>
                                        <p className="pb-2">&#8358;@@Price@@</p>
                                    </div>
                                </article>
                                </Link>
                                <div className="row px-[10px]">
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
                            </div>
                            <div className="group bg-white border-r-2 border-b-2 mx-0 px-0 py-2">
                               <Link to="/product-details">
                                <article className="p-[10px] pb-[5px]">
                                    <img className="lazy" src={bdn_spa_beschoice} alt="" />                                    
                                    <div className="gis-text pt-4">
                                        <p className="text-xl font-bold">@@ProductTitle@@</p>
                                        <p className="pb-2">&#8358;@@Price@@</p>
                                    </div>
                                </article>
                                </Link>
                                <div className="row px-[10px]">
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
                            </div>
                        </div>
                    </div>
                </section>
            </>
        );
    }

    export default Product1;
 """
 products["product_1"] = product_1


 """
 Add Product 2
 """
 product_2 ="""
import React, {useState, useEffect} from 'react';
const "@@ComponentName@@ = () => {

}

export default @@ComponentName@@;
 """
 products["product_2"] = product_2


 """
 ProductItem
 """
 product_item_1 ="""
import React, { useEffect } from 'react';
import { Link } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';

import PropType from 'prop-types';
import Skeleton, { SkeletonTheme } from 'react-loading-skeleton';
import 'react-loading-skeleton/dist/skeleton.css';

import { addQtyItem, addToCart, minusQtyItem } from '../../redux/actions/cartActions';
import * as ROUTE from '../../constants/routes';
import * as CONSTANT from '../../constants/constants';
import { displayMoney } from '../../helpers/utils'
import { setRequestStatus } from '../../redux/actions/miscActions';

const @@ComponentName@@ = ({ product }) => {
   const { cart } = useSelector((state) => ({
		cart: state.cart,
		requestStatus: state.app.requestStatus
	}));

	const productInCart = (productId) =>{
		if (cart) {
			return cart.filter((cartItem) => productId === cartItem.id);
		}
	};

	const dispatch = useDispatch();

	useEffect(() => {
        dispatch(setRequestStatus({}));
    }, []);

	const btnAddToCart = (product) => {
        dispatch(addToCart(product));
		dispatch(setRequestStatus({
			success: true,
			type: 'cart',
			isError: false,
			status: 'success',
			message: 'Added to cart.'
		}))
    }

	const btnIncreaseQtyCartList = (product) => {
		if(productInCart(product.id).length >= 1){
			const cartItem = productInCart(product.id)[0]
			const cart_quantity = cartItem['cart_quantity']
			const quantity = cartItem['quantity']
			if (cart_quantity < quantity) {
				dispatch(addQtyItem(cartItem['id']));
				dispatch(setRequestStatus({
					success: true,
					type: 'cart',
					isError: false,
					status: 'success',
					message: 'Quantity added.'
				}))
			}
		} else {
			dispatch(addToCart(product));
			dispatch(setRequestStatus({
				success: true,
				type: 'cart',
				isError: false,
				status: 'success',
				message: 'Added to cart.'
			}))
		}
    }

	const btnDecreaseQtyCartList = (product) => {
		if(productInCart(product.id).length >= 1){
			const cartItem = productInCart(product.id)[0]
			const cart_quantity = cartItem['cart_quantity']
			const quantity = cartItem['quantity']
			if ((quantity >= cart_quantity) && cart_quantity !== 0) {
				dispatch(minusQtyItem(cartItem['id']));
				dispatch(setRequestStatus({
					success: true,
					type: 'cart',
					isError: false,
					status: 'success',
					message: 'Quantity removed.'
				}))
			}
		}
    }

	return (
		<SkeletonTheme baseColor="#e1e1e1" highlightColor="#f2f2f2">
			<div className="place-self-stretch" key={product.id}>
				<div className="group mx-0 px-2 py-2">
					<div className='products '>
						<Link to={`${ROUTE.PRODUCT_DETAILS}/${product.slug}`} state={product}>
							<div className="pb-[5px] text-center bg-white shadow-xl">
								{product.name ? (
												<img className="lazy h-60 w-full" src={`${CONSTANT.IMAGE_STORE}/${product.image_path}`} alt={product.name} />
											): <Skeleton className='w-full' height={200} />}
								<div className="gis-text text-center pt-4 overflow-hidden w-full h-20">
									<p className="text-lg md:text-xl lg:text-xl font-bold overflow-hidden text-ellipsis whitespace-nowrap px-3">
										{product.name ? (
											product.name
										): <Skeleton className='w-full' height={50} />}
									</p>
									<div className="row text-center">
                                        <p className="text-md font-medium order-first text-bold text-center">
											{product.price ? (
                                                    <span>&#8358;{displayMoney(
														product.sale_price ? product.sale_price : product.price
													)}</span>
                                                ) : (<span><br/></span>)
                                            } &nbsp;
											{product.sale_price >= 1 && ( 
												<span className={"line-through font-light text-center text-sm mr-1 text-gray-500"}>
													<>&#8358;{displayMoney(product.price)}</>
												</span>
											)}
										</p>
									</div>
								</div>
							</div>
						</Link>
						
						<div className="row px-[10px] py-2 text-center w-full bg-white shadow-xl"> 
							<div className="custom-number-input w-full items-center">
								<div className="flex flex-row h-10 relative rounded-lg bg-transparent mt-1 mb-4">
									<button onClick={() => btnDecreaseQtyCartList(product)} className="bg-[#98c01d] text-2xl border-[#98c01d] hover:bg-[#88af14] 
										text-white h-full w-32 rounded-l cursor-pointer outline-none"
										disabled={productInCart(product.id).length >= 1 && productInCart(product.id)[0]['cart_quantity'] === 1}>
									<span className="m-auto text-2xl font-thin">−</span>
									</button>
									<input type="text" 
										value={productInCart(product.id).length >= 1 ? productInCart(product.id)[0]['cart_quantity'] : 0} 
										className="border-[#98c01d] text-center w-full bg-white font-semibold text-md hover:text-black 
										focus:text-black md:text-basecursor-default flex items-center text-gray-700" 
										name="custom-input-number" />
									<button onClick={() => btnIncreaseQtyCartList(product)} className="bg-[#98c01d] text-2xl border-[#88af14] 
										hover:bg-[#9c0] text-white h-full w-32 rounded-r cursor-pointer"
										disabled={productInCart(product.id).length >= 1 && 
											productInCart(product.id)[0]['quantity'] === productInCart(product.id)[0]['cart_quantity']
										}>
										<span className="m-auto text-2xl font-thin">+</span>
									</button>
								</div>
							</div>
							<div className="custom-number-input w-full pb-3">
								<div className="row w-full rounded-lg relative bg-transparent">
									{product.name ? (
												<button onClick={() => btnAddToCart(product)} className="w-full mt-1 font-semibold leading-none text-white py-4 bg-[#98c01d] rounded-md hover:bg-[#88af14] focus:ring-2 focus:ring-offset-2 focus:outline-none cursor-pointer md:w-2/3">Add to cart</button>
											): <Skeleton width={80} height={40} />}
									
								</div>
							</div>
						</div>
					</div> 
				</div>
			</div>
		</SkeletonTheme>
	);
}

 @@ComponentName@@.propTypes = {
  // eslint-disable-next-line react/forbid-prop-types
  product: PropType.object.isRequired
};

export default @@ComponentName@@;
 """
 products["product_item_1"] = product_item_1


 """
 ProductCard
 """
 product_card_1 ="""
import React from "react";
import PropType from 'prop-types';

import ProductItem from "../../../pages/product/ProductItem";
import { Search } from "../../default";
import { shallowEqual, useSelector } from "react-redux";

const @@ComponentName@@ = ({ products }) => {
    const store = useSelector((state) => ({
        products: state.products,
        requestStatus: state.app.requestStatus
    }), shallowEqual);

    return (
        <div className="">
            <div className="text-center py-4 mt-2 md:mt-4 luday_deals">
                @@Pos1@@
            </div>
            <section className="bg-gray-50">
                <div className="px-3 md:px-[120px] lg:px-[120px] py-[30px] pb-[30px] luday_wrap">  
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-2"> 
                        {products.length === 0 ? new Array(6).fill({}).map((product, index) => (
                            @@Pos2ShowProductItemLoading@@
                        )): store.products.items.map((product) => (
                            @@Pos2ShowProductItemIffProductExist@@
                        ))}
                    </div>
                </div>
            </section> 
        </div>
    )
};

@@ComponentName@@.propTypes = {
    products: PropType.array.isRequired
};

export default @@ComponentName@@;
 """
 products["product_card_1"] = product_card_1

 """
 ProductCard
 """
 product_card_list_1 ="""
import React, { useEffect, useState } from "react";
import { Link } from 'react-router-dom';
import PropType from 'prop-types';

import * as ROUTE from '../../../constants/routes';
import { getProducts } from "../../../redux/actions/productActions";
import { setLoading } from "../../../redux/actions/miscActions";
import { useDispatch } from "react-redux";

const @@ComponentName@@ = (props) => {
	const {
		products, children
	} = props;
	const [isFetching, setFetching] = useState(false);
	const dispatch = useDispatch();

	const fetchProducts = () => {
		setFetching(true);
		dispatch(getProducts(products.lastRefKey));
	};

	useEffect(() => {
		if (products.items.length === 0 || !products.lastRefKey) {
			fetchProducts();
		}

		window.scrollTo(0, 0);
		return () => dispatch(setLoading(false));
	}, []);
	
	useEffect(() => {
		setFetching(false);
	}, [products.lastRefKey]);

    return (
		<>
			{children}
			{products.nextPage && (
				<div className="flex space-x-2 justify-center pb-10">
					<button 
						type="button"
						disabled={isFetching}
						onClick={fetchProducts}
						className="inline-block px-6 py-2.5 bg-[#98c01d] text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-[#88af14] hover:shadow-lg focus:[#88af14] focus:shadow-lg focus:outline-none focus:ring-0 active:bg-[#98c01d] active:shadow-lg transition duration-150 ease-in-out">
						{isFetching ? '@@ShowMoreBtnOnLoadingText@@' : '@@ShowMoreBtnText@@'}
					</button>
				</div>
			)}
			<div className="justify-center mx-auto text-center">Click <Link to={`${ROUTE.SIGNUP_VENDOR}`} className="text-[#88af14]"> @@DetailsText1@@</Link> @@DetailsText1Contd@@ </div>
		</>
    )
};

@@ComponentName@@.defaultProps = {
	requestStatus: null
};

@@ComponentName@@.propTypes = {
	products: PropType.object.isRequired,
	requestStatus: PropType.string,
	children: PropType.oneOfType([
		PropType.arrayOf(PropType.node),
		PropType.node
	]).isRequired
  };

export default @@ComponentName@@;
 """
 products["product_card_list_1"] = product_card_list_1