#include <REG51.H>

unsigned char a, b;

void main() {
    a = 0x10;  // 16
    b = 0x04;  // 4

    P0 = a + b;  // P0 = 0x14 = 20 (Addition)
    P1 = a - b;  // P1 = 0x0C = 12 (Subtraction)

    while(1);
}
