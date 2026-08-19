# Library Management System

## About the Project

I created this project using **MySQL and SQL queries** as part of my internship learning.

The main purpose of this project is to manage books, members, and the process of issuing and returning books in a library.

## What I Created

The project has three tables:

### Books Table

This table stores the details of books in the library.

* Book ID
* Book Name
* Author
* Availability

### Members Table

This table stores the details of library members.

* Member ID
* Member Name
* Email

### Issued Books Table

This table keeps track of which member has taken which book.

* Issue ID
* Book ID
* Member ID
* Issue Date
* Return Date

## Features

Using SQL queries, I implemented:

* Adding books
* Adding members
* Issuing a book
* Returning a book
* Checking available books
* Searching for books
* Searching for members
* Viewing currently issued books
* Viewing borrowing history
* Counting total and available books

## SQL Concepts I Used

While making this project, I practiced:

* Creating a database
* Creating tables
* `INSERT`
* `SELECT`
* `UPDATE`
* `WHERE`
* `LIKE`
* `JOIN`
* `COUNT()`
* `ORDER BY`
* Primary Key
* Foreign Key
* Default values

## Tools Used

* MySQL
* SQL
* Visual Studio Code

## Project Files

```text
Library Management Sql/
── library.sql
── Readme.md
```

## What I Learned

While working on this project, I learned how to create and manage a database using SQL. I also learned how tables can be connected using foreign keys and how `JOIN` can be used to get information from multiple tables.

This project helped me understand SQL better by actually using the queries in a small real-world example.
