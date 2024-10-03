# Name of the TXT files
old_record = "student_record_v1.txt"
new_record = "student_record_v2.txt"

# Read the old_record TXT file
with open(old_record, 'r') as record:
    read = record.readlines()

# Store the readlines data here
ids = []
first_names = []
last_names = []
campuses = []
modes = []

# Extract the data into a list and remove spaces
for x in range(5):
    ids.append(read[x].strip())
    first_names.append(read[x + 5].strip())
    last_names.append(read[x + 10].strip())
    campuses.append(read[x + 15].strip())
    modes.append(read[x + 20].strip())

# Open the new record file for writing
with open(new_record, 'w') as record:
    for i in range(5):
        student_id = ids[i]
        first_name = first_names[i]
        last_name = last_names[i]
        campus = campuses[i]
        mode_of_study = modes[i]

        # Sets/Creates the email address for each person
        email = "{}_{}@yoobeecolleges.com".format(first_name.lower(), last_name.lower())

        # Printing the fixed format data into the new TXT file
        print("Student ID: {}".format(student_id), file=record)
        print("First Name: {}".format(first_name), file=record)
        print("Last Name: {}".format(last_name), file=record)
        print("Campus: {}".format(campus), file=record)
        print("Mode of Study: {}".format(mode_of_study), file=record)
        print("Email: {}".format(email), file=record)
        print("", file=record)
