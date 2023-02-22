class PageLayouts:

 layouts = {}

 '''
 LAYOUT index

 String used for creating index.js
 
    Variables:
        @@LandingPage@@: String representing the name of Landing page Component e.g "Home"
 '''
 layout_index_1 ="""
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import @@LandingPag@@ from './@@LandingPage@@';

ReactDOM.render(
  <@@LandingPage@@ />,
  document.getElementById('root')
);
"""
 layouts["layout_index_1"] = layout_index_1

 layout_index_2 ="""
import React from 'react';
import ReactDOM from 'react-dom';
import @@AppPage@@ from './@@AppPage@@';
import './index.css';
@@importPackage@@

ReactDOM.render(
  <React.StrictMode>
    <@@AppPage@@ />
  </React.StrictMode>,
  document.getElementById('root')
);
"""
 layouts["layout_index_2"] = layout_index_2

 layout_redux_index_1 ="""
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import configureStore from './redux/store/store';
import { onAuthStateFail, onAuthStateSuccess
} from './redux/actions/authActions';

import @@AppPage@@ from './@@AppPage@@';
import reportWebVitals from './reportWebVitals';

const { store, persistor } = configureStore();
const root = document.getElementById('root');

let auth_tokens = JSON.parse(localStorage.getItem('auth_tokens'));
let user = JSON.parse(localStorage.getItem('user'));

if (user && auth_tokens) {
  store.dispatch(onAuthStateSuccess(user));
} else {
  store.dispatch(onAuthStateFail('Failed to authenticate'));
}


ReactDOM.render(
  <React.StrictMode>
    <App store={store} persistor={persistor} />
  </React.StrictMode>,
  root
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
"""
 layouts["layout_redux_index_1"] = layout_redux_index_1


 layout_webui_redux_index_1 ="""
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import @@AppPage@@ from './@@AppPage@@';
import reportWebVitals from './reportWebVitals';
const root = document.getElementById('root');

ReactDOM.render(
  <React.StrictMode>
    <@@AppPage@@ />
  </React.StrictMode>,
  root
);
reportWebVitals();
"""
 layouts["layout_webui_redux_index_1"] = layout_webui_redux_index_1
 

 """
 Page index file
 """
 page_index ="""
/** Static */
export { default as Home } from './static/Home';
export { default as About } from './static/About';
export { default as Blog } from './static/Blog';
export { default as Contact } from './Contact/index';
export { default as FindDeal } from './deals/FindDeal';
export { default as TradeFair } from './deals/TradeFair';
export { default as UsersGuide } from './static/UsersGuide';
export { default as OwnersGuide } from './static/OwnersGuide';
/** Auth */
export { default as SignIn } from './auth/SignIn';
export { default as SignUp } from './auth/SignUp';
export { default as SignUpVendor } from './auth/SignUpVendor';
export { default as SignUpVendorsDetails } from './auth/SignUpVendorsDetails';
export { default as SignUpVendorComplete } from './auth/SingUpComplete';
export { default as ForgotPassword } from './auth/ForgotPassword';
export { default as ResetPassword } from './auth/ResetPassword';
/** Admin */
export { default as AdminDashboard} from './admin/AdminDashboard';
export { default as Categories} from './admin/categories/Categories';
export { default as EditCategories } from './admin/categories/EditCategories';
export { default as AllProducts } from './admin/products/Products';
export { default as AddProduct } from './admin/products/AddProduct';
export { default as EditProduct } from './admin/products/EditProduct';
export { default as AllVendors } from './admin/vendors/Vendors';
export { default as AddVendor } from './admin/vendors/AddVendor';
export { default as EditVendor } from './admin/vendors/EditVendor';
export { default as ViewVendor } from './admin/vendors/ViewVendor';
export { default as VerifyVendors } from './admin/vendors/UnVerifiedVendors';
export { default as Orders } from './admin/orders/Orders';
export { default as ViewOrder } from './admin/orders/ViewOrder';
export { default as VerifyProduct } from './admin/products/VerifyProduct';
export { default as ViewProductDetails } from './admin/products/ViewProductDetails';
/** Product */
export { default as Products } from './product/Products';
export { default as ProductDetails } from './product/ProductDetails';
export { default as CategoryProducts } from './product/CategoryProducts';
export { default as SearchProducts } from './product/Search';
export { default as VendorProduct } from './product/VendorProducts';
/** Checkout */
export { default as Cart } from './checkouts/Cart';
export { default as Checkout } from './checkouts/Checkouts';
export { default as Delivery } from './checkouts/Delivery';
export { default as Paymemt } from './checkouts/Payment';
export { default as BillingForm } from './checkouts/BillingForm';
export { default as PaystackCallback } from './checkouts/callback/PaystackCallback';
export { default as CashOnDeliveryCallback } from './checkouts/callback/CashOnDeliveryCallback';
/** Vendor */
export { default as VendorDasboard } from './vendor/VendorDashboard';
export { default as Vendors } from './vendor/Vendors';
export { default as VendorDetails } from './vendor/VendorDetails';
export { default as VendorAddProduct } from './vendor/products/AddProduct';
export { default as VendorProducts } from './vendor/products/ViewProducts';
export { default as VendorEditProduct } from './vendor/products/EditProduct';
export { default as VendorOrder } from './vendor/orders/Orders';
/** Account */
export { default as Profile } from './account/Profile';
export { default as EditForm } from './account/EditForm'
export { default as ChangePassword } from './account/ChangePassword';
export { default as OrderHistory } from './account/OrderHistory';
export { default as OrderDetails } from './account/OrderDetails';

/** Blog */
export { default as AllBlogs } from './admin/blogs/Blogs';
export { default as AddBlog } from './admin/blogs/AddBlog';
export { default as EditBlog } from './admin/blogs/EditBlog';
export { default as BlogDetails } from './static/BlogDetails';

/** User */
export { default as Users } from './admin/users/Users';
export { default as CreateAdmin } from './admin/users/CreateAdmin';
export { default as ManageAdmins } from './admin/users/ManageAdmins';
export { default as EditAdmins } from './admin/users/EditAdmins';
 """
 layouts["page_index"] = page_index


 """
 Product Page index file
 """
 product_page_index ="""
export { default as CategoryProducts } from './CategoryProducts';
export { default as ProductDetails } from './ProductDetails';
export { default as ProductItem } from './ProductItem';
export { default as ProductList } from './ProductList'
export { default as Products } from './Products';
 """
 layouts["product_page_index"] = product_page_index


 """
 Page index file
 """
 default_component_page_index ="""
export { default as Navigation } from './Navigation/main/index';
export { default as Footer } from './Footer/index';
export { default as Banner } from './Banner/index';
export { default as Slider } from './Slider';
export { default as ErrorBoundary } from './ErrorBoundary'
export { default as Pagination } from './Pagination';
export { default as Preloader } from './Preloader';
export { default as Search } from './Search';
export { default as Topic } from './Topic';
export { default as Owners_Topic } from './Owners_Topic';
 """
 layouts["default_component_page_index"] = default_component_page_index


 """
 Account Component index file
 """
 account_compenent_index ="""
export { default as AccountProfile } from './AccountProfile';
 """
 layouts["account_compenent_index"] = account_compenent_index


 """
 Admin Component index file
 """
 admin_compenent_index ="""
export { default as Dashboard } from './Dashboard';
 """
 layouts["admin_compenent_index"] = admin_compenent_index


 """
 Checkout Component index file
 """
 checkout_compenent_index ="""
export { default as OrderDetails } from './OrderDetails';
export { default as PaymentMethods } from './PaymentMethods';
export { default as Timeline } from './Timeline';
 """
 layouts["checkout_compenent_index"] = checkout_compenent_index


 """
 
 """
 layout_app_1 ="""
import React from 'react';
import {
  BrowserRouter as Router,
  Routes,
  Route
} from 'react-router-dom';
import @@LandingPage@@ from './@@LandingPage@@';
import @@Page1@@ from './@@Page1@@';

function App() {
  return (
  <>
    <Router>
      <Routes>
        <Route path="/" element={<@@LandingPage@@ />} />
        <Route path="/@@Path1@@" element={<@@Page1@@ />} />
      </Routes>
    </Router>
  </>
);
}

export default App;
"""
 layouts["layout_app_1"] = layout_app_1

 layout_app_2 ="""
import React, { useState, useEffect } from 'react';
import { IoIosArrowUp } from "react-icons/io";
import {
  BrowserRouter as Router,
  Routes,
  Route
} from 'react-router-dom';
import @@LandingPage@@ from './@@LandingPage@@';
import @@Component1@@ from './@@Component1@@';
import @@Component7@@ from './@@Component7@@';
import @@PageName1@@ from './@@PageName1@@';
import @@PageName2@@ from './@@PageName2@@';
import @@PageName3@@ from './@@PageName3@@';
import @@PageName4@@ from './@@PageName4@@';
import @@PageName5@@ from './@@PageName5@@';
import @@PageName6@@ from './@@PageName6@@';
import @@PageName7@@ from './@@PageName7@@';
import @@PageName8@@ from './@@PageName8@@';
import @@PageName9@@ from './@@PageName9@@';
import @@PageName10@@ from './@@PageName10@@';
import @@PageName11@@ from './@@PageName11@@';
import @@PageName12@@ from './@@PageName12@@';
import @@PageName13@@ from './@@PageName13@@';
import @@PageName14@@ from './@@PageName14@@';
import @@PageName15@@ from './@@PageName15@@';
import @@PageName16@@ from './@@PageName16@@';
import @@PageName17@@ from './@@PageName17@@';

import './App.css';


function App() {
  const [showButton, setShowButton] = useState(false);

  useEffect(() => {
    window.addEventListener("scroll", () => {
        if (window.pageYOffset > 300) {
          setShowButton(true);
        } else {
          setShowButton(false);
        }
      });
    }, []);

    const scrollToTop = () => {
      window.scrollTo({
        top: 0,
        behavior: 'smooth' // for smoothly scrolling
      });
    };
    return (
    <div>
      <Router>
        <@@Component1@@ />
          <@@PageName15@@>
            <Routes>
              <Route exact path="/" element={<@@LandingPage@@ />} />
              <Route path="@@path1@@" element={<@@PageName1@@ />} />
              <Route path="@@path2@@" element={<@@PageName2@@ />} />
              <Route path="@@path3@@" element={<@@PageName3@@ />} />
              <Route path="@@path4@@" element={<@@PageName4@@ />} />
              <Route path="@@path5@@" element={<@@PageName5@@ />} />
              <Route path="@@path6@@" element={<@@PageName6@@ />} /> 
              <Route path="@@path7@@" element={<@@PageName7@@ />} /> 
              <Route path="@@path8@@" element={<@@PageName8@@ />} /> 
              <Route path="@@path9@@" element={<@@PageName9@@ />} /> 
              <Route path="@@path10@@" element={<@@PageName10@@ />} /> 
              <Route path="@@path11@@" element={<@@PageName11@@ />} /> 
              <Route path="@@path12@@" element={<@@PageName12@@ />} /> 
              <Route path="@@path13@@" element={<@@PageName13@@ />} /> 
              <Route path="@@path14@@" element={<@@PageName14@@ />} /> 
              <Route path="@@path15@@" element={<@@PageName16@@ />} /> 
              <Route path="@@path16@@" element={<@@PageName17@@ />} /> 
            </Routes>
          </@@PageName15@@>
        <@@Component7@@ />
      </Router>
      {showButton && (
        <button
          onClick={scrollToTop}
          className="fixed bottom-0 right-0 z-20 flex items-center justify-center w-10 h-10 mb-8 mr-8
            overflow-hidden bg-[#9c0]  hover:bg-yellow-300 text-gray-200 transition-all ease-in-out duration-300 rounded"
          >< IoIosArrowUp />
          </button>
        )}
    </div>
  );
}

export default App;
"""
 layouts["layout_app_2"] = layout_app_2


 layout_app_3 ="""
@@Imports@@

function App() {
  return (
    <>
      <AppRouter />
    </>
  );
}

export default App;
"""
 layouts["layout_app_3"] = layout_app_3

 layout_redux_app_1 ="""
 import React, { useState, useEffect, StrictMode } from 'react';
 @@Imports@@

function App({ store, persistor }){
  useScrollTop();
  useSetAuthPersistence(store);

  const [showButton, setShowButton] = useState(false);
  const scrollHandler = () => {
    if (window.pageYOffset > 300) {
      setShowButton(true);
    } else {
      setShowButton(false);
    }
  };
  const scrollToTop = () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth' // for smoothly scrolling
    });
  };

  useEffect(() => {
    window.addEventListener('scroll', scrollHandler);
    return () => window.removeEventListener('scroll', scrollHandler);
  }, []);

  return (
    <div className="p-0">
      <StrictMode>
        <Provider store={store}>
          <PersistGate loading={<Preloader />} persistor={persistor}>
            <AppRouter />
          </PersistGate>
        </Provider>
      </StrictMode>     

      {showButton && (
        <button
          onClick={scrollToTop}
          className="fixed bottom-0 right-0 z-20 flex items-center justify-center w-10 h-10 mb-8 mr-8
            overflow-hidden bg-[#9c0]  hover:bg-[#84b000] text-gray-200 transition-all ease-in-out duration-300 rounded"
          ><IoIosArrowUp />
          </button>
        )
      }
    </div>
  )
}

App.propTypes = {
  store: PropType.any.isRequired,
  persistor: PropType.any.isRequired
};

export default App;
"""
 layouts["layout_redux_app_1"] = layout_redux_app_1

 layout_approuter_1 ="""
@@Imports@@

export const history = createBrowserHistory();

const AppRouter = () => (
	<Router history={history}>
		<>
			<Routes>
				<Route  element={<StaticRoute />} >
					<Route
						element={<Home />}
						path={ROUTES.HOME}
					/>
					<Route
						element={<About />}
						path={ROUTES.ABOUT}
					/>
					<Route
						element={<Blog />}
						path={ROUTES.BLOG}
					/>
					<Route
						element={<BlogDetails />}
						path={ROUTES.BLOG_DETAILS}
					/>
					<Route
						element={<Services />}
						path={ROUTES.SERVICES}
					/>
					<Route
						element={<ServiceDetails />}
						path={ROUTES.SERVICES}
					/>
					<Route
						element={<Quote />}
						path={ROUTES.QUOTE}
					/>
					<Route
						element={<Contact />}
						path={ROUTES.CONTACT}
					/>					
				</Route>
			</Routes>
		</>
	</Router>	
);
  
export default AppRouter;
"""
 layouts["layout_approuter_1"] = layout_approuter_1

 layout_webui_redux_app_1 ="""
@@Imports@@
function App(){
  return (
    <>
        <p>Hello, </p>
        from the AGT Web UI
    </>
  )
}
export default App;
"""
 layouts["layout_webui_redux_app_1"] = layout_webui_redux_app_1

 '''
LAYOUT 1
╔═════════════════════════════════════════╗
║               @@Pos1@@                  ║
╚═════════════════════════════════════════╝
╔═════════════════════════════════════════╗
║               @@Pos2@@                  ║
║                                         ║
║                                         ║
╚═════════════════════════════════════════╝
╔═════════════════════════════════════════╗
║               @@Pos3@@                  ║
╚═════════════════════════════════════════╝
╔═════════════════════════════════════════╗
║               @@Pos7@@                  ║
║                                         ║
║                                         ║
╚═════════════════════════════════════════╝
 '''
 layout_1 ="""
import React from 'react';
@@Imports@@


const @@PageName@@ = () => {
  return (
	<div className="app">
    @@Pos2@@
    @@Pos3@@
	</ div>
  )
}
export default @@PageName@@;
"""
 layouts["layout_1"] = layout_1


 '''
LAYOUT 2
╔═════════════════════════════════════════╗
║               @@Pos1@@                  ║
╚═════════════════════════════════════════╝
╔═════════════════════════════════════════╗
║               @@Pos2@@                  ║
║                                         ║
║                                         ║
╚═════════════════════════════════════════╝
╔═════════════════════════════════════════╗
║               @@Pos3@@                  ║
╚═════════════════════════════════════════╝
╔═════════════════════════════════════════╗
║               @@Pos4@@                  ║
╚═════════════════════════════════════════╝
╔═════════════════════════════════════════╗
║               @@Pos5@@                  ║
╚═════════════════════════════════════════╝
╔═════════════════════════════════════════╗
║               @@Pos6@@                  ║
╚═════════════════════════════════════════╝
╔═════════════════════════════════════════╗
║               @@Pos7@@                  ║
╚═════════════════════════════════════════╝
╔═════════════════════════════════════════╗
║               @@Pos8@@                  ║
║                                         ║
║                                         ║
╚═════════════════════════════════════════╝
 '''
 layout_2 ="""
import React from 'react';
@@Imports@@


function @@PageName@@() {
  return (
	<div className="app">
		@@Pos1@@
    @@Pos2@@
    @@Pos3@@
    @@Pos4@@
    @@Pos5@@
    @@Pos6@@
    @@Pos7@@
    @@Pos8@@
	</ div>
  )
}
export default @@PageName@@;
"""
 layouts["layout_2"] = layout_2

 '''
LAYOUT 3
╔═════════════════════════════════════════╗
║               @@Pos1@@                  ║
╚═════════════════════════════════════════╝
╔═════════════════════════════════════════╗
║               @@Pos2@@                  ║
║                                         ║
║                                         ║
╚═════════════════════════════════════════╝
╔═════════╦═════════════════════╦═════════╗
║@@Pos3@@ ║     @@Pos4@@        ║@@Pos5@@ ║
╚═════════╩═════════════════════╩═════════╝
╔═════════╦═════════════════════╦═════════╗
║@@Pos6@@ ║     @@Pos7@@        ║@@Pos8@@ ║
╚═════════╩═════════════════════╩═════════╝
╔═════════╦═════════════════════╦═════════╗
║@@Pos9@@ ║    @@Pos10@@        ║@@Pos11@@║
╚═════════╩═════════════════════╩═════════╝
╔═════════╦═════════════════════╦═════════╗
║@@Pos12@@║     @@Pos13@@       ║@@Pos14@@║
╚═════════╩═════════════════════╩═════════╝
╔═════════════════════════════════════════╗
║               @@Pos15@@                 ║
╚═════════════════════════════════════════╝
 '''
 layout_3 ="""
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
@@Imports@@

function @@PageName@@() {
  return (
  <div>
   <table>
    <tr style={{border:"1px solid black"}}> @@Pos1@@ </tr>
    <tr>&#160;</tr>
    <tr style={{border:"1px solid black"}}> @@Pos2@@ </tr>
    <tr>&#160;</tr>
    <tr style={{border:"1px solid black"}}>
      <td style={{border:"1px solid black"}}>@@Pos3@@</td>
      <td style={{border:"1px solid black"}}>@@Pos4@@</td>
      <td style={{border:"1px solid black"}}>@@Pos5@@</td>
    </tr>
    <tr>&#160;</tr>
    <tr style={{border:"1px solid black"}}>
      <td style={{border:"1px solid black"}}>@@Pos6@@</td>
      <td style={{border:"1px solid black"}}>@@Pos7@@</td>
      <td style={{border:"1px solid black"}}>@@Pos8@@</td>
    </tr>
    <tr>&#160;</tr>
    <tr style={{border:"1px solid black"}}>
      <td style={{border:"1px solid black"}}>@@Pos9@@</td>
      <td style={{border:"1px solid black"}}>@@Pos10@@</td>
      <td style={{border:"1px solid black"}}>@@Pos11@@</td>
    </tr>
    <tr>&#160;</tr>
    <tr style={{border:"1px solid black"}}>
      <td style={{border:"1px solid black"}}>@@Pos12@@</td>
      <td style={{border:"1px solid black"}}>@@Pos13@@</td>
      <td style={{border:"1px solid black"}}>@@Pos14@@</td>
    </tr>
    <tr>&#160;</tr>
    <tr style={{border:"1px solid black"}}> @@Pos15@@ </tr>
    <tr>&#160;</tr>
  </table>
 </ div>
)
}
export default @@PageName@@;
 """
 layouts["layout_3"] = layout_3

 '''
LAYOUT 4
╔═════════════════════════════════════════╗
║               @@Pos1@@                  ║
╚═════════════════════════════════════════╝
╔═════════════════════════════════════════╗
║               @@Pos2@@                  ║
║                                         ║
║                                         ║
╚═════════════════════════════════════════╝
╔═════════════════════════════════════════╗
║               @@Pos3@@                  ║
╚═════════════════════════════════════════╝
╔═════════════════════════════════════════╗
║               @@Pos4@@                  ║
╚═════════════════════════════════════════╝
╔═════════════════════════════════════════╗
║               @@Pos5@@                  ║
║                                         ║
║                                         ║
╚═════════════════════════════════════════╝
 '''
 layout_4 ="""
import React from 'react';
@@Imports@@

function @@PageName@@() {
  useDocumentTitle('Home | BestDealNaija');
  useScrollTop();
  return (
    <div>
      @@Pos2@@
      <div className="text-center mt-12 md:mt-5">
        @@Pos3@@
      </div>
      @@Pos4@@
      @@Pos5@@
    </div>
  )
}
export default @@PageName@@;
"""
 layouts["layout_4"] = layout_4

 '''
LAYOUT 5
╔═════════════════════════════════════════╗
║               @@Pos1@@                  ║
╚═════════════════════════════════════════╝
╔═════════════════════════════════════════╗
║               @@Pos2@@                  ║
║                                         ║
║                                         ║
╚═════════════════════════════════════════╝
╔═════════════════════════════════════════╗
║               @@Pos5@@                  ║
║                                         ║
║                                         ║
╚═════════════════════════════════════════╝
 '''
 layout_5 ="""
import React from 'react';
@@Imports@@
function @@PageName@@() {
  useDocumentTitle('@@DocumentTitle@@');
  useScrollTop();

  return (
    <div className="app">
      
      @@Pos2@@
      
    </ div>
  )
}
export default @@PageName@@;
"""
 layouts["layout_5"] = layout_5

 layout_contact_1 ="""
import React, { useEffect, useState }  from 'react';
import { useForm } from 'react-hook-form';
import swal from 'sweetalert';
import axios from 'axios';
@@Imports@@

const AddressMap = () =>{
    return (
        <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d17013.36898552257!2d11.96485892048908!3d57.78995966847573!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x464ff5452c3bf293%3A0xb01907807f46533!2s425%2032%20Hisings%20K%C3%A4rra%2C%20Sweden!5e0!3m2!1sen!2sng!4v1619707943827!5m2!1sen!2sng" className="px-3 py-4 w-full h-96" allowfullscreen loading="lazy"></iframe>
    )
};

const API = "@@ReactAppAPI@@";

function LudayContact() {    
  const [getMessage, setGetMessage] = useState({})
  const {register, handleSubmit, reset, formState: { errors } } = useForm();

  const [name, setName] = useState('')
  const [email, setEmail] = useState('')

  const successAlert = (response) => {
    return(
      swal({
          title: "Info!",
          text: response,
          icon: "success",
      })              
    )
  }

  useEffect(()=>{
    axios.get(`${API}/api/contact`)
    .then(response => {
      setGetMessage(response)
    })
    .catch(error => {
      console.log(error)
    })

  }, [])

  const submitForm = (data) => {
    const body = {
      name: data.name,
      email: data.email,
      subject: data.subject,
      mobile: data.mobile,
      mssg: data.mssg
    }

    const requestOptions = {
        method: "POST",
        headers: {
          'content-type': 'application/json'
        },
        body: JSON.stringify(body)
    }

    fetch(`${API}/api/contact/add`, requestOptions)
      .then(res => res.json())
      .then(data =>{
        console.log(data)
        successAlert(data.message)
      })
      .catch(err => console.log(err))

    reset()
  }

  return (
    <div>
      @@NavBar@@
      <div className="w-full">
          <div className="h-96"></div>
            <div className="sm:px-6 lg:px-8 lg:mx-32 mb-12">
                <div className="bg-white w-full shadow-2xl rounded-md p-4 lg:p-10 -mt-72">
                    <div className="">
                        <h2 className="text-center text-xl text-blue-600 uppercase font-bold">@@TitleText@@</h2>                                    
                        <h2 className="mt-4 text-center text-3xl font-extrabold text-blue-900">See why the World's best companies use Luday to become truly web-driven</h2>
                    </div>
                    <form className='bg-blue-100 rounded-md shadow-2xl m-2 lg:m-12 lg:m-24 p-4'>
                        <div className="md:flex items-center mt-12">
                            <div className="w-full md:w-1/2 flex flex-col">
                                <input type="text" placeholder='Your Name' 
                                    {...register("name", { required: true, maxLength: 25 })}
                                    className="leading-none text-gray-900 p-3 focus:outline-none focus:border-blue-700
                                      mt-4 bg-white border rounded border-gray-200" />
                                {errors.name && <small class="text-red-500 text-xs italic">Your name is required</small>}
                                {errors.name?.type === "maxLength" && <p style={{ color: "red" }}><small>Max characters should be 25 </small></p>}
                            </div>
                            <div className="w-full md:w-1/2 flex flex-col md:ml-6 md:mt-0 mt-4">
                                <input type="number" placeholder='Phone' 
                                    {...register("mobile", { required: true, maxLength: 15 })}
                                    className="leading-none text-gray-900 p-3 focus:outline-none focus:border-blue-700 mt-4 bg-white border rounded border-gray-200"/>
                                {errors.mobile && <small class="text-red-500 text-xs italic">Your mobile number is required</small>}
                                {errors.mobile?.type === "maxLength" && <p style={{ color: "red" }}><small>Max characters should be 15 </small></p>}
                            </div>
                        </div>
                        <div className="md:flex items-center mt-12">
                            <div className="w-full md:w-1/2 flex flex-col">
                                <input type="email" placeholder='Your Email' 
                                    {...register("email", { required: true, maxLength: 100 })}
                                    className="leading-none text-gray-900 p-3 focus:outline-none focus:border-blue-700 mt-4 bg-white border rounded border-gray-200" />
                                {errors.email && <small class="text-red-500 text-xs italic">Your e-mail is required</small>}
                                {errors.email?.type === "maxLength" && <p style={{ color: "red" }}><small>Max characters should be 100 </small></p>}
                            </div>
                            <div className="w-full md:w-1/2 flex flex-col md:ml-6 md:mt-0 mt-4">
                                <input type="text" placeholder='Subject' 
                                    {...register("subject", { required: true, maxLength: 80 })}
                                    className="leading-none text-gray-900 p-3 focus:outline-none focus:border-blue-700 mt-4 bg-white border rounded border-gray-200"/>
                                {errors.subject && <small class="text-red-500 text-xs italic">Subject message is required</small>}
                                {errors.subject?.type === "maxLength" && <p style={{ color: "red" }}><small>Max characters should be 80 </small></p>}
                            </div>
                            
                        </div>
                        <div>
                            <div className="w-full flex flex-col mt-8">
                                <textarea type="text" placeholder='Message' 
                                    {...register("mssg", { required: true, maxLength: 255 })}
                                    className="h-40 text-base leading-none text-gray-900 p-3 focus:outline-none focus:border-blue-700 mt-4 bg-white border rounded border-gray-200"></textarea>
                                {errors.mssg && <small class="text-red-500 text-xs italic">Message is required</small>}
                                {errors.mssg?.type === "maxLength" && <p style={{ color: "red" }}><small>Max characters should be 255 </small></p>}
                            </div>
                        </div>
                        <div className="flex items-center justify-center w-full">
                            <button type='submit' 
                                onClick={handleSubmit(submitForm)}
                                className="mt-9 font-semibold leading-none text-white py-4 px-10 bg-blue-700 rounded-md hover:bg-blue-600 focus:ring-2 focus:ring-offset-2 focus:ring-blue-700 focus:outline-none">
                                Send messages
                            </button>
                        </div>
                    </form>

                    <div className='h-full w-full'>
                        <AddressMap />
                    </div>
            </div>
        </div>
      </div>
    </div>
  )
}

export default LudayContact;
 """
 layouts["layout_contact_1"] = layout_contact_1
 
 '''

LAYOUT 3
╔═════════════════════════════════════════╗
║               @@Pos1@@                  ║
╚═════════════════════════════════════════╝
╔═════════════════════════════════════════╗
║               @@Pos2@@                  ║
║                                         ║
║                                         ║
╚═════════════════════════════════════════╝
╔═════════╦═════════════════════╦═════════╗
║@@Pos3@@ ║     @@Pos4@@        ║         ║
╚═════════╩═════════════════════║         ║
╔═════════╦═════════════════════║         ║
║@@Pos6@@ ║     @@Pos7@@        ║         ║
╚═════════╩═════════════════════║         ║
╔═════════╦═════════════════════║@@Pos5@@ ║
║@@Pos8@@ ║    @@Pos9@@         ║         ║
╚═════════╩═════════════════════║         ║
╔═════════╦═════════════════════║         ║
║@@Pos10@@║    @@Pos11@@        ║         ║
╚═════════╩═════════════════════╩═════════╝
╔═════════════════════════════════════════╗
║              @@Pos12@@                  ║
╚═════════════════════════════════════════╝

LAYOUT 4
╔═════════════════════════════════════════╗
║               @@Pos1@@                  ║
╚═════════════════════════════════════════╝
╔═════════════════════════════════════════╗
║               @@Pos2@@                  ║
║                                         ║
║                                         ║
╚═════════════════════════════════════════╝
╔═════════╦═════════════════════╦═════════╗
║@@Pos3@@ ║                     ║         ║
║         ║                     ║         ║
║         ║     @@Pos4@@        ║         ║
║         ║                     ║         ║
╚═════════╩═════════════════════║         ║
╔═══════════════════════════════║@@Pos5@@ ║
║         @@Pos6@@              ║         ║
╚═══════════════════════════════║         ║
╔═══════════════════════════════║         ║
║         @@Pos7@@              ║         ║
╚═══════════════════════════════╩═════════╝
╔═════════════════════════════════════════╗
║               @@Pos8@@                  ║
╚═════════════════════════════════════════╝
 '''

 layout_blog_1 ="""
import React, {useEffect, useState } from 'react';
@@Imports@@
function @@PageName@@() {
  useDocumentTitle('@@DocumentTitle@@');
  useScrollTop();

  const [loading, setLoading] = useState(false);
  const [blogs, fetchBlogs] = useState([]);
  const getData = () => {
      setLoading(true)
      fetch(`${ROUTE.BLOGS_API}/blogs`)
        .then((res) => res.json())
        .then((res) => {
          fetchBlogs(res.results)
          //console.log(res.results)
          setLoading(false)
      })
  }
  useEffect(() => {
      getData()
  }, []);

  let blogList = ''
  if(blogs.length > 0){
      blogList =  (
          <section className="bg-gray-50 pt-20 md:pt-30">
              <div className="px-36 py-[100px] pb-[80px] luday_wrap">                    
                  <div className="grid grid-cols-3 gap-6 luday_grid_wrap">
                  {blogs.map(item => 
                      <div key={item.id} className="h-84 group bg-white shadow-sm">
                          <Link to={`${ROUTE.BLOG_DETAILS}/${item.slug}`}>
                          <article>
                              <div>
                                  <img className="lazy" src={`${CONSTANT.IMAGE_STORE}/${item.image_path}`} alt="" />
                              </div>
                              <div className="px-[30px] pt-8">
                                  <h4 className="hover:text-[#98c01d] text-xl tracking-tight">{item.title}</h4>
                                  <div>
                                      <p className="py-3 text-xs text-gray-500 tracking-tight">{item.created_at}</p>
                                  </div>
                                  <p className="h-36 text-ellipsis overflow-y-hidden"
                                  > {item.summary}</p>
                                  
                              </div>
                          </article>
                          </Link>
                      </div>
                  )}
                  </div>
              </div>
          </section>
      )
  } else {
    blogList =  (
      <div className="flex flex-col space-y-5 -mt-36 justify-center items-center text-xl font-medium tracking-wide text-green-700 text-center h-screen">
          <FaBlog className="w-32 h-32"/>
          <h1 className="font-semibold text-3xl tracking-wider">@@EmptyBlogMssg@@</h1>
      </div>)    
  }

  let blogsLoading = (
      <>
          <section className="bg-gray-100 pt-20 md:pt-30">
              <div className="px-36 py-[100px] pb-[80px] luday_wrap">                    
                  <div className="grid grid-cols-3 gap-9 luday_grid_wrap"> 
                      <div className="group bg-white">    
                          <article>
                              <div data-placeholder className="w-full h-60 bg-gray-200 overflow-hidden relative">
                              </div>
                              <div className="p-[30px]">
                                  <p data-placeholder className="h-7 mb-2 w-full md:w-4/5 bg-gray-200 overflow-hidden relative"></p>
                                  <div>
                                      <p  data-paceholder className="h-6 py-3 font-bold text-sm"></p>
                                  </div>
                                  <div data-placeholder className="w-full h-32 bg-gray-200 overflow-hidden relative">
                                  </div>
                              </div>
                          </article>
                      </div>
                      <div className="group bg-white">    
                          <article>
                              <div data-placeholder className="w-full h-60 bg-gray-200 overflow-hidden relative">
                              </div>
                              <div className="p-[30px]">
                                  <p data-placeholder className="h-7 mb-2 w-full md:w-4/5 bg-gray-200 overflow-hidden relative"></p>
                                  <div>
                                      <p  data-paceholder className="h-6 py-3 font-bold text-sm"></p>
                                  </div>
                                  <div data-placeholder className="w-full h-32 bg-gray-200 overflow-hidden relative">
                                  </div>
                              </div>
                          </article>
                      </div>
                      <div className="group bg-white">    
                          <article>
                              <div data-placeholder className="w-full h-60 bg-gray-200 overflow-hidden relative">
                              </div>
                              <div className="p-[30px]">
                                  <p data-placeholder className="h-7 mb-2 w-full md:w-4/5 bg-gray-200 overflow-hidden relative"></p>
                                  <div>
                                      <p  data-paceholder className="h-6 py-3 font-bold text-sm"></p>
                                  </div>
                                  <div data-placeholder className="w-full h-32 bg-gray-200 overflow-hidden relative">
                                  </div>
                              </div>
                          </article>
                      </div>
                  </div>
              </div>
          </section>
      </>
  )

  return (
    <div className="bg-gray-100">
        <div className="header bg-white h-16 px-10 py-8 border-b-2 border-gray-200 flex items-center justify-between">
              <div className="flex items-center space-x-2 text-gray-400">
                <span className="text-green-700 tracking-wider font-thin text-md"><Link to={ROUTE.ADMIN_DASHBOARD}>@@HomeLinkText@@</Link></span>
                <span>/</span>
                <span className="tracking-wide text-md">
                    <span className="text-base">@@PageTitle@@</span>
                </span>
                <span>/</span>
              </div>
        </div>
          { loading
          ? blogsLoading
          : blogList }
    </div>
  )  
}
export default @@PageName@@;
 """
 layouts["layout_blog_1"] = layout_blog_1


 """
 About layout 1
 """
 layout_about_1 ="""
import React from 'react';
@@Imports@@
function @@PageName@@() {
  const title = '@@Title@@';
  const subtitle = '@@SubTitle@@';
  useDocumentTitle('@@DocumentTitle@@');
  useScrollTop();

  return (
    <div>
     @@Pos1@@   
      <div className="px-[300px] pb-[80px] luday_wrap text-center content_about">
        <div className="text-center py-10 pt-20">
          <p className="tracking-widest text-xs text-gray-500">@@Title@@</p>
          <h3 className="text-6xl luday_deals">@@SubHeading3@@</h3>
        </div>
        <p><span className="font-bold">BestDealNaija.com</span> @@Paragraph1@@ </p>

        <p>@@Paragraph2@@</p>

        <h6><b>@@HeaderText6@@:</b></h6>
        * @@Description1@@<br />
        * @@Description2@@<br />
        * @@Description3@@<br />
        * @@Description4@@<br />
        * @@Description5@@<br />
        * @@Description6@@<br />
      </div>
    </div>
  )
}
export default @@PageName@@;
"""
 layouts["layout_about_1"] = layout_about_1


 """
 Blog details layout 1
 """
 layout_blog_details_1 ="""
import React, {useState, useEffect} from 'react';
@@Imports@@
function @@PageName@@() {
  useDocumentTitle('@@DocumentTitle@@');
  useScrollTop();

  const {slug} = useParams();
  const [blog, fetchBlog] = useState([]);
  const [loading, setLoading] = useState(false);

  const getData = () => {
    setLoading(true)
  fetch(`${ROUTE.BLOGS_API}/sblog/${slug}`)
    .then((res) => res.json())
    .then((res) => {
      fetchBlog(res.data[0])
      
      setLoading(false)
    })
  }
  useEffect(() => {
    getData()
  }, []);
  
  let blogdetails = ''
  if(blog){
    blogdetails =  (
      <div>
        <h1 className="py-2 mb-4 text-center text-4xl leading-10 md:text-6xl "><b>{blog.title}</b></h1>
        <div className="flex justify-center">
          <img className="lazy h-2/3 w-2/3" src={`${CONSTANT.IMAGE_STORE}/${blog.image_path}`} alt={blog.title}/>
        </div>
        <div className="h-auto mt-5" dangerouslySetInnerHTML={{ __html: blog.content }} />
      </div>
    )
  }
  else{
    blogdetails =  (
      <div className="flex flex-col space-y-5 -mt-36 justify-center items-center text-xl font-medium tracking-wide text-green-700 text-center h-screen">
          @@NoBlogIcon@@
          <h1 className="font-semibold text-3xl tracking-wider">@@NoBlogMssg@@</h1>
      </div>)
  }

  let blogsLoading = (
    <>
      <section className="bg-gray-100 pt-5">
          <div className="px-36 py-[10px] pb-[80px] luday_wrap">     
            <div className="group bg-white">    
                <article>
                  <div>
                      <p  data-paceholder className="h-6 py-[30px] my-10  bg-gray-200 font-bold text-sm"></p>
                  </div>
                  <div data-placeholder className="w-full h-60 bg-gray-200 overflow-hidden relative">
                  </div>
                  <div className="py-[30px]">
                    <p data-placeholder className="h-7 mb-2 w-full bg-gray-200 overflow-hidden relative"></p>
                    <p data-placeholder className="h-7 mb-2 w-full bg-gray-200 overflow-hidden relative"></p>
                    <p data-placeholder className="h-7 mb-2 w-full bg-gray-200 overflow-hidden relative"></p>
                    <p data-placeholder className="h-7 mb-2 w-full bg-gray-200 overflow-hidden relative"></p>
                    <p data-placeholder className="h-7 mb-2 w-full bg-gray-200 overflow-hidden relative"></p>
                  </div>
                  <div data-placeholder className="w-full h-60 bg-gray-200 overflow-hidden relative">
                  </div>
                  <div className="py-[30px]">
                    <p data-placeholder className="h-7 mb-2 w-full bg-gray-200 overflow-hidden relative"></p>
                    <p data-placeholder className="h-7 mb-2 w-full bg-gray-200 overflow-hidden relative"></p>
                    <p data-placeholder className="h-7 mb-2 w-full bg-gray-200 overflow-hidden relative"></p>
                    <p data-placeholder className="h-7 mb-2 w-full bg-gray-200 overflow-hidden relative"></p>
                    <p data-placeholder className="h-7 mb-2 w-full bg-gray-200 overflow-hidden relative"></p>
                  </div>
                </article>
            </div>
          </div>
      </section>
    </>
  )

  return (
      <>
        <div className="post-body my-20 pt-10 px-6 lg:px-[200px]">
        { loading
          ? blogsLoading
          : blogdetails }
        </div>
      </>
  );
}
export default @@PageName@@;
 """
 layouts["layout_blog_details_1"] = layout_blog_details_1


 """
 Vendor layout 1
 """
 layout_vendor_1 ="""
import React, {useEffect, useState } from 'react';
@@Imports@@
const @@PageName@@ = () => {
  useDocumentTitle('@@DocumentTitle@@');
  useScrollTop();

  const [loading, setLoading] = useState(false);
    const [vendors, fetchVendors] = useState([]);
    
    const getData = () => {
        setLoading(true)
      fetch(`${ROUTE.USER_API}/user/vendors`)
        .then((res) => res.json())
        .then((res) => {
            fetchVendors(res.results)
            console.log(res.results)
            setLoading(false)
        })
    }
    useEffect(() => {
        getData()
    }, []);
            
    let vendorsList = ''
    if(vendors.length > 0){
        vendorsList =  (
            <section className="bg-gray-100">
                <div className="px-3 md:px-10 lg:px-36 py-[100px] pb-[80px] luday_wrap">                    
                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-9 luday_grid_wrap">
                        {vendors.map(item => 
                            <div key={item.id} className="group bg-white">
                                <article>
                                    <div>
                                        <img className="lazy" src={`${CONSTANT.IMAGE_STORE}/${item.image}`} alt={item.business_name} />
                                    </div>
                                    <div className="p-[30px]">
                                        <div className="gis-text">
                                            <h2 className="text-2xl pb-4 font-semibold">{item.business_name}</h2>
                                            <div className="pb-7 text-ellipsis overflow-y-hidden h-12 overflow-x-hidden"
                                                dangerouslySetInnerHTML={{ __html: item.business_description }}></div>
                                            <div className="button-wrap mt-10">
                                                <Link to={`${ROUTE.VENDORDETAILS}/${item.slug}`} className="button button--theme 
                                                overflow-hidden bg-[#9c0] hover:bg-yellow-300 text-white text-bold transition-all ease-in-out duration-300 rounded py-3 px-7">
                                                @@PageTitle@@</Link>
                                            </div>
                                        </div>
                                    </div>
                                </article>
                            </div>
                        )}
                    </div>
                </div>
            </section>
        )
    } else {
        vendorsList =  (
            <div className="flex flex-col space-y-5 -mt-36 justify-center items-center text-xl font-medium tracking-wide text-green-700 text-center h-screen">
                <FaBlog className="w-32 h-32"/>
                <h1 className="font-semibold text-3xl tracking-wider">@@EmptyVendorMssg@@</h1>
            </div>
        )
    }
    let vendorsLoading = (
    <>
      <section className="bg-gray-100 pt-20 md:pt-30">
          <div className="px-36 py-[100px] pb-[80px] luday_wrap">                    
              <div className="grid grid-cols-3 gap-9 luday_grid_wrap"> 
                  <div className="group bg-white">    
                      <article>
                          <div data-placeholder className="w-full h-60 bg-gray-200 overflow-hidden relative">
                          </div>
                          <div className="p-[30px]">
                              <p data-placeholder className="h-7 mb-2 w-full md:w-4/5 bg-gray-200 overflow-hidden relative"></p>
                              <div>
                                  <p  data-paceholder className="h-6 py-3 font-bold text-sm"></p>
                              </div>
                              <div data-placeholder className="w-full h-32 bg-gray-200 overflow-hidden relative">
                              </div>
                              <div className="button-wrap mt-5 w-32">
                                  <p className="button button--theme 
                                  overflow-hidden bg-gray-200 transition-all ease-in-out duration-300 rounded py-3 px-7">
                                  </p>
                              </div>
                          </div>
                      </article>
                  </div>
                  <div className="group bg-white">    
                      <article>
                          <div data-placeholder className="w-full h-60 bg-gray-200 overflow-hidden relative">
                          </div>
                          <div className="p-[30px]">
                              <p data-placeholder className="h-7 mb-2 w-full md:w-4/5 bg-gray-200 overflow-hidden relative"></p>
                              <div>
                                  <p  data-paceholder className="h-6 py-3 font-bold text-sm"></p>
                              </div>
                              <div data-placeholder className="w-full h-32 bg-gray-200 overflow-hidden relative">
                              </div>
                              <div className="button-wrap mt-5 w-32">
                                  <p className="button button--theme 
                                  overflow-hidden bg-gray-200 transition-all ease-in-out duration-300 rounded py-3 px-7">
                                  </p>
                              </div>
                          </div>
                      </article>
                  </div>
                  <div className="group bg-white">    
                      <article>
                          <div data-placeholder className="w-full h-60 bg-gray-200 overflow-hidden relative">
                          </div>
                          <div className="p-[30px]">
                              <p data-placeholder className="h-7 mb-2 w-full md:w-4/5 bg-gray-200 overflow-hidden relative"></p>
                              <div>
                                  <p  data-paceholder className="h-6 py-3 font-bold text-sm"></p>
                              </div>
                              <div data-placeholder className="w-full h-32 bg-gray-200 overflow-hidden relative">
                              </div>
                              <div className="button-wrap mt-5 w-32">
                                  <p className="button button--theme 
                                  overflow-hidden bg-gray-200 transition-all ease-in-out duration-300 rounded py-3 px-7">
                                  </p>
                              </div>
                          </div>
                      </article>
                  </div>
              </div>
          </div>
      </section>
    </>
  )

  return (
    <>
      <div className="bg-gray-100">
          
      <Banner subtitleText="Vendors" backgroundImage={img} />
      {/* <div className="header bg-white h-16 px-10 py-8 border-b-2 border-gray-200 flex items-center justify-between">
            <div className="flex items-center space-x-2 text-gray-400">
              <span className="text-green-700 tracking-wider font-thin text-md"><Link to={ROUTE.ADMIN_DASHBOARD}>Home</Link></span>
              <span>/</span>
              <span className="tracking-wide text-md">
                  <span className="text-base">Blogs</span>
              </span>
              <span>/</span>
            </div>
      </div> */}
          { loading
          ? vendorsLoading
          : vendorsList }
      </div>    
    </>
  );  
}
export default @@PageName@@;
 """
 layouts["layout_vendor_1"] = layout_vendor_1

 """
 Vendor details layout 1
 """
 layout_vendor_details_1 ="""
import React, {useState, useEffect} from 'react';
@@Imports@@
const @@PageName@@ = () => {
  useDocumentTitle('@@DocumentTitle@@');
  useScrollTop();

  const {slug} = useParams();
  const [vendors, fetchVendors] = useState([]);

  const getData = () => {
    //setLoading(true)
  fetch(`${ROUTE.USER_API}/user/vendors/${slug}`)
    .then((res) => res.json())
    .then((res) => {
        fetchVendors(res.vendor[0])
        //console.log(res.vendor)
        //setLoading(false)
    })
  }
  useEffect(() => {
    getData()
  }, []);

  
  return (
    <>
      @@Pos1@@
    
      <div className="py-2 px-[25px] md:px-[60px] lg:px-[140px]">                    
          <div className="grid grid-cols-1 md:grid-cols-2 luday_grid_wrap py-[100px]">		
            <div className="group">
              <p className="tracking-widest mb-2.5 text-xs ">B E S T  &nbsp;  D E A L S  &nbsp;  I N  &nbsp; N I G E R I A || <Link to={ROUTE.VENDORS} className="py-3 text-gray-500">View All Vendors</Link></p>
              <h3>{vendors.business_name}</h3>
              <div className="my-4 px-5" dangerouslySetInnerHTML={{ __html: vendors.business_description }}></div>
              <p className="my-4 pb-2"><Link to={`${ROUTE.VENDOR_PRODUCTS_VIEW}/${vendors.slug}`} className="py-3 text-gray-500">View all products from this Vendor</Link></p>	
            </div>		
            <div className="group md:gap-4">
              <img className="lazy w-full" src={`${CONSTANT.IMAGE_STORE}/${vendors.image}`} alt={vendors.business_name} />
            </div>
          </div>
      </div>
      @@Pos2@@
    </>
  );  
}
export default @@PageName@@;
 """
 layouts["layout_vendor_details_1"] = layout_vendor_details_1


 """
 Vendor dashboard layout 1
 """
 layout_vendor_dashboard_1 ="""
import React, { useEffect, useState }  from 'react'
@@Imports@@
const @@PageName@@ = () => {
    const [countOfProducts, setCountOfProducts] = useState([]);
    const [countOfOders, setCountOfOders] = useState([]);
    const [loading, setLoading] = useState(false);
    const [products, setProducts] = useState([]);
    const { vendor } = useSelector((state) => ({
        vendor: state.profile.id
    }));

    let productsLoading = (
        <>
            <tr className="mx-auto">
                <td className="p-2">
                    <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                    </div>
                </td>
                <td className="p-2">
                    <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                    </div>
                </td>
                <td className="p-2">
                    <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                    </div>
                </td>
                <td className="p-2">
                    <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative">
                    </div>
                </td>
                <td className="p-2">
                    <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                    </div>
                </td>
                <td className="p-2">
                    <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                    </div>
                </td>
                <td className="p-2">
                    <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                    </div>
                </td>
                <td className="p-2">
                    <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                    </div>
                </td>
            </tr>
            <tr className="mx-auto">
                <td className="p-2">
                    <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                    </div>
                </td>
                <td className="p-2">
                    <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                    </div>
                </td>
                <td className="p-2">
                    <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                    </div>
                </td>
                <td className="p-2">
                    <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative">
                    </div>
                </td>
                <td className="p-2">
                    <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                    </div>
                </td>
                <td className="p-2">
                    <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                    </div>
                </td>
                <td className="p-2">
                    <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                    </div>
                </td>
                <td className="p-2">
                    <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                    </div>
                </td>
            </tr>
        </>
    )
    let productList;
    if(products.length > 0){
        productList = products.slice(0, 5).map((item, i) => {
            return (
                <tr key={i}>
                    <td className="p-2 w-8">
                    <img src={`${CONSTANT.IMAGE_STORE}/${item.image_path}`} className="w-8 h-8 mx-auto overflow-hidden" alt={item.name} />
                    </td>
                    <td className="p-2">
                        {item.name}
                    </td>
                    <td className="p-2">
                        {item.sku}
                    </td>
                    <td className="p-2">
                        <span className={
                        item.sale_price ? "line-through mr-1" : "" }>{ item.price }</span> { item.sale_price ? item.sale_price : ''}
                        
                    </td>
                    <td className="p-2">
                        { item.product_category }
                    </td>
                    <td className="p-2">
                    {item.featured == 1 ?
                            <span><MdStar className="mx-auto h-6 w-6 text-green-600 text-center" /></span>
                            :
                            <span><MdStarOutline className="mx-auto h-6 w-6 text-green-600 text-center" /></span>}
                    </td>
                    <td className="">
                        {item.is_verified == 1 ?
                            <span className="rounded-md text-white bg-green-600 p-1 flex justify-center items-center text-center">Verified</span>
                            :
                            <span className="rounded-md  text-white bg-red-600 p-1 flex justify-center items-center text-center">Unverified</span>}
                    </td>
                </tr>
            )
        }
    );
  } if(products.length < 1) {
    productList =  (<tr className=''><td colSpan={8} className="">
      <div className="flex flex-col my-4 space-y-3 justify-center items-center text-xl font-medium tracking-wide py-4 text-green-700 text-center">
          <MdOutlineProductionQuantityLimits className="w-16 h-16" />
          <p>@@EmptyProductsMssg@@</p>
      </div>
      </td></tr>)
      
  }
  
  const getProducts = () => {
    setLoading(true)
    fetch(`${ROUTE.PRODUCTS_API}/vendors/${vendor}/products`)
      .then((res) => res.json())
      .then((res) => {
        setCountOfProducts((res.results.length))
        setProducts(res.results)
        console.log(res.results)
        setLoading(false)
      })
  }

  const getOders = () => {
    fetch(`${ROUTE.PRODUCTS_API}/order/vendor/id?user_id=${vendor}`)
        .then((res) => res.json())
        .then((res) => {
          setCountOfOders(res.data.length)
            
    })
  } 

  const reloadWindow = () => {
    const reloadCount = sessionStorage.getItem('reloadCount');
    sessionStorage.setItem('reloadCount', '0');
    if (typeof reloadCount !== 'undefined' && reloadCount < 1) {
      setTimeout(location.reload.bind(location), 200);
      sessionStorage.setItem('reloadCount', reloadCount + 1);
    }
  }
  useEffect(() => {
    getProducts()
    getOders()
  }, [vendor])
  

  useEffect(() => {
    reloadWindow()
  }, [])
  return (
    <>      
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 p-4 mt-3 gap-4">
        <div className="bg-white shadow-lg rounded-md px-3 pt-3 border-b-4 border-green-600 text-green-600 font-medium group hover:scale-105 transition-all duration-400">
          <div className="flex items-center justify-between mb-3">
            <div className="flex justify-center items-center w-14 h-14 bg-gray-100 rounded-full transition-all duration-300 transform group-hover:rotate-12">
            <svg width="30" height="30" fill="none" viewBox="0 0 24 24" stroke="currentColor" className="stroke-current transform transition-transform duration-500 ease-in-out"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"></path></svg>
            </div>
            <div className="text-right">
              <p className="text-2xl">{countOfOders > 0 ? countOfOders : 0}</p>
              <p>Orders</p>
            </div>
          </div>
          <div className="flex items-center text-sm mb-1 justify-start text-green-700">
              <Link to="{ROUTE.VENDOR_ORDERS}">View all orders</Link> <span><FaExternalLinkAlt className="ml-1 h-3 w-3"/></span>
          </div>
        </div>

        <div className="bg-white shadow-lg rounded-md px-3 pt-3 border-b-4 border-green-600 text-green-600 font-medium group hover:scale-105 transition-all duration-400 flex-col">
          <div className="flex items-center justify-between mb-3">
            <div className="flex justify-center items-center w-14 h-14 bg-gray-100 rounded-full transition-all duration-300 transform group-hover:rotate-12">
            <FaShoppingBasket className="w-8 h-8"/>
            </div>
            <div className="text-right">
              <p className="text-2xl">{countOfProducts}</p>
              <p>Products</p>
            </div>
          </div>
          <div className="flex items-center text-sm mb-1 justify-start text-green-700">
              <Link to="{ROUTE.VENDOR_PRODUCTS}">View all products</Link> <span><FaExternalLinkAlt className="ml-1 h-3 w-3"/></span>
          </div>            
        </div>
      </div>

      {/* Recently added products tab */}
      <div className="heade px-10 flex items-center justify-between">
      </div>
      <div className="flex flex-col mt-6 mx-1 lg:flex-row">
            <div className="w-full m-4 bg-white shadow-lg text-lg rounded-sm border border-gray-200">
                <div className="overflow-x-auto rounded-lg p-3">
                  <div className="header py-3 px-2 flex items-center justify-between">
                    <h3 className="font-medium text-xl">Recently added products</h3>
                    <Link className="focus:outline-none text-white p-1 px-2 rounded-md text-sm bg-green-700 hover:bg-green-600 hover:shadow-lg transition-all duration-100" to={ROUTE.VENDOR_PRODUCTS}>View all <span><FaAngleRight className="inline-flex w-3 h-3"/></span></Link>
                  </div>                
                    <table className="w-full whitespace-nowrap">
                        <thead className="text-sm font-semibold uppercase text-gray-800 bg-gray-50">
                            <tr className="font-semibold text-center">
                                <th className='w-12'><svg xmlns="http://www.w3.org/2000/svg" className="fill-current w-5 h-5 mx-auto" ><path d="M6 22h12a2 2 0 0 0 2-2V8l-6-6H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2zm7-18 5 5h-5V4zm-4.5 7a1.5 1.5 0 1 1-.001 3.001A1.5 1.5 0 0 1 8.5 11zm.5 5 1.597 1.363L13 13l4 6H7l2-3z"></path></svg></th>
                                <th className="p-2">@@TableHead1@@
                                </th>
                                <th className="p-2">@@TableHead2@@
                                </th>
                                <th className="p-2">@@TableHead3@@
                                </th>
                                <th className="p-2">@@TableHead4@@
                                </th>
                                <th className="p-2">@@TableHead5@@
                                </th>
                                <th className="p-2">@@TableHead6@@
                                </th>
                            </tr>
                        </thead>

                        <tbody className="text-sm divide-y divide-gray-100 text-center">
                          { loading
                            ? productsLoading
                            : productList }
                        </tbody>
                    </table>
                </div>
            </div>
            
        </div> 
    </>
  )
}
export default @@PageName@@;
 """
 layouts["layout_vendor_dashboard_1"] = layout_vendor_dashboard_1


 """
 Order layout 1
 """
 layout_order_1 ="""
import React, {useState, useEffect, useCallback} from 'react';
@@Imports@@
const @@PageName@@ = () => {
  const [allorders, fetchAllOrders] = useState([]);
    const [sortType, setSortType] = useState([]);
    const [sortLiist, setSortList] = useState([]);
    const [deliveryStatus, setDeliveryStatus] = useState([]);
    const [searchResult, setSearchResult] = useState('');
    const [searchData, fetchSearchData] = useState([]);
    const [searchRef, setSearchRef] = useState('');
    const [totalSum, setTotalSum] = useState('');
    const [sortDate, setSortDate] = useState(new Date());
    const nf = new Intl.NumberFormat();

    const { userId } = useSelector((state) => ({
        userId: state.profile.id
    }));

    const filterSortType = () => {
        const sdt = Sortlist.filter(y => y.value != 2)
        setSortList(sdt)
    }

    const getData = () => {
        fetch(`${ROUTE.PRODUCTS_API}/order/vendor/id?user_id=${userId}`)
            .then((res) => res.json())
            .then((res) => {
                fetchAllOrders(res.data)
                setTotalSum((res.data.reduce((a,v) =>  a = a + v.price , 0 )))
                
        })
    } 

    useEffect(() => {
        getData()
        filterSortType()
        return () => {
            fetchAllOrders({}); // This worked for me
          };
    }, [])


    const SearchOrder = useCallback( async (param)  => {
        if (param){
            fetch(`${ROUTE.PRODUCTS_API}/order/vendor/search/${param}/${userId}`)
            .then((res) => res.json())
            .then((res) => {
                fetchSearchData(res.data)
                setSearchResult("Success")
                setTotalSum((res.data.reduce((a,v) =>  a = a + v.price , 0 )))
            })
           
        }
        else {
            setSearchResult('')
            getData()
        }
    }, []);

    const SearchOrderByDate = useCallback( async (param)  => {
        if (param){
            var search_data = param.toString().slice(0, 24)
            fetch(`${ROUTE.PRODUCTS_API}/order/vendor/${userId}/sort?date=${search_data}`)
            .then((res) => res.json())
            .then((res) => {
                fetchSearchData(res.data)
                setSearchResult("Success")
                setTotalSum((res.data.reduce((a,v) =>  a = a + v.price , 0 )))
            })
        }
        else {
            setSearchResult('')
            getData()
        }
    }, []);


    const SearchOrderByDelivery = useCallback( async (param)  => {
        if (param){
            fetch(`${ROUTE.PRODUCTS_API}/order/vendor/delivery/${userId}/${param}`)
            .then((res) => res.json())
            .then((res) => {
                fetchSearchData(res.data)
                setSearchResult("Success")
                setTotalSum((res.data.reduce((a,v) =>  a = a + v.price , 0 )))
            })
        }
        else {
            setSearchResult('')
            getData()
        }
    }, []);


    const handleDateChange = (data) =>{
        setSortDate(data)
        SearchOrderByDate(data)
    }


    const searchRefID = () => {
        const timer = setSearchRef(() => {
            SearchOrder(searchRef)
       
        }, 2000)
        return () => clearTimeout(timer)
    }


    const handDeliverStatusChange = (selectedOption) => {
        setDeliveryStatus(selectedOption)
        SearchOrderByDelivery(selectedOption.value)
    }


    let orderList;
    if(allorders.length > 0){
        orderList = allorders.map((item, i) => {
            return (
                <tr key={i}>
                    <td className="p-2">
                        {item.Order_ref}
                    </td>
                    <td className="p-2">
                    <img src={`${CONSTANT.IMAGE_STORE}/${item.image_path}`} className="w-8 h-8 mx-auto overflow-hidden" alt={item.product_name} />
                    </td>
                    <td className="p-2">
                        <p className="text-center">{item.product_name}</p>
                    </td>
                    <td className="p-2">
                        <p className="text-center">{item.product_ref}</p>
                    </td>
                    <td className="p-2">
                        <p className="text-center">{item.quantity}</p>
                    </td>
                    <td className="p-2">
                    &#8358;{nf.format(item.price)}
                    </td>
                    <td className="p-2">
                        {item.quantity_remaining <= "5" ?
                            <p className=' text-center bg-red-200 text-red-800 px-2 py-1 rounded-full'> {item.quantity_remaining}</p>
                            :
                            <p className='text-center bg-green-200 text-green-800 px-2 py-1 rounded-full'> {item.quantity_remaining}</p>
                        }
                    </td>
                    <td className="p-2">
                        <p className="text-center">{ item.date_sold }</p>
                    </td>
                    <td className="p-2">
                        {item.delivery_status == "Pending" ?
                        <p className=' text-center bg-red-200 text-red-800 px-2 py-1 rounded-full'> Pending</p>
                        :
                        item.delivery_status == "Shipped" ?
                        <p className='text-center bg-blue-200 text-blue-800 px-2 py-1 rounded-full'> Shipped</p>
                        :
                        item.delivery_status == "Delivered" ?
                        <p className='text-center bg-green-200 text-green-800 px-2 py-1 rounded-full'> Delivered</p>
                        :
                        <p className=''> @@EmptyOrderMssg@@</p>
                         }
                    </td>
                </tr>
            )
        }

        );
    } else {
      orderList =  (<tr className=''><td colSpan={8} className="">
        <div className="flex flex-col my-4 space-y-3 justify-center items-center text-xl font-medium tracking-wide py-4 text-green-700 text-center">
            <MdOutlineProductionQuantityLimits className="w-16 h-16" />
            <p>No Record added yet</p>
        </div>
        </td></tr>)
    }

    let searchOrderList;
    if(searchData.length > 0){
        searchOrderList = searchData.map((item, i) => {
            return (
                <tr key={i}>
                    <td className="p-2">
                        {item.Order_ref}
                    </td>
                    <td className="p-2">
                    <img src={`${CONSTANT.IMAGE_STORE}/${item.image_path}`} className="w-8 h-8 mx-auto overflow-hidden" alt={item.product_name} />
                    </td>
                    <td className="p-2">
                        <p className="text-center">{item.product_name}</p>
                    </td>
                    <td className="p-2">
                        <p className="text-center">{item.product_ref}</p>
                    </td>
                    <td className="p-2">
                        <p className="text-center">{item.quantity}</p>
                    </td>
                    <td className="p-2">
                    &#8358;{nf.format(item.price)}
                    </td>
                    <td className="p-2">
                        {item.quantity_remaining <= "5" ?
                            <p className=' text-center bg-red-200 text-red-800 px-2 py-1 rounded-full'> {item.quantity_remaining}</p>
                            :
                            <p className='text-center bg-green-200 text-green-800 px-2 py-1 rounded-full'> {item.quantity_remaining}</p>
                        }
                        
                    </td>
                    <td className="p-2">
                        <p className="text-center">{ item.date_sold }</p>
                    </td>
                    <td className="p-2">
                        {item.delivery_status == "Pending" ?
                        <p className=' text-center bg-red-200 text-red-800 px-2 py-1 rounded-full'> Pending</p>
                        :
                        item.delivery_status == "Shipped" ?
                        <p className='text-center bg-blue-200 text-blue-800 px-2 py-1 rounded-full'> Shipped</p>
                        :
                        item.delivery_status == "Delivered" ?
                        <p className='text-center bg-green-200 text-green-800 px-2 py-1 rounded-full'> Delivered</p>
                        :
                        <p className=''> @@EmptyOrderMssg@@</p>
                         }
                    </td>
                </tr>
            )
        }

        );
    }else {
        searchOrderList =  (<tr className=''><td colSpan={8} className="">
          <div className="flex flex-col my-4 space-y-3 justify-center items-center text-xl font-medium tracking-wide py-4 text-green-700 text-center">
              <MdOutlineProductionQuantityLimits className="w-16 h-16" />
              <p>@@NoRecordMssg@@</p>
          </div>
          </td></tr>)
      }
  

  return (
    <div className="bg-gray-100">
        <div className="header bg-white h-16 px-10 py-8 border-b-2 border-gray-200 flex items-center justify-between">
            <div className="flex items-center space-x-2 text-gray-400">
                <span className="text-green-700 tracking-wider font-thin text-md"><Link to={ROUTE.ADMIN_DASHBOARD}>Home</Link></span>
                <span>/</span>
                <span className="tracking-wide text-md">
                    <span className="text-base">@@PageName@@</span>
                </span>
                <span>/</span>
            </div>
        </div>
        <div className="header mb-20 md:my-3 h-12 px-10 py-8 flex flex-col md:flex-row md:items-center md:justify-between">
            <h1 className="font-medium text-2xl">@@PageName@@</h1>
            <div className="focus:outline-none text-white m-4 p-3 font-semibold rounded-md bg-green-700 hover:bg-green-600 hover:shadow-lg"> <span className=' whitespace-nowrap overflow-x-auto items-center flex-nowrap'><FaMoneyCheckAlt className="inline-block w-5 h-5 mr-3"/>
                </span>&#8358;{nf.format(totalSum)}</div>
        </div>
           
        <div className="flex flex-col mx-3 lg:flex-row">
            <div className="w-full m-4 bg-white shadow-lg text-lg rounded-sm border border-gray-200">
                <div className="overflow-x-auto rounded-lg  p-3">
                    <h2 className="font-medium text-xl m-4">Filter</h2>
                    <hr/>
                    <div className='flex flex-col md:flex-row w-full my-6'>
                        <div className="w-full md:w-2/3 px-3 mb-6">
                            <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='vendor_first_name'>Search by PRODUCT REF	</label>
                            <input className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d]" type='text' name="vendor_first_name" placeholder="Enter Ref_id" value={searchRef}  onChange={(e) => setSearchRef(e.target.value)} onKeyUp={searchRefID}/>
                           
                        </div>
                        <div className="w-full md:w-2/3 px-3 mb-6">
                            <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='vendor_last_name'>Filter by</label>
                            <Select defaultValue={sortType} onChange={setSortType} options={sortLiist} className="z-20"/>
                            
                        </div>
                        {sortType.value == 1 ?
                            <div className="w-full md:w-2/3 px-3 mb-6">
                            <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='vendor_last_name'>Date</label>
                            <DatePicker selected={sortDate} onChange={(date:Date) => handleDateChange(date)} className="w-full" /> 
                            </div>
                        :
                        sortType.value == 3 ?
                            <div className="w-full md:w-2/3 px-3 mb-6">
                            <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='vendor_last_name'>Delivery</label>
                            <Select defaultValue={deliveryStatus} onChange={handDeliverStatusChange} options={DeliveryStatuslist} className=" z-10"/>
                            </div>
                        :
                        " "
                        }

                    </div>
                    <table className="table-auto w-full mt-3">
                        <thead className="text-sm font-semibold uppercase text-gray-800 bg-gray-50">
                            <tr className="font-semibold text-center">
                                <th>@@TableHead1@@</th>
                                <th className="p-2">@@TableHead2@@
                                </th>
                                <th className="p-2">@@TableHead3@@
                                </th>
                                <th className="p-2">@@TableHead4@@
                                </th>
                                <th className="p-2">@@TableHead5@@
                                </th>
                                <th className="p-2">@@TableHead6@@
                                </th>
                                <th className="p-2">@@TableHead7@@
                                </th>
                                <th className="p-2">@@TableHead8@@
                                </th>
                                <th className="p-2">@@TableHead9@@
                                </th>
                            </tr>
                        </thead>

                        <tbody className="text-sm divide-y divide-gray-100">
                        {searchResult == "Success"  ? 
                            searchOrderList
                        :
                            orderList
                        }
                       
                       
                        </tbody>
                    </table>
                </div>
            </div>
            
        </div>        
    </div>
    )
}
export default @@PageName@@;
 """
 layouts["layout_order_1"] = layout_order_1


 """
 Vendor add product layout 1
 """
 layout_vendor_add_product_1 ="""
import React, {useCallback, useEffect, useState} from 'react';
@@Imports@@
const @@PageName@@ = () => {
  const {register, handleSubmit, reset, formState: { errors } } = useForm();
  const [categories, fetchCategories] = useState([]);
  const [selectedImage, setSelectedImage] = useState();
  const [productImage, setProductImage] = useState();
  let formData = new FormData();

  const { userId } = useSelector((state) => ({
		userId: state.profile.id
	}));
  const [selectedImages, setSelectedImages] = useState([]);
  const [productGalleryImage, setProductGalleryImage] = useState([]);
    
  const onSelectMultipleImages = useCallback( async (e)  => {
    const selectedFilesArray = Array.from(e.target.files)
    console.log('selected array', selectedFilesArray)
    selectedFilesArray.map((file) => {
        const reader = new FileReader();
        reader.readAsDataURL(file);
        setProductGalleryImage((productGalleryImage) =>[...productGalleryImage, file]);     
        reader.onloadend = () => {
            setSelectedImages((selectedImages) =>[...selectedImages, reader.result]);
        };
    })
  }, []);

  const onSelectFile = useCallback( async (e)  => {
      const file = e.target.files[0];
      const reader = new FileReader();
      reader.readAsDataURL(file);
      setProductImage(file)
      reader.onloadend = () => {
          setSelectedImage(reader.result);
      };
  }, []);

  const submitForm = (data) => {
      formData.append('product_image', productImage)
      formData.append('name', data.product_name);
      formData.append('description', data.description)
      formData.append('price', data.price)
      formData.append('sale_price', data.sale_price)
      formData.append('quantity', data.quantity)
      formData.append('category_id', data.category)
      formData.append('user_id', userId)
      Array.from(productGalleryImage).forEach(item => {
          formData.append('product_gallery_image', item)
      })

      const requestOptions = {
          headers: {
            'Content-type': 'multipart/form-data'
          }
      }
      axios.post(
          `${ROUTE.PRODUCTS_API}/products`,
          formData,
          requestOptions
      ).then(res => res)
      .then(data =>{
        if (data.status == 200 || data.status == 302) {
              successAlert(data)
          }
          else {
              errorAlert(data.message)
          }
      })
      .catch(err => errorAlert(err))
  }
  
  const successAlert = (response) => {
      return(
        swal({
            title: "Info!",
            text: response.data.message,
            icon: "success"
        }).then(function() {
          reset()
          setSelectedImage('')
          setSelectedImages('')
          setProductImage('')
          setProductGalleryImage('')
        })           
      )
  }

  const errorAlert = (error) => {
    return(
      swal({
          title: "Error!",
          text: error.message,
          icon: "error"
      })              
    )
  }
  const getCategories = () => {
    fetch(`${ROUTE.PRODUCTS_API}/categories`)
      .then((res) => res.json())
      .then((res) => {
      fetchCategories(res.results)
    })
  }

  useEffect(() => {
    getCategories()
  }, [])

  let categoryDropdown = ''
  categoryDropdown = categories.map((item, i) => {
    return (<option className="my-2 hover:bg-gray-50" key={i} value={item.id}> {item.name} </option>)
  }) 

  return (
    <div className="bg-gray-100">
        <div className="header bg-white h-16 px-10 py-8 border-b-2 border-gray-200 flex items-center justify-between">
          <div className="flex items-center space-x-2 text-gray-400">
            <span className="text-green-700 tracking-wider font-thin text-md"><Link to={ROUTE.VENDOR_DASHBOARD}>@@NavLink1@@</Link></span>
            <span>/</span>
            <span className="tracking-wide text-md">
                <span className="text-green-700 tracking-wider font-thin text-md"><Link to={ROUTE.VENDOR_PRODUCTS}>@@NavLink2@@</Link></span>
            </span>
            <span>/</span>
            <span className="tracking-wide text-md">
                <span className="text-base">@@AddProductText@@</span>
            </span>
          </div>
        </div>
        <div className="header my-3 h-12 px-10 py-8  flex items-center justify-between">
            <h1 className="font-medium text-2xl">@@AddProductText@@</h1>
            <Link to={ROUTE.VENDOR_PRODUCTS} className="focus:outline-none text-white m-4 p-3 font-semibold rounded-md bg-green-700 hover:bg-green-600 hover:shadow-lg transition-all duration-100"> <span><FaAngleLeft className="inline-block w-5 h-5"/>
            </span> @@NavToProductsText@@</Link>
        </div>
        <div className="flex flex-col mx-3 lg:flex-row">
            <form className="w-full lg:w-3/5 bg-white shadow-md p-6" encType="multipart/form-data">
                <div className="flex flex-wrap -mx-3 mb-6">
                    <div className="w-full px-3 mb-6">
                        <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='product_name'>@@Input1Label@@</label>
                        <input className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d]" type='text' name="product_name" placeholder="@@Input1Placeholder@@"
                        {...register("product_name", { required: true})}
                          />
                        {errors.product_name && <small className="text-red-500 text-xs italic">@@Input1ErrorMssg@@</small>}
                        {errors.product_name?.type === "maxLength" && <p style={{ color: "red" }}><small>@@Input1ErrorMssgAlt1@@ </small></p>}
                    </div>

                    <div className="w-full px-3 mb-6">
                        <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='category'>@@Input2Label@@</label>
                        <select className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d]" name="category" {...register("category", { required: true })}
                        >
                            <option value={''}>@@Input2SelectOptionText@@</option>
                            { categoryDropdown }
                        </select>

                        {errors.category && <small className="text-red-500 text-xs italic">@@Input2ErrorMssg@@</small>}
                    </div>

                    <div className="w-full px-3 mb-6">
                        <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='price'>@@Input3Label@@</label>
                        <input className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d]" type='number' name="price" placeholder="@@Input3Placeholder@@" {...register("price", { required: true })}
                        />
                        {errors.price && <small className="text-red-500 text-xs italic">@@Input3ErrorMssg@@</small>}
                    </div>

                    <div className="w-full px-3 mb-6">
                        <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='sale_price'>@@Input4Label@@</label>
                        <input className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d]" type="number" inputMode="numeric" name="sale_price" placeholder="@@Input4Placeholder@@" {...register("sale_price")}
                        />
                    </div>

                    <div className="w-full px-3 mb-6">
                        <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='quantity'>@@Input5Label@@</label>
                        <input className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d]" inputMode="numeric" type='number' name="quantity" placeholder="@@Input5Placeholder@@"
                        {...register("quantity", { required: true })}
                        />
                        {errors.quantity && <small className="text-red-500 text-xs italic">@@Input5ErrorMssg@@</small>}
                    </div>
                    
                    <div className="w-full px-3 mb-6">
                        <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='description'>@@Input6Label@@</label>
                        <textarea className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d]" rows={5}  placeholder="@@Input6Placeholder@@" name="description" {...register("description")} />
                        {errors.description && <small className="text-red-500 text-xs italic">@@Input6ErrorMssg@@</small>}
                    </div>
                    <div className="w-full mx-auto px-3 mb-12">
                        <label className="mx-auto cursor-pointer flex w-full max-w-lg flex-col items-center justify-center rounded-xl border-2 border-dashed border-green-400 bg-white p-6 text-center" htmlFor='product_image'>
                        <svg xmlns="http://www.w3.org/2000/svg" className="h-10 w-10 text-green-800" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="2">
                        <path strokeLinecap="round" strokeLinejoin="round" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
                        </svg>

                        <h2 className="mt-4 text-xl font-medium text-gray-700 tracking-wide">@@Input7Label@@</h2>

                        <p className="mt-2 text-gray-500 tracking-wide">@@Input7Placeholder@@ </p>

                        <input name="product_image" id="product_image" type="file" className="hidden" onChange={onSelectFile} accept="image/png, image/jpeg, image/webp"/>
                        </label>
                        {errors.product_image && <small className="text-red-500 text-xs italic">@@Input7ErrorMssg@@</small>}
                    </div>
                    <div className="w-full flex justify-center mb-5">
                        {selectedImage &&
                            (
                                <img src={selectedImage} className="w-32 h-32"/>
                            )
                        } 
                    </div>
                    <div className="w-full px-3 flex justify-end mb-5 text-green-500">
                        <p className="flex mx-4 "> <span> <FaPlus className="w-4 h-4 mr-1 inline-flex" /> </span>@@Input8Label@@</p>
                    </div>

                    <div className="w-full px-3 mb-6">
                    <label className="mx-auto cursor-pointer flex w-full max-w-lg flex-col items-center justify-center rounded-xl border-2 border-dashed border-green-400 bg-white p-6 text-center" htmlFor='product_gallery_images'>
                        <svg xmlns="http://www.w3.org/2000/svg" className="h-10 w-10 text-green-800" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="2">
                        <path strokeLinecap="round" strokeLinejoin="round" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
                        </svg>

                        <h2 className="mt-4 text-xl font-medium text-gray-700 tracking-wide">@@Input9Label@@</h2>

                        <p className="mt-2 text-gray-500 tracking-wide">@@Input9Placeholder@@ </p>

                        <input type="file" className="hidden" name="product_gallery_images" id="product_gallery_images" onChange={onSelectMultipleImages} multiple accept="image/png, image/jpeg, image/webp"/>
                        </label>
                    </div>
                    <div className="overflow-x-auto flex justify-center mb-5 mx-auto">
                        {selectedImages &&
                            selectedImages.map((image, index) => {
                                return (
                                        <>
                                            <img key={index} src={image} className="w-32 h-32 relative"/>
                                            {/* <span className="relative"><button className="text-red-500 font-weight-bolder top-0" onClick={(e)=>removeImages(image, e)}><FaTimes/></button></span>   */}
                                        </>
                                )                                    
                            })
                        }
                    </div>
                    <div className="w-full px-3 mb-6">
                        <button className="appearance-none w-full block bg-green-700 text-gray-100 font-bold border border-gray-200 rounded-lg py-3 px-3 leading-tight hover:bg-green-600 focus:outline-none focus:bg-white focus:border-gray-500"
                        onClick={handleSubmit(submitForm)}>@@FormButtonText@@</button>
                    </div>
                </div>
            </form>          
        </div>        
    </div>
  )  
}
export default @@PageName@@;
 """
 layouts["layout_vendor_add_product_1"] = layout_vendor_add_product_1


 """
 Edit vendor product layout 1
 """
 layout_vendor_edit_product_1 ="""
import React, { useEffect, useState, useCallback } from 'react';
@@Imports@@
const @@PageName@@ = () => {
  const { id } = useParams();
    const [loading, setLoading] = useState(false);
    const [categories, fetchCategories] = useState([]);
    const [productId, setProductId] = useState('');
    const [productName, setProductName] = useState('');
    const [productCategoryId, setProductCategoryId] = useState('');
    const [productPrice, setProductPrice] = useState('');
    const [productSalePrice, setProductSalePrice] = useState('');
    const [productQuantity, setProductQuantity] = useState('');
    const [productDescription, setProductDescription] = useState('');
    const [productImage, setProductImage] = useState('');
    const [selectedImage, setSelectedImage] = useState();
    const [newProductImage, setNewProductImage] = useState();
    let formData = new FormData();

    const [selectedImages, setSelectedImages] = useState([]);
    const [productGalleryImage, setProductGalleryImage] = useState([]);

    const onSelectMultipleImages = useCallback( async (e)  => {
        const selectedFilesArray = Array.from(e.target.files)
        selectedFilesArray.map((file) => {
            const reader = new FileReader();
            reader.readAsDataURL(file);
            setProductGalleryImage((productGalleryImage) =>[...productGalleryImage, file]);     
            reader.onloadend = () => {
                setSelectedImages((selectedImages) =>[...selectedImages, reader.result]);
            };
        })
    }, []);

    const removeImageFromDB = (image, e) => {
        e.preventDefault();
        const requestOptions = {
            headers: {
              'Content-type': 'application/json'
            }
        }
        axios.delete(
            `${ROUTE.PRODUCTS_API}/products/${image}/gallery`,
            requestOptions
        ).then(res => res)
        .then(data =>{
          successAlert(data)
        })
        .catch(err => errorAlert(err))
        getData();
    }
    const getData = async () => {
        setLoading(true)
        await fetch(`${ROUTE.PRODUCTS_API}/products/${id}`)
          .then((res) => res.json())
          .then((res) => {
            setProductId(res.data[0].id)
            setProductName(res.data[0].name)
            setProductPrice(res.data[0].price)
            setProductSalePrice(res.data[0].sale_price)
            setProductQuantity(res.data[0].quantity)
            setProductDescription(res.data[0].description)
            setProductImage(res.data[0].image_path)
            setProductCategoryId(res.data[0].product_category_id)
            res.data[0].products_gallery.map(item => {
                setProductGalleryImage((productGalleryImage) =>[...productGalleryImage, item])
            })
            setLoading(false) 
          })
    }

    const {register, handleSubmit, reset, setValue, formState: { errors } } = useForm();
    const getCategories = () => {
        fetch(`${ROUTE.PRODUCTS_API}/categories`)
          .then((res) => res.json())
          .then((res) => {
            fetchCategories(res.results)
          })
    }

    useEffect(() => {
        getCategories()
        getData()
    }, [])

    useEffect(() => {
        setTimeout(() => 
            setValue("name", productName),
            setValue("category", productCategoryId),
            setValue("price", productPrice),
            setValue("sale_price", productSalePrice),
            setValue("quantity", productQuantity),
            setValue("description", productDescription)
        );
      }, [loading]);

    const onSelectFile = useCallback( async (e)  => {
        const file = e.target.files[0];
        const reader = new FileReader();
        reader.readAsDataURL(file);
        setNewProductImage(file)
        reader.onloadend = () => {
            setSelectedImage(reader.result);
        };
    }, []);

    const submitForm = (data) => {
        formData.append('product_image', newProductImage)
        formData.append('name', data.name);
        formData.append('description', data.description)
        formData.append('price', data.price)
        formData.append('sale_price', data.sale_price)
        formData.append('quantity', data.quantity)
        formData.append('category_id', data.category)
        Array.from(productGalleryImage).forEach(item => {
            formData.append('product_gallery_image', item)
        })
        const requestOptions = {
            method: "POST",
            headers: {
              'Content-type': 'multipart/form-data'
            }
        }
        axios.put(
            `${ROUTE.PRODUCTS_API}/products/${productId}`,
            formData,
            requestOptions
        ).then(res => res)
        .then(data =>{
          successAlert(data)
        })
        .catch(err => errorAlert(err))
      reset()
      setSelectedImage('');
    }

    const handleCategoryChange = (e) => {
        setProductCategoryId(e.target.value);
      };

    const successAlert = (response) => {
        return(
          swal({
              title: "Info!",
              text: response.data.message,
              icon: "success"
          }).then(function () {
                window.location.reload()
          })
        )
    }
    const errorAlert = (error) => {
        return(
          swal({
              title: "Error!",
              text: error,
              icon: "error"
          }).then(function () {
            window.location.reload()
          })          
        )
    }

    let categoryDropdown = categories.map((item, i) => {
        return (<option className="my-2 hover:bg-gray-50" key={i} value={item.id}> {item.name} </option>)
    }) 

  return (
    <div className="bg-gray-100">
      <div className="header bg-white h-16 px-10 py-8 border-b-2 border-gray-200 flex items-center justify-between">
              <div className="flex items-center space-x-2 text-gray-400">
              <span className="text-green-700 tracking-wider font-thin text-md"><Link to={ROUTE.VENDOR_DASHBOARD}>@@NavLink1@@</Link></span>
              <span>/</span>
              <span className="tracking-wide text-md">
                  <span className="text-green-700 tracking-wider font-thin text-md"><Link to={ROUTE.VENDOR_PRODUCTS}>@@NavLink2@@</Link></span>
              </span>
              <span>/</span>
              <span className="tracking-wide text-md">
                  <span className="text-base"> @@EditProductText@@</span>
              </span>
              </div>
      </div>
      <div className="header my-3 h-12 px-4 lg:px-10 py-8  flex items-center justify-between">
          <h1 className="font-medium text-2xl">@@EditProductText@@</h1>
          <Link to={ROUTE.VENDOR_PRODUCTS} className="focus:outline-none text-white m-4 p-3 font-semibold rounded-md bg-green-700 hover:bg-green-600 hover:shadow-lg transition-all duration-100"> <span><FaAngleLeft className="inline-block w-5 h-5"/>
          </span> @@NavToProductsText@@</Link>
      </div>
      {loading
      ? (<div className="h-full flex justify-center items-center">
              <h3 className="font-bold text-green-600 text-2xl mx-auto ">@@LoadingPageText@@</h3>
          </div>
      )
      :
      (
          <div className="flex flex-col mx-3 lg:flex-row">
          <form className="w-full lg:w-3/5 bg-white shadow-md p-6">
              <div className="flex flex-wrap -mx-3 mb-6">
                  <div className="w-full px-3 mb-6">
                      <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='name'>@@Input1Label@@</label>
                      <input className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d] invalid:border-pink-500 invalid:text-pink-600 focus:invalid:border-pink-500 focus:invalid:ring-pink-500" type='text' name="name" placeholder="@@Input1Placeholder@@"
                      defaultValue={productName} {...register("name", { required: true })} required onChange={(e) => setProductName(e.target.value)} />
                      {errors.product_name && <small className="text-red-500 text-xs italic">@@Input1ErrorMssg@@</small>}
                  </div>

                  <div className="w-full px-3 mb-6">
                      <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='category'>@@Input2Label@@</label>
                      <select className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d] invalid:border-pink-500 invalid:text-pink-600 focus:invalid:border-pink-500 focus:invalid:ring-pink-500" name="category"
                      onChange={handleCategoryChange}
                      defaultValue={productCategoryId || ""} {...register("category", { required: true })}
                      required>
                          { categoryDropdown }
                      </select>

                      {errors.category && <small className="text-red-500 text-xs italic">@@Input2ErrorMssg@@</small>}
                  </div>

                  <div className="w-full px-3 mb-6">
                      <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='price'>@@Input3Label@@</label>
                      <input className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d]" type='text' name="price" placeholder="@@Input3Placeholder@@"
                      {...register("price", { required: true })} required onChange={(e) => setProductPrice(e.target.value)} />
                        {errors.price && <small className="text-red-500 text-xs italic">@@Input3ErrorMssg@@</small>}
                  </div>

                  <div className="w-full px-3 mb-6">
                      <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='sale_price'>@@Input4Label@@</label>
                      <input className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d]" type='text' name="sale_price" placeholder="@@Input4Placeholder@@"
                      value={productSalePrice} {...register("sale_price")} onChange={(e) => setProductSalePrice(e.target.value)} />
                  </div>

                  <div className="w-full px-3 mb-6">
                      <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='quantity'>@@Input5Label@@</label>
                      <input className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d]" type='number' name="quantity" placeholder="@@Input5Placeholder@@"
                      required value={productQuantity} {...register("quantity", { required: true })} onChange={(e) => setProductQuantity(e.target.value)} />
                      {errors.quantity && <small className="text-red-500 text-xs italic">@@Input5ErrorMssg@@</small>}
                  </div>
                  
                  <div className="w-full px-3 mb-6">
                      <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='description'>@@Input6Label@@</label>
                      <textarea className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d]" rows={5}  placeholder="@@Input6Placeholder@@" name="description" value={productDescription} {...register("description", { required: true })} onChange={(e) => setProductDescription(e.target.value)} />
                      {errors.description && <small className="text-red-500 text-xs italic">@@Input6ErrorMssg@@</small>}
                  </div>
                  <div className="w-full px-3 mb-12">
                      <label className="mx-auto cursor-pointer flex w-full max-w-lg flex-col items-center justify-center rounded-xl border-2 border-dashed border-green-400 bg-white p-6 text-center" htmlFor='product_image'>
                      <svg xmlns="http://www.w3.org/2000/svg" className="h-10 w-10 text-green-800" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="2">
                      <path strokeLinecap="round" strokeLinejoin="round" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
                      </svg>

                      <h2 className="mt-4 text-xl font-medium text-gray-700 tracking-wide">@@Input7Label@@</h2>

                      <p className="mt-2 text-gray-500 tracking-wide">@@Input7Placeholder@@ </p>

                      <input name="product_image" id="product_image" type="file" className="hidden" onChange={onSelectFile} accept="image/png, image/jpeg, image/webp"/>
                      </label>
                      {errors.product_image && <small className="text-red-500 text-xs italic">@@Input7ErrorMssg@@</small>}
                  </div>
                  {errors.product_image && <small className="text-red-500 text-xs italic">@@Input7ErrorMssg@@</small>}

                  <div className="w-full mx-12 flex justify-center mb-5">
                      {productImage &&
                          (
                              <img src={`${CONSTANT.IMAGE_STORE}/${productImage}`} className={selectedImage ? "hidden" : `w-32 h-32 $`}/>
                          )
                      }
                      {selectedImage &&
                          (
                              <img src={selectedImage} className="w-32 h-32"/>
                          )

                      } 
                  </div>
                  <div className="w-full px-3 flex justify-end mb-5 text-green-500">
                      <p className="flex mx-4 "> @@Input8Label@@</p>
                  </div>

                  <div className="w-full px-3 mb-6">
                  <label className="mx-auto cursor-pointer flex w-full max-w-lg flex-col items-center justify-center rounded-xl border-2 border-dashed border-green-400 bg-white p-6 text-center" htmlFor='product_gallery_images'>
                      <svg xmlns="http://www.w3.org/2000/svg" className="h-10 w-10 text-green-800" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="2">
                      <path strokeLinecap="round" strokeLinejoin="round" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
                      </svg>

                      <h2 className="mt-4 text-xl font-medium text-gray-700 tracking-wide">@@Input9Label@@</h2>

                      <p className="mt-2 text-gray-500 tracking-wide">@@Input9Placeholder@@ </p>

                      <input type="file" className="hidden" name="product_gallery_images" id="product_gallery_images" onChange={onSelectMultipleImages} multiple accept="image/png, image/jpeg, image/webp"/>
                      </label>
                  </div>
                  <div className="overflow-x-auto flex justify-center mb-5 mx-auto">
                      {productGalleryImage &&
                          
                          productGalleryImage.map((image, index) => {
                              return (
                                  <>
                                      <img key={index}  src={`${CONSTANT.IMAGE_STORE}/${image.path}`} className="w-32 h-32"/>
                                      <span className="relative"><button className="text-red-500 font-weight-bolder top-0" onClick={(e) => removeImageFromDB(image.id, e)}><FaTimes/></button></span>
                                  </>
                              )
                          })
                      }
                      {selectedImages &&
                          selectedImages.map((image, index) => {
                              return (
                                  <>
                                      <img key={index} src={image} className="w-32 h-32 relative"/>
                                  </>
                              )                                    
                          })
                      }
                  </div>
                  <div className="w-full px-3 mb-6">
                      <button className="appearance-none w-full block bg-green-700 text-gray-100 font-bold border border-gray-200 rounded-lg py-3 px-3 leading-tight hover:bg-green-600 focus:outline-none focus:bg-white focus:border-gray-500"
                      onClick={handleSubmit(submitForm)}
                      >@@FormButtonText@@</button>
                  </div>
              </div>
          </form>          
      </div>
    )}         
  </div>
  )  
}
export default @@PageName@@;
 """
 layouts["layout_vendor_edit_product_1"] = layout_vendor_edit_product_1


 """
 Vendor view product layout 1
 """
 layout_vendor_view_product_1 ="""
import React, {useEffect, useState, useCallback} from 'react';
@@Imports@@
const @@PageName@@ = () => {
  const [loading, setLoading] = useState(false);
  const [products, fetchProducts] = useState([]);

  const { userId } = useSelector((state) => ({
    userId: state.profile.id
  }));
  
  const getData = () => {
      setLoading(true)
      fetch(`${ROUTE.PRODUCTS_API}/vendors/${userId}/products`)
        .then((res) => res.json())
        .then((res) => {
          fetchProducts(res.results)
          setLoading(false)
        })
    }

    useEffect(() => {
        getData()
    }, [])

    const successAlert = (response) => {
      return(
        swal({
            title: "Info!",
            text: response.data.message,
            icon: "success"
        }).then(function () {
              getData()
        })
      )
  }
  const errorAlert = (error) => {
      return(
        swal({
            title: "Error!",
            text: error,
            icon: "error"
        }).then(function () {
          getData()
        })          
      )
  }
    
    const deleteProduct = useCallback( async (id)  => {
      if(window.confirm('@@DelProductWarninMssg@@')){
        axios.delete(
          `${ROUTE.PRODUCTS_API}/products/${id}`,{
              method : 'DELETE',
              body : JSON.stringify({
                  id : id
              }),
              headers: {
                  'Content-type': 'application/json'
              }
          })
          .then(res => res)
          .then(data =>{
            successAlert(data)
          })
          .catch(err => errorAlert(err)
          )
      }

  }, []);
    let productList;
    if(products.length > 0){
      productList = products.map((item, i) => {
            return (
                <tr key={i}>
                    <td className="p-2">
                        <input type="checkbox" className="w-5 h-5" />
                    </td>
                    <td className="p-2 w-8">
                    <img src={`${CONSTANT.IMAGE_STORE}/${item.image_path}`} className="w-8 h-8 mx-auto overflow-hidden" alt={item.name} />
                    </td>
                    <td className="p-2">
                        {item.name}
                    </td>
                    <td className="p-2">
                        {item.sku}
                    </td>
                    <td className="p-2">
                      <span className={
                        item.sale_price ? "line-through mr-1" : "" }>{ item.price }</span> { item.sale_price ? item.sale_price : ''}
                        
                    </td>
                    <td className="p-2">
                        { item.product_category }
                    </td>
                    <td className="p-2">
                        {item.featured == 1 ?
                        <span><MdStar className="mx-auto h-6 w-6 text-green-600 text-center" /></span>
                        :
                        <span><MdStarOutline className="mx-auto h-6 w-6 text-green-600 text-center" /></span>}
                    </td>
                    <td className="">
                        {item.is_verified == 1 ?
                        <span className="rounded-md text-white bg-green-600 p-1 flex justify-center items-center text-center">@@StatusVerifiedText@@</span>
                        :
                        <span className="rounded-md  text-white bg-red-600 p-1 flex justify-center items-center text-center">@@StatusUnVerifiedText@@</span>}
                    </td>
                    <td className="p-2">
                      <div className="flex justify-center">
                          <Link to={`${ROUTE.VENDOR_EDIT_PRODUCTS}/${item.id}`} className="rounded-md hover:bg-gray-100 text-green-600 p-2 flex justify-between items-center">
                              <span><FaEdit className="w-4 h-4 mr-1"/>
                                </span> @@EditText@@
                          </Link>
                          <button className="rounded-md hover:bg-gray-100 text-red-600 p-2 flex justify-between items-center" value={item.id} onClick={() => deleteProduct(item.id)}>
                              <span><FaTrash className="w-4 h-4 mr-1" /></span> @@DeleteText@@
                          </button>
                        </div>
                    </td>
                </tr>
            )
        }

        );
    } else {
      productList =  (<tr className=''><td colSpan={10} className="">
        <div className="flex flex-col my-4 space-y-3 justify-center items-center text-xl font-medium tracking-wide py-4 text-green-700 text-center">
          <MdOutlineProductionQuantityLimits className="w-16 h-16" />
          <p>@@EmptyProductsMssg@@</p>
        </div>
        </td></tr>)
        
    }

    let productsLoading = (
      <>
          <tr className="mx-auto">
              <td className="p-2">
                  <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                  </div>
              </td>
              <td className="p-2">
                  <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                  </div>
              </td>
              <td className="p-2">
                  <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                  </div>
              </td>
              <td className="p-2">
                  <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                  </div>
              </td>
              <td className="p-2">
                  <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative">
                  </div>
              </td>
              <td className="p-2">
                  <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                  </div>
              </td>
              <td className="p-2">
                  <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                  </div>
              </td>
              <td className="p-2">
                  <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                  </div>
              </td>
              <td className="p-2">
                  <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                  </div>
              </td>
              <td className="p-2">
                  <div className="flex justify-center">
                      <div data-placeholder className="w-1/2 h-8 bg-gray-200 overflow-hidden relative">
                      </div>
                  </div>    
              </td>
          </tr>
          <tr className="mx-auto">
              <td className="p-2">
                  <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                  </div>
              </td>
              <td className="p-2">
                  <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                  </div>
              </td>
              <td className="p-2">
                  <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                  </div>
              </td>
              <td className="p-2">
                  <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                  </div>
              </td>
              <td className="p-2">
                  <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative">
                  </div>
              </td>
              <td className="p-2">
                  <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                  </div>
              </td>
              <td className="p-2">
                  <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                  </div>
              </td>
              <td className="p-2">
                  <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                  </div>
              </td>
              <td className="p-2">
                  <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                  </div>
              </td>              
              <td className="p-2">
                  <div className="flex justify-center">
                      <div data-placeholder className="w-1/2 h-8 bg-gray-200 overflow-hidden relative">
                      </div>
                  </div>    
              </td>
          </tr>
          <tr className="mx-auto">
              <td className="p-2">
                  <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                  </div>
              </td>
              <td className="p-2">
                  <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                  </div>
              </td>
              <td className="p-2">
                  <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                  </div>
              </td>
              <td className="p-2">
                  <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                  </div>
              </td>
              <td className="p-2">
                  <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative">
                  </div>
              </td>
              <td className="p-2">
                  <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                  </div>
              </td>
              <td className="p-2">
                  <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                  </div>
              </td>
              <td className="p-2">
                  <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                  </div>
              </td>
              <td className="p-2">
                  <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                  </div>
              </td>
              <td className="p-2">
                  <div className="flex justify-center">
                      <div data-placeholder className="w-1/2 h-8 bg-gray-200 overflow-hidden relative">
                      </div>
                  </div>    
              </td>
          </tr>
      </>
    )

  return (
    <div className="bg-gray-100">
        <div className="header bg-white h-16 px-10 py-8 border-b-2 border-gray-200 flex items-center justify-between">
              <div className="flex items-center space-x-2 text-gray-400">
                <span className="text-green-700 tracking-wider font-thin text-md"><Link to={ROUTE.VENDOR_DASHBOARD}>Home</Link></span>
                <span>/</span>
                <span className="tracking-wide text-md">
                    <span className="text-base">@@ProductsText@@</span>
                </span>
                <span>/</span>
              </div>
        </div>
        <div className="header my-3 h-12 px-10 py-8  flex items-center justify-between">
            <h1 className="font-medium text-2xl"> @@AllProductsHeadding@@</h1>
            <Link to={ROUTE.VENDOR_ADD_PRODUCTS} className="focus:outline-none text-white m-4 p-3 font-semibold rounded-md bg-green-700 hover:bg-green-600 hover:shadow-lg transition-all duration-100"> <span><FaPlus className="inline-block w-5 h-5"/>
            </span> @@AddProductsBtn@@</Link>
        </div>
        <div className="flex flex-col mx-3 lg:flex-row">
            <div className="w-full m-4 bg-white shadow-lg text-lg rounded-sm border border-gray-200">
                <div className="overflow-x-auto rounded-lg  p-3">
                    {/* Display products table */}
                    <table className="w-full whitespace-nowrap">
                        <thead className="text-sm font-semibold uppercase text-gray-800 bg-gray-50">
                            <tr className="font-semibold text-center">
                                <th><input type="checkbox" className="w-5 h-5"/></th>
                                <th className='w-12'><svg xmlns="http://www.w3.org/2000/svg" className="fill-current w-5 h-5 mx-auto" ><path d="M6 22h12a2 2 0 0 0 2-2V8l-6-6H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2zm7-18 5 5h-5V4zm-4.5 7a1.5 1.5 0 1 1-.001 3.001A1.5 1.5 0 0 1 8.5 11zm.5 5 1.597 1.363L13 13l4 6H7l2-3z"></path></svg></th>
                                <th className="p-2">@@TableHead1@@
                                </th>
                                <th className="p-2">@@TableHead2@@
                                </th>
                                <th className="p-2">@@TableHead3@@
                                </th>
                                <th className="p-2">@@TableHead4@@
                                </th>
                                <th className="p-2">@@TableHead5@@
                                </th>
                                <th className="p-2">@@TableHead6@@
                                </th>
                                <th className="p-2">@@TableHead7@@
                                </th>
                            </tr>
                        </thead>

                        <tbody className="text-sm divide-y divide-gray-100 text-center">
                          { loading
                            ? productsLoading
                            : productList }
                        </tbody>
                    </table>
                </div>
            </div>
            
        </div>        
    </div>
  )
}
export default @@PageName@@;
 """
 layouts["layout_vendor_view_product_1"] = layout_vendor_view_product_1


 """
 Product layout 1
 """
 layout_products_1 ="""
import React from 'react';
@@Imports@@
const @@PageName@@ = () => {
    useDocumentTitle('@@DocumentTitle@@');
    const store = useSelector((state) => ({
        products: state.products,
        requestStatus: state.app.requestStatus
    }), shallowEqual);

    return (
        <>
            @@Pos1@@
            <section className="bg-gray-50">
                <div className="px-3 md:px-0 lg:px-0 py-[50px] pb-[80px] luday_wrap">
                @@Pos2@@
                </div>
            </section>
            
            @@Pos3@@
        </>
  );
}
export default @@PageName@@;
 """
 layouts["layout_products_1"] = layout_products_1


 """
 Products details layout 1
 """
 layout_products_details_1 ="""
import React, {useState, useEffect} from 'react';
@@Imports@@
SwiperCore.use([Navigation, Autoplay]);
const @@PageName@@ = () => {
  useDocumentTitle('@@DocumentTitle@@');
  const [relatedProducts, setRelatedProducts] = useState([]);
  const [vendor, setVendor] = useState('');
  const {slug} = useParams();
  const [thumbsSwiper, setThumbsSwiper] = useState(null);
  const [products, setProducts] = useState([]);

  const getProductsBySlug = (slug) => {
      fetch(`${ROUTE.PRODUCTS_API}/products/details/${slug}`)
      .then((res) => res.json())
      .then((res) => {
          setProducts(res.data);
          getRelatedProducts(res.data[0].product_category_slug);
          getVendorData(res.data[0].vendor_id)
      })
      
      .catch((e) => {
          console.error(e);
        });
  }
  const getRelatedProducts = (catslug) => {
      fetch(`${ROUTE.PRODUCTS_API}/categories/${catslug}/products`)
      .then((res) => res.json())
      .then((res) => {
          setRelatedProducts(res.results)
      })
  }
  const getVendorData = (vendor_id) => {
      fetch(`${ROUTE.USER_API}/user/vendors/${vendor_id}/vendor`)
        .then((res) => res.json())
        .then((res) => {
          setVendor(res.vendor[0].slug)
        })
  }

  const dispatch = useDispatch();
  const btnAddToCart = (products) => {
      dispatch(addToCart(products));
  }

  useEffect(() => {
      getProductsBySlug(slug)
      window.scrollTo(0, 0)
  }, [slug])

  let relatedProductsList = ''
  if(relatedProducts.length > 0) {
      relatedProductsList = (
          <>
          <div className="px-3 md:px-4 lg:px-12 py-[50px] pb-[80px] luday_wrap" > 
              <Swiper 
              breakpoints={{
                  0: {
                      slidesPerView: 1
                  },
                  480: {
                      slidesPerView: 2
                  },
                  768: {
                      slidesPerView: 3
                  },
                  1024: {
                      slidesPerView: 4
                  }
              }}
              tag="section"
              wrapperTag="ul"
              slidesPerView={4} 
              loop={true} autoplay={{delay: 2500, disableOnInteraction: false}} navigation={true} className="mx-auto">
              { relatedProducts.filter((relatedProducts) => relatedProducts.id !== products.id)?.map(product =>
                  <SwiperSlide className="" key={product.id} tag="li">
                      <div className="group bg-white mx-0 px-0 py-2">
                          <div className='products '>
                              <Link to={`${ROUTE.PRODUCT_DETAILS}/${product.slug}`}  >
                                  <div className="p-[10px] pb-[5px]">
                                      <img className="lazy h-60 w-full" src={`${CONSTANT.IMAGE_STORE}/${product.image_path}`} alt={product.name} />            
                                      <div className="gis-text pt-4">
                                          <p className="text-lg md:text-xl overflow-hidden w-full h-8 text-left lg:text-xl font-bold">{product.name}</p>
                                          <div className="flex flex-row">
                                              <p className="text-md font-medium order-first">
                                                  <span className={
                                                  product.sale_price ? "line-through font-light text-sm mr-1" : "" }>
                                                      &#8358;{displayMoney(product.price)}
                                                  </span>
                                              </p>
                                              <p className="text-md font-medium">
                                                      {product.sale_price ? (
                                                          <span>&#8358;{displayMoney(product.sale_price)}</span>
                                                      ) : (<span><br/></span>)
                                                      }
                                              </p>
                                          </div>

                                      </div>
                                  </div>
                              </Link>
                          </div> 
                      </div>
                  </SwiperSlide>
              ) }
              </Swiper>
          </div>
          </>)
  }
  else {
      relatedProductsList = (
          <div className="text-center">
              <div className="px-3 md:px-10 lg:px-36 py-[50px] pb-[80px] luday_wrap">
                  <h2 className="text-4xl">@@EmptyProductsMssg@@</h2>
              </div>
          </div>
      )
  }
  

  return (
    <>
      {products.length > 0 ?
        (
          <>
            @@Pos1@@
            <div className="py-2 px-[15px] md:px-[60px] lg:px-[140px]"> 
                <div className="grid grid-cols-1 md:grid-cols-2 luday_grid_wrap py-[60px]"> 
                    <div className="group">
                        <div className="grid grid-cols-1 md:p-5 pt-2">
                            <div className="group bg-white">
                            <Swiper
                                spaceBetween={10}
                                navigation={true}
                                thumbs={{ swiper: thumbsSwiper }}
                                modules={[FreeMode, Navigation, Thumbs]}
                                className="mySwiper2"
                            >
                                <SwiperSlide>
                                    <img className="lazy h-auto w-full" src={`${CONSTANT.IMAGE_STORE}/${products[0].image_path}`} alt={products[0].name} />
                                </SwiperSlide>
                                {products[0].products_gallery &&
                                products[0].products_gallery.map(product_gallery =>
                                    <SwiperSlide key={product_gallery.id}>
                                        <img className="lazy h-auto w-60" src={`${CONSTANT.IMAGE_STORE}/${product_gallery.path}`} alt={product_gallery.name} />
                                    </SwiperSlide>
                                )}
                            </Swiper>
                            <Swiper
                                onSwiper={setThumbsSwiper}
                                spaceBetween={10}
                                slidesPerView={4}
                                freeMode={true}
                                watchSlidesProgress={true}
                                modules={[FreeMode, Navigation, Thumbs]}
                                className="mySwiper mt-2"
                            >
                                <SwiperSlide className='border-solid border-2'>
                                    <img className="lazy  w-auto h-[70px] md:h-28" src={`${CONSTANT.IMAGE_STORE}/${products[0].image_path}`} alt={products[0].name} />
                                </SwiperSlide>
                                {products[0].products_gallery &&
                                products[0].products_gallery.map(product_gallery =>
                                    <SwiperSlide key={product_gallery.id}>
                                        <img className="lazy  w-auto h-[70px] md:h-28" src={`${CONSTANT.IMAGE_STORE}/${product_gallery.path}`} alt={product_gallery.name} />
                                    </SwiperSlide>
                                )}
                            </Swiper>
                        </div>
                    </div> 
                    </div>
                    <div className="group md:pl-4">
                    <p className="tracking-widest mb-2.5 text-xs ">@@DealsTitleText@@</p>
                    <h3>{products[0].name}</h3>
                    <div className="inline-grid grid-cols-3 gap-3 whitespace-nowrap">
                    <p className="text-[#9c0] text-xl pb-2"><b>Price:</b></p>
                    {products[0].sale_price ? (
                        <p className="text-[#9c0] text-xl pb-2">&#8358;{products[0].sale_price}</p>
                    ) : (<span><br/></span>)
                    }
                    <p className={
                        products[0].sale_price ? "line-through font-light -ml-2 text-gray-400 text-xl pb-2" : " -ml-16 text-[#9c0] text-xl pb-2" }>
                        &#8358;{products[0].price}
                    </p>
                    
                    </div>
                    <p className="my-4">{products[0].description}</p>
                    <p className="my-4"><Link to={`${ROUTE.VENDORDETAILS}/${vendor}`} className="py-3 text-gray-500">@@VisitVendorLink@@</Link></p>
                    <div className="button-wrap">
                        <button 
                            onClick={() => btnAddToCart(products[0])} 
                            className="w-full mt-9 font-semibold leading-none text-white py-4 px-10 bg-[#98c01d] rounded-md hover:bg-[#88af14] focus:ring-2 focus:ring-offset-2 focus:outline-none cursor-pointer md:w-2/3">
                                @@AddToCartText@@
                        </button>
                    </div>
                    </div>
                </div>
            </div>
          </>
        )
      :(
        <div className="text-center">
            <div className="px-3 md:px-10 lg:px-36 py-[200px] pb-[80px] luday_wrap">
                <h2 className="text-2xl">@@EmptyProductServiceMssg@@</h2>
            </div>
        </div>
      )}
      <div className="justify-center mx-auto text-center mb-10">@@InfoText1@@ <Link to={`${ROUTE.SIGNUP_VENDOR}`} className="text-[#88af14]"> @@InfoText2@@</Link> @@InfoText3@@</div>
      <section className="bg-gray-100">
          <div className="px-3 md:px-10 luday_wrap">
              <div className="text-center py-5">
                  <p className="tracking-widest text-xs text-gray-500">@@DefaultPropstitleText@@</p>
                  <h3 className="text-6xl luday_deals">@@RelatedProductsText@@</h3>
                  <section className="bg-gray-100">
                      { relatedProductsList }
                  </section>
              </div>
          </div>
      </section>
      @@Pos2@@
    </>
  );  
}
export default @@PageName@@;
 """
 layouts["layout_products_details_1"] = layout_products_details_1


 """
 Products category layout 1
 """
 layout_products_category_1 ="""
import React, { useEffect, useState } from "react";
@@Imports@@
const @@PageName@@ = () => {
  const [products, setProducts] = useState([]);
    const [loading, setLoading] = useState(false);
    const [currentPage] = useState(1);
    const [productsPerPage] = useState(20);
    const {slug} = useParams();
    const [search_query, setSearch_query] = useState('')
    //const [filteredResults, setFilteredResults] = useState([]);
    //const [searchInput, setSearchInput] = useState('');
    const dispatch = useDispatch();
    const nf = new Intl.NumberFormat();
    var myStr = slug;
    var newStr = myStr.replace("-", " & ")
    useDocumentTitle(`Best deals in ${newStr} | BestDealNaija`);
    //console.log(newStr)
    const getProducts = async () => {
        await fetch(`${ROUTE.PRODUCTS_API}/categories/${slug}/products`)
        .then((res) => res.json())
        .then((res) => {
            setProducts(res.results);
            setLoading(false);
            dispatch(getProductsSuccess({
                products: res.results
            }));
        })
    }

    useEffect(() => {
        getProducts()
        window.scrollTo(0, 0)
    }, [slug])

    const indexOfLastProduct = currentPage * productsPerPage;
    const indexOfFirstPost = indexOfLastProduct - productsPerPage;
    const currentProducts = products.slice(indexOfFirstPost, indexOfLastProduct)

    const btnIncreaseQtyCartList = (product) => {
        dispatch(addToCart(product));
    }

    const navigate = useNavigate()
    const params = { sort: search_query };

    const searchItems = () => {
        navigate({
            pathname: '/search',
            search: `?${createSearchParams(params)}`
          });
    } 
    
    let productsList = ''
    if (products.length > 0) {
        productsList = (<div className="px-3 md:px-[120px] lg:px-[120px] py-[20px] pb-[80px] luday_wrap">  
        <div className="grid grid-cols-1 md:grid-cols-3 gap-2">                        
            {currentProducts.map(product =>
                <div className="place-self-stretch" key={product.id}>
                    <div className="group mx-0 px-2 py-2">
                        <div className='products'>
                            <Link to={`${ROUTE.PRODUCT_DETAILS}/${product.slug}`}>
                                <div className="pb-[5px] text-center bg-white shadow-xl">
                                    <img className="lazy h-60 w-full" src={`${CONSTANT.IMAGE_STORE}/${product.image_path}`} alt={product.name} />            
                                    <div className="gis-text text-center pt-4 overflow-hidden w-full h-20">
                                        <p className="text-lg md:text-xl lg:text-xl font-bold overflow-hidden text-ellipsis whitespace-nowrap px-3">{product.name}</p>
                                        <div className="row text-center">
                                            <p className="text-md font-medium order-first text-bold text-center">
                                                {product.sale_price ? (
                                                    <span>&#8358;{nf.format(product.sale_price)}</span>
                                                ) : ''
                                                } &nbsp;  
                                                <span className={
                                                product.sale_price ? "line-through font-light text-center text-sm mr-1 text-gray-500" : "" }>
                                                    &#8358;{nf.format(product.price)}
                                                </span>
                                            </p>
                                        </div>
                                    </div>
                                </div>
                            </Link>
                            <div className="row px-[10px] py-2 text-center bg-white">                                       
                                <div className="custom-number-input w-full pb-3">
                                    <div className="row w-full rounded-lg relative bg-transparent">
                                        <button onClick={() => btnIncreaseQtyCartList(product)} className="w-full mt-1 font-semibold leading-none text-white py-4 px-10 bg-[#98c01d] rounded-md hover:bg-[#88af14] focus:ring-2 focus:ring-offset-2 focus:outline-none cursor-pointer md:w-2/3">@@AddToCartBtn@@</button>
                                    </div>
                                </div>
                            </div>
                        </div> 
                    </div>
                </div>
            )}
        </div><br />
        <div className="justify-center mx-auto text-center">Click <Link to={`${ROUTE.SIGNUP_VENDOR}`} className="text-[#88af14]"> HERE</Link> to start SELLING your PRODUCTS now </div>
    </div>) 
    }
    else {
        productsList = (
            <div className="text-center">
                <div className="px-3 md:px-10 lg:px-36 py-[50px] pb-[80px] luday_wrap">
                    <h1 className="text-4xl">@@NavToProductsCategoryText@@</h1>
                </div>
            </div>
        )
    }
    let introbanner = ''
    if (products.length > 0) {
        introbanner=(
          @@Pos1BannerIffProductsExist@@
      )
    }
    else{
        introbanner=(
            @@Pos1BannerIffProductsIsEmpty@@
        )
    }
    
  return (
    <>
        {introbanner}
        <div className="text-center py-10 luday_deals bg-gray-50">
            <div className="flex justify-center py-8">
                <form id="submitForm" onSubmit={(e) => searchItems(e.target.value)}>
                    <div className="flex items-center flex-nowrap">
                        <input name="search_product" id="productName" value={search_query} onChange={(e) => setSearch_query(e.target.value)} type="search" className="focus:ring-green-500 w-full" placeholder="Search" aria-label="Search"
                        aria-describedby="search-addon" />
                        <button name="searchBtn" value="1" type="submit" className="bg-transparent hover:bg-gray-200 text-green-700 font-semibold hover:text-white py-2 px-2 border border-green-500"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" className="hover:text-white"><path d="M19.023 16.977a35.13 35.13 0 0 1-1.367-1.384c-.372-.378-.596-.653-.596-.653l-2.8-1.337A6.962 6.962 0 0 0 16 9c0-3.859-3.14-7-7-7S2 5.141 2 9s3.14 7 7 7c1.763 0 3.37-.66 4.603-1.739l1.337 2.8s.275.224.653.596c.387.363.896.854 1.384 1.367l1.358 1.392.604.646 2.121-2.121-.646-.604c-.379-.372-.885-.866-1.391-1.36zM9 14c-2.757 0-5-2.243-5-5s2.243-5 5-5 5 2.243 5 5-2.243 5-5 5z"></path></svg></button>
                    </div>
                </form>
            </div>
        </div>
        
        <div className="w-full">
            {loading ?
                <div className="py-2">
                    <div className="px-3 md:px-10 lg:px-36 py-[50px] pb-[80px] luday_wrap">  
                        <div className="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-2 gap-9">
                            <div className="w-full flex items-stretch flex-col p-[10px] pb-[5px]">
                                <div className="bg-white shadow rounded">
                                    <div data-placeholder className="w-full h-60 bg-gray-200 overflow-hidden relative">
                                    </div>
                                    <div className="pt-4 p-3">
                                        <p data-placeholder className="h-7 mb-2 w-full md:w-4/5 bg-gray-200 overflow-hidden relative"></p>
                                        <p data-placeholder className="h-4 mb-1 w-1/3 bg-gray-200 overflow-hidden relative"></p>
                                        <span data-placeholder className="h-6 mt-4 w-20 rounded-md bg-gray-200 overflow-hidden relative block px-[10px]">  
                                        </span>
                                    </div>
                                </div>
                            </div>

                            <div className="w-full flex items-stretch flex-col p-[10px] pb-[5px]">
                                <div className="bg-white shadow rounded">
                                    <div data-placeholder className="w-full h-60 bg-gray-200 overflow-hidden relative">
                                    </div>
                                    <div className="pt-4 p-3">
                                        <p data-placeholder className="h-7 mb-2 w-full md:w-4/5 bg-gray-200 overflow-hidden relative"></p>
                                        <p data-placeholder className="h-4 mb-1 w-1/3 bg-gray-200 overflow-hidden relative"></p>
                                        <span data-placeholder className="h-6 mt-4 w-20 rounded-md bg-gray-200 overflow-hidden relative block px-[10px]">  
                                        </span>
                                    </div>
                                </div>
                            </div>
                            <div className="w-full  items-stretch flex-col p-[10px] pb-[5px] hidden md:flex">
                                <div className="bg-white shadow rounded">
                                    <div data-placeholder className="w-full h-60 bg-gray-200 overflow-hidden relative">
                                    </div>
                                    <div className="pt-4 p-3">
                                        <p data-placeholder className="h-7 mb-2 w-full md:w-4/5 bg-gray-200 overflow-hidden relative"></p>
                                        <p data-placeholder className="h-4 mb-1 w-1/3 bg-gray-200 overflow-hidden relative"></p>
                                        <span data-placeholder className="h-6 mt-4 w-20 rounded-md bg-gray-200 overflow-hidden relative block px-[10px]">  
                                        </span>
                                    </div>
                                </div>
                            </div>
                            <div className="w-full items-stretch flex-col p-[10px] pb-[5px] hidden md:flex">
                                <div className="bg-white shadow rounded">
                                    <div data-placeholder className="w-full h-60 bg-gray-200 overflow-hidden relative">
                                    </div>
                                    <div className="pt-4 p-3">
                                        <p data-placeholder className="h-7 mb-2 w-full md:w-4/5 bg-gray-200 overflow-hidden relative"></p>
                                        <p data-placeholder className="h-4 mb-1 w-1/3 bg-gray-200 overflow-hidden relative"></p>
                                        <span data-placeholder className="h-6 mt-4 w-20 rounded-md bg-gray-200 overflow-hidden relative block px-[10px]">  
                                        </span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            :
            products &&
                (
                    
                    <section className="bg-gray-50">
                        {
                            productsList
                        }
                        @@Pos2@@
                    </section> 
                )
            }
        </div>
      @@Pos3@@
    </>
  )  
}
export default @@PageName@@;
 """
 layouts["layout_products_category_1"] = layout_products_category_1


 """
 Products list 1
 """
 layout_products_list_1 ="""
import React, { useEffect } from "react";
@@Imports@@
const @@PageName@@ = (props) => {
    const {
      products, productsArr, isLoading, requestStatus, children
    } = props;
    
    const dispatch = useDispatch();

    const fetchProducts = () => {
        dispatch(getProducts());
    };

    useEffect(() => {
        if (products.items.length === 0) {
          fetchProducts();
        }
    
        window.scrollTo(0, 0);
        return () => dispatch(setLoading(false));
      }, []);

    if (productsArr.length === 0 && !isLoading) {
        return (
          requestStatus?.message || '@@NoProductsMssg@@'
        );
    }
    if (productsArr.length === 0 && requestStatus) {
        return (
          requestStatus?.message || '@@ErrorMssg@@'
        );
    }
    return (
        <>
			{/* <ErrorBoundary> */}
				{children}
			{/* </ErrorBoundary> */}
        </>
    );
};

@@PageName@@.defaultProps = {
    requestStatus: null
};

@@PageName@@.propTypes = {
	products: PropType.object.isRequired,
	productsArr: PropType.array.isRequired,
	isLoading: PropType.bool.isRequired,
	requestStatus: PropType.string,
	children: PropType.oneOfType([
		PropType.arrayOf(PropType.node),
		PropType.node
	]).isRequired
};

export default @@PageName@@;
 """
 layouts["layout_products_list_1"] = layout_products_list_1

 """
 Search product layout 1
 """
 layout_search_product_1 ="""
import React, { useEffect } from "react";
@@Imports@@
const @@PageName@@ = () => {
    const {searchQuery} = useParams();
    const dispatch = useDispatch();
    const didMount = useDidMount(true);

    const store = useSelector((state) => ({
        isLoading: state.app.loading,
        products: state.products.searchedProducts.items,
        search: state.products.searchedProducts,
        basket: state.basket,
        requestStatus: state.app.requestStatus
    }));
    const lastRefKey = store.search.lastRefKey

    useEffect(() => {
        if (didMount && !store.isLoading) {
            dispatch(searchProduct(searchQuery));
        }
        window.scrollTo(0, 0);
		return () => dispatch(setLoading(false));
    }, [searchQuery]);

    useEffect(() => {
        dispatch(setRequestStatus(''));
    }, [lastRefKey]);

    const getSearchProducts = () => {
		dispatch(searchProduct(searchQuery, lastRefKey));
    }

    const btnIncreaseQtyCartList = (product) => {
        dispatch(addToCart(product));
    }

    let productsList = ''
    if (store.products.length !== 0) {
        productsList = (<div className="px-3 md:px-[120px] lg:px-[120px] py-[20px] pb-[40px] luday_wrap">  
        <div className="text-center">
            <div className="px-3 md:px-10 lg:px-36 py-[20px] pb-[40px] luday_wrap">
                <h1 className="text-4xl">@@SearchPlaceholder@@ &quot; {searchQuery} &quot;</h1>
            </div>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-2">                        
            {store.products.map(product =>
                <div className="place-self-stretch" key={product.id}>
                    <div className="group mx-0 px-2 py-2">
                        <div className='products'>
                            <Link to={`${ROUTE.PRODUCT_DETAILS}/${product.slug}`} state={product}>
                                <div className="pb-[5px] text-center bg-white shadow-xl">
                                    <img className="lazy h-60 w-full" src={`${CONSTANT.IMAGE_STORE}/${product.image_path}`} alt={product.name} />            
                                    <div className="gis-text text-center pt-4">
                                        <p className="text-lg md:text-xl lg:text-xl font-bold overflow-hidden text-ellipsis whitespace-nowrap px-3">{product.name}</p>
                                        <div className="row text-center">
                                            <p className="text-md font-medium order-first text-bold text-center">
                                                {product.sale_price ? (
                                                    <span>&#8358;{displayMoney(product.sale_price)}</span>
                                                ) : ""
                                                } &nbsp;  
                                                <span className={
                                                product.sale_price ? "line-through font-light text-center text-sm mr-1 text-gray-500" : "" }>
                                                    &#8358;{displayMoney(product.price)}
                                                </span>
                                            </p>
                                        </div>
                                    </div>
                                </div>
                            </Link>
                            <div className="row px-[10px] py-2 text-center bg-white">                                       
                                <div className="custom-number-input w-full pb-3">
                                    <div className="row w-full rounded-lg relative bg-transparent">
                                        <button onClick={() => btnIncreaseQtyCartList(product)} className="w-full mt-1 font-semibold leading-none text-white py-4 px-10 bg-[#98c01d] rounded-md hover:bg-[#88af14] focus:ring-2 focus:ring-offset-2 focus:outline-none cursor-pointer md:w-2/3">Add to cart</button>
                                    </div>
                                </div>
                            </div>
                        </div> 
                    </div>
                </div>
            )}
        </div><br />
        {store.search.nextPage && (
            <div className="flex space-x-2 justify-center pb-10">
                <button 
                    type="button"
                    disabled={store.isLoading}
                    onClick={getSearchProducts}
                    className="inline-block px-6 py-2.5 bg-[#98c01d] text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-[#88af14] hover:shadow-lg focus:[#88af14] focus:shadow-lg focus:outline-none focus:ring-0 active:bg-[#98c01d] active:shadow-lg transition duration-150 ease-in-out">
                    {store.isLoading ? '@@ShowMoreBtnOnLoadingText@@' : '@@ShowMoreBtnText@@'}
                </button>
            </div>
        )}

        <div className="justify-center mx-auto text-center">@@InfoText1@@ <Link to={`${ROUTE.SIGNUP_VENDOR}`} className="text-[#88af14]"> @@InfoText2@@</Link> @@InfoText3@@ </div>
    </div>) 
    }
    else {
        productsList = (
            <div className="text-center">
                <div className="px-3 md:px-10 lg:px-36 py-[50px] pb-[80px] luday_wrap">
                    <h1 className="text-4xl">@@NoProductsMssg@@ &quot; {searchQuery} &quot;</h1>
                </div>
            </div>
        )
    }

    return (
        <>
        @@Pos1@@
        <div className="text-center mt-12 md:mt-5">
            @@Pos2@@
        </div>
       
        <div className="">
            {store.isLoading ?
                <div className="py-2">
                    <div className="px-3 md:px-10 lg:px-36 py-[50px] pb-[80px] luday_wrap">  
                        <div className="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-2 gap-9">
                            <div className="w-full flex items-stretch flex-col p-[10px] pb-[5px]">
                                <div className="bg-white shadow rounded">
                                    <div data-placeholder className="w-full h-60 bg-gray-200 overflow-hidden relative">
                                    </div>
                                    <div className="pt-4 p-3">
                                        <p data-placeholder className="h-7 mb-2 w-full md:w-4/5 bg-gray-200 overflow-hidden relative"></p>
                                        <p data-placeholder className="h-4 mb-1 w-1/3 bg-gray-200 overflow-hidden relative"></p>
                                        <span data-placeholder className="h-6 mt-4 w-20 rounded-md bg-gray-200 overflow-hidden relative block px-[10px]">  
                                        </span>
                                    </div>
                                </div>
                            </div>

                            <div className="w-full flex items-stretch flex-col p-[10px] pb-[5px]">
                                <div className="bg-white shadow rounded">
                                    <div data-placeholder className="w-full h-60 bg-gray-200 overflow-hidden relative">
                                    </div>
                                    <div className="pt-4 p-3">
                                        <p data-placeholder className="h-7 mb-2 w-full md:w-4/5 bg-gray-200 overflow-hidden relative"></p>
                                        <p data-placeholder className="h-4 mb-1 w-1/3 bg-gray-200 overflow-hidden relative"></p>
                                        <span data-placeholder className="h-6 mt-4 w-20 rounded-md bg-gray-200 overflow-hidden relative block px-[10px]">  
                                        </span>
                                    </div>
                                </div>
                            </div>
                            <div className="w-full  items-stretch flex-col p-[10px] pb-[5px] hidden md:flex">
                                <div className="bg-white shadow rounded">
                                    <div data-placeholder className="w-full h-60 bg-gray-200 overflow-hidden relative">
                                    </div>
                                    <div className="pt-4 p-3">
                                        <p data-placeholder className="h-7 mb-2 w-full md:w-4/5 bg-gray-200 overflow-hidden relative"></p>
                                        <p data-placeholder className="h-4 mb-1 w-1/3 bg-gray-200 overflow-hidden relative"></p>
                                        <span data-placeholder className="h-6 mt-4 w-20 rounded-md bg-gray-200 overflow-hidden relative block px-[10px]">  
                                        </span>
                                    </div>
                                </div>
                            </div>
                            <div className="w-full items-stretch flex-col p-[10px] pb-[5px] hidden md:flex">
                                <div className="bg-white shadow rounded">
                                    <div data-placeholder className="w-full h-60 bg-gray-200 overflow-hidden relative">
                                    </div>
                                    <div className="pt-4 p-3">
                                        <p data-placeholder className="h-7 mb-2 w-full md:w-4/5 bg-gray-200 overflow-hidden relative"></p>
                                        <p data-placeholder className="h-4 mb-1 w-1/3 bg-gray-200 overflow-hidden relative"></p>
                                        <span data-placeholder className="h-6 mt-4 w-20 rounded-md bg-gray-200 overflow-hidden relative block px-[10px]">  
                                        </span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            :
                (
                    <section className="bg-gray-50">
                        { productsList }
                    </section> 
                )
            }
        </div>
        @@Pos3@@
        </>
    )
}
export default @@PageName@@;
 """
 layouts["layout_search_product_1"] = layout_search_product_1


 """
 Vendor products layout 1
 """
 layout_vendor_products_1 ="""
import React, { useEffect, useState, useCallback} from "react";
@@Imports@@
const @@PageName@@ = () => {
    const [products, setProducts] = useState([]);
    const [loading, setLoading] = useState(false);
    const [currentPage] = useState(1);
    const [productsPerPage] = useState(20);
    const {slug} = useParams();
    const [search_query, setSearch_query] = useState('')
    const [vendor, fetchVendors] = useState([]);
    //const [searchInput, setSearchInput] = useState('');
    
    const dispatch = useDispatch();
    const nf = new Intl.NumberFormat();

    const getData = () => {
        //setLoading(true)
      fetch(`${ROUTE.USER_API}/user/vendors/${slug}`)
        .then((res) => res.json())
        .then((res) => {
            fetchVendors(res.vendor)
            getProducts(res.vendor[0].id)
        })
      }

    const getProducts = useCallback(async (vendor_id) => {
        await fetch(`${ROUTE.PRODUCTS_API}/vendors/products/${vendor_id}/verified`)
        .then((res) => res.json())
        .then((res) => {
            setProducts(res.results);
            setLoading(false);
            dispatch(getProductsSuccess({
                products: res.results
            }));
        })
    })

    useEffect(() => {
        getData()
    }, [])

    const indexOfLastProduct = currentPage * productsPerPage;
    const indexOfFirstPost = indexOfLastProduct - productsPerPage;
    const currentProducts = products.slice(indexOfFirstPost, indexOfLastProduct)

    const btnIncreaseQtyCartList = (product) => {
        dispatch(addToCart(product));
    }

    const navigate = useNavigate()
    const params = { sort: search_query };

    const searchItems = () => {
        navigate({
            pathname: '/search',
            search: `?${createSearchParams(params)}`
          });
    } 
    
    let productsList = ''
    if (products.length > 0) {
        productsList = (<div className="px-3 md:px-[120px] lg:px-[120px] py-[20px] pb-[80px] luday_wrap">  
        <div className="grid grid-cols-1 md:grid-cols-3 gap-2">                        
            {currentProducts.map(product =>
                <div className="place-self-stretch" key={product.id}>
                    <div className="group mx-0 px-2 py-2">
                        <div className='products'>
                            <Link to={`${ROUTE.PRODUCT_DETAILS}/${product.slug}`}>
                                <div className="pb-[5px] text-center bg-white shadow-xl">
                                    <img className="lazy h-60 w-full" src={`${CONSTANT.IMAGE_STORE}/${product.image_path}`} alt={product.name} />            
                                    <div className="gis-text text-center pt-4 overflow-hidden w-full h-20">
                                        <p className="text-lg md:text-xl lg:text-xl font-bold overflow-hidden text-ellipsis whitespace-nowrap px-3">{product.name}</p>
                                        <div className="row text-center">
                                            <p className="text-md font-medium order-first text-bold text-center">
                                                {product.sale_price ? (
                                                    <span>&#8358;{nf.format(product.sale_price)}</span>
                                                ) : ''
                                                } &nbsp;  
                                                <span className={
                                                product.sale_price ? "line-through font-light text-center text-sm mr-1 text-gray-500" : "" }>
                                                    &#8358;{nf.format(product.price)}
                                                </span>
                                            </p>
                                        </div>
                                    </div>
                                </div>
                            </Link>
                            <div className="row px-[10px] py-2 text-center bg-white">                                       
                                <div className="custom-number-input w-full pb-3">
                                    <div className="row w-full rounded-lg relative bg-transparent">
                                        <button onClick={() => btnIncreaseQtyCartList(product)} className="w-full mt-1 font-semibold leading-none text-white py-4 px-10 bg-[#98c01d] rounded-md hover:bg-[#88af14] focus:ring-2 focus:ring-offset-2 focus:outline-none cursor-pointer md:w-2/3">@@AddToCartBtn@@</button>
                                    </div>
                                </div>
                            </div>
                        </div> 
                    </div>
                </div>
            )}
        </div><br />
        <div className="justify-center mx-auto text-center">@@InfoText1@@ <Link to={`${ROUTE.SIGNUP_VENDOR}`} className="text-[#88af14]"> @@InfoText2@@</Link> @@InfoText3@@ </div>
    </div>) 
    }
    else {
        productsList = (
            <div className="text-center">
                <div className="px-3 md:px-10 lg:px-36 py-[50px] pb-[80px] luday_wrap">
                    <h1 className="text-4xl">@@NoProductsMssg@@</h1>
                </div>
            </div>
        )
    }
    let introbanner = ''
    if (vendor.length > 0) {
        introbanner=(
            @@Pos1BannerIffVendorExist@@
        )
    }
    else{
        introbanner=(
            @@Pos1BannerIffVendorIsEmpty@@
        )
    }
    
  return (
    <>
        {introbanner}
        <div className="text-center py-10 luday_deals bg-gray-50">
            <div className="flex justify-center py-8">
                <form id="submitForm" onSubmit={(e) => searchItems(e.target.value)}>
                    <div className="flex items-center flex-nowrap">
                        <input name="search_product" id="productName" value={search_query} onChange={(e) => setSearch_query(e.target.value)} type="search" className="focus:ring-green-500 w-full" placeholder="Search" aria-label="Search"
                        aria-describedby="search-addon" />
                        <button name="searchBtn" value="1" type="submit" className="bg-transparent hover:bg-gray-200 text-green-700 font-semibold hover:text-white py-2 px-2 border border-green-500"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" className="hover:text-white"><path d="M19.023 16.977a35.13 35.13 0 0 1-1.367-1.384c-.372-.378-.596-.653-.596-.653l-2.8-1.337A6.962 6.962 0 0 0 16 9c0-3.859-3.14-7-7-7S2 5.141 2 9s3.14 7 7 7c1.763 0 3.37-.66 4.603-1.739l1.337 2.8s.275.224.653.596c.387.363.896.854 1.384 1.367l1.358 1.392.604.646 2.121-2.121-.646-.604c-.379-.372-.885-.866-1.391-1.36zM9 14c-2.757 0-5-2.243-5-5s2.243-5 5-5 5 2.243 5 5-2.243 5-5 5z"></path></svg></button>
                    </div>
                </form>
            </div>
        </div>
        
        <div className="w-full">
            {loading ?
                <div className="py-2">
                    <div className="px-3 md:px-10 lg:px-36 py-[50px] pb-[80px] luday_wrap">  
                        <div className="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-2 gap-9">
                            <div className="w-full flex items-stretch flex-col p-[10px] pb-[5px]">
                                <div className="bg-white shadow rounded">
                                    <div data-placeholder className="w-full h-60 bg-gray-200 overflow-hidden relative">
                                    </div>
                                    <div className="pt-4 p-3">
                                        <p data-placeholder className="h-7 mb-2 w-full md:w-4/5 bg-gray-200 overflow-hidden relative"></p>
                                        <p data-placeholder className="h-4 mb-1 w-1/3 bg-gray-200 overflow-hidden relative"></p>
                                        <span data-placeholder className="h-6 mt-4 w-20 rounded-md bg-gray-200 overflow-hidden relative block px-[10px]">  
                                        </span>
                                    </div>
                                </div>
                            </div>

                            <div className="w-full flex items-stretch flex-col p-[10px] pb-[5px]">
                                <div className="bg-white shadow rounded">
                                    <div data-placeholder className="w-full h-60 bg-gray-200 overflow-hidden relative">
                                    </div>
                                    <div className="pt-4 p-3">
                                        <p data-placeholder className="h-7 mb-2 w-full md:w-4/5 bg-gray-200 overflow-hidden relative"></p>
                                        <p data-placeholder className="h-4 mb-1 w-1/3 bg-gray-200 overflow-hidden relative"></p>
                                        <span data-placeholder className="h-6 mt-4 w-20 rounded-md bg-gray-200 overflow-hidden relative block px-[10px]">  
                                        </span>
                                    </div>
                                </div>
                            </div>
                            <div className="w-full  items-stretch flex-col p-[10px] pb-[5px] hidden md:flex">
                                <div className="bg-white shadow rounded">
                                    <div data-placeholder className="w-full h-60 bg-gray-200 overflow-hidden relative">
                                    </div>
                                    <div className="pt-4 p-3">
                                        <p data-placeholder className="h-7 mb-2 w-full md:w-4/5 bg-gray-200 overflow-hidden relative"></p>
                                        <p data-placeholder className="h-4 mb-1 w-1/3 bg-gray-200 overflow-hidden relative"></p>
                                        <span data-placeholder className="h-6 mt-4 w-20 rounded-md bg-gray-200 overflow-hidden relative block px-[10px]">  
                                        </span>
                                    </div>
                                </div>
                            </div>
                            <div className="w-full items-stretch flex-col p-[10px] pb-[5px] hidden md:flex">
                                <div className="bg-white shadow rounded">
                                    <div data-placeholder className="w-full h-60 bg-gray-200 overflow-hidden relative">
                                    </div>
                                    <div className="pt-4 p-3">
                                        <p data-placeholder className="h-7 mb-2 w-full md:w-4/5 bg-gray-200 overflow-hidden relative"></p>
                                        <p data-placeholder className="h-4 mb-1 w-1/3 bg-gray-200 overflow-hidden relative"></p>
                                        <span data-placeholder className="h-6 mt-4 w-20 rounded-md bg-gray-200 overflow-hidden relative block px-[10px]">  
                                        </span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            :
            products &&
                (
                    
                    <section className="bg-gray-50">
                        {
                            productsList
                        }
                        @@Pos2@@
                    </section> 
                )
            }
        </div>
        @@Pos3@@
    </>
  )
}
export default @@PageName@@;
 """
 layouts["layout_vendor_products_1"] = layout_vendor_products_1


 """
 Tradefair layout 1
 """
 layout_trade_fair_1 ="""
import React from 'react';
@@Imports@@
const @@PageName@@ = () => {
  useDocumentTitle('@@DocumentTitle@@');
  useScrollTop();

  const title = '@@Title@@';
	const subtitle = '@@SubTitle@@';
	return (
		<>
			@@Pos1@@
			<div className="py-2 p-3">                   
				<div className="flex items-center flex-col-reverse lg:flex-row lg:justify-between gap-9">
					<div className="group py-12 lg:px-16 lg:w-1/2 lg:text-justify">
						<p className="tracking-widest mb-2.5 text-xs ">@@Paragraph1@@</p>
						<h4>@@HeaderText4@@</h4>
						<p className="my-4">@@Paragraph2@@</p>
						<p className="my-4">@@Paragraph3@@</p>		
					</div>
					<div className="lg:px-4 lg:w-1/2">
						<div className="grid gap-3 pb-2 grid-cols-2">
							<img className="lazy h-aufullto min-h-[40%] bg-cover bg-center" src={image1} alt="" />
							<img className="lazy h-full min-h-[40%] bg-cover bg-center" src={image2} alt="" />
						</div>
						<div className="grid gap-3 pt-2 grid-cols-3">
							<img className="lazy height_top min-h-[40%] bg-cover bg-center" src={image3} alt="" />
							<img className="lazy height_top min-h-[40%] bg-cover bg-center" src={image4} alt="" />
							<img className="lazy height_top min-h-[40%] bg-cover bg-center" src={image5} alt="" />
						</div>
					</div>
				</div>
			</div>
		</>
	);
}
export default @@PageName@@;
 """
 layouts["layout_trade_fair_1"] = layout_trade_fair_1


 """
 Contact Us layout 1
 """
 layout_contact_us_1 ="""
import React from 'react';
@@Imports@@
const @@PageName@@ = () => {
  const {register, handleSubmit, reset, formState: { errors } } = useForm();

  const successAlert = (response) => {
    return(
      swal({
          title: "Info!",
          text: response,
          icon: "success"
      })              
    )
  }

  const submitForm = (data) => {
    const body = {
      name: data.name,
      email: data.email,
      subject: data.subject,
      mobile: data.mobile,
      mssg: data.mssg
    }

    const requestOptions = {
        method: "POST",
        headers: {
          'content-type': 'application/json'
        },
        body: JSON.stringify(body)
    }

    fetch(`${ROUTE.CONTACT_API}/contact/add`, requestOptions)
      .then(res => res.json())
      .then(data =>{
        console.log(data)
        successAlert(data.message)
      })
      .catch(err => console.log(err))

    reset()
  }

  useDocumentTitle('@@DocumentTitle@@');
  useScrollTop();
  return (
    <>
      <section className="contact_hero">
        <div className="hero_inner">
            <div className="text-center">
                <p className="tracking-widest mb-4 text-xs text-gray-200">@@PreHeading1Title@@</p>
                <h1 className="text-6xl font-semibold text-white tracking-tight">@@PageTitleHeading1@@</h1>
            </div>
        </div>
      </section>
      <section>
        <div className="h-5/6 my-10">
          <div className="flex flex-col lg:flex-row-reverse justify-between lg:text-left">
            <div className="lg:w-3/5 flex flex-col justify-center">
              <div className="flex justify-center items-center">
                <div className="w-full my-4">
                  
                  <form className='rounded-md shadow-md p-8'>
                    <h2 className="text-center text-4xl uppercase font-bold">@@HeaderText2@@</h2>
                      <div className="md:flex items-center mt-12">
                          <div className="w-full md:w-1/2 flex flex-col">
                              <input type="text" placeholder='@@Input1Placeholder@@' 
                                  {...register("name", { required: true, maxLength: 25 })}
                                  className="leading-none text-gray-900 p-3 focus:outline-none focus:border-[#98c01d]
                                    mt-4 bg-white border rounded border-gray-200" />
                              {errors.name && <small className="text-red-500 text-xs italic">@@Input1ErrorMssg@@</small>}
                              {errors.name?.type === "maxLength" && <p style={{ color: "red" }}><small>@@Input1ErrorMssgAlt1@@ </small></p>}
                          </div>
                          <div className="w-full md:w-1/2 flex flex-col md:ml-6 md:mt-0 mt-4">
                              <input type="number" placeholder='@@Input2Placeholder@@' 
                                  {...register("mobile", { required: true, maxLength: 15 })}
                                  className="leading-none text-gray-900 p-3 focus:outline-none focus:border-[#98c01d] mt-4 bg-white border rounded border-gray-200"/>
                              {errors.mobile && <small className="text-red-500 text-xs italic">@@Input2ErrorMssg@@</small>}
                              {errors.mobile?.type === "maxLength" && <p style={{ color: "red" }}><small>@@Input2ErrorMssgAlt1@@ </small></p>}
                          </div>
                      </div>
                      <div className="md:flex items-center mt-12">
                          <div className="w-full md:w-1/2 flex flex-col">
                              <input type="email" placeholder='@@Input3Placeholder@@' 
                                  {...register("email", { required: true, maxLength: 100 })}
                                  className="leading-none text-gray-900 p-3 focus:outline-none focus:border-[#98c01d] mt-4 bg-white border rounded border-gray-200" />
                              {errors.email && <small className="text-red-500 text-xs italic">@@Input3ErrorMssg@@</small>}
                              {errors.email?.type === "maxLength" && <p style={{ color: "red" }}><small>@@Input3ErrorMssgAlt1@@ </small></p>}
                          </div>
                          <div className="w-full md:w-1/2 flex flex-col md:ml-6 md:mt-0 mt-4">
                              <input type="text" placeholder='@@Input4Placeholder@@' 
                                  {...register("subject", { required: true, maxLength: 80 })}
                                  className="leading-none text-gray-900 p-3 focus:outline-none focus:border-[#98c01d] mt-4 bg-white border rounded border-gray-200"/>
                              {errors.subject && <small className="text-red-500 text-xs italic">@@Input4ErrorMssg@@</small>}
                              {errors.subject?.type === "maxLength" && <p style={{ color: "red" }}><small>@@Input4ErrorMssgAlt1@@ </small></p>}
                          </div>
                          
                      </div>
                      <div>
                          <div className="w-full flex flex-col mt-8">
                              <textarea type="text" placeholder='@@Input5Placeholder@@' 
                                  {...register("mssg", { required: true, maxLength: 255 })}
                                  className="h-40 text-base leading-none text-gray-900 p-3 focus:outline-none focus:border-[#98c01d] mt-4 bg-white border rounded border-gray-200"></textarea>
                              {errors.mssg && <small className="text-red-500 text-xs italic">@@Input5ErrorMssg@@</small>}
                              {errors.mssg?.type === "maxLength" && <p style={{ color: "red" }}><small>@@Input5ErrorMssgAlt1@@ </small></p>}
                          </div>
                      </div>
                      <div className="flex items-center justify-center w-full">
                          <button type='submit' 
                            onClick={handleSubmit(submitForm)}
                            className="mt-9 font-semibold leading-none text-white py-4 px-10 bg-[#98c01d] rounded-md hover:bg-[#88af14] focus:ring-2 focus:ring-offset-2 focus:outline-none"
                          >
                            @@SubmitBtnText@@
                          </button>
                      </div>
                  </form>
                </div>
              </div>
            </div>
            <div className="lg:w-2/5 flex flex-col justify-center">
              <div className="flex align-middle px-8 lg:px-24 py-10">
                <div className="flex font-thin text-lg flex-col space-y-4">
                  <p className="">
                    <span className="inline-flex mr-3">
                      <svg 
                        xmlns="http://www.w3.org/2000/svg" 
                        width="24" 
                        height="24"
                        className="fill-[#98c01d]" 
                      >
                        <path d="M12 2C7.589 2 4 5.589 4 9.995 3.971 16.44 11.696 21.784 12 22c0 0 8.029-5.56 8-12 0-4.411-3.589-8-8-8zm0 12c-2.21 0-4-1.79-4-4s1.79-4 4-4 4 1.79 4 4-1.79 4-4 4z"></path>
                      </svg>
                    </span>

                    @@AddressParagraphText@@
                  </p>
                  <a 
                    href="tel:@@LinkTel1Text@@" 
                    className="text-green text-[#98c01d]"
                  >
                    <span className="inline-flex mr-3">
                      <svg 
                        xmlns="http://www.w3.org/2000/svg" 
                        width="24" 
                        height="24"
                        className="fill-[#98c01d]" 
                      >
                        <path d="m20.487 17.14-4.065-3.696a1.001 1.001 0 0 0-1.391.043l-2.393 2.461c-.576-.11-1.734-.471-2.926-1.66-1.192-1.193-1.553-2.354-1.66-2.926l2.459-2.394a1 1 0 0 0 .043-1.391L6.859 3.513a1 1 0 0 0-1.391-.087l-2.17 1.861a1 1 0 0 0-.29.649c-.015.25-.301 6.172 4.291 10.766C11.305 20.707 16.323 21 17.705 21c.202 0 .326-.006.359-.008a.992.992 0 0 0 .648-.291l1.86-2.171a.997.997 0 0 0-.085-1.39z"></path>
                      </svg>
                    </span>
                    
                    @@LinkTel1Text@@
                  </a>
                  <a 
                    href="@@LinkTel2Text@@" 
                    className="text-green text-[#98c01d]"
                  >
                    <span className="inline-flex mr-3">
                      <svg 
                        xmlns="http://www.w3.org/2000/svg" 
                        width="24" 
                        height="24"
                        className="fill-[#98c01d]" 
                      >
                        <path d="m20.487 17.14-4.065-3.696a1.001 1.001 0 0 0-1.391.043l-2.393 2.461c-.576-.11-1.734-.471-2.926-1.66-1.192-1.193-1.553-2.354-1.66-2.926l2.459-2.394a1 1 0 0 0 .043-1.391L6.859 3.513a1 1 0 0 0-1.391-.087l-2.17 1.861a1 1 0 0 0-.29.649c-.015.25-.301 6.172 4.291 10.766C11.305 20.707 16.323 21 17.705 21c.202 0 .326-.006.359-.008a.992.992 0 0 0 .648-.291l1.86-2.171a.997.997 0 0 0-.085-1.39z"></path>
                      </svg>
                    </span>
                    @@LinkTel2Text@@
                  </a>
                  <a 
                    href="mailto:@@LinkEmailText@@" className="text-[#98c01d]"
                  >
                      <span className="inline-flex mr-3">
                      <svg 
                        xmlns="http://www.w3.org/2000/svg" 
                        width="24" 
                        height="24"
                        className="fill-[#98c01d] contact_us"
                      >
                        <path d="M20 4H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2zm0 4.7-8 5.334L4 8.7V6.297l8 5.333 8-5.333V8.7z"></path>
                      </svg>
                      </span>
                    
                    @@LinkEmailText@@
                  </a>
                  <p className="">@@ParagraphWorkHourText@@</p>                          
                </div>
                  
              </div>
            </div>
          </div>
        </div>
      </section>
      <section>
          <div className="h-5/6 lg:mt-20">
              <div className="flex flex-col lg:flex-row justify-between lg:text-left">
                  <div className="w-full flex flex-col justify-center">
                      <iframe title="Bestdeal Map" className="w-full h-[480px]" src="@@GoogleMapIframeLink@@" allowFullScreen="" loading="lazy" referrerPolicy="no-referrer-when-downgrade"></iframe>
                  </div>
              </div>
          </div>
      </section>
    </>
  )  
}
export default @@PageName@@;
 """
 layouts["layout_contact_us_1"] = layout_contact_us_1

 """
 Cart layout 1
 """
 layout_cart_1 ="""
import React from 'react';
@@Imports@@
const @@PageName@@ = () => {
    useDocumentTitle('@@DocumentTitle@@');
    const { cart } = useSelector((state) => ({
		cart: state.cart
	}));
	const dispatch = useDispatch();

    const handleRemoveFromCart = (cartItem) => {
        dispatch(removeFromCart(cartItem));
    }
    const btnIncreaseQtyCartList = (cartItem) => {
        if (cartItem.cart_quantity < cartItem.quantity) {
			dispatch(addQtyItem(cartItem.id));
		}
    }
    const btnDecreaseQtyCartList = (cartItem) => {
		if ((cartItem.quantity >= cartItem.cart_quantity) && cartItem.cart_quantity !== 0) {
			dispatch(minusQtyItem(cartItem.id));
		}
    }
    const btnClearCart = () => {
		if (cart.length !== 0) {
			dispatch(clearCart());
		}
    }
	const nf = new Intl.NumberFormat();
	return (
		<>
			@@Pos1@@
			{cart.length === 0 ? (
				<div className="text-center py-[50px] my-4">   
					<div className="text-center py-10 mt-20 md:mt-4">
						<h3 className="text-6xl luday_deals">@@EmptyCartMssg@@</h3>
					</div>
					<Link to={ROUTE.PRODUCTS} className="bg-[#9c0] border-[#490] p-2 px-6 font-bold hover:bg-[#98c01d] text-white rounded 
					cursor-pointer">
					<span>@@StartShoppingText@@</span>
					</Link>
				</div>
            ) : (
			<div className="py-2 px-[10px] mt-10 md:px-[60px] lg:px-[90px]">
				@@Pos2@@                   
				<div className="flex flex-col md:flex-row py-[50px]">	
					<div className="w-full md:w-3/4 m-2">
						<div className="overflow-x-auto">
							<table className="w-full whitespace-nowrap">
								<thead className="bg-gray-50" >
									<tr>
										<th className="px-6 py-2 text-left whitespace-nowrap">@@TableHead1@@</th>
										<th className="px-6 py-2">@@TableHead2@@</th>
										<th className="px-6 py-2">@@TableHead3@@</th>
										<th className="px-6 py-2">@@TableHead4@@</th>
									</tr>
								</thead>
								<tbody>
								{cart?.map(cartItem => (  
									<tr key={cartItem.id} className="border border-black-600 whitespace-nowrap">
										<td className="">
											<div className="flex flex-row">
												<div className="bg-white py-2 h-30 w-32">
													<Link to={`${ROUTE.PRODUCT_DETAILS}/${cartItem.slug}`}>
														<img className="h-32 w-32" src={`${CONSTANT.IMAGE_STORE}/${cartItem.image_path}`}/> 
													</Link>
												</div>
												<div className="bg-white py-2">
													<Link to={`${ROUTE.PRODUCT_DETAILS}/${cartItem.slug}`}>
														<h2 className="px-6 text-left text-lg w-[300px] overflow-hidden text-ellipsis md:text-xl">{cartItem.name}</h2>
													</Link>
													<button onClick={() => handleRemoveFromCart(cartItem.id)} 
														className="px-6 py-2 text-left text-sm font-bold text-[#9c0]">@@RemoveItemText@@</button>
												</div>
											</div>
										</td>										
										{cartItem?.sale_price ? (
											<td className="px-6 py-2 text-right">&#8358; {nf.format(cartItem.sale_price)} </td>) 
										: (
											<td className="px-6 py-2 text-right">&#8358; {nf.format(cartItem.price)} </td>
										)}
										{cartItem?.sale_price ? (
											<td className="px-6 py-2 text-right">&#8358;{nf.format(cartItem.sale_price * cartItem.cart_quantity)}</td>) 
										: (
											<td className="px-6 py-2 text-right">&#8358;{nf.format(cartItem.price * cartItem.cart_quantity)}</td>
										)}
										
										<td className="px-6 py-2 text-right">
											<div className="custom-number-input h-10 w-32">
												<div className="flex flex-row h-10 w-full rounded-lg relative bg-transparent mt-1">
													<button onClick={() => btnDecreaseQtyCartList(cartItem)} className="bg-[#98c01d] text-2xl border-[#98c01d] hover:bg-[#88af14] 
														text-white h-full w-32 rounded-l cursor-pointer outline-none"
														disabled={cartItem.cart_quantity === 1}>
													<span className="m-auto text-2xl font-thin">−</span>
													</button>
													<input type="text" value={cartItem.cart_quantity} className="border-[#98c01d] text-center w-full bg-white font-semibold text-md hover:text-black 
														focus:text-black md:text-basecursor-default flex items-center text-gray-700" name="custom-input-number" />
													<button onClick={() => btnIncreaseQtyCartList(cartItem)} className="bg-[#98c01d] text-2xl border-[#88af14] 
														hover:bg-[#9c0] text-white h-full w-32 rounded-r cursor-pointer"
														disabled={cartItem.quantity === cartItem.cart_quantity}>
														<span className="m-auto text-2xl font-thin">+</span>
													</button>
												</div>
											</div>
										</td>										
									</tr>
								))}
								</tbody>
							</table>					
							<div className="cart-summary">
								<button className="button button--theme overflow-hidden [#9c0] font-bold 
									border border-[#98c01d]-600 hover:bg-[#88af14] text-[#98c01d] text-sm transition-all ease-in-out duration-300 
									rounded py-3 px-5 my-2 flex items-center flex-nowrap" 
									onClick={btnClearCart}
									type="button"
									disabled={cart.length === 0}>@@ClearAllItemText@@</button>
							</div>
						</div>
					</div>
					@@Pos3@@
				</div>
			</div>			
			)}
		</>
	);  
}
export default @@PageName@@;
 """
 layouts["layout_cart_1"] = layout_cart_1



 """
 Checkout layout 1
 """
 layout_checkout_1 ="""
import React, { useEffect } from "react";
@@Imports@@
const @@PageName@@ = () => {
    let UpdateCheckoutSchema = Yup.object().shape({
        email: Yup.string()
            .email('Email is not valid.')
            .required('Email is required.'),
        first_name: Yup.string()
            .required('First name is required.')
            .min(2, 'Name should be at least 2 characters.'),
        last_name: Yup.string()
            .required('Last name is required.')
            .min(2, 'Name should be at least 2 characters.'),
        address: Yup.string()
            .required('Billing address is required.'),
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
            .required('City is required.'),
        check_box: Yup.boolean(),
        password: Yup.string().when('check_box', {
                is: true,
                then: (UpdateCheckoutSchema) => 
                    UpdateCheckoutSchema.required('Password is required.')
                        .min(8, 'Password length should be at least 8 characters.')
                        .matches(/[A-Z\W]/g, 'Password should contain at least 1 uppercase letter.')
            }),
        password_confirmation: Yup.string().when('check_box', {
            is: true,
            then: (UpdateCheckoutSchema) => 
                UpdateCheckoutSchema.required('Confirm password is required.')
                .oneOf([Yup.ref('password')], 'Passwords does not match')
            })
    });
  useDocumentTitle('@@DocumentTitle@@');
  const { 
		profile, auth, cart, 
		billing, isOrderLoading, isAuth,
		isOrderStatus
	} = useSelector((store) => ({
		profile: store?.profile,
		isAuth: !!store?.auth?.id && !!store?.auth?.user_type,
		auth: store?.auth,
		billing: store?.checkout?.billing,
		cart: store?.cart,
		isOrderLoading: store?.app?.orderLoading,
		isOrderStatus: store?.app?.orderStatus
	}));

	const dispatch = useDispatch();
	const navigate = useNavigate();

	const subtotal = calculateArrayTotal(
		cart.map((product) => 
			product?.sale_price ? product.sale_price * product.cart_quantity
			: product.price * product.cart_quantity
		)
	);
	useEffect(() => {
        dispatch(setRequestStatus(null));
        if (isOrderStatus?.success && !isOrderStatus?.isError) {
            navigate(ROUTE.PAYMENT);
			dispatch(setOrderStatus(null));
        }
    }, [isOrderStatus]);

	const initFormikValues = {
		first_name: profile.first_name || billing.first_name || '',
		last_name: profile.last_name || billing.last_name || '',
		email: profile.email || billing.email || '',
		address: profile.address || billing.address || '',
		mobile_number: profile.mobile_number || billing.mobile_number || '',
		state: {
			countryCode: '',
			isoCode: '',
			label: '',
			latitude: '',
			longitude: '',
			name: profile.ref_state || billing.state,
			value: profile.ref_state || billing.state
		},
		city: {
			countryCode: '',
			stateCode: '',
			name: profile.ref_local_govt || billing.city || '',
			value: profile.ref_local_govt || billing.city || ''
		},
		check_box: false,
		password: '',
		password_confirmation: ''
	};

	const onSubmitForm = (form, credentials={}) => {
		let status = CONSTANT.ORDER_PAYMENT_PENDING

		dispatch(setBillingDetails({
			first_name: form.first_name,
			last_name: form.last_name,
			email: form.email,
			address: form.address,
			mobile_number: form.mobile_number,
			state: form.state,
			city: form.city,
			isDone: true
		}));

		if(form.check_box) {
			dispatch(signUp({
				first_name: form.first_name.trim(),
				last_name: form.last_name.trim(),
				email: form.email.trim().toLowerCase(),
				password: form.password.trim()
			}));
		}

		if (isAuth) {
			dispatch(updateProfile({
				updates: {
					first_name: form.first_name,
					last_name: form.last_name,
					email: form.email,
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

			dispatch(addOrder({
				guest: {},
				user: {
					first_name: form.first_name,
					last_name: form.last_name,
					ref_transaction_id:  null,
					mobile_number: form.mobile_number,
					amount: subtotal,
					currency:  'NGN',
					tax: 0,
					status: status,
					products: cart
				}
			}));
		} else {
			dispatch(updateProfile({
				updates: {
					first_name: form.first_name,
					last_name: form.last_name,
					email: form.email,
					mobile_number: form.mobile_number
					
				},
				address : {
					address: form.address,
					ref_local_govt: form.city.value,
					ref_state: form.state.value,
					email: form.email
				},
				credentials
			}));

			dispatch(addOrder({
				guest: {
					first_name: form.first_name,
					last_name: form.last_name,
					ref_transaction_id:  null,
					mobile_number: form.mobile_number,
					email: form.email,
					amount: subtotal,
					currency:  'NGN',
					tax: 0,
					status: status,
					products: cart
				},
				user: {}
			}));
		}
	};

	return (
        <>
            <Banner subtitleText="Check out" backgroundImage={img} />
            <div className="py-2 px-[10px] mt-10 md:px-[60px] lg:px-[90px]">
                <Timeline current={2} />
                <Formik
                    initialValues={initFormikValues}
                    validateOnChange
                    validationSchema={UpdateCheckoutSchema}
                    onSubmit={onSubmitForm}
                >
                    {() => (
                        <div className="flex flex-col-reverse md:flex-row py-[50px]">
                            <div className="w-full md:w-2/3 m-2 border border-black-600 drop-shadow-md p-5">
                                <div className="">
                                    <h4 className="mb-2">Billing Details</h4>
                                    <hr/>
                                </div>
                                {!isAuth && (
                                    <div className="mt-3 mb-3 w-auto">
                                        <p>Already have an account? <Link to={ROUTE.SIGNIN} 
                                            className="text-[#9c0]"> Sign in</Link> and you don&apos;t have to fill this </p>
                                    </div>
                                )}
                                <Form>
                                    <BillingForm auth={isAuth} isOrderLoading={isOrderLoading}/>
                                </Form>
                            </div>				
                            <CartSummary />
                        </div>
                    )}
                </Formik>
            </div>
        </>
	);  
}
export default @@PageName@@;
 """
 layouts["layout_checkout_1"] = layout_checkout_1


 """
 Delivery layout 1
 """
 layout_delivery_1 ="""
import React from 'react';
@@Imports@@
const @@PageName@@ = () => {
    useDocumentTitle('@@DocumentTitle@@');
    const cart = useSelector((state) => state.cart);
	const nf = new Intl.NumberFormat();

	return (
        <>
            @@Pos1@@
            <div className="py-2 px-[10px] mt-10 md:px-[60px] lg:px-[90px]">                    
                <div className="flex flex-col-reverse md:flex-row py-[50px]">	
                    <div className="w-full md:w-2/3 m-2 border border-black-600 drop-shadow-md p-5">
                        <div className="">
                            <h4 className="mb-2">@@HeaderText4@@</h4>
                            <hr/>
                        </div>
                        <div className="flex flex-col md:flex-row">
                            <div className="mt-3 mb-3 w-auto md:w-full">
                                <label htmlFor="address">@@Input1Label@@
                                <span className="text-danger">*</span></label>
                                <div className="input-group">
                                    <textarea name="address" type="text" className="w-full text-black shadow-sm bg-white rounded" id="address" placeholder="@@Input1Placeholder@@" rows="3" required/>
                                </div>
                            </div>
                        </div>
                        <div className="flex flex-col md:flex-row justify-between">
                            <div className="mt-3 mb-3 w-auto md:w-[400px]">
                                <label htmlFor="postal">@@Input2Label@@</label>
                                <div className="input-group">
                                    <select name="conutry_id" id="countryid" className="w-full p-2 h-10 text-black shadow-sm bg-white rounded" required>
                                        <option value="">@@SelectInput2Option1@@</option>
                                        <option value="">@@SelectInput2Option2@@</option>
                                    </select>
                                </div>
                            </div>
                            <div className="mt-3 mb-3 w-auto md:w-[400px]">
                                <label htmlFor="postal">@@Input3Label@@
                                <span className="text-danger">*</span></label>
                                <div className="input-group">
                                    <select name="state_id" id="stateid" className="w-full p-2 h-10 text-black shadow-sm bg-white rounded" required>
                                        <option value="">@@SelectInput3Option1@@</option>
                                        <option value="">@@SelectInput3Option2@@</option>
                                    </select>
                                </div>
                            </div>
                        </div>
                        <div className="mt-10 flex flex-col md:flex-row">
                            <Link to={ROUTE.CHECKOUT} className="button button--theme overflow-hidden border border-[#9c0]-600
                            hover:bg-yellow-300 text-[#9c0] text-sm transition-all ease-in-out duration-300 
                            rounded py-3 px-5 m-2 flex items-center flex-nowrap w-full md:w-1/2">
                            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" ><path d="M12.707 17.293 8.414 13H18v-2H8.414l4.293-4.293-1.414-1.414L4.586 12l6.707 6.707z"></path></svg>
                            <span>@@ProceedToPreviousPageText@@</span>
                            </Link>
                            <Link to="/payment" className="button button--theme overflow-hidden bg-[#9c0] 
                            hover:bg-yellow-300 text-white text-sm transition-all ease-in-out duration-300 
                            rounded py-3 px-5 m-2 flex items-center flex-nowrap w-full md:w-1/2">
                            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" className="fill-current mr-2" ><path d="M5 21h14a2 2 0 0 0 2-2V8a1 1 0 0 0-.29-.71l-4-4A1 1 0 0 0 16 3H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2zm10-2H9v-5h6zM13 7h-2V5h2zM5 5h2v4h8V5h.59L19 8.41V19h-2v-5a2 2 0 0 0-2-2H9a2 2 0 0 0-2 2v5H5z"></path></svg>
                            <span>@@SubmitBtnText@@</span>
                            </Link>
                        </div>
                    </div>
                    <div className="w-full md:w-1/4 m-2 border border-black-600 drop-shadow-md p-5 h-1/2">	
                        <h2 className="text-2xl mb-5">@@CartSummarySubHeading2@@</h2>
                        <p>VAT <span>&#8358;0.00</span></p>
                        <p className="mb-5">@@CartSummarySubtoalText@@ <br /><span>&#8358;{nf.format(cart.cartTotalAmount)}</span></p>
                        <hr/>
                        <h2 className="text-2xl mt-5">@@CartSummaryGrandTotalText@@</h2>
                        <h2 className="text-3xl mt-5 font-bold">&#8358;{nf.format(cart.cartTotalAmount + 0.00)}</h2>
                        <div className="mt-4 mx-0">
                            <Link to={ROUTE.CART} className="button button--theme overflow-hidden [#490] border border-[#9c0]-600
                            hover:bg-yellow-300 text-[#490] text-sm transition-all ease-in-out duration-300 
                            rounded py-3 px-5 my-2 flex items-center flex-nowrap">
                            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" ><path d="M12.707 17.293 8.414 13H18v-2H8.414l4.293-4.293-1.414-1.414L4.586 12l6.707 6.707z"></path></svg>
                            <span>@@ProceedToPreviousPageText2@@</span>
                            </Link>
                        </div>
                    </div>
                </div>
            </div>
        </>
    );
}
export default @@PageName@@;
 """
 layouts["layout_delivery_1"] = layout_delivery_1


 """
 Payment layout 1
 """
 layout_payment_1 ="""
import React, { useEffect,useState } from "react";
@@Imports@@

const FormSchema = Yup.object().shape({
	payment_type: Yup.string().required('Please select payment method')
});

const @@PageName@@ = () => {
  useDocumentTitle('@@DocumentTitle@@');
  const state = useSelector((store) => ({
		profile: store?.profile,
		cart: store?.cart,
		isAuth: !!store?.auth?.id && !!store?.auth?.user_type,
		billing: store?.checkout?.billing,
		requestStatus: store?.app.requestStatus,
		isLoading: store?.app?.loading
	}));

	const dispatch = useDispatch();
	const [isPaystackPayment, setPaystackPayment] = useState(false);

	useEffect(() => {
		dispatch(setRequestStatus(null));
	}, []);

	if (state.requestStatus) {
		return <Navigate to={ROUTE.CASH_ORDER_CALLBACK} />;
	}
	if (!state.billing || !state.billing.isDone) {
		return <Navigate to={ROUTE.CHECKOUT} />;
	}
	if (!isPaystackPayment && state.cart.length === 0) {
		return<Navigate to={ROUTE.PRODUCTS} />;
	}

	const initFormikValues = {
		payment_type: state.billing.type || 'paystack'
	};

	const onConfirm = (form) => {
		if (form.payment_type == 'cash') {
			dispatch(updateOrder({
				order: {
					first_name: state.billing.first_name,
					last_name: state.billing.last_name,
					ref_transaction_id:  state.billing.ref_transaction_id,
					ref_id: state.billing.ref_id,
					mobile_number: state.billing.mobile_number,
					amount: state.billing.amount,
					tax: state.billing.tax,
					status: state.billing.status,
					billing_address_id: state.profile.ref_address_id
				},
				type: 'cash'
			}));
			dispatch(setPaymentDetails({
				type: 'cash',
				name: state.billing.first_name+ ' ' +state.billing.last_name
			}))
		}
		if (form.payment_type == 'paystack') {
			setPaystackPayment(true);
			dispatch(updateOrder({
				order: {
					first_name: state.billing.first_name,
					last_name: state.billing.last_name,
					ref_transaction_id:  state.billing.ref_transaction_id,
					ref_id: state.billing.ref_id,
					mobile_number: state.billing.mobile_number,
					amount: state.billing.amount,
					tax: state.billing.tax,
					status: state.billing.status,
					billing_address_id: state.profile.ref_address_id
				},
				user: {},
				type: 'paystack'
			}));
			dispatch(setPaymentDetails({
				type: 'paystack',
				name: state.billing.first_name+ ' ' +state.billing.last_name
			}))
		}
	};

	return (
	<>
        @@Pos1@@
		<div className="py-2 px-[10px] mt-10 md:px-[60px] lg:px-[90px]">  
			@@Pos2@@
			<Formik
				initialValues={initFormikValues}
				validateOnChange
				validationSchema={FormSchema}
				onSubmit={onConfirm}
			>
				{() => (
					<Form>          
						<div className="flex flex-col-reverse md:flex-row py-[50px]">	
							<div className="w-full md:w-2/3 m-2 border border-black-600 drop-shadow-md p-5">
								<div>
									<h4 className="mb-2" >Payment Method</h4>
									<hr/>
								</div>
                                @@Pos3@@
							</div>
                            @@Pos4@@
						</div>
					</Form> 
				)}
			</Formik>
		</div>
	</>
  );
}
export default @@PageName@@;
 """
 layouts["layout_payment_1"] = layout_payment_1


 """
 Sign-in layout 1
 """
 layout_sign_in_1 ="""
import React, { useEffect } from 'react';
@@Imports@@

const SignInSchema = Yup.object().shape({
    email: Yup.string()
      .email('Email is not valid.')
      .required('Email is required.'),
    password: Yup.string()
      .required('Password is required.')
});

const @@PageName@@ = () => {
    const { isAuthenticating } = useSelector((state) => ({
        isAuthenticating: state.app.isAuthenticating
    }));
  
    const dispatch = useDispatch();
    
	useDocumentTitle('@@DocumentTitle@@');
    useScrollTop();

    useEffect(() => {
        dispatch(setAuthStatus(null));
        dispatch(setAuthenticating(false));
    }, []);

    const onFormSubmit = (form) => {
        dispatch(signIn(form.email, form.password));
    };

    const onClickLink = (e) => {
        if (isAuthenticating) e.preventDefault();
    };

	return (
		<>
            <div className='pt-20 md:pt-32 bg-gray-50'>
            <div className="flex flex-col items-center min-h-screen sm:justify-center sm:pt-0">
                <div>
                    <a href={ROUTES.HOME}>
                        <h1 className="text-4xl font-bold text-[#9c0]">
                            @@SubHeading3@@
                        </h1>
                    </a>
                </div>
                <Formik
                    initialValues={{
                    email: '',
                    password: ''
                    }}
                    validateOnChange
                    validationSchema={SignInSchema}
                    onSubmit={onFormSubmit}
                >
                    <div className="w-full px-6 py-4 my-6 overflow-hidden bg-white shadow-md sm:max-w-lg sm:rounded-lg">
                        <Form>
                            <div>
                                <Field
                                    disabled={isAuthenticating}
                                    id="email" 
                                    name="email"
                                    placeholder="@@Input1Placeholder@@"
                                    type="email"
                                    label="@@Input1Label1@@"
                                    component={CustomInput}
                                />
                            </div>
                            <div className="mt-4">
                                <Field
                                    disabled={isAuthenticating}
                                    id="password" 
                                    name="password"
                                    placeholder="@@Input2Placeholder@@"
                                    type="password"
                                    label="@@Input2Label2@@"
                                    component={CustomInput}
                                />
                            </div>
                            <div className="mt-2">
                            <Link
                                onClick={onClickLink}
                                className="text-xs text-green-600 hover:underline"
                                to={ROUTES.FORGOT_PASSWORD}
                                >
                                <span>@@SpanText1@@</span>
                            </Link>
                            </div>
                            <div className="flex items-center mt-4">
                                <button 
                                    disabled={isAuthenticating}
                                    type="submit"
                                    className="w-full px-4 py-2 tracking-wide text-white transition-colors duration-200 transform bg-primary rounded-md hover:bg-secondary focus:outline-none focus:bg-green-600">
                                    {isAuthenticating ? '@@SubmitBtnOnLoadingText@@' : '@@SubmitBtnText@@'}
                                </button>
                            </div>
                        </Form>
                        <div className="mt-4 text-grey-600">
                            @@SpanText2@@
                            <Link to={SIGNUP} 
                                className="text-primary hover:underline"
                                disabled={isAuthenticating}>
                                <span>
                                    @@SpanText3@@
                                </span>
                            </Link>
                        </div>
                        {/* <div className="flex items-center w-full my-4">
                            <hr className="w-full" />
                            <p className="px-3 ">@@SpanText4@@</p>
                            <hr className="w-full" />
                        </div>
                        <div className="my-6 space-y-2">
                            <button
                                aria-label="Login with Google"
                                type="button"
                                className="flex items-center justify-center w-full p-2 space-x-4 border rounded-full focus:ring-2 focus:ring-offset-1 dark:border-gray-400 focus:ring-green-600"
                            >
                                @@SignInOptionIcon1@@
                                <p>@@SignInOptionText1@@</p>
                            </button>
                            <button
                                aria-label="Login with GitHub"
                                role="button"
                                className="flex items-center justify-center w-full p-2 space-x-4 border rounded-full focus:ring-2 focus:ring-offset-1 dark:border-gray-400 focus:ring-green-600"
                            >
                                @@SignInOptionIcon2@@
                                <p>@@SignInOptionText2@@</p>
                            </button>
                        </div>  */}
                    </div>
                </Formik>
            </div>
        </div>
		</>
	);
}
export default @@PageName@@;
 """
 layouts["layout_sign_in_1"] = layout_sign_in_1


 """
 Sign Up layout 1
 """
 layout_sign_up_1 ="""
import React, { useEffect } from 'react';
@@Imports@@

const SignUpSchema = Yup.object().shape({
    email: Yup.string()
      .email('Email is not valid.')
      .required('Email is required.'),
    password: Yup.string()
      .required('Password is required.')
      .min(8, 'Password length should be at least 8 characters.')
      .matches(/[A-Z\W]/g, 'Password should contain at least 1 uppercase letter.'),
    password_confirmation: Yup.string()
      .required('Confirm password is required.')
      .oneOf([Yup.ref('password')], 'Passwords does not match'),
    first_name: Yup.string()
      .required('First name is required.')
      .min(2, 'Name should be at least 2 characters.'),
    last_name: Yup.string()
      .required('Last name is required.')
      .min(2, 'Name should be at least 2 characters.'),
    gender: Yup.string()
      .required('Gender is required.')
});

const @@PageName@@ = () => {
    const { isAuthenticating } = useSelector((state) => ({
        isAuthenticating: state.app.isAuthenticating
    }));

    const dispatch = useDispatch();

	useDocumentTitle('@@DocumentTitle@@');
    useScrollTop();

    useEffect(() => {
        dispatch(setAuthStatus(null));
        dispatch(setAuthenticating(false));
    }, []);

    const onFormSubmit = (form) => {
        dispatch(signUp({
            first_name: form.first_name.trim(),
            last_name: form.last_name.trim(),
            email: form.email.trim().toLowerCase(),
            password: form.password.trim(),
            gender: form.gender.trim(),
            is_active: true
        }));
    };

	return (
		<>
            <div className='pt-20 bg-gray-50'>
            <div className="flex flex-col items-center min-h-screen sm:justify-center sm:pt-0">
                <div>
                    <h1 className="text-4xl font-bold text-[#9c0]">
                        @@SubHeading3@@
                    </h1>
                </div>
                <Formik
                    initialValues={{
                        first_name: '',
                        last_name: '',
                        email: '',
                        password: '',
                        gender: ''
                    }}
                    validateOnChange
                    validationSchema={SignUpSchema}
                    onSubmit={onFormSubmit}
                >
                    <div className="w-full px-6 py-4 my-6 overflow-hidden bg-white shadow-md sm:max-w-lg sm:rounded-lg">
                        <Form>
                            <div>
                                <Field
                                    disabled={isAuthenticating}
                                    id="first-name" 
                                    name="first_name"
                                    placeholder="@@Input1Placeholder@@"
                                    style={{ textTransform: 'capitalize' }}
                                    type="text"
                                    label="@@Input1Label@@"
                                    component={CustomInput}
                                />
                            </div>
                            <div className="mt-4">
                                <Field
                                    disabled={isAuthenticating}
                                    id="last-name" 
                                    name="last_name"
                                    placeholder="@@Input2Placeholder@@"
                                    style={{ textTransform: 'capitalize' }}
                                    type="text"
                                    label="@@Input2Label@@"
                                    component={CustomInput}
                                />
                            </div>
                            <div className="mt-4">
                                <Field
                                    disabled={isAuthenticating}
                                    id="email" 
                                    name="email"
                                    placeholder="@@Input3Placeholder@@"
                                    type="email"
                                    label="@@Input3Label@@"
                                    component={CustomInput}
                                />
                            </div>
                            <div className="mt-4">
                                <Field
                                    disabled={isAuthenticating}
                                    id="password" 
                                    name="password"
                                    placeholder="@@Input4Placeholder@@"
                                    type="password"
                                    label="@@Input4Label@@"
                                    component={CustomInput}
                                />
                            </div>
                            <div className="mt-4">
                                <Field
                                    disabled={isAuthenticating}
                                    id="password-confirmation" 
                                    name="password_confirmation"
                                    placeholder="@@Input5Placeholder@@"
                                    type="password"
                                    label="@@Input5Label@@"
                                    component={CustomInput}
                                />
                            </div>
                            <div className="mt-4">
                                <label className="block text-sm font-medium text-gray-700 undefined" htmlFor="gender">
                                    {"@@Radio1SpanText@@"}
                                </label>
                                {/* TODO: map gender from constant class */}
                                <div role="group" aria-labelledby="my-radio-group">
                                    <span className="mr-4">
                                        <Field className="mr-2" 
                                            type="radio"
                                            id="gender"
                                            name="gender" 
                                            value="male" 
                                        />
                                        @@Radio1Option2@@
                                    </span>
                                    <span>
                                        <Field className="mr-2" 
                                            type="radio" 
                                            id="gender"
                                            name="gender" 
                                            value="female"
                                        />
                                        @@Radio1Option2@@
                                    </span>
                                </div>
                            </div>
                            <div className="flex items-center mt-4">
                                <button 
                                    disabled={isAuthenticating}
                                    type="submit"
                                    className="w-full px-4 py-2 tracking-wide text-white transition-colors duration-200 transform bg-primary rounded-md hover:bg-secondary focus:outline-none focus:bg-green-600">
                                    {isAuthenticating ? '@@SubmitBtnOnLoadingText@@' : '@@SubmitBtnText@@'}
                                </button>
                            </div>
                        </Form>
                        <div className="mt-4 text-grey-600">
                            @@SpanText2@@{" "}
                            <Link to={SIGNIN} 
                                className="text-primary hover:underline"
                                disabled={isAuthenticating}>
                                <span>
                                    @@SpanText3@@
                                </span>
                            </Link>
                        </div>
                        {/* <div className="flex items-center w-full my-4">
                            <hr className="w-full" />
                            <p className="px-3 ">@@SpanText4@@</p>
                            <hr className="w-full" />
                        </div>
                        <div className="my-6 space-y-2">
                            <button
                                aria-label="Login with Google"
                                type="button"
                                className="flex items-center justify-center w-full p-2 space-x-4 border rounded-full focus:ring-2 focus:ring-offset-1 dark:border-gray-400 focus:ring-green-600"
                            >
                                @@SignInOptionIcon1@@
                                <p>@@SignUpOptionText1@@</p>
                            </button>
                            <button
                                aria-label="Login with GitHub"
                                role="button"
                                className="flex items-center justify-center w-full p-2 space-x-4 border rounded-full focus:ring-2 focus:ring-offset-1 dark:border-gray-400 focus:ring-green-600"
                            >
                                @@SignInOptionIcon2@@
                                <p>@@SignUpOptionText2@@</p>
                            </button>
                        </div> */}
                    </div>
                </Formik>
            </div>
        </div>
		</>
	);
  
}
export default @@PageName@@;
 """
 layouts["layout_sign_up_1"] = layout_sign_up_1


 """
 Sign Up vendor layout 1
 """
 layout_sign_up_vendor_1 ="""
import React, { useEffect } from 'react';
@@Imports@@

const SignUpVendorSchema = Yup.object().shape({
    email: Yup.string()
      .email('Email is not valid.')
      .required('Email is required.'),
    password: Yup.string()
      .required('Password is required.')
      .min(8, 'Password length should be at least 8 characters.')
      .matches(/[A-Z\W]/g, 'Password should contain at least 1 uppercase letter.'),
    password_confirmation: Yup.string()
      .required('Confirm password is required.')
      .oneOf([Yup.ref('password')], 'Passwords does not match'),
    first_name: Yup.string()
      .required('First name is required.')
      .min(2, 'Name should be at least 2 characters.'),
    last_name: Yup.string()
      .required('Last name is required.')
      .min(2, 'Name should be at least 2 characters.'),
    gender: Yup.string()
      .required('Gender is required.')
});

const @@PageName@@ = () => {
    const { isAuthenticating, authStatus } = useSelector((state) => ({
        isAuthenticating: state.app.isAuthenticating,
        authStatus: state.app.authStatus
    }));

    const dispatch = useDispatch();
    let navigate = useNavigate();
    
	useDocumentTitle('@@DocumentTitle@@');
	useScrollTop();

    useEffect(() => {
        dispatch(setAuthStatus(null));
        dispatch(setAuthenticating(false));
    }, []);

    const onClickSignIn = () => navigate(SIGNIN);

    const onFormSubmit = (form) => {
        dispatch(signUpVendor({
            first_name: form.first_name.trim(),
            last_name: form.last_name.trim(),
            email: form.email.trim().toLowerCase(),
            password: form.password.trim(),
            gender: form.gender.trim(),
            is_active: false
        }));
    };

	return (
		<>
            <Navigation/>
            {authStatus?.message && (
                <nav className='fixed z-20 w-full top-0 bg-white border-gray-200'>
                    <Alert
                        status={authStatus.status}
                        mssg={authStatus.message}
                        type={authStatus.type}
                    />
                </nav>
            )}
			<div className='pt-20 bg-gray-50'>
                <div className="flex flex-col items-center min-h-screen sm:justify-center sm:pt-0">
                    <div>
                        <h1 className="text-4xl font-bold text-[#9c0]">
                            @@SubHeading3@@
                        </h1>
                    </div>
                    <Formik
                        initialValues={{
                            first_name: '',
                            last_name: '',
                            email: '',
                            password: '',
                            gender: ''
                        }}
                        validateOnChange
                        validationSchema={SignUpVendorSchema}
                        onSubmit={onFormSubmit}
                    >
                        <div className="w-full px-6 py-4 my-6 overflow-hidden bg-white shadow-md sm:max-w-lg sm:rounded-lg">
                            <Form>
                                <div>
                                    <Field
                                        disabled={isAuthenticating}
                                        id="first-name" 
                                        name="first_name"
                                        placeholder="@@Input1Placeholder@@"
                                        style={{ textTransform: 'capitalize' }}
                                        type="text"
                                        label="@@Input1Label@@"
                                        component={CustomInput}
                                    />
                                </div>
                                <div className="mt-4">
                                    <Field
                                        disabled={isAuthenticating}
                                        id="last-name" 
                                        name="last_name"
                                        placeholder="@@Input2Placeholder@@"
                                        style={{ textTransform: 'capitalize' }}
                                        type="text"
                                        label="@@Input2Label@@"
                                        component={CustomInput}
                                    />
                                </div>
                                <div className="mt-4">
                                    <Field
                                        disabled={isAuthenticating}
                                        id="email" 
                                        name="email"
                                        placeholder="@@Input3Placeholder@@"
                                        type="email"
                                        label="@@Input3Label@@"
                                        component={CustomInput}
                                    />
                                </div>
                                <div className="mt-4">
                                    <Field
                                        disabled={isAuthenticating}
                                        id="password" 
                                        name="password"
                                        placeholder="@@Input4Placeholder@@"
                                        type="password"
                                        label="@@Input4Label@@"
                                        component={CustomInput}
                                    />
                                </div>
                                <div className="mt-4">
                                    <Field
                                        disabled={isAuthenticating}
                                        id="password-confirmation" 
                                        name="password_confirmation"
                                        placeholder="@@Input5Placeholder@@"
                                        type="password"
                                        label="@@Input5Label@@"
                                        component={CustomInput}
                                    />
                                </div>
                                <div className="mt-4">
                                    <label className="block text-sm font-medium text-gray-700 undefined" htmlFor="gender">
                                        {"@@Radio1SpanText@@"}
                                    </label>
                                    {/* TODO: map gender from constant class */}
                                    <div role="group" aria-labelledby="my-radio-group">
                                        <span className="mr-4">
                                            <Field className="mr-2" 
                                                type="radio"
                                                id="gender"
                                                name="gender" 
                                                value="male" 
                                            />
                                            @@Radio1Option1@@
                                        </span>
                                        <span>
                                            <Field className="mr-2" 
                                                type="radio" 
                                                id="gender"
                                                name="gender" 
                                                value="female"
                                            />
                                            @@Radio1Option2@@
                                        </span>
                                    </div>
                                </div>
                                <div className="flex items-center mt-4">
                                    <button 
                                        disabled={isAuthenticating}
                                        type="submit"
                                        className="w-full px-4 py-2 tracking-wide text-white transition-colors duration-200 transform bg-[#9c0] rounded-md hover:bg-[#84b000] focus:outline-none focus:bg-green-600">
                                        {isAuthenticating ? '@@SubmitBtnOnLoadingText@@' : '@@SubmitBtnText@@'}
                                    </button>
                                </div>
                            </Form>
                            <div className="mt-4 text-grey-600">
                                @@SpanText2@@{" "}
                                <span>
                                    <a className="text-[#9c0] hover:underline" 
                                        disabled={isAuthenticating}
                                        onClick={onClickSignIn}
                                    >
                                        @@SpanText3@@
                                    </a>
                                </span>
                            </div>
                            {/* <div className="flex items-center w-full my-4">
                                <hr className="w-full" />
                                <p className="px-3 ">@@SpanText4@@</p>
                                <hr className="w-full" />
                            </div>
                            <div className="my-6 space-y-2">
                                <button
                                    aria-label="Login with Google"
                                    type="button"
                                    className="flex items-center justify-center w-full p-2 space-x-4 border rounded-full focus:ring-2 focus:ring-offset-1 dark:border-gray-400 focus:ring-green-600"
                                >
                                    @@SignInOptionIcon1@@
                                    <p>@@SignUpOptionText1@@</p>
                                </button>
                                <button
                                    aria-label="Login with GitHub"
                                    role="button"
                                    className="flex items-center justify-center w-full p-2 space-x-4 border rounded-full focus:ring-2 focus:ring-offset-1 dark:border-gray-400 focus:ring-green-600"
                                >
                                    @@SignInOptionIcon2@@
                                    <p>@@SignUpOptionText2@@</p>
                                </button>
                            </div> */}
                        </div>
                    </Formik>
                </div>
            </div>
		</>
	);
}
export default @@PageName@@;
 """
 layouts["layout_sign_up_vendor_1"] = layout_sign_up_vendor_1


 """
 
 """
 layout_sign_up_vendor_details_1 ="""
import React, { useEffect } from 'react';
@@Imports@@

const SignUpVendorDetailsSchema = Yup.object().shape({
    bank_name: Yup.object()
		.shape({
			label: Yup.string(),
			value: Yup.string().required('State is required.')
		})
		.required('Bank name is required.'),
    bank_acct_number: Yup.string()
        .required('Bank account number is required.')
        .min(10, 'Number should be at least 10 characters.'),
    bank_account_name: Yup.string()
        .required('Bank account name is required.')
        .min(10, 'Number should be at least 10 characters.'),
    title: Yup.string()
        .required('Business title is required.'),
	address: Yup.string()
        .required('Address is required.'),
    description: Yup.string()
        .required('Business description is required.'),
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
  const { profile, auth, authStatus, isAuthenticating } = useSelector((state) => ({
        profile: state.profile,
        auth: state.auth,
        authStatus: state.app.authStatus,
        isAuthenticating: state.app.isAuthenticating
    }));
    const dispatch = useDispatch();
    let navigate = useNavigate();
    
    useDocumentTitle('@@DocumentTitle@@');
    useScrollTop();

    useEffect(() => {
        dispatch(setAuthStatus(null));
        dispatch(setAuthenticating(false));
        
        if (authStatus?.message == "Successfully signed details.") navigate('/vendor/signup/complete')
    }, [authStatus]);

    const initFormikValues = {
        bank_name: profile.bank_name || {},
        bank_acct_number: profile.bank_acct_number || '',
        bank_account_name: profile.bank_account_name || '',
        mobile_number: profile.mobile_number || '',
        address: profile.address || '',
        title: profile.title || '',
        description: profile.description || '',
        state: {
			countryCode: '',
			isoCode: '',
			label: '',
			latitude: '',
			longitude: '',
			name: profile.ref_state || '',
			value: profile.ref_state || ''
		},
		city: {
			countryCode: '',
			stateCode: '',
			name: profile.ref_local_govt || '',
			value: profile.ref_local_govt || ''
		}
	};

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

	const banks = Banks.getAllBanks();
	const updatedBanks = banks.map((bank) => ({
		label: bank.label,
		value: bank.value
	}));

    const {
		imageFile,
		onFileChange
	} = useFileHandler({ display_pics: {} });
    
    const onFormSubmit = (form) => {
        if (imageFile.display_pics.file) {
            let formData = new FormData();

            formData.set('business_bank_name', form.bank_name.label)
            formData.set('business_bank_name_value', form.bank_name.value)
            formData.set('business_account_no', form.bank_acct_number)
            formData.set('business_account_name', form.bank_account_name)
            formData.set('business_address', form.address)
            formData.set('business_city', form.city.value)
            formData.set('business_state', form.state.value)
            formData.set('business_state_value', form.state.isoCode)
            formData.set('name', form.title)
            formData.set('business_description', form.description)
            formData.set('image_file', imageFile.display_pics.file)
            formData.set('user_id', auth.id)

            dispatch(SignUpVendorDetails(formData));
        } else {
            // eslint-disable-next-line no-alert
            alert('Business image is required.');
        }
    };

	return (
		<>
			<div className='pt-20 md:pt-32 py-2 px-[10px] md:px-[60px] lg:px-[90px]'>
                <Formik
                    initialValues={initFormikValues}
                    validateOnChange
                    validationSchema={SignUpVendorDetailsSchema}
                    onSubmit={onFormSubmit}
                >
                    {({values}) => (
                        <div className="flex flex-col items-center min-h-screen sm:justify-center sm:pt-0">
                            <div className="">
                                <a href={ROUTES.HOME}>
                                    <h3 className="text-4xl font-bold text-[#9c0]">
                                        Vendor Details
                                    </h3>
                                </a>
                            </div>
                            <div className="w-full md:w-2/3 m-2 border border-black-600 drop-shadow-md p-5">
                                <Form encType="multipart/form-data">
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
                                    <div className="flex flex-col md:flex-row justify-between">
                                        <div className="mt-3 mb-3 w-auto md:w-3/5 md:mr-3">
                                            @@InputComponent8@@
                                        </div>
                                        <div className="mt-3 mb-3 w-auto md:w-3/5 md:mr-3">
                                            @@InputComponent9@@
                                        </div>
                                    </div>
                                    <div className="flex flex-col md:flex-row justify-between">
                                        <div className="mt-3 mb-3 w-auto md:w-full">
                                            @@InputComponent10@@
                                        </div>
                                    </div>
                                    <div className="mt-10 flex justify-center">
                                        <button 
                                            disabled={isAuthenticating} 
                                            className="button button--theme overflow-hidden bg-primary hover:bg-secondary text-white text-sm transition-all ease-in-out duration-300 rounded py-3 px-5 m-2 flex items-center flex-nowrap w-80 justify-center"
                                            type="submit"
                                        >
                                            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" className="fill-current mr-2" ><path d="M5 21h14a2 2 0 0 0 2-2V8a1 1 0 0 0-.29-.71l-4-4A1 1 0 0 0 16 3H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2zm10-2H9v-5h6zM13 7h-2V5h2zM5 5h2v4h8V5h.59L19 8.41V19h-2v-5a2 2 0 0 0-2-2H9a2 2 0 0 0-2 2v5H5z"></path></svg>
                                            <span>{isAuthenticating ? '@@SubmitBtnOnLoadingText@@' : '@@SubmitBtnText@@'}</span>
                                        </button>
                                    </div>
                                </Form>
                            </div>				
                        </div>
                    )}
                </Formik>
            </div>
		</>
	);
}
export default @@PageName@@;
 """
 layouts["layout_sign_up_vendor_details_1"] = layout_sign_up_vendor_details_1


 """
 Forgot password layout 1
 """
 layout_forgot_password_1 ="""
import React, { useEffect, useState } from 'react';
@@Imports@@

const ForgotPasswordSchema = Yup.object().shape({
    email: Yup.string()
      .email('Email is not valid.')
      .required('Email is required.')
});

const @@PageName@@ = () => {
    useDocumentTitle('@@DocumentTitle@@');
    useScrollTop();

    const { authStatus, isAuthenticating } = useSelector((state) => ({
        isAuthenticating: state.app.isAuthenticating,
        authStatus: state.app.authStatus
    }));
    const dispatch = useDispatch();
    const didMount = useDidMount();

    const [forgotPasswordStatus, setForgotPasswordStatus] = useState({});

    useEffect(() => () => {
		if (didMount) {
            setForgotPasswordStatus(authStatus);
        }
	}, [authStatus, isAuthenticating]);

    const onFormSubmit = (form) => {
        dispatch(forgotPassword(form.email));
    };

	return (
		<>
            {forgotPasswordStatus?.message && (
                <nav className='fixed z-20 w-full top-0 bg-white border-gray-200'>
                    <Alert
                        status={authStatus.status}
                        mssg={authStatus.message}
                        type={authStatus.type}
                    />
                </nav>
            )}
			<div className='pt-20 md:pt-2 lg:pt-2 bg-gray-50'>
            <div className="flex flex-col items-center min-h-screen sm:justify-center sm:pt-0">
                <div>
                    <h1 className="text-4xl font-bold text-[#9c0]">
                        @@SubHeading1@@
                    </h1>
                </div>
                <Formik
                    initialValues={{
                        email: ''
                    }}
                    validateOnChange
                    validationSchema={ForgotPasswordSchema}
                    onSubmit={onFormSubmit}
                >
                    <div className="w-full px-6 py-4 my-6 overflow-hidden bg-white shadow-md sm:max-w-lg sm:rounded-lg">
                        <Form>
                            <div>
                                <Field
                                    id="email" 
                                    name="email"
                                    placeholder="@@Input1Placeholder@@"
                                    type="email"
                                    label="@@Input1Label1@@"
                                    maxLength={40}
                                    component={CustomInput}
                                     readOnly={isAuthenticating}
                                />
                            </div>
                            
                            <div className="mt-5">
                            <Link className=" text-xs text-primary hover:underline" to={ROUTES.SIGNIN}>
                                <span className='flex flex-row items-center text-base'><FaArrowLeft/>@@LinkToLogin@@</span>
                            </Link>
                            </div>
                            <div className="flex items-center mt-4">
                                <button 
                                    type="submit"
                                    disabled={isAuthenticating}
                                    className="w-full px-4 py-2 tracking-wide text-white transition-colors duration-200 transform bg-primary rounded-md hover:bg-secondary focus:outline-none focus:bg-green-600">
                                    {isAuthenticating ? <LoadingOutlined /> : <CheckOutlined />}
                                    &nbsp;
                                    {isAuthenticating ? '@@SubmitBtnOnLoadingText@@' : '@@SubmitBtnText@@'}
                                </button>
                            </div>
                        </Form>
                        <div className="mt-4 text-grey-600">
                            @@SpanText1@@{" "}
                            <Link to={ROUTES.SIGNUP} 
                                className="text-primary hover:underline"
                                disabled={isAuthenticating || authStatus?.success}>
                                <span>
                                    @@SpanText2@@
                                </span>
                            </Link>
                        </div>
                    </div>
                </Formik>
            </div>
        </div>
		</>
	);
}
export default @@PageName@@;
 """
 layouts["layout_forgot_password_1"] = layout_forgot_password_1


 """
 Reset password layout 1
 """
 layout_reset_password_1 ="""
import React, { useEffect } from 'react';
@@Imports@@

const ResetPasswordSchema = Yup.object().shape({
    new_password: Yup.string()
      .required('Password is required.')
      .min(8, 'Password length should be at least 8 characters.')
      .matches(/[A-Z\W]/g, 'Password should contain at least 1 uppercase letter.'),
    password_confirmation: Yup.string()
      .required('Confirm password is required.')
      .oneOf([Yup.ref('new_password')], 'Passwords does not match')
});

const @@PageName@@ = () => {
  const { token } = useParams();
    const { isAuthenticating } = useSelector((state) => ({
        isAuthenticating: state.app.isAuthenticating
    }));
    const dispatch = useDispatch();
    
	useDocumentTitle('@@DocumentTitle@@');
	useScrollTop();

    useEffect(() => () => {
		dispatch(setLoading(false));
	}, []);
    const onFormSubmit = (form) => {
        dispatch(resetPassword({
            token: token,
            new_password: form.new_password}));
    };

	return (
		<>
            <div className='pt-20 md:pt-2 bg-gray-50'>
            <div className="flex flex-col items-center min-h-screen sm:justify-center sm:pt-0">
                <div>
                    <h1 className="text-4xl font-bold text-[#9c0]">
                        @@SubHeading1@@
                    </h1>
                </div>
                <Formik
                    initialValues={{
                        new_password: ''
                    }}
                    validateOnChange
                    validationSchema={ResetPasswordSchema}
                    onSubmit={onFormSubmit}
                >
                    <div className="w-full px-6 py-4 my-6 overflow-hidden bg-white shadow-md sm:max-w-lg sm:rounded-lg">
                        <Form>
                        <div className="mt-4">
                                <Field
                                    disabled={isAuthenticating}
                                    id="new_password" 
                                    name="new_password"
                                    placeholder="@@Input1Placeholder@@"
                                    type="password"
                                    label="@@Input1Label1@@"
                                    component={CustomInput}
                                />
                            </div>
                            <div className="mt-4">
                                <Field
                                    disabled={isAuthenticating}
                                    id="password-confirmation" 
                                    name="password_confirmation"
                                    placeholder="@@Input2Placeholder@@"
                                    type="password"
                                    label="@@Input1Label2@@"
                                    component={CustomInput}
                                />
                            </div>
                            <div className="flex items-center mt-4">
                                <button 
                                    type="submit"
                                    className="w-full px-4 py-2 tracking-wide text-white transition-colors duration-200 transform bg-primary rounded-md hover:bg-secondary focus:outline-none focus:bg-green-600">
                                    {isAuthenticating ? <LoadingOutlined /> : ''}
                                    &nbsp;
                                    {isAuthenticating ? '@@SubmitBtnOnLoadingText@@' : '@@SubmitBtnText@@'}
                                </button>
                            </div>
                        </Form>
                    </div>
                </Formik>
            </div>
        </div>
		</>
	);
}
export default @@PageName@@;
 """
 layouts["layout_reset_password_1"] = layout_reset_password_1


 """
 Sign Up complete layout 1
 """
 layout_sign_up_complete_1 ="""
import React from 'react';
@@Imports@@
const @@PageName@@ = () => {
    useDocumentTitle('@@DocumentTitle@@');
    useScrollTop();

    return (
        <>
        <div className='flex py-2 px-[10px] md:px-[60px] lg:px-[90px] h-screen'>
                <div className='rounded-md mx-auto my-auto shadow-md p-8 items-center justify-center'>
                    <div className='appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d] cursor-not-allowed items-center justify-center'>
                        <h2 className="text-center text-4xl uppercase font-bold text-[#98c01d]">@@SubHeading2@@</h2>
                        <p className='text-center'>@@paragraph1@@</p>
                    </div>  
                    <a href="/" className=" mt-8 mx-auto appearance-none w-full md:w-1/3  block bg-gray-700 text-gray-100 font-bold border border-gray-200 rounded-lg py-3 px-3 leading-tight hover:bg-gray-600 focus:outline-none focus:bg-white focus:border-gray-500 text-center">@@ProceedToHomePageText@@</a>
                </div>
            </div>
        </>
    )
}
export default @@PageName@@;
 """
 layouts["layout_sign_up_complete_1"] = layout_sign_up_complete_1


 """
 
 """
 layout_profile_1 ="""
import React, { Suspense } from 'react';
@@Imports@@

const AccountProfile = React.lazy(() => import('./components/AccountProfile'));

const @@PageName@@ = () => {
    useDocumentTitle('@@DocumentTitle@@');

    return (
		<div>
			<Suspense fallback={(
				<div className="loader" style={{ minHeight: '80vh' }}>
					<h6>@@LoadingPageText@@</h6>
					<br />
					<LoadingOutlined />
				</div>
			)}>
				<AccountProfile />
			</Suspense>
		</div>
	);
}
export default @@PageName@@;
 """
 layouts["layout_profile_1"] = layout_profile_1


 """
 User order history layout
 """
 layout_user_order_history_1 ="""
import React from 'react';
@@Imports@@
const @@PageName@@ = () => {
    useDocumentTitle('@@DocumentTitle@@');
    const { token, isLoading } = useSelector((state) => ({
		token: state.profile.access_token,
		isLoading: state.app.loading
	}));

    const { orders } = useOrders(token, isLoading);
 
	return (
		<>
			@@Pos1@@
			<div className="py-2 px-[10px] mt-10 md:px-[60px] lg:px-[90px]">                    
				<div className="flex flex-col md:flex-row py-[50px]">
					<div className="w-full md:w-1/3 m-2 border border-black-600 drop-shadow-md p-5 h-1/2">
					@@Pos2@@
					</div>
					<div className="w-full md:w-2/3 m-2 border border-black-600 drop-shadow-md p-5">
						<div className="overflow-x-auto">
							
							<table className="divide-y divide-gray-300 w-full">
								<thead className="bg-gray-50" >
									<tr>
										<th className="px-6 py-2 text-left whitespace-nowrap">@@TableHead1@@</th>
										<th className="px-6 py-2 text-center">@@TableHead2@@</th>
										<th className="px-6 py-2 text-center">@@TableHead3@@</th>
										<th className="px-6 py-2 text-center">@@TableHead4@@</th>
										<th className="px-6 py-2 text-left">@@TableHead5@@</th>
										<th className="px-6 py-2 text-right">@@TableHead6@@</th>
									</tr>
								</thead>
								{orders.length > 0 ?
								<tbody>
									{orders?.map((order) => (
										<>
											<tr className="border border-black-600 whitespace-nowrap">
												@@Pos3@@
                                            </tr>
										</>
									))}
								</tbody>
								:
								<tbody>
									<tr className="border border-black-600 text-center">
										<td className="items-cente p-3 w-[200px]" colSpan={4}>
											<p className="text-lg">{isLoading ? '@@OnScreenLoadingText@@' : '@@EmptyRecordMssg@@'}</p>
										</td>
									</tr>
								</tbody>
								}
							</table>
						</div>
					</div>
				</div>
			</div>
		</>
	);  
}
export default @@PageName@@;
 """
 layouts["layout_user_order_history_1"] = layout_user_order_history_1


 """
 User order details layout 1
 """
 layout_user_order_details_1 ="""
import React from 'react';
@@Imports@@
const @@PageName@@ = () => {
    useDocumentTitle('@@DocumentTitle@@');
    return (
        <>
            @@Pos1@@
            <div className="py-2 px-[10px] mt-10 md:px-[60px] lg:px-[90px]">                    
                <div className="flex flex-col md:flex-row py-[50px]">
                    <div className="w-full md:w-1/3 m-2 border border-black-600 drop-shadow-md p-5 h-1/2">
                    @@Pos2@@
                    </div>
                    <div className="w-full md:w-2/3 m-2 border border-black-600 drop-shadow-md p-5">
                        <div className="overflow-x-auto">
                            @@Pos3@@
                        </div>
                    </div>
                </div>
            </div>
        </>
    );
}
export default @@PageName@@;
 """
 layouts["layout_user_order_details_1"] = layout_user_order_details_1


 """
 User change password layout 1
 """
 layout_user_change_password_1 ="""
import React, { useEffect } from 'react';
@@Imports@@

const UpdatePasswordSchema = Yup.object().shape({
    old_password: Yup.string()
      .required('Current password is required.'),
    password: Yup.string()
      .required('Password is required.')
      .min(8, 'Password length should be at least 8 characters.')
      .matches(/[A-Z\W]/g, 'Password should contain at least 1 uppercase letter.'),
    password_confirm: Yup.string()
        .required('Confirm password is required.')
        .oneOf([Yup.ref('password')], 'Passwords does not match')
});

const @@PageName@@ = () => {
  useDocumentTitle('@@DocumentTitle@@');
  const { profile, isLoading } = useSelector((state) => ({
		profile: state.profile,
		isLoading: state.app.loading
	}));
    const dispatch = useDispatch();

    useEffect(() => () => {
		dispatch(setLoading(false));
	}, []);

    const update = (credentials) => {
		dispatch(updateProfile({
			updates: {
				first_name: profile.first_name,
				last_name: profile.last_name,
				email: profile.email,
				gender: profile.gender,
				mobile_number: 
                    profile.mobile_number ?
                    profile.mobile_number : ''
				
			},
			address : {
				state_id: profile.state ? profile.state : '',
				city_id: profile.city ? profile.city : ''
			},
			credentials
		}));
	};

    const onSubmitUpdate = (form) => {
		// check if data has changed
		const fieldsChanged = Object.keys(form).some((key) => profile[key] !== form[key]);
		if (fieldsChanged) {
            let password = form.password
            let old_password = form.old_password
			update({password, old_password});
		}
	};
  return (
	<>
		@@Pos1@@
		<div className="py-2 px-[10px] mt-10 md:px-[60px] lg:px-[90px]">                    
			<div className="flex flex-col md:flex-row py-[50px]">	
                <div className="w-full md:w-1/3 m-2 border border-black-600 drop-shadow-md p-5 h-1/2">
                    @@Pos2@@
                </div>
                <Formik
                    initialValues={{
                        old_password: '',
                        password: '',
                        password_confirm: ''
                    }}
                    validateOnChange
                    validationSchema={UpdatePasswordSchema}
                    onSubmit={onSubmitUpdate}
                >
                    <div className="w-full md:w-2/3 m-2 border border-black-600 drop-shadow-md p-5">
                        <Form>
                            <div className="overflow-x-auto">
                                <div className="flex flex-col md:flex-row">
                                    <div className="mt-3 mb-3 w-auto md:w-full">
                                        @@Pos3@@
                                    </div>
                                </div>
                                <div className="flex flex-col md:flex-row">
                                    <div className="mt-3 mb-3 w-auto md:w-full">
                                        @@Pos4@@
                                    </div>
                                </div>
                                <div className="flex flex-col md:flex-row">
                                    <div className="mt-3 mb-3 w-auto md:w-full">
                                        @@Pos5@@
                                    </div>
                                </div>
                                <div className="mt-10 flex justify-center">
                                    <button 
                                        type="submit"
                                        disabled={isLoading}
                                        className="button button--theme overflow-hidden bg-[#9c0] 
                                        hover:bg-yellow-300 text-white text-sm transition-all ease-in-out duration-300 
                                        rounded py-3 px-5 m-2 flex items-center flex-nowrap w-80 justify-center">
                                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" className="fill-current mr-2" ><path d="M5 21h14a2 2 0 0 0 2-2V8a1 1 0 0 0-.29-.71l-4-4A1 1 0 0 0 16 3H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2zm10-2H9v-5h6zM13 7h-2V5h2zM5 5h2v4h8V5h.59L19 8.41V19h-2v-5a2 2 0 0 0-2-2H9a2 2 0 0 0-2 2v5H5z"></path></svg>
                                        <span>{isLoading ? '@@LoadingPageText@@' : '"@@SubmitBtnText@@'}</span>
                                    </button>
                                </div>
                            </div>
                        </Form>
                    </div>  
                </Formik>
			</div>
		</div>
	</>
  );  
}
export default @@PageName@@;
 """
 layouts["layout_user_change_password_1"] = layout_user_change_password_1


 """
 Admin View order
 """
 layout_admin_view_order ="""
import React from 'react';
@@Imports@@
const @@PageName@@ = () => {
    const { id } = useParams();
    return (
        <div className="bg-gray-100">
            <div className="header bg-white h-16 px-10 py-8 border-b-2 border-gray-200 flex items-center justify-between">
                <div className="flex items-center space-x-2 text-gray-400">
                    <span className="text-green-700 tracking-wider font-thin text-md"><Link to={ROUTE.ADMIN_DASHBOARD}>@@NavLink1@@</Link></span>
                    <span>/</span>
                    <span className="text-green-700 tracking-wider font-thin text-md"><Link to={ROUTE.ADMIN_ORDERS}>@@NavLink2@@</Link></span>
                    <span>/</span>
                    <span className="tracking-wide text-md">
                        <span className="text-base">@@SubHeading1@@</span>
                    </span>
                    <span>/</span>
                </div>
            </div>
            <div className="header my-3 h-12 px-10 py-8  flex items-center justify-between">
                <h1 className="font-medium text-2xl">@@SubHeading1@@</h1>
                <Link to={ROUTE.ADMIN_ORDERS} className="focus:outline-none text-white m-4 p-3 font-semibold rounded-md bg-green-700 hover:bg-green-600 hover:shadow-lg transition-all duration-100"> <span><FaAngleLeft className="inline-block w-5 h-5"/>
            </span> Back to orders</Link>
            </div>
            <Orderlist orderId={id}/>
        </div>
    )  
}
export default @@PageName@@;
 """
 layouts["layout_admin_view_order"] = layout_admin_view_order


 layout_admin_orders ="""
import React, {useState, useEffect, useCallback} from 'react';
@@Imports@@
const @@PageName@@ = () => {
    const [allorders, fetchAllOrders] = useState([]);
    const [sortType, setSortType] = useState([]);
    const [paymentType, setPaymentType] = useState([]);
    const [deliveryStatus, setDeliveryStatus] = useState([]);
    const [searchResult, setSearchResult] = useState('');
    const [searchData, fetchSearchData] = useState([]);
    const [searchRef, setSearchRef] = useState('');
    const [totalSum, setTotalSum] = useState('');
    const [sortDate, setSortDate] = useState(new Date());
    const nf = new Intl.NumberFormat();

    const getData = () => {
        fetch(`${ROUTE.PRODUCTS_API}/order/all`)
            .then((res) => res.json())
            .then((res) => {
                fetchAllOrders(res.data)
               //console.log(res.data)
               setTotalSum((res.data.reduce((a,v) =>  a = a + v.amount , 0 )))
        })
    } 


    useEffect(() => {
        getData()
        return () => {
            fetchAllOrders({});
          };
    }, [])


    const SearchOrder = useCallback( async (param)  => {
        if (param){
            fetch(`${ROUTE.PRODUCTS_API}/order/search/${param}`)
            .then((res) => res.json())
            .then((res) => {
                fetchSearchData(res.data)
                setSearchResult("Success")
                setTotalSum((res.data.reduce((a,v) =>  a = a + v.amount , 0 )))
            })
           
        }
        else {
            setSearchResult('')
            getData()
        }
    }, []);

    const SearchOrderByDate = useCallback( async (param)  => {
        if (param){
            var search_data = param.toString().slice(0, 24)
            fetch(`${ROUTE.PRODUCTS_API}/order/sort?date=${search_data}`)
            .then((res) => res.json())
            .then((res) => {
                fetchSearchData(res.data)
                setSearchResult("Success")
                setTotalSum((res.data.reduce((a,v) =>  a = a + v.amount , 0 )))
            })
        }
        else {
            setSearchResult('')
            getData()
        }
    }, []);


    const SearchOrderByPayment = useCallback( async (param)  => {
        if (param){
            fetch(`${ROUTE.PRODUCTS_API}/order/payment/${param}`)
            .then((res) => res.json())
            .then((res) => {
                fetchSearchData(res.data)
                setSearchResult("Success")
                setTotalSum((res.data.reduce((a,v) =>  a = a + v.amount , 0 )))
            })
           
        }
        else {
            setSearchResult('')
            getData()
        }
    }, []);

    const SearchOrderByDelivery = useCallback( async (param)  => {
        if (param){
            fetch(`${ROUTE.PRODUCTS_API}/order/delivery/${param}`)
            .then((res) => res.json())
            .then((res) => {
                fetchSearchData(res.data)
                setSearchResult("Success")
                setTotalSum((res.data.reduce((a,v) =>  a = a + v.amount , 0 )))
            })
        }
        else {
            setSearchResult('')
            getData()
        }
    }, []);


    const handleDateChange = (data) =>{
        setSortDate(data)
        SearchOrderByDate(data)
    }


    const searchRefID = () => {
        const timer = setSearchRef(() => {
            SearchOrder(searchRef)
       
        }, 2000)
        return () => clearTimeout(timer)
    }


    const handPaymentChange = (selectedOption) => {
       setPaymentType(selectedOption)
        SearchOrderByPayment(selectedOption.value)
    
    }


    const handDeliverStatusChange = (selectedOption) => {
        setDeliveryStatus(selectedOption)
        SearchOrderByDelivery(selectedOption.value)
    }


    let orderList;
    if(allorders.length > 0){
        orderList = allorders.map((item, i) => {
            return (
                <tr key={i}>
                    <td className="p-2">
                        {item.ref_id}
                    </td>
                    <td className="p-2">
                        <p className="text-center">{item.first_name} {item.last_name}</p>
                    </td>
                    <td className="p-2">
                        <p className="text-center">{item.email}</p>
                    </td>
                    <td className="p-2">
                    &#8358;{nf.format(item.amount)}
                    </td>
                    <td className="p-2">
                    {item.status == "New" ?
                    <p className='text-center bg-blue-200 text-blue-900 px-2 py-1 rounded-md'> New</p>
                    :
                    item.status == "Pending" ?
                    <p className='text-center bg-yellow-200 text-yellow-900 px-2 py-1 rounded-md'> Pending</p>
                    :
                    item.status == "Failed" ?
                    <p className='text-center bg-red-200 text-red-900 px-2 py-1 rounded-md'> Failed</p>
                    :
                    item.status == "Successful" ?
                    <p className='text-center bg-lime-200 text-lime-900 px-2 py-1 rounded-md'> Successful</p>
                    :
                    <p className='text-center'> Payment not initiated</p>
                    }
                        
                    </td>
                    <td className="p-2">
                        <p className="text-center">{ item.created_at }</p>
                    </td>
                    <td className="p-2">
                        {item.delivery_status == "Pending" ?
                        <p className=' text-center bg-red-200 text-red-800 px-2 py-1 rounded-full'> Pending</p>
                        :
                        item.delivery_status == "Shipped" ?
                        <p className='text-center bg-blue-200 text-blue-800 px-2 py-1 rounded-full'> Shipped</p>
                        :
                        item.delivery_status == "Delivered" ?
                        <p className='text-center bg-green-200 text-green-800 px-2 py-1 rounded-full'> Delivered</p>
                        :
                        <p className=''> Not Delivered</p>
                         }
                    </td>
                    <td className="p-2">
                        <div className="flex justify-center">
                            <button>
                            <Link to={`${ROUTE.VIEW_ORDERS}/${item.id}/${item.ref_transaction_id}`}> <FaEye className="text-green-800 mx-2 h-5 w-5" /></Link>
                            </button>                               
                        </div>
                    </td>
                </tr>
            )
        }

        );
    } else {
      orderList =  (<tr className=''><td colSpan={8} className="">
        <div className="flex flex-col my-4 space-y-3 justify-center items-center text-xl font-medium tracking-wide py-4 text-green-700 text-center">
            <MdOutlineProductionQuantityLimits className="w-16 h-16" />
            <p>@@EmptyRecordMssg@@</p>
        </div>
        </td></tr>)
    }

    let searchOrderList;
    if(searchData.length > 0){
        searchOrderList = searchData.map((items, i) => {
            return (
                <tr key={i}>
                    <td className="p-2">
                        {items.ref_id}
                    </td>
                    <td className="p-2">
                        <p className="text-center">{items.first_name} {items.last_name}</p>
                    </td>
                    <td className="p-2">
                        <p className="text-center">{items.email}</p>
                    </td>
                    <td className="p-2">
                    &#8358;{nf.format(items.amount)}
                    </td>
                    <td className="p-2">
                    {items.status == "New" ?
                    <p className='text-center bg-blue-200 text-blue-900 px-2 py-1 rounded-md'> New</p>
                    :
                    items.status == "Pending" ?
                    <p className='text-center bg-yellow-200 text-yellow-900 px-2 py-1 rounded-md'> Pending</p>
                    :
                    items.status == "Failed" ?
                    <p className='text-center bg-red-200 text-red-900 px-2 py-1 rounded-md'> Failed</p>
                    :
                    items.status == "Successful" ?
                    <p className='text-center bg-lime-200 text-lime-900 px-2 py-1 rounded-md'> Successful</p>
                    :
                    <p className='text-center'> Payment not initiated</p>
                    }
                        
                    </td>
                    <td className="p-2">
                        <p className="text-center">{ items.created_at }</p>
                    </td>
                    <td className="p-2">
                        {items.delivery_status == "Pending" ?
                        <p className=' text-center bg-red-200 text-red-800 px-2 py-1 rounded-full'> Pending</p>
                        :
                        items.delivery_status == "Shipped" ?
                        <p className='text-center bg-blue-200 text-blue-800 px-2 py-1 rounded-full'> Shipped</p>
                        :
                        items.delivery_status == "Delivered" ?
                        <p className='text-center bg-green-200 text-green-800 px-2 py-1 rounded-full'> Delivered</p>
                        :
                        <p className=''> Not Delivered</p>
                         }
                    </td>
                    <td className="p-2">
                        <div className="flex justify-center">
                            <button>
                            <Link to={`${ROUTE.VIEW_ORDERS}/${items.id}/${items.ref_transaction_id}`}> <FaEye className="text-green-800 mx-2 h-5 w-5" /></Link>
                            </button>                               
                        </div>
                    </td>
                </tr>
            )
        }

        );
    }else {
        searchOrderList =  (<tr className=''><td colSpan={8} className="">
          <div className="flex flex-col my-4 space-y-3 justify-center items-center text-xl font-medium tracking-wide py-4 text-green-700 text-center">
              <MdOutlineProductionQuantityLimits className="w-16 h-16" />
              <p>@@EmptyRecordMssg@@</p>
          </div>
          </td></tr>)
      }

    return (
        <div className="bg-gray-100">
            <div className="header bg-white h-16 px-10 py-8 border-b-2 border-gray-200 flex items-center justify-between">
                <div className="flex items-center space-x-2 text-gray-400">
                    <span className="text-green-700 tracking-wider font-thin text-md"><Link to={ROUTE.ADMIN_DASHBOARD}>Home</Link></span>
                    <span>/</span>
                    <span className="tracking-wide text-md">
                        <span className="text-base">@@SubHeading1@@</span>
                    </span>
                    <span>/</span>
                </div>
            </div>
            <div className="header my-3 h-12 px-10 py-8  flex items-center justify-between">
                <h1 className="font-medium text-2xl">@@SubHeading1@@</h1>
                <div className="focus:outline-none text-white m-4 p-3 font-semibold rounded-md bg-green-700 hover:bg-green-600 hover:shadow-lg transition-all duration-100 overflow-x-auto"> <span className=' whitespace-nowrap overflow-x-auto items-center flex-nowrap'><FaMoneyCheckAlt className="inline-block w-5 h-5 mr-3"/>
                    </span>&#8358;{nf.format(totalSum)}</div>
            </div>
            
            <div className="flex flex-col mx-3 lg:flex-row">
                <div className="w-full m-4 bg-white shadow-lg text-lg rounded-sm border border-gray-200">
                    <div className="overflow-x-auto rounded-lg  p-3">
                        <h2 className="font-medium text-xl m-4">Filter</h2>
                        <hr/>
                        <div className='flex flex-col md:flex-row w-full my-6'>
                            <div className="w-full md:w-2/3 px-3 mb-6">
                                <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='vendor_first_name'>Search by ref_id</label>
                                <input className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d]" type='text' name="vendor_first_name" placeholder="Enter Ref_id" value={searchRef}  onChange={(e) => setSearchRef(e.target.value)} onKeyUp={searchRefID}/>
                            
                            </div>
                            <div className="w-full md:w-2/3 px-3 mb-6">
                                <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='vendor_last_name'>Filter by</label>
                                <Select defaultValue={sortType} onChange={setSortType} options={Sortlist} className="z-50"/>
                                
                            </div>
                            {sortType.value == 1 ?
                                <div className="w-full md:w-2/3 px-3 mb-6">
                                <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='vendor_last_name'>Date</label>
                                <DatePicker selected={sortDate} onChange={(date:Date) => handleDateChange(date)} />
                                </div>
                            :
                            sortType.value == 2 ?
                                <div className="w-full md:w-2/3 px-3 mb-6">
                                <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='vendor_last_name'>Payment</label>
                                <Select defaultValue={paymentType} options={Paymentlist} onChange={handPaymentChange} className="z-50"/>
                                </div>
                            :
                            sortType.value == 3 ?
                                <div className="w-full md:w-2/3 px-3 mb-6">
                                <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='vendor_last_name'>Delivery</label>
                                <Select defaultValue={deliveryStatus} onChange={handDeliverStatusChange} options={DeliveryStatuslist} className="z-50"/>
                                </div>
                            :
                            " "
                            }

                        </div>
                        
                        <table className="table-auto w-full mt-3">
                            <thead className="text-sm font-semibold uppercase text-gray-800 bg-gray-50">
                                <tr className="font-semibold text-center">
                                    <th>@@TableHead1@@</th>
                                    <th className="p-2">@@TableHead2@@
                                    </th>
                                    <th className="p-2">@@TableHead3@@
                                    </th>
                                    <th className="p-2">@@TableHead4@@
                                    </th>
                                    <th className="p-2">@@TableHead5@@
                                    </th>
                                    <th className="p-2">@@TableHead6@@
                                    </th>
                                    <th className="p-2">@@TableHead7@@
                                    </th>
                                    <th className="p-2">@@TableHead8@@
                                    </th>
                                </tr>
                            </thead>

                            <tbody className="text-sm divide-y divide-gray-100">
                                {searchResult == "Success" && sortType.value != 0 ? 
                                    searchOrderList
                                :searchResult == "Success" && sortType.value == 0 ? 
                                    orderList
                                :
                                    orderList
                                }
                            </tbody>
                        </table>
                    
                    </div>
                </div>
                
            </div>        
        </div>
    )
}
export default @@PageName@@;
 """
 layouts["layout_admin_orders"] = layout_admin_orders


 layout_admin_addblog ="""
import React, {useCallback, useEffect, useState} from 'react';
@@Imports@@
const @@PageName@@ = () => {
  const [blogs, fetchblogs] = useState([]);
    const {register, handleSubmit, reset, formState: { errors }, clearErrors } = useForm();
    const [selectedImage, setSelectedImage] = useState();
    const [blogImage, setBlogImage] = useState();
    const [blogContent, setBlogContent] = useState('');

    const handleChange = (e, editor) => {
        clearErrors('content');
        setBlogContent(editor.getData())
    }
    const [loading, setLoading] = useState(false);
    let formData = new FormData();

    const onSelectFile = useCallback( async (e)  => {
        const file = e.target.files[0];
        const reader = new FileReader();
        reader.readAsDataURL(file);
        setBlogImage(file)
        reader.onloadend = () => {
            setSelectedImage(reader.result);
        };
    }, []);
 
    const submitForm = (data) => {
        formData.append('blog_image', blogImage)
        formData.append('title', data.title);
        formData.append('summary', data.summary);
        formData.append('content', blogContent)

        const requestOptions = {
            headers: {
              'Content-type': 'multipart/form-data'
            }
        }        
        axios.post(
            `${ROUTE.BLOGS_API}/blogs`,

            formData,
            requestOptions
        ).then(res => res)
        .then(data =>{
            if (data.status == 200 || data.status == 302) {
                successAlert(data)
            }
            else {
                errorAlert(data)
            }
        })
        .catch(err => console.log(err))
      reset()
      setSelectedImage('');
      setBlogContent('')
    }
    const successAlert = (response) => {
        return(
          swal({
              title: "Saved successfully!",
              text: response.data.message,
              icon: "success"
          }).then(function () {
                getData()
          })
        )
    }
    const errorAlert = (error) => {
        return(
          swal({
              title: "Error!",
              text: error,
              icon: "error"
          }).then(function () {
            getData()
          })          
        )
    }    
    const getData = () => {
      setLoading(true)
      fetch(`${ROUTE.BLOGS_API}/blogs`)
        .then((res) => res.json())
        .then((res) => {
          fetchblogs(res.results.slice(0, 5))
          setLoading(false)
        })
    }
    useEffect(() => {
        getData()
    }, [])

    useEffect(() => {
        if (blogContent == '') {
            errors.content = 'Content is required';
            return
        }
    })    
    const deleteCategory = useCallback( async (id)  => {
        if(confirm('Are you sure you want to delete this category?')){
        axios.delete(
            `${ROUTE.BLOGS_API}/blogs/${id}`,{
                method : 'DELETE',
                body : JSON.stringify({
                    id : id
                }),
                headers: {
                    'Content-type': 'application/json'
                }
            })
            .then(res => res)
            .then(data =>{
              successAlert(data)
            })
            .catch(err => errorAlert(err)
            )
        }
    }, []);

    let blogList = ''
    if(blogs.length > 0){
        blogList = blogs.map((item) => {
            return (
                <tr key={item.id}>
                    <td className="p-2">
                    <img src={`${CONSTANT.IMAGE_STORE}/${item.image_path}`} className="w-8 h-8 mx-auto" alt={item.name} />
                    </td>
                    <td className="p-2">
                        {item.title}
                    </td>
                    <td className="p-2">
                        <div className="flex justify-center">
                        <Link to={`${ROUTE.ADMIN_EDIT_BLOGS}/${item.id}`} className="rounded-md hover:bg-gray-100 text-green-600 p-2 flex justify-between items-center">
                            <span><FaEdit className="w-4 h-4 mr-1"/>
                             </span> Edit
                        </Link>
                        <button className="rounded-md hover:bg-gray-100 text-red-600 p-2 flex justify-between items-center" onClick={() => deleteCategory(item.id)}>
                            <span><FaTrash className="w-4 h-4 mr-1" /></span> Delete
                        </button>
                        </div>
                    </td>
                </tr>
            )
        }

        );
    } else {
        blogList =  (<tr className=''><td colSpan={5} className="">
        <div className="flex flex-col my-4 space-y-3 justify-center items-center text-xl font-medium tracking-wide py-4 text-green-700 text-center">
            <BiCategory className="w-16 h-16" />
            <p>No blogs added yet</p>
        </div>
        </td></tr>)        
    }

    let blogLoading = (
        <>
            <tr className="mx-auto">
                <td className="p-2">
                    <div data-placeholder className="w-1/2 h-8 bg-gray-200 overflow-hidden relative">
                    </div>
                </td>
                <td className="p-2">
                    <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative">
                    </div>
                </td>
                <td className="p-2">
                    <div className="flex justify-center">
                        <div data-placeholder className="w-1/3 h-8 bg-gray-200 overflow-hidden relative">
                        </div>
                        
                    </div>    
                </td>
            </tr>
            <tr className="mx-auto">
                <td className="p-2">
                    <div data-placeholder className="w-1/2 h-8 bg-gray-200 overflow-hidden relative">
                    </div>
                </td>
                <td className="p-2">
                    <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative">
                    </div>
                </td>
                <td className="p-2">
                    <div className="flex justify-center">
                        <div data-placeholder className="w-1/3 h-8 bg-gray-200 overflow-hidden relative">
                        </div>
                        
                    </div>    
                </td>
            </tr>
            <tr className="mx-auto">
                <td className="p-2">
                    <div data-placeholder className="w-1/2 h-8 bg-gray-200 overflow-hidden relative">
                    </div>
                </td>
                <td className="p-2">
                    <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative">
                    </div>
                </td>
                <td className="p-2">
                    <div className="flex justify-center">
                        <div data-placeholder className="w-1/3 h-8 bg-gray-200 overflow-hidden relative">
                        </div>
                        
                    </div>    
                </td>
            </tr>
        </>    
    )
    
    return (
    <div className="bg-gray-100">
        <div className="header bg-white h-16 px-10 py-8 border-b-2 border-gray-200 flex items-center justify-between">
            <div className="flex items-center space-x-2 text-gray-400">
                <span className="text-green-700 tracking-wider font-thin text-md"><Link to={ROUTE.ADMIN_DASHBOARD}>Home</Link></span>
                <span>/</span>
                <span className="tracking-wide text-md">
                    <span className="text-base">@@PageTitle@@</span>
                </span>
                <span>/</span>
            </div>
        </div>
        <div className="header my-3 h-12 px-10 flex items-center justify-between">
            <h1 className="font-medium text-2xl">@@SubTitle@@</h1>
        </div>
        <div className="flex flex-col mx-3 mt-6 lg:flex-row">
            <div className="w-full m-1">
                {/* Display add blog form */}
                <form className="w-full bg-white shadow-md p-6" encType="multipart/form-data">
                    <div className="flex flex-wrap -mx-3 mb-6">
                        <div className="w-full md:w-full px-3 mb-6">
                            <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='title'>@@Input1Label@@</label>
                            <input className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d]" 
                                type='text' 
                                name="title" 
                                placeholder="Enter the Blog Title"  
                                {...register("title", { required: true})}
                            required />
                            {errors.title && <small className="text-red-500 text-xs italic mx-auto flex justify-center mt-2">Title is required</small>}
                        </div>
                        <div className="w-full md:w-full px-3 mb-6">
                            <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='title'>@@Input2Label@@</label>
                            <textarea className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d]" 
                                type='text' 
                                name="Summary" 
                                placeholder="Blog summary 250 words"  rows={3}
                                {...register("summary", { required: true})}
                            required maxLength={250}/>
                            {errors.summary && <small className="text-red-500 text-xs italic mx-auto flex justify-center mt-2">Summary is required</small>}
                        </div>
                        <div className="flex justify-center w-full overflow-x-auto mx-3 lg:mx-0">
                            <CKEditor 
                                editor={ClassicEditor}
                                onChange={handleChange} data={blogContent} className="w-full"
                            />
                        </div>
                            {errors && 
                                errors.content && <small className="text-red-500 text-xs italic mx-auto flex justify-center mt-2">Content is required</small>}

                        <div className="w-full px-3  my-8">
                            <label className="mx-auto cursor-pointer flex w-full max-w-lg flex-col items-center justify-center rounded-xl border-2 border-dashed border-green-400 bg-white p-6 text-center" htmlFor='dropzone-file'>
                            <svg xmlns="http://www.w3.org/2000/svg" className="h-10 w-10 text-green-800" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="2">
                            <path strokeLinecap="round" strokeLinejoin="round" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
                            </svg>

                            <h2 className="mt-4 text-xl font-medium text-gray-700 tracking-wide">@@Input3Label@@</h2>

                            <p className="mt-2 text-gray-500 tracking-wide">Upload or drag & drop your file SVG, PNG, JPG or GIF. </p>

                            <input id="dropzone-file" type="file" className="hidden" 
                                name="blog_image" onChange={onSelectFile} accept="image/png, image/jpeg, image/webp"/>
                            </label>
                            {errors.blog_image && <small className="text-red-500 text-xs italic">Blog image is required</small>}
                        </div>
                        <div className="w-full flex justify-center mb-5">
                            {selectedImage &&
                                (
                                    <img src={selectedImage} className="w-32 h-32"/>
                                )
                            } 
                        </div>
                        <div className="w-full md:w-full px-3 mb-6">
                            <button className="appearance-none block w-full bg-green-700 text-gray-100 font-bold border border-gray-200 rounded-lg py-3 px-3 leading-tight hover:bg-green-600 focus:outline-none focus:bg-white focus:border-gray-500"
                            onClick={handleSubmit(submitForm)}
                            >Post Blog</button>
                        </div>
                        
                    </div>
                </form>
            </div>            
        </div>
        <div className="w-full m-1 bg-white shadow-lg text-lg rounded-sm border border-gray-200">
            <h2 className="font-medium text-2xl text-center mx-auto py-4">Recently added blog posts</h2>
                <div className="overflow-x-auto rounded-lg p-3">
                    {/* Display blogs table */}
                    <table className="table-auto w-full">
                        <thead className="text-sm font-semibold uppercase text-gray-800 bg-gray-50">
                            <tr>
                                <th className="p-2">
                                <svg xmlns="http://www.w3.org/2000/svg" className="fill-current w-5 h-5 mx-auto"><path d="M6 22h12a2 2 0 0 0 2-2V8l-6-6H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2zm7-18 5 5h-5V4zm-4.5 7a1.5 1.5 0 1 1-.001 3.001A1.5 1.5 0 0 1 8.5 11zm.5 5 1.597 1.363L13 13l4 6H7l2-3z"></path></svg>
                                </th>
                                <th className="p-2">
                                    <div className="font-semibold text-left">Blog Title</div>
                                </th>
                                <th className="p-2">
                                    <div className="font-semibold text-center">Action</div>
                                </th>
                            </tr>
                        </thead>

                        <tbody className="text-sm divide-y divide-gray-100">
                            {loading 
                                ? 
                                blogLoading
                                : blogList   
                            }
                        </tbody>
                    </table>
                </div>
            </div>       
    </div>
  )
}
export default @@PageName@@;
 """
 layouts["layout_admin_addblog"] = layout_admin_addblog

 layout_admin_editblog ="""
import React, { useEffect, useState, useCallback } from 'react';
@@Imports@@
const @@PageName@@ = () => {
  const { id } = useParams();
    const [loading, setLoading] = useState(false);
    const [blogId, setblogId] = useState('');
    const [blogTitle, setBlogTitle] = useState('');
    const [blogContent, setBlogContent] = useState('');
    const [productImage, setProductImage] = useState('');
    const [selectedImage, setSelectedImage] = useState();
    const [newProductImage, setNewProductImage] = useState();
    const [blogSummary, setBlogSummary] = useState();
    let formData = new FormData();
    const handleChange = (e, editor) => {
        clearErrors('content');
        setBlogContent(editor.getData())
    }
    const {register, handleSubmit, reset, setValue, formState: { errors }, clearErrors } = useForm();
    const getData = async () => {
        setLoading(true)
        await fetch(`${ROUTE.BLOGS_API}/blogs/${id}`)
          .then((res) => res.json())
          .then((res) => {
            setblogId(res.data[0].id)
            setBlogTitle(res.data[0].title)
            setBlogSummary(res.data[0].summary)
            setBlogContent(res.data[0].content)
            setProductImage(res.data[0].image_path)
        })
        setLoading(false)
    }

    useEffect(() => {
        getData()
    }, [])

    useEffect(() => {
        setTimeout(() => 
            setValue("title", blogTitle),
            setValue("summary", blogSummary)
        );
    }, [loading]);

    const onSelectFile = useCallback( async (e)  => {
        const file = e.target.files[0];
        const reader = new FileReader();
        reader.readAsDataURL(file);
        setNewProductImage(file)
        reader.onloadend = () => {
            setSelectedImage(reader.result);
        };
    }, []);

    const submitForm = (data) => {
        
        formData.append('product_image', newProductImage)
        formData.append('title', data.title);
        formData.append('summary', data.summary);
        formData.append('content', blogContent)      

        const requestOptions = {
            method: "POST",
            headers: {
              'Content-type': 'multipart/form-data'
            }
        }
        axios.put(
            `${ROUTE.BLOGS_API}/blogs/${blogId}`,
            formData,
            requestOptions
        ).then(res => res)
        .then(data =>{
            if (data.status == 200 || data.status == 302) {
                successAlert(data)
            }
            else {
                errorAlert(data.message)
            }
        })
        .catch(err => errorAlert(err))
  
      reset()
      setSelectedImage('');
    }

    const successAlert = (response) => {
        return(
          swal({
              title: "Info!",
              text: response.data.message,
              icon: "success"
          }).then(function () {
                getData()
          })
        )
    }
    const errorAlert = (error) => {
        return(
          swal({
              title: "Error!",
              text: error,
              icon: "error"
          }).then(function () {
            getData()
          })          
        )
    }

  return (
    <div className="bg-gray-100">
        <div className="header bg-white h-16 px-10 py-8 border-b-2 border-gray-200 flex items-center justify-between">
                <div className="flex items-center space-x-2 text-gray-400">
                <span className="text-green-700 tracking-wider font-thin text-md"><Link to={ROUTE.ADMIN_DASHBOARD}>@@NavLink1@@</Link></span>
                <span>/</span>
                <span className="tracking-wide text-md">
                    <span className="text-green-700 tracking-wider font-thin text-md"><Link to={ROUTE.ADMIN_BLOGS}>@@NavLink2@@</Link></span>
                </span>
                <span>/</span>
                <span className="tracking-wide text-md">
                    <span className="text-base">@@PageTitle@@</span>
                </span>
                </div>
        </div>
        <div className="header my-3 h-12 px-4 lg:px-10 py-8  flex items-center justify-between">
            <h1 className="font-medium text-2xl">@@SubTitle@@</h1>
            <Link to={ROUTE.ADMIN_BLOGS} className="focus:outline-none text-white m-4 p-3 font-semibold rounded-md bg-green-700 hover:bg-green-600 hover:shadow-lg transition-all duration-100"> <span><FaAngleLeft className="inline-block w-5 h-5"/>
            </span>@@ProceedToPreviousPageText@@</Link>
        </div>
        {loading
        ? (<div className="h-full flex justify-center items-center">
                <h3 className="font-bold text-green-600 text-2xl mx-auto ">Loading...</h3>
            </div>
        )
        :
        (
            <div className="flex flex-col mx-3 lg:flex-row">
            <form className="w-full lg:w-3/5 bg-white shadow-md p-6">
                <div className="flex flex-wrap -mx-3 mb-6">
                    <div className="w-full px-3 mb-6">
                        <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='title'>@@Input1Label@@</label>
                        <input className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d] focus:ring-[#98c01d]" type='text' name="title"
                        {...register("title", { required: true })} required onChange={(e) => setBlogTitle(e.target.value)} />
                        {errors.title && <small className="text-red-500 text-xs italic">Blog title is required</small>}
                    </div>

                    <div className="w-full md:w-full px-3 mb-6">
                            <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='title'>@@Input2Label@@</label>
                            <textarea className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d]" 
                            type='text' 
                            name="summary" 
                            placeholder="Blog summary 250 words" rows={3} 
                            {...register("summary", { required: true})}
                            required maxLength={250} onChange={(e) => setBlogSummary(e.target.value)}/>
                            {errors.summary && <small className="text-red-500 text-xs italic mx-auto flex justify-center mt-2">Summary is required</small>}
                        </div>

                    <div className="w-full px-3 mb-6">
                        <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='content'>@@Input3Label@@</label>
                            <CKEditor 
                                editor={ClassicEditor}
                                onChange={handleChange} data={blogContent} className="w-full"
                            />
                    </div>
                    <div className="w-full px-3 mb-12">
                        <label className="cursor-pointer flex w-fit max-w-lg flex-col items-center justify-center rounded-xl border-2 border-dashed border-green-400 bg-white p-6 mx-auto" htmlFor='product_image'>
                        <svg xmlns="http://www.w3.org/2000/svg" className="h-10 w-10 text-green-800" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="2">
                        <path strokeLinecap="round" strokeLinejoin="round" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
                        </svg>

                        <h2 className="mt-4 text-xl font-medium text-gray-700 tracking-wide">@@Input4Label@@</h2>

                        <p className="mt-2 text-gray-500 tracking-wide">Upload or drag & drop your file SVG, PNG, JPG or GIF. </p>

                        <input name="product_image" id="product_image" type="file" className="hidden" onChange={onSelectFile} accept="image/png, image/jpeg, image/webp"/>
                        </label>
                        {errors.product_image && <small className="text-red-500 text-xs italic">Blog image is required</small>}
                    </div>
                    {errors.product_image && <small className="text-red-500 text-xs italic">Blog image is required</small>}

                    <div className="w-full mx-12 flex justify-center mb-5">
                        {productImage &&
                            (
                                <img src={`${CONSTANT.IMAGE_STORE}/${productImage}`}  className={selectedImage ? "hidden" : `w-32 h-32 $`}/>
                            )
                        }
                        {selectedImage &&
                            (
                                <img src={selectedImage} className="w-32 h-32"/>
                            )
                        } 
                    </div>
                    <div className="w-full px-3 mb-6">
                        <button className="appearance-none w-full block bg-green-700 text-gray-100 font-bold border border-gray-200 rounded-lg py-3 px-3 leading-tight hover:bg-green-600 focus:outline-none focus:bg-white focus:border-gray-500"
                        onClick={handleSubmit(submitForm)}
                        >Update Blog</button>
                    </div>
                </div>
            </form>          
        </div> 
        )
        }       
    </div>
  )
}
export default @@PageName@@;
 """
 layouts["layout_admin_editblog"] = layout_admin_editblog


 layout_admin_blogs ="""
import React, {useEffect, useState, useCallback} from 'react';
@@Imports@@
const @@PageName@@ = () => {
  const [blogs, fetchBlogs] = useState([]);
  const [loading, setLoading] = useState(false);
  const getData = () => {
    setLoading(true)
      fetch(`${ROUTE.BLOGS_API}/blogs`)
        .then((res) => res.json())
        .then((res) => {
          fetchBlogs(res.results)
          setLoading(false)
        })
    }

    useEffect(() => {
        getData()
    }, [])

    const successAlert = (response) => {
      return(
        swal({
            title: "Info!",
            text: response.data.message,
            icon: "success"
        }).then(function () {
              getData()
        })
      )
  }
  const errorAlert = (error) => {
      return(
        swal({
            title: "Error!",
            text: error,
            icon: "error"
        }).then(function () {
          getData()
        })          
      )
  }
    
    const deleteBlog = useCallback( async (id)  => {
      if(confirm('Are you sure you want to delete this blog post?')){
        axios.delete(
          `${ROUTE.BLOGS_API}/blogs/${id}`,{
              method : 'DELETE',
              body : JSON.stringify({
                  id : id
              }),
              headers: {
                  'Content-type': 'application/json'
              }
          })
          .then(res => res)
          .then(data =>{
            successAlert(data)
          })
          .catch(err => errorAlert(err)
          )
      }

  }, []);
    let blogList = ''
    if(blogs.length > 0){
      blogList = blogs.map((item, i) => {
            return (
                <tr key={i}>
                    <td className="p-2">
                      <img src={`${CONSTANT.IMAGE_STORE}/${item.image_path}`} className="h-8 w-16 mx-auto" />
                    </td>
                    <td className="p-2">
                        {item.title}
                    </td>
                    <td className="p-2">
                      <div className="flex justify-center">
                          <Link to={`${ROUTE.ADMIN_EDIT_BLOGS}/${item.id}`} className="rounded-md hover:bg-gray-100 text-green-600 p-2 flex justify-between items-center">
                              <span><FaEdit className="w-4 h-4 mr-1"/>
                                </span> Edit
                          </Link>
                          <button className="rounded-md hover:bg-gray-100 text-red-600 p-2 flex justify-between items-center" value={item.id} onClick={() => deleteBlog(item.id)}>
                              <span><FaTrash className="w-4 h-4 mr-1" /></span> Delete
                          </button>
                        </div>
                    </td>
                </tr>
            )
        }

        );
    } else {
      blogList =  (<tr className=''><td colSpan={8} className="">
        <div className="flex flex-col my-4 space-y-3 justify-center items-center text-xl font-medium tracking-wide py-4 text-green-700 text-center">
            <MdOutlineProductionQuantityLimits className="w-16 h-16" />
            <p>No blogs added yet</p>
        </div>
        </td></tr>)
        
    }

    let blogLoading = (
      <>
          <tr className="mx-auto">
              <td className="p-2">
                  <div data-placeholder className="w-1/2 h-8 bg-gray-200 overflow-hidden relative mx-auto">
                  </div>
              </td>
              <td className="p-2">
                  <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative">
                  </div>
              </td>
              <td className="p-2">
                  <div className="flex justify-center">
                      <div data-placeholder className="w-1/3 h-8 bg-gray-200 overflow-hidden relative">
                      </div>
                      
                  </div>    
              </td>
          </tr>
          <tr className="mx-auto">
              <td className="p-2">
                  <div data-placeholder className="w-1/2 h-8 bg-gray-200 overflow-hidden relative mx-auto">
                  </div>
              </td>
              <td className="p-2">
                  <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative">
                  </div>
              </td>
              <td className="p-2">
                  <div className="flex justify-center">
                      <div data-placeholder className="w-1/3 h-8 bg-gray-200 overflow-hidden relative">
                      </div>
                      
                  </div>    
              </td>
          </tr>
          <tr className="mx-auto">
              <td className="p-2">
                  <div data-placeholder className="w-1/2 h-8 bg-gray-200 overflow-hidden relative mx-auto">
                  </div>
              </td>
              <td className="p-2">
                  <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative">
                  </div>
              </td>
              <td className="p-2">
                  <div className="flex justify-center">
                      <div data-placeholder className="w-1/3 h-8 bg-gray-200 overflow-hidden relative">
                      </div>
                      
                  </div>    
              </td>
          </tr>
      </>
  
  )

  return (
    <div className="bg-gray-100">
        <div className="header bg-white h-16 px-10 py-8 border-b-2 border-gray-200 flex items-center justify-between">
              <div className="flex items-center space-x-2 text-gray-400">
                <span className="text-green-700 tracking-wider font-thin text-md"><Link to={ROUTE.ADMIN_DASHBOARD}>@@LinkToDashboard@@</Link></span>
                <span>/</span>
                <span className="tracking-wide text-md">
                    <span className="text-base">@@PageTitle@@</span>
                </span>
                <span>/</span>
              </div>
        </div>
        <div className="header my-3 h-12 px-10 py-8  flex items-center justify-between">
            <h1 className="font-medium text-2xl">All Blogs</h1>
            <Link to={ROUTE.ADMIN_ADD_BLOGS} className="focus:outline-none text-white m-4 p-3 font-semibold rounded-md bg-green-700 hover:bg-green-600 hover:shadow-lg transition-all duration-100"> <span><FaPlus className="inline-block w-4 h-3"/>
            </span> @@PostNewBlog@@</Link>
        </div>
        <div className="flex flex-col mx-3 lg:flex-row">
            <div className="w-full m-4 bg-white shadow-lg text-lg rounded-sm border border-gray-200">
                <div className="overflow-x-auto rounded-lg  p-3">
                    {/* Display blogs table */}
                    <table className="table-auto w-full">
                        <thead className="text-sm font-semibold uppercase text-gray-800 bg-gray-50">
                            <tr className="font-semibold">
                                <th><svg xmlns="http://www.w3.org/2000/svg" className="fill-current w-5 h-5 mx-auto" ><path d="M6 22h12a2 2 0 0 0 2-2V8l-6-6H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2zm7-18 5 5h-5V4zm-4.5 7a1.5 1.5 0 1 1-.001 3.001A1.5 1.5 0 0 1 8.5 11zm.5 5 1.597 1.363L13 13l4 6H7l2-3z"></path></svg></th>
                                <th className="p-2">@@TableHead1@@
                                </th>
                                <th className="p-2">@@TableHead2@@
                                </th>
                            </tr>
                        </thead>
                        <tbody className="text-sm divide-y divide-gray-100">
                          { loading
                            ? blogLoading
                            : blogList }
                        </tbody>
                    </table>
                </div>
            </div>
            
        </div>        
    </div>
  )
}
export default @@PageName@@;
 """
 layouts["layout_admin_blogs"] = layout_admin_blogs


 layout_admin_categories ="""
import React, { useState, useEffect, useCallback } from 'react';
@@Imports@@
const @@PageName@@ = () => {
  const [loading, setLoading] = useState(false);
    const [categories, fetchcategories] = useState([]);
    const {register, handleSubmit, reset, formState: { errors } } = useForm();
    const [selectedImage, setSelectedImage] = useState();
    const [categoryImage, setCategoryImage] = useState();
    let formData = new FormData();

    const onSelectFile = useCallback( async (e)  => {
        const file = e.target.files[0];
        const reader = new FileReader();
        reader.readAsDataURL(file);
        setCategoryImage(file)
        reader.onloadend = () => {
            setSelectedImage(reader.result);
        };
    }, []);

    const submitForm = (data) => {
        formData.append('category_image', categoryImage)
        formData.append('name', data.name);
        formData.append('description', data.description)        

        const requestOptions = {
            method: "POST",
            headers: {
              'Content-type': 'multipart/form-data'
            }
        }
        axios.post(
            `${ROUTE.PRODUCTS_API}/categories`,
            formData,
            requestOptions
        ).then(res => res)
        .then(data =>{
          successAlert(data)
        })
        .catch(err => console.log(err))
      reset()
      setSelectedImage('');

    }
    const successAlert = (response) => {
        return(
          swal({
              title: "Info!",
              text: response.data.message,
              icon: "success"
          }).then(function () {
                getData()
          })
        )
    }
    const errorAlert = (error) => {
        return(
          swal({
              title: "Error!",
              text: error,
              icon: "error"
          }).then(function () {
            getData()
          })          
        )
    }

    
    const getData = () => {
      setLoading(true)
      fetch(`${ROUTE.PRODUCTS_API}/categories`)
        .then((res) => res.json())
        .then((res) => {
          fetchcategories(res.results)
          setLoading(false)
        })
    }

    useEffect(() => {
        getData()
    }, [])

    let categoryLoading = (
        <>
            <tr className="mx-auto">
                <td className="p-2">
                    <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                    </div>
                </td>
                <td className="p-2">
                    <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                    </div>
                </td>
                <td className="p-2">
                    <div data-placeholder className="w-1/2 h-8 bg-gray-200 overflow-hidden relative mx-auto">
                    </div>
                </td>
                <td className="p-2">
                    <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative">
                    </div>
                </td>
                <td className="p-2">
                    <div className="flex justify-center">
                        <div data-placeholder className="w-1/2 h-8 bg-gray-200 overflow-hidden relative">
                        </div>
                        
                    </div>    
                </td>
            </tr>
            <tr className="mx-auto">
                <td className="p-2">
                    <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                    </div>
                </td>
                <td className="p-2">
                    <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                    </div>
                </td>
                <td className="p-2">
                    <div data-placeholder className="w-1/2 h-8 bg-gray-200 overflow-hidden relative mx-auto">
                    </div>
                </td>
                <td className="p-2">
                    <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative">
                    </div>
                </td>
                <td className="p-2">
                    <div className="flex justify-center">
                        <div data-placeholder className="w-1/2 h-8 bg-gray-200 overflow-hidden relative">
                        </div>
                        
                    </div>    
                </td>
            </tr>
            <tr className="mx-auto">
                <td className="p-2">
                    <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                    </div>
                </td>
                <td className="p-2">
                    <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                    </div>
                </td>
                <td className="p-2">
                    <div data-placeholder className="w-1/2 h-8 bg-gray-200 overflow-hidden relative mx-auto">
                    </div>
                </td>
                <td className="p-2">
                    <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative">
                    </div>
                </td>
                <td className="p-2">
                    <div className="flex justify-center">
                        <div data-placeholder className="w-1/2 h-8 bg-gray-200 overflow-hidden relative">
                        </div>
                        
                    </div>    
                </td>
            </tr>
        </>
      )    
    const deleteCategory = useCallback( async (id)  => {
        if(window.confirm('Are you sure you want to delete this category?')){
        axios.delete(
            `${ROUTE.PRODUCTS_API}/categories/${id}`,{
                method : 'DELETE',
                body : JSON.stringify({
                    id : id
                }),
                headers: {
                    'Content-type': 'application/json'
                }
            })
            .then(res => res)
            .then(data =>{
              successAlert(data)
            })
            .catch(err => errorAlert(err)
            )
        }
    }, []);

    let categoryList = ''
    if(categories.length > 0){
        categoryList = categories.map((item) => {
            return (
                <tr key={item.id}>
                    <td className="p-2">
                        <input type="checkbox" className="w-5 h-5" />
                    </td>
                    {/* {require(`../../../${item.image_path}`)} */}
                    <td className="p-2">
                    <img src={`${CONSTANT.IMAGE_STORE}/${item.image_path}`} className="h-8 w-16 mx-auto" />
                    </td>
                    <td className="p-2">
                        {item.name}
                    </td>
                    <td className="p-2">
                        {item.description}
                    </td>
                    <td className="p-2">
                        <div className="flex justify-center">
                        <Link to={`${ROUTE.ADMIN_EDIT_CATEGORIES}/${item.id}`} className="rounded-md hover:bg-gray-100 text-green-600 p-2 flex justify-between items-center">
                            <span><FaEdit className="w-4 h-4 mr-1"/>
                             </span> Edit
                        </Link>
                        <button className="rounded-md hover:bg-gray-100 text-red-600 p-2 flex justify-between items-center" onClick={() => deleteCategory(item.id)}>
                            <span><FaTrash className="w-4 h-4 mr-1" /></span> Delete
                        </button>
                        </div>
                    </td>
                </tr>
            )
        }

        );
    } else {
        categoryList =  (<tr className=''><td colSpan={5} className="">
        <div className="flex flex-col my-4 space-y-3 justify-center items-center text-xl font-medium tracking-wide py-4 text-green-700 text-center">
            <BiCategory className="w-16 h-16" />
            <p>No categories added yet</p>
        </div>
        </td></tr>)        
    }
    
  return (
    <div className="bg-gray-100">
        <div className="header bg-white h-16 px-10 py-8 border-b-2 border-gray-200 flex items-center justify-between">
              <div className="flex items-center space-x-2 text-gray-400">
                <span className="text-green-700 tracking-wider font-thin text-md"><Link to={ROUTE.ADMIN_DASHBOARD}>@@LinkToDashboard@@</Link></span>
                <span>/</span>
                <span className="tracking-wide text-md">
                    <span className="text-base">@@PageTitle@@</span>
                </span>
                <span>/</span>
              </div>
        </div>
        <div className="header my-3 h-12 px-10 flex items-center justify-between">
            <h1 className="font-medium text-2xl">Product @@PageTitle@@</h1>
        </div>
        <div className="flex flex-col mx-3 mt-6 lg:flex-row">
            <div className="w-full lg:w-1/3 m-1">
                {/* Display add category form */}
                <form className="w-full bg-white shadow-md p-6" encType="multipart/form-data">
                    <div className="flex flex-wrap -mx-3 mb-6">
                        <div className="w-full md:w-full px-3 mb-6">
                            <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='category_name'>Category Name</label>
                            <input className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d]" type='text' name="name" placeholder="Category Name"  {...register("name", { required: true})}
                            required />
                            {errors.name && <small className="text-red-500 text-xs italic">Category name is required</small>}
                            {errors.name?.type === "maxLength" && <p style={{ color: "red" }}><small>Max characters should be 25 </small></p>}
                        </div>
                        
                        <div className="w-full px-3 mb-6">
                            <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='description'>Description</label>
                            <textarea rows="4" className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d]" type='text' name="description" {...register("description", { required: true })} required />
                            {errors.description && <small className="text-red-500 text-xs italic">Description is required</small>}
                        </div>
                        <div className="w-full px-3 mb-8">
                            <label className="mx-auto cursor-pointer flex w-full max-w-lg flex-col items-center justify-center rounded-xl border-2 border-dashed border-green-400 bg-white p-6 text-center" htmlFor='dropzone-file'>
                            <svg xmlns="http://www.w3.org/2000/svg" className="h-10 w-10 text-green-800" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="2">
                            <path strokeLinecap="round" strokeLinejoin="round" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
                            </svg>

                            <h2 className="mt-4 text-xl font-medium text-gray-700 tracking-wide">Category image</h2>

                            <p className="mt-2 text-gray-500 tracking-wide">Upload or drag & drop your file SVG, PNG, JPG or GIF. </p>

                            <input id="dropzone-file" type="file" className="hidden" name="category_image" onChange={onSelectFile} accept="image/png, image/jpeg, image/webp"/>
                            </label>
                            {errors.category_image && <small className="text-red-500 text-xs italic">Category image is required</small>}
                        </div>
                        <div className="w-full flex justify-center mb-5">
                            {selectedImage &&
                                (
                                    <img src={selectedImage} className="w-32 h-32"/>
                                )
                            } 
                        </div>
                        <div className="w-full md:w-full px-3 mb-6">
                            <button className="appearance-none block w-full bg-green-700 text-gray-100 font-bold border border-gray-200 rounded-lg py-3 px-3 leading-tight hover:bg-green-600 focus:outline-none focus:bg-white focus:border-gray-500"
                            onClick={handleSubmit(submitForm)}
                            >@@AddCategoryBtn@@</button>
                        </div>
                    </div>
                </form>
            </div>
            <div className="w-full lg:w-2/3 m-1 bg-white shadow-lg text-lg rounded-sm border border-gray-200">
                <div className="overflow-x-auto rounded-lg p-3">
                    {/* Display category table */}
                    <table className="table-auto w-full">
                        <thead className="text-sm font-semibold uppercase text-gray-800 bg-gray-50 mx-auto">
                            <tr>
                                <th></th>
                                <th><svg xmlns="http://www.w3.org/2000/svg" className="fill-current w-5 h-5 mx-auto"><path d="M6 22h12a2 2 0 0 0 2-2V8l-6-6H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2zm7-18 5 5h-5V4zm-4.5 7a1.5 1.5 0 1 1-.001 3.001A1.5 1.5 0 0 1 8.5 11zm.5 5 1.597 1.363L13 13l4 6H7l2-3z"></path></svg></th>
                                <th className="p-2">
                                    <div className="font-semibold">@@TableHead1@@</div>
                                </th>
                                <th className="p-2">
                                    <div className="font-semibold text-left">@@TableHead2@@</div>
                                </th>
                                <th className="p-2">
                                    <div className="font-semibold text-center">@@TableHead3@@</div>
                                </th>
                            </tr>
                        </thead>

                        <tbody className="text-sm divide-y divide-gray-100">
                            { loading
                            ? categoryLoading
                            : categoryList }
                        </tbody>
                    </table>
                </div>
            </div>            
        </div>        
    </div>
  )
}
export default @@PageName@@;
 """
 layouts["layout_admin_categories"] = layout_admin_categories

 layout_admin_edit_categories ="""
import React, { useEffect, useState, useCallback } from 'react';
@@Imports@@
const @@PageName@@ = () => {
  const [categoryId, setCategoryId] = useState("");
    const [name, setName] = useState("");
    const [loading, setLoading] = useState(false);
    const [description, setDescription] = useState("");
    const [image, setImage] = useState();
    const {register, handleSubmit, reset, setValue, formState: { errors } } = useForm();
    const [selectedImage, setSelectedImage] = useState();
    const [categoryImage, setCategoryImage] = useState();
    let formData = new FormData();

    const { id } = useParams();
    const getData = async () => {
        setLoading(true)
        await fetch(`${ROUTE.PRODUCTS_API}/categories/${id}`)
          .then((res) => res.json())
          .then((res) => {
            setCategoryId(res.data.id)
            setName(res.data.name)
            setDescription(res.data.description)
            setImage(res.data.image_path)
            setLoading(false)
          })
    }

    useEffect(() => {
        getData()
    }, [])
    useEffect(() => {
        setTimeout(() => 
            setValue("name", name),
            setValue("description", description)
        );
    }, [loading]);

    const onSelectFile = useCallback( async (e)  => {
        const file = e.target.files[0];
        const reader = new FileReader();
        reader.readAsDataURL(file);
        setCategoryImage(file)
        reader.onloadend = () => {
            setSelectedImage(reader.result);
        };
    }, []);
    const submitForm = (data) => {
        formData.append('category_image', categoryImage)
        formData.append('name', data.name);
        formData.append('description', data.description)        

        const requestOptions = {
            method: "POST",
            headers: {
              'Content-type': 'multipart/form-data'
            }
        }
        axios.put(
            `${ROUTE.PRODUCTS_API}/categories/${categoryId}`,
            formData,
            requestOptions
        ).then(res => res)
        .then(data =>{
          successAlert(data)
        })
        .catch(err => errorAlert(err))
  
      reset()
      setSelectedImage('');
    }

    const successAlert = (response) => {
        return(
          swal({
              title: "Info!",
              text: response.data.message,
              icon: "success"
          }).then(function () {
                getData()
          })
        )
    }
    const errorAlert = (error) => {
        return(
          swal({
              title: "Error!",
              text: error,
              icon: "error"
          }).then(function () {
            getData()
          })          
        )
    }
  return (
    <div className="bg-gray-100">
        <div className="header bg-white h-16 px-10 py-8 border-b-2 border-gray-200 flex items-center justify-between">
              <div className="flex items-center space-x-2 text-gray-400">
                <span className="text-green-700 tracking-wider font-thin text-md"><Link to={ROUTE.ADMIN_DASHBOARD}>@@LinkToDashboard@@</Link></span>
                <span>/</span>
                <span className="text-green-700 tracking-wider font-thin text-md">
                    <Link to={ROUTE.ADMIN_CATEGORIES}>@@LinkToCategories@@</Link>
                </span>
                <span>/</span>
                <span className="tracking-wide text-md">
                    <span className="text-base">@@PageTitle@@</span>
                </span>
                <span>/</span>
              </div>
        </div>
        <div className="header my-3 h-12 px-10 py-8  flex items-center justify-between">
                <h1 className="font-medium text-2xl">@@PageTitle@@</h1>
                <Link to={ROUTE.ADMIN_CATEGORIES} className="focus:outline-none text-white m-4 p-3 font-semibold rounded-md bg-green-700 hover:bg-green-600 hover:shadow-lg transition-all duration-100"> <span><FaAngleLeft className="inline-block w-5 h-5"/>
                </span> @@LinkToCategories@@</Link>
            </div>
        {loading
        ? (<div className="h-full flex justify-center items-center">
                <h3 className="font-bold text-green-600 text-2xl mx-auto ">Loading...</h3>
            </div>
        )
        :
        (<div className="w-full lg:w-1/2 mx-auto m-1">
            {/* Display edit category form */}
            <form className="w-full bg-white shadow-md p-6" encType="multipart/form-data">
                <div className="flex flex-wrap -mx-3 mb-6">
                        <div className="w-full md:w-full px-3 mb-6">
                            <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='name'>Category Name</label>
                            <input className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d]" type='text' name="name" placeholder="Category Name"  {...register("name", { required: true})}
                            required onChange={(e) => setName(e.target.value)} />
                            {errors.name && <small className="text-red-500 text-xs italic">Category name is required</small>}
                            {errors.name?.type === "maxLength" && <p style={{ color: "red" }}><small>Max characters should be 25 </small></p>}
                        </div>
                        
                        <div className="w-full px-3 mb-6">
                            <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='description'>@@TableHead1@@</label>
                            <textarea rows="4" className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d]" type='text' name="description" {...register("description", { required: true })} required onChange={(e) => setDescription(e.target.value)} />
                            {errors.description && <small className="text-red-500 text-xs italic">Description is required</small>}
                        </div>
                        <div className="w-full px-3 mb-8">
                            <label className="mx-auto cursor-pointer flex w-full max-w-lg flex-col items-center justify-center rounded-xl border-2 border-dashed border-green-400 bg-white p-6 text-center" htmlFor='dropzone-file'>
                            <svg xmlns="http://www.w3.org/2000/svg" className="h-10 w-10 text-green-800" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="2">
                            <path strokeLinecap="round" strokeLinejoin="round" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
                            </svg>

                            <h2 className="mt-4 text-xl font-medium text-gray-700 tracking-wide">@@TableHead2@@</h2>

                            <p className="mt-2 text-gray-500 tracking-wide">Upload or drag & drop your file SVG, PNG, JPG or GIF. </p>

                            <input id="dropzone-file" type="file" className="hidden" name="category_image" onChange={onSelectFile} accept="image/png, image/jpeg, image/webp"/>
                            </label>
                            {errors.category_image && <small className="text-red-500 text-xs italic">Category image is required</small>}
                        </div>
                        <div className="w-full mx-12 flex justify-center mb-5">
                            {image &&
                                (
                                    <img src={`${CONSTANT.IMAGE_STORE}/${image}`} className={selectedImage ? "hidden" : `w-32 h-32 $`}/>
                                )

                            }
                            
                            {selectedImage &&
                                (
                                    <img src={selectedImage} className="w-32 h-32"/>
                                )

                            } 
                        </div>
                        <div className="w-full md:w-full px-3 mb-6">
                            <button className="appearance-none block w-full bg-green-700 text-gray-100 font-bold border border-gray-200 rounded-lg py-3 px-3 leading-tight hover:bg-green-600 focus:outline-none focus:bg-white focus:border-gray-500"
                            onClick={handleSubmit(submitForm)}
                            >Update Category</button>
                        </div>
                    </div>
            </form>
        </div>
        )

        }
    
    </div>
  )
}
export default @@PageName@@;
 """
 layouts["layout_admin_edit_categories"] = layout_admin_edit_categories


 layout_admin_add_product ="""
import React, {useCallback, useEffect, useState} from 'react';
@@Imports@@
const @@PageName@@ = () => {
  const {register, handleSubmit, reset, formState: { errors } } = useForm();
    const [categories, fetchCategories] = useState([]);
    const [selectedImage, setSelectedImage] = useState();
    const [productImage, setProductImage] = useState();
    let formData = new FormData();

    const { userId } = useSelector((state) => ({
		userId: state.profile.id
	}));

    const [selectedImages, setSelectedImages] = useState([]);
    const [productGalleryImage, setProductGalleryImage] = useState([]);
    //Code to remove selected images; Images not being removed from 
    // const removeImages = (item, e) => {
    //     e.preventDefault();
    //     setSelectedImages((selectedImages) =>
    //     selectedImages.filter((selectedImages) => selectedImages !== item));
    //     console.log('gallery images', productGalleryImage, 'files>>>>', selectedImages)
    // }
    
    const onSelectMultipleImages = useCallback( async (e)  => {
        const selectedFilesArray = Array.from(e.target.files)
        console.log('selected array', selectedFilesArray)
        selectedFilesArray.map((file) => {
            const reader = new FileReader();
            reader.readAsDataURL(file);
            setProductGalleryImage((productGalleryImage) =>[...productGalleryImage, file]);     
            reader.onloadend = () => {
                setSelectedImages((selectedImages) =>[...selectedImages, reader.result]);
            };
        })
    }, []);

    const onSelectFile = useCallback( async (e)  => {
        const file = e.target.files[0];
        const reader = new FileReader();
        reader.readAsDataURL(file);
        setProductImage(file)
        reader.onloadend = () => {
            setSelectedImage(reader.result);
        };
    }, []);

    const submitForm = (data) => {
        formData.append('product_image', productImage)
        formData.append('name', data.product_name);
        formData.append('description', data.description)
        formData.append('price', data.price)
        formData.append('sale_price', data.sale_price)
        formData.append('quantity', data.quantity)
        formData.append('category_id', data.category)
        formData.append('user_id', userId)
        Array.from(productGalleryImage).forEach(item => {
            formData.append('product_gallery_image', item)
        })

        const requestOptions = {
            headers: {
              'Content-type': 'multipart/form-data'
            }
        }
        axios.post(
            `${ROUTE.PRODUCTS_API}/products`,
            formData,
            requestOptions
        ).then(res => res)
        .then(data =>{
          if (data.status == 200 || data.status == 302) {
                successAlert(data)
            }
            else {
                errorAlert(data.message)
            }
        })
        .catch(err => errorAlert(err))
    }
    
    const successAlert = (response) => {
        return(
          swal({
              title: "Info!",
              text: response.data.message,
              icon: "success"
          }).then(function() {
            reset()
            setSelectedImage('')
            setSelectedImages('')
            setProductImage('')
            setProductGalleryImage('')
          })           
        )
    }

    const errorAlert = (error) => {
        return(
          swal({
              title: "Error!",
              text: error.message,
              icon: "error"
          })              
        )
    }
    const getCategories = () => {
        fetch(`${ROUTE.PRODUCTS_API}/categories`)
          .then((res) => res.json())
          .then((res) => {
            fetchCategories(res.results)
          })
    }

    useEffect(() => {
        getCategories()
    }, [])

    let categoryDropdown = ''
    categoryDropdown = categories.map((item, i) => {
        return (<option className="my-2 hover:bg-gray-50" key={i} value={item.id}> {item.name} </option>)
    }) 


    return (
        <div className="bg-gray-100">
            <div className="header bg-white h-16 px-10 py-8 border-b-2 border-gray-200 flex items-center justify-between">
                    <div className="flex items-center space-x-2 text-gray-400">
                    <span className="text-green-700 tracking-wider font-thin text-md"><Link to={ROUTE.ADMIN_DASHBOARD}>@@LinkToDashboard@@</Link></span>
                    <span>/</span>
                    <span className="tracking-wide text-md">
                        <span className="text-green-700 tracking-wider font-thin text-md"><Link to={ROUTE.ADMIN_PRODUCTS}>@@LinkToProducts@@</Link></span>
                    </span>
                    <span>/</span>
                    <span className="tracking-wide text-md">
                        <span className="text-base">@@PageTitle@@</span>
                    </span>
                    </div>
            </div>
            <div className="header my-3 h-12 px-10 py-8  flex items-center justify-between">
                <h1 className="font-medium text-2xl">@@PageTitle@@</h1>
                <Link to={ROUTE.ADMIN_PRODUCTS} className="focus:outline-none text-white m-4 p-3 font-semibold rounded-md bg-green-700 hover:bg-green-600 hover:shadow-lg transition-all duration-100"> <span><FaAngleLeft className="inline-block w-5 h-5"/>
                </span> @@LinkToProducts@@</Link>
            </div>
            <div className="flex flex-col mx-3 lg:flex-row">
                <form className="w-full lg:w-3/5 bg-white shadow-md p-6" encType="multipart/form-data">
                    <div className="flex flex-wrap -mx-3 mb-6">
                        <div className="w-full px-3 mb-6">
                            <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='product_name'>@@TableHead1@@</label>
                            <input className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d]" type='text' name="product_name" placeholder="Enter product Name"
                            {...register("product_name", { required: true})}
                             />
                            {errors.product_name && <small className="text-red-500 text-xs italic">Product name is required</small>}
                            {errors.product_name?.type === "maxLength" && <p style={{ color: "red" }}><small>Max characters should be 25 </small></p>}
                        </div>

                        <div className="w-full px-3 mb-6">
                            <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='category'>@@TableHead2@@</label>
                            <select className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d]" name="category" {...register("category", { required: true })}
                            >
                                <option value={''}>Select category</option>
                                { categoryDropdown }
                            </select>

                            {errors.category && <small className="text-red-500 text-xs italic">Select at least one category</small>}
                        </div>

                        <div className="w-full px-3 mb-6">
                            <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='price'>@@TableHead3@@</label>
                            <input className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d]" type='number' name="price" placeholder="Enter price" {...register("price", { required: true })}
                            />
                            {errors.price && <small className="text-red-500 text-xs italic">Price is required</small>}
                        </div>

                        <div className="w-full px-3 mb-6">
                            <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='sale_price'>@@TableHead4@@</label>
                            <input className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d]" type="number" inputMode="numeric" name="sale_price" placeholder="Enter sale price" {...register("sale_price")}
                            />
                        </div>

                        <div className="w-full px-3 mb-6">
                            <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='quantity'>@@TableHead5@@</label>
                            <input className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d]" inputMode="numeric" type='number' name="quantity" placeholder="Enter count in stock"
                            {...register("quantity", { required: true })}
                            />
                            {errors.quantity && <small className="text-red-500 text-xs italic">Count in stock is required</small>}
                        </div>
                        
                        <div className="w-full px-3 mb-6">
                            <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='description'>@@TableHead6@@</label>
                            <textarea className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d]" rows={5}  placeholder="Enter product description" name="description" {...register("description")} />
                            {errors.description && <small className="text-red-500 text-xs italic">Description is required</small>}
                        </div>
                        <div className="w-full mx-auto px-3 mb-12">
                            <label className="mx-auto cursor-pointer flex w-full max-w-lg flex-col items-center justify-center rounded-xl border-2 border-dashed border-green-400 bg-white p-6 text-center" htmlFor='product_image'>
                            <svg xmlns="http://www.w3.org/2000/svg" className="h-10 w-10 text-green-800" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="2">
                            <path strokeLinecap="round" strokeLinejoin="round" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
                            </svg>

                            <h2 className="mt-4 text-xl font-medium text-gray-700 tracking-wide">@@TableHead7@@</h2>

                            <p className="mt-2 text-gray-500 tracking-wide">Upload or drag & drop your file SVG, PNG, JPG or GIF. </p>

                            <input name="product_image" id="product_image" type="file" className="hidden" onChange={onSelectFile} accept="image/png, image/jpeg, image/webp"/>
                            </label>
                            {errors.product_image && <small className="text-red-500 text-xs italic">Product image is required</small>}
                        </div>
                        <div className="w-full flex justify-center mb-5">
                            {selectedImage &&
                                (
                                    <img src={selectedImage} className="w-32 h-32"/>
                                )

                            } 
                        </div>
                        <div className="w-full px-3 flex justify-end mb-5 text-green-500">
                            <p className="flex mx-4 "> <span> <FaPlus className="w-4 h-4 mr-1 inline-flex" /> </span>Add product gallery images</p>
                        </div>

                        <div className="w-full px-3 mb-6">
                        <label className="mx-auto cursor-pointer flex w-full max-w-lg flex-col items-center justify-center rounded-xl border-2 border-dashed border-green-400 bg-white p-6 text-center" htmlFor='product_gallery_images'>
                            <svg xmlns="http://www.w3.org/2000/svg" className="h-10 w-10 text-green-800" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="2">
                            <path strokeLinecap="round" strokeLinejoin="round" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
                            </svg>

                            <h2 className="mt-4 text-xl font-medium text-gray-700 tracking-wide">Product gallery images</h2>

                            <p className="mt-2 text-gray-500 tracking-wide">Upload or drag multiple images SVG, PNG, JPG or GIF. </p>

                            <input type="file" className="hidden" name="product_gallery_images" id="product_gallery_images" onChange={onSelectMultipleImages} multiple accept="image/png, image/jpeg, image/webp"/>
                            </label>
                        </div>
                        <div className="overflow-x-auto flex justify-center mb-5 mx-auto">
                            {selectedImages &&
                                selectedImages.map((image, index) => {
                                    return (
                                            <>
                                                <img key={index} src={image} className="w-32 h-32 relative"/>
                                                {/* <span className="relative"><button className="text-red-500 font-weight-bolder top-0" onClick={(e)=>removeImages(image, e)}><FaTimes/></button></span>   */}
                                            </>
                                    )                                    
                                })
                            }
                        </div>
                        <div className="w-full px-3 mb-6">
                            <button className="appearance-none w-full block bg-green-700 text-gray-100 font-bold border border-gray-200 rounded-lg py-3 px-3 leading-tight hover:bg-green-600 focus:outline-none focus:bg-white focus:border-gray-500"
                            onClick={handleSubmit(submitForm)}>Add Product</button>
                        </div>
                    </div>
                </form>          
            </div>        
        </div>
    )
}
export default @@PageName@@;
 """
 layouts["layout_admin_add_product"] = layout_admin_add_product


 layout_admin_edit_product ="""
import React, { useEffect, useState, useCallback } from 'react';
@@Imports@@
const @@PageName@@ = () => {
  const { id } = useParams();
    const [categories, fetchCategories] = useState([]);
    const [productId, setProductId] = useState('');
    const [productName, setProductName] = useState('');
    const [productCategoryId, setProductCategoryId] = useState('');
    const [productPrice, setProductPrice] = useState('');
    const [productSalePrice, setProductSalePrice] = useState('');
    const [productQuantity, setProductQuantity] = useState('');
    const [productDescription, setProductDescription] = useState('');
    const [productImage, setProductImage] = useState('');
    const [selectedImage, setSelectedImage] = useState();
    const [newProductImage, setNewProductImage] = useState();
    let formData = new FormData();

    const [selectedImages, setSelectedImages] = useState([]);
    const [productGalleryImage, setProductGalleryImage] = useState([]);

    const onSelectMultipleImages = useCallback( async (e)  => {
        const selectedFilesArray = Array.from(e.target.files)
        selectedFilesArray.map((file) => {
            const reader = new FileReader();
            reader.readAsDataURL(file);
            setProductGalleryImage((productGalleryImage) =>[...productGalleryImage, file]);     
            reader.onloadend = () => {
                setSelectedImages((selectedImages) =>[...selectedImages, reader.result]);
            };
        })
    }, []);

    const {register, handleSubmit, reset, formState: { errors } } = useForm();
    const getCategories = () => {
        fetch(`${ROUTE.PRODUCTS_API}/categories`)
          .then((res) => res.json())
          .then((res) => {
            fetchCategories(res.results)
          })
    }

    const removeImageFromDB = (image, e) => {
        e.preventDefault();
        const requestOptions = {
            headers: {
              'Content-type': 'application/json'
            }
        }
        axios.delete(
            `${ROUTE.PRODUCTS_API}/products/${image}/gallery`,
            requestOptions
        ).then(res => res)
        .then(data =>{
          successAlert(data)
        })
        .catch(err => errorAlert(err))
        getData();
    }
    const getData = () => {
        fetch(`${ROUTE.PRODUCTS_API}/products/${id}`)
          .then((res) => res.json())
          .then((res) => {
            setProductId(res.data[0].id)
            setProductName(res.data[0].name)
            setProductPrice(res.data[0].price)
            setProductSalePrice(res.data[0].sale_price)
            setProductQuantity(res.data[0].quantity)
            setProductDescription(res.data[0].description)
            setProductImage(res.data[0].image_path)
            setProductCategoryId(res.data[0].product_category_id)
            res.data[0].products_gallery.map(item => {
                setProductGalleryImage((productGalleryImage) =>[...productGalleryImage, item])
            })
          })
    }

    useEffect(() => {
        getCategories()
        getData()
    }, [])

    const onSelectFile = useCallback( async (e)  => {
        const file = e.target.files[0];
        const reader = new FileReader();
        reader.readAsDataURL(file);
        setNewProductImage(file)
        reader.onloadend = () => {
            setSelectedImage(reader.result);
        };
    }, []);

    const submitForm = (data) => {
        
        formData.append('product_image', newProductImage)
        formData.append('name', data.name);
        formData.append('description', data.description)
        formData.append('price', data.price)
        formData.append('sale_price', data.sale_price)
        formData.append('quantity', data.quantity)
        formData.append('category_id', data.category)
        Array.from(productGalleryImage).forEach(item => {
            formData.append('product_gallery_image', item)
        })
        const requestOptions = {
            method: "POST",
            headers: {
              'Content-type': 'multipart/form-data'
            }
        }
        axios.put(
            `${ROUTE.PRODUCTS_API}/products/${productId}`,
            formData,
            requestOptions
        ).then(res => res)
        .then(data =>{
          successAlert(data)
        })
        .catch(err => errorAlert(err))
      reset()
      setSelectedImage('');
    }

    const handleCategoryChange = (e) => {
        setProductCategoryId(e.target.value);
      };

    const successAlert = (response) => {
        return(
          swal({
              title: "Info!",
              text: response.data.message,
              icon: "success"
          }).then(function () {
                window.location.reload()
          })
        )
    }
    const errorAlert = (error) => {
        return(
          swal({
              title: "Error!",
              text: error,
              icon: "error"
          }).then(function () {
            window.location.reload()
          })          
        )
    }

    let categoryDropdown = categories.map((item, i) => {
        return (<option className="my-2 hover:bg-gray-50" key={i} value={item.id}> {item.name} </option>)
    }) 

  return (
    <div className="bg-gray-100">
        <div className="header bg-white h-16 px-10 py-8 border-b-2 border-gray-200 flex items-center justify-between">
                <div className="flex items-center space-x-2 text-gray-400">
                <span className="text-green-700 tracking-wider font-thin text-md"><Link to={ROUTE.ADMIN_DASHBOARD}>@@LinkToDashboard@@</Link></span>
                <span>/</span>
                <span className="tracking-wide text-md">
                    <span className="text-green-700 tracking-wider font-thin text-md"><Link to={ROUTE.ADMIN_PRODUCTS}>@@LinkToProducts@@</Link></span>
                </span>
                <span>/</span>
                <span className="tracking-wide text-md">
                    <span className="text-base">@@PageTitle@@</span>
                </span>
                </div>
        </div>
        <div className="header my-3 h-12 px-4 lg:px-10 py-8  flex items-center justify-between">
            <h1 className="font-medium text-2xl">@@PageTitle@@</h1>
            <Link to={ROUTE.ADMIN_PRODUCTS} className="focus:outline-none text-white m-4 p-3 font-semibold rounded-md bg-green-700 hover:bg-green-600 hover:shadow-lg transition-all duration-100"> <span><FaAngleLeft className="inline-block w-5 h-5"/>
            </span> Back to products</Link>
        </div>
        <div className="flex flex-col mx-3 lg:flex-row">
            <form className="w-full lg:w-3/5 bg-white shadow-md p-6">
                <div className="flex flex-wrap -mx-3 mb-6">
                    <div className="w-full px-3 mb-6">
                        <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='name'>@@Input1Label@@Product Name</label>
                        <input className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d] invalid:border-pink-500 invalid:text-pink-600 focus:invalid:border-pink-500 focus:invalid:ring-pink-500" type='text' name="name" placeholder="Enter product Name"
                        defaultValue={productName} {...register("name", { required: true })} required onChange={(e) => setProductName(e.target.value)} />
                        {errors.product_name && <small className="text-red-500 text-xs italic">Product name is required</small>}
                    </div>

                    <div className="w-full px-3 mb-6">
                        <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='category'>@@Input2Label@@</label>
                        <select className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d] invalid:border-pink-500 invalid:text-pink-600 focus:invalid:border-pink-500 focus:invalid:ring-pink-500" name="category"
                        onChange={handleCategoryChange}
                        defaultValue={productCategoryId || ""} {...register("category", { required: true })}
                        required>
                            { categoryDropdown }
                        </select>

                        {errors.category && <small className="text-red-500 text-xs italic">Select at least one category</small>}
                    </div>

                    <div className="w-full px-3 mb-6">
                        <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='price'>@@Input3Label@@</label>
                        <input className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d]" type='text' name="price" placeholder="Enter price"
                        value={productPrice} {...register("price", { required: true })} required onChange={(e) => setProductPrice(e.target.value)} />
                         {errors.price && <small className="text-red-500 text-xs italic">Price is required</small>}
                    </div>

                    <div className="w-full px-3 mb-6">
                        <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='sale_price'>@@Input4Label@@</label>
                        <input className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d]" type='text' name="sale_price" placeholder="Enter price"
                        value={productSalePrice} {...register("sale_price")} onChange={(e) => setProductSalePrice(e.target.value)} />
                    </div>

                    <div className="w-full px-3 mb-6">
                        <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='quantity'>@@Input5Label@@</label>
                        <input className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d]" type='number' name="quantity" placeholder="Enter count in stock"
                        required value={productQuantity} {...register("quantity", { required: true })} onChange={(e) => setProductQuantity(e.target.value)} />
                        {errors.quantity && <small className="text-red-500 text-xs italic">Count in stock is required</small>}
                    </div>
                    
                    <div className="w-full px-3 mb-6">
                        <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='description'>@@Input6Label@@</label>
                        <textarea className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d]" rows={5}  placeholder="Enter product description" name="description" value={productDescription} {...register("description", { required: true })} onChange={(e) => setProductDescription(e.target.value)} />
                        {errors.description && <small className="text-red-500 text-xs italic">Description is required</small>}
                    </div>
                    <div className="w-full px-3 mb-12">
                        <label className="mx-auto cursor-pointer flex w-full max-w-lg flex-col items-center justify-center rounded-xl border-2 border-dashed border-green-400 bg-white p-6 text-center" htmlFor='product_image'>
                        <svg xmlns="http://www.w3.org/2000/svg" className="h-10 w-10 text-green-800" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="2">
                        <path strokeLinecap="round" strokeLinejoin="round" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
                        </svg>

                        <h2 className="mt-4 text-xl font-medium text-gray-700 tracking-wide">@@Input7Label@@</h2>

                        <p className="mt-2 text-gray-500 tracking-wide">Upload or drag & drop your file SVG, PNG, JPG or GIF. </p>

                        <input name="product_image" id="product_image" type="file" className="hidden" onChange={onSelectFile} accept="image/png, image/jpeg, image/webp"/>
                        </label>
                        {errors.product_image && <small className="text-red-500 text-xs italic">Product image is required</small>}
                    </div>
                    {errors.product_image && <small className="text-red-500 text-xs italic">Product image is required</small>}

                    <div className="w-full mx-12 flex justify-center mb-5">
                        {productImage &&
                            (
                                <img src={`${CONSTANT.IMAGE_STORE}/${productImage}`} className={selectedImage ? "hidden" : `w-32 h-32 $`}/>
                            )
                        }
                        {selectedImage &&
                            (
                                <img src={selectedImage} className="w-32 h-32"/>
                            )

                        } 
                    </div>
                    <div className="w-full px-3 flex justify-end mb-5 text-green-500">
                        <p className="flex mx-4 "> Product gallery images</p>
                    </div>

                    <div className="w-full px-3 mb-6">
                    <label className="mx-auto cursor-pointer flex w-full max-w-lg flex-col items-center justify-center rounded-xl border-2 border-dashed border-green-400 bg-white p-6 text-center" htmlFor='product_gallery_images'>
                        <svg xmlns="http://www.w3.org/2000/svg" className="h-10 w-10 text-green-800" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="2">
                        <path strokeLinecap="round" strokeLinejoin="round" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
                        </svg>

                        <h2 className="mt-4 text-xl font-medium text-gray-700 tracking-wide">Product gallery images</h2>

                        <p className="mt-2 text-gray-500 tracking-wide">Upload or drag multiple images SVG, PNG, JPG or GIF. </p>

                        <input type="file" className="hidden" name="product_gallery_images" id="product_gallery_images" onChange={onSelectMultipleImages} multiple accept="image/png, image/jpeg, image/webp"/>
                        </label>
                    </div>
                    <div className="overflow-x-auto flex justify-center mb-5 mx-auto">
                        {productGalleryImage &&
                            
                            productGalleryImage.map((image, index) => {
                                return (
                                    <>
                                        <img key={index}  src={`${CONSTANT.IMAGE_STORE}/${image.path}`} className="w-32 h-32"/>
                                        <span className="relative"><button className="text-red-500 font-weight-bolder top-0" onClick={(e) => removeImageFromDB(image.id, e)}><FaTimes/></button></span>
                                    </>
                                )
                            })
                        }
                        {selectedImages &&
                            selectedImages.map((image, index) => {
                                return (
                                    <>
                                        <img key={index} src={image} className="w-32 h-32 relative"/>
                                    </>
                                )                                    
                            })
                        }
                    </div>
                    <div className="w-full px-3 mb-6">
                        <button className="appearance-none w-full block bg-green-700 text-gray-100 font-bold border border-gray-200 rounded-lg py-3 px-3 leading-tight hover:bg-green-600 focus:outline-none focus:bg-white focus:border-gray-500"
                        onClick={handleSubmit(submitForm)}
                        >Update Product</button>
                    </div>
                </div>
            </form>          
        </div>        
    </div>
  )
}
export default @@PageName@@;
 """
 layouts["layout_admin_edit_product"] = layout_admin_edit_product
 

 layout_admin_products ="""
import React, {useEffect, useState } from 'react';
@@Imports@@
const @@PageName@@ = () => {
  const [loading, setLoading] = useState(false);
    const [products, fetchProducts] = useState([]);
    const getData = () => {
      setLoading(true)
      fetch(`${ROUTE.PRODUCTS_API}/products`)
        .then((res) => res.json())
        .then((res) => {
          fetchProducts(res.results)
          setLoading(false)
        })
    }

    useEffect(() => {
        getData()
    }, [])

    let productList;
    if(products.length > 0){
      productList = products.map((item, i) => {
            return (
                <tr key={i}>
                    <td className="p-2">
                        <input type="checkbox" className="w-5 h-5" />
                    </td>
                    <td className="p-2 w-8">
                    <img src={`${CONSTANT.IMAGE_STORE}/${item.image_path}`} className="w-8 h-8 mx-auto overflow-hidden" alt={item.name} />
                    </td>
                    <td className="p-2 text-left">
                        {item.name}
                    </td>
                    <td className="p-2">
                        {item.sku}
                    </td>
                    <td className="p-2">
                      <span className={
                        item.sale_price ? "line-through mr-1" : "" }>{ item.price }</span> { item.sale_price ? item.sale_price : ''}
                        
                    </td>
                    <td className="p-2">
                        { item.product_category }
                    </td>
                    <td className="p-2">
                        {item.featured == 1 ?
                        <span><MdStar className="mx-auto h-6 w-6 text-green-600 text-center" /></span>
                        :
                        <span><MdStarOutline className="mx-auto h-6 w-6 text-green-600 text-center" /></span>}
                    </td>
                    <td className="">
                        {item.is_verified == 1 ?
                        <span className="rounded-md text-white bg-green-600 p-1 flex justify-center items-center text-center">Verified</span>
                        :
                        <span className="rounded-md  text-white bg-red-600 p-1 flex justify-center items-center text-center">Unverified</span>}
                    </td>
                    <td className="p-2">
                      <div className="flex justify-center">
                            <Link to={`${ROUTE.ADMIN_VIEW_PRODUCT}/${item.id}`} className="rounded-md hover:bg-gray-100 text-green-600 p-2 flex justify-between items-center">
                                <span><MdInfoOutline className="w-4 h-4 mr-1"/>
                                    </span> View
                            </Link>
                        </div>
                    </td>
                </tr>
            )
        }

        );
    } else {
      productList =  (<tr className=''><td colSpan={10} className="">
        <div className="flex flex-col my-4 space-y-3 justify-center items-center text-xl font-medium tracking-wide py-4 text-green-700 text-center">
            <MdOutlineProductionQuantityLimits className="w-16 h-16" />
            <p>No products added yet</p>
        </div>
        </td></tr>)
        
    }

    let productsLoading = (
      <>
          <tr className="mx-auto">
              <td className="p-2">
                  <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                  </div>
              </td>
              <td className="p-2">
                  <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                  </div>
              </td>
              <td className="p-2">
                  <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                  </div>
              </td>
              <td className="p-2">
                  <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                  </div>
              </td>
              <td className="p-2">
                  <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative">
                  </div>
              </td>
              <td className="p-2">
                  <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                  </div>
              </td>
              <td className="p-2">
                  <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                  </div>
              </td>
              <td className="p-2">
                  <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                  </div>
              </td>
              <td className="p-2">
                  <div className="flex justify-center">
                      <div data-placeholder className="w-1/2 h-8 bg-gray-200 overflow-hidden relative">
                      </div>
                  </div>    
              </td>
          </tr>
          <tr className="mx-auto">
              <td className="p-2">
                  <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                  </div>
              </td>
              <td className="p-2">
                  <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                  </div>
              </td>
              <td className="p-2">
                  <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                  </div>
              </td>
              <td className="p-2">
                  <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                  </div>
              </td>
              <td className="p-2">
                  <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative">
                  </div>
              </td>
              <td className="p-2">
                  <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                  </div>
              </td>
              <td className="p-2">
                  <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                  </div>
              </td>
              <td className="p-2">
                  <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                  </div>
              </td>              
              <td className="p-2">
                  <div className="flex justify-center">
                      <div data-placeholder className="w-1/2 h-8 bg-gray-200 overflow-hidden relative">
                      </div>
                  </div>    
              </td>
          </tr>
          <tr className="mx-auto">
              <td className="p-2">
                  <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                  </div>
              </td>
              <td className="p-2">
                  <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                  </div>
              </td>
              <td className="p-2">
                  <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                  </div>
              </td>
              <td className="p-2">
                  <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                  </div>
              </td>
              <td className="p-2">
                  <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative">
                  </div>
              </td>
              <td className="p-2">
                  <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                  </div>
              </td>
              <td className="p-2">
                  <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                  </div>
              </td>
              <td className="p-2">
                  <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                  </div>
              </td>
              <td className="p-2">
                  <div className="flex justify-center">
                      <div data-placeholder className="w-1/2 h-8 bg-gray-200 overflow-hidden relative">
                      </div>
                  </div>    
              </td>
          </tr>
      </>
    )

  return (
    <div className="bg-gray-100">
        <div className="header bg-white h-16 px-10 py-8 border-b-2 border-gray-200 flex items-center justify-between">
              <div className="flex items-center space-x-2 text-gray-400">
                <span className="text-green-700 tracking-wider font-thin text-md"><Link to={ROUTE.ADMIN_DASHBOARD}>@@LinkToDashboard@@</Link></span>
                <span>/</span>
                <span className="tracking-wide text-md">
                    <span className="text-base">@@PageName@@</span>
                </span>
                <span>/</span>
              </div>
        </div>
        <div className="header my-3 h-12 px-10 py-8  flex items-center justify-between">
            <h1 className="font-medium text-2xl">All @@PageName@@</h1>
        </div>
        <div className="flex flex-col mx-3 lg:flex-row">
            <div className="w-full m-4 bg-white shadow-lg text-lg rounded-sm border border-gray-200">
                <div className="overflow-x-auto rounded-lg  p-3">
                    <table className="w-full whitespace-nowrap">
                        <thead className="text-sm font-semibold uppercase text-gray-800 bg-gray-50">
                            <tr className="font-semibold text-center">
                                <th><input type="checkbox" className="w-5 h-5"/></th>
                                <th className='w-12'><svg xmlns="http://www.w3.org/2000/svg" className="fill-current w-5 h-5 mx-auto" ><path d="M6 22h12a2 2 0 0 0 2-2V8l-6-6H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2zm7-18 5 5h-5V4zm-4.5 7a1.5 1.5 0 1 1-.001 3.001A1.5 1.5 0 0 1 8.5 11zm.5 5 1.597 1.363L13 13l4 6H7l2-3z"></path></svg></th>
                                <th className="p-2 text-left">@@TableHead1@@
                                </th>
                                <th className="p-2">@@TableHead2@@
                                </th>
                                <th className="p-2">@@TableHead3@@
                                </th>
                                <th className="p-2">@@TableHead4@@
                                </th>
                                <th className="p-2">@@TableHead5@@
                                </th>
                                <th className="p-2">@@TableHead6@@
                                </th>
                                <th className="p-2">@@TableHead7@@
                                </th>
                            </tr>
                        </thead>

                        <tbody className="text-sm divide-y divide-gray-100 text-center">
                          { loading
                            ? productsLoading
                            : productList }
                        </tbody>
                    </table>
                </div>
            </div>
            
        </div>        
    </div>
  )
}
export default @@PageName@@;
 """
 layouts["layout_admin_products"] = layout_admin_products


 layout_admin_verify_product ="""
import React, {useEffect, useState, useCallback} from 'react';
@@Imports@@
const @@PageName@@ = () => {
  const [loading, setLoading] = useState(false);
    const [products, fetchProducts] = useState([]);

    const getData = () => {
        setLoading(true)
        fetch(`${ROUTE.PRODUCTS_API}/products/unverified`)
          .then((res) => res.json())
          .then((res) => {
            fetchProducts(res.results)
            setLoading(false)
          })
      }
  
    useEffect(() => {
        getData()
    }, [])

    let productsLoading = (
        <>
            <tr className="mx-auto">
                <td className="p-2">
                    <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                    </div>
                </td>
                <td className="p-2">
                    <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                    </div>
                </td>
                <td className="p-2">
                    <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                    </div>
                </td>
                <td className="p-2">
                    <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                    </div>
                </td>
                <td className="p-2">
                    <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative">
                    </div>
                </td>
                <td className="p-2">
                    <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                    </div>
                </td>
                <td className="p-2">
                    <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                    </div>
                </td>
                <td className="p-2">
                    <div className="flex justify-center">
                        <div data-placeholder className="w-1/2 h-8 bg-gray-200 overflow-hidden relative">
                        </div>
                    </div>    
                </td>
            </tr>
            <tr className="mx-auto">
                <td className="p-2">
                    <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                    </div>
                </td>
                <td className="p-2">
                    <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                    </div>
                </td>
                <td className="p-2">
                    <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                    </div>
                </td>
                <td className="p-2">
                    <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                    </div>
                </td>
                <td className="p-2">
                    <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative">
                    </div>
                </td>
                <td className="p-2">
                    <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                    </div>
                </td>
                <td className="p-2">
                    <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                    </div>
                </td>
                <td className="p-2">
                    <div className="flex justify-center">
                        <div data-placeholder className="w-1/2 h-8 bg-gray-200 overflow-hidden relative">
                        </div>
                    </div>    
                </td>
            </tr>
            <tr className="mx-auto">
                <td className="p-2">
                    <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                    </div>
                </td>
                <td className="p-2">
                    <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                    </div>
                </td>
                <td className="p-2">
                    <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                    </div>
                </td>
                <td className="p-2">
                    <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                    </div>
                </td>
                <td className="p-2">
                    <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative">
                    </div>
                </td>
                <td className="p-2">
                    <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                    </div>
                </td>
                <td className="p-2">
                    <div data-placeholder className="w-full h-8 bg-gray-200 overflow-hidden relative mx-auto">
                    </div>
                </td>
                <td className="p-2">
                    <div className="flex justify-center">
                        <div data-placeholder className="w-1/2 h-8 bg-gray-200 overflow-hidden relative">
                        </div>
                    </div>    
                </td>
            </tr>
        </>
    )

    const verifyProduct = useCallback( async (id)  => {
    axios.put(
        `${ROUTE.PRODUCTS_API}/products/${id}/verify`,{
            method : 'PUT',
            body : JSON.stringify({
                id : id
            }),
            headers: {
                'Content-type': 'application/json'
            }
        })
        .then(res => res)
        .then(data =>{
          successAlert(data)
        })
        .catch(err => errorAlert(err)
        )
    }, []);

    const verifyAll = useCallback( async ()  => {
        axios.put(
            `${ROUTE.PRODUCTS_API}/products/verify/all`,{
                method : 'PUT',
                headers: {
                    'Content-type': 'application/json'
                }
            })
            .then(res => res)
            .then(data =>{
                successAlert(data)
            })
            .catch(err => errorAlert(err)
            )
        }, []);

        const successAlert = (response) => {
            return(
              swal({
                  title: "Info!",
                  text: response.data.message,
                  icon: "success"
              }).then(function () {
                    getData()
              })
            )
        }
        const errorAlert = (error) => {
            return(
              swal({
                  title: "Error!",
                  text: error,
                  icon: "error"
              }).then(function () {
                getData()
              })          
            )
        }

    let productList;
    if(products.length > 0){
      productList = products.map((item, i) => {
            return (
                <tr key={i}>
                    <td className="p-2">
                        <input type="checkbox" className="w-5 h-5" />
                    </td>
                    <td className="p-2 w-8">
                    <img src={`${CONSTANT.IMAGE_STORE}/${item.image_path}`} className="w-8 h-8 mx-auto overflow-hidden" alt={item.name} />
                    </td>
                    <td className="p-2">
                        {item.name}
                    </td>
                    <td className="p-2">
                        {item.sku}
                    </td>
                    <td className="p-2">
                        {item.description}
                    </td>
                    <td className="p-2">
                      <span className={
                        item.sale_price ? "line-through mr-1" : "" }>{ item.price }</span> { item.sale_price ? item.sale_price : ''}
                        
                    </td>
                    <td className="p-2">
                        { item.product_category }
                    </td>
                    <td className="p-2">
                      <div className="flex justify-center">
                          <Link to={`${ROUTE.ADMIN_VIEW_PRODUCT}/${item.id}`} className="rounded-md hover:bg-gray-100 text-green-600 p-2 flex justify-between items-center">
                              <span><MdInfoOutline className="w-4 h-4 mr-1"/>
                                </span> View
                          </Link>
                          <button className="rounded-md text-green-600 hover:bg-gray-200 p-2 flex justify-between items-center" value={item.id} onClick={() => verifyProduct(item.id)}>
                              <span><ImCheckmark className="w-4 h-4 mr-1" /></span> Verify
                          </button>
                        </div>
                    </td>
                </tr>
            )
        }

        );
    } else {
      productList =  (<tr className=''><td colSpan={8} className="">
        <div className="flex flex-col my-4 space-y-3 justify-center items-center text-xl font-medium tracking-wide py-4 text-green-700 text-center">
            <MdOutlineProductionQuantityLimits className="w-16 h-16" />
            <p>No pending products for verification</p>
        </div>
        </td></tr>)
        
    }
    
    return (
        <div className="bg-gray-100">
            <div className="header bg-white h-16 px-10 py-8 border-b-2 border-gray-200 flex items-center justify-between">
                <div className="flex items-center space-x-2 text-gray-400">
                    <span className="text-green-700 tracking-wider font-thin text-md"><Link to={ROUTE.ADMIN_DASHBOARD}>@@LinkToDashboard@@</Link></span>
                    <span>/</span>
                    <span className="text-green-700 tracking-wider font-thin text-md"><Link to={ROUTE.ADMIN_PRODUCTS}>@@LinkToProducts@@</Link></span>
                    <span>/</span>
                    <span className="tracking-wide text-md">
                        <span className="text-base">@@PageTitle@@</span>
                    </span>
                </div>
            </div>
            <div className="header my-3 h-12 px-10 py-8  flex items-center justify-between">
                <h1 className="font-medium text-2xl">@@PageTitle@@</h1>
                <button onClick={() => verifyAll()} className="focus:outline-none text-white m-4 p-3 font-semibold rounded-md bg-green-700 hover:bg-green-600 hover:shadow-lg transition-all duration-100"><span><ImCheckmark className="inline-block w-5 h-5"/></span>Verify all</button>
            </div>
            <div className="flex flex-col mx-3 lg:flex-row">
                <div className="w-full m-4 bg-white shadow-lg text-lg rounded-sm border border-gray-200">
                    <div className="overflow-x-auto rounded-lg  p-3">
                        {/* Display products table */}
                        <table className="w-full whitespace-nowrap">
                            <thead className="text-sm font-semibold uppercase text-gray-800 bg-gray-50">
                                <tr className="font-semibold text-center">
                                    <th><input type="checkbox" className="w-5 h-5"/></th>
                                    <th className='w-12'><svg xmlns="http://www.w3.org/2000/svg" className="fill-current w-5 h-5 mx-auto" ><path d="M6 22h12a2 2 0 0 0 2-2V8l-6-6H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2zm7-18 5 5h-5V4zm-4.5 7a1.5 1.5 0 1 1-.001 3.001A1.5 1.5 0 0 1 8.5 11zm.5 5 1.597 1.363L13 13l4 6H7l2-3z"></path></svg></th>
                                    <th className="p-2">@@TableHead1@@
                                    </th>
                                    <th className="p-2">@@TableHead2@@
                                    </th>
                                    <th className="p-2">@@TableHead3@@
                                    </th>
                                    <th className="p-2">@@TableHead4@@
                                    </th>
                                    <th className="p-2">@@TableHead5@@
                                    </th>
                                    <th className="p-2">@@TableHead6@@
                                    </th>
                                </tr>
                            </thead>

                            <tbody className="text-sm divide-y divide-gray-100 text-center">
                            { loading
                                ? productsLoading
                                : productList }
                            </tbody>
                        </table>
                    </div>
                </div>                
            </div>        
        </div>
    )
}
export default @@PageName@@;
 """
 layouts["layout_admin_verify_product"] = layout_admin_verify_product


 layout_admin_view_product_details ="""
import React, { useEffect, useState, useCallback } from 'react';
@@Imports@@
const @@PageName@@ = () => {
  const { id } = useParams();
    const [productName, setProductName] = useState('');
    const [productCategory, setProductCategory] = useState('');
    const [productPrice, setProductPrice] = useState('');
    const [productSalePrice, setProductSalePrice] = useState('');
    const [productQuantity, setProductQuantity] = useState('');
    const [productDescription, setProductDescription] = useState('');
    const [productImage, setProductImage] = useState('');
    const [productFeatured, setProductFeatured] = useState('');
    const [productVerified, setProductVerified] = useState('');
    const [productGalleryImage, setProductGalleryImage] = useState([]);

    const getData = () => {
        fetch(`${ROUTE.PRODUCTS_API}/products/${id}`)
          .then((res) => res.json())
          .then((res) => {
            console.log(res.data[0])
            setProductVerified(res.data[0].is_verified)
            setProductFeatured(res.data[0].featured)
            setProductName(res.data[0].name)
            setProductPrice(res.data[0].price)
            setProductSalePrice(res.data[0].sale_price)
            setProductQuantity(res.data[0].quantity)
            setProductDescription(res.data[0].description)
            setProductImage(res.data[0].image_path)
            setProductCategory(res.data[0].product_category)
            res.data[0].products_gallery.map(item => {
                setProductGalleryImage((productGalleryImage) =>[...productGalleryImage, item])
            })
          })
    }

    useEffect(() => {
        getData()
    }, [])

    const featureProduct = useCallback( async (id, e)  => {
        e.preventDefault();
        axios.put(
            `${ROUTE.PRODUCTS_API}/products/${id}/feature`,{
                method : 'PUT',
                body : JSON.stringify({
                    id : id
                }),
                headers: {
                    'Content-type': 'application/json'
                }
            })
            .then(res => res)
            .then(data =>{
              successAlert(data)
            })
            .catch(err => errorAlert(err)
            )
    }, []);

    const unfeatureProduct = useCallback( async (id, e)  => {
        e.preventDefault();
        await axios.put(
            `${ROUTE.PRODUCTS_API}/products/${id}/unfeature`,{
                method : 'PUT',
                body : JSON.stringify({
                    id : id
                }),
                headers: {
                    'Content-type': 'application/json'
                }
            })
            .then(res => res)
            .then(data =>{
              successAlert(data)
            })
            .catch(err => errorAlert(err)
            )
    }, []);

    const verifyProduct = useCallback( async (id, e)  => {
        e.preventDefault();
        await axios.put(
            `${ROUTE.PRODUCTS_API}/products/${id}/verify`,{
                method : 'PUT',
                body : JSON.stringify({
                    id : id
                }),
                headers: {
                    'Content-type': 'application/json'
                }
            })
            .then(res => res)
            .then(data =>{
              successAlert(data)
            })
            .catch(err => errorAlert(err)
            )
    }, []);
    
    const unverifyProduct = useCallback( async (id, e)  => {
        e.preventDefault();
        await axios.put(
            `${ROUTE.PRODUCTS_API}/products/${id}/unverify`,{
                method : 'PUT',
                body : JSON.stringify({
                    id : id
                }),
                headers: {
                    'Content-type': 'application/json'
                }
            })
            .then(res => res)
            .then(data =>{
                successAlert(data)
            })
            .catch(err => errorAlert(err)
            )
    }, []);

    const successAlert = (response) => {
        return(
            swal({
                title: "Info!",
                text: response.data.message,
                icon: "success"
            }).then(function () {
                window.location.reload()
            })
        )
    }
    const errorAlert = (error) => {
        return(
            swal({
                title: "Error!",
                text: error,
                icon: "error"
            }).then(function () {
                window.location.reload()
            })          
        )
    }

  return (
    <div className="bg-gray-100">
        <div className="header bg-white h-16 px-10 py-8 border-b-2 border-gray-200 flex items-center justify-between">
                <div className="flex items-center space-x-2 text-gray-400">
                <span className="text-green-700 tracking-wider font-thin text-md"><Link to={ROUTE.ADMIN_DASHBOARD}>@@LinkToDashboard@@</Link></span>
                <span>/</span>
                <span className="tracking-wide text-md">
                    <span className="text-green-700 tracking-wider font-thin text-md"><Link to={ROUTE.ADMIN_PRODUCTS}>@@LinkToProducts@@</Link></span>
                </span>
                <span>/</span>
                <span className="tracking-wide text-md">
                    <span className="text-base">@@PageTitle@@</span>
                </span>
                </div>
        </div>
        <div className="header my-3 h-12 px-4 lg:px-10 py-8  flex items-center justify-between">
            <h1 className="font-medium text-2xl">@@PageTitle@@</h1>
            <Link className="focus:outline-none text-white m-4 p-3 font-semibold rounded-md bg-green-700 hover:bg-green-600 hover:shadow-lg transition-all duration-100" to={ROUTE.ADMIN_PRODUCTS}><span><FaAngleLeft className="inline-block w-5 h-5"/>
            </span> @@LinkToProducts@@</Link>
        </div>
        <div className="flex mx-3 justify-center">
            <div className="w-full lg:w-4/5 bg-white shadow-md p-6">
                <div className="flex py-5 items-center justify-between">
                    {productVerified == 1 ?
                        <button className="rounded-md text-white bg-red-600 p-2 flex justify-between items-center" value={id} onClick={(e) => unverifyProduct(id, e)}>
                              <span><FaTimes className="w-4 h-4 mr-1" /></span> Unverify
                        </button>
                        :
                        <button className="rounded-md text-white bg-green-600 p-2 flex justify-between items-center" value={id} onClick={(e) => verifyProduct(id, e)}>
                              <span><FaCheck className="w-4 h-4 mr-1" /></span> Verify
                        </button>
                    }
                    {productVerified == 1 ?
                        productFeatured == 1 ?
                        <button className="rounded-md text-white bg-red-600 p-2 flex justify-center items-center text-center" value={id} onClick={(e) => unfeatureProduct(id, e)}>
                              <span><FaTimes className="w-4 h-4 mr-1" /></span> Unfeature
                        </button>
                        :
                        <button className="rounded-md text-white bg-green-600 p-2 flex justify-between items-center" value={id} onClick={(e) => featureProduct(id, e)}>
                              <span><FaStar className="w-4 h-4 mr-1" /></span> Feature Product
                        </button>
                        : ''
                        
                    }
                </div>
                <div className="flex flex-wrap -mx-3 mb-6">
                    <div className="w-full px-3 mb-6">
                        <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='name'>@@Input1Label@@</label>
                        <input className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d] invalid:border-pink-500 invalid:text-pink-600 focus:invalid:border-pink-500 focus:invalid:ring-pink-500" type='text' disabled
                        defaultValue={productName}/>
                    </div>

                    <div className="w-full px-3 mb-6">
                        <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='name'>@@Input2Label@@</label>
                        <input className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d] invalid:border-pink-500 invalid:text-pink-600 focus:invalid:border-pink-500 focus:invalid:ring-pink-500" type='text' disabled
                        defaultValue={productCategory}/>
                    </div>

                    <div className="w-full px-3 mb-6">
                        <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='price'>@@Input3Label@@</label>
                        <input className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d]" type='text' disabled
                        value={productPrice}/>
                    </div>

                    <div className="w-full px-3 mb-6">
                        <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='sale_price'>@@Input4Label@@</label>
                        <input className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d]" type='text' disabled
                        value={productSalePrice} />
                    </div>

                    <div className="w-full px-3 mb-6">
                        <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='quantity'>@@Input5Label@@</label>
                        <input className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d]" type='number' disabled
                        required value={productQuantity}/>
                    </div>
                    
                    <div className="w-full px-3 mb-6">
                        <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='description'>@@Input6Label@@</label>
                        <textarea className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d]" rows={5}  disabled value={productDescription}/>
                        
                    </div>

                    <div className="w-full px-3 flex justify-end mb-5 text-green-500">
                        <p className="flex mx-4 "> @@Input7Label@@</p>
                    </div>
                    <div className="w-full mx-12 flex justify-center mb-5">
                        {productImage &&
                            (
                                <img src={`${CONSTANT.IMAGE_STORE}/${productImage}`} className="w-32 h-32"/>
                            )
                        }
                    </div>
                    <div className="w-full px-3 flex justify-end mb-5 text-green-500">
                        <p className="flex mx-4 ">Product gallery images</p>
                    </div>
                    <div className="overflow-x-auto flex justify-center mb-5 mx-auto">
                        {productGalleryImage &&
                            
                            productGalleryImage.map((image, index) => {
                                return (
                                    <>
                                        <img key={index}  src={`${CONSTANT.IMAGE_STORE}/${image.path}`} className="w-32 h-32"/>
                                    </>
                                )
                            })
                        }
                    </div>
                </div>
            </div>          
        </div>        
    </div>
  )
}
export default @@PageName@@;
 """
 layouts["layout_admin_view_product_details"] = layout_admin_view_product_details


 layout_admin_create_admin ="""
import React from 'react';
@@Imports@@
const @@PageName@@ = () => {
    const {register, handleSubmit, reset, formState: { errors } } = useForm();
    const submitForm = (data) => {
        let _data = {
            first_name: data.first_name.trim(),
            last_name: data.last_name.trim(),
            gender: data.gender.trim(),
            email: data.email.trim().toLowerCase(),
            mobile_number: data.mobile_number.trim(),
            user_type: CONSTANT.SUB_ADMIN_ROLE,
            password: data.password.trim()
        } 

        console.log('Getting set to post data')
        const requestOptions = {
            headers: {
                'Accept': '*/*',
                'Content-Type': 'application/json'
            }
        }
        axios.post(
            `${ROUTE.USER_API}/user`,
            JSON.stringify(_data),
            requestOptions
        ).then(res => res)
        .then(data =>{
            successAlert(data)
        })
        .catch(err => errorAlert(err))
    }
   
    const successAlert = (response) => {
        return(
          swal({
              title: "Successfully added!",
              text: response.data.message,
              icon: "success"
          }).then(function() {
            reset()
          })           
        )
    }

    const errorAlert = (error) => {
        return(
          swal({
              title: "Error!",
              text: error.message,
              icon: "error"
          })              
        )
    }

    return (
        <div className="bg-gray-100">
            <div className="header bg-white h-16 px-10 py-8 border-b-2 border-gray-200 flex items-center justify-between">
                <div className="flex items-center space-x-2 text-gray-400">
                    <span className="text-green-700 tracking-wider font-thin text-md"><Link to={ROUTE.ADMIN_DASHBOARD}>@@LinkToDashboard@@</Link></span>
                    <span>/</span>
                    <span className="tracking-wide text-md">
                        <span className="text-green-700 tracking-wider font-thin text-md"><Link to={ROUTE.ADMIN_USERS}>@@LinkToUsers@@</Link></span>
                    </span>
                    <span>/</span>
                    <span className="tracking-wide text-md">
                        <span className="text-base">@@PageTitle@@</span>
                    </span>
                </div>
            </div>
            <div className="header my-3 h-12 px-10 py-8  flex items-center justify-between">
                <h1 className="font-medium text-2xl">@@PageTitle@@</h1>
                <Link to={ROUTE.ADMIN_USERS} className="focus:outline-none text-white m-4 p-3 font-semibold rounded-md bg-green-700 hover:bg-green-600 hover:shadow-lg transition-all duration-100"> <span><FaAngleLeft className="inline-block w-5 h-5" />
                </span> Back to Users</Link>
            </div>
            <div className="flex flex-col mx-3 lg:flex-row">
                <form className="w-full lg:w-3/5 bg-white shadow-md p-6">
                    <div className="flex flex-wrap -mx-3 mb-6">
                        <div className='flex flex-col md:flex-row w-full'>
                            <div className="w-full md:w-1/2 px-3 mb-6">
                                <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='first_name'>@@Input1Label@@</label>
                                <input className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d]" type='text' name="first_name" placeholder="Enter First Name"
                                    {...register("first_name", { required: true })}
                                    required />
                                {errors.first_name && <small className="text-red-500 text-xs italic">First name is required</small>}
                            </div>
                            <div className="w-full md:w-1/2 px-3 mb-6">
                                <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='last_name'>@@Input2Label@@</label>
                                <input className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d]" type='text' name="last_name" placeholder="Enter Last Name"
                                    {...register("last_name", { required: true })}
                                    required />
                                {errors.last_name && <small className="text-red-500 text-xs italic">Last name is required</small>}
                            </div>
                        </div>

                        <div className='flex flex-col md:flex-row w-full'>
                            <div className="w-full md:w-1/2 px-3 mb-6">
                                <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='vendor_email'>@@Input3Label@@</label>
                                <input className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d]" type='email' name="email" placeholder="you@example.com"
                                    {...register("email", { required: true })}
                                    required />
                                {errors.email && <small className="text-red-500 text-xs italic">Email is required</small>}
                            </div>

                            <div className="w-full md:w-1/2 px-3 mb-6">
                                <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='mobile_number'>@@Input4Label@@</label>
                                <input className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d]" type='text' name="mobile_number" placeholder="080X XXX XXXX"
                                    {...register("mobile_number", { required: true })}
                                    required />
                                {errors.mobile_number && <small className="text-red-500 text-xs italic">Phone number is required</small>}
                            </div>
                        </div>

                        <div className='flex flex-col md:flex-row w-full'>
                            <div className="w-full md:w-1/2 px-3 mb-6">
                                <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='password'>@@Input5Label@@</label>
                                <input className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d]" type='password' name="password"
                                    {...register("password", { required: true })}
                                    required />
                                {errors.password && <small className="text-red-500 text-xs italic">Password is required</small>}
                            </div>
                            <div className="w-full md:w-1/2 px-3 mb-6">
                                <fieldset>
                                    <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='gender'>@@Input6Label@@</label>
                                    <div>
                                        <input type="radio" id="gender1"
                                            name="gender" value="male" className='m-2' {...register("gender", { required: true })} />
                                        <label htmlFor="gender1">Male</label>

                                        <input type="radio" id="gender2"
                                            name="gender" value="female" className='m-2' {...register("gender", { required: true })} />
                                        <label htmlFor="gender2">Female</label>
                                        {errors.vendor_gender && <small className="text-red-500 text-xs italic">Gender is required</small>}
                                    </div>
                                </fieldset>
                            </div>
                        </div>
                        <div className="w-full px-3 mb-6">
                            <button className="appearance-none w-full block bg-green-700 text-gray-100 font-bold border border-gray-200 rounded-lg py-3 px-3 leading-tight hover:bg-green-600 focus:outline-none focus:bg-white focus:border-gray-500"
                                onClick={handleSubmit(submitForm)}>@@PageTitle@@</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    )
}
export default @@PageName@@;
 """
 layouts["layout_admin_create_admin"] = layout_admin_create_admin


 layout_admin_edit_admins ="""
import React, { useEffect, useState } from 'react';
@@Imports@@
const @@PageName@@ = () => {
    const { id } = useParams();
    const [loading, setLoading] = useState(false);
    const [adminId, setAdminId] = useState('');
    const [adminFirstName, setAdminFirstName] = useState('');
    const [adminLastName, setAdminLastName] = useState('');
    const [adminGender, setAdminGender] = useState('');
    const [adminMobileNumber, setAdminMobileNumber] = useState('');
    const [adminUserType, setAdminUserType] = useState('');
    const [adminEmail, setAdminEmail] = useState('');
    
    const {register, handleSubmit, reset, setValue, formState: { errors } } = useForm();
    const getData = async () => {
        setLoading(true)
        await fetch(`${ROUTE.USER_API}/user/${id}`)
          .then((res) => res.json())
          .then((res) => {
            // const response = res.first_name
            // console.log("Response :::",response)
            setAdminId(res.id)
            setAdminFirstName(res.first_name)
            setAdminLastName(res.last_name)
            setAdminGender(res.gender)
            setAdminMobileNumber(res.mobile_number)
            setAdminUserType(res.user_type)
            setAdminEmail(res.email)
        })
        setLoading(false)
    }
    //console.log(getData)
    
    useEffect(() => {
        getData()
    }, [])
    
    useEffect(() => {
        setTimeout(() => 
            setValue("first_name", adminFirstName),
            setValue("last_name", adminLastName),
            setValue("gender", adminGender),
            setValue("mobile_number", adminMobileNumber),
            setValue("user_type", adminUserType),
            setValue("email", adminEmail)
        );
    }, [loading]);

    const submitForm = (data) => {
        let _data = {
            first_name: data.first_name.trim(),
            last_name: data.last_name.trim(),
            email: data.email.trim().toLowerCase(),
            mobile_number: data.mobile_number.trim(),
            user_type: data.user_type.trim()
        } 

        const requestOptions = {
            method: "POST",
            headers: {
                'Accept': '*/*',
                'Content-Type': 'application/json'
            }
        }
        axios.put(
            `${ROUTE.USER_API}/admin/${adminId}`,
            _data,
            //console.log(_data),
            requestOptions
        ).then(res => res)
        .then(data =>{
            if (data.status == 200 || data.status == 302) {
                successAlert(data)
            }
            else {
                errorAlert(data.message)
            }
        })
        .catch(err => errorAlert(err))
  
      reset()
    }

    const successAlert = (response) => {
        return(
          swal({
              title: "Successfully updated!",
              text: response.data.message,
              icon: "success"
          }).then(function () {
                getData()
          })
        )
    }
    const errorAlert = (error) => {
        return(
          swal({
              title: "Error!",
              text: error,
              icon: "error"
          }).then(function () {
            getData()
          })          
        )
    }

  return (
    <div className="bg-gray-100">
        <div className="header bg-white h-16 px-10 py-8 border-b-2 border-gray-200 flex items-center justify-between">
                <div className="flex items-center space-x-2 text-gray-400">
                <span className="text-green-700 tracking-wider font-thin text-md"><Link to={ROUTE.ADMIN_DASHBOARD}>@@LinkToDashboard@@</Link></span>
                <span>/</span>
                <span className="tracking-wide text-md">
                    <span className="text-green-700 tracking-wider font-thin text-md"><Link to={ROUTE.ADMIN_MANAGE_ADMINS}>@@LinkToAdmins@@</Link></span>
                </span>
                <span>/</span>
                <span className="tracking-wide text-md">
                    <span className="text-base">@@PageTitle@@</span>
                </span>
                </div>
        </div>
        <div className="header my-3 h-12 px-4 lg:px-10 py-8  flex items-center justify-between">
            <h1 className="font-medium text-2xl">@@PageTitle@@</h1>
            <Link to={ROUTE.ADMIN_MANAGE_ADMINS} className="focus:outline-none text-white m-4 p-3 font-semibold rounded-md bg-green-700 hover:bg-green-600 hover:shadow-lg transition-all duration-100"> <span><FaAngleLeft className="inline-block w-5 h-5"/>
            </span> @@LinkToDashboard@@</Link>
        </div>
        <div className="flex flex-col mx-3 lg:flex-row">
            <form className="w-full lg:w-3/5 bg-white shadow-md p-6">
                <div className='flex flex-col md:flex-row w-full'>
                    <div className="w-full md:w-1/2 px-3 mb-6">
                        <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='first_name'>@@Input1Label@@</label>
                        <input className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d] focus:ring-[#98c01d]" type='text' name="first_name"
                        {...register("first_name", { required: true })} required onChange={(e) => setAdminFirstName(e.target.value)} />
                        {errors.first_name && <small className="text-red-500 text-xs italic">First name is required</small>}
                    </div>
                    <div className="w-full md:w-1/2 px-3 mb-6">
                        <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='last_name'>@@Input2Label@@</label>
                        <input className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d] focus:ring-[#98c01d]" type='text' name="last_name"
                        {...register("last_name", { required: true })} required onChange={(e) => setAdminLastName(e.target.value)} />
                        {errors.last_name && <small className="text-red-500 text-xs italic">ast name is required</small>}
                    </div>
                </div>
                <div className='flex flex-col md:flex-row w-full'>
                    <div className="w-full md:w-1/2 px-3 mb-6">
                        <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='mobile_number'>@@Input3Label@@</label>
                        <input className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d] focus:ring-[#98c01d]" type='text' name="mobile_number"
                        {...register("mobile_number")} onChange={(e) => setAdminMobileNumber(e.target.value)} />
                    </div>
                    <div className="w-full md:w-1/2 px-3 mb-6">
                        <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='email'>@@Input4Label@@</label>
                        <input className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d] focus:ring-[#98c01d]" type='email' name="email"
                        {...register("email", { required: true })} required onChange={(e) => setAdminEmail(e.target.value)} />
                        {errors.last_name && <small className="text-red-500 text-xs italic">Last name is required</small>}
                    </div>
                </div>
                <div className='flex flex-col md:flex-row w-full'>
                    <div className="w-full md:w-1/2 px-3 mb-6">
                        <fieldset>
                            <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='user_type'>@@Input5Label@@</label>
                            <div>
                                <input type="radio" id="user_type1"
                                    name="user_type" value={CONSTANTS.SUB_ADMIN_ROLE} className='m-2' {...register("user_type", { required: true })} />
                                <label htmlFor="user_type1">Admin</label>

                                <input type="radio" id="user_type2"
                                    name="user_type" value="" className='m-2' {...register("user_type", { required: true })} />
                                <label htmlFor="user_type2">Other</label>
                                {errors.user_type && <small className="text-red-500 text-xs italic">User Type is required</small>}
                            </div>
                        </fieldset>
                    </div>
                </div>
                <div className='flex flex-col md:flex-row w-full'>
                    <div className="w-full md:w-1/2 px-3 mb-6">
                        <button className="appearance-none w-full block bg-green-700 text-gray-100 font-bold border border-gray-200 rounded-lg py-3 px-3 leading-tight hover:bg-green-600 focus:outline-none focus:bg-white focus:border-gray-500"
                        onClick={handleSubmit(submitForm)}
                        >Update Admin</button>
                    </div>
                </div>
            </form>          
        </div>      
    </div>
  )
}
export default @@PageName@@;
 """
 layouts["layout_admin_edit_admins"] = layout_admin_edit_admins
 
 
 layout_admin_manage_admins ="""
import React, {useEffect, useState, useCallback} from 'react';
@@Imports@@
  const @@PageName@@ = () => {
  const [users, fetchUsers] = useState([]);

  const { accessToken } = useSelector((state) => ({
    accessToken: state.profile.access_token
  }));

  const getData = () => {
      fetch(`${ROUTE.USER_API}/user/sub-admin`, {
          headers:{
            'Content-Type':'application/json',
            'Authorization': 'Bearer ' + accessToken    
          }
      })
      .then((res) => res.json())
      .then((res) => {
        fetchUsers(res)
      })
  }

  useEffect(() => {
      getData()
  }, [])

  const successAlert = (response) => {
    return(
      swal({
          title: "Info!",
          text: response.data.message,
          icon: "success"
      }).then(function () {
            getData()
      })
    )
  }
  const errorAlert = (error) => {
      return(
        swal({
            title: "Error!",
            text: error,
            icon: "error"
        }).then(function () {
          getData()
        })          
      )
  }

  const deleteAdmin = useCallback( async (id)  => {
    if(confirm('Are you sure you want to delete this admin?')){
      axios.delete(
        `${ROUTE.USER_API}/admin/${id}`,{
            method : 'DELETE',
            body : JSON.stringify({
                id : id
            }),
            headers: {
                'Content-type': 'application/json'
            }
        })
        .then(res => res)
        .then(data =>{
          successAlert(data)
        })
        .catch(err => errorAlert(err)
        )
    }
}, []);

  let userList = ''
  if(users.length > 0){ 
      userList = users.map((user) => {
          return (
            <tr key={user.id}>
              <td className="p-2">
                  {user.first_name} {user.last_name}
              </td>
              <td className="p-2 capitalize">
                  {user.gender}
              </td>
              <td className="p-2">
                  {user.mobile_number.substring(0,12)}
              </td>
              <td className="p-2">
                  {user.email.substring(0,25)}
              </td>
              <td className="p-2">
                  {user.created_at.substring(0,17)}
              </td>
              <td className="p-2">
                <div className="flex">
                  <Link to={`${ROUTE.ADMIN_EDIT_ADMINS}/${user.id}`} className="rounded-md hover:bg-gray-100 text-green-600 p-2 flex justify-between items-center">
                      <span><FaEdit className="w-4 h-4 mr-1"/>
                        </span> Edit
                  </Link>
                  <button className="rounded-md hover:bg-gray-100 text-red-600 p-2 flex justify-between items-center" value={user.id} onClick={() => deleteAdmin(user.id)}>
                      <span><FaTrash className="w-4 h-4 mr-1" /></span> Delete
                  </button>
                </div>
              </td>
            </tr>
          )  
      });
    } else {
      userList =  (<tr className=''><td colSpan={8} className="">
        <div className="flex flex-col my-4 space-y-3 justify-center items-center text-xl font-medium tracking-wide py-4 text-green-700 text-center">
            <MdOutlineProductionQuantityLimits className="w-16 h-16" />
            <p>No admins registered yet</p>
        </div>
        </td></tr>)
    }

  return (
    <div className="bg-gray-100">
        <div className="header bg-white h-16 px-10 py-8 border-b-2 border-gray-200 flex items-center justify-between">
              <div className="flex items-center space-x-2 text-gray-400">
                <span className="text-green-700 tracking-wider font-thin text-md"><Link to={ROUTE.ADMIN_DASHBOARD}>@@LinkToDashboard@@</Link></span>
                <span>/</span>
                <span className="tracking-wide text-md">
                    <span className="text-base">@@PageTitle@@</span>
                </span>
                <span>/</span>
              </div>
        </div>
        <div className="header my-3 h-12 px-10 py-8  flex items-center justify-between">
            <h1 className="font-medium text-2xl">@@PageTitle@@</h1>
            <Link to={ROUTE.ADMIN_CREATE_ADMIN} className="focus:outline-none text-white m-4 p-3 font-semibold rounded-md bg-green-700 hover:bg-green-600 hover:shadow-lg transition-all duration-100"> <span><FaPlus className="inline-block w-4 h-3"/>
            </span> Create new admin</Link>
        </div>
        <div className="flex flex-col mx-3 lg:flex-row">
            <div className="w-full m-4 bg-white shadow-lg text-lg rounded-sm border border-gray-200">
                <div className="overflow-x-auto rounded-lg  p-3">
                    {/* Display blogs table */}
                    <table className="table-auto w-full">
                        <thead className="text-sm font-semibold uppercase text-gray-800 bg-gray-50">
                          <tr className="font-semibold text-left">
                            <th className="p-2">@@TableHead1@@</th>
                            <th className="p-2">@@TableHead2@@</th>
                            <th className="p-2">@@TableHead3@@</th>
                            <th className="p-2">@@TableHead4@@</th>
                            <th className="p-2">@@TableHead5@@</th>
                            <th className="p-2">@@TableHead6@@</th>
                          </tr>
                        </thead>
                        <tbody className="text-sm divide-y divide-gray-100">
                          { userList }
                        </tbody>
                    </table>
                </div>
            </div>            
        </div>        
    </div>
  )
}
export default @@PageName@@;
 """
 layouts["layout_admin_manage_admins"] = layout_admin_manage_admins
 

 layout_admin_users ="""
import React, { useEffect, useState } from 'react';
@@Imports@@
const @@PageName@@ = () => {
  const [users, fetchUsers] = useState([]);

  const { user } = useSelector((state) => ({
    user: state.profile.access_token
  }));

    const getData = () => {
        fetch(`${ROUTE.USER_API}/users`, {
            headers:{
                'Content-Type':'application/json',
                'Authorization': 'Bearer ' + user    
            }
        })
        .then((res) => res.json())
        .then((res) => {
          fetchUsers(res)
        })
    }

    useEffect(() => {
        getData()
    }, [])

  let userList = ''
  if(users.length > 0){ 
      userList = users.map((user) => {
          return (
            <tr key={user.id}>
              <td className="p-2">
                  {user.first_name} {user.last_name}
              </td>
              <td className="p-2 capitalize">
                  {user.gender}
              </td>
              <td className="p-2">
                  {user.mobile_number}
              </td>
              <td className="p-2">
                  {user.email}
              </td>
              <td className="p-2">
                  {user.created_at.substring(0,17)}
              </td>
            </tr>
          )  
      });
    } else {
      userList =  (<tr className=''><td colSpan={8} className="">
        <div className="flex flex-col my-4 space-y-3 justify-center items-center text-xl font-medium tracking-wide py-4 text-green-700 text-center">
            <MdOutlineProductionQuantityLimits className="w-16 h-16" />
            <p>No customers registered yet</p>
        </div>
        </td></tr>)
        
    }

  return (
    <div className="bg-gray-100">
        <div className="header bg-white h-16 px-10 py-8 border-b-2 border-gray-200 flex items-center justify-between">
              <div className="flex items-center space-x-2 text-gray-400">
                <span className="text-green-700 tracking-wider font-thin text-md"><Link to={ROUTE.ADMIN_DASHBOARD}>@@LinkToDashboard@@</Link></span>
                <span>/</span>
                <span className="tracking-wide text-md">
                    <span className="text-base">@@PageTitle@@</span>
                </span>
                <span>/</span>
              </div>
        </div>
        <div className="header my-3 h-12 px-10 py-8  flex items-center justify-between">
            <h1 className="font-medium text-2xl">@@PageTitle@@</h1>
            <Link to={ROUTE.ADMIN_CREATE_ADMIN} className="focus:outline-none text-white m-4 p-3 font-semibold rounded-md bg-green-700 hover:bg-green-600 hover:shadow-lg transition-all duration-100"> <span><FaPlus className="inline-block w-4 h-3"/>
            </span> @@CreateNewAdmin@@</Link>
        </div>
        <div className="flex flex-col mx-3 lg:flex-row">
            <div className="w-full m-4 bg-white shadow-lg text-lg rounded-sm border border-gray-200">
                <div className="overflow-x-auto rounded-lg  p-3">
                    {/* Display blogs table */}
                    <table className="table-auto w-full">
                        <thead className="text-sm font-semibold uppercase text-gray-800 bg-gray-50">
                          <tr className="font-semibold text-left">
                            <th className="p-2">@@TableHead1@@</th>
                            <th className="p-2">@@TableHead2@@</th>
                            <th className="p-2">@@TableHead3@@</th>
                            <th className="p-2">@@TableHead4@@</th>
                            <th className="p-2">@@TableHead5@@</th>
                          </tr>
                        </thead>
                        <tbody className="text-sm divide-y divide-gray-100">
                          { userList }
                        </tbody>
                    </table>
                </div>
            </div>
            
        </div>        
    </div>
  )
}
export default @@PageName@@;
 """
 layouts["layout_admin_users"] = layout_admin_users


 layout_admin_addvendor ="""
import React, { useCallback, useState, useEffect} from 'react';
@@Imports@@
const @@PageName@@ = () => {
  const {register, handleSubmit, reset, formState: { errors }, clearErrors } = useForm();
    const [selectedImage, setSelectedImage] = useState();
    const [vendorImage, setVendorImage] = useState();
    const [vendorDescription, setVendorDescription] = useState('');
    const [bank_id, setBank_id] = useState([]);
    const [account_no, setAccount_no] = useState('');
    const [accountName, setAccountName] = useState('');
    const [statelst, setStateLst] = useState([]);
    const [selectedState, setSelectedState] = useState([]);
    const [selectedStateValue, setSelectedStateValue] = useState([]);
    const [city, setCity] = useState([]);
    let formData = new FormData();

    const onSelectFile = useCallback(async (e) => {
        const file = e.target.files[0];
        const reader = new FileReader();
        reader.readAsDataURL(file);
        setVendorImage(file)
        reader.onloadend = () => {
            setSelectedImage(reader.result);
        };
    }, []);

    const handleChange = (e, editor) => {
        clearErrors('content');
        setVendorDescription(editor.getData())
    }

    const submitForm = (data) => {
        if (accountName){
            formData.append('vendor_first_name', data.vendor_first_name)
            formData.append('vendor_last_name', data.vendor_last_name)
            formData.append('vendor_gender', data.vendor_gender);
            formData.append('vendor_email', data.vendor_email);
            formData.append('vendor_phone', data.vendor_phone);
            formData.append('vendor_image', vendorImage)
            formData.append('vendor_business_name', data.vendor_business_name);
            formData.append('vendor_Description', vendorDescription);
            formData.append('vendor_address', data.vendor_business_address);
            formData.append('vendor_Bank', bank_id.label);
            formData.append('vendor_Bank_value', bank_id.value);
            formData.append('vendor_state', selectedState[0].name);
            formData.append('vendor_state_value', selectedStateValue[0].isoCode);
            formData.append('vendor_city', data.vendor_city);
            formData.append('vendor_account_number', data.vendor_account_no);
            formData.append('vendor_account_name', accountName);

            const requestOptions = {
                headers: {
                    'Content-type': 'multipart/form-data'
                }
            }
            axios.post(
                `${ROUTE.USER_API}/user/vendors`,
                formData,
                requestOptions
            ).then(res => res)
            .then(data =>{
                successAlert(data)
            })
            .catch(err => errorAlert(err))
        }
        else{
            console.log("account name not resolved")
        }
    }
   
    const successAlert = (response) => {
        return(
          swal({
              title: "Info!",
              text: response.data.message,
              icon: "success"
          }).then(function() {
            reset()
            setSelectedImage('')
          })           
        )
    }

    const errorAlert = (error) => {
        return(
          swal({
              title: "Error!",
              text: error.message,
              icon: "error"
          })              
        )
    }

    const accountNokeyup = () => {
        const timer = setAccount_no(() => {
            if(bank_id.value){
                resolveAccount();
            }
        }, 1000)
    
        return () => clearTimeout(timer)
      }

    const resolveAccount = () => { 
        const result2 = (account_no || 123).length;
        if (result2 === 10){
        fetch(`https://api.paystack.co/bank/resolve?account_number=${account_no}&bank_code=${bank_id.value}`, {
        'method':'GET',
        headers:{
        'Content-Type':'application/json',
        'Authorization': `Bearer ${process.env.REACT_APP_PAYSTACK_SECRET_KEY}` // eslint-disable-line
        }
        }).then(resp => resp.json())
        .then(resp => setAccountName(resp.data.account_name))
        .catch(error => console.log(error),  setAccountName(''))
        }
    }  

    useEffect(() => {
        setStateLst(stateList)
     },[])
   
    const handleSelectedState = (sCode) => {
        const sdt = stateList.filter(y => y.isoCode === sCode)
        const dt = localGovtList.filter(x => x.stateCode === sCode)
        setCity(dt);
        setSelectedState(sdt)
        setSelectedStateValue(sdt)
    }
    return (
        <div className="bg-gray-100">
            <div className="header bg-white h-16 px-10 py-8 border-b-2 border-gray-200 flex items-center justify-between">
                <div className="flex items-center space-x-2 text-gray-400">
                    <span className="text-green-700 tracking-wider font-thin text-md"><Link to={ROUTE.ADMIN_DASHBOARD}>@@LinkToDashboard@@</Link></span>
                    <span>/</span>
                    <span className="tracking-wide text-md">
                        <span className="text-green-700 tracking-wider font-thin text-md"><Link to={ROUTE.ADMIN_VENDORS}>@@LinkToVendor@@</Link></span>
                    </span>
                    <span>/</span>
                    <span className="tracking-wide text-md">
                        <span className="text-base">@@PageTitle@@</span>
                    </span>
                </div>
            </div>
            <div className="header my-3 h-12 px-10 py-8  flex items-center justify-between">
                <h1 className="font-medium text-2xl">@@PageTitle@@</h1>
                <Link to={ROUTE.ADMIN_VENDORS} className="focus:outline-none text-white m-4 p-3 font-semibold rounded-md bg-green-700 hover:bg-green-600 hover:shadow-lg transition-all duration-100"> <span><FaAngleLeft className="inline-block w-5 h-5" />
                </span> Back to @@LinkToVendor@@</Link>
            </div>
            <div className="flex flex-col mx-3 lg:flex-row">
                <form className="w-full lg:w-3/5 bg-white shadow-md p-6" encType="multipart/form-data">
                    <div className="flex flex-wrap -mx-3 mb-6">
                        <div className='flex flex-col md:flex-row w-full'>
                            <div className="w-full md:w-1/2 px-3 mb-6">
                                <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='vendor_first_name'>@@Input1Label@@</label>
                                <input className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d]" type='text' name="vendor_first_name" placeholder="Enter Vendors' First Name"
                                    {...register("vendor_first_name", { required: true })}
                                    required />
                                {errors.vendor_first_name && <small className="text-red-500 text-xs italic">Vendors first name is required</small>}
                            </div>
                            <div className="w-full md:w-1/2 px-3 mb-6">
                                <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='vendor_last_name'>@@Input2Label@@</label>
                                <input className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d]" type='text' name="vendor_last_name" placeholder="Enter Vendors' Last Name"
                                    {...register("vendor_last_name", { required: true })}
                                    required />
                                {errors.vendor_last_name && <small className="text-red-500 text-xs italic">Vendors last name is required</small>}
                            </div>
                        </div>

                        <div className='flex flex-col md:flex-row w-full'>
                            <div className="w-full md:w-1/2 px-3 mb-6">
                                <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='vendor_email'>@@Input3Label@@</label>
                                <input className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d]" type='text' name="vendor_email" placeholder="you@example.com"
                                    {...register("vendor_email", { required: true })}
                                    required />
                                {errors.vendor_email && <small className="text-red-500 text-xs italic">Vendors email is required</small>}
                            </div>

                            <div className="w-full md:w-1/2 px-3 mb-6">
                                <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='vendor_phone'>@@Input4Label@@</label>
                                <input className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d]" type='text' name="vendor_phone" placeholder="080X XXX XXXX"
                                    {...register("vendor_phone", { required: true })}
                                    required />
                                {errors.vendor_phone && <small className="text-red-500 text-xs italic">Vendors phone is required</small>}
                            </div>
                        </div>

                        <div className='flex flex-col md:flex-row w-full'>
                            <div className="w-full md:w-1/2 px-3 mb-6">
                                <fieldset>
                                    <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='vendor_gender'>@@Input5Label@@</label>
                                    <div>
                                        <input type="radio" id="vendorGender1"
                                            name="vendor_gender" value="male" className='m-2' {...register("vendor_gender", { required: true })} />
                                        <label htmlFor="vendorGender1">Male</label>

                                        <input type="radio" id="vendorGender2"
                                            name="vendor_gender" value="female" className='m-2' {...register("vendor_gender", { required: true })} />
                                        <label htmlFor="vendorGender2">Female</label>
                                        {errors.vendor_gender && <small className="text-red-500 text-xs italic">Vendors gender is required</small>}
                                    </div>
                                </fieldset>
                            </div>
                            <div className="w-full md:w-1/2 px-3 mb-6">
                                <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='Bank_name'>@@Input6Label@@</label>
                                {errors.Bank_name && <small className="text-red-500 text-xs italic">Select at least one Bank</small>}
                                <Select defaultValue={bank_id} onChange={setBank_id} options={BankList}/>
                            </div>
                        </div>

                        <div className='flex flex-col md:flex-row w-full'>
                            <div className="w-full md:w-1/2 px-3 mb-6">
                                <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='vendor_account_no'>@@Input7Label@@</label>
                                <div className='flex flex-row'>
                                        {/* <input className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 leading-tight focus:outline-none focus:border-[#98c01d]" name="vendor_account_no" placeholder="05X XXX XXXX"
                                        {...register("vendor_account_no", { required: true })} defaultValue={5}
                                        required type="number" value={account_no} onChange={inputChanged} /> */}
                                        <input className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 leading-tight focus:outline-none focus:border-[#98c01d]" name="vendor_account_no" placeholder="05X XXX XXXX"
                                        {...register("vendor_account_no", { required: true })} defaultValue={5}
                                        required type="number" value={account_no} onChange={(e) => setAccount_no(e.target.value)} onKeyUp={accountNokeyup}/>
                                        {errors.vendor_account_no && <small className="text-red-500 text-xs italic">Vendors account number is required</small>}
                                    
                                </div>
                            </div>
                            <div className="w-full md:w-1/2 px-3 mb-6">
                                <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='vendor_account_name'>@@Input8Label@@</label>
                                <p className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d] cursor-not-allowed" 
                                >{accountName}</p>
                            </div>
                        </div>

                        <div className="w-full px-3 mb-6">
                            <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='vendor_business_address'>@@Input9Label@@</label>
                            <input className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d]" type='text' name="vendor_business_address" placeholder="Enter Business Address"
                                {...register("vendor_business_address", { required: true })}
                                required />
                            {errors.vendor_business_address && <small className="text-red-500 text-xs italic">Vendor business address is required</small>}
                        </div>

                        <div className='flex flex-col md:flex-row w-full'>
                            <div className="w-full md:w-1/2 px-3 mb-6">
                                <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='business_state'>State</label>                                
                                <select id="ddlstate" className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d]" name="business_state" {...register("business_state", { required: true })} onChange={(e) => handleSelectedState(e.target.value)}>
                                    <option value={'0'}>Select State</option>
                                    {statelst &&
                                    statelst !== undefined ?
                                    statelst.map((st,i) => {
                                        return(
                                            <option key={i} value={st.isoCode}>{st.name}</option>
                                        )
                                    }):
                                    "No State"
                                    }
                                </select>

                            {errors.business_state && <small className="text-red-500 text-xs italic">Select at least one state</small>}
                            </div>
                            <div className="w-full md:w-1/2 px-3 mb-6">
                                <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='vendor_last_name'>City</label>
                                <select id="ddlcity" className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d]" name="Bank_name" {...register("vendor_city", { required: true })}>
                                    <option value={'0'}>Select City</option>
                                    {/* { cityDropDown } */}
                                    {city &&
                                    city !== undefined ?
                                    city.map((st,i) => {
                                        return(
                                            <option key={i} value={st.name}>{st.name}</option>
                                        )
                                    }):
                                    "No City"
                                    }
                                </select>

                            {errors.vendor_city && <small className="text-red-500 text-xs italic">Select at least one city</small>}
                            </div>
                        </div>

                        <div className="w-full px-3 mb-6">
                            <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='vendor_business_name'>Vendors Business Title</label>
                            <input className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d]" type='text' name="vendor_business_name" placeholder="Enter Business Title"
                                {...register("vendor_business_name", { required: true })}
                                required />
                            {errors.vendor_business_name && <small className="text-red-500 text-xs italic">Vendor business title is required</small>}
                        </div>

                        <div className="w-full px-3 mb-6">
                            <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='description'>Business Description</label>
                            <div className="w-full overflow-x-auto mx-3">
                                <CKEditor
                                    editor={ClassicEditor}
                                    onChange={handleChange} 
                                    data={vendorDescription} 
                                />
                            </div>
                        </div>


                        <div className="w-full mx-auto px-3 mb-12">
                            <label className="mx-auto cursor-pointer flex w-full max-w-lg flex-col items-center justify-center rounded-xl border-2 border-dashed border-green-400 bg-white p-6 text-center" htmlFor='product_image'>
                                <svg xmlns="http://www.w3.org/2000/svg" className="h-10 w-10 text-green-800" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="2">
                                    <path strokeLinecap="round" strokeLinejoin="round" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
                                </svg>

                                <h2 className="mt-4 text-xl font-medium text-gray-700 tracking-wide">Vendor image</h2>

                                <p className="mt-2 text-gray-500 tracking-wide">Upload or drag & drop your file SVG, PNG, JPG or GIF. </p>

                                <input name="product_image" id="product_image" type="file" className="hidden" onChange={onSelectFile} accept="image/png, image/jpeg, image/webp" />
                            </label>
                            {errors.product_image && <small className="text-red-500 text-xs italic">Vendor image is required</small>}
                        </div>
                        <div className="w-full flex justify-center mb-5">
                            {selectedImage &&
                                (
                                    <img src={selectedImage} className="w-32 h-32" />
                                )
                            }
                        </div>
                        <div className="w-full px-3 mb-6">
                            <button className="appearance-none w-full block bg-green-700 text-gray-100 font-bold border border-gray-200 rounded-lg py-3 px-3 leading-tight hover:bg-green-600 focus:outline-none focus:bg-white focus:border-gray-500"
                                onClick={handleSubmit(submitForm)}>@@PageTitle@@</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    )
}
export default @@PageName@@;
 """
 layouts["layout_admin_addvendor"] = layout_admin_addvendor


 """
 Layout example to be copied for use and replaced
 """
 layout_admin_editvendor ="""
import React, { useEffect, useState, useCallback } from 'react';
@@Imports@@
const @@PageName@@ = () => {
  const { id, slug } = useParams();
    const [loading, setLoading] = useState(false);
    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [email, setEmail] = useState('');
    const [phone, setPhone] = useState('');
    const [vendorsName, setVendorsName] = useState('');
    const [vendorsDescription, setVendorDescription] = useState('');
    const [vendortImage, setVendorImage] = useState('');
    const [selectedImage, setSelectedImage] = useState('');
    const [newImage, setNewImage] = useState('');
    const [bank_id, setBank_id] = useState([]);
    const [account_no, setAccount_no] = useState('');
    const [accountName, setAccountName] = useState('');
    const [statelst, setStateLst] = useState([]);
    const [selectedState, setSelectedState] = useState([]);
    const [city, setCity] = useState([]);
    const [address, setAddress] = useState('');
    const [readBank, setReadBank] = useState('');
    const [readState, setReadSate] = useState('');
    const [readCity, setReadCity] = useState('');
    const [readAccountNo, setReadAccountNo] = useState('');
    const [isBankDivShown, setIsBankDivShown] = useState(false);
    const checkboxHandler = () => {
        setIsBankDivShown(!isBankDivShown);
	};
    
    let formData = new FormData();

    const {register, handleSubmit, reset, setValue, formState: { errors }, clearErrors} = useForm();
   
    const getData = async () => {
        setLoading(true)
        await fetch(`${ROUTE.USER_API}/user/vendors/${id}/${slug}`)
          .then((res) => res.json())
          .then((res) => {
            setFirstName(res.vendor[0].first_name)
            setLastName(res.vendor[0].last_name)
            setEmail(res.vendor[0].email)
            setPhone(res.vendor[0].phone)
            setVendorsName(res.vendor[0].business_name)
            setVendorDescription(res.vendor[0].business_description)
            setVendorImage(res.vendor[0].image)
            setAddress(res.vendor[0].business_address)
            setAccount_no(res.vendor[0].business_account_no)
            setAccountName(res.vendor[0].business_account_name)
            setReadCity(res.vendor[0].business_city)
            setReadSate(res.vendor[0].business_state)
            setReadBank(res.vendor[0].business_bank)
            setReadAccountNo(res.vendor[0].business_account_no)
            setLoading(false)
        })
    }

    useEffect(() => {
        getData()
    }, [])

    useEffect(() => {
        setTimeout(() => 
            setValue("vendor_business_name", vendorsName)
        );
    }, [loading]);

    const onSelectFile = useCallback( async (e)  => {
        const file = e.target.files[0];
        const reader = new FileReader();
        reader.readAsDataURL(file);
        setNewImage(file)
        reader.onloadend = () => {
            setSelectedImage(reader.result);
        };
    }, []);

    const handleChange = (e, editor) => {
        clearErrors('content');
        setVendorDescription(editor.getData())
    }

    const submitForm = (data) => {
        if (isBankDivShown === false){
            if (accountName){
                formData.append('vendor_image', newImage)
                formData.append(
                    'vendor_business_name', 
                    data.vendor_business_name
                    );
                formData.append('vendor_Description', vendorsDescription);
                formData.append('vendor_address', address);
                formData.append('vendor_Bank', readBank);
                formData.append('vendor_state', readState);
                formData.append('vendor_city', readCity);
                formData.append('vendor_account_number', account_no);
                formData.append('vendor_account_name', accountName);
    
                const requestOptions = {
                    method: "PUT",
                    headers: {
                    'Content-type': 'multipart/form-data'
                    }
                }
                axios.put(
                    `${ROUTE.USER_API}/user/vendors/${id}/${slug}`,
                    formData,
                    requestOptions
                ).then(res => res)
                .then(data =>{
                successAlert(data)
                })
                .catch(err => errorAlert(err))
        
                reset()
                setSelectedImage('');
            }
        }
        else if(isBankDivShown !== false) {
            if (accountName){
                formData.append('vendor_image', newImage)
                formData.append('vendor_business_name', 
                    data.vendor_business_name);
                formData.append('vendor_Description', vendorsDescription);
                formData.append('vendor_address', data.vendor_business_address);
                formData.append('vendor_Bank', bank_id.label);
                formData.append('vendor_state', selectedState[0].name);
                formData.append('vendor_state_code', selectedState[0].isoCode);
                formData.append('vendor_city', data.vendor_city);
                formData.append('vendor_account_number', data.vendor_account_no);
                formData.append('vendor_account_name', accountName);
                console.log('Getting set to post data')    
    
                const requestOptions = {
                    method: "PUT",
                    headers: {
                    'Content-type': 'multipart/form-data'
                    }
                }
                axios.put(
                    `${ROUTE.USER_API}/user/vendors/${id}/${slug}`,
                    formData,
                    requestOptions
                ).then(res => res)
                .then(data =>{
                successAlert(data)
                })
                .catch(err => errorAlert(err))
                setIsBankDivShown(false)
                reset()
                setSelectedImage('');
            }
        }  
    }

    const successAlert = (response) => {
        return(
          swal({
              title: "Info!",
              text: response.data.message,
              icon: "success"
          }).then(function () {
                getData()
          })
        )
    }
    const errorAlert = (error) => {
        return(
          swal({
              title: "Error!",
              text: error,
              icon: "error"
          }).then(function () {
            getData()
          })          
        )
    }

    const accountNokeyup = () => {
        const timer = setAccount_no(() => {
            if(bank_id.value){
                resolveAccount();
            }
        }, 1000)
    
        return () => clearTimeout(timer)
      }

    const resolveAccount = () => { 
        const result2 = (account_no || 123).length;
        if (result2 === 10){
        fetch(`https://api.paystack.co/bank/resolve?account_number=${account_no}&bank_code=${bank_id.value}`, {
        'method':'GET',
        headers:{
        'Content-Type':'application/json',
        'Authorization': `Bearer ${process.env.REACT_APP_PAYSTACK_SECRET_KEY}`
        }
        }).then(resp => resp.json())
        .then(resp => setAccountName(resp.data.account_name))
        .then(resp => console.log(resp))
        .catch(error => console.log(error),  setAccountName(''))
        }
    }  

    useEffect(() => {
        setStateLst(stateList)
     },[])
   
    const handleSelectedState = (sCode) => {
        const sdt = stateList.filter(y => y.isoCode === sCode)
        const dt = localGovtList.filter(x => x.stateCode === sCode)
        setCity(dt);
        setSelectedState(sdt)
    }

  return (
    <div className="bg-gray-100">
        <div className="header bg-white h-16 px-10 py-8 border-b-2 border-gray-200 flex items-center justify-between">
                <div className="flex items-center space-x-2 text-gray-400">
                    <span className="text-green-700 tracking-wider font-thin text-md"><Link to={ROUTE.ADMIN_DASHBOARD}>@@LinkToDashboard@@</Link></span>
                    <span>/</span>
                    <span className="tracking-wide text-md">
                        <span className="text-green-700 tracking-wider font-thin text-md"><Link to={ROUTE.ADMIN_VENDORS}>@@LinkToVendor@@</Link></span>
                    </span>
                    <span>/</span>
                    <span className="tracking-wide text-md">
                        <span className="text-base">@@PageTitle@@</span>
                    </span>
                </div>
            </div>
        <div className="header my-3 h-12 px-4 lg:px-10 py-8  flex items-center justify-between">
            <h1 className="font-medium text-2xl">@@PageTitle@@</h1>
            <Link to={ROUTE.ADMIN_VENDORS} className="focus:outline-none text-white m-4 p-3 font-semibold rounded-md bg-green-700 hover:bg-green-600 hover:shadow-lg transition-all duration-100"> <span><FaAngleLeft className="inline-block w-5 h-5" />
                </span> Back to @@LinkToVendor@@</Link>
        </div>
        {loading
        ? (<div className="h-full flex justify-center items-center">
                <h3 className="font-bold text-green-600 text-2xl mx-auto ">Loading...</h3>
            </div>
        )
        :
        (<div className="flex flex-col mx-3 lg:flex-row">
            <form className="w-full lg:w-3/5 bg-white shadow-md p-6">
                <div className="flex flex-wrap -mx-3 mb-6">
                    <div className='flex flex-col md:flex-row w-full'>
                        <div className="w-full md:w-1/2 px-3 mb-6">
                            <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='vendor_first_name'>@@Input1Label@@</label>
                            <input className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d] cursor-not-allowed" type='text' name="vendor_first_name" value={firstName} placeholder="Enter Vendors' First Name"
                                disabled/>
                        </div>
                        <div className="w-full md:w-1/2 px-3 mb-6">
                            <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='vendor_last_name'>@@Input2Label@@</label>
                            <input className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d] cursor-not-allowed" type='text' name="vendor_last_name" value={lastName} placeholder="Enter Vendors' Last Name"
                            disabled/>
                        </div>
                    </div>

                    <div className='flex flex-col md:flex-row w-full'>
                            <div className="w-full md:w-1/2 px-3 mb-6">
                                <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='vendor_email'>@@Input3Label@@</label>
                                <input className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d] cursor-not-allowed" type='text' name="vendor_email" value={email} placeholder="you@example.com"
                                disabled/>
                            </div>
                            <div className="w-full md:w-1/2 px-3 mb-6">
                                <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='vendor_phone'>@@Input4Label@@</label>
                                <input className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d] cursor-not-allowed" type='text' name="vendor_phone" value={phone} placeholder="080X XXX XXXX"
                                disabled/>
                            </div>
                    </div>

                    <div className='flex flex-col md:flex-row w-full'>
                        <div className="w-full px-3 mb-6">
                            <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2 mr-2" htmlFor='Bank_name'>@@Input6Label@@</label>
                            <p className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d] cursor-not-allowed" 
                            >{readBank}</p>
                        </div>
                    </div>
                    <div className='flex flex-col md:flex-row w-full'>
                        <div className="w-full md:w-1/2 px-3 mb-6">
                            <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='vendor_account_no'>@@Input7Label@@</label>
                            <div className='flex flex-row'>
                                <p className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d] cursor-not-allowed" 
                                >{readAccountNo}</p>
                            </div>
                        </div>
                        <div className="w-full md:w-1/2 px-3 mb-6">
                            <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='vendor_account_name'>@@Input8Label@@</label>
                            <p className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d] cursor-not-allowed" 
                            >{accountName}</p>
                        </div>
                    </div>

                    <div className="w-full px-3 mb-6">
                        <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='vendor_business_address'>@@Input9Label@@</label>
                        <p className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d] cursor-not-allowed">{address}</p>
                    </div>

                    <div className='flex flex-col md:flex-row w-full'>
                        <div className="w-full md:w-1/2 px-3 mb-6">
                            <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='business_state'>@@Input10Label@@</label>                                
                            <p className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d] cursor-not-allowed">{readState}</p>
                        </div>
                        <div className="w-full md:w-1/2 px-3 mb-6">
                            <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='vendor_last_name'>@@Input11Label@@</label>
                            <p className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d] cursor-not-allowed" 
                            >{readCity}</p>
                        </div>
                    </div>

                    <div className='flex flex-col md:flex-row w-full'>
                        <div className="w-full px-3 mb-6">
                            <div className="flex flex-row itmes-center">
                                <input 
                                    type="checkbox" 
                                    name="check_box" 
                                    className="text-black shadow-sm bg-white rounded mr-1" 
                                    id="account"
                                    value={isBankDivShown} 
                                    onChange={checkboxHandler}/>
                                <p className="pl-2"> change bank and address details</p>
                            </div>
                            
                        </div>
                    </div>

                    {isBankDivShown && <div className='w-full'>
                    <div className='flex flex-col md:flex-row w-full'>
                        <div className="w-full px-3 mb-6">
                            <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='Bank_name'>Bank Name</label>
                            {errors.Bank_name && <small className="text-red-500 text-xs italic">Select at least one Bank</small>}
                            <Select defaultValue={readBank} onChange={setBank_id} options={BankList}/>
                        </div>
                    </div>

                    <div className='flex flex-col md:flex-row w-full'>
                        <div className="w-full md:w-1/2 px-3 mb-6">
                            <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='vendor_account_no'>Bank account number</label>
                            <div className='flex flex-row'>
                                    <input className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 leading-tight focus:outline-none focus:border-[#98c01d]" name="vendor_account_no" placeholder="05X XXX XXXX"
                                    {...register("vendor_account_no", { required: true })} defaultValue={5}
                                    required type="number" value={account_no} onChange={(e) => setAccount_no(e.target.value)} onKeyUp={accountNokeyup}/>
                                    {errors.vendor_account_no && <small className="text-red-500 text-xs italic">Vendors account number is required</small>}
                                
                            </div>
                        </div>
                        <div className="w-full md:w-1/2 px-3 mb-6">
                            <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='vendor_account_name'>Vendors Account Name</label>
                            <p className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d] cursor-not-allowed" 
                            >{accountName}</p>
                        </div>
                    </div>

                    <div className="w-full px-3 mb-6">
                        <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='vendor_business_address'>Vendors Business Address</label>
                        <input className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d]" type='text' name="vendor_business_address" placeholder="Enter Vendors' Address"
                            {...register("vendor_business_address", { required: true })}
                            required/>
                        {errors.vendor_business_address && <small className="text-red-500 text-xs italic">Vendor business address is required</small>}
                    </div>

                    <div className='flex flex-col md:flex-row w-full'>
                        <div className="w-full md:w-1/2 px-3 mb-6">
                            <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='business_state'>State</label>                                
                            <select id="ddlstate" className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d]" name="business_state" defaultValue={readState || ""} {...register("business_state", { required: true })} onChange={(e) => handleSelectedState(e.target.value)}>
                                <option value={'0'}>Select State</option>
                                {statelst &&
                                statelst !== undefined ?
                                statelst.map((st,i) => {
                                    return(
                                        <option key={i} value={st.isoCode}>{st.name}</option>
                                    )
                                }):
                                "No State"
                                }
                            </select>

                        </div>
                        <div className="w-full md:w-1/2 px-3 mb-6">
                            <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='vendor_last_name'>City</label>
                            <select id="ddlcity" className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d]" name="Bank_name" defaultValue={readCity || ""} {...register("vendor_city", { required: true })}>
                                <option value={'0'}>Select City</option>
                                {city &&
                                city !== undefined ?
                                city.map((st,i) => {
                                    return(
                                        <option key={i} value={st.name}>{st.name}</option>
                                    )
                                }):
                                "No City"
                                }
                            </select>
                        </div>
                    </div>
                    </div>}

                    <div className="w-full px-3 mb-6">
                        <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='name'>Business Name</label>
                        <input className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d]" type='text' name="vendor_business_name" placeholder="Enter Business Name"
                        value={vendorsName} {...register("vendor_business_name", { required: true })} required onChange={(e) => setVendorsName(e.target.value)} />
                        {errors.vendor_business_name && <small className="text-red-500 text-xs italic">Business name is required</small>}
                    </div>
                    
                    <div className="w-full px-3 mb-6">
                        <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='description'>Business Description</label>
                        <div className="w-full overflow-x-auto mx-3">
                            <CKEditor
                                editor={ClassicEditor}
                                onChange={handleChange} 
                                data={vendorsDescription} 
                            />
                        </div>
                    </div>
                   
                    <div className="flex justify-center w-full px-3 mb-12">
                        <label className="cursor-pointer flex w-fit max-w-lg flex-col items-center justify-start rounded-xl border-2 border-dashed border-green-400 bg-white p-6" htmlFor='vendor_image'>
                        <svg xmlns="http://www.w3.org/2000/svg" className="h-10 w-10 text-green-800" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="2">
                        <path strokeLinecap="round" strokeLinejoin="round" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
                        </svg>

                        <h2 className="mt-4 text-xl font-medium text-gray-700 tracking-wide">Vendor image</h2>

                        <p className="mt-2 text-gray-500 tracking-wide">Upload or drag & drop your file SVG, PNG, JPG or GIF. </p>

                        <input name="vendor_image" id="vendor_image" type="file" className="hidden" onChange={onSelectFile} accept="image/png, image/jpeg, image/webp" />
                            </label>
                            {errors.vendor_image && <small className="text-red-500 text-xs italic">Vendor image is required</small>}
                    </div>
                    {errors.vendor_image && <small className="text-red-500 text-xs italic">Vendor image is required</small>}

                    <div className="w-full mx-12 flex justify-center mb-5">
                        {vendortImage &&
                            (
                                <img src={`${CONSTANT.IMAGE_STORE}/${vendortImage}`} className={selectedImage ? "hidden" : `w-32 h-32 $`}/>
                            )
                        }
                        {selectedImage &&
                            (
                                <img src={selectedImage} className="w-32 h-32"/>
                            )

                        } 
                    </div>
                    <div className="w-full px-3 mb-6">
                        <button className="appearance-none w-full block bg-green-700 text-gray-100 font-bold border border-gray-200 rounded-lg py-3 px-3 leading-tight hover:bg-green-600 focus:outline-none focus:bg-white focus:border-gray-500"
                        onClick={handleSubmit(submitForm)}
                        >Update Vendor</button>
                    </div>
                </div>
            </form>          
        </div> 
        )
        }      
    </div>
        )
}
export default @@PageName@@;
 """
 layouts["layout_admin_editvendor"] = layout_admin_editvendor
 

 layout_admin_unverified_vendors ="""
import React, {useEffect, useState, useCallback} from 'react';
@@Imports@@
const @@PageName@@ = () => {
    const [vendors, fetchVendors] = useState([]);
    const getData = () => {
      fetch(`${ROUTE.USER_API}/user/vendors`)
        .then((res) => res.json())
        .then((res) => {
            fetchVendors(res.results)
        })
    }

    useEffect(() => {
        getData()
    }, [])

    const successAlert = (response) => {
        return(
            swal({
                title: "Info!",
                text: response.data.message,
                icon: "success"
            }).then(function () {
                getData()
            })
        )
    }
    const errorAlert = (error) => {
        return(
            swal({
                title: "Error!",
                text: error,
                icon: "error"
            }).then(function () {
            getData()
            })          
        )
    }
    
    const deleteVendor = useCallback( async (id, slug)  => {
      if(window.confirm('Are you sure you want to delete this vendor?')){
        axios.delete(
          `${ROUTE.USER_API}/user/vendors/${id}/${slug}`,{
              method : 'DELETE',
              body : JSON.stringify({
                  id : id
              }),
              headers: {
                  'Content-type': 'application/json'
              }
          })
          .then(res => res)
          .then(data =>{
            successAlert(data)
          })
          .catch(err => errorAlert(err)
          )
      }
    }, []);

    const verifyVendor = useCallback( async (id)  => {
        axios.put(
            `${ROUTE.USER_API}/user/vendors/verify/${id}`,{
                method : 'PUT',
                body : JSON.stringify({
                    id : id
                }),
                headers: {
                    'Content-type': 'application/json'
                }
            })
            .then(res => res)
            .then(data =>{
              successAlert(data)
            })
            .catch(err => errorAlert(err)
            )
    }, []);
    
    const verifyAll = useCallback( async ()  => {
        axios.put(
            `${ROUTE.USER_API}/vendors/verify/all`,{
                method : 'PUT',
                headers: {
                    'Content-type': 'application/json'
                }
            })
            .then(res => res)
            .then(data =>{
                successAlert(data)
            })
            .catch(err => errorAlert(err)
            )
    }, []);


    let vendorList;
    if(vendors.length > 0){
      vendorList = vendors.filter((vendors) => vendors.status == 0)?.map((item, i) => {
            return (
                <tr key={i}>
                    <td className="p-2">
                        <input type="checkbox" className="w-5 h-5" />
                    </td>
                    <td className="p-2 w-8">
                    <img src={`${CONSTANT.IMAGE_STORE}/${item.image}`} className="w-8 h-8 mx-auto" alt={item.business_name} />
                    </td>
                    <td className="p-2">
                        {item.business_name}
                    </td>
                    <td className="p-2">
                        <p>{item.first_name} {item.last_name}</p>
                    </td>
                    <td className="p-2">
                        <p>{item.email}</p>
                    </td>
                    <td className="p-2">
                        { item.business_city }
                    </td>
                    <td className="p-2">
                        { item.business_state }
                    </td>
                    <td className="p-2">
                        <span className="rounded-md  text-white bg-red-600 p-1 flex justify-center items-center text-center">Unverified</span>
                    </td>
                    <td className="p-2">
                      <div className="flex justify-center">
                        <button className="rounded-md text-green-600 hover:bg-gray-200 p-2 flex justify-between items-center" value={item.vendor_id} onClick={() => verifyVendor(item.user_id)}>
                              <span><ImCheckmark className="w-4 h-4 mr-1" /></span> Verify
                          </button>
                          <Link to={`${ROUTE.ADMIN_VIEW_VENDORS}/${item.vendor_id}/${item.slug}`} className="rounded-md hover:bg-gray-100 text-green-600 p-2 flex justify-between items-center">
                              <span><MdInfoOutline className="w-4 h-4 mr-1"/>
                                </span> View
                          </Link>
                          <Link to={`${ROUTE.ADMIN_EDIT_VENDORS}/${item.vendor_id}/${item.slug}`} className="rounded-md hover:bg-gray-100 text-green-600 p-2 flex justify-between items-center">
                              <span><FaEdit className="w-4 h-4 mr-1"/>
                                </span> Edit
                          </Link>
                          <button className="rounded-md hover:bg-gray-100 text-red-600 p-2 flex justify-between items-center" value={item.vendor_id} onClick={() => deleteVendor(item.vendor_id, item.slug)}>
                              <span><FaTrash className="w-4 h-4 mr-1" /></span> Delete
                          </button>
                        </div>
                    </td>
                </tr>
            )
        }

        );
    } else {
      vendorList =  (<tr className=''><td colSpan={8} className="">
        <div className="flex flex-col my-4 space-y-3 justify-center items-center text-xl font-medium tracking-wide py-4 text-green-700 text-center">
            <MdOutlineProductionQuantityLimits className="w-16 h-16" />
            <p>@@NoRecordMssg@@</p>
        </div>
        </td></tr>)
        
    }

    return (
        <div className="bg-gray-100">
            <div className="header bg-white h-16 px-10 py-8 border-b-2 border-gray-200 flex items-center justify-between">
                <div className="flex items-center space-x-2 text-gray-400">
                    <span className="text-green-700 tracking-wider font-thin text-md"><Link to={ROUTE.ADMIN_DASHBOARD}>@@LinkToDashboard@@</Link></span>
                    <span>/</span>
                    <span className="tracking-wide text-md">
                        <span className="text-base">@@PageSubTitle@@</span>
                    </span>
                    <span>/</span>
                </div>
            </div>
            <div className="header my-3 h-12 px-10 py-8  flex items-center justify-between">
                <h1 className="font-medium text-2xl">@@PageTitle@@</h1>
                <div className="focus:outline-none text-white m-4 p-3 font-semibold rounded-md bg-green-700 hover:bg-green-600 hover:shadow-lg transition-all duration-100"> List</div>
                {/* <Link to={ROUTE.ADMIN_ADD_VENDORS} className="focus:outline-none text-white m-4 p-3 font-semibold rounded-md bg-green-700 hover:bg-green-600 hover:shadow-lg transition-all duration-100"> <span><FaPlus className="inline-block w-5 h-5"/>
                </span> Add Vendors</Link> */}
            </div>
            <div className="flex flex-col mx-3 lg:flex-row">
                <div className="w-full m-4 bg-white shadow-lg text-lg rounded-sm border border-gray-200">
                    <div className="overflow-x-auto rounded-lg  p-3">
                    <button onClick={() => verifyAll()} className="focus:outline-none text-white m-4 p-3 font-semibold rounded-md bg-green-700 hover:bg-green-600 hover:shadow-lg transition-all duration-100"><span><ImCheckmark className="inline-block w-5 h-5"/></span>Verify all</button>
                        <table className="w-full whitespace-nowrap">
                            <thead className="text-sm font-semibold uppercase text-gray-800 bg-gray-50">
                                <tr className="font-semibold text-center">
                                    <th><input type="checkbox" className="w-5 h-5"/></th>
                                    <th className='w-12'><svg xmlns="http://www.w3.org/2000/svg" className="fill-current w-5 h-5 mx-auto" ><path d="M6 22h12a2 2 0 0 0 2-2V8l-6-6H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2zm7-18 5 5h-5V4zm-4.5 7a1.5 1.5 0 1 1-.001 3.001A1.5 1.5 0 0 1 8.5 11zm.5 5 1.597 1.363L13 13l4 6H7l2-3z"></path></svg></th>
                                    <th className="p-2">@@TableHead1@@
                                    </th>
                                    <th className="p-2">@@TableHead2@@
                                    </th>
                                    <th className="p-2">@@TableHead3@@
                                    </th>
                                    <th className="p-2">@@TableHead4@@
                                    </th>
                                    <th className="p-2">@@TableHead5@@
                                    </th>
                                    <th className="p-2">@@TableHead6@@
                                    </th>
                                    <th className="p-2">@@TableHead7@@
                                    </th>
                                </tr>
                            </thead>

                            <tbody className="text-sm divide-y divide-gray-100 text-center">
                          { vendorList }
                        </tbody>
                    </table>
                </div>
            </div>
            
        </div>        
    </div>
  )
}
export default @@PageName@@;
 """
 layouts["layout_admin_unverified_vendors"] = layout_admin_unverified_vendors


 layout_admin_vendors ="""
import React, {useEffect, useState, useCallback} from 'react';
@@Imports@@
const @@PageName@@ = () => {
  const [vendors, fetchVendors] = useState([]);

  const { accessToken } = useSelector((state) => ({
    accessToken: state.profile.access_token
  }));

  const getData = () => {
      fetch(`${ROUTE.USER_API}/user/vendors`, {
        headers:{
            'Content-Type':'application/json',
            'Authorization': 'Bearer ' + accessToken    
          }
      })
        .then((res) => res.json())
        .then((res) => {
            fetchVendors(res.results)
        })
    }

    useEffect(() => {
        getData()
    }, [])

    const successAlert = (response) => {
        return(
            swal({
                title: "Info!",
                text: response.data.message,
                icon: "success"
            }).then(function () {
                getData()
            })
        )
    }
    const errorAlert = (error) => {
        return(
            swal({
                title: "Error!",
                text: error,
                icon: "error"
            }).then(function () {
            getData()
            })          
        )
    }
    
    const deleteVendor = useCallback( async (id, slug)  => {
        if(window.confirm('Are you sure you want to delete this vendor?')){
            axios.delete(
            `${ROUTE.USER_API}/user/vendors/${id}/${slug}`,{
                method : 'DELETE',
                body : JSON.stringify({
                    id : id
                }),
                headers: {
                    'Content-type': 'application/json'
                }
            })
            .then(res => res)
            .then(data =>{
                successAlert(data)
            })
            .catch(err => errorAlert(err)
            )
        }

    }, []);
    
    let vendorList;
    if(vendors.length > 0){
      vendorList = vendors.map((item, i) => {
            return (
                <tr key={i}>
                    <td className="p-2">
                        <input type="checkbox" className="w-5 h-5" />
                    </td>
                    <td className="p-2 w-8">
                    <img src={`${CONSTANT.IMAGE_STORE}/${item.image}`} className="w-8 h-8 mx-auto" alt={item.business_name} />
                    </td>
                    <td className="p-2">
                        {item.business_name}
                    </td>
                    <td className="p-2">
                        <p>{item.first_name} {item.last_name}</p>
                    </td>
                    <td className="p-2">
                        <p>{item.email}</p>
                    </td>
                    <td className="p-2">
                        { item.business_city }
                    </td>
                    <td className="p-2">
                        { item.business_state }
                    </td>
                    <td className="p-2">
                        {item.status == 1 ?
                        <span className="rounded-md text-white bg-green-600 p-1 flex justify-center items-center text-center">Verified</span>
                        :
                        <span className="rounded-md  text-white bg-red-600 p-1 flex justify-center items-center text-center">Unverified</span>}
                    </td>
                    <td className="p-2">
                      <div className="flex justify-center">
                          <Link to={`${ROUTE.ADMIN_VIEW_VENDORS}/${item.vendor_id}/${item.slug}`} className="rounded-md hover:bg-gray-100 text-green-600 p-2 flex justify-between items-center">
                              <span><MdInfoOutline className="w-4 h-4 mr-1"/>
                                </span> View
                          </Link>
                          <Link to={`${ROUTE.ADMIN_EDIT_VENDORS}/${item.vendor_id}/${item.slug}`} className="rounded-md hover:bg-gray-100 text-green-600 p-2 flex justify-between items-center">
                              <span><FaEdit className="w-4 h-4 mr-1"/>
                                </span> Edit
                          </Link>
                          <button className="rounded-md hover:bg-gray-100 text-red-600 p-2 flex justify-between items-center" value={item.vendor_id} onClick={() => deleteVendor(item.vendor_id, item.slug)}>
                              <span><FaTrash className="w-4 h-4 mr-1" /></span> Delete
                          </button>
                        </div>
                    </td>
                </tr>
            )
        }

        );
    } else {
      vendorList =  (<tr className=''><td colSpan={8} className="">
        <div className="flex flex-col my-4 space-y-3 justify-center items-center text-xl font-medium tracking-wide py-4 text-green-700 text-center">
            <MdOutlineProductionQuantityLimits className="w-16 h-16" />
            <p>No Vendor added yet</p>
        </div>
        </td></tr>)
        
    }

    return (
        <div className="bg-gray-100">
            <div className="header bg-white h-16 px-10 py-8 border-b-2 border-gray-200 flex items-center justify-between">
                <div className="flex items-center space-x-2 text-gray-400">
                    <span className="text-green-700 tracking-wider font-thin text-md"><Link to={ROUTE.ADMIN_DASHBOARD}>Home</Link></span>
                    <span>/</span>
                    <span className="tracking-wide text-md">
                        <span className="text-base">Vendors</span>
                    </span>
                    <span>/</span>
                </div>
            </div>
            <div className="header my-3 h-12 px-10 py-8  flex items-center justify-between">
                <h1 className="font-medium text-2xl">All Vendors</h1>
                <div className="focus:outline-none text-white m-4 p-3 font-semibold rounded-md bg-green-700 hover:bg-green-600 hover:shadow-lg transition-all duration-100"> List</div>
                {/* <Link to={ROUTE.ADMIN_ADD_VENDORS} className="focus:outline-none text-white m-4 p-3 font-semibold rounded-md bg-green-700 hover:bg-green-600 hover:shadow-lg transition-all duration-100"> <span><FaPlus className="inline-block w-5 h-5"/>
                </span> Add Vendors</Link> */}
            </div>
            <div className="flex flex-col mx-3 lg:flex-row">
                <div className="w-full m-4 bg-white shadow-lg text-lg rounded-sm border border-gray-200">
                    <div className="overflow-x-auto rounded-lg  p-3">
                        {/* Display vendors table */}
                        <table className="w-full whitespace-nowrap">
                            <thead className="text-sm font-semibold uppercase text-gray-800 bg-gray-50">
                                <tr className="font-semibold text-center">
                                    <th><input type="checkbox" className="w-5 h-5"/></th>
                                    <th className='w-12'><svg xmlns="http://www.w3.org/2000/svg" className="fill-current w-5 h-5 mx-auto" ><path d="M6 22h12a2 2 0 0 0 2-2V8l-6-6H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2zm7-18 5 5h-5V4zm-4.5 7a1.5 1.5 0 1 1-.001 3.001A1.5 1.5 0 0 1 8.5 11zm.5 5 1.597 1.363L13 13l4 6H7l2-3z"></path></svg></th>
                                    <th className="p-2">Business Name
                                    </th>
                                    <th className="p-2">Business Owner
                                    </th>
                                    <th className="p-2">email
                                    </th>
                                    <th className="p-2">City
                                    </th>
                                    <th className="p-2">State
                                    </th>
                                    <th className="p-2">Status
                                    </th>
                                    <th className="p-2">Action
                                    </th>
                                </tr>
                            </thead>

                            <tbody className="text-sm divide-y divide-gray-100 text-center">
                            { vendorList }
                            </tbody>
                        </table>
                    </div>
                </div>   
            </div>        
        </div>       
    )
}
export default @@PageName@@;
 """
 layouts["layout_admin_vendors"] = layout_admin_vendors


 layout_admin_view_vendor ="""
import React, { useEffect, useState } from 'react';
@@Imports@@
const @@PageName@@ = () => {
  const { id, slug } = useParams();
    const [loading, setLoading] = useState(false);
    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [email, setEmail] = useState('');
    const [phone, setPhone] = useState('');
    const [vendorsName, setVendorsName] = useState('');
    const [vendorsDescription, setVendorDescription] = useState('');
    const [vendortImage, setVendorImage] = useState('');
    const [accountName, setAccountName] = useState('');
    const [address, setAddress] = useState('');
    const [readBank, setReadBank] = useState('');
    const [readState, setReadSate] = useState('');
    const [readCity, setReadCity] = useState('');
    const [readAccountNo, setReadAccountNo] = useState('');
    const [status, setStatus] = useState('');
    const [userId, setUserId] = useState('');
    const [dataChange, setDataChange] = useState(false);
   
    const getData = async () => {
        setLoading(true)
        await fetch(`${ROUTE.USER_API}/user/vendors/${id}/${slug}`)
          .then((res) => res.json())
          .then((res) => {
            setFirstName(res.vendor[0].first_name)
            setLastName(res.vendor[0].last_name)
            setEmail(res.vendor[0].email)
            setPhone(res.vendor[0].phone)
            setVendorsName(res.vendor[0].business_name)
            setVendorDescription(res.vendor[0].business_description)
            setVendorImage(res.vendor[0].image)
            setAddress(res.vendor[0].business_address)
            setAccountName(res.vendor[0].business_account_name)
            setReadCity(res.vendor[0].business_city)
            setReadSate(res.vendor[0].business_state)
            setReadBank(res.vendor[0].business_bank)
            setReadAccountNo(res.vendor[0].business_account_no)
            setStatus(res.vendor[0].status)
            setUserId(res.vendor[0].user_id)
            console.log(res.vendor[0].user_id)
            setLoading(false)
           
        })
    }
    useEffect(() => {
        getData()
    }, [dataChange])


    const verifyVendor = async ()  => {
        axios.put(
            `${ROUTE.USER_API}/user/vendors/verify/${userId}`,{
                method : 'PUT',
                headers: {
                    'Content-type': 'application/json'
                }
            })
            .then(res => res.json())
            .then(function () {
                getData()
          })
            setDataChange(true)
            setStatus(1)
            .then(data =>{
              successAlert(data)
            })
            .catch(err => errorAlert(err)
            );

        window.location.reload();
    };


    const unVerifyVendor = async ()  => {
        axios.put(
            `${ROUTE.USER_API}/user/vendors/unverify/${userId}`,{
                method : 'PUT',
                headers: {
                    'Content-type': 'application/json'
                }
            })
            .then(res => res.json())
            setDataChange(true)
            setStatus(1)
            .then(function () {
                getData()
          })
            .then(data =>{
              successAlert(data)
            })
            .catch(err => errorAlert(err)
            );
        window.location.reload(); 
    };

    const successAlert = (response) => {
        return(
          swal({
              title: "Info!",
              text: response.data.message,
              icon: "success"
          }).then(function () {
                getData()
          })
        )
    }
    const errorAlert = (error) => {
        return(
          swal({
              title: "Error!",
              text: error,
              icon: "error"
          }).then(function () {
            getData()
          })          
        )
    }
    
  return (
    <div className="bg-gray-100">
        <div className="header bg-white h-16 px-10 py-8 border-b-2 border-gray-200 flex items-center justify-between">
                <div className="flex items-center space-x-2 text-gray-400">
                    <span className="text-green-700 tracking-wider font-thin text-md"><Link to={ROUTE.ADMIN_DASHBOARD}>Home</Link></span>
                    <span>/</span>
                    <span className="tracking-wide text-md">
                        <span className="text-green-700 tracking-wider font-thin text-md"><Link to={ROUTE.ADMIN_VENDORS}>Vendors</Link></span>
                    </span>
                    <span>/</span>
                    <span className="tracking-wide text-md">
                        <span className="text-base">View Vendor</span>
                    </span>
                </div>
            </div>
        <div className="header my-3 h-12 px-4 lg:px-10 py-8  flex items-center justify-between">
            <h1 className="font-medium text-2xl">View Vendor</h1>
            <Link to={ROUTE.ADMIN_VENDORS} className="focus:outline-none text-white m-4 p-3 font-semibold rounded-md bg-green-700 hover:bg-green-600 hover:shadow-lg transition-all duration-100"> <span><FaAngleLeft className="inline-block w-5 h-5" />
                </span> Back to Vendors</Link>
        </div>
        {loading
        ? (<div className="h-full flex justify-center items-center">
                <h3 className="font-bold text-green-600 text-2xl mx-auto ">Loading...</h3>
            </div>
        )
        :
        (<div className="flex flex-col mx-3 lg:flex-row">
            <form className="w-full lg:w-3/5 bg-white shadow-md p-6">
                <div className="flex flex-wrap -mx-3 mb-6">
                    <div className='flex flex-col md:flex-row w-full'>
                        <div className="w-full md:w-1/2 px-3 mb-6">
                            <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='vendor_first_name'>Vendors First Name</label>
                            <p className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d] cursor-not-allowed">{firstName}</p>
                        </div>
                        <div className="w-full md:w-1/2 px-3 mb-6">
                            <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='vendor_last_name'>Vendors Last Name</label>
                            <p className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d] cursor-not-allowed">{lastName}</p>
                        </div>
                    </div>

                    <div className='flex flex-col md:flex-row w-full'>
                            <div className="w-full md:w-1/2 px-3 mb-6">
                                <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='vendor_email'>Vendors email</label>
                                <p className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d] cursor-not-allowed">{email}</p>
                            </div>
                            <div className="w-full md:w-1/2 px-3 mb-6">
                                <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='vendor_phone'>Vendors Phone</label>
                                <p className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d] cursor-not-allowed">{phone}</p>
                            </div>
                    </div>

                    <div className='flex flex-col md:flex-row w-full'>
                        <div className="w-full px-3 mb-6">
                            <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2 mr-2" htmlFor='Bank_name'>Bank Name</label>
                            <p className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d] cursor-not-allowed" 
                            >{readBank}</p>
                        </div>
                    </div>
                    <div className='flex flex-col md:flex-row w-full'>
                        <div className="w-full md:w-1/2 px-3 mb-6">
                            <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='vendor_account_no'>Bank account number</label>
                            <div className='flex flex-row'>
                                <p className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d] cursor-not-allowed" 
                                >{readAccountNo}</p>
                            </div>
                        </div>
                        <div className="w-full md:w-1/2 px-3 mb-6">
                            <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='vendor_account_name'>Vendors Account Name</label>
                            <p className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d] cursor-not-allowed" 
                            >{accountName}</p>
                        </div>
                    </div>

                    <div className="w-full px-3 mb-6">
                        <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='vendor_business_address'>Vendors Business Address</label>
                        <p className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d] cursor-not-allowed">{address}</p>
                    </div>

                    <div className='flex flex-col md:flex-row w-full'>
                        <div className="w-full md:w-1/2 px-3 mb-6">
                            <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='business_state'>State</label>                                
                            <p className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d] cursor-not-allowed">{readState}</p>
                        </div>
                        <div className="w-full md:w-1/2 px-3 mb-6">
                            <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='vendor_last_name'>City</label>
                            <p className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d] cursor-not-allowed" 
                            >{readCity}</p>
                        </div>
                    </div>

                    <div className="w-full px-3 mb-6">
                        <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='name'>Business Name</label>
                        <p className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d]" name="vendor_business_name" placeholder="Enter Business Name">{vendorsName}</p>
                    </div>
                    
                    <div className="w-full px-3 mb-6">
                        <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='description'>Business Description</label>
                        <div className="w-full overflow-x-auto mx-3">
                            <div className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d]" dangerouslySetInnerHTML={{ __html: vendorsDescription }}/>
                        </div>
                    </div>
                   
                    <div className="flex justify-center w-full px-3 mb-12">
                        <label className="cursor-pointer flex w-fit max-w-lg flex-col items-center justify-start rounded-xl border-2 border-dashed border-green-400 bg-white p-6" htmlFor='vendor_image'>Vendor Image
                            <div className="w-full mx-12 flex justify-center mb-5">
                            <img src={`${CONSTANT.IMAGE_STORE}/${vendortImage}`} className={`w-32 h-32 $`}/>
                            </div>
                        </label>
                    </div>
                    <div className="w-full flex flex-row px-3 mb-6">
                    <Link to={`${ROUTE.ADMIN_EDIT_VENDORS}/${id}/${slug}`} className="appearance-none w-1/2  block bg-gray-700 text-gray-100 font-bold border border-gray-200 rounded-lg py-3 px-3 leading-tight hover:bg-gray-600 focus:outline-none focus:bg-white focus:border-gray-500 text-center">Edit Vendor</Link>
                    {status==0 ?
                        <button className="appearance-none w-1/2 block bg-green-700 text-gray-100 font-bold border border-gray-200 rounded-lg py-3 px-3 leading-tight hover:bg-green-600 focus:outline-none focus:bg-white focus:border-gray-500 text-center" onClick={() => verifyVendor(id)}> Verify Vendor</button>
                        :
                        <button className="appearance-none w-1/2 block bg-red-700 text-gray-100 font-bold border border-gray-200 rounded-lg py-3 px-3 leading-tight hover:bg-red-600 focus:outline-none focus:bg-white focus:border-gray-500 text-center" onClick={() => unVerifyVendor(id)}> Unverify Vendor</button>
                    
                    }
                    </div>
                </div>
            </form>          
        </div> 
        )
        }      
    </div>
  )
}
export default @@PageName@@;
 """
 layouts["layout_admin_view_vendor"] = layout_admin_view_vendor


 layout_datatables ="""
import React, { useState, useEffect } from 'react';
@@Imports@@
function @@PageName@@(){
    const [blogs, fetchBlogs] = useState([]);
    const [loading, setLoading] = useState(false);

    const getData = () => {
        setLoading(true)
        fetch(`${ROUTE.BLOGS_API}/blogs`)
            .then((res) => res.json())
            .then((res) => {
            fetchBlogs(res.results)
            console.log(res.results)
            setLoading(false)
        })
    }
    useEffect(() => {
        getData()
    }, []);

    const dataSet = blogs.map((blog) => ([
        blog.title,
        blog.summary,
        blog.slug,
        blog.created_at  
    ]));

      let blogsLoading = (
      <>
          <section className="bg-gray-100 pt-20 md:pt-30">
              <div className="px-36 py-[100px] pb-[80px] luday_wrap">                    
                  <div className="grid grid-cols-3 gap-9 luday_grid_wrap"> 
                      <div className="group bg-white">    
                          <article>
                              <div data-placeholder className="w-full h-60 bg-gray-200 overflow-hidden relative">
                              </div>
                              <div className="p-[30px]">
                                  <p data-placeholder className="h-7 mb-2 w-full md:w-4/5 bg-gray-200 overflow-hidden relative"></p>
                                  <div>
                                      <p  data-paceholder className="h-6 py-3 font-bold text-sm"></p>
                                  </div>
                                  <div data-placeholder className="w-full h-32 bg-gray-200 overflow-hidden relative">
                                  </div>
                              </div>
                          </article>
                      </div>
                      <div className="group bg-white">    
                          <article>
                              <div data-placeholder className="w-full h-60 bg-gray-200 overflow-hidden relative">
                              </div>
                              <div className="p-[30px]">
                                  <p data-placeholder className="h-7 mb-2 w-full md:w-4/5 bg-gray-200 overflow-hidden relative"></p>
                                  <div>
                                      <p  data-paceholder className="h-6 py-3 font-bold text-sm"></p>
                                  </div>
                                  <div data-placeholder className="w-full h-32 bg-gray-200 overflow-hidden relative">
                                  </div>
                              </div>
                          </article>
                      </div>
                      <div className="group bg-white">    
                          <article>
                              <div data-placeholder className="w-full h-60 bg-gray-200 overflow-hidden relative">
                              </div>
                              <div className="p-[30px]">
                                  <p data-placeholder className="h-7 mb-2 w-full md:w-4/5 bg-gray-200 overflow-hidden relative"></p>
                                  <div>
                                      <p  data-paceholder className="h-6 py-3 font-bold text-sm"></p>
                                  </div>
                                  <div data-placeholder className="w-full h-32 bg-gray-200 overflow-hidden relative">
                                  </div>
                              </div>
                          </article>
                      </div>
                  </div>
              </div>
          </section>
      </>
    )

    return (
      <div>
        <br />
        <h2>@@PageTitle@@</h2>
        { loading ? 
            blogsLoading : 
            <Tbl data={dataSet}></Tbl>
        }
      </div>
    )
}
export default @@PageName@@;
 """
 layouts["layout_datatables"] = layout_datatables


 layout_datatables_tbl ="""
@@Imports@@
import React, { Component } from 'react';

const $ = require('jquery')
$.DataTable = require('datatables.net')

class @@PageName@@ extends Component{
    componentDidMount(){
        // console.log(this.el)
        this.$el = $(this.el)
        this.$el.DataTable(
            {
                data: this.props.data,
                columns: [
                    { title: 'Title' },
                    { title: 'Summary' },
                    { title: 'Slug' },
                    { title: 'Created at' }
                ]
            }
        )
    }
    componentWillUnmount(){
        this.$el.DataTable.destroy(true)
    }

    render(){
        return (
            <section className="bg-gray-50 pt-20 md:pt-30">
                <div className="bg-white mx-36 my-[100px] p-[22px] luday_wrap rounded drop-shadow-lg">
                    <table id="example" className="display" width="100%" 
                        ref={ el => this.el = el }>
                    </table>
                </div>
                <br /><br />
            </section>
        )
    }
}

Tbl.propTypes = {
    data: PropType.object.isRequired
};
export default @@PageName@@;
 """
 layouts["layout_datatables_tbl"] = layout_datatables_tbl

# Users Guide layout

 layout_usersguide ="""
@@Imports@@
const @@PageName@@ = () => { 
    const title = '@@AppTitle@@';
    const subtitle = '@@PageTitle@@';
    useDocumentTitle('@@PageTitle@@ | BestDealNaija');
    useScrollTop();
    const [check, setCheck] = useState(null);
    
    const guide = () => {
        setCheck(<Topic />);
    } 
    const guide2 = () => {
      setCheck(<Topic2 />);
    }
    const guide3 = () => {
      setCheck(<Topic3 />);
    }
    const guide4 = () => {
        setCheck(<Topic4 />);
    }
    const guide5 = () => {
        setCheck(<Topic5 />);
    }

    return (
      <>
        <Banner backgroundImage={bannerImage} titleText={title} subtitleText={subtitle} /> 
        <section className="pt-20 md:pt-30">
            <div className="lg:px-16"> 

                <div className="grid grid-cols-5 gap-9 luday_grid_wrap"> 
                    <div className="group col-span-2"> 

                    <div id="accordion-arrow-icon" data-accordion="open">
                        <p className="text-xl" id="accordion-arrow-icon-heading-1">
                            <button type="button" className="bg-primary text-black flex items-center justify-between w-full p-5 font-medium text-left text-gray-900 bg-gray-100 border border-b-0 border-gray-200 rounded-t-xl focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800 dark:border-gray-700 dark:text-white dark:bg-gray-800 hover:bg-gray-100 dark:hover:bg-gray-800" data-accordion-target="#accordion-arrow-icon-body-1" aria-expanded="true" aria-controls="accordion-arrow-icon-body-1">
                            <span>@@Topic1Title@@</span>
                            <svg data-accordion-icon className="w-6 h-6 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M15 13l-3 3m0 0l-3-3m3 3V8m0 13a9 9 0 110-18 9 9 0 010 18z"></path></svg>
                            </button>
                        </p>
                        <div id="accordion-arrow-icon-body-1" aria-labelledby="accordion-arrow-icon-heading-1">
                            <div className="p-5 font-light border border-b-0 border-gray-200 dark:border-gray-700 dark:bg-gray-900">
                                <p>@@Topic1SubTitle@@</p>
                                <li><a onClick={guide} href="#1.1" className="accordion_links">@@Topic1Link1@@</a></li>
                                <li><a onClick={guide} href="#1.2" className="accordion_links">@@Topic1Link2@@</a></li>
                                <li><a onClick={guide} href="#1.3" className="accordion_links">@@Topic1Link3@@</a></li>
                                <li><a onClick={guide} href="#1.4" className="accordion_links">@@Topic1Link4@@</a></li>
                                <li><a onClick={guide} href="#1.5" className="accordion_links">@@Topic1Link5@@</a></li>
                                <li><a onClick={guide} href="#1.6" className="accordion_links">@@Topic1Link6@@</a></li>
                                <li><a onClick={guide} href="#1.7" className="accordion_links">@@Topic1Link7@@</a></li>
                                <li><a onClick={guide} href="#1.8" className="accordion_links">@@Topic1Link8@@</a></li>
                                <li><a onClick={guide} href="#1.9" className="accordion_links">@@Topic1Link9@@</a></li>
                                <li><a onClick={guide} href="#1.10" className="accordion_links">@@Topic1Link10@@</a></li>
                                <li><a onClick={guide} href="#1.11" className="accordion_links">@@Topic1Link11@@</a></li>
                            </div>
                        </div>
                        <p className="text-xl" id="accordion-arrow-icon-heading-2">
                            <button type="button" className="bg-primary text-black flex items-center justify-between w-full p-5 font-medium text-left text-gray-500 border border-b-0 border-gray-200 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800 dark:border-gray-700 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800" data-accordion-target="#accordion-arrow-icon-body-2" aria-expanded="false" aria-controls="accordion-arrow-icon-body-2">
                            <span>@@Topic2Title@@</span>
                            <svg data-accordion-icon className="w-6 h-6 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M15 13l-3 3m0 0l-3-3m3 3V8m0 13a9 9 0 110-18 9 9 0 010 18z"></path></svg>
                            </button>
                        </p>
                        <div id="accordion-arrow-icon-body-2" className="hidden" aria-labelledby="accordion-arrow-icon-heading-2">
                            <div className="p-5 font-light border border-b-0 border-gray-200 dark:border-gray-700">
                                <li><a onClick={guide2} href="#2.1" className="accordion_links">@@Topic2Link1@@</a></li>
                                <li><a onClick={guide2} href="#2.2" className="accordion_links">@@Topic2Link2@@</a></li>
                                <li><a onClick={guide2} href="#2.3" className="accordion_links">@@Topic2Link3@@</a></li>
                                <li><a onClick={guide2} href="#2.4" className="accordion_links">@@Topic2Link4@@</a></li>
                                <li><a onClick={guide2} href="#2.5" className="accordion_links">@@Topic2Link5@@</a></li>
                                <li><a onClick={guide2} href="#2.6" className="accordion_links">@@Topic2Link6@@</a></li>
                                <li><a onClick={guide2} href="#2.7" className="accordion_links">@@Topic2Link7@@</a></li>
                                <li><a onClick={guide2} href="#2.8" className="accordion_links">@@Topic2Link8@@</a></li>
                                <li><a onClick={guide2} href="#2.9" className="accordion_links">@@Topic2Link9@@</a></li>
                                <li><a onClick={guide2} href="#2.10" className="accordion_links">@@Topic2Link10@@</a></li>
                            </div>
                        </div>
                        <p className="text-xl" id="accordion-arrow-icon-heading-3">
                            <button type="button" className="bg-primary text-black flex items-center justify-between w-full p-5 font-medium text-left text-gray-500 border border-gray-200 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800 dark:border-gray-700 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800" data-accordion-target="#accordion-arrow-icon-body-3" aria-expanded="false" aria-controls="accordion-arrow-icon-body-3">
                            <span>@@Topic3Title@@</span>
                            <svg data-accordion-icon className="w-6 h-6 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M15 13l-3 3m0 0l-3-3m3 3V8m0 13a9 9 0 110-18 9 9 0 010 18z"></path></svg>
                            </button>
                        </p>
                        <div id="accordion-arrow-icon-body-3" className="hidden" aria-labelledby="accordion-arrow-icon-heading-3">
                            <div className="p-5 font-light border border-t-0 border-gray-200 dark:border-gray-700">
                                <li><a onClick={guide3} href="#3.1" className="accordion_links">@@Topic3Link1@@</a></li>
                                <li><a onClick={guide3} href="#3.2" className="accordion_links">@@Topic3Link2@@</a></li>
                                <li><a onClick={guide3} href="#3.3" className="accordion_links">@@Topic3Link3@@</a></li>
                                <li><a onClick={guide3} href="#3.4" className="accordion_links">@@Topic3Link4@@</a></li>
                                <li><a onClick={guide3} href="#3.5" className="accordion_links">@@Topic3Link5@@</a></li>  
                                <li><a onClick={guide3} href="#3.6" className="accordion_links">@@Topic3Link6@@</a></li>
                                <li><a onClick={guide3} href="#3.7" className="accordion_links">@@Topic3Link7@@</a></li>
                                <li><a onClick={guide3} href="#3.8" className="accordion_links">@@Topic3Link8@@</a></li>
                                <li><a onClick={guide3} href="#3.9" className="accordion_links">@@Topic3Link9@@</a></li>
                                <li><a onClick={guide3} href="#3.10" className="accordion_links">@@Topic3Link10@@</a></li>
                                <li><a onClick={guide3} href="#3.11" className="accordion_links">@@Topic3Link11@@</a></li>
                            </div>
                        </div>
                        <p className="text-xl" id="accordion-arrow-icon-heading-4">
                            <button type="button" className="bg-primary text-black flex items-center justify-between w-full p-5 font-medium text-left text-gray-500 border border-gray-200 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800 dark:border-gray-700 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800" data-accordion-target="#accordion-arrow-icon-body-4" aria-expanded="false" aria-controls="accordion-arrow-icon-body-4">
                            <span>@@Topic4Title@@</span>
                            <svg data-accordion-icon className="w-6 h-6 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M15 13l-3 3m0 0l-3-3m3 3V8m0 13a9 9 0 110-18 9 9 0 010 18z"></path></svg>
                            </button>
                        </p>
                        <div id="accordion-arrow-icon-body-4" className="hidden" aria-labelledby="accordion-arrow-icon-heading-4">
                            <div className="p-5 font-light border border-t-0 border-gray-200 dark:border-gray-700">
                                <li><a onClick={guide4} href="#4.1" className="accordion_links">@@Topic4Link1@@</a></li>
                                <li><a onClick={guide4} href="#4.2" className="accordion_links">@@Topic4Link2@@</a></li>
                                <li><a onClick={guide4} href="#4.3" className="accordion_links">@@Topic4Link3@@</a></li>
                                <li><a onClick={guide4} href="#4.4" className="accordion_links">@@Topic4Link4@@</a></li>
                                <li><a onClick={guide4} href="#4.5" className="accordion_links">@@Topic4Link5@@</a></li>  
                                <li><a onClick={guide4} href="#4.6" className="accordion_links">@@Topic4Link6@@</a></li>
                            </div>
                        </div>
                        <p className="text-xl" id="accordion-arrow-icon-heading-5">
                            <button type="button" className="bg-primary text-black flex items-center justify-between w-full p-5 font-medium text-left text-gray-500 border border-gray-200 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800 dark:border-gray-700 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800" data-accordion-target="#accordion-arrow-icon-body-5" aria-expanded="false" aria-controls="accordion-arrow-icon-body-5">
                            <span>@@Topic5Title@@</span>
                            <svg data-accordion-icon className="w-6 h-6 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M15 13l-3 3m0 0l-3-3m3 3V8m0 13a9 9 0 110-18 9 9 0 010 18z"></path></svg>
                            </button>
                        </p>
                        <div id="accordion-arrow-icon-body-4" className="hidden" aria-labelledby="accordion-arrow-icon-heading-5">
                            <div className="p-5 font-light border border-t-0 border-gray-200 dark:border-gray-700">
                                <li><a onClick={guide5} href="#5.1" className="accordion_links">@@Topic5Link1@@</a></li>
                                <li><a onClick={guide5} href="#5.1" className="accordion_links">@@Topic5Link2@@</a></li>
                                <li><a onClick={guide5} href="#5.1" className="accordion_links">@@Topic5Link3@@</a></li>
                                <li><a onClick={guide5} href="#5.1" className="accordion_links">@@Topic5Link4@@</a></li>
                                <li><a onClick={guide5} href="#5.1" className="accordion_links">@@Topic5Link5@@</a></li>
                                <li><a onClick={guide5} href="#5.1" className="accordion_links">@@Topic5Link6@@</a></li>
                                <li><a onClick={guide5} href="#5.1" className="accordion_links">@@Topic5Link7@@</a></li>
                            </div>
                        </div>
                      </div>                 
                    </div>
                    <div className="group col-span-3"> 
                    <div className="p-[15px]">    
                        <h1 className="userguide_header text-green-600">@@PageTitle@@</h1>  
                        {check}    
                    </div>
                    </div>
                </div>
            </div>
        </section>
      </>
    );
}
export default @@PageName@@;
 """
 layouts["layout_usersguide"] = layout_usersguide


# Owners Guide layout

 layout_ownersguide ="""
@@Imports@@
const @@PageName@@ = () => { 
    const title = '@@AppTitle@@';
    const subtitle = '@@PageTitle@@';
    useDocumentTitle('@@PageTitle@@ | BestDealNaija');
    useScrollTop();
    const [check, setCheck] = useState(null);
    
    const guide = () => {
        setCheck(<Owners_Topic />);
    } 
    const guide2 = () => {
      setCheck(<Owners_Topic2 />);
    }
    const guide3 = () => {
        setCheck(<Owners_Topic3 />);
    } 
    const guide4 = () => {
      setCheck(<Owners_Topic4 />);
    }
    const guide5 = () => {
        setCheck(<Owners_Topic5 />);
    } 
    const guide6 = () => {
      setCheck(<Owners_Topic6 />);
    }

    return (
      <>
        <Banner backgroundImage={bannerImage} titleText={title} subtitleText={subtitle} /> 
        <section className="pt-20 md:pt-30">
            <div className="lg:px-16"> 

                <div className="grid grid-cols-5 gap-9 luday_grid_wrap"> 
                    <div className="group col-span-2">
                    <div id="accordion-arrow-icon" data-accordion="open">
                        <p className="text-xl" id="accordion-arrow-icon-heading-1">
                            <button type="button" className="bg-primary text-black flex items-center justify-between w-full p-5 font-medium text-left text-gray-900 bg-gray-100 border border-b-0 border-gray-200 rounded-t-xl focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800 dark:border-gray-700 dark:text-white dark:bg-gray-800 hover:bg-gray-100 dark:hover:bg-gray-800" data-accordion-target="#accordion-arrow-icon-body-1" aria-expanded="true" aria-controls="accordion-arrow-icon-body-1">
                            <span>@@Owners_Topic1Title@@</span>
                            <svg data-accordion-icon className="w-6 h-6 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M15 13l-3 3m0 0l-3-3m3 3V8m0 13a9 9 0 110-18 9 9 0 010 18z"></path></svg>
                            </button>
                        </p>
                        <div id="accordion-arrow-icon-body-1" aria-labelledby="accordion-arrow-icon-heading-1">
                            <div className="p-5 font-light border border-b-0 border-gray-200 dark:border-gray-700 dark:bg-gray-900">
                                <p>@@Owners_Topic1SubTitle@@</p>
                                <li><a onClick={guide} href="#1.1" className="accordion_links">@@Owners_Topic1Link1@@</a></li>
                                <li><a onClick={guide} href="#1.2" className="accordion_links">@@Owners_Topic1Link2@@</a></li>
                                <li><a onClick={guide} href="#1.3" className="accordion_links">@@Owners_Topic1Link3@@</a></li>
                                <li><a onClick={guide} href="#1.4" className="accordion_links">@@Owners_Topic1Link4@@</a></li>
                                <li><a onClick={guide} href="#1.5" className="accordion_links">@@Owners_Topic1Link5@@</a></li>
                                <li><a onClick={guide} href="#1.6" className="accordion_links">@@Owners_Topic1Link6@@</a></li>
                            </div>
                        </div>
                        <p className="text-xl" id="accordion-arrow-icon-heading-2">
                            <button type="button" className="bg-primary text-black flex items-center justify-between w-full p-5 font-medium text-left text-gray-500 border border-b-0 border-gray-200 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800 dark:border-gray-700 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800" data-accordion-target="#accordion-arrow-icon-body-2" aria-expanded="false" aria-controls="accordion-arrow-icon-body-2">
                            <span>@@Owners_Topic2Title@@</span>
                            <svg data-accordion-icon className="w-6 h-6 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M15 13l-3 3m0 0l-3-3m3 3V8m0 13a9 9 0 110-18 9 9 0 010 18z"></path></svg>
                            </button>
                        </p>
                        <div id="accordion-arrow-icon-body-2" className="hidden" aria-labelledby="accordion-arrow-icon-heading-2">
                            <div className="p-5 font-light border border-b-0 border-gray-200 dark:border-gray-700">
                                <li><a onClick={guide2} href="#2.1" className="accordion_links">@@Owners_Topic2Link1@@</a></li>
                                <li><a onClick={guide2} href="#2.2" className="accordion_links">@@Owners_Topic2Link2@@</a></li>
                                <li><a onClick={guide2} href="#2.3" className="accordion_links">@@Owners_Topic2Link3@@</a></li>
                                <li><a onClick={guide2} href="#2.4" className="accordion_links">@@Owners_Topic2Link4@@</a></li>
                                <li><a onClick={guide2} href="#2.5" className="accordion_links">@@Owners_Topic2Link5@@</a></li>
                                <li><a onClick={guide2} href="#2.6" className="accordion_links">@@Owners_Topic2Link6@@</a></li>
                                <li><a onClick={guide2} href="#2.7" className="accordion_links">@@Owners_Topic2Link7@@</a></li>
                            </div>
                        </div>


                        <p className="text-xl" id="accordion-arrow-icon-heading-2">
                            <button type="button" className="bg-primary text-black flex items-center justify-between w-full p-5 font-medium text-left text-gray-500 border border-b-0 border-gray-200 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800 dark:border-gray-700 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800" data-accordion-target="#accordion-arrow-icon-body-2" aria-expanded="false" aria-controls="accordion-arrow-icon-body-2">
                            <span>@@Owners_Topic3Title@@</span>
                            <svg data-accordion-icon className="w-6 h-6 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M15 13l-3 3m0 0l-3-3m3 3V8m0 13a9 9 0 110-18 9 9 0 010 18z"></path></svg>
                            </button>
                        </p>
                        <div id="accordion-arrow-icon-body-2" className="hidden" aria-labelledby="accordion-arrow-icon-heading-2">
                            <div className="p-5 font-light border border-b-0 border-gray-200 dark:border-gray-700">
                                <li><a onClick={guide3} href="#3.1" className="accordion_links">@@Owners_Topic3Link1@@</a></li>
                                <li><a onClick={guide3} href="#3.2" className="accordion_links">@@Owners_Topic3Link2@@</a></li>
                                <li><a onClick={guide3} href="#3.3" className="accordion_links">@@Owners_Topic3Link3@@</a></li>
                                <li><a onClick={guide3} href="#3.4" className="accordion_links">@@Owners_Topic3Link4@@</a></li>
                                <li><a onClick={guide3} href="#3.5" className="accordion_links">@@Owners_Topic3Link5@@</a></li>
                                <li><a onClick={guide3} href="#3.6" className="accordion_links">@@Owners_Topic3Link6@@</a></li>
                            </div>
                        </div>
                        <p className="text-xl" id="accordion-arrow-icon-heading-2">
                            <button type="button" className="bg-primary text-black flex items-center justify-between w-full p-5 font-medium text-left text-gray-500 border border-b-0 border-gray-200 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800 dark:border-gray-700 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800" data-accordion-target="#accordion-arrow-icon-body-2" aria-expanded="false" aria-controls="accordion-arrow-icon-body-2">
                            <span>@@Owners_Topic4Title@@</span>
                            <svg data-accordion-icon className="w-6 h-6 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M15 13l-3 3m0 0l-3-3m3 3V8m0 13a9 9 0 110-18 9 9 0 010 18z"></path></svg>
                            </button>
                        </p>
                        <div id="accordion-arrow-icon-body-2" className="hidden" aria-labelledby="accordion-arrow-icon-heading-2">
                            <div className="p-5 font-light border border-b-0 border-gray-200 dark:border-gray-700">
                                <li><a onClick={guide4} href="#4.1" className="accordion_links">@@Owners_Topic4Link1@@</a></li>
                                <li><a onClick={guide4} href="#4.2" className="accordion_links">@@Owners_Topic4Link2@@</a></li>
                                <li><a onClick={guide4} href="#4.3" className="accordion_links">@@Owners_Topic3Link3@@</a></li>
                                <li><a onClick={guide4} href="#4.4" className="accordion_links">@@Owners_Topic4Link4@@</a></li>
                            </div>
                        </div>

                        <p className="text-xl" id="accordion-arrow-icon-heading-2">
                            <button type="button" className="bg-primary text-black flex items-center justify-between w-full p-5 font-medium text-left text-gray-500 border border-b-0 border-gray-200 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800 dark:border-gray-700 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800" data-accordion-target="#accordion-arrow-icon-body-2" aria-expanded="false" aria-controls="accordion-arrow-icon-body-2">
                            <span>@@Owners_Topic5Title@@</span>
                            <svg data-accordion-icon className="w-6 h-6 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M15 13l-3 3m0 0l-3-3m3 3V8m0 13a9 9 0 110-18 9 9 0 010 18z"></path></svg>
                            </button>
                        </p>
                        <div id="accordion-arrow-icon-body-2" className="hidden" aria-labelledby="accordion-arrow-icon-heading-2">
                            <div className="p-5 font-light border border-b-0 border-gray-200 dark:border-gray-700">
                                <li><a onClick={guide5} href="#5.1" className="accordion_links">@@Owners_Topic5Link1@@</a></li>
                                <li><a onClick={guide5} href="#5.2" className="accordion_links">@@Owners_Topic5Link2@@</a></li>
                                <li><a onClick={guide5} href="#5.3" className="accordion_links">@@Owners_Topic5Link3@@</a></li>
                                <li><a onClick={guide5} href="#5.4" className="accordion_links">@@Owners_Topic5Link4@@</a></li>
                                <li><a onClick={guide4} href="#5.5" className="accordion_links">@@Owners_Topic5Link3@@</a></li>
                                <li><a onClick={guide5} href="#5.6" className="accordion_links">@@Owners_Topic5Link4@@</a></li>
                            </div>
                        </div>

                        <p className="text-xl" id="accordion-arrow-icon-heading-2">
                            <button type="button" className="bg-primary text-black flex items-center justify-between w-full p-5 font-medium text-left text-gray-500 border border-b-0 border-gray-200 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800 dark:border-gray-700 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800" data-accordion-target="#accordion-arrow-icon-body-2" aria-expanded="false" aria-controls="accordion-arrow-icon-body-2">
                            <span>@@Owners_Topic6Title@@</span>
                            <svg data-accordion-icon className="w-6 h-6 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M15 13l-3 3m0 0l-3-3m3 3V8m0 13a9 9 0 110-18 9 9 0 010 18z"></path></svg>
                            </button>
                        </p>
                        <div id="accordion-arrow-icon-body-2" className="hidden" aria-labelledby="accordion-arrow-icon-heading-2">
                            <div className="p-5 font-light border border-b-0 border-gray-200 dark:border-gray-700">
                                <li><a onClick={guide6} href="#6.1" className="accordion_links">@@Owners_Topic6Link1@@</a></li>
                                <li><a onClick={guide6} href="#6.2" className="accordion_links">@@Owners_Topic6Link2@@</a></li>
                                <li><a onClick={guide6} href="#6.3" className="accordion_links">@@Owners_Topic6Link3@@</a></li>
                                <li><a onClick={guide6} href="#6.4" className="accordion_links">@@Owners_Topic6Link4@@</a></li>
                            </div>
                        </div>

                      </div>                 
                    </div>
                    <div className="group col-span-3"> 
                    <div className="p-[15px]">    
                        <h1 className="userguide_header text-green-600">@@PageTitle@@</h1>  
                        {check}    
                    </div>
                    </div>
                </div>
            </div>
        </section>
      </>
    );
}
export default @@PageName@@;
 """
 layouts["layout_ownersguide"] = layout_ownersguide

 """
 AdminDashboard layout 1
 """
 layout_admin_dashboard_1 ="""
import React, { Suspense } from 'react';
@@Imports@@

const Dashboard = React.lazy(() => import('./components/Dashboard'));

const @@PageName@@ = () => {
    const isLoading = useSelector((state) => state.app.loading);
    return (
        <div>
        <Suspense fallback={(
            <div className="loader" style={{ minHeight: '80vh' }}>
            <h6>@@LoadingPageText@@</h6>
            <br />
            <LoadingOutlined />
            </div>
        )}>
            <Dashboard isLoading={isLoading} />
        </Suspense>
        </div>
    );
}

export default @@PageName@@;
 """
 layouts["layout_admin_dashboard_1"] = layout_admin_dashboard_1


 """
 Layout example to be copied for use and replaced
 """
 layout_example_1 ="""
import React from 'react';
@@Imports@@
const @@PageName@@ = () => {
  useDocumentTitle('@@DocumentTitle@@');
  useScrollTop();
}
export default @@PageName@@;
 """
 layouts["layout_example_1"] = layout_example_1
 