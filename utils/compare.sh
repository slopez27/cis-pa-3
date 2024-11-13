#!/bin/bash

# List of file names
file_names=("PA3-A-Debug" "PA3-B-Debug" "PA3-C-Debug" "PA3-D-Debug" "PA3-E-Debug" "PA3-F-Debug")
expected_dir="../data"
actual_dir="../outputs"
# Loop through each pair and calculate the percent error
for name in "${file_names[@]}"; do
    set -- $name 
    expected="${expected_dir}/${name}-Output.txt"
    actual="${actual_dir}/${name}-Output.txt"

    # Check if both files exist
    if [ ! -f "$expected" ] || [ ! -f "$actual" ]; then
        echo "Error: One or both files ($expected, $actual) do not exist. Must do run_all_files.sh first."
        continue
    fi

    echo "Calculating percent error for $expected and $actual:"
    
    # Calculate the percent error of the magnitude differences
    paste <(awk '{print $NF}' "$expected") <(awk '{print $NF}' "$actual") | \
        awk '{if ($1 != 0) print (($2 - $1) / $1) * 100; else print "0"}'

    echo 
done

exit 0
