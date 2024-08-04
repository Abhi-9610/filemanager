import os

FOLDER_NAME = 'Uploads'

def ensure_folder_exists():
    if not os.path.exists(FOLDER_NAME):
        os.makedirs(FOLDER_NAME)

def create(filename):
    ensure_folder_exists()
    file_path = os.path.join(FOLDER_NAME, filename)
    try:
        with open(file_path, 'x') as f:
            print(f"{filename} created successfully in {FOLDER_NAME} folder!")
    except FileExistsError:
        print('File already exists! Try with another name.')
    except Exception as e:
        print('Error occurred:', e)

def edit(filename):
    ensure_folder_exists()
    file_path = os.path.join(FOLDER_NAME, filename)
    try:
        with open(file_path, 'a') as f:
            content = input('Enter the content to append to the file: ')
            f.write(content + '\n')
            print('Content edited successfully!')
    except FileNotFoundError:
        print('File not found! Try with another name.')
    except Exception as e:
        print('Error occurred:', e)

def read(filename):
    ensure_folder_exists()
    file_path = os.path.join(FOLDER_NAME, filename)
    try:
        with open(file_path, 'r') as f:
            content = f.read()
            print(f"Content of the file:\n{content}")
    except FileNotFoundError:
        print('File not found!')
    except Exception as e:
        print('Error occurred:', e)

def allfile():
    ensure_folder_exists()
    try:
        files = os.listdir(FOLDER_NAME)
        if not files:
            print('No files found in the folder!')
        else:
            print(f'Files in the {FOLDER_NAME} folder:')
            for file in files:
                print(file)
    except Exception as e:
        print('Error occurred:', e)

def delete(filename):
    ensure_folder_exists()
    file_path = os.path.join(FOLDER_NAME, filename)
    try:
        os.remove(file_path)
        print(f"{filename} deleted successfully!")
    except FileNotFoundError:
        print('File not found!')
    except Exception as e:
        print('Error occurred:', e)

def main():
    try:
        print('WELCOME TO FILEMANAGER!')
        options = {1: 'Create file', 2: 'Read file', 3: 'Update file', 4: 'View all files', 5: 'Delete file', 6: 'Exit App'}
        print("\nOptions available:")
        for i in range(1, 7):
                print(f"{i}. {options[i]}")
        while True:
            
            
            choice = input('Enter your choice: ')
            if choice == '1':
                filename = input('Enter the filename to create: ')
                create(filename)
            elif choice == '2':
                filename = input('Enter the filename to read: ')
                read(filename)
            elif choice == '3':
                filename = input('Enter the filename to edit: ')
                edit(filename)
            elif choice == '4':
                allfile()
            elif choice == '5':
                filename = input('Enter the filename to delete: ')
                delete(filename)
            elif choice == '6':
                print('Exiting App!')
                break
            else:
                print('Enter a valid input.')

    except Exception as e:
        print(f'Error occurred: {e}')

if __name__ == "__main__":
    main()
