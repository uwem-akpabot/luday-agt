class Abouts:

 abouts = {}
 
 '''
 

 '''
 about_1 ="""
    import React from 'react';
    import { Link } from 'react-router-dom';
    

    const About1 = () => {
        return (
            <>
                <section className="trade_fair_bg ">
                    <div className="aboutbg_overlay">
                        <div className="container">
                            <div className="hero_inner">
                                <div className="text-center">
                                    
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
                
                <div className="pb-[80px] luday_wrap text-center content_about">
                    <div className="text-center py-10 pt-20">
                        <p className="tracking-widest text-xs text-gray-500">@@prePageTitle@@</p>
                        <h3 className="text-6xl luday_deals">@@PageTitle@@</h3>
                    </div>
                    <p><span className="font-bold">@@companywebsite@@</span> @@paragraph1@@</p>

                    <p>@@paragraph2@@</p>

                    <h6><b>@@innerheading@@</b></h6>
                    @@paragraph3@@
                </div>
                
            </>
        );
    }

    export default About1;
 """
 abouts["about_1"] = about_1

    # Add page 2
 about_2 ="""

 """
 abouts["about_2"] = about_2