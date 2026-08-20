import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

connection = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cursor = connection.cursor()

print("Connected to MySQL successfully!")


def view_books():
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    print("\n--- Books ---")
    for book in books:
        print(book)


def view_members():
    cursor.execute("SELECT * FROM members")
    members = cursor.fetchall()

    print("\n--- Members ---")
    for member in members:
        print(member)


def view_issued_books():
    query = """
    SELECT m.member_name, b.book_name, i.issue_date, i.return_date
    FROM issued_books i
    JOIN members m ON i.member_id = m.member_id
    JOIN books b ON i.book_id = b.book_id
    """

    cursor.execute(query)
    records = cursor.fetchall()

    print("\n--- Issued Books ---")
    for record in records:
        print(record)


def add_book():
    book_id = int(input("Enter book ID: "))
    book_name = input("Enter book name: ")
    author = input("Enter author name: ")

    query = """
    INSERT INTO books (book_id, book_name, author)
    VALUES (%s, %s, %s)
    """

    cursor.execute(query, (book_id, book_name, author))
    connection.commit()

    print("Book added successfully!")

def issue_book():
    book_id = int(input("Enter book ID: "))
    member_id = int(input("Enter member ID: "))

    # Check whether the book is available
    cursor.execute(
        "SELECT available FROM books WHERE book_id = %s",
        (book_id,)
    )
    result = cursor.fetchone()

    if result is None:
        print("Book not found!")
        return

    if result[0] == 0:
        print("Book is already issued!")
        return

    # Issue the book
    cursor.execute(
        """
        INSERT INTO issued_books (book_id, member_id, issue_date)
        VALUES (%s, %s, CURDATE())
        """,
        (book_id, member_id)
    )

    # Mark book as unavailable
    cursor.execute(
        "UPDATE books SET available = FALSE WHERE book_id = %s",
        (book_id,)
    )

    connection.commit()

    print("Book issued successfully!")

def return_book():
    book_id = int(input("Enter book ID: "))
    member_id = int(input("Enter member ID: "))

    # Check if the book is currently issued
    cursor.execute(
        """
        SELECT issue_id
        FROM issued_books
        WHERE book_id = %s
        AND member_id = %s
        AND return_date IS NULL
        """,
        (book_id, member_id)
    )

    result = cursor.fetchone()

    if result is None:
        print("No active issue record found!")
        return

    # Update return date
    cursor.execute(
        """
        UPDATE issued_books
        SET return_date = CURDATE()
        WHERE issue_id = %s
        """,
        (result[0],)
    )

    # Make the book available again
    cursor.execute(
        """
        UPDATE books
        SET available = TRUE
        WHERE book_id = %s
        """,
        (book_id,)
    )

    connection.commit()

    print("Book returned successfully!")

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. View Books")
    print("2. View Members")
    print("3. View Issued Books")
    print("4. Add Book")
    print("5. Issue Book")
    print("6. Return Book")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_books()

    elif choice == "2":
        view_members()

    elif choice == "3":
        view_issued_books()

    elif choice == "4":
        add_book()

    elif choice == "5":
        issue_book()

    elif choice == "6":
        return_book()

    elif choice == "7":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")


cursor.close()
connection.close()


