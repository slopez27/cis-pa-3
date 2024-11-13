#!/bin/bash

# Array of names to run the main function on
names=("PA3-A-Debug" "PA3-B-Debug" "PA3-C-Debug" "PA3-D-Debug" "PA3-E-Debug" "PA3-F-Debug" "PA3-G-Unknown" "PA3-H-Unknown" "PA3-J-Unknown" )

# Run the main function for each unknown 
for name in "${names[@]}"; do
    echo "Processing $name..."
    
    # Run the Python script with the current name
    python3 main_pa3.py "$name" "3"

done
