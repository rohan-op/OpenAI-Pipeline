import os
import sys
sys.path.append("..")
from base import transform

base_dir = "/N/u/shahrob/Carbonate/Research/Datasets"

filter_dir ="Filter/Domain/Geology"
filter_fname = "filter_semantic_Geology.csv"

transform_dir = "Transform/Domain/Geology"
transform_fname = "transform_semantic_Geology.csv"

transform(os.path.join(base_dir,filter_dir,filter_fname), os.path.join(base_dir,transform_dir,transform_fname))
