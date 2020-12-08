#include <RTClib.h>
#include <Wire.h>
#include <U8g2lib.h>
#include <ESP8266WiFi.h>
#include <time.h>
#define WIFI_SSID   "S-Kitting"
#define WIFI_PASSWORD   "asdf7890"
#define JST     3600*9

char a[32];
char b[32];
char c[24];
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

  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  while(WiFi.status() != WL_CONNECTED) {
    Serial.print('.');
    delay(500);
  }
  Serial.println();
  Serial.printf("Connected, IP address: ");
  Serial.println(WiFi.localIP());
  configTzTime("JST-9", "time.google.com", "ntp.nict.jp");
}

void loop() {
  time_t t;
  struct tm *tm;
  t = time(NULL);
  tm = localtime(&t);
  sprintf(c, "%04d,%02d,%02d,%02d,%02d,%02d", tm->tm_year+1900, tm->tm_mon+1, tm->tm_mday, tm->tm_hour, tm->tm_min, tm->tm_sec);
  Serial.println(c);
  RTC.adjust(DateTime(tm->tm_year+1900, tm->tm_mon+1, tm->tm_mday, tm->tm_hour, tm->tm_min, tm->tm_sec));
//this part for display nowtime on serialmonitor
  DateTime now = RTC.now();
  sprintf(a, " %02d/%02d",  now.month(), now.day());
  sprintf(b, " %02d:%02d:%02d",  now.hour(), now.minute(), now.second()); 
   
  Serial.print(F("Date: "));
  Serial.println(a);
  Serial.print(F("Time: "));
  Serial.println(b);

//  time_t t;
//  struct tm *tm;
//  t = time(NULL);
//  tm = localtime(&t);
//  Serial.printf("Date Time :  %04d/%02d/%02d %02d:%02d:%02d\n",
//        tm->tm_year+1900, tm->tm_mon+1, tm->tm_mday,
//        tm->tm_hour, tm->tm_min, tm->tm_sec);

//  sprintf(a, "DATE:%02d/%02d", tm->tm_mon+1, tm->tm_mday); 
//  sprintf(b, "TIME %02d:%02d:%02d", tm->tm_hour, tm->tm_min, tm->tm_sec); 
//this part for display nowtime on LCD
  u8g2.clearBuffer();                   // clear the internal memory
  u8g2.setFont(u8g2_font_8x13_tf);  // choose a suitable font  u8g2_font_8x13_tf u8g2_font_fur30_tf
  u8g2.drawStr(1,15,a); // write date
  u8g2.drawStr(1,31,b); // write time
  u8g2.sendBuffer();
  delay(1000);
}
