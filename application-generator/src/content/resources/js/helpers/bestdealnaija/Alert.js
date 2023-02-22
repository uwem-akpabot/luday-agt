import React from "react";
import PropType from 'prop-types';
import * as ROUTES from '../constants/routes'

const Alert = ({ status='info', mssg, type, state=true }) => {
	const [showAlert, setShowAlert] = React.useState(state);
	let _status;
	if (status === 'success') {
		_status = 'bg-[#9c0]'
	}
	if (status === 'info') {
		_status = 'bg-blue-500'
	}
	if (status === 'warning') {
		_status = 'bg-yellow-500'
	}
	if (status === 'error') {
		_status = 'bg-red-500'
	}
	return (
		<>
		{showAlert ? (
			<div className={
					"left-0 text-white px-3 lg:px:6 py-4 border-0 relative mt-10 md:mt-20 lg:mt-20 " +
					_status + 
				""}>
				<span className="text-xl inline-block mr-5 align-middle">
					<i className="fas fa-bell" />
				</span>
				{ type ==='support' &&
					<span className="inline-block align-middle mr-8">
						<b className="capitalize">{status}!</b>
						&nbsp;{mssg} Kindly contact support <a className="underline" href={ROUTES.CONTACT}>here</a>.
					</span>
				}
				{ type !=='support' &&
					<span className="inline-block align-middle mr-8">
						<b className="capitalize">{status}!</b>
						&nbsp;{mssg}
					</span>
				}
				<button
					className="absolute bg-transparent text-2xl font-semibold leading-none right-0 top-0 mt-6 md:mt-3 lg:mt-3 mr-6 outline-none focus:outline-none"
					onClick={() => setShowAlert(false)}>
					<span>×</span>
				</button>
			</div>
		) : null}
		</>
	);
};

Alert.propTypes = {
	status: PropType.string.isRequired,
	mssg: PropType.string.isRequired,
	type: PropType.string.isRequired,
	state: PropType.bool
};
  
export default Alert;