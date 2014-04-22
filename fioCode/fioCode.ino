#include <WiFi.h>
#include <WiFiUdp.h>
#include <SPI.h>

//SSID of your network 
char ssid[] = "thisIsMyMob";
//password of your WPA Network 
char pass[] = "whatwhat22";
WiFiUDP Udp;

void setup()
{

  WiFi.begin(ssid, pass);
  Udp.begin(7797);


}

void loop () {
  delay(1000);
  long rssi = WiFi.RSSI();
//  Udp.beginPacket(0x45000034e10d400620e9c0a82b1f6011ecf4, 7787);
  Udp.beginPacket(343434343, 7787);
  Udp.write(rssi);
  Udp.endPacket();
}


