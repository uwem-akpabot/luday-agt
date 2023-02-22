class Services:

 services = {}
 
 # Add Service index
 services_index ="""
export * as REQUEST_METHOD from './request';
export * as USER_API from './user';
export * as PRODUCT_API from './product';
 """
 services["services_index"] = services_index


 # Add product Service
 product_service ="""
import { REQUEST_METHOD } from ".";
import * as ROUTES from '../constants/routes';

const PRODUCT_ROUTE = `${ROUTES.PRODUCTS_API}`

export function getCategoryProducts(data) {
	return REQUEST_METHOD.get(`${PRODUCT_ROUTE}/categories/${data}/products`)
}

export function searchProducts(searchKey, lastKeyRef) {
	if(lastKeyRef){
		return REQUEST_METHOD.get(`${PRODUCT_ROUTE}/products/search?q=${searchKey}&last_key=${lastKeyRef}`)
	}
	return REQUEST_METHOD.get(`${PRODUCT_ROUTE}/products/search?q=${searchKey}`)
}

export function getProducts(lastKeyRef) {
	if (lastKeyRef) {
		return REQUEST_METHOD.get(`${PRODUCT_ROUTE}/products/verified?last_key=${lastKeyRef}`)
	}
	return REQUEST_METHOD.get(`${PRODUCT_ROUTE}/products/verified`)
}

export function addOrder(data, kwargs) {
	return REQUEST_METHOD.post(`${PRODUCT_ROUTE}/order/user`, data, kwargs)
}

export function addGuestOrder(data) {
	return REQUEST_METHOD.post(`${PRODUCT_ROUTE}/order/guest`, data)
}

export function updateOrderBillingAddressIdByRefId(data) {
	return REQUEST_METHOD.put(`${PRODUCT_ROUTE}/order/billing-address`, data)
}
 """
 services["product_service"] = product_service


 # Add request Service
 request_service ="""
import { stringify } from 'query-string'
import Cookies from 'js-cookie'
import { Buffer } from 'buffer'

export function url(uri, queryParams, route_api) {
	const baseUrl = `${route_api}${uri}`
	return queryParams
	? `${baseUrl}?${stringify(queryParams)}`
	: baseUrl
}

export function get(url, kwargs = {}) {
	const { token, ...options } = kwargs
	const defaults = {
		// credentials: 'include',
		headers: Object.assign({
		'Accept': 'application/json',
		'Content-Type': 'application/json'
		}, token ? { 'Authorization': `Bearer ${token}` } : {}),
		method: 'GET'
	}
	return request(url, _mergeOptions(defaults, options))
}

export function post(url, data, kwargs = {}) {
	const { token, ...options } = kwargs
	const defaults = {
		// credentials: 'include',
		headers: Object.assign({
		'Accept': 'application/json',
		'Content-Type': 'application/json',
		'X-CSRFToken': Cookies.get('csrf_token')
		}, token ? { 'Authorization': `Bearer ${token}` } : {}),
		method: 'POST',
		body: JSON.stringify(data)
	}
	return request(url, _mergeOptions(defaults, options))
  }

  export function postFormData(url, data, kwargs = {}) {
	const { token, ...options } = kwargs
	const defaults = {
		headers: Object.assign(token ? { 'Authorization': `Bearer ${token}` } : {}),
		method: 'POST',
		body: data
	}
	return request(url, _mergeOptions(defaults, options))
  }

  export function authHeader(url, data, kwargs = {}) {
	const { ...options } = kwargs
	const encodedString = Buffer.from(`${data.email}:${data.password}`).toString('base64');
	const defaults = {
		headers: Object.assign({
		'Accept': 'application/json',
		'Content-Type': 'application/json',
		'Authorization': `Basic ${encodedString}`
		}),
		method: 'POST'
	}
	return request(url, _mergeOptions(defaults, options))
  }
  
export function put(url, data, options = {}) {
	return post(url, data, _setMethod(options, 'PUT'))
}

export function putFormData(url, data, options = {}) {
	return postFormData(url, data, _setMethod(options, 'PUT'))
}
  
export function patch(url, data, options = {}) {
	return post(url, data, _setMethod(options, 'PATCH'))
}
  
export function delete_(url, options = {}) {
	return get(url, _setMethod(options, 'DELETE'))
}
  

export const request = async (url, options) => {
	return await fetch(url, options)
		.then(_checkStatusAndParseJSON)
		.catch((e) => {
		return new Promise((_, reject) => {
			if (e.response) {
				reject(e)
			} else {
				// should only end up here if the flask application has gone away
				e.response = {
					status: -1,
					statusText: e.message,
					error: e.message
				}
				reject(e)
			}
		})
	})
}

function _checkStatusAndParseJSON(response) {
	return new Promise((resolve, reject) => {
		response.json()
		.then((json) => {
			if (_checkStatus(response)) {
				// success response with json body
				resolve(json)
			} else {
				// error response with json error message
				reject(json.messages)
			}
		})
		// response with no body (response.json() raises SyntaxError)
		.catch(() => {
			if (_checkStatus(response)) {
				// success response with no body (most likely HTTP 204: No Content)
				resolve(null)
			} else {
				// error response, create generic error message from HTTP status
				reject(_responseError(response, { error: response.statusText }))
			}
		})
	})
  }
  
function _mergeOptions(defaults, options) {
	return Object.assign({}, defaults, {
		...options,
		headers: {
		...defaults.headers,
		...options.headers
		}
	})
}

function _setMethod(options, method) {
	return Object.assign({}, options, { method })
}  
  
function _checkStatus(response) {
	return response.status >= 200 && response.status < 300
}
  
function _responseError(response, json) {
	const error = new Error(response.statusText)
	error.response = Object.assign({
		status: response.status,
		statusText: response.statusText
	}, json)
	return error
}
 """
 services["request_service"] = request_service


 # Add user Service
 user_service ="""
import { REQUEST_METHOD } from ".";
import * as ROUTES from '../constants/routes';

const USER_ROUTE = `${ROUTES.USER_API}/user`
const AUTH_ROUTE = `${ROUTES.USER_API}/auth`

export function signUp(data) {
	return REQUEST_METHOD.post(USER_ROUTE, data)
}

export function signUpVendorDetails(data, kwargs) {
	return REQUEST_METHOD.putFormData(`${AUTH_ROUTE}/user/vendors`, data, kwargs)
}

export function signIn(data) {
	return REQUEST_METHOD.authHeader(`${AUTH_ROUTE}/tokens`, data)
}

export function signOut(data) {
	return REQUEST_METHOD.delete_(`${AUTH_ROUTE}/tokens`, data)
}

export function getRefreshToken(data) {
	return REQUEST_METHOD.put(`${AUTH_ROUTE}/tokens`, data)
}

export function getAuthenticatedUser(kwargs) {
	return REQUEST_METHOD.get(`${USER_ROUTE}/auth`, kwargs)
}

export function updateUserDetails(data, kwargs) {
	return REQUEST_METHOD.put(`${USER_ROUTE}/edit`, data, kwargs)
}

export function addOrUpdateAuthenticatedUserAddress(data, kwargs) {
	return REQUEST_METHOD.put(`${AUTH_ROUTE}/user/address`, data, kwargs)
}

export function addOrUpdateGuestUserAddress(data, kwargs) {
	return REQUEST_METHOD.put(`${USER_ROUTE}/address`, data, kwargs)
}

export function resetUserPassword(data) {
	return REQUEST_METHOD.put(`${AUTH_ROUTE}/tokens/reset`, data)
}

export function forgotUserPassword(data) {
	return REQUEST_METHOD.post(`${AUTH_ROUTE}/tokens/reset`, data)
}
 """
 services["user_service"] = user_service

 # Service #Ludayab
 company_services_card ="""
import React from 'react'
import { Link } from 'react-router-dom'
import { ArrowRightIcon } from '@heroicons/react/20/solid'

const ServicesCard = () => {
    const Services =[
        {
            name: 'Web Development',
            description:
              'We build user-centered web & Mobile applications to meet our clients need using latest technology and models. We develop cross platform apps for both iOS and Android devices',
            icon: "M9 17.25v1.007a3 3 0 01-.879 2.122L7.5 21h9l-.621-.621A3 3 0 0115 18.257V17.25m6-12V15a2.25 2.25 0 01-2.25 2.25H5.25A2.25 2.25 0 013 15V5.25m18 0A2.25 2.25 0 0018.75 3H5.25A2.25 2.25 0 003 5.25m18 0V12a2.25 2.25 0 01-2.25 2.25H5.25A2.25 2.25 0 013 12V5.25",
            path: '/web-development'
        },
        {
            name: 'Embedded Software Development',
            description: 'We offer senior and junior consultants with vast knowledge in embedded software development and architecture. Our experience span across several industries and we are proficient in several embedded technologies.',
            icon: "M8.25 3v1.5M4.5 8.25H3m18 0h-1.5M4.5 12H3m18 0h-1.5m-15 3.75H3m18 0h-1.5M8.25 19.5V21M12 3v1.5m0 15V21m3.75-18v1.5m0 15V21m-9-1.5h10.5a2.25 2.25 0 002.25-2.25V6.75a2.25 2.25 0 00-2.25-2.25H6.75A2.25 2.25 0 004.5 6.75v10.5a2.25 2.25 0 002.25 2.25zm.75-12h9v9h-9v-9z",
        },
        {
            name: 'Digital Marketing',
            description: ' We have a team of digital marketers committed to increasing your online presence on whatever Social platform is most convenient for your brand.',
            icon: "M20.25 8.511c.884.284 1.5 1.128 1.5 2.097v4.286c0 1.136-.847 2.1-1.98 2.193-.34.027-.68.052-1.02.072v3.091l-3-3c-1.354 0-2.694-.055-4.02-.163a2.115 2.115 0 01-.825-.242m9.345-8.334a2.126 2.126 0 00-.476-.095 48.64 48.64 0 00-8.048 0c-1.131.094-1.976 1.057-1.976 2.192v4.286c0 .837.46 1.58 1.155 1.951m9.345-8.334V6.637c0-1.621-1.152-3.026-2.76-3.235A48.455 48.455 0 0011.25 3c-2.115 0-4.198.137-6.24.402-1.608.209-2.76 1.614-2.76 3.235v6.226c0 1.621 1.152 3.026 2.76 3.235.577.075 1.157.14 1.74.194V21l4.155-4.155",
            path: '/digital-marketing'
        },
        {
            name: 'UI/UX Design',
            description: 'Our team is ready to work with you to provide a remarkable user experience design that distinguishes your products and businesses from the others.',
            icon: "M2.25 7.125C2.25 6.504 2.754 6 3.375 6h6c.621 0 1.125.504 1.125 1.125v3.75c0 .621-.504 1.125-1.125 1.125h-6a1.125 1.125 0 01-1.125-1.125v-3.75zM14.25 8.625c0-.621.504-1.125 1.125-1.125h5.25c.621 0 1.125.504 1.125 1.125v8.25c0 .621-.504 1.125-1.125 1.125h-5.25a1.125 1.125 0 01-1.125-1.125v-8.25zM3.75 16.125c0-.621.504-1.125 1.125-1.125h5.25c.621 0 1.125.504 1.125 1.125v2.25c0 .621-.504 1.125-1.125 1.125h-5.25a1.125 1.125 0 01-1.125-1.125v-2.25z",
            path: '/ui-ux-design'
        },
        {
            name: 'Product Management',
            description: 'We specialise in transforming ideas into profitable products. Our team helps with the different stages of product management and we are committed to delivering quality products to the right people.',
            icon: "M6.429 9.75L2.25 12l4.179 2.25m0-4.5l5.571 3 5.571-3m-11.142 0L2.25 7.5 12 2.25l9.75 5.25-4.179 2.25m0 0L21.75 12l-4.179 2.25m0 0l4.179 2.25L12 21.75 2.25 16.5l4.179-2.25m11.142 0l-5.571 3-5.571-3",
            path: '/product-management'
        },
        {
            name: 'Data Analytics',
            description: 'We help organizations mine data and leverage it for making informed decisions. Our experts are vast in data interpretation, visualization and creating predictive models.',
            icon: "M3.75 3v11.25A2.25 2.25 0 006 16.5h2.25M3.75 3h-1.5m1.5 0h16.5m0 0h1.5m-1.5 0v11.25A2.25 2.25 0 0118 16.5h-2.25m-7.5 0h7.5m-7.5 0l-1 3m8.5-3l1 3m0 0l.5 1.5m-.5-1.5h-9.5m0 0l-.5 1.5M9 11.25v1.5M12 9v3.75m3-6v6",
            path: '/data-analytics'
        }
    ]
  return (
   
	<div className="grid grid-cols-1 gap-4 mt-8 xl:mt-12 xl:gap-5 md:grid-cols-2 xl:grid-cols-3">
		{Services.map((service) => (
		<div key={service.name} class="mx-5 grid place-content-center">
			<div class="bg-gradient-to-r from-blue-400 to-indigo-500 rounded-2xl text-white p-5 text-center h-72 max-w-sm mx-auto">
				<p class="text-lg">{service.description}</p>
			</div>
			<div class="bg-white py-8 px-10 text-center rounded-md shadow-lg transform -translate-y-20 sm:-translate-y-24 max-w-xs mx-auto">
				<h2 class="font-semibold text-2xl mb-6">{service.name}</h2>
				<div class="w-20 h-20 object-cover rounded-full mx-auto shadow-lg flex items-center mb-8"> 
					<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-10 h-10 mx-auto">
						<path strokeLinecap="round" strokeLinejoin="round" d={service.icon} />
					</svg>
				</div>
				<Link to={service.path} class="rounded-md bg-gradient-to-r from-blue-400 to-indigo-500 text-xl text-white pt-3 pb-4 px-8 flex items-center">Read More <ArrowRightIcon className="h-5 w-5 text-white" aria-hidden="true" /></Link>
			</div>
		</div>
		))}
	</div>
    )
}

export default ServicesCard
 """
 services["company_services_card"] = company_services_card

 # Service #Ludayab-card
 company_services ="""
import React from 'react'
import ServiceCard from './ServicesCard'

const Services = () => {
  return (
    <section className="bg-gray-900">
            <div className="container max-w-7xl px-6 py-10 mx-auto">
                <h2 className="text-lg font-semibold leading-8 tracking-tight text-blue-600">@@Heading1@@</h2>
                <p className="mt-2 text-3xl font-bold tracking-tight text-white sm:text-4xl">@@Paragraph1@@</p>
                
                <p className="mt-4 text-gray-500 xl:mt-6 dark:text-gray-300">
                    @@Paragraph2@@
                </p>
                <ServiceCard/>
            </div>
        </section>
  )
}
export default Services
 """
 services["company_services"] = company_services
