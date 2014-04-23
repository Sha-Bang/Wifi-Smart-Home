
const int led = 13;
const int GROUND = 10;
const int POWER = 11;
const int SIGNAL = 12;
const int SENSOR_ID = 1;

unsigned long duration;
int PIN = 7;


int sensor;
byte switchSignal;


// the setup routine runs once when you press reset:
void setup(){
  // initialize the digital pin as an output.
      
  Serial.begin(9600);
  
  pinMode(PIN, INPUT);
  pinMode(led, OUTPUT); 
  pinMode(GROUND, OUTPUT);
  pinMode(POWER, OUTPUT);
  pinMode(SIGNAL, OUTPUT);
  digitalWrite(10, LOW); 
  digitalWrite(11, HIGH);
}

// the loop routine runs over and over again forever:
void loop(){
  delay(100);
  duration = pulseIn(PIN, HIGH);
  Serial.print(duration);
  Serial.print(" ");
  Serial.println(SENSOR_ID);
  
  
  if (Serial.available()>0) {
  // read the incoming byte:
    sensor = Serial.read() - '0';
    switchSignal = Serial.read() - '0';
    Serial.print("#");
    Serial.print(sensor);
    Serial.print("-");
    Serial.println(switchSignal);
    
    analogRead(A5);
    if(sensor == SENSOR_ID) {
      if(switchSignal == 1) {     
        digitalWrite(SIGNAL, HIGH);   // turn the LED on (HIGH is the voltage level) 
        Serial.print("##Turned ON");    
      }
      
      if(switchSignal == 0) {        
        digitalWrite(SIGNAL, LOW);    // turn the LED off by making the voltage LOW    
      }
    }
  }
}




