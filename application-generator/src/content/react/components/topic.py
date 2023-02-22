class Topic:

 topics = {}


 """
 Topic Component
 """
 topic_1 ="""
import React from 'react';
import image1_1 from '../../images/imgs_userguide/image1_1.png';
import image1_2 from '../../images/imgs_userguide/image1_2.png';
import image1_5 from '../../images/imgs_userguide/image1_5.png';
import image1_5b from '../../images/imgs_userguide/image1_5b.png';

const @@PageName@@ = () => { 
  return (
    <>
      <div>
        <p className="userguide_header">@@Topic1Title@@</p>
        <p>@@Company@@ provides local businesses in Nigeria with the marketing tools they need to 
        increase their online visibility. We provide a variety of services such as online presence, local search, 
        display ads, direct marketing, and discounts. Our goal is to assist local businesses in promoting their 
        products and services as well as increasing website traffic. We strive to offer our users the best deals 
        and discounts, as well as the most enjoyable shopping experience in Nigeria.
        </p>
      </div>
      <div>
        <p className="userguide_subheader" id="1.1">@@Topic1SubTitle@@</p>

        <p className="userguide_subheader" id="1.2">@@Topic1Link1@@</p>
        <p>Visit @@Company@@ and click on the <b>Sign Up</b> button to create an account. You will need to provide 
        basic information such as your name, email address, and password. Once your account is created, you can 
        start using the site. </p>

        <img src={image1_1} style={{width:"80%"}} className="text-success py-3" />

        <p className="userguide_subheader" id="1.3">@@Topic1Link2@@</p>
        <p>Once you are logged in, you can search for deals and discounts on BestDealNaija. You can search by category, location, and more. You can also search for specific products and services. 
        </p>
        <img src={image1_2} style={{width:"80%"}} className="text-success py-3" />
      </div>
      <div>
        <p className="userguide_subheader" id="1.4">@@Topic1Link3@@</p>
        <p>Once you have found the deals you want, you can browse and select them. You can then purchase the deals 
        directly from the site or contact the business directly for more information.
        </p>
        <p className="userguide_subheader" id="1.5">@@Topic1Link4@@</p>
        <p>If you own a business, you can use BestDealNaija to promote it. You can create a profile for your business, 
        list your products and services, and offer discounts and deals to attract customers. You can also use the sites 
        marketing tools to reach new customers and build your brand.</p>
      </div>

      <div>
        <p className="userguide_subheader" id="1.6">@@Topic1Link5@@</p>
        <p>To find products on Bestdealnaija, browse through the categories. Products on bestdealnaija are 
        categorized, making it easy to find products of a particular type by looking through the category the 
        product belongs to. Additionally, you can search for products by entering the product name into the search 
        box on the products page.</p>
        <img src={image1_5} style={{width:"80%"}} className="text-success py-3" />
        <br /><br />
        <img src={image1_5b} style={{width:"80%"}} className="text-success py-3" />
      </div>
      <div>
        <p className="userguide_subheader" id="1.6">@@Topic1Link6@@</p>
        <p>You can search for deals and discounts by navigating through respective categories under the 
        recommended deals section on the home page. You can also find deals by clicking on the “Find your deal” 
        link on the sites navigation menu.</p>
      </div>
      <div>
        <p className="userguide_subheader" id="1.7">@@Topic1Link7@@</p>
        <p>To create your own listing you need to be a registered vendor on bestdealnaija. Once you have been 
        verified as a vendor on bestdealnaija you can start posting products from your vendor account dashboard. 
        To learn more about being a vendor see the section on becoming a vendor</p>
      </div>
      <div>
        <p className="userguide_subheader" id="1.8">@@Topic1Link8@@</p>
        <p>You can pay for products on bestdealnaija in a variety of ways including using a debit card, 
        USSD Code or a Bank Transfer. To pay for a product, add the product to your shopping cart, then click 
        on checkout. This will send you to a page where you can select your preferred payment option.</p>
      </div>

      <div>
        <p className="userguide_subheader" id="1.9">@@Topic1Link9@@</p>
        <p>You can contact customer service by email, or Phone call. 
        Our customer support line is [INSERT:contact], our support email is [INSERT:email].</p>
      </div>

      <div>
        <p className="userguide_subheader" id="1.10">@@Topic1Link10@@</p>
        <p>You can change your account settings from your dashboard. 
        To change your account settings login to your account with your email and password. Once logged in you 
        can change your password and Edit your profile information. </p>
      </div>
      <div>
        <p className="userguide_subheader" id="1.11">@@Topic1Link11@@</p>
        <p>The terms and conditions for using Bestdealnaija can be found by navigating to the terms and conditions page. 
        [Link: Terms and Conditions].</p>
      </div>
    </>
  )
}
export default Topic
 """
 topics["topic_1"] = topic_1
 
 """
 Topic 2 Component goes in here
 """
 topic_2 ="""
import React from 'react';
import image2_3 from '../../images/imgs_userguide/image2_3.jpeg';
const @@PageName@@ = () => { 
  return (
    <>
      <div>
        <p className="userguide_header">@@Topic2Title@@</p>
        <p className="userguide_subheader" id="2.1">@@Topic2Link1@@</p>
        <p>To create an account, click on the Sign Up button to create an account. You will need to provide basic 
        information such as your name, email address, and password. Once your account is created, you can start using 
        the site. 
        </p>
      </div>
      <div>
        <p className="userguide_subheader" id="2.2">@@Topic2Link2@@</p>
        <p>Once you create an account and verify your email you can start performing transactions on bestdealnaija. 
        Vendor accounts however take anywhere from 24 hours to 7 Days for an account to undergo review and be 
        approved.
        </p>
      </div>
      <div>
        <p className="userguide_subheader" id="2.3">@@Topic2Link3@@</p>
        <p>To create an account on Best Deal Naija you need basic personal information such as your name, email, and Gender. 
        Once you have created your account you will be routed to a profile page where you can edit your profile 
        information. To complete your profile you will need to provide additional information such as your phone 
        number, your state, and your address.</p>
        <img src={image2_3} style={{width:"40%"}} className="text-success py-3" />
      </div>
      <div>
        <p className="userguide_subheader" id="2.4">@@Topic2Link4@@</p>
        <p>To reset or change your password, navigate to the login page, click on the forgot password link, and enter your 
        email address registered with Bestdealnaija. A password reset link will be sent to your email. Click on the 
        password reset link and choose a new password. You can access your account with the new password that you 
        have created.</p>
      </div>
      <div>
        <p className="userguide_subheader" id="2.5">@@Topic2Link5@@</p>
        <p>No. There is no limit to the number of user accounts that can be created. However, each account must 
        have a different email address as no two accounts can have the same email.</p>
      </div>
      <div>
        <p className="userguide_subheader" id="2.6">@@Topic2Link6@@</p>
        <p>No. User accounts are not associated with any form of payment. Users can choose from multiple payment 
        options when trying to make a purchase but no payment needs to be made nor payment options set when creating
         an account. </p>
      </div>
      <div>
        <p className="userguide_subheader" id="2.7">@@Topic2Link7@@</p>
        <p>No. User accounts are not linked to any third-party services. </p>
      </div>
      <div>
        <p className="userguide_subheader" id="2.8">@@Topic2Link8@@</p>
        <p>Yes. User accounts are subject to the privacy policy of bestdealnaija. Refer to the bestdealnaija privacy policy document for more information.</p>
      </div>
      <div>
        <p className="userguide_subheader" id="2.9">@@Topic2Link9@@</p>
        <p>No, it is not possible to delete an account from bestdealnaija, however, you can deactivate it.</p>
      </div>
      <div>
        <p className="userguide_subheader" id="2.10">@@Topic2Link10@@</p>
        <p>All user accounts are subject to the Terms and Conditions of Bestdealnaija. Refer to the Terms and Conditions for more information.</p>
      </div>
    </>
  )
}
export default Topic2
 """
 topics["topic_2"] = topic_2

 """
 Topic 3 Component goes in here
 """
 topic_3 ="""
import React from 'react';
const Topic3 = () => {
  return (
    <>
      <div>
        <p className="userguide_header">@@Topic3Title@@</p>
        <p className="userguide_subheader" id="3.1">@@Topic3Link1@@</p>
        <p>a. To become a vendor, create a vendor account by visiting [VENDOR ACCOUNT CREATION LINK] and filling out the form with the relevant information.</p>
        <p>b. You will be routed to a Your vendor profile page where you will be required to complete your account by providing additional information about your business.</p>
        <p>c. Once your information is complete and submitted, your account will undergo a period during which it will be reviewed. After the review, if your account is approved, 
        you may begin selling on Best deal Naija, otherwise, you may need to apply for another review by updating your vendor profile details.</p>
      </div>
      <div>
        <p className="userguide_subheader" id="3.2">@@Topic3Link2@@</p>
        <p>You can list your products on the Best Deal Naija marketplace by signing up as a vendor. Once you have created and 
        verified your vendor status, you can begin to make product listings on bestdealnaija.
        </p>
      </div>
      <div>
        <p className="userguide_subheader" id="3.3">@@Topic3Link3@@</p>
        <p>Purchases can be made from bestdealnaija using Debit Cards, Bank transfers, or USSD codes. When a user makes a purchase, 
        the vendors payment is made to the vendor.</p>
      </div>
      <div>
        <p className="userguide_subheader" id="3.4">@@Topic3Link4@@</p>
        <p>There are no fees associated with being a vendor on bestdealnaija. Vendor accounts are free and do not come with any charges.</p>
      </div>
      <div>
        <p className="userguide_subheader" id="3.5">@@Topic3Link5@@</p>
        <p>Customer inquiries about your products are made to you directly via your business contact information provided when creating a vendor account. You can handle 
        these inquiries by contacting the customer to provide feedback either by call or by replying by email.</p>
      </div>
      <div>
        <p className="userguide_subheader" id="3.6">@@Topic3Link6@@</p>
        <p>Our online marketplace offers customer support services to ensure our clients satisfaction. To address any questions or concerns our customers may have, we offer 24/7 customer service, live chat support, email support, and phone support. 
        We also have a large knowledge base and FAQs to help customers find answers to their questions quickly.</p>
      </div>
      <div>
        <p className="userguide_subheader" id="3.7">@@Topic3Link7@@</p>
        <p>Our online marketplace makes managing shipping and fulfillment easy. Customers can easily set up their preferred shipping method, view tracking information, and print shipping labels. We also offer third-party support for customers who choose to use a different provider. 
        Our intuitive dashboard makes it simple to track orders and manage fulfillment. Customers can also access their order history, view estimated delivery times, and track their shipments in real-time.</p>
      </div>
      <div>
        <p className="userguide_subheader" id="3.8">@@Topic3Link8@@</p>
        <p>Payments from bestdealnaija are forwarded to the vendor account as soon as the customer confirms receipt of the goods they ordered. Payment 
        typically takes the amount of time required to deliver the product to the client.</p>
      </div>
      <div>
        <p className="userguide_subheader" id="3.9">@@Topic3Link9@@</p>
        <p>BestDealNaija offers comprehensive marketing services to help local businesses in Nigeria reach their target audience and maximize their online presence. Services include search engine optimization, local search, display advertising, social media promotion, digital promotion, and discount and deal listings. 
        With these services, businesses can attract more customers, build brand awareness and increase their sales.</p>
      </div>
      <div>
        <p className="userguide_subheader" id="3.10">@@Topic3Link10@@</p>
        <p>Yes, there are restrictions on the kind of products that can be listed on bestdealnaija. Illegal items 
        such as weapons and drugs are not permitted on the website. Any account caught posting offensive content 
        will be blocked permanently</p>
      </div>
      <div>
        <p className="userguide_subheader" id="3.11">@@Topic3Link11@@</p>
        <p>@@Company@@ offers several tools to help businesses track sales and customer feedback. Businesses can 
        set up tracking pixels on their website to measure conversions and track performance. They can also use 
        analytics tools to monitor website traffic and measure the effectiveness of their campaigns. Additionally, 
        BestDealNaija provides customer feedback forms so businesses can collect customer reviews and ratings to 
        measure customer satisfaction.</p>
      </div>
    </>
  )
}
export default Topic3
 """
 topics["topic_3"] = topic_3

 """
 Topic 4 Component goes in here
 """
 topic_4 ="""
import React from 'react';
const Topic4 = () => {
  return (
    <>
      <div>
        <p className="userguide_header">@@Topic4Title@@</p>
        <p className="userguide_subheader" id="4.1">@@Topic4Link1@@</p>
        <p>To log in to your account, click on the account option and select login. Provide your email and password
         then click login. You will be automatically logged into your bestdealnaija account.</p>
      </div>
      <div>
        <p className="userguide_subheader" id="4.2">@@Topic4Link2@@</p>
        <p>To view your transaction history simply login to your dashboard and click on “My Order History”. 
        You will be routed to a page where you will be able to view all orders and transactions.</p>
      </div>
      <div>
        <p className="userguide_subheader" id="4.3">@@Topic4Link3@@</p>
        <p>To view your vendor account log in using the email and password used to create your vendor account. User accounts cannot coexist with vendor
         accounts which means even if you have a user account on bestdealnaija your vendor account will have different login details.</p>
      </div>
      <div>
        <p className="userguide_subheader" id="4.4">@@Topic4Link4@@</p>
        <p>To edit your profile information log in to your account and go to the profile page. Click on the edit button and a form drops down which allows you to update your 
        profile information. You can update all your information including your name, email, phone number, and address.</p>
      </div>
      <div>
        <p className="userguide_subheader" id="4.5">@@Topic4Link5@@</p>
        <p>To change your password log in to your profile and click on the change password button.</p>
      </div>
      <div>
        <p className="userguide_subheader" id="4.6">@@Topic4Link6@@</p>
        <p>For users payment information is only required when making a purchase. For vendors, payment information 
        is required to set up a receiving account when funds will be transferred after payment for a product has 
        been made.</p>
      </div>
    </>
  )
}
export default Topic4
 
 """
 topics["topic_4"] = topic_4


 """
 Topic 5 Component goes in here
 """
 topic_5 ="""
import React from 'react';
const Topic5 = () => {
  return (
    <>
      <div>
        <p className="userguide_header">@@Topic5Title@@</p>
        <p className="userguide_subheader" id="5.1">@@Topic5Link1@@</p>
        <p>You can process customer orders from your vendor dashboard. Each order contains the information of the 
        customer who placed the order and information on the order thats been placed including product, cost 
        and fulfillment preferences.</p>
      </div>
      <div>
        <p className="userguide_subheader" id="5.2">@@Topic5Link2@@</p>
        <p>You set the pricing information of a product when you create or add the product from your vendor 
        dashboard. To add a product you</p>
      </div>
      <div>
        <p className="userguide_subheader" id="5.3">@@Topic5Link3@@</p>
        <p>Bestdealnaija does not allow for inventory management and hence does not include support for such 
        features.</p>
      </div>
      <div>
        <p className="userguide_subheader" id="5.4">@@Topic5Link4@@</p>
        <p>To issue refunds for a product, the product has to be returned. Refunds depend largely on the refund 
        policy of the vendor and quality assurance is handled on the vendor's end.</p>
      </div>
      <div>
        <p className="userguide_subheader" id="5.5">@@Topic5Link5@@</p>
        <p>Customer payments can be tracked from your vendor dashboard. Once a sale is completed the registered 
        bank account is credited with the transaction history is logged and is visible on the vendor account dashboard.</p>
      </div>
      <div>
        <p className="userguide_subheader" id="5.6">@@Topic5Link6@@</p>
        <p>Bestdealnaija does not support email notifications for orders. Order tracking is maintained from the vendor dashboard.</p>
      </div>
      <div>
        <p className="userguide_subheader" id="5.7">@@Topic5Link7@@</p>
        <p>Bestdealnaija is securely built using the industry best practices security protocols to ensure the safety of its users.  It runs on a secure database which keeps all user information safe guarded against intrusions as well as SSL security to ensure 
        safety against transactional fraud. Additionally, bestdealnaija keeps all its user information provate</p>
      </div>
    </>
  )
}
export default Topic5
 
 """
 topics["topic_5"] = topic_5


 """
 Topic Example Component goes in here
 """
 topic_example ="""
 
 
 """
 topics["topic_example"] = topic_example
 '''
 

 '''
 
