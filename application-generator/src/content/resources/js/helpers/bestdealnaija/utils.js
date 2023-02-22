export const displayMoney = (n) => {
	const format = new Intl.NumberFormat('en-gb');

	return format.format(n);
};

export const calculateArrayTotal = (arr) => {
	if (!arr || arr?.length === 0) return 0;
  
	const total = arr.reduce((acc, val) => acc + val, 0);
  
	return total.toFixed(2);
};

export const compare = (a, b) => {
	if (a.name < b.name) return -1;
	if (a.name > b.name) return 1;
	return 0;
};

export const getReference = () => {
	let text = "";
	let possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

	for( let i=0; i < 15; i++ )
		text += possible.charAt(Math.floor(Math.random() * possible.length + (new Date()).getTime().toString()));

	return text;
};