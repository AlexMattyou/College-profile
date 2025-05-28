#include <REG51.H>

unsigned char arr[5] = {0x30, 0x10, 0x50, 0x20, 0x40};
unsigned char i, j, temp;

void main() {
    // Sorting in Descending Order
    for(i = 0; i < 4; i++) {
        for(j = i + 1; j < 5; j++) {
            if (arr[i] < arr[j]) {  // Swap if the current element is smaller
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }

    P2 = arr[0];  // Largest element
    P3 = arr[4];  // Smallest element

    while(1);
}
