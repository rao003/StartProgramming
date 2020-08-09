void setup(){
pinMode(2,OUTPUT); // verde rua A
pinMode(3,OUTPUT); // amarelo rua A
pinMode(4,OUTPUT); // vermelho rua A
pinMode(5,OUTPUT); // verde rua B
pinMode(6,OUTPUT); // amarelo rua B
pinMode(7,OUTPUT); // vermelho rua B
 
}
void loop()
 
{
 
digitalWrite(2, HIGH); // turn the green LED on pin 2 on
digitalWrite(3, LOW); // turn the yellow LED on pin 3 off
digitalWrite(4, LOW); // turn the red LED on pin 4 off
digitalWrite(5, LOW); // turn the green LED on pin 5 off
digitalWrite(6, LOW); // turn the yellow LED on pin 6 off
digitalWrite(7, HIGH); // turn the red LED on pin 7 on
delay(1000);
digitalWrite(2, LOW); // turn the green LED on pin 2 off
digitalWrite(3, HIGH); // turn the yellow LED on pin 3 on
digitalWrite(4, LOW); // turn the red LED on pin 4 off
digitalWrite(5, LOW); // turn the green LED on pin 5 off
digitalWrite(6, LOW); // turn the yellow LED on pin 6 off
digitalWrite(7, HIGH); // turn the red LED on pin 7 on
delay(1000);
digitalWrite(2, LOW); // turn the green LED on pin 2 off
digitalWrite(3, LOW); // turn the yellow LED on pin 3 off
digitalWrite(4, HIGH); // turn the red LED on pin 4 on
digitalWrite(5, HIGH); // turn the green LED on pin 5 on
digitalWrite(6, LOW); // turn the yellow LED on pin 6 off
digitalWrite(7, LOW); // turn the red LED on pin 7 off
delay(1000);
digitalWrite(2, LOW); // turn the green LED on pin 2 off
digitalWrite(3, LOW); // turn the yellow LED on pin 3 off
digitalWrite(4, HIGH); // turn the red LED on pin 4 on
digitalWrite(5, LOW); // turn the green LED on pin 5 off
digitalWrite(6, HIGH); // turn the yellow LED on pin 6 on
digitalWrite(7, LOW); // turn the red LED on pin 7 off
delay(1000);
}
