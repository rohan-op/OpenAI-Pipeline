import os
import sys
sys.path.append("..")
from base import filter_raw

base_dir = "/N/u/shahrob/Carbonate/Research/Datasets"
raw_dir= "Raw/Domain/Physics"
raw_fname= "raw_semantic_Physics.csv"

filter_dir ="Filter/Domain/Physics"
filter_fname = "filter_semantic_Physics.csv"

filter_raw(os.path.join(base_dir,raw_dir,raw_fname), os.path.join(base_dir,filter_dir,filter_fname))
