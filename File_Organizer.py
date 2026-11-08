import os
import shutil

# Sorting file extensions by their file type
# Files that don't match any of these extensions go into "Other"
file_categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Audio": [".mp3", ".wav"],
    "Other": []
}

# Prevents files with the same name From overwriting each other
def get_unique_filename(destination):
    # If the filename is available, use it
    if not os.path.exists(destination):
        return destination
    # separates the folder path and filename
    folder = os.path.dirname(destination)
    filename = os.path.basename(destination)

    #Seperates the filename from its extension
    name, extension = os.path.splitext(filename)

    # Start numbering duplicate files at 1
    counter = 1

    # Keep checking filenames until an available one is found
    while True:
        new_filename = f"{name}_{counter}{extension}"
        destination = os.path.join(folder, new_filename)

        # Stop the loop when the filename is available
        if not os.path.exists(destination):
            break

        # Increase the number if the filename already exists
        counter += 1
    # Return the available filename
    return destination

# Shows the directory where the program is running
print("Looking in:", os.getcwd())

# This organizes the files into folders by type
def organize_files(folder_path):

    # Checks if the folder exists before continuing
    if os.path.isdir(folder_path):
        print("\nFolder found!")

        # looks through everything inside the selected folder
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)

            # only organizes files, not existing folders
            if os.path.isfile(file_path):

                #Get the file extension in lowercase
                file_extension = os.path.splitext(filename)[1].lower()

                #Tracks whether the file matches a category
                moved = False

                # Checks the file extension against each category.
                for category, extensions in file_categories.items():
                    if category != "Other" and file_extension in extensions:

                        # Create the category folder if it doesn't exist.
                        category_folder = os.path.join(folder_path, category)
                        os.makedirs(category_folder, exist_ok=True)

                        # Set the destination for the file.
                        destination = os.path.join(category_folder, filename)

                        # Prevent duplicate filenames.
                        destination = get_unique_filename(destination)

                        try:
                            # Move the file into its category folder
                            shutil.move(file_path, destination)
                            print(f"Moved {filename} to {category}")

                        # Handle files that cannot be accessed
                        except PermissionError:
                            print(f"Permission denied: {filename}")

                        # Handle other errors when moving files
                        except OSError as error:
                            print(f"Could not move {filename}: {error}")

                        #Stop checking categories after a match
                        moved = True
                        break

                # Files without a matching category go into Other
                if not moved:

                    # create the other folder if needed
                    other_folder = os.path.join(folder_path, "Other")
                    os.makedirs(other_folder, exist_ok=True)

                    # set the  destination for unmatched files
                    destination = os.path.join(other_folder, filename)

                    # prevents duplicate filenames
                    destination = get_unique_filename(destination)

                    try:
                        # move the file into the other folder
                        shutil.move(file_path, destination)
                        print(f"Moved {filename} to Other")

                    except PermissionError:
                        print(f"Permission denied: {filename}")

                    except OSError as error:
                        print(f"Could not move {filename}: {error}")

        print("\nOrganization complete!")

    else:
        # display an error if the folder does not exist
        print("\nFolder does not exist.")

# keep the program running until the user chooses to exit
while True:
    # Display the main menu
    print("\n===== FILE ORGANIZER =====")
    print("1. Organize files")
    print("2. Exit")

    # ask the user to choose an option
    choice = input("Select an option: ")

    if choice == "1":

        # Ask which folder the user wants to organize
        folder_path = input("Enter folder path: ")
        # Run the file organizing function
        organize_files(folder_path)

    elif choice == "2":
        # Close the program
        print("Exiting File Organizer...")
        break

    else:
        # Handle invalid menu selections
        print("Invalid option. Please try again.")

