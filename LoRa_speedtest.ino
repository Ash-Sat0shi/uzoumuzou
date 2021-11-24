#include "Arduino.h"
#include <SoftwareSerial.h>
uint32_t serialTime;
 
SoftwareSerial E22serial(5, 4);
 
void setup() {
  
}
 
void loop() {
  E22serial.begin(9600);
serialTime = micros();
  E22serial.println("Time:");
  for (int i = 1 ; i <= 64 ; i++){
  E22serial.print(i);
  E22serial.print("\t");
    if((i % 8) == 0 ){
      E22serial.print("\r\n");
    }
  }
  E22serial.print("\r\n");
  E22serial.println(micros() - serialTime);
  E22serial.println("\r\n");
  E22serial.end();
  delay(1000);
}
