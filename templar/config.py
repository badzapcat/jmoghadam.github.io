import os
import re
# Import various utilities from utils
import templar.utils.html
import templar.utils.filters

# Path of the current file -- best not to change this
FILEPATH = os.path.dirname(os.path.abspath(__file__))
PH_PATH = "../"

if os.path.isfile("PH_PATH"):
    with open("PH_PATH", 'r') as f:
        for line in f:
            PH_PATH = line.rstrip()

PH_ASSETS_PATH = os.path.join(PH_PATH, "assets")

##################
# Configurations #
##################

configurations = {
    # List of directories in which to search for templates
    'TEMPLATE_DIRS': [
        FILEPATH,
        # Add directories that contain templates
        # os.path.join(FILEPATH, 'example'),
    ],

    # Variables that can be used in templates
    'VARIABLES': {
        'link_open_sans': "https://fonts.googleapis.com/css?family=Open+Sans:300,400,600",
        'link_common_css': os.path.join(PH_ASSETS_PATH, "css/common.css"),
        'link_lab_css': os.path.join(PH_ASSETS_PATH, "css/lab.css"),
        'link_jquery': os.path.join(PH_ASSETS_PATH, "js/jquery-1.11.2.min.js"),
        'link_script': os.path.join(PH_ASSETS_PATH, "js/script.js"),

        'link_index': os.path.join(PH_PATH, "index.html"),

    },

    # Substitutions for the linker
    'SUBSTITUTIONS': [
        ('<home-page-link>', PH_PATH),
        # Add substitutions of the form
        # (regex, sub_function),
        # (regex, sub_function, condition),
    ],

    # Use the following to scrape "headers"
    # TOC_BUILDER should be a subclass of templar.utils.core.TocBuilder
    # 'TOC_BUILDER': templar.utils.htmlHeaderParser,
}
