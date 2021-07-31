#include <ESP8266WiFi.h>
#include <WiFiUdp.h>
#include <Servo.h>

Servo motor;

char ssid[] = "name"; 
char pass[] = "pass";    

unsigned int localPort = 2390;

char recievedMessage[255]; 
char  ReplyBuffer[] = "acknowledged";      
String decoded;
char  ReplyBuffer[] = "door opened"; 
int PacketSize;

void setup() {
  Serial.begin(9600);
  WiFi.begin(ssid);
  delay(1000);
  Udp.begin(localPort);
  motor.attach(2)
}

void loop() {
  PacketSize = udp.parsePacket();
  if(PacketSize){
    int len = udp.read(packetBuffer, receivePacketSize);
        if (len > 0) {
            packetBuffer[len] = 0;}
    }
    Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());
    Udp.write(ReplyBuffer);
    Udp.endPacket();
    
    Serial.println(packetBuffer);
    delay(5000);
    decoded = Serial.readStringUntil("\n")
    if(decoded=="YES"){
          for(pos=180;pos>=0;pos-=1){
            motor.write(pos)
            delay(5)}
          Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());
          Udp.write(ReplyBuffer2);
          Udp.endPacket();
      }
    PacketSize = 0;
    Upd.flush();
}
