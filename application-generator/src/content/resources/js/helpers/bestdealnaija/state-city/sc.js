import stateList from '../../assets/states';
import localGovtList from '../../assets/local_govt';
import { compare } from '../utils'

function getAllStates() {
	return stateList;
}

function getAllLocalGovt() {
	return localGovtList;
}

function getLocalGovtOfState(stateCode) {
	if(!stateCode) return []
	const states = localGovtList.filter((value) => {
		return value.stateCode === stateCode;
	});
	return states.sort(compare);
}

export default {
	getAllStates,
	getAllLocalGovt,
	getLocalGovtOfState
};