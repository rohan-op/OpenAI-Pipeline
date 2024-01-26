import os
import sys
sys.path.append("..")
from base import filter_raw

base_dir = "/N/u/shahrob/Carbonate/Research/Datasets"
raw_dir= "Raw/Domain/Engineering"
raw_fname= "raw_semantic_Engineering.csv"

filter_dir ="Filter/Domain/Engineering"
filter_fname = "filter_semantic_Engineering.csv"

filter_raw(os.path.join(base_dir,raw_dir,raw_fname), os.path.join(base_dir,filter_dir,filter_fname))
