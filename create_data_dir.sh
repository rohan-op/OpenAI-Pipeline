#!/bin/bash

# Define the base directory
base_dir="/N/u/shahrob/Carbonate/Research/Datasets"

# Define the intermediate directories
# intermediate_dirs=("Filter" "Transform")
intermediate_dirs=("Generative")

# Define the directories to be created
directories=("Chemistry" "Physics" "MaterialsScience" "Geology" "Mathematics" "Psychology" "Engineering" "EnvironmentalScience")

# Loop through intermediate directories
for intermediate_dir in "${intermediate_dirs[@]}"; do
    # Check if the intermediate directory exists
    if [ ! -d "$base_dir/$intermediate_dir/Domain" ]; then
        mkdir -p "$base_dir/$intermediate_dir/Domain"
    fi
    
    # Loop through directories and create them
    for dir in "${directories[@]}"; do
        mkdir -p "$base_dir/$intermediate_dir/Domain/$dir"
    done
done

echo "Directories created successfully."
