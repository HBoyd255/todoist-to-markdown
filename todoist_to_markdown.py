import sys
import csv

# Harry Boyd - hboyd255@gmail.com - 06/05/2024

ENCODING = "utf-8-sig"

SECTION_HEADER_LEVEL = 2
SECTION_HEADER = SECTION_HEADER_LEVEL * "#" + " "

from datetime import date

creation_date = date.today().strftime("%d/%m/%Y")
creation_credit = "https://github.com/HBoyd255/todoist-to-markdown"


# # If no arguments are provided, print usage
# if len(sys.argv) != 2:
#     print("Please provide the input csv file as an argument.")
#     sys.exit()
#
# # Get the file name of the input csv file
# project_csv = sys.argv[1]


project_csv = "Demo.csv"

# Get the project name from the csv file name.
project_name = project_csv.split(".")[0]

# Create the output markdown file name.
project_md = project_name + ".md"

# Open the csv file and read the contents.
with open(project_csv, "r", encoding=ENCODING) as csv_file:

    # Create a csv reader object. The first row of the csv file will be the keys
    # for the dictionary.
    csv_reader = csv.DictReader(csv_file)

    # Create the markdown file and write the contents.
    with open(project_md, "w", encoding=ENCODING) as md_file:

        # Write the project name as the header.
        md_file.write(f"# {project_name}\n\n")

        # Write the creation date and credit as comments.
        md_file.write("<!-- File created on: " + creation_date + " -->\n\n")
        md_file.write("<!-- File created by: " + creation_credit + " -->\n\n")

        # Iterate through the csv file.
        for row in csv_reader:

            # Get the item type, name, and description.
            item_type = row["TYPE"]
            item_name = row["CONTENT"]
            item_description = row["DESCRIPTION"]

            # If the item is a section, write it as a header.
            if item_type == "section":
                md_file.write(SECTION_HEADER)
                md_file.write(item_name)
                md_file.write("\n\n")

            # If the item is a task, write it as a header, with a description if it exists.
            if item_type == "task":
                # If the name of the item starts with an asterisk, it is not a
                # completable task.
                # https://todoist.com/help/articles/how-to-create-an-uncompletable-task-QxQosZuF
                completable = item_name[0] != "*"

                # If the item is not completable, remove the asterisk.
                if not completable:
                    item_name = item_name[2:]

                # Remove any labels from the item name.
                item_name = item_name.split("@")[0]

                # If the task is completable, add a checkbox.
                if completable:
                    md_file.write("- [ ] ")

                # Write the task name.
                md_file.write(item_name)

                ## Add two new lines to separate the task
                md_file.write("\n\n")
