class FakeExampleComponents:

 fakeExampleComponents = {}
 
 '''
 Navbar1 

 This component represent a nav bar
 
    Variables:
        @@menu1@@: String representing the name of 1st menu e.g "Home"
        @@menu2@@: String representing the name of 2nd menu
        @@menu3@@: String representing the name of 3rd menu
        @@menu4@@: String representing the name of 4th menu
        @@menu5@@: String representing the name of 5th menu
 '''
 navbar_1 ="""
import React from 'react';

function Navbar1(){
  return( 
      <div> 
         <div> @@menu1@@ | @@menu2@@  | @@menu3@@  | @@menu4@@  | @@menu5@@  </div>
      </div>
  )
}

export default Navbar1;
 """
 fakeExampleComponents["navbar_1"] = navbar_1
 
 '''
 Footer1 

 This component represent a footer
 
    Variables:
        @@CompanyName@@: String representing the company name e.g "Bestdealnaija"
        @@Email@@: String representing the email of the company
 '''
 footer_1 ="""
import React from 'react';

function Footer1(){
  return( 
      <div> 
         <div> @@CompanyName@@ </div>
         <div> @@Email@@ </div>
      </div>
  )
}

export default Footer1;
 """
 fakeExampleComponents["footer_1"] = footer_1
 