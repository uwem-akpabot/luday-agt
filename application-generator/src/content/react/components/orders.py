class Orders:

 orders = {}
 
 '''
 Order deatials component 1
 '''
 order_details_1 ="""
import React from 'react';
import PropType from 'prop-types';
import * as CONSTANT from "../../../constants/constants"
import { displayMoney } from '../../../helpers/utils';
const @@PageName@@ = ({order, isLoading}) => {
  const nf = new Intl.NumberFormat();
	return (
		<>
			{order.length === 0 ? (
				<>
					<div className="text-center py-[50px] my-4">   
						<div className="text-center py-10 mt-20 md:mt-4">
							<p className="text-lg">{isLoading ? '@@OnScreenLoadingText@@' : '@@EmptyRecordMssg@@'}</p>
						</div>
					</div>
				</>
            ) : (
			<div className="py-2 px-[10px] mt-10 md:px-[60px] lg:px-[90px]">
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
										<th className="px-6 py-2">@@TableHead5@@</th>
									</tr>
								</thead>
								<tbody>
								{order.products?.map(product => (  
									<tr key={product.id} className="border border-black-600 whitespace-nowrap">
										<td className="">
											<div className="flex flex-row">
												<div className="bg-white py-2 h-30 w-32">
													<img className="h-32 w-32" src={`${CONSTANT.IMAGE_STORE}/${product.product_image_path}`}/> 
												</div>
												<div className="bg-white py-2">
													<h4 className="px-6 text-left">{product.name}</h4>
													<span className="pl-6 py-2 text-left text-sm font-bold text-[#9c0]">
														@@SkuText@@: </span>{product.product_sku}
												</div>
											</div>
										</td>										
										<td className="px-6 py-2 text-right">&#8358;{nf.format(product.price)}</td>
										<td className="px-6 py-2 text-right">{nf.format(product.quantity)}</td>
										<td className="text-center"><span className="bg-green-200 text-green-800 px-2 py-1 rounded-full">{order.status}</span></td>
										<td className="px-6 py-2 text-right">&#8358;{nf.format(product.price * product.quantity)}</td>
									</tr>
								))}
								</tbody>
							</table>
						</div>
					</div>
					<div className="w-full md:w-1/4 m-2 border border-black-600 drop-shadow-md p-5 h-1/2">
						<h2 className="text-2xl mb-5">@@SubHeading2@@</h2>
						<p>@@paragraph2@@ <span>#{order.id}</span></p>
						<p className="mb-5">@@SubtotalParagraphText@@ <span>
								&#8358;{displayMoney(order.amount)}
							</span>
						</p>
						<hr/>
						<h2 className="text-2xl mt-5">@@GrandTotalHeading2Text@@</h2>
						<h2 className="text-3xl mt-5 font-bold">
						&#8358;{displayMoney(order.amount)}
						</h2>
					</div>
				</div>
			</div>			
			)}
		</>
	);  
};

@@PageName@@.propTypes = {
	order: PropType.any.isRequired,
	isLoading: PropType.bool.isRequired
  };

export default @@PageName@@;
 """
 orders["order_details_1"] = order_details_1

 # src/pages/admin/orders /Orders 
 admin_orders ="""
import React, {useState, useEffect, useCallback} from 'react';
@@imports@@

const Orders = () => {
    const [allorders, fetchAllOrders] = useState([]);
    const [sortType, setSortType] = useState([]);
    const [paymentType, setPaymentType] = useState([]);
    const [deliveryStatus, setDeliveryStatus] = useState([]);
    const [searchResult, setSearchResult] = useState('');
    const [searchData, fetchSearchData] = useState([]);
    const [searchRef, setSearchRef] = useState('');
    const [totalSum, setTotalSum] = useState('');
    //const [sortDate, setSortDate] = useState(new Date());
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
            fetchAllOrders({}); // This worked for me
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

    // const SearchOrderByDate = useCallback( async (param)  => {
    //     if (param){
    //         fetch(`${ROUTE.PRODUCTS_API}/order/date/${param}`)
    //         .then((res) => res.json())
    //         .then((res) => {
    //             fetchSearchData(res.data)
    //             setSearchResult("Success")
    //             setTotalSum((res.data.reduce((a,v) =>  a = a + v.amount , 0 )))
    //         })
    //     }
    //     else {
    //         setSearchResult('')
    //         getData()
    //     }
    // }, []);


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


    // const handleDateChange = (data) =>{
    //     setSortDate(data)
    //     SearchOrderByDate(data)
    // }


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
            <p>No Record added yet</p>
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
                            <Link to={ROUTE.VIEW_ORDERS}> <FaEye className="text-green-800 mx-2 h-5 w-5" /></Link>
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
              <p>No Record found</p>
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
                    <span className="text-base">Orders</span>
                </span>
                <span>/</span>
            </div>
        </div>
        <div className="header my-3 h-12 px-10 py-8  flex items-center justify-between">
            <h1 className="font-medium text-2xl">Orders</h1>
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
                        {
                        sortType.value == 1 ?
                            <div className="w-full md:w-2/3 px-3 mb-6">
                            <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='vendor_last_name'>Payment</label>
                            <Select defaultValue={paymentType} options={Paymentlist} onChange={handPaymentChange} className="z-50"/>
                            </div>
                        :
                        sortType.value == 2 ?
                            <div className="w-full md:w-2/3 px-3 mb-6">
                            <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='vendor_last_name'>Delivery</label>
                            <Select defaultValue={deliveryStatus} onChange={handDeliverStatusChange} options={DeliveryStatuslist} className="z-50"/>
                            </div>
                        :
                        " "
                        }
                        {/* {sortType.value == 1 ?
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
                        } */}

                    </div>
                    
                    <table className="table-auto w-full mt-3">
                        <thead className="text-sm font-semibold uppercase text-gray-800 bg-gray-50">
                            <tr className="font-semibold text-center">
                                <th>Ref ID</th>
                                <th className="p-2">User
                                </th>
                                <th className="p-2">Email
                                </th>
                                <th className="p-2">Total
                                </th>
                                <th className="p-2">Payment
                                </th>
                                <th className="p-2">Date
                                </th>
                                <th className="p-2">Status
                                </th>
                                <th className="p-2">Action
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
export default Orders;
 """
 orders["admin_orders"] = admin_orders

 # src/pages/admin/orders /ViewOrder 
 admin_view_order ="""
import React from 'react';
@@imports@@

const ViewOrder = () => {
    const { id } = useParams();
    return (
        <div className="bg-gray-100">
            <div className="header bg-white h-16 px-10 py-8 border-b-2 border-gray-200 flex items-center justify-between">
                <div className="flex items-center space-x-2 text-gray-400">
                    <span className="text-green-700 tracking-wider font-thin text-md"><Link to={ROUTE.ADMIN_DASHBOARD}>Home</Link></span>
                    <span>/</span>
                    <span className="text-green-700 tracking-wider font-thin text-md"><Link to={ROUTE.ADMIN_ORDERS}>Order</Link></span>
                    <span>/</span>
                    <span className="tracking-wide text-md">
                        <span className="text-base">Order details</span>
                    </span>
                    <span>/</span>
                </div>
            </div>
            <div className="header my-3 h-12 px-10 py-8  flex items-center justify-between">
                <h1 className="font-medium text-2xl">Order details</h1>
                <Link to={ROUTE.ADMIN_ORDERS} className="focus:outline-none text-white m-4 p-3 font-semibold rounded-md bg-green-700 hover:bg-green-600 hover:shadow-lg transition-all duration-100"> <span><FaAngleLeft className="inline-block w-5 h-5"/>
            </span> Back to orders</Link>
            </div>
            <Orderlist orderId={id}/>
        </div>
    )
}
export default ViewOrder;
 """
 orders["admin_view_order"] = admin_view_order

 # src/pages/admin/orders /ViewOrder 
 admin_order_list ="""
/* eslint-disable react/prop-types */
import React, {useState, useEffect} from 'react';
import * as ROUTE from '../../constants/routes';
import { MdOutlineProductionQuantityLimits } from "react-icons/md";
import * as CONSTANT from '../../constants/constants';

const @@PageName@@ = (props) => {
    const [orders, fetchOrders] = useState([]);
    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [email, setEmail] = useState('');
    const [phone, setPhone] = useState('');
    const [address, setAddress] = useState('');
    const [postCode, setPostCode] = useState('');
    const [readState, setReadSate] = useState('');
    const [readCity, setReadCity] = useState('');
    const [createdDate, setCreatedDate] = useState('');
    const [amount, setAmount] = useState('');
    const [oderStatus, setOderStatus] = useState('');
    const [paymentStatus, setPaymentStatus] = useState('');  
    const [products, setProducts] = useState([]);
    const nf = new Intl.NumberFormat();

    const getData = () => {
        fetch(`${ROUTE.PRODUCTS_API}/order/id?order_id=${props.orderId}`)
            .then((res) => res.json())
            .then((res) => {
                fetchOrders(res)
                setFirstName(res.first_name)
                setLastName(res.last_name)
                setEmail(res.email)
                setPhone(res.mobile_number)
                setAddress(res.address.street)
                setCreatedDate(res.created_at)
                setAmount(res.amount)
                setPostCode(res.address.postal_code)
                setReadCity(res.address.lga)
                setReadSate(res.address.ref_state)
                setOderStatus(res.delivery_status)
                setPaymentStatus(res.status)
                setProducts(res.products)
        })
    } 

    console.log(orders)
    useEffect(() => {
        getData()
    }, [])

    let orderList;
    if(products.length > 0){
        orderList = products.map((item, i) => {
            return (
                <tr key={i}>
                    <td className="p-2">
                        {item.product_sku}
                    </td>
                    <td className="p-2 w-8">
                    <img src={`${CONSTANT.IMAGE_STORE}/${item.product_image_path}`} className="w-8 h-8 mx-auto overflow-hidden" alt={item.name} />
                    </td>
                    <td className="p-2">
                        <p className="text-center">{item.name}</p>
                    </td>
                    <td className="p-2">
                    {item.quantity}
                    </td>
                    <td className="p-2">
                    &#8358;{nf.format(item.price)}
                    </td>
                    
                    <td className="p-2">
                        <p className="text-center">{ item.vendor_business_name }</p>
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

    return (
        <>
            <div className="flex flex-col mx-3 lg:flex-row ">
                <div className="w-full bg-white shadow-md p-6">
                    <div className="flex flex-wrap -mx-3 mb-6">
                        <div className='flex flex-col md:flex-row w-full'>
                            <div className="w-full md:w-1/2 px-3 mb-6">
                                <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='vendor_first_name'>@@Input1Label@@</label>
                                <p className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d] cursor-not-allowed">{firstName}</p>
                            </div>
                            <div className="w-full md:w-1/2 px-3 mb-6">
                                <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='vendor_last_name'>@@Input2Label@@</label>
                                <p className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d] cursor-not-allowed">{lastName}</p>
                            </div>
                        </div>

                        <div className='flex flex-col md:flex-row w-full'>
                                <div className="w-full md:w-1/2 px-3 mb-6">
                                    <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='vendor_email'>@@Input3Label@@</label>
                                    <p className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d] cursor-not-allowed">{email}</p>
                                </div>
                                <div className="w-full md:w-1/2 px-3 mb-6">
                                    <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='vendor_phone'>@@Input4Label@@</label>
                                    <p className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d] cursor-not-allowed">{phone}</p>
                                </div>
                        </div>

                        <div className="w-full px-3 mb-6">
                            <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='vendor_business_address'>@@Input5Label@@</label>
                            <p className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d] cursor-not-allowed">{address} {postCode}</p>
                        </div>

                        <div className='flex flex-col md:flex-row w-full'>
                            <div className="w-full md:w-1/2 px-3 mb-6">
                                <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='business_state'>@@Input6Label@@</label>                                
                                <p className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d] cursor-not-allowed">{readState}</p>
                            </div>
                            <div className="w-full md:w-1/2 px-3 mb-6">
                                <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='vendor_last_name'>@@Input7Label@@</label>
                                <p className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d] cursor-not-allowed" 
                                >{readCity}</p>
                            </div>
                        </div>

                        <div className='flex flex-col md:flex-row w-full'>
                            <div className="w-full md:w-1/2 px-3 mb-6">
                                <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='vendor_account_no'>@@Input8Label@@</label>
                                <div className='flex flex-row'>
                                    <p className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d] cursor-not-allowed" 
                                    >{createdDate}</p>
                                </div>
                            </div>
                            <div className="w-full md:w-1/2 px-3 mb-6">
                                <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='vendor_account_name'>@@Input9Label@@</label>
                                <p className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d] cursor-not-allowed" 
                                >{amount}</p>
                            </div>
                        </div>

                        <div className='flex flex-col md:flex-row w-full'>

                            <div className="w-full md:w-1/2 px-3 mb-6">
                                <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='vendor_account_name'>@@Input10Label@@</label>
                                {paymentStatus == "New" ?
                                <p className='text-center bg-blue-200 text-blue-900 px-2 py-1 rounded-md'> New</p>
                                :
                                paymentStatus == "Pending" ?
                                <p className='text-center bg-yellow-200 text-yellow-900 px-2 py-1 rounded-md'> Pending</p>
                                :
                                paymentStatus == "Failed" ?
                                <p className='text-center bg-red-200 text-red-900 px-2 py-1 rounded-md'> Failed</p>
                                :
                                paymentStatus == "Successful" ?
                                <p className='text-center bg-lime-200 text-lime-900 px-2 py-1 rounded-md'> Successful</p>
                                :
                                <p className='text-center'> Payment not initiated</p>
                                }
                               
                            </div>
                            <div className="w-full md:w-1/2 px-3 mb-6">
                                <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='vendor_account_name'>@@Input11Label@@</label>
                                {oderStatus == "Pending" ?
                                <p className=' text-center bg-red-200 text-red-800 px-2 py-1 rounded-full'> Pending</p>
                                :
                                oderStatus == "Shipped" ?
                                <p className='text-center bg-blue-200 text-blue-800 px-2 py-1 rounded-full'> Shipped</p>
                                :
                                oderStatus == "Delivered" ?
                                <p className='text-center bg-green-200 text-green-800 px-2 py-1 rounded-full'> Delivered</p>
                                :
                                <p className=''> Not Delivered</p>
                                }
                                
                            </div>
                        </div>
                    </div>
                    <div className='overflow-x-scroll'>
                        <table className="table-auto w-full mt-3">
                        <thead className="text-sm font-semibold uppercase text-gray-800 bg-gray-50">
                            <tr className="font-semibold">
                                <th className='text-left'>@@TableHead1@@</th>
                                <th className='text-center'>@@TableHead2@@</th>
                                <th className="p-2">@@TableHead3@@</th>
                                <th className="p-2 text-left">@@TableHead4@@</th>
                                <th className="p-2 text-left">@@TableHead5@@</th> 
                                <th></th> 
                                <th className="p-2">@@TableHead6@@</th>     
                                <th></th>     
                            </tr>
                        </thead>

                        <tbody className="text-sm divide-y divide-gray-100">
                        {
                            orderList
                        }
                        
                        
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
 orders["admin_order_list"] = admin_order_list

 '''
 Order example component 1
 '''
 payment_example_1 ="""
import React from 'react';
const @@PageName@@ = () => {
  useDocumentTitle('@@DocumentTitle@@');
  useScrollTop();

  
}
export default @@PageName@@;
 """
 orders["payment_example_1"] = payment_example_1