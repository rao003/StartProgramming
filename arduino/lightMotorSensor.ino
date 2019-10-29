// https://www.instructables.com/id/Motion-activated-light-with-Arduino-and-HC-SR04-se/

#define trigPin 6 //Define the HC-SE04 triger on pin 6 on the arduino
#define echoPin 5 //Define the HC-SE04 echo on pin 5 on the arduino

#define bulb 9 //Define the relay signal on pin 9 on the arduino

void setup()

{

Serial.begin (9600); //Start the serial monitor

pinMode(trigPin, OUTPUT); //set the trigpin to output

pinMode(echoPin, INPUT); //set the echopin to input

pinMode (bulb, OUTPUT); //set the bulb on pin 9 to output

}

void loop()

{

int duration, distance; //Define two intregers duration and distance to be used to save data

digitalWrite(trigPin, HIGH); //write a digital high to the trigpin to send out the pulse

delayMicroseconds(500); //wait half a millisecond

digitalWrite(trigPin, LOW); //turn off the trigpin

duration = pulseIn(echoPin, HIGH); //measure the time using pulsein when the echo receives a signal set it to high

distance = (duration/2) / 29.1; //distance is the duration devided by 2 becasue the signal traveled from the trigpin then back to the echo pin, then divide by 29.1 to convert to centimeters

if (distance < 13) //if the distance is less than 13 CM

{

Light(); //execute the Light subroutine below

}

Serial.print(distance); //Dispaly the distance on the serial monitor

Serial.println(" CM"); //in centimeters

delay(500); //delay half a second

}

void Light() //Start the Light subroutine

{ digitalWrite(bulb, HIGH); //turn on the light

delay (15000); //wait 15 seconds

digitalWrite(bulb, LOW); //turn off the light

}
