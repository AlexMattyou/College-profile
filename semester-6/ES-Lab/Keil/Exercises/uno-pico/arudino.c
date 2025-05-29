#include <SoftwareSerial.h>
SoftwareSerial mySerial(2, 3); // RX, TX

void setup() {
  mySerial.begin(9600);
}

void loop() {
  mySerial.write('A');
  delay(1000);
  mySerial.write('B');
  delay(1000);
}