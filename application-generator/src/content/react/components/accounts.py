class Accounts:

 accounts = {}


 """
 Account navigation component
 """
 account_navigation ="""
import React from 'react';
import { NavLink } from "react-router-dom";
import * as ROUTE from '../../../../constants/routes';

const @@PageName@@ = () => {
    return (
        <ul>
            <li className="flex flex-row m-5"> 
                <NavLink to={ROUTE.PROFILE} className="flex flex-row whitespace-nowrap items-center"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24"><path d="M7.5 6.5C7.5 8.981 9.519 11 12 11s4.5-2.019 4.5-4.5S14.481 2 12 2 7.5 4.019 7.5 6.5zM20 21h1v-1c0-3.859-3.141-7-7-7h-4c-3.86 0-7 3.141-7 7v1h17z"></path></svg>
                &nbsp; @@NavLink1@@ </NavLink>
            </li>
            <li className="flex flex-row m-5"> 
                <NavLink to="/change-password" className="flex flex-row whitespace-nowrap items-center"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24"><path d="m18.988 2.012 3 3L19.701 7.3l-3-3zM8 16h3l7.287-7.287-3-3L8 13z"></path><path d="M19 19H8.158c-.026 0-.053.01-.079.01-.033 0-.066-.009-.1-.01H5V5h6.847l2-2H5c-1.103 0-2 .896-2 2v14c0 1.104.897 2 2 2h14a2 2 0 0 0 2-2v-8.668l-2 2V19z"></path></svg>
                &nbsp; @@NavLink2@@ </NavLink>
            </li>
            <li className="flex flex-row m-5"> 
                <NavLink to="/order-history" className="flex flex-row whitespace-nowrap items-center"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24"><path d="M20 3H4c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2h16c1.103 0 2-.897 2-2V5c0-1.103-.897-2-2-2zm-1 4v2h-5V7h5zm-5 4h5v2h-5v-2zM4 19V5h7v14H4z"></path></svg>
                &nbsp;@@NavLink3@@ </NavLink>
            </li>
        </ul>
    );
};

export default @@PageName@@;
 """
 accounts["account_navigation"] = account_navigation


 """
 Account edit form component
 """
 account_edit_form ="""
import React, { useEffect } from 'react';

import PropType from 'prop-types';
import { Field, useFormikContext } from 'formik';

import CustomMobileInput from '../../components/formik/CustomMobileInput';
import { 
	CustomInput, 
	CustomSelectCity, 
	CustomSelectState,
	CustomTextarea
} from '../../components/formik';
import sc from '../../helpers/state-city/sc';

const @@PageName@@ = ({ isLoading, authProvider }) => {
    const _states = sc.getAllStates();

	const updatedStates = _states.map((country) => ({
		label: country.name,
		value: country.name,
		...country
	}));
	const updatedCities = (stateId) =>
		sc
		.getLocalGovtOfState(stateId)
		.map((city) => ({ label: city.name, value: city.name, ...city })
	);
	const { values, handleSubmit } = useFormikContext();
	
	useEffect(() => {}, [values]);

	return (
		<>
			<div className="flex flex-col md:flex-row justify-between">
				<div className="mt-3 mb-3 w-auto md:w-3/5 md:mr-3">
					@@InputComponent1@@
				</div>
				<div className="mt-3 mb-3 w-auto md:w-3/5 md:mr-3">
					@@InputComponent2@@
				</div>
			</div>
			<div className="flex flex-col md:flex-row justify-between">
				<div className="mt-3 mb-3 w-auto md:w-3/5 md:mr-3 w-full ">
					@@InputComponent3@@
				</div>
				<div className="mt-3 mb-3 w-auto md:w-3/5 md:mr-3">
					@@InputComponent4@@
				</div>
			</div>
			<div className="flex flex-col md:flex-row justify-between">
				<div className="mt-3 mb-3 w-auto md:w-full">
					@@InputComponent5@@
				</div>
			</div>
			<div className="flex flex-col md:flex-row justify-between">
				<div className="mt-3 mb-3 w-auto md:w-3/5 md:mr-3 w-full ">
					@@InputComponent6@@
				</div>
				<div className="mt-3 mb-3 w-auto md:w-3/5 md:mr-3 w-full ">
					@@InputComponent7@@
				</div>
			</div>
			<div className="mt-10 flex justify-center">
				<button 
					disabled={isLoading} 
					className="button button--theme overflow-hidden bg-[#9c0] hover:bg-yellow-300 text-white text-sm transition-all ease-in-out duration-300 rounded py-3 px-5 m-2 flex items-center flex-nowrap w-80 justify-center"
					onClick={handleSubmit}
					type="button"
				>
					<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" className="fill-current mr-2" ><path d="M5 21h14a2 2 0 0 0 2-2V8a1 1 0 0 0-.29-.71l-4-4A1 1 0 0 0 16 3H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2zm10-2H9v-5h6zM13 7h-2V5h2zM5 5h2v4h8V5h.59L19 8.41V19h-2v-5a2 2 0 0 0-2-2H9a2 2 0 0 0-2 2v5H5z"></path></svg>
					<span>{isLoading ? '@@SubmitBtnOnLoadingText@@' : '@@SubmitBtnText@@'}</span>
				</button>
			</div>
		</>
	);
};

@@PageName@@.propTypes = {
  isLoading: PropType.bool.isRequired,
  authProvider: PropType.any
};

export default @@PageName@@;
 """
 accounts["account_edit_form"] = account_edit_form
 
  
 """
 Account order item component 1
 """
 account_order_item_1 ="""
import React from 'react';
import { Link } from "react-router-dom";
import PropType from 'prop-types';
import * as ROUTE from '../../../constants/routes';

const @@PageName@@ = ({ order }) => {
const nf = new Intl.NumberFormat();
	return (
		<>
			<td className="float-right mx-5">
				<Link to={`${ROUTE.ORDER_DETAILS}/${order.order_id}/${order.ref_id}`}
					className="m-2 float-right">
					<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24">
						<path d="M12 2C6.486 2 2 6.486 2 12s4.486 10 10 10 10-4.486 10-10S17.514 2 12 2zm0 17c-3.859 0-7-3.14-7-7s3.141-7 7-7 7 3.14 7 7-3.141 7-7 7z"></path>
						<path d="M12 7c-2.757 0-5 2.243-5 5s2.243 5 5 5 5-2.243 5-5-2.243-5-5-5zm0 7c-1.103 0-2-.897-2-2s.897-2 2-2 2 .897 2 2-.897 2-2 2z"></path>
					</svg>
				</Link>
			</td>
			<td className="items-center p-3 w-[200px]">
				<p className="text-sm">{order.ref_id}</p>
			</td>
			<td className="text-center">{order.status == "Pending" ?
				<span className="bg-yellow-200 text-yellow-800 px-2 py-1 rounded-full">{order.status} or Cash delivery</span>
			:
			order.status == "Failed" ?
				<span className="bg-red-200 text-red-800 px-2 py-1 rounded-full">{order.status}</span>
			:
			order.status == "Successful" ?
			<span className="bg-green-200 text-green-800 px-2 py-1 rounded-full">{order.status}</span>
			:
			<span className="">not completed</span>
		}
				</td>
			<td className="items-center p-3">
				<p className="bg-green-200 text-green-800 px-2 py-1 rounded-full">{order.delivery_status}</p>
			</td>
			<td className="items-center p-3">
				<p className="text-sm"><b>&#8358;{nf.format(order.amount)}</b></p>
			</td>
			
			<td className="items-center">
				<p className="text-sm">{order.created_at.toString().slice(0, 16)}</p>
			</td>
			
		</>
	);
};

@@PageName@@.propTypes = {
  // eslint-disable-next-line react/forbid-prop-types
  order: PropType.object.isRequired
};

export default @@PageName@@;
 """
 accounts["account_order_item_1"] = account_order_item_1


 """
 Account order item component 2
 """
 account_order_item_2 ="""
import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { useSelector } from 'react-redux';
import * as ROUTE from '../../../constants/routes';
import { useDocumentTitle } from "../../../hooks";
import { displayMoney } from "../../../helpers/utils";
import * as CONSTANT from '../../../constants/constants';

const @@PageName@@ = () => {
    const { id, ref } = useParams();
	const { token } = useSelector((state) => ({
		token: state.profile.access_token
	}));
	const [order, setOrder] = useState([]);
	const [orderInfo, setOrderInfo] = useState([]);
	const [isLoading, setLoading] = useState(false);
	const [error, setError] = useState(null);
	const [totalSum, setTotalSum] = useState('');
	//const { order, isLoading } = useOrder(id, token);

	useEffect(() => {
		(async () => {
			try {
				const requestOptions = {
					method: "GET",
					headers: {
						'Content-Type': 'application/json',
						'Accept': 'application/json',
						'Authorization': `Bearer ${token}`
					}
				}
				await fetch(`${ROUTE.PRODUCTS_API}/order/mapping/${id}`, requestOptions)
				.then((res) => res.json())
				.then((res) => {
				//console.log(res.length)
				setOrder(res);
				setOrderInfo(res[0])
				setTotalSum((res.reduce((a,v) =>  a = a + v.product_sale_price , 0 )))
				setLoading(false)
				});
			} catch (err) {
				
					setLoading(false);
					setError(err?.message || 'Something went wrong.');
				
			}
		})();
	}, [id, token]);

	useDocumentTitle('My Profile | BestDealNaija');
	let OrderItemlist = ''
    if(order.length > 0){
        OrderItemlist =  (
            <>
			{order.map(item => 
				<tr key={item.id} className="border border-black-600 whitespace-nowrap">
					<td className="items-left">
						<div className="flex flex-row">
								<div className=" py-2 h-30 w-32">
									<img className="h-32 w-32" src={`${CONSTANT.IMAGE_STORE}/${item.product_image_path}`}/> 
								</div>
								<div className=" py-2">
										<h2 className="px-6 text-left text-lg w-[300px] overflow-hidden text-ellipsis md:text-xl">{item.product_name}</h2>
								</div>
						</div>
					</td>
					<td className="text-center">
						{item.order_product_mapping_quantity}
					</td>
					<td className="text-center">&#8358;{displayMoney(item.order_product_mapping_price)}</td>
				</tr>
				)}
			</>
        )
    } else {
		OrderItemlist =  (
        <>
			<tr className="border border-black-600 whitespace-nowrap">
				<p className="text-center">Loading...</p>
			</tr>
		</> 
	)}

	return (
		<>
			{order && !isLoading ?(
				<>
					<div className="">
						<h4 className="mb-2">My Order</h4>
						<div className="flex flex-col space-y-2">
							<p>Order id: {ref}</p>
							<p>Order status: 
								{orderInfo.status == "Pending" ?
										<span className="bg-yellow-200 text-yellow-800 px-2 py-1 rounded-full">{orderInfo.status} or Cash delivery</span>
									:
									orderInfo.status == "Failed" ?
										<span className="bg-red-200 text-red-800 px-2 py-1 rounded-full">{orderInfo.status}</span>
									:
									orderInfo.status == "Successful" ?
									<span className="bg-green-200 text-green-800 px-2 py-1 rounded-full">{orderInfo.status}</span>
									:
									<span className="">loading...</span>
								}
							</p>
							
							<p>Date: {orderInfo.created_at}</p>
						</div>
						<hr/><br/>
					</div>
					<div className="overflow-x-auto">
						<table className="divide-y divide-gray-300 md:w-full">
							<thead className="bg-gray-50" >
								<tr>
									<th className="px-6 py-2 text-left">Product</th>
									<th className="px-6 py-2 text-center">Quantity</th>
									<th className="px-6 py-2 ">Price</th>
								</tr>
							</thead>
							<tbody>
							{OrderItemlist}
							</tbody>
						</table>
					</div>
					<div className="float-right">
					<p className="text-2xl mt-5 ">Grand Total
						<span className=" ml-1">&#8358;{displayMoney(totalSum)}</span></p>
					</div>
				</>
			):
				<p>Loading..... {error}</p>
			}
		</>
	);
};

export default @@PageName@@;
 """
 accounts["account_order_item_2"] = account_order_item_2

 
 """
 Account Profile Component
 """
 account_profile_component_1 ="""
import React, { useState, useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';

import * as Yup from 'yup';
import { Formik } from 'formik';

import { Popup } from '../../../hooks';
import Banner from '../../../components/default/Banner/index';
import bannerImage from '../../../images/bdn_about_image_2.jpg';
import Accnav from '../../../components/default/Navigation/account/index';
import { updateProfile } from '../../../redux/actions/profileActions';
import { setLoading } from '../../../redux/actions/miscActions';
import EditForm from '../EditForm';
import '../styles/profile.css'

const UpdateProfileSchema = Yup.object().shape({
    email: Yup.string()
      .email('Email is not valid.')
      .required('Email is required.'),
    first_name: Yup.string()
      .required('First name is required.')
      .min(2, 'Name should be at least 2 characters.'),
    last_name: Yup.string()
      .required('Last name is required.')
      .min(2, 'Name should be at least 2 characters.'),
    // gender: Yup.string()
    //   .required('Gender is required.'),
	address: Yup.string()
      .required('Address is required.'),
	mobile_number: Yup.string()
		.required('Mobile is required.')
		.min(12, 'Mobile number should be at least 11 characters.')
		.max(13, 'Mobile number should be only be 11 characters long.'),
	state: Yup.object()
		.shape({
			countryCode: Yup.string(),
			isoCode: Yup.string(),
			label: Yup.string(),
			latitude: Yup.string(),
			longitude: Yup.string(),
			name: Yup.string(),
			value: Yup.string().required('State is required.')
		})
		.required('State is required.'),
	city: Yup.object()
		.shape({
			countryCode: Yup.string(),
			stateCode: Yup.string(),
			name: Yup.string(),
			value: Yup.string().required('City is required.')
		})
		.required('City is required.')
});

const @@PageName@@ = () => {
    const { profile, auth, isLoading } = useSelector((state) => ({
		profile: state.profile,
		auth: state.auth,
		isLoading: state.app.loading
	}));
	const dispatch = useDispatch();
	const [isOpen, setIsOpen] = useState(false);

	const togglePopup = () => {
		setIsOpen(!isOpen);
	}

	useEffect(() => {
		dispatch(setLoading(false));
	}, []);

	const initFormikValues = {
		first_name: profile.first_name || '',
		last_name: profile.last_name || '',
		email: profile.email || '',
		// gender: profile.gender || '',
		mobile_number: profile.mobile_number || '',
		address: profile.address || '',
		state: profile.ref_state || {},
		city: profile.ref_local_govt || {}
	};

	const update = (form, credentials={}) => {
		dispatch(updateProfile({
			updates: {
				first_name: form.first_name,
				last_name: form.last_name,
				email: form.email,
				// gender: form.gender,
				mobile_number: form.mobile_number
				
			},
			address : {
				address: form.address,
				ref_local_govt: form.city.value,
				ref_state: form.state.value,
				user_id: auth.id
			},
			credentials
		}));
	};

	const onSubmitUpdate = (form) => {
		// check if data has changed
		const fieldsChanged = Object.keys(form).some((key) => profile[key] !== form[key]);
		if (fieldsChanged) {
			update(form);
		}
	};

	return (
		<>
			@@Pos1@@
			{isOpen && <Popup
				content={
					<Formik
						initialValues={initFormikValues}
						validateOnChange
						validationSchema={UpdateProfileSchema}
						onSubmit={onSubmitUpdate}
					>
						{() => (
							<>
								<div className="">
									<h4 className="mb-2">Edit Profile</h4>
									<hr/>
								</div>
								@@FormComponent1@@
							</>
						)}
					</Formik>
				}
				handleClose={togglePopup} />
			}
			<div className="py-2 px-[10px] mt-10 md:px-[60px] lg:px-[90px]">                    
				<div className="flex flex-col md:flex-row py-[50px]">	
					<div className="w-full md:w-1/3 m-2 border border-black-600 drop-shadow-md p-5 h-1/2">
						@@Pos2@@
					</div>
					<div className="w-full md:w-2/3 m-2 border border-black-600 drop-shadow-md p-5">
						<div className="overflow-x-auto">
								<div className="flex flex-col md:flex-row justify-between">
							<div className="mt-3 mb-3 w-auto md:w-[400px]">
								<label htmlFor="firstName">@@Input1Label@@: </label>
								<div className="">
									<label htmlFor="firstName">{profile.first_name}</label>
								</div>
							</div>
							<div className="mt-3 mb-3 w-auto md:w-[400px]">
								<label htmlFor="lastname">@@Input2Label@@: </label>
								<div className="input-group">
									<label htmlFor="lastname">{profile.last_name}</label>
								</div>
							</div>
						</div>
						<div className="flex flex-col md:flex-row justify-between">
							<div className="mt-3 mb-3 w-auto md:w-[400px]">
								<label htmlFor="mobile">@@Input3Label@@: </label>
								<div className="input-group">
								<label htmlFor="mobile">
									{profile.mobile_number ? (
										<label htmlFor="state">{profile.mobile_number}</label>
									) : (
										<label htmlFor="state" className="text-gray-400">@@Input3EmptyMssg@@</label>
									)}
								</label>
								</div>
							</div>
							<div className="mt-3 mb-3 w-auto md:w-[400px]">
								<label htmlFor="email">@@Input4Label@@: </label>
								<div className="input-group">
									<label htmlFor="email">{profile.email}</label>
								</div>
							</div>
						</div>
						<div className="flex flex-col md:flex-row">
							<div className="mt-3 mb-3 w-auto md:w-full">
								<label htmlFor="address">@@Input5Label@@: </label>
								<div className="input-group">
									{profile.address ? (
										<label htmlFor="address">{profile.address}</label>
									) : (
										<label htmlFor="address" className="text-gray-400">@@Input5EmptyMssg@@</label>
									)}
								</div>
							</div>
						</div>
						<div className="flex flex-col md:flex-row justify-between">
							<div className="mt-3 mb-3 w-auto md:w-[400px]">
								<label htmlFor="state">@@Input6Label@@: </label>
								<div className="input-group">
									{profile.ref_state ? (
										<label htmlFor="state">{profile.ref_state}</label>
									) : (
										<label htmlFor="state" className="text-gray-400">@@Input6EmptyMssg@@</label>
									)}
								</div>
							</div>
							<div className="mt-3 mb-3 w-auto md:w-[400px]">
								<label htmlFor="postal">@@Input7Label@@: </label>
								<div className="input-group">
									{profile.ref_local_govt ? (
										<label htmlFor="local_govt">{profile.ref_local_govt}</label>
									) : (
										<label htmlFor="local_govt" className="text-gray-400">@@Input7EmptyMssg@@</label>
									)}
								</div>
							</div>
						</div>
						<div className="mt-10 flex justify-center">
							<button onClick={togglePopup} className="button button--theme overflow-hidden bg-[#9c0] 
							hover:bg-yellow-300 text-white text-sm transition-all ease-in-out duration-300 
							rounded py-3 px-5 m-2 flex items-center flex-nowrap w-80 justify-center">
							<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24"><path d="m18.988 2.012 3 3L19.701 7.3l-3-3zM8 16h3l7.287-7.287-3-3L8 13z"></path><path d="M19 19H8.158c-.026 0-.053.01-.079.01-.033 0-.066-.009-.1-.01H5V5h6.847l2-2H5c-1.103 0-2 .896-2 2v14c0 1.104.897 2 2 2h14a2 2 0 0 0 2-2v-8.668l-2 2V19z"></path></svg>
							<span> &nbsp; @@SubmitBtnText@@</span>
							</button>
						</div>
						</div>
					</div>
				</div>
			</div>
		</>
	);
}
export default @@PageName@@;
 """
 accounts["account_profile_component_1"] = account_profile_component_1


 """
 
 """
 example ="""
const @@PageName@@ = () => {

};

export default @@PageName@@;
 """
 accounts["example"] = example
 