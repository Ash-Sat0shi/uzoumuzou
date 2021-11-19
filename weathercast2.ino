#include <RTClib.h>
#include <Wire.h>
#include <U8g2lib.h>
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <ArduinoJson.h>
#include <time.h>
#define WIFI_SSID   "S-Kitting"
#define WIFI_PASSWORD   "asdf7890"
#define JST     3600*9

RTC_DS3231 RTC;
U8G2_SSD1306_128X32_UNIVISION_F_HW_I2C u8g2(U8G2_R0, /* reset=*/ U8X8_PIN_NONE); //DSDtech I2C

const String endpoint = "http://api.openweathermap.org/data/2.5/weather?q=chiba,jp&units=metric&APPID=";
const String forecast = "http://api.openweathermap.org/data/2.5/forecast?q=chiba,jp&units=metric&cnt=5&appid=";
const String key = "8ddf1636b91a1f919b29d8b49f644f2e";

void setup() {
  Serial.begin(9600);
  Wire.begin();
  RTC.begin();
  u8g2.begin();
    
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
  if ((WiFi.status() == WL_CONNECTED)) {
   HTTPClient http;
   http.begin(endpoint + key); 
   int httpCode = http.GET();
   if (httpCode > 0) {
     String payload = http.getString();
     Serial.println(payload);
     DynamicJsonBuffer jsonBuffer;
     String json = payload;
     JsonObject& weatherdata = jsonBuffer.parseObject(json);
     const char* weather = weatherdata["weather"][0]["main"].as<char*>();
     const char* description = weatherdata["weather"][0]["description"].as<char*>();
     const double temp = weatherdata["main"]["temp"].as<double>();
     //const double pressure = weatherdata["main"]["pressure"].as<double>();
     const char* pressure = weatherdata["main"]["pressure"].as<char*>();
     const double humidity = weatherdata["main"]["humidity"].as<double>();
     const char hpa[16] = "hPa [NOW]";
       
       /* ----------------------------------------------------------------------------------- */
       http.setTimeout(9999999999);
       http.begin(forecast + key);
       int httpCode = http.GET();
            if (httpCode > 0) {
                String forecastpayload = http.getString();
                Serial.println(forecastpayload);
                DynamicJsonBuffer jsonBuffer;
                String json = forecastpayload;
                JsonObject& forecastdata = jsonBuffer.parseObject(json);
                const char* forecastweather = forecastdata["list"][4]["weather"][0]["main"].as<char*>();
                const char* forecastdescription = forecastdata["list"][4]["weather"][0]["description"].as<char*>();
                const double forecasttemp = forecastdata["list"][4]["main"]["temp"].as<double>();
                const char* forecastpressure = forecastdata["list"][4]["main"]["pressure"].as<char*>();
                const double forecasthumidity = forecastdata["list"][4]["main"]["humidity"].as<double>();
                const char fhpa[17] = "hPa [21PM]";
   
    u8g2.clearBuffer(); // clear the internal memory
    u8g2.setFont(u8g2_font_8x13_tf); // choose a suitable font
    u8g2.drawStr(1,15,description); // write weather
    u8g2.drawStr(1,31,pressure); // write air pressure
    u8g2.drawStr(35,31,hpa);
    u8g2.sendBuffer();
    delay(5000);
        u8g2.clearBuffer(); // clear the internal memory
        u8g2.setFont(u8g2_font_8x13_tf); // choose a suitable font
        u8g2.drawStr(1,15,forecastdescription); // write weather
        u8g2.drawStr(1,31,forecastpressure); // write air pressure
        u8g2.drawStr(35,31,fhpa);
        u8g2.sendBuffer();
        delay(5000);
/* ----------------------------------------------------------------------------------- */
        u8g2.clearBuffer(); // clear the internal memory
    u8g2.setFont(u8g2_font_8x13_tf); // choose a suitable font
    u8g2.drawStr(1,15,description); // write weather
    u8g2.drawStr(1,31,pressure); // write air pressure
    u8g2.drawStr(35,31,hpa);
    u8g2.sendBuffer();
    delay(5000);
        u8g2.clearBuffer(); // clear the internal memory
        u8g2.setFont(u8g2_font_8x13_tf); // choose a suitable font
        u8g2.drawStr(1,15,forecastdescription); // write weather
        u8g2.drawStr(1,31,forecastpressure); // write air pressure
        u8g2.drawStr(35,31,fhpa);
        u8g2.sendBuffer();
        delay(5000);
    
            }
   }
    http.end(); 
   }
 //delay(10*60*1000); //10分おきに更新
}
