SEQUENTIAL FILE ORGANIZATION:
Create File: Write a fixed sequence of records to a binary file.
Read File: Read and print records sequentially from the file.
Sequential Access: All records are accessed in the order they were written.

INDEXED FILE ORGANIZATION:
Create File: Write a sequence of records to a binary file.
Indexed Access: Read file sequentially, comparing IDs until the desired record is found.
Direct Access: Search for a specific record using its index.

LINKED FILE ORGANIZATION:
Create File: Write records to a binary file with each record containing a pointer to the next record.
Read File: Start from the first record and follow the pointers to access subsequent records.
Linked Access: Records are linked through pointers, enabling sequential traversal.