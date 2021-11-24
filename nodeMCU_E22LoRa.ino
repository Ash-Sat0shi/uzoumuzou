#include "Arduino.h"
#include <SoftwareSerial.h>
 
SoftwareSerial E22serial(5, 4);
 
void setup() {
  Serial.begin(9600);
  delay(500);
 
  Serial.println("Hi, I'm going to send message!");
 
  E22serial.begin(9600);
  E22serial.println("  HELLO");
  delay(50);
  E22serial.println("  WORLD");
}
 
void loop() {
  if (E22serial.available()) {
    Serial.write(E22serial.read());
  }
  if (Serial.available()) {
    E22serial.write(Serial.read());
  }
  E22serial.println("  HELLO WORLD");
}
