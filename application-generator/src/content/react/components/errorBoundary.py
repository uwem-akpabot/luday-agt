class ErrorBoundaries:

 errorBoundaries = {}


 """
 ErrorBoundary 1 Component
 """
 error_boundary_1 ="""
import PropType from 'prop-types';
import React from 'react';

class @@PageName@@ extends React.Component {
	constructor(props) {
		super(props);
		this.state = { hasError: false };
	}

	static getDerivedStateFromError() {
		// Update state so the next render will show the fallback UI.
		return { hasError: true };
	}

	componentDidCatch(error, errorInfo) {
		console.log(error, errorInfo);
	}

	render() {
		const { hasError } = this.state;
		const { children } = this.props.children;
		if (this.state.hasError || hasError) {
		// Render custom fallback UI
		return (
			<div>
				<h1>Something went wrong.</h1>
			</div>
			);
		}

		return children; 
	}
}

@@PageName@@.propTypes = {
	children: PropType.oneOfType([
		PropType.arrayOf(PropType.node),
		PropType.node
	]).isRequired
};

export default @@PageName@@;
 """
 errorBoundaries["error_boundary_1"] = error_boundary_1
 