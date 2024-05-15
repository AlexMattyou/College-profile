#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_RECORDS 3
struct Record {
    int id;
    char name[30];
    int next;
};
void create_linked_file() {
    FILE *file = fopen("linked_alloc.dat", "wb");
    struct Record records[] = {
        {1, "Alice", 1},
        {2, "Bob", 2},
        {3, "Charlie", -1}
    };
    fwrite(records, sizeof(struct Record), MAX_RECORDS, file);
    fclose(file);
}
void read_linked_file() {
    FILE *file = fopen("linked_alloc.dat", "rb");
    struct Record record;
    int index = 0;
    while (index != -1) {
        fseek(file, index * sizeof(struct Record), SEEK_SET);
        fread(&record, sizeof(struct Record), 1, file);
        printf("ID: %d, Name: %s\n", record.id, record.name);
        index = record.next;
    }
    fclose(file);
}
int main() {
    create_linked_file();
    printf("Linked File Allocation Contents:\n");
    read_linked_file();
    return 0;
}
