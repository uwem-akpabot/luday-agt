const stateList = [
	{
		"name": "Abia",
		"isoCode": "AB",
		"countryCode": "NG",
		"latitude": "5.45273540",
		"longitude": "7.52484140"
	},
	{
		"name": "Adamawa",
		"isoCode": "AD",
		"countryCode": "NG",
		"latitude": "9.32647510",
		"longitude": "12.39838530"
	},
	{
		"name": "Akwa Ibom",
		"isoCode": "AK",
		"countryCode": "NG",
		"latitude": "4.90573710",
		"longitude": "7.85366750"
	},
	{
		"name": "Anambra",
		"isoCode": "AN",
		"countryCode": "NG",
		"latitude": "6.22089970",
		"longitude": "6.93695590"
	},
	{
		"name": "Bauchi",
		"isoCode": "BA",
		"countryCode": "NG",
		"latitude": "10.77606240",
		"longitude": "9.99919430"
	},
	{
		"name": "Benue",
		"isoCode": "BE",
		"countryCode": "NG",
		"latitude": "7.33690240",
		"longitude": "8.74036870"
	},
	{
		"name": "Borno",
		"isoCode": "BO",
		"countryCode": "NG",
		"latitude": "11.88463560",
		"longitude": "13.15196650"
	},
	{
		"name": "Bayelsa",
		"isoCode": "BY",
		"countryCode": "NG",
		"latitude": "4.77190710",
		"longitude": "6.06985260"
	},
	{
		"name": "Cross River",
		"isoCode": "CR",
		"countryCode": "NG",
		"latitude": "5.87017240",
		"longitude": "8.59880140"
	},
	{
		"name": "Delta",
		"isoCode": "DE",
		"countryCode": "NG",
		"latitude": "33.74537840",
		"longitude": "-90.73545080"
	},
	{
		"name": "Ebonyi",
		"isoCode": "EB",
		"countryCode": "NG",
		"latitude": "6.26492320",
		"longitude": "8.01373020"
	},
	{
		"name": "Edo",
		"isoCode": "ED",
		"countryCode": "NG",
		"latitude": "6.63418310",
		"longitude": "5.93040560"
	},
	{
		"name": "Ekiti",
		"isoCode": "EK",
		"countryCode": "NG",
		"latitude": "7.71898620",
		"longitude": "5.31095050"
	},
	{
		"name": "Enugu",
		"isoCode": "EN",
		"countryCode": "NG",
		"latitude": "6.53635300",
		"longitude": "7.43561940"
	},
	{
		"name": "Federal Capital Territory",
		"isoCode": "FC",
		"countryCode": "NG",
		"latitude": "8.89406910",
		"longitude": "7.18604020"
	},
	{
		"name": "Gombe",
		"isoCode": "GO",
		"countryCode": "NG",
		"latitude": "10.36377950",
		"longitude": "11.19275870"
	},
	{
		"name": "Imo",
		"isoCode": "IM",
		"countryCode": "NG",
		"latitude": "5.57201220",
		"longitude": "7.05882190"
	},
	{
		"name": "Jigawa",
		"isoCode": "JI",
		"countryCode": "NG",
		"latitude": "12.22801200",
		"longitude": "9.56158670"
	},
	{
		"name": "Kebbi",
		"isoCode": "KE",
		"countryCode": "NG",
		"latitude": "11.49420030",
		"longitude": "4.23333550"
	},
	{
		"name": "Kaduna",
		"isoCode": "KD",
		"countryCode": "NG",
		"latitude": "10.37640060",
		"longitude": "7.70945370"
	},
	{
		"name": "Kano",
		"isoCode": "KN",
		"countryCode": "NG",
		"latitude": "11.74706980",
		"longitude": "8.52471070"
	},
	{
		"name": "Kogi",
		"isoCode": "KO",
		"countryCode": "NG",
		"latitude": "7.73373250",
		"longitude": "6.69058360"
	},
	{
		"name": "Katsina",
		"isoCode": "KT",
		"countryCode": "NG",
		"latitude": "12.37967070",
		"longitude": "7.63057480"
	},
	{
		"name": "Kwara",
		"isoCode": "KW",
		"countryCode": "NG",
		"latitude": "8.96689610",
		"longitude": "4.38740510"
	},
	{
		"name": "Lagos",
		"isoCode": "LA",
		"countryCode": "NG",
		"latitude": "6.52437930",
		"longitude": "3.37920570"
	},
	{
		"name": "Nassarawa",
		"isoCode": "NA",
		"countryCode": "NG",
		"latitude": "8.49979080",
		"longitude": "8.19969370"
	},
	{
		"name": "Niger",
		"isoCode": "NI",
		"countryCode": "NG",
		"latitude": "9.93092240",
		"longitude": "5.59832100"
	},
	{
		"name": "Ogun",
		"isoCode": "OG",
		"countryCode": "NG",
		"latitude": "6.99797470",
		"longitude": "3.47373780"
	},
	{
		"name": "Ondo",
		"isoCode": "ON",
		"countryCode": "NG",
		"latitude": "6.91486820",
		"longitude": "5.14781440"
	},
	{
		"name": "Osun",
		"isoCode": "OS",
		"countryCode": "NG",
		"latitude": "7.56289640",
		"longitude": "4.51995930"
	},
	{
		"name": "Oyo",
		"isoCode": "OY",
		"countryCode": "NG",
		"latitude": "8.15738090",
		"longitude": "3.61465340"
	},
	{
		"name": "Plateau",
		"isoCode": "PL",
		"countryCode": "NG",
		"latitude": "9.21820930",
		"longitude": "9.51794880"
	},
	{
		"name": "Rivers",
		"isoCode": "RI",
		"countryCode": "NG",
		"latitude": "5.02134200",
		"longitude": "6.43760220"
	},
	{
		"name": "Sokoto",
		"isoCode": "SO",
		"countryCode": "NG",
		"latitude": "13.05331430",
		"longitude": "5.32227220"
	},
	{
		"name": "Taraba",
		"isoCode": "TA",
		"countryCode": "NG",
		"latitude": "7.99936160",
		"longitude": "10.77398630"
	},
	{
		"name": "Yobe",
		"isoCode": "YO",
		"countryCode": "NG",
		"latitude": "12.29387600",
		"longitude": "11.43904110"
	},
	{
		"name": "Zamfara",
		"isoCode": "ZA",
		"countryCode": "NG",
		"latitude": "12.12218050",
		"longitude": "6.22358190"
	}
];

export default stateList;