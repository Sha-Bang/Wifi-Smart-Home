int pin = 7;
unsigned long duration;

void setup()
{
  Serial.begin(9600); 
  pinMode(pin, INPUT);
  Serial.println("Getting started");
}

void loop()
{
  delay(100);
  duration = pulseIn(pin, HIGH);
  Serial.println(duration);
  while(Serial.available()>0){
    Serial.write(Serial.read());
  }
}



