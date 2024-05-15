#include <stdio.h>
#include <string.h>

#define MAX_RECORDS 3

struct Record {
    int id;
    char name[30];
};

void create_sequential_file() {
    FILE *file = fopen("sequential_alloc.dat", "wb");
    struct Record records[] = {
        {1, "Alice"},
        {2, "Bob"},
        {3, "Charlie"}
    };
    fwrite(records, sizeof(struct Record), MAX_RECORDS, file);
    fclose(file);
}

void read_sequential_file() {
    FILE *file = fopen("sequential_alloc.dat", "rb");
    struct Record record;
    while (fread(&record, sizeof(struct Record), 1, file)) {
        printf("ID: %d, Name: %s\n", record.id, record.name);
    }
    fclose(file);
}

int main() {
    create_sequential_file();
    printf("Sequential File Allocation Contents:\n");
    read_sequential_file();
    return 0;
}

