class Contacts:

 contacts = {}
 
 '''
 

 '''
 contact_1 ="""
    import React from 'react';
    import { Link } from 'react-router-dom';
    import { useForm } from 'react-hook-form';
    import swal from 'sweetalert';
    

    const Contact1 = () => {
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
    return (
            <>
                <section className="mt-40">
                    <div className="hero_inner">
                        <div className="text-center">
                            <p className="tracking-widest mb-4 text-xs text-gray-200">@@prePageTitle@@</p>
                            <h3 className="text-6xl font-semibold text-white tracking-tight">@@PageTitle@@</h3>
                        </div>
                    </div>
                </section>
                <section>
                    <div className="h-5/6 my-10">
                    <div className="flex flex-col lg:flex-row-reverse justify-between lg:text-left">
                        <div className="lg:w-3/5 flex flex-col justify-center">
                        <div className="flex justify-center items-center">
                            <div className="w-full my-4">
                            
                            <form className='rounded-md shadow-2xl p-8'>
                                <h2 className="text-center text-4xl text-[#98c01d] uppercase font-bold">Send us a message</h2>
                                <div className="md:flex items-center mt-12">
                                    <div className="w-full md:w-1/2 flex flex-col">
                                        <input type="text" placeholder='Your Name' 
                                            {...register("name", { required: true, maxLength: 25 })}
                                            className="leading-none text-gray-900 p-3 focus:outline-none focus:border-[#98c01d]
                                                mt-4 bg-white border rounded border-gray-200" />
                                        {errors.name && <small className="text-red-500 text-xs italic">Your name is required</small>}
                                        {errors.name?.type === "maxLength" && <p style={{ color: "red" }}><small>Max characters should be 25 </small></p>}
                                    </div>
                                    <div className="w-full md:w-1/2 flex flex-col md:ml-6 md:mt-0 mt-4">
                                        <input type="number" placeholder='Phone' 
                                            {...register("mobile", { required: true, maxLength: 15 })}
                                            className="leading-none text-gray-900 p-3 focus:outline-none focus:border-[#98c01d] mt-4 bg-white border rounded border-gray-200"/>
                                        {errors.mobile && <small className="text-red-500 text-xs italic">Your mobile number is required</small>}
                                        {errors.mobile?.type === "maxLength" && <p style={{ color: "red" }}><small>Max characters should be 15 </small></p>}
                                    </div>
                                </div>
                                <div className="md:flex items-center mt-12">
                                    <div className="w-full md:w-1/2 flex flex-col">
                                        <input type="email" placeholder='Your Email' 
                                            {...register("email", { required: true, maxLength: 100 })}
                                            className="leading-none text-gray-900 p-3 focus:outline-none focus:border-[#98c01d] mt-4 bg-white border rounded border-gray-200" />
                                        {errors.email && <small className="text-red-500 text-xs italic">Your e-mail is required</small>}
                                        {errors.email?.type === "maxLength" && <p style={{ color: "red" }}><small>Max characters should be 100 </small></p>}
                                    </div>
                                    <div className="w-full md:w-1/2 flex flex-col md:ml-6 md:mt-0 mt-4">
                                        <input type="text" placeholder='Subject' 
                                            {...register("subject", { required: true, maxLength: 80 })}
                                            className="leading-none text-gray-900 p-3 focus:outline-none focus:border-[#98c01d] mt-4 bg-white border rounded border-gray-200"/>
                                        {errors.subject && <small className="text-red-500 text-xs italic">Subject message is required</small>}
                                        {errors.subject?.type === "maxLength" && <p style={{ color: "red" }}><small>Max characters should be 80 </small></p>}
                                    </div>
                                    
                                </div>
                                <div>
                                    <div className="w-full flex flex-col mt-8">
                                        <textarea type="text" placeholder='Message' 
                                            {...register("mssg", { required: true, maxLength: 255 })}
                                            className="h-40 text-base leading-none text-gray-900 p-3 focus:outline-none focus:border-[#98c01d] mt-4 bg-white border rounded border-gray-200"></textarea>
                                        {errors.mssg && <small className="text-red-500 text-xs italic">Message is required</small>}
                                        {errors.mssg?.type === "maxLength" && <p style={{ color: "red" }}><small>Max characters should be 255 </small></p>}
                                    </div>
                                </div>
                                <div className="flex items-center justify-center w-full">
                                    <button type='submit' 
                                        className="mt-9 font-semibold leading-none text-white py-4 px-10 bg-[#98c01d] rounded-md hover:bg-[#88af14] focus:ring-2 focus:ring-offset-2 focus:outline-none"
                                    >
                                        Send message
                                    </button>
                                </div>
                            </form>
                            </div>
                        </div>
                        </div>
                        <div className="lg:w-2/5 flex flex-col justify-center">
                        <div className="flex align-middle px-24 py-10">
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

                                @@address@@
                            </p>
                            <a 
                                href="tel:@@telephone1@@" 
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
                                
                                @@telephone1@@
                            </a>
                            <a 
                                href="tel:@@telephone2@@" 
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
                            @@telephone2@@
                            </a>
                            <a 
                                href="mailto:@@email@@" className="text-[#98c01d]"
                            >
                                <span className="inline-flex mr-3">
                                <svg 
                                    xmlns="http://www.w3.org/2000/svg" 
                                    width="24" 
                                    height="24"
                                    className="fill-[#98c01d]" contact_us
                                >
                                    <path d="M20 4H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2zm0 4.7-8 5.334L4 8.7V6.297l8 5.333 8-5.333V8.7z"></path>
                                </svg>
                                </span>
                                
                                @@email@@
                            </a>
                            <p className="">@@workhour@@</p>                          
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
                                <iframe title="Bestdeal Map" className="w-full h-[480px]" src="@@map@@" allowFullScreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
                            </div>
                        </div>
                    </div>    
                </section>
            </>
        );
    }

    export default Contact1;
 """
 contacts["contact_1"] = contact_1

    # Add page 2
 contact_2 ="""

 """
 contacts["contact_2"] = contact_2