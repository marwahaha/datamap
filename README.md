datamap
========

If you want to contribute, you can always make an issue or a pull request. Or, you can email me at marwahaha@berkeley.edu .

Development
-----------

To build locally, clone the repository and run ```jekyll serve``` at the command line. The website should be accessible from localhost:4000 . (Might need to run  ```bundle install``` in case you don't have all the ruby gems.)

Make sure you change the site url in the _config.yml to "http://localhost:4000" (otherwise, it will still pull stylesheets from online!)


Adding Data
-----------
To add to the resource tables, you can update the CSVs in the folder ```_data```.

There are Python scripts (```csv_to_jekyll_projects.py```, ```csv_to_jekyll_support.py```,```csv_to_jekyll_courses.py```) to run that will regenerate all files. Run them before ```jekyll serve```.
