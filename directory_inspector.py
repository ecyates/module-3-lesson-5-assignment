### Task 1: Directory Inspector

# Problem Statement: Create a Python script that lists all files and subdirectories in a given directory. 
# Your script should prompt the user for the directory path and then display the contents.
# 
# Expected Outcome: 
# - The script should correctly list all files and subdirectories in the specified directory. 
# - Handle exceptions for invalid paths or inaccessible directories.

import os

def list_directory_contents(directory):
    '''This function takes a directory and extracts the contents in a list. If there's sub-directory, 
    it will extract the contents of that directory as well, adding it as a dictionary within the list.'''
    contents = []
    try:
        # Raise error if the directory does not exist
        if not os.path.exists(directory):
            raise FileNotFoundError()
        # Extract the contents of the directory
        contents = os.listdir(directory)
        # Iterate over the contents
        for i, c in enumerate(contents):
            # If it is sub-directory, create a dictionary, where the key is the sub-directory
            # and the values are another list of content (calling the same function to provide that)
            if os.path.isdir(directory+"/" + c):
                contents[i] = {c: list_directory_contents(directory+"/" + c)}
    except FileNotFoundError:
        print("That directory does not exist.")
    finally:
        return contents # Return the list of content, if the directory doesn't exist, will return []

def main():
    try: 
        # Prompt the user for a directory path
        # If the user hits enter, it will provide the path for the current directory
        directory = os.path.realpath(input("Please input a directory path: "))
        # Call function and print the contents if it's not empty
        contents = list_directory_contents(directory)
        if contents != []:
            print(contents)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()