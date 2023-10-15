import os
import csv

# Input and output file paths
input_file_path = '/Users/alexeidias/Desktop/deed_finder_project/dashb/deed_hunter/output.csv'
output_file_path = '/Users/alexeidias/Desktop/deed_finder_project/dashb/deed_hunter/formatted_file.csv'
temp_file_path = '/Users/alexeidias/Desktop/deed_finder_project/dashb/deed_hunter/temp_file.csv'

# Open the input file in read mode and the temporary file in write mode
with open(input_file_path, 'r', newline='', encoding='utf-8') as input_file, \
        open(temp_file_path, 'w', newline='', encoding='utf-8') as temp_file:
    reader = csv.reader(input_file)
    writer = csv.writer(temp_file)

    # Initialize variables
    headers = None
    has_view_images = False

    # Loop through each row in the input file
    for row in reader:
        combined_row = ','.join(row).split(',')

        # If headers are not defined, it's the first data row
        if not headers:
            # Add "View Images" to headers
            headers = combined_row[1:] + ["View Images"]
            writer.writerow(headers)  # Write the header to the temporary file
        else:
            # If "View Images" is present after "Status" in this section
            if has_view_images and "View Images" in combined_row:
                # Fill in "View Images" in the corresponding cell
                view_images_index = headers.index("View Images") + 1
                combined_row[view_images_index] = "View Images"

            # Write the data to the temporary file
            writer.writerow([combined_row[headers.index(
                header) + 1].strip() if header in headers else "" for header in headers])

            # Check if the current section has "Status" and set has_view_images accordingly
            if "Status" in combined_row:
                has_view_images = "View Images" in combined_row

# Rename the temporary file to the final output file
os.rename(temp_file_path, output_file_path)
