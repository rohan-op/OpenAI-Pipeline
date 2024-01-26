import os
import sys
sys.path.append("..")
from base import transform

base_dir = "/N/u/shahrob/Carbonate/Research/Datasets"

filter_dir ="Filter/Domain/Physics"
filter_fname = "filter_semantic_Physics.csv"

transform_dir = "Transform/Domain/Physics"
transform_fname = "transform_semantic_Physics.csv"

transform(os.path.join(base_dir,filter_dir,filter_fname), os.path.join(base_dir,transform_dir,transform_fname))
