class ReportWebVitals:

 reportWebVitals = {}
 
 """
 reportWebVitals 1
 """
 web_vital_1 ="""
const @@PageName@@ = onPerfEntry => {
	if (onPerfEntry && onPerfEntry instanceof Function) {
    import('web-vitals').then(({ getCLS, getFID, getFCP, getLCP, getTTFB }) => {
      getCLS(onPerfEntry);
      getFID(onPerfEntry);
      getFCP(onPerfEntry);
      getLCP(onPerfEntry);
      getTTFB(onPerfEntry);
    });
  }
};

export default @@PageName@@;
 """
 reportWebVitals["web_vital_1"] = web_vital_1


 """
 reportWebVitals example
 """
 example ="""
const @@PageName@@ = onPerfEntry => {

};

export default @@PageName@@;
 """
 reportWebVitals["example"] = example
