import sys
import os
import glob
import click
import dotenv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# find .env automagically by walking up directories until it's found, then
# load up the .env entries as environment variables
dotenv.load_dotenv(dotenv.find_dotenv())
sys.path.append(os.environ.get("common_lib_dir"))
