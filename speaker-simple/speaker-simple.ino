const int speakerPin = 9; // Select the pin that your speaker is outputting to
int distance;
int newDistance; 
int count = 0;
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(speakerPin, OUTPUT);
distance = 1500;
}

void loop() {

newDistance = distance - 75;

if (newDistance <= 25){
  newDistance = 25;
  count ++;

}

if(count<50){  // put your main code here, to run repeatedly:
tone(speakerPin, 2000, 250);
}
noTone(speakerPin);
delay(newDistance);

distance = newDistance;
Serial.println(distance);
Serial.println(count);

}
