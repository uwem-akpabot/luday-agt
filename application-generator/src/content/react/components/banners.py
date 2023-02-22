class Banners:

 banner = {}

 '''
 

 '''
 default ="""
import React from 'react';
import PropType from 'prop-types';

import './styles/banner.css';

const Banner = ({ backgroundImage, titleText, subtitleText }) => {
    return (
        <section>
            <div className="bg_overlay" style={{ 
                background: `linear-gradient(rgba(242, 238, 238, 0.4),rgba(0,0,0,.4)),url("${backgroundImage}") center `
                }}>
                <div className="container">
                    <div className="hero_inner">
                        <div className="text-center">
                            <p dangerouslySetInnerHTML={{ __html: titleText }} className="tracking-widest mb-2.5 text-xs text-white"></p>
                            <h1 dangerouslySetInnerHTML={{ __html: subtitleText }} className="text-3xl md:text-6xl font-semibold tracking-tight text-white overflow-hidden text-ellipsis drop-shadow-md"></h1>
                        </div>
                    </div>
                </div>
            </div>
            {/* <div className="bg_overlay" style={{ 
                background: `linear-gradient(rgba(242, 238, 238, 0.4),rgba(0,0,0,.4)),url("${backgroundImage + "?width=1920"}") center center`
                }}>
                <div className="container">
                    <div className="hero_inner">
                        <div className="text-center">
                            <p dangerouslySetInnerHTML={{ __html: titleText }} className="tracking-widest mb-2.5 text-xs text-white"></p>
                            <h1 dangerouslySetInnerHTML={{ __html: subtitleText }} className="text-3xl md:text-6xl font-semibold tracking-tight text-white overflow-hidden text-ellipsis drop-shadow-md"></h1>
                        </div>
                    </div>
                </div>
            </div> */}
        </section>
    )
}

Banner.defaultProps = {
    backgroundImage: '',
    titleText: '@@DefaultPropstitleText@@'
};

Banner.propTypes = {
    backgroundImage: PropType.string,
    titleText: PropType.string,
    subtitleText: PropType.string
};

export default Banner
 """
 banner["default"] = default
 
 '''
 

 '''
 default_1 ="""

 """
 banner["default_1"] = default_1
 '''
 

 '''
 