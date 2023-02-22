from usecase.i_data_handler import IDataHandler
from os import path
import shutil,platform, os, pathlib, logging
from distutils.dir_util import copy_tree

logger = logging.getLogger(path.basename(__file__))

class FileHandler(IDataHandler):

    def __init__(self):
        self.generated_folder = pathlib.Path(__file__).parent.resolve() / ".." / ".." / "generated"
        self.conf_folder = pathlib.Path(__file__).parent.resolve() / ".." / "content" / "conf"
        self.python_modules_folder = pathlib.Path(__file__).parent.resolve() / ".." / "content" / "python" / "modules"
        self.resources_folder = pathlib.Path(__file__).parent.resolve() / ".." / "content" / "resources"
        self.root_directory = pathlib.Path(__file__).parent.resolve() / ".." / ".."

    def write(self, content, path):
        self.create_folder(pathlib.Path(path).parent.resolve())
        with open(f"{path}", 'w', encoding='utf-8') as file:
            file.write(content)
            
    def create_folder(self, path):
        try:
            os.makedirs(path)
        except FileExistsError:
            # directory already exists
            pass

    def copy_file(self, src, dest):
        # shutil.copy2(path, dest / path.relative_to(source))
        pass

    def copy_directory(self, src, dest):
        try:
            copy_tree(src, dest)
        
        # except DistutilsFileError: TODO(dayo) Investigate why:  "name 'DistutilsFileError' is not defined"
            #logger.debug("Not a directory. Copying as file instead")
            #self.create_folder(dest)
            #shutil.copy(src, dest)

        except PermissionError:
            logger.debug("PermissionError: [Errno 13] Permission denied:")

        except Exception as e:
            logger.debug(f"{e.__str__()}. Trying to copy as file instead." )
            self.create_folder(dest)
            shutil.copy(src, dest)

    def remove(self, file):
        if os.path.isfile(file):
            os.remove(file)
        else:
            logger.debug(f"{file}: does not exist!")


    def get_application_root_folder(self, application_name : str):
        application_root_path = f"{self.generated_folder}/{application_name}"
        is_exist = os.path.exists(application_root_path)
        if is_exist:
            logger.debug(f"Application folder exist already: {application_root_path}")
        else:
            os.makedirs(application_root_path)
            logger.debug(f"New application folder created: {application_root_path}")
        return application_root_path


    def is_path_exist(self, path):
        is_exist = os.path.exists(path)
        if is_exist:
            logger.debug(f"Exist: {path}")
            return True
        else:
            logger.debug(f"Does not exist: {path} ")
            return False


    def get_conf_file_path(self):
        return self.conf_folder


    def get_resources_file_path(self):
        return self.resources_folder


    def get_python_modules_file_path(self):
        return self.python_modules_folder


    def get_root_directory(self):
        return self.root_directory


    def install_python_package(self, module_path, python_venv_folder):
        if platform.system() == 'Windows':
            logger.debug(f"Installing application packages: {module_path}/{python_venv_folder}")
            os.system(f"{module_path}/{python_venv_folder}/Scripts/activate.bat \
                && cd {module_path} \
                && pip install -r requirements.txt"
            )

        else:
            logger.debug(f"Installing application packages: {module_path}/{python_venv_folder}")
            os.system(f"source {module_path}/{python_venv_folder}/bin/activate \
                && cd {module_path} \
                && pip install -r requirements.txt"
            )
