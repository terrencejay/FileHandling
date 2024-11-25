# Problem Statement: Create a Python script that lists all files and subdirectories in a given directory. Your script should prompt the user for the directory path and then display the contents.

# Code Example:
#     import os

#     def list_directory_contents(path):
#         # List and print all files and subdirectories in the given path
# Expected Outcome: The script should correctly list all files and subdirectories in the specified directory. Handle exceptions for invalid paths or inaccessible directories.

import os

def list_directory_contents(path):
    try:
        if path:
            for root, dirs, files in os.walk(path):
                print(f"\nDirectory: {root}")
                if dirs:
                    print("subdirectories")
                    for dir in dirs:
                        print(f"\n{dir}")
                if files:
                    print("Here are the contents")
                    for file in files:
                        print(f"\n{file}")
    except FileNotFoundError: 
        print("directory not found please check your path and try again")
            
directory_path = input("What is the path of your directory?: ").strip()
            
list_directory_contents(directory_path)