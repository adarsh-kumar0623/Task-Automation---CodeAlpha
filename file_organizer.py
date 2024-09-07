import os
import shutil

def organize_files(directory):
    # Create a dictionary to store files by extension
    files_by_extension = {}

    # Iterate through files in the directory
    for filename in os.listdir(directory):
        # Get the file extension
        file_extension = os.path.splitext(filename)[1][1:]

        # Create a subdirectory for the file extension if it doesn't exist
        extension_dir = os.path.join(directory, file_extension)
        if not os.path.exists(extension_dir):
            os.makedirs(extension_dir)

        # Move the file into the appropriate subdirectory
        shutil.move(os.path.join(directory, filename), os.path.join(extension_dir, filename))

        # Add the file to the dictionary
        if file_extension not in files_by_extension:
            files_by_extension[file_extension] = []
        files_by_extension[file_extension].append(filename)

    # Print a summary of the organized files
    for extension, files in files_by_extension.items():
        print(f"Moved {len(files)} files to {extension} directory")

if __name__ == "__main__":
    # Specify the directory to organize
    target_directory = 'path/to/your/directory'
    organize_files(target_directory)