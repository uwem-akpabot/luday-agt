class Portfolio:

 portfolio = {}
 
 '''
 

 '''
 #Luday
 portfolio_1 ="""

import React from 'react'


const Portfolio = () => {
  return (
    <section className="bg-white">
        <div className="container max-w-7xl px-6 py-10 mx-auto">
            <h2 className="text-lg font-semibold leading-8 tracking-tight text-blue-600">Portfolio</h2>
            <p className="mt-2 text-3xl font-bold tracking-tight text-black sm:text-4xl">Our works</p>
            <p className="mt-4 xl:mt-6 text-gray-900">
                A collection of our work that highlights our expertise. Explore the projects
            </p>
            
            <div id="portfolio" class="portfolio">
                <div class="container" data-aos="fade-up">
                    <div class="row mb-3" data-aos="fade-up" data-aos-delay="100">
                        <div class="col-lg-12 d-flex justify-content-center">
                            <ul id="portfolio-flters">
                                <li data-filter="*" class="filter-active">All</li>
                                <li data-filter=".filter-app">Applications</li>
                                <li data-filter=".filter-card">Product Designs</li>
                                <li data-filter=".filter-web">Websites</li> 
                            </ul>
                        </div>
                    </div>
                    <div class="row gy-4 portfolio-container d-flex align-items-center justify-content-center" data-aos="fade-up" data-aos-delay="200">
                        <div class="col-lg-3 col-md-6 mx-auto portfolio-item filter-web"></div>
                        <div class="col-lg-3 col-md-6 portfolio-item filter-web">
                            <div class="portfolio-wrap">
                                <img src="https://luday.se/img/afjfarms.png" class="img-fluid" alt="afj-farms-logo"/>
                                <div class="portfolio-info">
                                    <h4>AFJ Farms</h4>
                                    <p>AFJ Farms is a leading poultry farm determined to transform Agriculture in Nigeria by undertaking opportunities for growth and business.</p>
                                    <div class="portfolio-links">
                                     <a href="assets/img/portfolio/comdoity.png" data-gallery="portfolioGallery" class="portfokio-lightbox" title="App 1"><i class="bi bi-plus"></i></a> 
                                    <a href="https://afjfarms.com" target="_blank" title="More Details"><i class="bi bi-link"></i></a>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-3 col-md-6 portfolio-item filter-web">
                            <div class="portfolio-wrap">
                                <img src="https://luday.se/img/comdoity.png" class="img-fluid" alt="comdoity-logo"/>
                                <div class="portfolio-info">
                                    <h4>Comdoity</h4>
                                    <p>An online platform for people to exchange their skills and time for free and network as they do so.</p>
                                    <div class="portfolio-links">
                                     <a href="assets/img/portfolio/comdoity.png" data-gallery="portfolioGallery" class="portfokio-lightbox" title="App 1"><i class="bi bi-plus"></i></a> 
                                    <a href="https://comdoity.com" target="_blank" title="More Details"><i class="bi bi-link"></i></a>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-3 col-md-6 portfolio-item filter-web"></div>
                        <div class="col-lg-4 col-md-6 portfolio-item filter-card">
                            <div class="portfolio-wrap">
                            <img src="assets/img/portfolio/portfolio-4.jpg" class="img-fluid" alt=""/>
                            <div class="portfolio-info">
                                <h4>Card 2</h4>
                                <p>Card</p>
                                <div class="portfolio-links">
                                <a href="assets/img/portfolio/portfolio-4.jpg" data-gallery="portfolioGallery" class="portfokio-lightbox" title="Card 2"><i class="bi bi-plus"></i></a>
                                <a href="portfolio-details.html" title="More Details"><i class="bi bi-link"></i></a>
                                </div>
                            </div>
                            </div>
                        </div>
                        <div class="col-lg-4 col-md-6 portfolio-item filter-web">
                            <div class="portfolio-wrap">
                            <img src="assets/img/portfolio/portfolio-5.jpg" class="img-fluid" alt=""/>
                            <div class="portfolio-info">
                                <h4>Web 2</h4>
                                <p>Web</p>
                                <div class="portfolio-links">
                                <a href="assets/img/portfolio/portfolio-5.jpg" data-gallery="portfolioGallery" class="portfokio-lightbox" title="Web 2"><i class="bi bi-plus"></i></a>
                                <a href="portfolio-details.html" title="More Details"><i class="bi bi-link"></i></a>
                                </div>
                            </div>
                            </div>
                        </div>
                        <div class="col-lg-4 col-md-6 portfolio-item filter-app">
                            <div class="portfolio-wrap">
                            <img src="assets/img/portfolio/portfolio-6.jpg" class="img-fluid" alt=""/>
                            <div class="portfolio-info">
                                <h4>App 3</h4>
                                <p>App</p>
                                <div class="portfolio-links">
                                <a href="assets/img/portfolio/portfolio-6.jpg" data-gallery="portfolioGallery" class="portfokio-lightbox" title="App 3"><i class="bi bi-plus"></i></a>
                                <a href="portfolio-details.html" title="More Details"><i class="bi bi-link"></i></a>
                                </div>
                            </div>
                            </div>
                        </div>
                        <div class="col-lg-4 col-md-6 portfolio-item filter-card">
                            <div class="portfolio-wrap">
                            <img src="assets/img/portfolio/portfolio-7.jpg" class="img-fluid" alt=""/>
                            <div class="portfolio-info">
                                <h4>Card 1</h4>
                                <p>Card</p>
                                <div class="portfolio-links">
                                <a href="assets/img/portfolio/portfolio-7.jpg" data-gallery="portfolioGallery" class="portfokio-lightbox" title="Card 1"><i class="bi bi-plus"></i></a>
                                <a href="portfolio-details.html" title="More Details"><i class="bi bi-link"></i></a>
                                </div>
                            </div>
                            </div>
                        </div>
                        <div class="col-lg-4 col-md-6 portfolio-item filter-card">
                            <div class="portfolio-wrap">
                            <img src="assets/img/portfolio/portfolio-8.jpg" class="img-fluid" alt=""/>
                            <div class="portfolio-info">
                                <h4>Card 3</h4>
                                <p>Card</p>
                                <div class="portfolio-links">
                                <a href="assets/img/portfolio/portfolio-8.jpg" data-gallery="portfolioGallery" class="portfokio-lightbox" title="Card 3"><i class="bi bi-plus"></i></a>
                                <a href="portfolio-details.html" title="More Details"><i class="bi bi-link"></i></a>
                                </div>
                            </div>
                            </div>
                        </div>
                        <div class="col-lg-4 col-md-6 portfolio-item filter-web">
                            <div class="portfolio-wrap">
                                <img src="assets/img/portfolio/portfolio-9.jpg" class="img-fluid" alt=""/>
                                        <div class="portfolio-info">
                                            <h4>Web 3</h4>
                                            <p>Web</p>
                                            <div class="portfolio-links">
                                            <a href="assets/img/portfolio/portfolio-9.jpg" data-gallery="portfolioGallery" class="portfokio-lightbox" title="Web 3"><i class="bi bi-plus"></i></a>
                                            <a href="portfolio-details.html" title="More Details"><i class="bi bi-link"></i></a>
                                        </div>
                                    </div>
                                </div>
                            </div> 
                        </div>
                </div>
            </div>
        </div>
    </section>
  )
}
export default Portfolio
 """
 portfolio["portfolio_1"] = portfolio_1