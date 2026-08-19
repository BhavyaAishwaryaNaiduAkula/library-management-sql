-- ============================================
-- LIBRARY MANAGEMENT SYSTEM
-- ============================================

-- 1. Create Database
CREATE DATABASE library_management;

USE library_management;


-- 2. Create Books Table
CREATE TABLE books (
    book_id INT PRIMARY KEY,
    book_name VARCHAR(100),
    author VARCHAR(100),
    available BOOLEAN DEFAULT TRUE
);


-- 3. Create Members Table
CREATE TABLE members (
    member_id INT PRIMARY KEY,
    member_name VARCHAR(100),
    email VARCHAR(100)
);


-- 4. Create Issued Books Table
CREATE TABLE issued_books (
    issue_id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT,
    member_id INT,
    issue_date DATE,
    return_date DATE,
    FOREIGN KEY (book_id) REFERENCES books(book_id),
    FOREIGN KEY (member_id) REFERENCES members(member_id)
);


-- 5. Insert Books
INSERT INTO books (book_id, book_name, author)
VALUES
(1, 'Python Basics', 'John Smith'),
(2, 'SQL Fundamentals', 'David Lee'),
(3, 'Data Science', 'Robert Brown'),
(4, 'Web Development', 'James Wilson'),
(5, 'Machine Learning', 'Andrew Ng');


-- 6. Insert Members
INSERT INTO members (member_id, member_name, email)
VALUES
(101, 'Bhavya', 'bhavya@gmail.com'),
(102, 'Rahul', 'rahul@gmail.com'),
(103, 'Priya', 'priya@gmail.com');


-- 7. Issue a Book
INSERT INTO issued_books (book_id, member_id, issue_date)
VALUES (1, 101, CURDATE());


-- 8. Mark Book as Unavailable
UPDATE books
SET available = FALSE
WHERE book_id = 1;


-- 9. View Issued Books
SELECT
    m.member_name,
    b.book_name,
    b.author,
    i.issue_date
FROM issued_books i
JOIN members m
ON i.member_id = m.member_id
JOIN books b
ON i.book_id = b.book_id;


-- 10. Return Book
UPDATE issued_books
SET return_date = CURDATE()
WHERE book_id = 1
AND member_id = 101
AND return_date IS NULL;


-- 11. Mark Book as Available
UPDATE books
SET available = TRUE
WHERE book_id = 1;


-- 12. Show Available Books
SELECT *
FROM books
WHERE available = TRUE;


-- 13. Search for a Book
SELECT *
FROM books
WHERE book_name LIKE '%Python%';


-- 14. Search for a Member
SELECT *
FROM members
WHERE member_name LIKE '%Bhavya%';


-- 15. Show Currently Issued Books
SELECT
    m.member_name,
    b.book_name,
    i.issue_date
FROM issued_books i
JOIN members m
ON i.member_id = m.member_id
JOIN books b
ON i.book_id = b.book_id
WHERE i.return_date IS NULL;


-- 16. Count Total Books
SELECT COUNT(*) AS total_books
FROM books;


-- 17. Count Available Books
SELECT COUNT(*) AS available_books
FROM books
WHERE available = TRUE;


-- 18. Count Issued Books
SELECT COUNT(*) AS issued_books
FROM issued_books
WHERE return_date IS NULL;


-- 19. Complete Borrowing History
SELECT
    i.issue_id,
    m.member_name,
    b.book_name,
    i.issue_date,
    i.return_date
FROM issued_books i
JOIN members m
ON i.member_id = m.member_id
JOIN books b
ON i.book_id = b.book_id
ORDER BY i.issue_date DESC;