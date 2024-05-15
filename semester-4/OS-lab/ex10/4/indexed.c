#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_RECORDS 3
#define INDEX_SIZE 3

struct Record {
    int id;
    char name[30];
};

struct Index {
    int id;
    long position;
};

void create_indexed_file() {
    FILE *file = fopen("indexed_alloc.dat", "wb");
    FILE *index_file = fopen("index.dat", "wb");
    
    struct Record records[] = {
        {1, "Alice"},
        {2, "Bob"},
        {3, "Charlie"}
    };
    struct Index indexes[MAX_RECORDS];

    for (int i = 0; i < MAX_RECORDS; i++) {
        indexes[i].id = records[i].id;
        indexes[i].position = i * sizeof(struct Record);
        fwrite(&records[i], sizeof(struct Record), 1, file);
    }
    
    fwrite(indexes, sizeof(struct Index), INDEX_SIZE, index_file);
    
    fclose(file);
    fclose(index_file);
}

void read_indexed_file(int id) {
    FILE *file = fopen("indexed_alloc.dat", "rb");
    FILE *index_file = fopen("index.dat", "rb");

    struct Index indexes[INDEX_SIZE];
    fread(indexes, sizeof(struct Index), INDEX_SIZE, index_file);
    
    for (int i = 0; i < INDEX_SIZE; i++) {
        if (indexes[i].id == id) {
            struct Record record;
            fseek(file, indexes[i].position, SEEK_SET);
            fread(&record, sizeof(struct Record), 1, file);
            printf("ID: %d, Name: %s\n", record.id, record.name);
            fclose(file);
            fclose(index_file);
            return;
        }
    }
    printf("Record not found.\n");
    fclose(file);
    fclose(index_file);
}

int main() {
    create_indexed_file();
    printf("Indexed File Allocation Contents for ID 2:\n");
    read_indexed_file(2);
    return 0;
}
