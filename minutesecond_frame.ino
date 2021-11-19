#include <RTClib.h>
#include <Wire.h>
#include <U8g2lib.h>

char s[8];
//char t[32];
RTC_DS3231 RTC;
U8G2_SSD1306_128X32_UNIVISION_F_HW_I2C u8g2(U8G2_R0, /* reset=*/ U8X8_PIN_NONE); //STM32F103C8T6(BlackPill) and DSDtech I2C

void setup() {
  Serial.begin(9600);
  Wire.begin();
  RTC.begin();
  u8g2.begin();
  /*RTC.adjust(DateTime(F(__DATE__),F(__TIME__)));
    rtc.adjust(DateTime(2020, 5, 14, 9, 27, 0));
    to set time on boot
  */
  #define timestr " DATE  TIME"
}

void loop() {
//this part for display nowtime on serialmonitor
  DateTime now = RTC.now();
  //sprintf(t, " %02d/%02d %02d:%02d:%02d",  now.month(), now.day(), now.hour(), now.minute(), now.second());
   
  Serial.print(F("Date/Time: "));
  //Serial.println(t);
  
//this part for display nowtime on LCD
  sprintf(s, "  %02d:%02d",  now.minute(), now.second()); 
  u8g2.clearBuffer();                   // clear the internal memory
  u8g2.setFont(u8g2_font_profont29_mn);  // choose a suitable font  u8g2_font_8x13_tf
  u8g2.drawFrame(0,1,128,31);
  u8g2.drawStr(1,25,s); // write time
  u8g2.sendBuffer();
  delay(100);
  u8g2.clearBuffer();
  u8g2.drawFrame(0,1,128,31);
  sprintf(s, "  %02d %02d",  now.minute(), now.second());
  u8g2.drawStr(1,25,s); // write time
  u8g2.sendBuffer();
  delay(100);
}
