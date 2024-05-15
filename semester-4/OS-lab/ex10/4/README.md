SEQUENTIAL FILE ALLOCATION:
Create File: Write a fixed sequence of records to a binary file.
Read File: Read and print records sequentially from the file.
Sequential Access: All records are accessed in the order they were written.

INDEXED FILE ALLOCATION:
Create File and Index: Write records to a binary file and create an index file storing record IDs and their positions.
Read File: Use the index to find the position of a specific record and read it from the file.
Indexed Access: Access records directly using the index file.

LINKED FILE ALLOCATION:
Create File: Write records to a binary file, each containing a pointer to the next record.
Read File: Start from the first record and follow the pointers to access subsequent records.
Linked Access: Records are linked through pointers, enabling sequential traversal.