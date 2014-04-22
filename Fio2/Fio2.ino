

byte packet[] = {0x7E, 0x00, 0x04, 0x08, 0x01, 0x44, 0x42, 0x70}

void setup() { 
  Serial.begin(9600); 
  Serial.flush();
  delay(1000);//enter AT mode start
  Serial.print("+");//AT
  Serial.print("+");//AT
  Serial.print("+");//AT
  Serial.flush();
  delay(1000);//enter AT mode finish 
  while(Serial.available()>0){
    Serial.write(Serial.read());
  }

}

void loop(){
  Serial.println("ATDB");
  
  while(Serial.available()>0){
    Serial.write(Serial.read());
  }
  
  delay(750);//3/4 a sec
} 




