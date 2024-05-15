#include <stdio.h>
#include <string.h>
struct Record {
    int id;
    char name[30];
};
void create_sequential_file() {
    FILE *file = fopen("sequential.dat", "wb");
    struct Record records[] = {
        {1, "Alice"},
        {2, "Bob"},
        {3, "Charlie"}
    };
    fwrite(records, sizeof(struct Record), 3, file);
    fclose(file);
}
void read_sequential_file() {
    FILE *file = fopen("sequential.dat", "rb");
    struct Record record;
    while (fread(&record, sizeof(struct Record), 1, file)) {
        printf("ID: %d, Name: %s\n", record.id, record.name);
    }
    fclose(file);
}
int main() {
    create_sequential_file();
    printf("Sequential File Contents:\n");
    read_sequential_file();
    return 0;
}
