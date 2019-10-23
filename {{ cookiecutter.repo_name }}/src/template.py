#!/usr/bin/env python
# coding: utf-8
################################################################################
# Template for most scripts
################################################################################
import sys, os, glob
import logging
logging.basicConfig(level=logging.INFO)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import astropy.table
#import plotdefaults
#from plotdefaults import axis_font, title_font

import dotenv
from dotenv import find_dotenv, load_dotenv, dotenv_values
load_dotenv(find_dotenv())
#sys.path.append(os.environ.get("common_lib_dir"))
#sys.path.append(os.environ.get("local_lib_dir"))

# find .env automagically by walking up directories until it's found, then
# load up the .env entries as environment variables
dotenv.load_dotenv(dotenv.find_dotenv())
parsed_dotenv = dotenv.dotenv_values()
sys.path.append(parsed_dotenv["common_lib_dir"])
sys.path.append(parsed_dotenv["local_lib_dir"])

save_dir = os.path.join(parsed_dotenv["report_dir"], f"progress/{parsed_dotenv['progress_dir']}")
################################################################################
