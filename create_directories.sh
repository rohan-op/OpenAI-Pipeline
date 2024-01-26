#!/bin/bash

# Define the base directory
base_dir="/N/u/shahrob/Carbonate/Research/Scripts/Domain"

# List of directory names to create
directories=("Chemistry" "Physics" "Biology" "MaterialsScience" "Geology" "Mathematics" "Psychology" "Engineering" "EnvironmentalScience")

# Static content for raw.py
raw_py_content=""" 
import sys
sys.path.append("..")
from base import *
import pandas as pd

research_topics = {}
raw_df = get_papers(research_topics)
raw_df.to_csv("/N/u/shahrob/Carbonate/Research/Datasets/Raw/Domain/CompSci/raw_semantic_.csv", index=False)
"""

# Static content for raw_batch.script
raw_batch_content="""
#!/bin/bash

#SBATCH -J RAW_
#SBATCH -A general
#SBATCH -o /N/u/shahrob/Carbonate/Research/Scripts/Domain//output/_%j.out
#SBATCH -e /N/u/shahrob/Carbonate/Research/Scripts/Domain//error/_%j.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=shahrob@iu.edu
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --time=07:00:00
#SBATCH --mem=16G

# Load any modules that your program needs

# Activate your Python environment if necessary
source activate env

# Run your Python script
python raw.py"""

# Loop through the directory names and create the structure
for dir_name in "${directories[@]}"; do
    # Create the main directory
    mkdir -p "$base_dir/$dir_name"
    
    # Create "error" and "output" directories inside the main directory
    mkdir -p "$base_dir/$dir_name/error"
    mkdir -p "$base_dir/$dir_name/output"
    
    # Create and populate "raw.py" file
    echo -e "$raw_py_content" > "$base_dir/$dir_name/raw.py"
    
    # Create and populate "raw_batch.script" file
    echo -e "$raw_batch_content" > "$base_dir/$dir_name/raw_batch.script"
    
    # Print a message indicating the directory creation
    echo "Created directory: $base_dir/$dir_name"
done

echo "All directories created successfully."
