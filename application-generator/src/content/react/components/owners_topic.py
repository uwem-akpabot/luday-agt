class Owners_Topic:

 owners_topics = {}


 """
 Owners_Topic Component
 """

 owners_topic_1 ="""
import React from 'react';

const @@PageName@@ = () => { 
  return (
    <>
      <div><p className="userguide_header">@@Owners_Topic1Title@@</p></div>
      <div>
        <p className="userguide_subheader" id="1.1">@@Owners_Topic1Title00@@</p>
        <p>@@Company@@ admin dashboard is a powerful tool designed to help administrators manage activity on 
        the website. The dashboard provides an overview of all that goes on on the website including viewing and 
        managing user activity. It also includes tools for managing other admins who may have access to the 
        dashboard. With the dashboard, administrators can access the necessary information to gain insights into user activity. Get a comprehensive view of the website and allows easy management of website activity.</p>
        
        <p id="" className="userguide_subheader">@@Owners_Topic1Title01@@</p>
        <p>To get started using the admin dashboard navigate to the log in page and log in by clicking the user icon at 
        the top right corner of the screen and login with your administrator credentials. Once logged in you can access 
        administrator privileges on all modules including, Admin users, Vendors, Categories, Blogs, Orders, and Products. </p>

        <p className="userguide_subheader" id="1.2">@@Owners_Topic1Title@@</p>

        <p className="userguide_subheader" id="1.2">@@Owners_Topic1Link1@@</p>
<p>To add a new admin click on the Users tab and click on create admin from the dropdown menu that appears. This 
will route you to a page where you can create a new admin account by filling out the relevant admin user details 
including names, email, and Passwords. A message containing the login details for the admin user created is sent by 
mail to the email address used to create the account, which the admin can use to access the account created and 
gain access to the admin dashboard.
</p>
        <p className="userguide_subheader" id="1.3">@@Owners_Topic1Link2@@</p>
<p>To remove admin accounts created, click on users and navigate to manage admins. This routes you to a page where 
all admins are visible in a tabulated list. From the action column on the table, you can choose to delete or edit 
an admin account. To remove an admin account simply click on “delete” next to the administrators profile.
</p>
      </div>
      <div>
        <p className="userguide_subheader" id="1.4">@@Owners_Topic1Link3@@</p>
<p>You cannot manage admin user permissions. Once an admin account is created the admin has access to the same privileges as all other administrator accounts.
</p>
        <p className="userguide_subheader" id="1.5">@@Owners_Topic1Link4@@</p>
<p>There is only one admin role which consists of a general set of  privileges available to all administrators.
</p>
      </div>
      <div>
        <p className="userguide_subheader" id="1.6">@@Owners_Topic1Link5@@</p>
<p>To reset the admin password, click on the forgot password link on the admin login page and enter your administrator email address. An email will be forwarded to you including a password reset link and instructions on how to reset your password.
</p>
      </div>
      <div>
        <p className="userguide_subheader" id="1.6">@@Owners_Topic1Link6@@</p>
<p>You can manage your admin profile from the admin list. Click on users on the dashboard menu, then click on manage 
admins. From the table of listed admins select the admin profile you want to manage and click Edit. Here you can 
update the information on the corresponding admin profile.
</p>
      </div>
    </>
  )
}
export default @@PageName@@
 """
 owners_topics["owners_topic_1"] = owners_topic_1
 
 """
 Owners_Topic 2 Component goes in here
 """
 owners_topic_2 ="""
import React from 'react';
const @@PageName@@ = () => { 
  return (
    <>
      <div><p className="userguide_header">@@Owners_Topic2Title@@</p>
      </div>
      <div>
        <p className="userguide_subheader" id="2.2">@@Owners_Topic2Link1@@</p>
<p>To view all current vendors in the BestDealNaija admin dashboard, click on “Vendors” in the left sidebar. Here, you will have a list of all current vendors, where you can view their profiles and account details.
</p>
      </div>
      <div>
        <p className="userguide_subheader" id="2.3">@@Owners_Topic2Link2@@</p>
<p>You cannot add a vendor from the admin dashboard. A vendor account has to be created from the vendor registration portal. To remove vendors from the dashboard, click on “Vendors” in the left sidebar then click on All Vendors. This routes you to a page with a tabulated list of all vendors, simply click on the “Delete” button next to the vendors name to remove the selected vendor.
</p>
      </div>
      <div>
        <p className="userguide_subheader" id="2.4">@@Owners_Topic2Link3@@</p>
<p>To edit vendor profiles in the dashboard, click on “Vendors” and navigate to All Vendors. This routes you to a tabulated list of all vendors. Click on the “Edit” button next to the vendors name. Here you can edit the vendors details and then click “Save”.
</p>     
      </div>
      <div>
        <p className="userguide_subheader" id="2.5">@@Owners_Topic2Link4@@</p> 
<p>To edit vendor profiles in the dashboard, click on “Vendors” and navigate to All Vendors. This routes you to a tabulated list of all vendors. Click on the “Verify” button next to the vendors name to verify the vendors profile.
</p>       
      </div>
      <div>
        <p className="userguide_subheader" id="2.6">@@Owners_Topic2Link5@@</p> 
<p>You can monitor vendor orders and transactions by navigating to the “Orders” section in the left sidebar. Here you can view all orders placed and the associated transactions.
</p>    
      </div>
      <div>
        <p className="userguide_subheader" id="2.7">@@Owners_Topic2Link6@@</p>
<p>You can track the inventory of each vendor by navigating to the “Products” section of the dashboard. Here you can view the current stock levels for each vendor and manage stock levels for each product.
</p>
      </div>
      <div>
        <p className="userguide_subheader" id="2.8">@@Owners_Topic2Link7@@</p>
<p>There are currently no reporting tools available for vendors on bestdealnaija.</p>
      </div>
    </>
  )
}
export default @@PageName@@
 """
 owners_topics["owners_topic_2"] = owners_topic_2

 """
 Owners_Topic 3 Component goes in here
 """
 owners_topic_3 ="""
import React from 'react';
const @@PageName@@ = () => {
  return (
    <>
      <div><p className="userguide_header">@@Owners_Topic3Title@@</p></div>
      <div>
      <p className="userguide_subheader" id="3.1">@@Owners_Topic3Link1@@</p>
<p>To view orders, click on orders on the navigation menu. You will be routed to an order page where you can view all orders as a tabulated list. Here you can view order details.</p>

      </div>
      <div>
        <p className="userguide_subheader" id="3.1">@@Owners_Topic3Link2@@</p>
<p>It is not possible to modify order information</p>
      </div>

      <div>
        <p className="userguide_subheader" id="3.2">@@Owners_Topic3Link3@@</p>
<p>It is not possible to cancel orders from the admin dashboard. </p>
      </div>
      <div>
        <p className="userguide_subheader" id="3.3">@@Owners_Topic3Link4@@</p> 
<p>Privileges cannot be assigned to any order that has been placed.</p>
      </div>
      <div>
        <p className="userguide_subheader" id="3.4">@@Owners_Topic3Link5@@</p>     
<p>Information about all orders including payments and ... </p>  
      </div>
      <div>
        <p className="userguide_subheader" id="3.5">@@Owners_Topic3Link6@@</p>    
<p>Bestdealnaija does not provide support for order tracking. Order tracking has to be from the end of the vendor.  </p>
      </div>
    </>
  )
}
export default @@PageName@@
 """
 owners_topics["owners_topic_3"] = owners_topic_3

 """
 Owners_Topic 4 Component goes in here
 """
 owners_topic_4 ="""
import React from 'react';
const @@PageName@@ = () => {
  return (
    <>
      <div><p className="userguide_header">@@Owners_Topic4Title@@</p></div>
      <div>
        <p className="userguide_subheader" id="4.1">@@Owners_Topic4Link1@@</p>
<p>Categories enable products and vendors to be organized according to product type under a spectrum. Each vendor and product has a category it belongs to which makes it easy to find a specific set of products within a specific scope.</p>
      </div>
      <div>
        <p className="userguide_subheader" id="4.2">@@Owners_Topic4Link2@@</p>
<p>To create a new category click on the categories link on the navigation menu. You will be routed to a categories page where you can add a new category. To add a new category fill in the category name, a brief description of the category and upload a category image then click “add category”.</p>
      </div>
      <div>
        <p className="userguide_subheader" id="4.3">@@Owners_Topic4Link3@@</p>
<p>To edit any category click on the categories link from the menu and navigate to the categories page. On the categories page, a tabulated list of all created categories is visible. Under the action column, you can find an option to edit the category on that row. Click edit and fill out the new category information click save </p>  
      </div>
      <div>
        <p className="userguide_subheader" id="4.4">@@Owners_Topic4Link4@@</p> 
<p>To delete any category click on the categories link from the menu and navigate to the categories page. On the categories page, a tabulated list of all created categories is visible. Under the action column, you can find an option to delete the category on that row. Click delete to remove the category</p>     
      </div>
    </>
  )
}
export default @@PageName@@
 """
 owners_topics["owners_topic_4"] = owners_topic_4


 """
 Owners_Topic 5 Component goes in here
 """
 owners_topic_5 ="""
import React from 'react';
const @@PageName@@ = () => {
  return (
    <>
      <div><p className="userguide_header">@@Owners_Topic5Title@@</p></div>

      <div><p className="userguide_subheader" id="5.1">@@Owners_Topic5Link1@@</p></div>
      <div>
        <p>To view, all products click on the products option on the navigation menu. From the dropdown that appears, 
        select all products. You will be routed to a page where all products are outlined in tabulated form.</p>
      </div>

      <div><p className="userguide_subheader" id="5.2">@@Owners_Topic5Link2@@</p></div>
      <div>
        <p>An admin cannot add products to bestdealnaija, the admin can only verify products that vendors have added. 
        Only vendors can add products.</p>
      </div>

      <div><p className="userguide_subheader" id="5.3">@@Owners_Topic5Link3@@</p></div>
      <div>
        <p>An admin cannot edit product information on bestdealnaija, administrators can only verify products that 
        vendors have added or switch the status of the product to unverified. Only vendors can edit product details.</p>
      </div>
      
      <div><p className="userguide_subheader" id="5.4">@@Owners_Topic5Link4@@</p></div>
      <div>
        <p>Administrators cannot delete products from bestdealnaija. Only vendors can delete products that they have 
        uploaded. This is done from the vendors account dashboard.</p>
      </div>

      <div><p className="userguide_subheader" id="5.5">@@Owners_Topic5Link5@@</p></div>
      <div>
        <p>Vendors can only create product listings once their vendor account has been verified. Similarly, Products 
        that are visible on bestdealnaija have to be verified by the administrators before they can be purchased.</p>
      </div>

      <div><p className="userguide_subheader" id="5.6">@@Owners_Topic5Link6@@</p></div>
      <div>
        <p>To verify a product, navigate to the products page. From the table of products under the actions column 
        click on the verify button next to the product you want to verify. To unverify a product click on the unverify 
        button next to the product.</p>
      </div>
    </>
  )
}
export default @@PageName@@
 """
 owners_topics["owners_topic_5"] = owners_topic_5


 """
 Owners_Topic 6 Component goes in here
 """
 owners_topic_6 ="""
import React from 'react';
const @@PageName@@ = () => {
  return (
    <>
      <div><p className="userguide_header">@@Owners_Topic6Title@@</p></div>

      <div><p className="userguide_subheader" id="6.1">@@Owners_Topic6Link1@@</p></div>
      <div>
        <p>To view all blog posts click on the Blog option on the navigation menu then click on all blogs. You will be routed to a page with a tabulated outline of all blog posts.
Creating a new blog post</p>
      </div>

      <div><p className="userguide_subheader" id="6.2">@@Owners_Topic6Link2@@</p></div>
      <div>
        <p>To create a new blog posts click on the Blog option on the navigation menu then click on “post blog”. You will be routed to a page with a form. Fill out the details of the post you want to create including the title, a blog summary, content of the post and a 
        corresponding image. After filling out the form click on the “Post Blog” button.</p>
      </div>

      <div><p className="userguide_subheader" id="6.3">@@Owners_Topic6Link3@@</p></div>
      <div>
        <p>To edit a blog post navigate to the list of all blogs. On the tabulated view of the outline of blog 
        posts under the action column click on “Edit” next to the post you want to edit. This routes you to a form 
        where you can fill out the details you wish to change. After making your changes to the blog post form 
        click on “Update Blog”.</p>
      </div>

      <div><p className="userguide_subheader" id="6.4">@@Owners_Topic6Link4@@</p></div>
      <div>
        <p>To delete a blog post navigate to the list of all blogs. On the tabulated view of the outline of blog posts 
        under the action column click on “Delete” option  next to the post you want to delete. A popup box appears 
        confirming that you want to delete a post. Click on okay. The post will then be removed from the list of blog posts.</p>
      </div>
    </>
  )
}
export default @@PageName@@
 """
 owners_topics["owners_topic_6"] = owners_topic_6


 """
 Owners Topic Example Component goes in here
 """
 owners_topic_example ="""
 
 
 """
 owners_topics["owners_topic_example"] = owners_topic_example
 '''
 

 '''
 
