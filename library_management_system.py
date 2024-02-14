class Library:
    def __init__(self, filename='books.txt'):
        self.filename = filename
        self.file = open(self.filename, 'a+')

    def __del__(self):
        self.file.close()

    def books(self):
        self.file.seek(0)
        data = self.file.read()
        books_list = data.splitlines()
        list_of_books = []
        for books in books_list:
            info = books.split(",")
            list_of_books.append(info[0].upper())
        return list_of_books

    def list_books(self):
        self.file.seek(0)  # to read the text from the beginning
        data = self.file.read()
        books_list = data.splitlines()
        if not books_list:
            print("There is no book.")
        else:
            for books in books_list:
                info = books.split(',')
                print(f"Book Title: {info[0]}, Author: {info[1]}")

    def add_book(self):
        title = input("Enter the book title: ")
        if title == "":
            return False

        author = input("Enter the author of the book: ")
        if author == "":
            return False

        release_year = input("Enter the release year of the book: ")
        if release_year == "":
            return False
        else:
            while not release_year.isdigit() or int(release_year) == 0:
                release_year = input("Please provide a valid year: ")

        number_of_pages = input("Enter the number of pages of the book: ")
        if number_of_pages == "":
            return False
        else:
            while not number_of_pages.isdigit() or int(number_of_pages) == 0:
                number_of_pages = input("Please provide a valid number: ")

        is_volume = input("Is it a part of book series? Y/N: ")
        if is_volume == "":
            return False
        else:
            while is_volume.upper() != "Y" and is_volume.upper() != "N":
                is_volume = input("Y/N: ")
            if is_volume.upper() == "N":
                volume = None
                volume_name = None
            else:
                volume = input("Enter the volume number: ")
                if volume == "":
                    return False
                else:
                    while not volume.isdigit() or int(volume) == 0:
                        volume = input("Please enter a valid number: ")

                volume_name = input("Please provide the volume name: ")
                if volume_name == "":
                    return False

        available_status = 1
        book = f"{title},{author},{release_year},{number_of_pages},{volume},{volume_name},{available_status}\n"
        self.file.write(book)
        print("The given book added successfully.")

    def remove_book(self, title_to_remove):
        self.file.seek(0)  # to read the file from the beginning
        data = self.file.read()
        books_list = data.splitlines()
        print("--------------------------------------------------------------")
        count = lib.same_book_counter(title_to_remove)
        if int(count) == 0:
            print(f"{title_to_remove.upper()} does not exist.")
        elif int(count) == 1:
            for i, books in enumerate(books_list):
                info = books.split(',')
                if info[0].lower() == title_to_remove.lower():  # to make the matching case-insensitive
                    del books_list[i]
                    print(f"Book '{title_to_remove}' removed successfully.")
                    break
        else:
            id_list = []
            for i, books in enumerate(books_list):
                info = books.split(",")
                if info[0].upper() == title_to_remove.upper():
                    id_list.append(i)
                    print(f"Author: {info[1]} -> Book: {info[0]} -> ID:{i}")
                    print("----------------------------------------------------------------")
            id_input = input("Please enter the ID of the book you want to remove: ")
            while not id_input.isdigit():
                id_input = input("Please enter a correct ID: ")
            while int(id_input) not in id_list:
                id_input = input("Please enter a correct ID: ")
            for i, books in enumerate(books_list):
                if i == int(id_input):
                    del books_list[i]
                    print(f"Book '{title_to_remove}' with {id_input} removed successfully.")
                    break

        self.file.seek(0)  # to go back to the start before the cleaning
        self.file.truncate()  # to clear the content of the text

        for books in books_list:
            self.file.write(books + '\n')

    def counter_by_author(self, author_name):
        self.file.seek(0)
        data = self.file.read()
        books_list = data.splitlines()
        counter = 0

        for books in books_list:
            info = books.split(",")
            if len(info) >= 2 and info[1].lower() == author_name.lower():
                counter += 1
        if counter == 0:
            print(f"There is no book written by {author_name}")
        elif counter == 1:
            print(f"There is {counter} book written by {author_name}")
        else:
            print(f"There are {counter} books written by {author_name}")

    def same_book_counter(self, book_name):
        self.file.seek(0)
        data = self.file.read()
        books_list = data.splitlines()
        counter = 0

        for books in books_list:
            info = books.split(",")
            if info[0].lower() == book_name.lower():
                counter += 1
        return counter

    def total_number(self):
        self.file.seek(0)
        data = self.file.read()
        books_list = data.splitlines()
        if len(books_list) == 0:
            print("There is no book in the list.")
        elif len(books_list) == 1:
            print("There is only 1 book in the list.")
        else:
            print(f"There are {len(books_list)} books in the list.")

    def all_books(self, book_author):
        self.file.seek(0)
        data = self.file.read()
        books_list = data.splitlines()
        print(f"All books of {book_author}:")
        i = 1
        for books in books_list:
            info = books.split(",")
            if len(info) >= 2 and info[1].lower() == book_author.lower():
                if info[4] == "None":
                    print(f"{i}: {info[0]}")
                else:
                    print(f"{i}: {info[0]}, {info[5]}:{info[4]}")
                i += 1

    def available_status(self, book):
        self.file.seek(0)
        data = self.file.read()
        books_list = data.splitlines()
        print("----------------------------------------------------------------")
        lib.same_book_counter(book)
        print("----------------------------------------------------------------")
        for i, books in enumerate(books_list):
            info = books.split(",")
            if info[0].upper() == book.upper():
                print(f"Author: {info[1]} -> Book: {info[0]} -> ID:{i}")
                print("----------------------------------------------------------------")

        for i, books in enumerate(books_list):
            info = books.split(",")
            if info[0].upper() == book.upper():
                if info[6] == "1":
                    print(f"'{book.upper()}' with ID: {i} is available.")
                else:
                    print(f"'{book.upper()}' with ID: {i} is currently unavailable.")
                print("----------------------------------------------------------------")

    def borrow(self, book):
        self.file.seek(0)
        data = self.file.read()
        books_list = data.splitlines()
        id_list = []
        for i, books in enumerate(books_list):
            info = books.split(",")
            if info[0].upper() == book.upper():
                if info[6] == "1":
                    print("----------------------------------------------------------------")
                    print("Here is the available book list: ")
                    print(f"Author: {info[1]} -> Book: {info[0]} -> ID:{i}")
                    print("----------------------------------------------------------------")
                    id_list.append(i)
        if len(id_list) == 0:
            print("There is no book available!")
            return False

        id_input = input("Please enter the ID of the book you want to borrow: ")
        if id_input == "":
            return False
        else:
            while not id_input.isdigit():
                id_input = input("Please enter a correct ID: ")
            while int(id_input) >= len(books_list):
                id_input = input("Please enter a valid ID: ")

        id_input = int(id_input)

        while id_input not in id_list:
            id_input = input("Error! Please enter an ID from the list: ")
            id_input = int(id_input)

        info = books_list[id_input].split(",")
        info[6] = "0"
        books_list[id_input] = ",".join(info)

        self.file.seek(0)
        self.file.truncate()
        for books in books_list:
            self.file.write(books + "\n")
        
        print("Your request has been completed.")
        print("Returning back to the menu...")

    def returning(self, book):
        self.file.seek(0)
        data = self.file.read()
        books_list = data.splitlines()
        id_list = []
        for i, books in enumerate(books_list):
            info = books.split(",")
            if info[0].upper() == book.upper():
                id_list.append(i)
        for i, books in enumerate(books_list):
            info = books.split(",")
            if info[0].upper() == book.upper():
                if info[6] == "0":
                    print("Here is the available book list: ")
                    print(f"Author: {info[1]} -> Book: {info[0]} -> ID:{i}")
                    print("----------------------------------------------------------------")
                else:
                    if i == id_list[-1]:
                        print(f"Error! There is no book '{book.upper()}' to be delivered.")
                        return None
        id_input = input("Please enter the ID of the book you want to deliver: ")
        if id_input == "":
            return False
        else:
            while not id_input.isdigit():
                id_input = input("Please enter a correct ID: ")
            while int(id_input) >= len(books_list):
                id_input = input("Please enter a valid ID: ")

        id_input = int(id_input)

        while id_input not in id_list:
            id_input = input("Error! Please enter an ID from the list: ")
            id_input = int(id_input)

        info = books_list[id_input].split(",")
        info[6] = "1"
        books_list[id_input] = ",".join(info)

        self.file.seek(0)
        self.file.truncate()
        for books in books_list:
            self.file.write(books + "\n")

        print("Your request has been completed.")
        print("Returning back to the menu...")


