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

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())
sys.path.append(os.environ.get("common_lib_dir"))
sys.path.append(os.environ.get("local_lib_dir"))

# find .env automagically by walking up directories until it's found, then
# load up the .env entries as environment variables
dotenv.load_dotenv(dotenv.find_dotenv())
sys.path.append(os.environ.get("common_lib_dir"))

progress_dir = os.environ.get("progress_dir")
save_dir     = os.path.join(os.environ.get("report_dir"), f"/progress/{progress_dir}")
data_dir     = os.path.join(os.environ.get("data_dir"))
################################################################################
