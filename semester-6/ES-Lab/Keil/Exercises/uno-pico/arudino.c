Okay, let's break down the Arduino and Raspberry Pi Pico codes provided for your Bluetooth communication experiment, following the clear structure you liked.

✅ Experiment 9: Communicate Between Arduino and Raspberry Pi (via Bluetooth) Explanation
🎯 Aim:

To send data wirelessly from Arduino to Raspberry Pi Pico using Bluetooth (HC-05).

🔌 Connections:

🔷 HC-05 to Arduino

HC-05 Pin	Arduino Pin	Notes
VCC	5V	Power supply for the HC-05 module.
GND	GND	Ground connection.
TXD	Pin 2	Transmit pin of HC-05 connected to RX pin of Arduino.
RXD	Pin 3	Receive pin of HC-05 connected to TX pin of Arduino through a voltage divider (important because HC-05 TX is 3.3V and Arduino RX is 5V tolerant, but it's good practice to level shift).

Export to Sheets
🔶 HC-05 to Raspberry Pi Pico

HC-05 Pin	Pico Pin (GPIO)	Notes
VCC	3.3V	Power supply for the HC-05 module.
GND	GND	Ground connection.
TXD	GP1 (Pin 2)	Transmit pin of HC-05 connected to RX pin of Pico.
RXD	GP0 (Pin 1)	Receive pin of HC-05 connected to TX pin of Pico.

Export to Sheets
💻 Code

🟦 Arduino Code

C++

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