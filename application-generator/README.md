# Application Generator with Python

## Getting Started
This document explains how to generate a web application in the terminal. It assumes you are familiar with Python and know how to edit JSON file.

## Features
- The tool can generate a complete functioning website within an hour
- The tool can generate different backend languages and components (Authentication, Mail, Basic CRUD etc.) for any Module and corresponding frontend components (Contact form, Navigation, Slider etc.)
- The tool can generate same backend codebase (API) for different user interface such as IOS mobile app, Android mobile app and web browsers.
- The tool supports adding more frontend and backend modules

### A typical top-level directory layout
    .
    ├── application-generator 	# Application folder
		├── doc              	# Application docs
			├── ...
		├── src              	# Application src
			├── content			# Application contents
				├── ...
			├── handlers		# Application handlers
				├── ...
			├── usecases		# Application usecases
				├── ...
			├── main.py			# Application entry point
		├── tests              	# Application test case
		├── ...              
    └── ...

## Before You Start
You’ll need to have the following on your machine:
 - Python Version : >= 3.6.0.
 - Database : MySQL : >= 7.4.27
 - npm : >= v5.6
 - Node: >= v14.0.0
## Installation
- Clone the repository to your local computer
-  _cd_ into `application` folder
``` 
./application-generator
```
- Create virtual environment in [Windows](#markdown-header-windows) or [MacOS/Linux](#markdown-header-macos/linux) and install packages

# Running the application
The application has different handlers that require setting up to run the handler.

## Handlers
- [Python Handler](#markdown-header-python-handler-prerequisites)
- [React Handler](#markdown-header-react-handler-prerequisites)
- [Resource Handler](#markdown-header-resource-handler-prerequisites)
- [TailwindCSS Handler](#markdown-header-tailwindcss-handler-prerequisites)

## Python Handler Prerequisites
The python handler uses Python & MySQL database.
- Python Version : >= 3.6.0.
-  MySQL : >= 7.4.27.
### Next Step:
- Ensure you have MySQL running.
- Create database name, database user, and database password
```
CREATE USER 'database_user'@'localhost' IDENTIFIED BY 'password';
CREATE DATABASE database_name;
GRANT ALL PRIVILEGES ON database_name.* TO 'database_user'@'localhost';
``` 
- Create [secret key](#markdown-heade-generating-secret-key) and paste in the config section of the handler (Python) in the JSON file
```
"replacements": [
	{
		"pattern": "@@secret_key@@",
		"content": "2xMnqTxbfgppAWaOOBDbSA"
	}
],
```

### How it Works
The handler uses [Flask](https://flask.palletsprojects.com/en/2.1.x/) that requires `.env`, `config.py`, and `i_config.py` to run. The handler install Flask and then run migration and build `.env`, `config.py`, and `i_config.py` page and other modules e.g. contact_us from the source folder.

    .
    ├── application-generator 	# Application folder
		├── src              	# Application src
			├── content			# Application contents
				├── python		# Python source folder
					├── modules	# Python modules folder
						├── ...	# Python modules e.g. contact_us
							├── app
							├── ...
							├── .flask.env 	# Flask env variable declaration
							├── config.py	# Flask config
							├── i_config.py	# Flask config interface
							├── .env.py		# Flask env config
							├── ...
							├── run.py		# Flask entry point
				├── ...
			├── ...
		├── ...              
    └── ...

### Python Handler JSON Formatting
- It supports different key-variables.

*The env, config and i_config pages are required to run the handler*

```
{
	"application_name": "www.appname.tld",	# Apllication desired name
    "parts": [
		{
			"part_handler": "PythonHandler",	# Handle PythonHandler
			"modules": [
				{
					"module_name": "contact_us",	# Module source name: src/content/python/modules/contact_us
					"pages": [
						{
							"page_name": "env",		# Page name to be created
							"file_class": "Env",	# Predefined Python Class
							"file_group": "env",	# Predefined Python Class Group
							"file_name": "default",	# Predefined Python Class Group name
							"replacements": [
								{
									"pattern": "@@Config@@",				# Predefined File pattern to be replaced
									"content": "config.ProductionConfig"	# Replace pattern with content
								}
							],
							"sections": []	# Handle Modules Section: To be implemented
						},
                        {
                            "page_name": "config",	# Page name to be created
                            "file_class": "Config",	# Predefined Python Class
                            "file_group": "config",	# Predefined Python Class Group
                            "file_name": "default",	# Predefined Python Class Group name
                            "replacements": [
                                {
                                    "pattern": "@@db_user@@",		# Predefined File pattern to be replaced
                                    "content": "db_user"			# Replace pattern with content
                                },
                                {
                                    "pattern": "@@db_password@@",	# Predefined File pattern to be replaced
                                    "content": "password"			# Replace pattern with content
                                },
                                {
                                    "pattern": "@@db_name@@",		# Predefined File pattern to be replaced
                                    "content": "db_name"			# Replace pattern with content
                                }
                            ],
                            "sections": []
                        },
                        {
                            "page_name": "i_config",	# Page name to be created
                            "file_class": "IConfig",	# Predefined Python Class
                            "file_group": "i_config",	# Predefined Python Class Group
                            "file_name": "default",		# Predefined Python Class Group name
                            "replacements": [
                                {
                                    "pattern": "@@secret_key@@",		# Predefined File pattern to be replaced
                                    "content": "place secret key here"	# Replace pattern with content
                                }
                            ],
                            "sections": []
                        }
					]	# Handle Python pages
				}		# Handle Python Modules
			],
		} # Handles different Application parts
	]
}

```

## React Handler Prerequisites
The React handler uses Node Package Manager.
- npm : >= v5.6
- Node: >= v14.0.0

### How it Works
The handler installs the latest react version then install to the desired version (handles react versioning for package installation), deletes the source folder and copy necessary files (Components/Layouts) from the React source folder to the destination folder as it is been directed in the JSON file.
 
    .
    ├── application-generator 	# Application folder
		├── src              	# Application src
			├── content			# Application contents
				├── react		# React source folder
					├── components	# React components folder
						├── ...		# React components e.g. navbars.py, footers.py etc.
					├── layouts		# React layouts folder
						├── page_layout.py		# React page layout file
				├── ...
			├── ...
		├── ...              
    └── ...

### React Handler JSON Formatting
- It supports different key-variables
- Different pacages can be installed/imported to a page or component when specified in the JSON file.

*The react version key is required to install desired react version that is compactible with packages*

```
{
	"application_name": "www.appname.tld",	# Apllication desired name
    "parts": [
		{
			"part_handler": "ReactHandler",	# Handles ReactHandler
            "version": "0.0.0",				# Handles react versioning
            "pages": [
				{
					"page_name": "name",		# Page name to be created
                    "layout": "layout_name",	# Uses react Layout name
                    "replacements": [
                        {
                            "pattern": "@@Pattern@@",		# Predefined Layout pattern to be replaced
                            "content": "content goes here" 	# Replace pattern with content 
                    ],
                    "sections": [
						{
							"component_name": "Navbar1",	# Component name to be created
                            "template_class": "Navbars",	# Predefined Component Class name
                            "template_group": "navbars",	# Predefined Component Group name
                            "template_name": "navbar_1", 	# Predefined Component Class Group Tempalte name
                            "replacements": [
								{
									"pattern": "@@Pattern@@",		# Predefined Component pattern to be replaced
									"content": "content goes here" 	# Replace pattern with content
							],
                            "packages": [
								{
                                    "package_name": "react-package-name",		# Package to be installed for current Component
                                    "imports": [
                                        {
                                            "import_name": "Navbar1",	# Package Import name for current Component
                                            "import_src": "./Navbar1"	# Optional: Package name to be imported.
                                        }
                                    ]
                                }
							]
						}
					],
                    "packages": [
                        {
							"package_name": "package",		# Package to be installed for current Page
							"imports": [
								{
									"import_name": "Navbar1",	# Package Import name for current Page
									"import_src": "./Navbar1"	# Optional: Package name to be imported.
								}
							]
						}
                    ]
				}
			]	# Handles different page
		}	# Handles different Application parts
	]
}
```
## Resource Handler Prerequisites
The Resource handler copy file from one location to the other.

### How it Works
The handler copy either a file or folder from the resource folder to the destination folder as it is been directed in the JSON file.
 
    .
    ├── application-generator 	# Application folder
		├── src              	# Application src
			├── content			# Application contents
				├── resource		# Resource source folder
					├── images	# Resource image folder
						├── ...		# Application folder e.g. bestdealnaija, luday etc.
							├── ...		# Application images.
					├── styling		# Resource style folder
						├── styles.py		# Resource stles file
					├── ...		# Other resource folders to  be included. NB: not in place
				├── ...
			├── ...
		├── ...              
    └── ...


### Resource Handler JSON Formatting
- It supports different key-variables. 
- It supports copying files(e.g. styling) and folder(e.g. images). 

```
{
	"application_name": "www.appname.tld",	# Apllication desired name
    "parts": [
		{
			"part_handler": "ResourceHandler",	# Handle ResourceHandler
            "resources": [
                {
                    "resource_name": "styling",	# Resource name: resources/styling
                    "resource_type": "react", # Resource destination type
                    "resource_folder": "styling", # Resource source folder name i.e. styling
                    "sections": [
                        {
                            "file_name": "App",	# file name to be created
                            "source_class": "Styles",	# Styling source Class
                            "source_group": "styles",	# Styling source Class Group
                            "source_name": "styles_bestdealnaija_1",	# Styling source Class Group name
                            "source_type": "css"		# Styling type. example: file_name.css
                        }	# Handle sections
                    ]
                },
                {
                    "resource_name": "images",	# Resource name: resources/images
                    "resource_type": "react",	# Resource destination type
                    "resource_folder": "bestdealnaija", # Resource source folder name i.e. images/bestdealnaija for images
                    "sections": []
                }
            ]
		}	# Handles different Application parts
	]
}
```

## TailwindCSS Handler Prerequisites
The TailwindCSS handler uses Node Package Manager.
- npm : >= v5.6
- Node: >= v14.0.0

### How it Works
The handler installs the latest tailwindCSS config for a React application then replace the `content`, `theme` and `plugin` in the `tailwind.config.js` file if specified in the JSON file

### TailwindCSS Handler JSON Formatting
- It supports different key-variables

*A React application is required to be in place before running*

```
{
	"application_name": "www.appname.tld",	# Apllication desired name
    "parts": [
		{
			"part_handler": "TailwindCssHandler",	# Handles TailwindCSS event
			"plugins": [
				{
					"plugin_name": "plugin",	# Plugin to be installed
					"replacements": [
						{
							"pattern": "@@thirdPartyContent@@",	# Predefined plugin pattern to be replaced
							"content": "./node_modules/flowbite/**/*.js"	# Replace pattern with content
						},
						{
							"pattern": "@@thirdPartyTheme@@",	# Predefined plugin pattern to be replaced
							"content": "fontFamily: { sans: ['Graphik', 'sans-serif'],}"	# Replace pattern with content
						},
						{
							"pattern": "@@thirdPartyPlugins@@",	# Predefined plugin pattern to be replaced
							"content": "require('flowbite/plugin')"	# Replace pattern with content
						}
					]
				}
			]
		} # Handles different Application parts
	]
}
```
## Before You Run the Application
- Activate the [virtual environment](#markdown-header-installation) in the terminal
- Execute the command 
```
cd ./application-generator
python ./src/main.py --conf <JSON_FILE_NAME>
e.g python ./src/main.py --conf luday.json
```

# Generating secret key:
Execute the code in terminal:
```
>>> import secrets
>>> secrets.token_urlsafe(16)
```
# Windows
Open a command prompt or powershell and run the following commands, replacing 'project-root' with the path to the root folder of the project.
```
> cd 'application-generator'
> python -m venv venv
> venv\Scripts\activate.bat
> pip install -r requirements.txt
```

# MacOS/Linux
Open a terminal and run the following commands, replacing 'project-root' with the path to the root folder of the project.
```
$ cd 'application-generator'
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```
*Note: If you've installed Python 3 using a method other than Homebrew, you might need to type `python` in the second command instead of `python3`.*

# About pip
Versions pip updates frequently, but versions greater than 10.x.x should work with this project.

# Running PyReverse
Insert file name to generate file UML running the command
`pyreverse -o pic-name.png -a1 -s1 -mn ./file_name.py` in Linux

# under Development
To skip a acomponent under development
`"under_development": "yes",` 