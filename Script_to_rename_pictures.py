# Script to rename pictures
# Lennart Rathgeb | Ulm, 08-03-2024

import os
from tkinter import Tk, filedialog

# Exception Handling (sim. mk-ms-dir def confirm):
#   4 digit year input
#   Capital letters
#   single character input
#   empty input

def get_year_of_gig_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_month_of_gig_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_day_of_gig_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def ask_counter_offset_input(prompt):
    while True:
        value = input(prompt).strip().lower()
        if value == 'y':
            return get_counter_offset_input("Start counting at: ")
        elif value == 'n':
            return 1
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")

def get_counter_offset_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_valid_string_input(prompt):
    while True:
        value = input(prompt).strip().replace(" ", "_")  # Replace spaces with underscores
        if value:
            return value
        else:
            print("Input can not be empty. Please provide a name.")

def rename_pictures(input_folder, year, month, day, gig_name, location_name, location_town, first_name, last_name, i):
    offset = i if isinstance(i, int) else 1  # Check if i is an integer, otherwise set the offset to 1
    files = sorted([f for f in os.listdir(input_folder) if f.lower().endswith(('.jpg', '.jpeg'))])  # Consider only JPG and JPEG files

    print('') # Just to keep space

    for counter, filename in enumerate(files, start=offset):  # Start counting from the obtained offset
        if os.path.isfile(os.path.join(input_folder, filename)):
            file_extension = os.path.splitext(filename)[1]
            new_filename = f"{year}-{month}-{day}-{gig_name}-{location_name}-{location_town}-{str(counter).zfill(4)}-(c)-{first_name}-{last_name}{file_extension}"

            old_filepath = os.path.join(input_folder, filename)
            new_filepath = os.path.join(input_folder, new_filename)

            os.rename(old_filepath, new_filepath)
            print(f"Renamed: {filename} -> {new_filename}")
                      
def main():
    root = Tk()
    root.withdraw()

    input_folder = filedialog.askdirectory(title="Select Input Folder")
    year = str(get_year_of_gig_input("Enter the year of the gig (yyyy): "))
    month = str(get_month_of_gig_input("Enter the month of the gig (mm): ")).zfill(2)
    day = str(get_day_of_gig_input("Enter the day of the gig (dd): ")).zfill(2)
    gig_name = get_valid_string_input("Enter the name of the gig: ")
    location_name = get_valid_string_input("Enter the name of the gig location: ")
    location_town = get_valid_string_input("Enter the town of the gig location: ")
    first_name = get_valid_string_input("Enter the first name of the photographer: ")
    last_name = get_valid_string_input("Enter the last name of the photographer: ")
    i = ask_counter_offset_input("Do you want to offset the counter? (y/n): ")

    while True:
        print("\nReview your inputs:")
        print("1. Year: " + str(year))
        print("2. Month: " + str(month))
        print("3. Day: " + str(day))
        print("4. Gig Name: " + str(gig_name))
        print("5. Location Name: " + str(location_name))
        print("6. Town Name: " + str(location_town))
        print("7. First Name: " + str(first_name))
        print("8. Last Name: " + str(last_name))
        print("9. Counter Offset: " + str(i))

        confirm = str(input("\nTo change an input, type it's number or press ENTER to rename the pictures with the given input: ")).strip()

        if confirm == '':
            rename_pictures(input_folder, year, month, day, gig_name, location_name, location_town, first_name, last_name, i)
            print("Pictures renamed successfully.")
            break
        elif confirm == '1':
            year = str(get_year_of_gig_input("Enter the new year of the gig (yyyy): "))
        elif confirm == '2':
            month = str(get_month_of_gig_input("Enter the new month of the gig (mm): ")).zfill(2)
        elif confirm == '3':
            day = str(get_day_of_gig_input("Enter the new day of the gig (dd): ")).zfill(2)
        elif confirm == '4':
            gig_name = get_valid_string_input("Enter the new name of the gig: ")
        elif confirm == '5':
            location_name = get_valid_string_input("Enter the new name of the gig location: ")
        elif confirm == '6':
            location_town = get_valid_string_input("Enter the new town of the gig location: ")
        elif confirm == '7':
            first_name = get_valid_string_input("Enter the new first name of the photographer: ")
        elif confirm == '8':
            last_name = get_valid_string_input("Enter the new last name of the photographer: ")
        elif confirm == '9':
            i = ask_counter_offset_input("Do you want to offset the counter? (y/n): ")
        else:
            print("Invalid confirm. Please enter a valid input number (1-9).")


if __name__ == "__main__":
    main()
    input("Press ENTER to continue.")
