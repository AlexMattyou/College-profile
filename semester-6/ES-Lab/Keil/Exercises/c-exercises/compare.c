#include <REG51.H>

unsigned char a, b;

void main() {
    a = P1;  // Read input from Port 1
    b = P2;  // Read input from Port 2

    if (a > b) {
        P0 = 0x01;  // a is greater → P0 = 1
    }  
    else if (a < b) {
        P0 = 0x02;  // b is greater → P0 = 2
    }  
    else {
        P0 = 0x00;  // Equal → P0 = 0
    }

    while(1);
}
