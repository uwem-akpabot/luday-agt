class Datatables:

 datatables = {}
 
 '''
 
 '''
 datatable_1 ="""
import React from 'react';
import { Link } from 'react-router-dom';
import Pressup_image from './images/blog/pressup.jpeg';

const Datatables = () => {
  return (
    <>
        <section class="bg-gray-100 mt-20 md:mt-40">
            <div className="px-3 md:px-10 lg:px-36 py-[100px] pb-[80px] luday_wrap ">                    
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-9 luday_grid_wrap">
                    <div className="group bg-white">
                        <article>
                            <div>
                                <Link to="/blog-details"><img class="lazy w-full" src={Pressup_image} alt="" /></Link>
                            </div>
                            <div class="p-[30px]">
                               <Link to="/blog-details"> <h4>@@ArticleTitle@@ <i class="fa fa-chevron-right"></i></h4></Link>
                                <div>
                                    @@ArticleDate@@
                                </div>
                                @@ArticleIntro@@
                            </div>
                        </article>
                    </div>
                    <div className="group bg-white">
                        <article>
                            <div>
                                <Link to="/blog-details"><img class="lazy w-full" src={Pressup_image} alt="" /></Link>
                            </div>
                            <div class="p-[30px]">
                                <Link to="/blog-details"><h4>@@ArticleTitle1@@ <i class="fa fa-chevron-right"></i></h4></Link>
                                <div>
                                    @@ArticleDate@@
                                </div>
                                People are thinking about belonging to a gym but do not know which one to go. You are in luck as we have gathered a list of top six gyms that can help you keep fit.
                            </div>
                        </article>
                    </div>
                    <div className="group bg-white">
                        <article>
                            <div>
                                <Link to="/blog-details"><img class="lazy w-full" src={Pressup_image} alt="" /></Link>
                            </div>
                            <div class="p-[30px]">
                                <Link to="/blog-details"><h4>@@ArticleTitle2@@ <i class="fa fa-chevron-right"></i></h4></Link>
                                <div>
                                    @@ArticleDate@@
                                </div>
                                @@ArticleIntro@@
                            </div>
                        </article>
                    </div>
                </div>
            </div>
        </section>
    </>
  );
}

export default Datatables;
 """
 datatables["datatable_1"] = datatable_1

# static/Tbl.js 
 datatables_tbl ="""
import PropType from 'prop-types';
import 'datatables.net';
import 'datatables.net-dt';
@@Imports@@
import React, { Component } from 'react';

const $ = require('jquery')
$.DataTable = require('datatables.net')

class Tbl extends Component{
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
    // eslint-disable-next-line react/forbid-prop-types
    data: PropType.object.isRequired
};

export default Tbl;
 """
 datatables["datatables_tbl"] = datatables_tbl
