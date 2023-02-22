class Forms:

 forms = {}
 

 '''
Billing Form
 '''
 billing_form ="""
import React, { useEffect } from 'react';
import { Link } from 'react-router-dom';

import PropType from 'prop-types';
import { Field, useFormikContext } from 'formik';

import { 
	CustomAccountCheckbox,
	CustomInput, CustomMobileInput, 
	CustomSelectCity, CustomSelectState, 
	CustomTextarea 
} from "../../components/formik";
import sc from '../../helpers/state-city/sc';

const @@PageName@@ = ({ auth, isOrderLoading }) => {
    const _states = sc.getAllStates();

	const updatedStates = _states.map((state) => ({
		label: state.name,
		value: state.name,
		...state
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
				<div className="mt-3 mb-3 w-auto md:w-[400px]">
					@@InputComponent1@@
				</div>
				<div className="mt-3 mb-3 w-auto md:w-[400px]">
					@@InputComponent2@@
				</div>
			</div>
			<div className="flex flex-col md:flex-row justify-between">
				<div className="mt-3 mb-3 w-auto md:w-[400px]">
					@@InputComponent3@@
				</div>
				<div className="mt-3 mb-3 w-auto md:w-[400px]">
					@@InputComponent4@@
				</div>
			</div>
			<div className="flex flex-col md:flex-row">
				<div className="mt-3 mb-3 w-auto md:w-full">
					@@InputComponent5@@
				</div>
			</div>
			<div className="flex flex-col md:flex-row justify-between">
				<div className="mt-3 mb-3 w-auto md:w-[400px]">
					@@InputComponent6@@
				</div>
				<div className="mt-3 mb-3 w-auto md:w-[400px]">
					@@InputComponent7@@
				</div>
			</div>
			{!auth && (
				@@InputAuthComponent1@@
			)}
			<div className="mt-10 flex justify-center">
				<button
					disabled={isOrderLoading}
					type="button" 
					className="button button--theme overflow-hidden bg-[#9c0] 
						hover:bg-[#84b000] text-white text-sm transition-all ease-in-out duration-300 
						rounded py-3 px-5 m-2 flex items-center flex-nowrap w-80 justify-center"
					onClick={handleSubmit}
				>
					<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" className="fill-current mr-2" ><path d="M5 21h14a2 2 0 0 0 2-2V8a1 1 0 0 0-.29-.71l-4-4A1 1 0 0 0 16 3H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2zm10-2H9v-5h6zM13 7h-2V5h2zM5 5h2v4h8V5h.59L19 8.41V19h-2v-5a2 2 0 0 0-2-2H9a2 2 0 0 0-2 2v5H5z"></path></svg>
					<span>{isOrderLoading ? '@@SubmitBtnOnLoadingText@@' : '@@SubmitBtnText@@'}</span>
				</button>
			</div>
			{!auth && (
				<p className="text-center">
					By clicking Save and continue, you agree to our 
					<Link to="/terms-and-conditions" 
						className="text-[#9c0]">Terms and Conditions
					</Link> and 
					<Link to="/privacy-policy" 
						className="text-[#9c0]">
						&nbsp;Privacy Policy
					</Link>
				</p>
			)}
		</>
	);
};

@@PageName@@.propTypes = {
  auth: PropType.bool.isRequired,
  isOrderLoading: PropType.bool.isRequired
};

export default @@PageName@@;
 """
 forms["billing_form"] = billing_form


 """
 Other form type
 """
# Add any other form type
 other_form ="""
const @@PageName@@ = () => {
    
}
export default @@PageName@@;
 """
 forms["other_form"] = other_form
