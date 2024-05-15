# Script to rename pictures
# Lennart Rathgeb | Ulm, 08-03-2024

import os
from tkinter import Tk, filedialog

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

    for counter, filename in enumerate(files, start=offset):  # Start counting from the obtained offset
        if os.path.isfile(os.path.join(input_folder, filename)):
            file_extension = os.path.splitext(filename)[1]
            new_filename = f"{str(year).zfill(4)}-{str(month).zfill(2)}-{str(day).zfill(2)}-{gig_name}-{location_name}-{location_town}-{str(counter).zfill(4)}-(c)-{first_name}-{last_name}{file_extension}"

            old_filepath = os.path.join(input_folder, filename)
            new_filepath = os.path.join(input_folder, new_filename)

            os.rename(old_filepath, new_filepath)
            print(f"Renamed: {filename} -> {new_filename}")
                      
def main():
    root = Tk()
    root.withdraw()

    input_folder = filedialog.askdirectory(title="Select Input Folder")
    year = get_year_of_gig_input("Enter the year of the gig (yyyy): ")
    month = get_month_of_gig_input("Enter the month of the gig (mm): ")
    day = get_day_of_gig_input("Enter the day of the gig (dd): ")
    gig_name = get_valid_string_input("Enter the name of the gig: ")
    location_name = get_valid_string_input("Enter the name of the gig location: ")
    location_town = get_valid_string_input("Enter the town of the gig location: ")
    first_name = get_valid_string_input("Enter the first name of the photographer: ")
    last_name = get_valid_string_input("Enter the last name of the photographer: ")
    i = ask_counter_offset_input("Do you want to offset the counter? (y/n): ")

    rename_pictures(input_folder, year, month, day, gig_name, location_name, location_town, first_name, last_name, i)

if __name__ == "__main__":
    main()
    input("Press ENTER to continue.")
