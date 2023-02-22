class Formik:

 formik = {}
 

 """
 CustomInput
 """
 index ="""
export { default as CustomInput } from './CustomInput';
export { default as CustomTextarea } from './CustomTextarea';
export { default as CustomAccountCheckbox } from './CustomAccountCheckbox';
export { default as CustomBankAccountNameInput } from './CustomBankAccountNameInput';
export { default as CustomMobileInput } from './CustomMobileInput';
export { default as CustomSelectState } from './CustomSelectState';
export { default as CustomSelectCity } from './CustomSelectCity';
export { default as CustomSelectBank } from './CustomSelectBank';
export { default as CustomFileInput } from './CustomFileInput';
 """
 formik["index"] = index
 '''
CustomAccountCheckbox
 '''
 custom_account_checkbox ="""
import React, { useState } from 'react';
import { Field, useField } from 'formik';

import CustomInput from './CustomInput';

const @@PageName@@ = (props) => {
  const [field, meta, helpers] = useField(props);
  const { touched, error } = meta;
  const { setValue } = helpers;

  const [isPreviousCheckoutValue, setPreviousCheckoutValue] = useState(false);
  const [isPasswordDivShown, setisPasswordDivShown] = useState(false);

  const handleChange = () => {
	if (!isPreviousCheckoutValue) {
		setPreviousCheckoutValue(true)
		setValue(true);
	} else {
		setPreviousCheckoutValue(false)
		setValue(false);
	}
	setisPasswordDivShown(!isPasswordDivShown);
  };

  return (
	<>
		<div className="flex flex-row itmes-center mt-2">
			<input
				type="checkbox"
				id={field.name}
				className={`text-black shadow-sm bg-white rounded mr-1
					${touched && error && 'border-red-500'}`}
				{...field}
				{...props}
				onChange={handleChange}
			/>
			<p className="pl-2"> Create my account with these details</p>
			{touched && error && (
				<span className="border-red-300 text-red-500">{error?.value}</span>
			)}
		</div>
		{isPasswordDivShown && <div className="flex flex-col md:flex-row justify-between">
			<div className="mt-3 mb-3 w-auto md:w-[400px]">
				<Field
					id="password" 
					name="password"
					placeholder="Your Password"
					type="password"
					label="Password"
					component={CustomInput}
					required={true}
				/>
			</div>
			<div className="mt-3 mb-3 w-auto md:w-[400px]">
				<Field
					id="password-confirmation" 
					name="password_confirmation"
					placeholder="Confirm Password"
					type="password"
					label="Confirm Password"
					component={CustomInput}
					required={true}
				/>
			</div>
		</div>}
	</>
  );  
};

export default @@PageName@@;
 """
 formik["custom_account_checkbox"] = custom_account_checkbox


 """
 CustomBankAccountNameInput
 """
 custom_bank_account_name_input ="""
/* eslint-disable react/prop-types */
/* eslint-disable no-extra-boolean-cast */
import React, { useEffect } from 'react';

import { Field, useField, useFormikContext } from 'formik';

async function fetchAccountName(acctNo, bankCode) {
	await new Promise((r) => setTimeout(r, 500));
	const requestOptions = {
		method: "GET",
		headers: {
			'Content-Type':'application/json',
			'Authorization': `Bearer ${process.env.REACT_APP_PAYSTACK_SECRET_KEY}` // eslint-disable-line
		}
	}
	const response = await fetch(`https://api.paystack.co/bank/resolve?account_number=${acctNo}&bank_code=${bankCode}`, requestOptions)
			.then(res => res.json())
			.then(data =>{
				return data
			})
			.catch(err => console.log(err))
	if (response && response.status == true) {
		return response.data.account_name;
	} else {
		alert('Account name not found.')
		return ''
	}
}

const @@PageName@@ = (props) => {
    const {
		values: { bank_name, bank_acct_number },
		setFieldValue
	} = useFormikContext();
	const [field, meta] = useField(props);

	useEffect(() => {
		let isCurrent = true;
		if (bank_name !== {} && bank_acct_number.length == 10) {
			fetchAccountName(bank_acct_number, bank_name.value).then((bank_account_name) => {
				if (!!isCurrent) {
					// prevent setting old values
					setFieldValue(props.name, bank_account_name);
				}
			});
		}
		return () => {
			isCurrent = false;
		};
	}, [bank_acct_number, bank_name, setFieldValue, props.name]);

	return (
		<>
			<label className="block text-sm font-medium text-gray-700 undefined" 
				htmlFor={field.name}>
				{"Bank Account Name"}<span className='text-red-500'> *</span>
			</label>
			<div className="flex flex-col items-start">
				<Field
					disabled={true}
					type="text"
					name={field.name}
					className={`block w-full text-gray-700 focus:ring focus:ring-green-200 focus:ring-opacity-50 
						shadow-sm border focus:border-green-300 border-gray-300 rounded py-2 px-4
						${!!meta.touched && !!meta.error && 'border-red-500'}`}
					{...field}
					{...props}
				/>
				{!!meta.touched && !!meta.error && (
					<span className="border-red-300 text-red-500">{meta.error}</span>
				)}
			</div>
		</>
	);
};

export default @@PageName@@;
 """
 formik["custom_bank_account_name_input"] = custom_bank_account_name_input


 """
 CustomFileInput
 """
 custom_file_input ="""
import React from 'react';

import PropType from 'prop-types';
import { useField } from 'formik';

const @@PageName@@ = (props) => {
   const [field, meta] = useField(props);
	const { label } = props;
	const { touched, error } = meta;
  
	return (
		<div className="">
			<label className="block text-sm font-medium text-gray-700 undefined" 
				htmlFor={field.name}>
				{label}<span className='text-red-500'> *</span>
			</label>
			<input
				type="file"
				hidden
				accept="image/png,image/x-png,image/jpeg,image/webp"
				className={`block w-full text-gray-700 cursor-pointer bg-gray-50 focus:ring focus:ring-green-200 focus:ring-opacity-50 
					shadow-sm border focus:border-green-300 border-gray-300 rounded px-4
					${touched && error && 'border-red-500'}`}
				{...field}
				{...props}
				required
			/>
			{touched && error && (
				<span className="border-red-300 text-red-500">{error}</span>
			)}
		</div>
	); 
};
  
@@PageName@@.propTypes = {
	label: PropType.string
};

export default @@PageName@@;
 """
 formik["custom_file_input"] = custom_file_input


 """
 CustomInput
 """
 custom_input ="""
import PropType from 'prop-types';
import React from 'react';

const @@PageName@@ = ({
  field, form: { touched, errors }, label, required, inputRef, ...props
}) => (
   <div className="">
		{required ?
			<label className="block text-sm font-medium text-gray-700 undefined" 
				htmlFor={field.name}>
				{label}<span className='text-red-500'> *</span>
			</label> :
			<label className="block text-sm font-medium text-gray-700 undefined" 
				htmlFor={field.name}>
				{label}
			</label>
		}
		<div className="flex flex-col items-start">
			<input
				type="text"
				id={field.name}
				className={`block w-full text-gray-700 focus:ring focus:ring-green-200 focus:ring-opacity-50 
					shadow-sm border focus:border-green-300 border-gray-300 rounded py-2 px-4
					${touched[field.name] && errors[field.name] && 'border-red-500'}`}
				ref={inputRef}
				{...field}
				{...props}
			/>
			{touched[field.name] && errors[field.name] && (
				<span className="border-red-300 text-red-500">{errors[field.name]}</span>
			)}
		</div>
	</div> 
);

@@PageName@@.defaultProps = {
	required: false,
	inputRef: undefined
};

@@PageName@@.propTypes = {
  label: PropType.string.isRequired,
  required: PropType.bool,
  field: PropType.object.isRequired,
  form: PropType.object.isRequired,
  inputRef: PropType.oneOfType([
    PropType.func,
    PropType.shape({ current: PropType.instanceOf(Element) })
  ])
};

export default @@PageName@@;
 """
 formik["custom_input"] = custom_input


 """
 CustomMobileInput
 """
 custom_mobile_input ="""
import { useField } from 'formik';
import PropType from 'prop-types';
import React from 'react';
import PhoneInput from 'react-phone-input-2';
import 'react-phone-input-2/lib/style.css'
import '../../pages/account/styles/profile.css'

const @@PageName@@ = (props) => {
   const [field, meta, helpers] = useField(props);
  const { label, placeholder, required } = props;
  const { touched, error } = meta;
  const { setValue } = helpers;
  
  return (
    <div className="">
		{required ?
			<label className="block text-sm font-medium text-gray-700 undefined" 
				htmlFor={field.name}>
				{label}<span className='text-red-500'> *</span>
			</label> :
			<label className="block text-sm font-medium text-gray-700 undefined" 
				htmlFor={field.name}>
				{label}
			</label>
		}
		<PhoneInput
			id={field.name}
			country={'ng'}
			inputClass="block text-gray-700 focus:ring focus:ring-green-200 focus:ring-opacity-50 
			shadow-sm border focus:border-green-300 border-gray-300 rounded py-2 px-4"
			style={{
			border: touched && error ? 'border-red-500' : 'border-green-300'
			}}
			inputExtraProps={{ required: true }}
			onChange={setValue}
			placeholder={placeholder}
			value={field.value}
		/>
		{touched && error && (
			<span className="border-red-300 text-red-500">{error}</span>
		)}
    </div>
  );
};

@@PageName@@.defaultProps = {
  label: 'Mobile Number',
  placeholder: '8081122233',
  required: false
};

@@PageName@@.propTypes = {
  label: PropType.string,
  required: PropType.bool,
  placeholder: PropType.string
};

export default @@PageName@@;
 """
 formik["custom_mobile_input"] = custom_mobile_input


 """
 CustomSelectBank
 """
 custom_select_bank ="""
import React from 'react';

import { useField } from 'formik';
import PropType from 'prop-types';

import Select from 'react-select';

const @@PageName@@ = (props) => {
	const [field, meta, helpers] = useField(props);
	const { label, placeholder, defaultValue, options } = props;
	const { touched, error } = meta;
	const { setValue } = helpers;

	const handleChange = (value) => {
		const bank_name = {
			label: value.label,
			value: value.value
		};
		setValue(bank_name);
	};

	return (
		<div className="">
			<label className="block text-sm font-medium text-gray-700 undefined" 
				htmlFor={field.name}>
				{label}<span className='text-red-500'> *</span>
			</label>
			<Select
				name={field.name}
				id={field.name}
				className={`block w-full text-gray-700 focus:ring focus:ring-green-200 focus:ring-opacity-50 
					shadow-sm border focus:border-green-300 border-gray-300 rounded
					${touched && error && 'border-red-500'}`}
				inputExtraProps={{ required: true }}
				onChange={handleChange}
				placeholder={placeholder}
				defaultValue={defaultValue.value}
				options={options}
				theme={(theme) => ({
					...theme,
					borderRadius: 0,
					colors: {
						...theme.colors,
						primary25: '#B3B3B3',
						primary: 'green'
					}
				})}
			/>
			{touched && error && (
				<span className="border-red-300 text-red-500">{error.value}</span>
			)}
		</div>
	);
};

@@PageName@@.propTypes = {
	label: PropType.string,
	placeholder: PropType.string,
	defaultValue: PropType.any,
	options: PropType.any.isRequired
};

export default @@PageName@@;
 """
 formik["custom_select_bank"] = custom_select_bank


 """
 CustomSelectCity
 """
 custom_select_city ="""
import React from 'react';

import { useField } from 'formik';
import PropType from 'prop-types';

import Select from 'react-select';

const @@PageName@@ = (props) => {
	const [field, meta, helpers] = useField(props);
	const { label, placeholder, defaultValue, options } = props;
	const { touched, error } = meta;
	const { setValue } = helpers;

	const handleChange = (value) => {
		const state = {
			countryCode: value.countryCode,
			stateCode: value.stateCode,
			name: value.name,
			value: value.name
		};

		setValue(state);
	};

	return (
		<div className="">
			<label className="block text-sm font-medium text-gray-700 undefined" 
				htmlFor={field.name}>
				{label}<span className='text-red-500'> *</span>
			</label>
			<Select
				name={field.name}
				id={field.name}
				className={`block w-full text-gray-700 focus:ring focus:ring-green-200 focus:ring-opacity-50 
					shadow-sm border focus:border-green-300 border-gray-300 rounded
					${touched && error && 'border-red-500'}`}
				inputExtraProps={{ required: true }}
				onChange={handleChange}
				placeholder={placeholder}
				defaultValue={{ label: placeholder, value: defaultValue.value }}
				options={options}
				theme={(theme) => ({
					...theme,
					borderRadius: 0,
					colors: {
						...theme.colors,
						primary25: '#B3B3B3',
						primary: 'green'
					}
				})}
			/>
			{touched && error && (
				<span className="border-red-300 text-red-500">{error.value}</span>
			)}
		</div>
	);
};

@@PageName@@.propTypes = {
  label: PropType.string,
  placeholder: PropType.string,
  defaultValue: PropType.any,
  options: PropType.any.isRequired
};

export default @@PageName@@;
 """
 formik["custom_select_city"] = custom_select_city


 """
 CustomSelectState
 """
 custom_select_state ="""
import React from 'react';

import { useField } from 'formik';
import PropType from 'prop-types';

import Select from 'react-select';

const @@PageName@@ = (props) => {
	const [field, meta, helpers] = useField(props);
	const { label, placeholder, defaultValue, options } = props;
	const { touched, error } = meta;
	const { setValue } = helpers;
	const handleChange = (value) => {
		const state = {
			countryCode: value.countryCode,
			isoCode: value.isoCode,
			label: value.label,
			latitude: value.latitude,
			longitude: value.longitude,
			name: value.name,
			value: value.name
		};

		setValue(state);
	};


	return (
		<div className="">
			<label className="block text-sm font-medium text-gray-700 undefined" 
				htmlFor={field.name}>
				{label}<span className='text-red-500'> *</span>
			</label>
			<Select
				name={field.name}
				id={field.name}
				className={`block w-full text-gray-700 focus:ring focus:ring-green-200 focus:ring-opacity-50 
					shadow-sm border focus:border-green-300 border-gray-300 rounded
					${touched && error && 'border-red-500'}`}
				inputExtraProps={{ required: true }}
				onChange={handleChange}
				placeholder={placeholder}
				defaultValue={{ label: placeholder, value: defaultValue.value }}
				options={options}
				theme={(theme) => ({
					...theme,
					borderRadius: 0,
					colors: {
						...theme.colors,
						primary25: '#B3B3B3',
						primary: 'green'
					}
				})}
			/>
			{touched && error && (
				<span className="border-red-300 text-red-500">{error.value}</span>
			)}
		</div>
	);
};

@@PageName@@.propTypes = {
  label: PropType.string,
  placeholder: PropType.string,
  defaultValue: PropType.any,
  options: PropType.any.isRequired
};

export default @@PageName@@;
 """
 formik["custom_select_state"] = custom_select_state


 """
 CustomTextarea
 """
 custom_text_area ="""
/* eslint-disable react/jsx-props-no-spreading */
/* eslint-disable react/forbid-prop-types */
import PropType from 'prop-types';
import React from 'react';

const @@PageName@@ = ({
  field, form: { touched, errors }, label, required, inputRef, ...props
}) => (
	<div className="">
		{required ?
			<label className="block text-sm font-medium text-gray-700 undefined" 
				htmlFor={field.name}>
				{label}<span className='text-red-500'> *</span>
			</label> :
			<label className="block text-sm font-medium text-gray-700 undefined" 
				htmlFor={field.name}>
				{label}
			</label>
		}
		<div className="flex flex-col items-start">
			<textarea
				type="textarea"
				id={field.name}
				className={`block w-full text-gray-700 focus:ring focus:ring-green-200 focus:ring-opacity-50 
					shadow-sm border focus:border-green-300 border-gray-300 rounded py-2 px-4
					${touched[field.name] && errors[field.name] && 'border-red-500'}`}
				ref={inputRef}
				{...field}
				{...props}
			/>
			{touched[field.name] && errors[field.name] && (
				<span className="border-red-300 text-red-500">{errors[field.name]}</span>
			)}
		</div>
	</div>
);

@@PageName@@.defaultProps = {
	required: false,
	inputRef: undefined
};

@@PageName@@.propTypes = {
  label: PropType.string.isRequired,
  required: PropType.bool,
  field: PropType.object.isRequired,
  form: PropType.object.isRequired,
  inputRef: PropType.oneOfType([
    PropType.func,
    PropType.shape({ current: PropType.instanceOf(Element) })
  ])
};

export default @@PageName@@;
 """
 formik["custom_text_area"] = custom_text_area


 """
 CustomType Example
 """
 custom_input_type ="""
const @@PageName@@ = (props) => {
    
}
export default @@PageName@@;
 """
 formik["custom_input_type"] = custom_input_type
