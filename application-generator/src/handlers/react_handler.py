from usecase.i_part_handler import IPartHandler
from usecase.i_data_handler import IDataHandler
from content.react.layouts.page_layouts import PageLayouts
from content.react.components.fake_example_components import FakeExampleComponents
from content.react.components.heros import Heros
from content.react.components.intros import Intros
from content.react.components.clients import Clients
from content.react.components.navbars import Navbars
from content.react.components.footers import Footers
from content.react.components.blogs import Blogs
from content.react.components.supportPages import SupportPage
from content.react.components.blogdetails import BlogDetails
from content.react.components.products import Products
from content.react.components.vendors import Vendors
from content.react.components.vendorsDetails import VendorDetails
from content.react.components.productDetails import ProductDetails
from content.react.components.about import Abouts
from content.react.components.contacts import Contacts
from content.react.components.carts import Carts
from content.react.components.deliverys import Deliverys
from content.react.components.checkout import Checkouts
from content.react.components.payments import Payments
from content.react.components.privacyPolicy import PrivacyPolicy
from content.react.components.termsAndConditions import TermsAndCondition
from content.react.components.constants import Constants
from content.react.components.hooks import Hooks
from content.react.components.redux import Redux
from content.react.components.routers import Routers
from content.react.components.services import Services
from content.react.components.find_deal import FindDeals
from content.react.components.slider import Sliders
from content.react.components.featured_products import FeaturedProducts
from content.react.components.banners import Banners
from content.react.components.pagination import Pagination
from content.react.components.timelines import Timelines
from content.react.components.forms import Forms
from content.react.components.formik import Formik
from content.react.components.orders import Orders
from content.react.components.accounts import Accounts
from content.react.components.admin import Admin
from content.react.components.preloader import Preloader
from content.react.components.sidebars import Sidebars
from content.react.components.topic import Topic
from content.react.components.owners_topic import Owners_Topic
from content.react.components.topic import Topic
from content.react.components.owners_topic import Owners_Topic
from content.react.components.search import Search
from content.react.components.errorBoundary import ErrorBoundaries
from content.react.components.reportWebVitals import ReportWebVitals
from content.react.components.default_component_page_index import DefaultIndex
from content.react.components.portfolio import Portfolio
from content.react.components.counter import Counter
from content.react.components.testimonials import Testimonials
from .partials.react_init import ReactInit
from os import path
import logging
import sys

 
logger = logging.getLogger(path.basename(__file__))
 
class ReactHandler(IPartHandler):    
    def __init__(self, data_handler : IDataHandler, react_setup_handler):
        self.data_handler = data_handler
        self.react_setup_handler = react_setup_handler
        self.version = ""
        self.packages = ""
        self.current_page_string = ""
        self.current_page_package_import_string = ""
        self.application_path = ""
        
    def replace_variables(self, replacement_variables, content):
        for variable in replacement_variables:
            content = content.replace(variable["pattern"], variable["content"])
            logger.debug(f"Replaced {variable['pattern']} with {variable['content']}")
        return content
        
    def get_import_string(self, import_array):       
        import_string = ""
        if import_array:
            for each_import in import_array:
                import_string += f"{each_import}\n"
                logger.debug(f"{each_import} added to page import string")     
        return import_string 

    def add_to_page_package_import_string(self, packages):
        for package in packages:
            package_src = package.get("import_src")
            package_name = package.get("import_name")
            if package_src:
                self.current_page_package_import_string += f"import {package_name} from '{package_src}';\n"
            else:
                self.current_page_package_import_string += f"import '{package_name}';\n"
            logger.debug(f"{package['import_name']} added to package import string")
        

    def get_method_or_variable(self, class_name : str, method_or_variable_name : str):
        object = getattr(sys.modules[__name__], class_name)
        return getattr(object, method_or_variable_name)
    

    def build_section(self, section):
        template_group = self.get_method_or_variable(section["template_class"], section["template_group"])
        component = template_group[section["template_name"]]
        component_imports = self.get_import_string(section.get("component_imports"))
        component = component.replace("@@Imports@@", component_imports)
        component = self.replace_variables(section["replacements"], component)

        packages = section.get("packages")
        for package in packages:
            package_imports = package.get("imports")
            logger.debug(f"Package: {package_imports}")

            if package_imports:
                self.add_to_page_package_import_string(package_imports)
                component = component.replace("@@importPackage@@", self.current_page_package_import_string)
        if not section.get("under_development"):
            self.data_handler.write(component, f"{self.application_path}/{section['install_path']}/{section['component_name']}.js")


    def build_react_page(self, page):
        logger.debug(f"Page name: {page['page_name']}")
        
        self.current_page_string = PageLayouts.layouts[page["layout"]]
        packages = page.get("packages")
        if packages:
            for package in packages:
                package_imports = package.get("imports")
                if package_imports:
                    self.add_to_page_package_import_string(package_imports)
                self.current_page_string = self.current_page_string.replace("@@importPackage@@", self.current_page_package_import_string)
        for section in page.get("sections"):
            self.build_section(section)
        
        import_string = self.get_import_string(page.get("page_imports"))
        self.current_page_string = self.current_page_string.replace("@@Imports@@", import_string)
        
        self.current_page_string = self.replace_variables(page["replacements"], self.current_page_string)
        self.data_handler.write(self.current_page_string, f"{self.application_path}/{page['install_path']}/{page['page_name']}.js")
       
    def handle_part(self, application_name : str, part_information):
        logger.debug("Handle React application")
        self.application_path = self.data_handler.get_application_root_folder(application_name)
        self.react_setup_handler.setup_react_app(self.application_path, part_information)
        for page in part_information.get("pages"):
            self.current_page_string = ""
            self.build_react_page(page)