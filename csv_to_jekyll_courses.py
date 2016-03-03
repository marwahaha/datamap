# Takes a file CSV file called "_data/projects.csv" and outputs each row as a YAML file named after first column.
# Data in the first row of the CSV is assumed to be the column heading.
# Original work borrowed from: https://github.com/hfionte/csv_to_yaml

# remove contents of projects folder
import shutil, os
shutil.rmtree('courses')
os.mkdir('courses')

# Import the python library for parsing CSV files.
import csv

# Open our data file in read-mode.
csvfile = open('_data/courses.csv', 'r')

# Save a CSV Reader object.
datareader = csv.reader(csvfile, delimiter=',', quotechar='"')

# Empty array for data headings, which we will fill with the first row from our CSV.
data_headings = []

# Loop through each row...
for row_index, row in enumerate(datareader):

	# If this is the first row, populate our data_headings variable.
	if row_index == 0:
		data_headings = row

	# Otherwise, create a YAML file from the data in this row...
	else:
		# Open a new file with filename based on the column named title
		filename = 'courses/' + row[data_headings.index('title')].lower().replace(" ", "-").replace("/","-").replace(":","-") + '.md'
		new_yaml = open(filename, 'w')

		# Empty string that we will fill with YAML formatted text based on data extracted from our CSV.
		yaml_text = ""
		yaml_text += "---\n"
		yaml_text += "layout: course \n"

		# Loop through each cell in this row...
		for cell_index, cell in enumerate(row):

			# Compile a line of YAML text from our headings list and the text of the current cell, followed by a linebreak.
			# Heading text is converted to lowercase. Spaces are converted to hyphens.
			# In the cell text, line endings are replaced with commas.
			cell_heading = data_headings[cell_index].lower().replace(" ", "-").replace("%", "percent").replace("$", "").replace(",", "").replace("#","number")
			cell_text = cell_heading + ": " + cell.replace("\n", ", ").replace(":"," -") + "\n"

			# Add this line of text to the current YAML string.
			if len(cell_heading) > 0:
				yaml_text += cell_text

		# Write our YAML string to the new text file and close it.
		new_yaml.write(yaml_text + "---\n")
		new_yaml.close()

# We're done! Close the CSV file.
csvfile.close()