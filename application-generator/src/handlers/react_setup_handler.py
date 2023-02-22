from usecase.i_data_handler import IDataHandler
from .i_react_setup_handler import IReactSetupHandler
import os
import logging
import shutil
from .partials.react_init import ReactInit

logger = logging.getLogger(os.path.basename(__file__))
 
class ReactSetupHandler(IReactSetupHandler):
    
    def __init__(self, data_handler : IDataHandler):
        self.data_handler = data_handler
        self.react_version = ""
        self.react_pages = ""
        self.react_installed = ReactInit.react_init_['app_gen_folder']


    def empty_react_src_folder(self, react_src_folder):
        shutil.rmtree(react_src_folder)
        os.makedirs(react_src_folder)


    def install_react_package(self, destination, package):
        logger.debug(f"Installing React package: {package}")
        os.system(f"cd {destination} \
            && npm install --legacy-peer-deps {package}"
        )


    def setup_react_package(self, destination):
        for page in self.react_pages:
            packages = page.get("packages")
            sections = page.get("sections")

            if packages:
                for package in packages:
                    self.install_react_package(destination, package['package_name'])
            if sections:
                for section in sections:
                    section_packages = section.get("packages")
                    for package in section_packages:
                        self.install_react_package(destination, package['package_name'])


    def setup_react_app(self, destination, part_information):
        is_path_exist = self.data_handler.is_path_exist(f"{destination}/{self.react_installed}")
        if is_path_exist:
            logger.debug(f"React already setup in {destination}")
        else:
            os.system(f"npx create-react-app {destination}")
            self.react_version = part_information.get("version")
            os.system(f"cd {destination} \
                && npm install --legacy-peer-deps react@{self.react_version} \
                && npm install --legacy-peer-deps react-dom@{self.react_version}"
            )
            self.data_handler.write("React installed", f"{destination}/{self.react_installed}")
            self.empty_react_src_folder(f"{destination}/src")

            self.react_pages = part_information.get("pages")
            if self.react_pages:
                self.setup_react_package(destination)            
            logger.debug(f"New react application setup in {destination}")    