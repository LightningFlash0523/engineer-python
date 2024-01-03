DATABASE COMMAND-LINE INTERFACE
Overview
This is a simple in-memory database system with a command-line interface implemented in Python. The database supports basic operations such as SET, GET, DELETE, COUNT, and transactions (BEGIN, ROLLBACK, COMMIT). This README provides instructions on running the program and understanding its functionality.

USAGE

Prerequisites
Python installed on your machine (version 3.x recommended)


Running the Program
Save the code in a file, for example, database.py.
Open a terminal or command prompt.
Navigate to the directory where database.py is saved.
Run the program using the command:
python database.py


Command-Line Interface

SET [name] [value]: Sets the value associated with the given name in the database.
GET [name]: Retrieves and prints the value for the specified name. If the name is not in the database, it prints "NULL."
DELETE [name]: Deletes the value associated with the specified name from the database.
COUNT [value]: Returns the count of names that have the given value assigned to them. If the value is not assigned to any name, it prints "0."
BEGIN: Starts a new transaction.
ROLLBACK: Rolls back the most recent transaction. If there is no transaction to rollback, it prints "TRANSACTION NOT FOUND."
COMMIT: Commits all open transactions and makes changes permanent.
END: Exits the database.
Type END to exit the program.


EXAMPLE:
Enter command: SET name Michael
Enter command: GET name
Michael
Enter command: DELETE name
Enter command: GET name
NULL
Enter command: COUNT Michael
0
Enter command: BEGIN
Enter command: SET name Michelle
Enter command: GET name
Michelle
Enter command: ROLLBACK
Enter command: GET name
NULL
Enter command: COMMIT
Enter command: GET name
Michelle
Enter command: END


NOTES:
The database operates in-memory and does not persist data between program runs.
Ensure that Python is in your system's PATH to run the program from any directory.