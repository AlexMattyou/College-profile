#include <stdio.h>
#include <string.h>

struct Record {
    int id;
    char name[30];
};
void create_indexed_file() {
    FILE *file = fopen("indexed.dat", "wb");
    struct Record records[] = {
        {1, "Alice"},
        {2, "Bob"},
        {3, "Charlie"}
    };
    fwrite(records, sizeof(struct Record), 3, file);
    fclose(file);
}
void read_indexed_file(int id) {
    FILE *file = fopen("indexed.dat", "rb");
    struct Record record;
    while (fread(&record, sizeof(struct Record), 1, file)) {
        if (record.id == id) {
            printf("ID: %d, Name: %s\n", record.id, record.name);
            fclose(file);
            return;
        }
    }
    printf("Record not found.\n");
    fclose(file);
}
int main() {
    create_indexed_file();
    printf("Read record with ID 2:\n");
    read_indexed_file(2);
    return 0;
}