lib = Library()
isTrue = True

while isTrue:
    user_choice = input("""\n*** MENU***
    1) List Books
    2) Add Book
    3) Remove Book
    4) How many...
        a) books are there written by author...: 
        b) books are there named...:
        c) books are there in total?
    5) List all books of...:
    6) Available Status Query:
    7) Borrow book:
    8) Return book:
    q) Exit\n""")

    if user_choice == "1":
        lib.list_books()
        answer = input("\nDo you want to go back to the menu? Y/N: ")
        while answer.upper() != "Y" and answer.upper() != "N":
            answer = input("You did not make a valid choice. Please enter Y or N: ")
        if answer.upper() == "N":
            print("Terminating...")
            break
        else:
            print("Returning to the menu...")
            continue

    elif user_choice == "2":
        if not lib.add_book():
            continue
        else:
            answer = input("\nDo you want to go back to the menu? Y/N: ")
            while answer.upper() != "Y" and answer.upper() != "N":
                answer = input("You did not make a valid choice. Please enter Y or N: ")
            if answer.upper() == "N":
                print("Terminating...")
                break
            else:
                print("Returning to the menu...")
                continue

    elif user_choice == "3":
        book_to_remove = input("Enter the title of the book to remove: ")
        if book_to_remove == "":
            continue
        lib.remove_book(book_to_remove)
        answer = input("\nDo you want to go back to the menu? Y/N: ")
        while answer.upper() != "Y" and answer.upper() != "N":
            answer = input("You did not make a valid choice. Please enter Y or N: ")
        if answer.upper() == "N":
            print("Terminating...")
            break
        else:
            print("Returning to the menu...")
            continue

    elif user_choice == "4":
        sub_choice = input("Please make your sub choice: ")
        while sub_choice.lower() not in ['a', 'b', 'c']:
            sub_choice = input("Please make a valid choice: ")

        if sub_choice.lower() == "a":
            full_name = input("Please provide the full name of the author: ")
            while full_name == "":
                full_name = input("Please provide the full name of the author: ")
            lib.counter_by_author(full_name)
            answer = input("\nDo you want to go back to the menu? Y/N: ")
            while answer.upper() != "Y" and answer.upper() != "N":
                answer = input("You did not make a valid choice. Please enter Y or N: ")
            if answer.upper() == "N":
                print("Terminating...")
                break
            else:
                print("Returning to the menu...")
                continue

        elif sub_choice.lower() == "b":
            name_of_book = input("Please provide the name of the book: ")
            while name_of_book == "":
                name_of_book = input("Please provide the name of the book: ")
            num = lib.same_book_counter(name_of_book)
            if num == 0:
                print(f"There is no book named '{name_of_book.upper()}'")
            elif num == 1:
                print(f"There is {num} book named '{name_of_book.upper()}'")
            else:
                print(f"There are {num} books named '{name_of_book.upper()}'")
            answer = input("\nDo you want to go back to the menu? Y/N: ")
            while answer.upper() != "Y" and answer.upper() != "N":
                answer = input("You did not make a valid choice. Please enter Y or N: ")
            if answer.upper() == "N":
                print("Terminating...")
                break
            else:
                print("Returning to the menu...")
                continue

        elif sub_choice.lower() == "c":
            lib.total_number()
            answer = input("\nDo you want to go back to the menu? Y/N: ")
            while answer.upper() != "Y" and answer.upper() != "N":
                answer = input("You did not make a valid choice. Please enter Y or N: ")
            if answer.upper() == "N":
                print("Terminating...")
                break
            else:
                print("Returning to the menu...")
                continue

        else:
            print("Error! Please make a valid choice.")

    elif user_choice.lower() == "q":
        print("Terminating...")
        break

    elif user_choice == "5":
        name = input("\nPlease provide the full name of the author: ")
        while name == "":
            name = input("Please provide the full name of the author: ")
        lib.all_books(name)
        answer = input("\nDo you want to go back to the menu? Y/N: ")
        while answer.upper() != "Y" and answer.upper() != "N":
            answer = input("You did not make a valid choice. Please enter Y or N: ")
        if answer.upper() == "N":
            print("Terminating...")
            break
        else:
            print("Returning to the menu...")
            continue

    elif user_choice == "6":
        name = input("\nPlease provide the name of the book: ")
        while name == "":
            name = input("Please provide the name of the book: ")
        lib.available_status(name)
        answer = input("\nDo you want to go back to the menu? Y/N: ")
        while answer.upper() != "Y" and answer.upper() != "N":
            answer = input("You did not make a valid choice. Please enter Y or N: ")
        if answer.upper() == "N":
            print("Terminating...")
            break
        else:
            print("Returning to the menu...")
            continue

    elif user_choice == "7":
        name = input("\nPlease provide the name of the book\nor press Enter to get back to the menu: ")
        if name == "":
            continue
        else:
            while name.upper() not in lib.books():
                name = input(f"There is no book '{name}'. Please enter a valid one: ")
        lib.borrow(name)
        answer = input("\nDo you want to go back to the menu? Y/N: ")
        while answer.upper() != "Y" and answer.upper() != "N":
            answer = input("You did not make a valid choice. Please enter Y or N: ")
        if answer.upper() == "N":
            print("Terminating...")
            break
        else:
            print("Returning to the menu...")
            continue

    elif user_choice == "8":
        name = input("\nPlease provide the name of the book\nor press Enter to get back to the menu: ")
        if name == "":
            continue
        else:
            while name.upper() not in lib.books():
                name = input(f"There is no book '{name}'. Please enter a valid one: ")
            lib.returning(name)
            answer = input("\nDo you want to go back to the menu? Y/N: ")
            while answer.upper() != "Y" and answer.upper() != "N":
                answer = input("You did not make a valid choice. Please enter Y or N: ")
            if answer.upper() == "N":
                print("Terminating...")
                break
            else:
                print("Returning to the menu...")
                continue

    else:
        print("Error! Please enter a valid input!")
