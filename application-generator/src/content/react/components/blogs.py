class Blogs:

 blogs = {}
 
 '''
 

 '''
 blog_1 ="""
import React from 'react';
import { Link } from 'react-router-dom';
import Pressup_image from './images/blog/pressup.jpeg';

const Blog1 = () => {
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

export default Blog1;
 """
 blogs["blog_1"] = blog_1

# src/pages/admin/blogs/ addblog 
 admin_addblog ="""
import React, {useCallback, useEffect, useState} from 'react';
@@Imports@@

const AddBlog = () => {
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
        //console.log(data);
        //console.log(blogContent)

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
                    <span className="text-base">Blogs</span>
                </span>
                <span>/</span>
            </div>
        </div>
        <div className="header my-3 h-12 px-10 flex items-center justify-between">
            <h1 className="font-medium text-2xl">Add a Blog</h1>
        </div>
        <div className="flex flex-col mx-3 mt-6 lg:flex-row">
            <div className="w-full m-1">
                {/* Display add blog form */}
                <form className="w-full bg-white shadow-md p-6" encType="multipart/form-data">
                    <div className="flex flex-wrap -mx-3 mb-6">
                        <div className="w-full md:w-full px-3 mb-6">
                            <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='title'>Blog Title</label>
                            <input className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d]" 
                                type='text' 
                                name="title" 
                                placeholder="Enter the Blog Title"  
                                {...register("title", { required: true})}
                            required />
                            {errors.title && <small className="text-red-500 text-xs italic mx-auto flex justify-center mt-2">Title is required</small>}
                        </div>
                        <div className="w-full md:w-full px-3 mb-6">
                            <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='title'>Blog Summary</label>
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
                                editor={Editor}
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

                            <h2 className="mt-4 text-xl font-medium text-gray-700 tracking-wide">Blog image</h2>

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

export default AddBlog;
 """
 blogs["admin_addblog"] = admin_addblog

 # src/pages/admin/blogs/ blogs
 admin_blogs ="""
import React, {useCallback, useEffect, useState} from 'react';
@@Imports@@

const Blogs = () => {
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
                <span className="text-green-700 tracking-wider font-thin text-md"><Link to={ROUTE.ADMIN_DASHBOARD}>Home</Link></span>
                <span>/</span>
                <span className="tracking-wide text-md">
                    <span className="text-base">Blogs</span>
                </span>
                <span>/</span>
              </div>
        </div>
        <div className="header my-3 h-12 px-10 py-8  flex items-center justify-between">
            <h1 className="font-medium text-2xl">All Blogs</h1>
            <Link to={ROUTE.ADMIN_ADD_BLOGS} className="focus:outline-none text-white m-4 p-3 font-semibold rounded-md bg-green-700 hover:bg-green-600 hover:shadow-lg transition-all duration-100"> <span><FaPlus className="inline-block w-4 h-3"/>
            </span> Post a new blog</Link>
        </div>
        <div className="flex flex-col mx-3 lg:flex-row">
            <div className="w-full m-4 bg-white shadow-lg text-lg rounded-sm border border-gray-200">
                <div className="overflow-x-auto rounded-lg  p-3">
                    {/* Display blogs table */}
                    <table className="table-auto w-full">
                        <thead className="text-sm font-semibold uppercase text-gray-800 bg-gray-50">
                            <tr className="font-semibold">
                                <th><svg xmlns="http://www.w3.org/2000/svg" className="fill-current w-5 h-5 mx-auto" ><path d="M6 22h12a2 2 0 0 0 2-2V8l-6-6H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2zm7-18 5 5h-5V4zm-4.5 7a1.5 1.5 0 1 1-.001 3.001A1.5 1.5 0 0 1 8.5 11zm.5 5 1.597 1.363L13 13l4 6H7l2-3z"></path></svg></th>
                                <th className="p-2">Blog Title
                                </th>
                                <th className="p-2">Action
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
export default Blogs;
 """
 blogs["admin_blogs"] = admin_blogs

 # src/pages/admin/blogs/ editblog
 admin_editblog ="""
import React, {useCallback, useEffect, useState} from 'react';
@@Imports@@

const EditBlog = () => {
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
                <span className="text-green-700 tracking-wider font-thin text-md"><Link to={ROUTE.ADMIN_DASHBOARD}>Home</Link></span>
                <span>/</span>
                <span className="tracking-wide text-md">
                    <span className="text-green-700 tracking-wider font-thin text-md"><Link to={ROUTE.ADMIN_BLOGS}>Blogs</Link></span>
                </span>
                <span>/</span>
                <span className="tracking-wide text-md">
                    <span className="text-base">Edit Blogs</span>
                </span>
                </div>
        </div>
        <div className="header my-3 h-12 px-4 lg:px-10 py-8  flex items-center justify-between">
            <h1 className="font-medium text-2xl">Edit Blogs</h1>
            <Link to={ROUTE.ADMIN_BLOGS} className="focus:outline-none text-white m-4 p-3 font-semibold rounded-md bg-green-700 hover:bg-green-600 hover:shadow-lg transition-all duration-100"> <span><FaAngleLeft className="inline-block w-5 h-5"/>
            </span> Back to Blogs</Link>
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
                        <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='title'>Blog Title</label>
                        <input className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d] focus:ring-[#98c01d]" type='text' name="title"
                        {...register("title", { required: true })} required onChange={(e) => setBlogTitle(e.target.value)} />
                        {errors.title && <small className="text-red-500 text-xs italic">Blog title is required</small>}
                    </div>

                    <div className="w-full md:w-full px-3 mb-6">
                            <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='title'>Blog Summary</label>
                            <textarea className="appearance-none block w-full bg-white text-gray-900 font-medium border border-gray-400 rounded-lg py-3 px-3 leading-tight focus:outline-none focus:border-[#98c01d]" 
                            type='text' 
                            name="summary" 
                            placeholder="Blog summary 250 words" rows={3} 
                            {...register("summary", { required: true})}
                            required maxLength={250} onChange={(e) => setBlogSummary(e.target.value)}/>
                            {errors.summary && <small className="text-red-500 text-xs italic mx-auto flex justify-center mt-2">Summary is required</small>}
                        </div>

                    <div className="w-full px-3 mb-6">
                        <label className="block uppercase tracking-wide text-gray-700 text-sm font-bold mb-2" htmlFor='content'>Content</label>
                            <CKEditor 
                                editor={Editor}
                                onChange={handleChange} data={blogContent} className="w-full"
                            />
                    </div>
                    <div className="w-full px-3 mb-12">
                        <label className="cursor-pointer flex w-fit max-w-lg flex-col items-center justify-center rounded-xl border-2 border-dashed border-green-400 bg-white p-6 mx-auto" htmlFor='product_image'>
                        <svg xmlns="http://www.w3.org/2000/svg" className="h-10 w-10 text-green-800" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="2">
                        <path strokeLinecap="round" strokeLinejoin="round" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
                        </svg>

                        <h2 className="mt-4 text-xl font-medium text-gray-700 tracking-wide">Blog image</h2>

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
export default EditBlog;
 """
 blogs["admin_editblog"] = admin_editblog
