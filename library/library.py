import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("library/library.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
book_collection = db.collection("books").get()

choice = "0"
while choice != "5":
    # Main Menu
    print("Welcome to the library!")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Change a book")
    print("4. View Books")
    print("5. Quit")
    choice = input("What would you like to do? \n> ")

    # Add Book
    if choice == "1":
        title = input("\nWhat is the book's title? ")
        author = input("Who is the author? ")
        pages = int(input("How many pages will it be? "))
        publisher = input("Who published it? ")
        language = input("What language is it in? ")

        db.collection("books").add({
            "title": title,
            "author": author,
            "page_count": pages,
            "publisher": publisher,
            "language": language
        })

        book_collection = db.collection("books").get()

    # Subtract Book
    elif choice == "2":
        for bc in book_collection:
            book = bc.to_dict()

            print(f"\"{book["title"]}\" by {book["author"]}")

        removal = input("Which book would you like to remove? (Insert Title) ")
        
        book_to_remove = db.collection("books").where("title", "==", removal).limit(1).get()

        if not book_to_remove:
            print("Book not found.")
        else:
            # Delete the book document
            db.collection("books").document(book_to_remove[0].id).delete()
            print("Book removed successfully.")

            book_collection = db.collection("books").get()

    # Change Book
    elif choice == "3":
        for bc in book_collection:
            book = bc.to_dict()
            title = book["title"]
            author = book["author"]
            print(f"\"{title}\" by {author}")

        chosen_book_title = input("Which book would you like to edit? (Insert Title) ")

        results = db.collection("books").where("title", "==", chosen_book_title).get()

        if len(results) == 1:
            chosen_book = results[0]
            chosen_book_id = chosen_book.id
            loop = True

            while loop:
                book_data = chosen_book.to_dict()
                print(f"1. Title: {book_data['title']}")
                print(f"2. Author: {book_data['author']}")
                print(f"3. Pages: {book_data.get('page_count', 'N/A')}")
                print(f"4. Language: {book_data.get('language', 'N/A')}")
                print(f"5. Publisher: {book_data.get('publisher', 'N/A')}")
                print("6. Finish Editing")

                item = input("Which part do you want to edit? ")

                if item.lower() == "title" or item == "1":
                    chosen_book_title = input("Enter new title: ")
                    db.collection("books").document(chosen_book_id).update({"title": chosen_book_title})

                elif item.lower() == "author" or item == "2":
                    new_author = input("Enter new author: ")
                    db.collection("books").document(chosen_book_id).update({"author": new_author})

                elif item.lower() == "pages" or item == "3":
                    new_pages = int(input("Enter new page count: "))
                    db.collection("books").document(chosen_book_id).update({"page_count": new_pages})

                elif item.lower() == "language" or item == "4":
                    new_language = input("Enter new language: ")
                    db.collection("books").document(chosen_book_id).update({"language": new_language})

                elif item.lower() == "publisher" or item == "5":
                    new_publisher = input("Enter new publisher: ")
                    db.collection("books").document(chosen_book_id).update({"publisher": new_publisher})

                elif item == "6":
                    loop = False

                else:
                    print("Invalid input. Please try again.")

                book_collection = db.collection("books").get()
                results = db.collection("books").where("title", "==", chosen_book_title).get()
                chosen_book = results[0]
                chosen_book_id = chosen_book.id
                
                
        else:
            print("That book does not exist.")
    

    # View Books
    elif choice == "4":
        for bc in book_collection:
            book = bc.to_dict()
            title = book["title"]
            author = book["author"]
            print(f"\"{title}\" by {author}")

        input("\nPress enter to continue")