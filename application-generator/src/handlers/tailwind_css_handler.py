from usecase.i_part_handler import IPartHandler
from usecase.i_data_handler import IDataHandler
from content.react.layouts.page_layouts import PageLayouts
from .partials.tailwind_css_init import TailwindCssInit
from os import path
import os
import logging

 
logger = logging.getLogger(path.basename(__file__))

 
class TailwindCssHandler(IPartHandler):
    
    
    def __init__(self, data_handler : IDataHandler):
        
        self.data_handler = data_handler
        self.tailwind_css_setup_complete = ".tailwind_css_setup_complete"
        self.application_path = ""
        self.index_css_file_name = TailwindCssInit.tailwind_css_init_['index_css_file_name']
        self.tailwind_config_file_name = TailwindCssInit.tailwind_css_init_['tailwind_config_file_name']
        self.tailwind_config_plugins = ""
        self.tailwind_config_current_plugin_name = ""
        
        self.index_css_content ="""
@tailwind base;
@tailwind components;
@tailwind utilities;

@import url('https://fonts.googleapis.com/css2?family=Fjalla+One&family=Roboto:wght@500&display=swap');
"""
        
        self.tailwind_config_content="""
module.exports = {
    content: [
        "./src/**/*.{js,jsx,ts,tsx}",
        "@@thirdPartyContent@@",
    ],
    theme: {
        @@thirdPartyTheme@@
        extend: {
            colors: {
                primary: '#9c0',
                secondary: '#84b000'
            },
            @@thirdPartyThemeExtension@@
        }
    },
    plugins: [
        @@thirdPartyPlugins@@
    ]
}
"""
                   
    def replace_variables(self, replacement_variables, content):
        for variable in replacement_variables:
            content = content.replace(variable["pattern"], variable["content"])
            logger.debug(f"Replaced {variable['pattern']} with {variable['content']}")
        return content

    
    def remove_variables(self, content):
        content = content.replace('"@@thirdPartyContent@@",', "")
        content = content.replace("@@thirdPartyTheme@@", "")
        content = content.replace("@@thirdPartyPlugins@@", "")
        content = content.replace("@@thirdPartyThemeExtension@@", "")
        logger.debug(f"Replaced tailwind plugins variables")
        return content


    def setup_tailwind_config_plugins(self):
        self.tailwind_config_current_plugin_name = ""
        for tailwind_plugin in self.tailwind_config_plugins:
            self.tailwind_config_current_plugin_name = tailwind_plugin['plugin_name']
            replacements = tailwind_plugin["replacements"]
            if not replacements:
                self.tailwind_config_content = self.remove_variables(self.tailwind_config_content)
            else:
                self.tailwind_config_content = self.replace_variables(tailwind_plugin["replacements"], self.tailwind_config_content)

           
    def setup_tailwind_css(self, part_information : str):
        install_path = f"{self.application_path}/{part_information.get('install_path')}"
        is_tailwind_css_setup_complete = self.data_handler.is_path_exist(f"{install_path}/{self.tailwind_css_setup_complete}")
        
        if is_tailwind_css_setup_complete:
            logger.debug(f"Tailwind was already setup for {self.application_path}")
        else:
            os.system(f"cd {self.application_path} && npm install -D tailwindcss postcss autoprefixer")
            os.system(f"cd {self.application_path} && npx tailwindcss init -p")
            logger.debug(f"Tailwind css setup successfully in {self.application_path}")
            self.data_handler.write(self.index_css_content, f"{install_path}/{self.index_css_file_name}")
            self.tailwind_config_plugins = part_information['plugins']
            if self.tailwind_config_plugins:
                self.setup_tailwind_config_plugins()
            else:
                self.tailwind_config_content = self.remove_variables(self.tailwind_config_content)
                
            self.data_handler.write(self.tailwind_config_content, f"{self.application_path}/{self.tailwind_config_file_name}")
            self.data_handler.write("Tailwind css setup complete", f"{install_path}/{self.tailwind_css_setup_complete}")    

  
    def handle_part(self, application_name : str, part_information):
        logger.debug("Handle React application")
        self.application_path = self.data_handler.get_application_root_folder(application_name)
        self.tailwind_config_plugins = ""
        self.setup_tailwind_css(part_information)
        

