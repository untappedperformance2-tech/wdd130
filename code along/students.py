import csv

def read_dictionary(filename, key_column_index):
    s_dictionary = {}
    with open(filename, 'rt') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if not row:
                continue
            key_value = row[key_column_index]
            s_dictionary[key_value] = row
    return s_dictionary

def main():
    KEY_INDEX = 0
    NAME_INDEX = 1
    
    students = read_dictionary('students.csv', KEY_INDEX)
    
    # Loop until a valid I-Number is entered and found
    while True:
        inumber = input("Please enter an I-Number: ")
        inumber = inumber.replace("-", "")
        
        # Validate the I-Number
        if not inumber.isdigit():
            print("Invalid character in I-Number. Please try again.")
            continue  # Go back to the start of the loop
        
        if len(inumber) < 9:
            print(f"Invalid I-Number: too few digits (has {len(inumber)} digits, needs 9). Please try again.")
            continue
        
        if len(inumber) > 9:
            print(f"Invalid I-Number: too many digits (has {len(inumber)} digits, needs 9). Please try again.")
            continue
        
        # If we get here, the I-Number is valid format (9 digits)
        # Now check if it exists in our dictionary
        if inumber in students:
            student_info = students[inumber]
            name = student_info[NAME_INDEX]
            print(f"The student's name is {name}")
            break  # Exit the loop since we found the student
        else:
            print("No such student! Please try again.")
            # Continue looping to ask for input again

if __name__ == "__main__":
    main()