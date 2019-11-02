int light = 0; // store the current light value

void setup() {
    // put your setup code here, to run once:
    Serial.begin(9600); //configure serial to talk to computer
    pinMode(13, OUTPUT); // configure digital pin 13 as an output
    pinMode(12, OUTPUT); // configure digital pin 12 as an output
}

void loop() {
    // put your main code here, to run repeatedly:
    light = analogRead(A0); // read and save value from PR
    
    Serial.println(light); // print current light value
 
    if(light > 450) { // If it is bright...
        Serial.println("It is quite light!");
        digitalWrite(13,LOW); //turn left LED off
        digitalWrite(12,LOW); // turn right LED off
    }
    else if(light > 229 && light < 451) { // If it is average light...
        Serial.println("It is average light!");
       digitalWrite(13, HIGH); // turn left LED on
       digitalWrite(12,LOW);  // turn right LED off
    }
    else { // If it's dark...
        Serial.println("It is pretty dark!");
        digitalWrite(13,HIGH); // Turn left LED on
        digitalWrite(12,HIGH); // Turn right LED on
    }
    delay(1000); // don't spam the computer!
}
