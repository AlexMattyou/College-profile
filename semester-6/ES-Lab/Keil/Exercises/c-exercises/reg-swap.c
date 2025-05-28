#include <REG51.H>

unsigned char temp;

void main() {
    ACC = 0x25;  // Load 0x25 into Accumulator (Register A)
    B = 0x10;    // Load 0x10 into Register B

    // Swapping the values
    temp = ACC;
    ACC = B;
    B = temp;

    // Output the swapped values
    P0 = ACC;  // Will show 0x10
    P1 = B;    // Will show 0x25

    while(1);
}
