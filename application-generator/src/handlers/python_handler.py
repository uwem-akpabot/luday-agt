from usecase.i_part_handler import IPartHandler
from usecase.i_data_handler import IDataHandler

from content.python.modules.contact_us.config import ContactUsConfig
from content.python.modules.contact_us.env import ContactUsEnv
from content.python.modules.contact_us.i_config import ContactUsIConfig

from content.python.modules.user.config import UserConfig
from content.python.modules.user.env import UserEnv
from content.python.modules.user.i_config import UserIConfig

from content.python.modules.products.config import ProductsConfig
from content.python.modules.products.env import ProductsEnv
from content.python.modules.products.i_config import ProductsIConfig

from content.python.modules.blogs.config import BlogsConfig
from content.python.modules.blogs.env import BlogsEnv
from content.python.modules.blogs.i_config import BlogsIConfig

from content.python.modules.home.config import HomeConfig
from content.python.modules.home.env import HomeEnv
from content.python.modules.home.i_config import HomeIConfig

from .partials.python_init import PythonInit
from os import path
import logging, os, sys
logger = logging.getLogger(path.basename(__file__))

class PythonHandler(IPartHandler):

    def __init__(self, data_handler : IDataHandler, python_setup_handler):
        self.data_handler = data_handler
        self.python_setup_handler = python_setup_handler
        self.current_module_string = ""
        self.current_module_name = ""
        self.python_modules_folder_path = ""
        self.python_folder = PythonInit.python_init_['python_folder']
        self.python_folder_path = ""
        self.python_venv_folder = PythonInit.python_init_['python_venv_folder']
        self.python_env_file = PythonInit.python_init_['python_env_file']
        self.python_config_file = PythonInit.python_init_['python_config_file']
        self.python_i_config_file = PythonInit.python_init_['python_i_config_file']
        self.application_path = ""
        self.module_path = ""

    def replace_variables(self, replacement_variables, content):
        for variable in replacement_variables:
            content = content.replace(variable["pattern"], variable["content"])
            logger.debug(f"Replaced {variable['pattern']} with {variable['content']}")
        return content


    def get_method_or_variable(self, class_name : str, method_or_variable_name : str):
        object = getattr(sys.modules[__name__], class_name)
        return getattr(object, method_or_variable_name)


    def remove_config(self, page):
        if page['page_name'] == self.python_env_file:
            dot_env_file = f"{self.module_path}/{self.python_env_file}.py"
            self.data_handler.remove(dot_env_file)

        elif page['page_name'] == self.python_config_file:
            config_file = f"{self.module_path}/{self.python_config_file}.py"
            self.data_handler.remove(config_file)

        elif page['page_name'] == self.python_i_config_file:
            config_file = f"{self.module_path}/{self.python_i_config_file}.py"
            self.data_handler.remove(config_file)


    def install_python_package(self):
        self.data_handler.install_python_package(self.module_path, self.python_venv_folder)


    def run_flask_migration_init(self):
        logger.debug(f"Initializing migrations: {self.module_path}")
        os.system(f"cd {self.module_path} \
            && {self.module_path}/{self.python_venv_folder}/Scripts/activate.bat \
            && flask db init"
        )
        logger.debug(f"Migration initialization successful: {self.module_path}")


    def run_flask_migration(self):
        logger.debug(f"Running migrations: {self.module_path}")
        os.system(f"cd {self.module_path} \
            && {self.module_path}/{self.python_venv_folder}/Scripts/activate.bat \
            && flask db migrate \
            && flask db upgrade"
        )
        logger.debug(f"Migration successful: {self.module_path}")


    def create_virtual_environment(self):
        os.system(f"cd {self.module_path} && python -m {self.python_venv_folder} {self.python_venv_folder}")
        self.install_python_package()


    def python_build(self, page):
        file_group = self.get_method_or_variable(page["file_class"], page["file_group"])
        file = file_group[page["file_name"]]
        _file = self.replace_variables(page["replacements"], file)
        if page['page_name'] == self.python_env_file:
            self.data_handler.write(_file, f"{self.module_path}/.env")
        else:
            self.data_handler.write(_file, f"{self.module_path}/{page['page_name']}.py")


    def python_build_pages(self, module):
        for page in module.get("pages"):
            self.remove_config(page)
            self.python_build(page)
        venv_exist = os.path.exists(f"{self.module_path}/{self.python_venv_folder}")
        dunda_init_exist = os.path.exists(f"{self.module_path}/__init__.py")

        if dunda_init_exist:
            dunda_init_file = f"{self.module_path}/__init__.py"
            self.data_handler.remove(dunda_init_file)

        if not venv_exist:
            logger.debug(f"Creating venv: {self.module_path}/{self.python_venv_folder}")
            self.create_virtual_environment()
            if self.current_module_name != "home":
                self.run_flask_migration_init()
                self.run_flask_migration()

        else:
            logger.debug(f"venv folder exists already: {self.module_path}/{self.python_venv_folder}")
            if self.current_module_name != "home":
                self.run_flask_migration()


    def build_python_module(self, module):
        logger.debug(f"Building Module: {self.current_module_name}")
        self.module_path = f"{self.python_folder_path}/{self.current_module_name}"
        self.current_module_string = f"{self.python_modules_folder_path}/{module['module_name']}"

        self.data_handler.copy_directory(self.current_module_string, self.module_path)
        logger.debug(f"Copied path: {self.current_module_string}")
        self.python_build_pages(module)


    def setup_paths(self, application_name : str):
        self.application_path = self.data_handler.get_application_root_folder(application_name)
        self.python_folder_path = f"{self.application_path}/{self.python_folder }"
        self.python_modules_folder_path = self.data_handler.get_python_modules_file_path()


    def handle_part(self, application_name : str, part_information):
        logger.debug("Handle Python application")
        self.setup_paths(application_name)
        self.python_setup_handler.setup_python_module(self.python_folder_path)
        for module in part_information.get("modules"):
            self.current_module_string = ""
            self.module_path = ""
            self.current_module_name = module['module_name']
            self.build_python_module(module)
