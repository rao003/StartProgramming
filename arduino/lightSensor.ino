// https://pimylifeup.com/arduino-light-sensor/

/*
  Arduino Light Sensor
  Created: 02/19/2016
  By Gus
  Modified N/A
  By Gus
  https://arduinomylifeup.com/arduino-light-sensor
*/


int greenLedPin = 2;           // Pin Green LED is connected to
int yellowLedPin = 3;          // Pin Yellow LED is connected to
int redLedPin = 4;             // Pin Red LED is connected to

int lightSensorPin = A0;        // PIN Light Sensor is connected to
int analogValue = 0;


void setup() {
  //Set pins to outputs
  pinMode(greenLedPin, OUTPUT);
  pinMode(yellowLedPin,OUTPUT);
  pinMode(redLedPin,OUTPUT);
}

void loop(){
  analogValue = analogRead(lightSensorPin);
  if(analogValue < 50){            
    digitalWrite(redLedPin, HIGH);
  }
  else if(analogValue >= 50 && analogValue <= 100){
    digitalWrite(yellowLedPin, HIGH);
  }
  else{
    digitalWrite(greenLedPin, HIGH);
  }
  delay(200);
  digitalWrite(greenLedPin, LOW);
  digitalWrite(yellowLedPin, LOW);
  digitalWrite(redLedPin, LOW);
}
