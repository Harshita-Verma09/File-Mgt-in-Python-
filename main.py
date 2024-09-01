import os 

#create NEW file
def create_file(filename):
    try: 
        with open(filename, "x") as f:
            print(f"File {filename} Created Successfully")
    except FileExistsError: 
        print(f"File {filename} already exists")

    except Exception as E:
        print("An Error Occured")


#View a new File
def view_file():
    try:
        files = os.listdir()
        if not files:
            print("No file found")
        else: 
            print("File directory are")
            for file in files:
                print(file)
    except FileNotFoundError:
        print("Path not Found")


#Delete New file
def delete_file(filename):
    try: 
        os.remove(filename)
    except FileNotFoundError:
        print("File Not Found")
    except Exception as E:
        print("An Error occur")


#Read a file
def read_file(filename):
    try:
        with open(filename, "r") as f:
            content = f.read()
            print(f"Content of{filename}: \n {content}")
    except FileNotFoundError:
        print("File Not found")

    except Exception as E:
        print("An error occur")


#Edit a file
def edit_file(filename):
    try:
        with open(filename, "a") as f:
            content= input("Enter your data you want to add ")
            f.write(content + "\n")
            print("Content added to Successfully ")
    except FileNotFoundError:
        print(f"File {filename} not found")
    except Exception as E:
        print("An error occur")


def main():
    while True:
        print("File management App")
        print("1: Create a file")
        print("2: View a file")
        print("3: Delete a file")
        print("4: Read a file")
        print("5: Edit  a file")
        print("6: Exit a file")

        choice = input("Enter your Choice(1-6) ")
        if choice == "1":
            filename = input("Enter file name for Create New  File: ")
            create_file(filename)

        elif choice =="2":
            view_file()
        
        elif choice == "3":
            filename = input("Enter file name for Delete: ")
            delete_file(filename)

        elif choice =="4":
            filename = input("Enter file name for  Read: ")
            read_file(filename)

        elif choice == "5":
            filename = input("Enter file name for Edit: ")
            edit_file(filename)

        elif choice == "6":
            print("Closing the app.......")
            break
        else:
            print("Enter Valid Number to continue this app..")
if __name__ == "__main__":
    main()
