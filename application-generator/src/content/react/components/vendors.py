class Vendors:

 vendors = {}
 
 '''
 

 '''
 vendor_1 ="""
    import React from 'react';
    import { Link } from 'react-router-dom';
    import img from './images/tradefair/tradefairbg.jpg';
    

    const Vendor1 = () => {
        return (
            <>
                <section className="trade_fair_bg ">
                    <div className="bg_overlay">
                        <div className="container">
                            <div className="hero_inner">
                                <div className="text-center">
                                    <p className="tracking-widest mb-2.5 text-xs">@@PreheaderText@@</p>
                                    <h1 className="text-6xl font-semibold tracking-tight">@@HeaderText@@</h1>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>

                <section className="bg-gray-100">
                    <div className="px-3 md:px-10 lg:px-36 py-[100px] pb-[80px] luday_wrap">                    
                        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-9 luday_grid_wrap">
                            <div className="group bg-white">
                                <article>
                                    <div>
                                        <img className="lazy" src={img} alt="" />
                                    </div>
                                    <div className="p-[30px]">
                                        <div className="gis-text">
                                            <h2 className="text-2xl pb-4 font-semibold">@@PostHeaderText@@</h2>
                                            <p className="pb-7">@@Paragraph1@@</p>
                                            <div className="button-wrap">
                                                <Link to="/vendor-details" className="button button--theme 
                                                overflow-hidden bg-[#9c0] hover:bg-yellow-300 text-white text-bold transition-all ease-in-out duration-300 rounded py-3 px-7">
                                                Vendor details</Link>
                                            </div>
									    </div>
                                    </div>
                                </article>
                            </div>
                            <div className="group bg-white">
                                <article>
                                    <div>
                                        <img className="lazy" src={img} alt="" />
                                    </div>
                                    <div className="p-[30px]">
                                        <div className="gis-text">
                                            <h2 className="text-2xl pb-4 font-semibold">@@PostHeaderText@@</h2>
                                            <p className="pb-7">@@Paragraph1@@</p>
                                            <div className="button-wrap">
                                                <Link to="/vendor-details" className="button button--theme 
                                                overflow-hidden bg-[#9c0] hover:bg-yellow-300 text-white text-bold transition-all ease-in-out duration-300 rounded py-3 px-7">
                                                Vendor details</Link>
                                            </div>
									    </div>
                                    </div>
                                </article>
                            </div>
                            <div className="group bg-white">
                                <article>
                                    <div>
                                        <img className="lazy" src={img} alt="" />
                                    </div>
                                    <div className="p-[30px]">
                                        <div className="gis-text">
                                            <h2 className="text-2xl pb-4 font-semibold">@@PostHeaderText@@</h2>
                                            <p className="pb-7">@@Paragraph1@@</p>
                                            <div className="button-wrap">
                                                <Link to="/vendor-details" className="button button--theme 
                                                overflow-hidden bg-[#9c0] hover:bg-yellow-300 text-white text-bold transition-all ease-in-out duration-300 rounded py-3 px-7">
                                                Vendor details</Link>
                                            </div>
									    </div>
                                    </div>
                                </article>
                            </div>
                        </div>
                    </div>
                </section>
            </>
        );
    }

    export default Vendor1;
 """
 vendors["vendor_1"] = vendor_1