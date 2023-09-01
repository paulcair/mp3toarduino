#include "abc.h"

// Constants
const int speakerPin = 9; // Select the pin that your speaker is outputting to

void setup() {
  // Configure the output pin
  pinMode(speakerPin, OUTPUT);
  Serial.begin(9600);
  Serial.println("welcome to tone player");
  tone(speakerPin, 1000, 10000);
  
}

void loop() {
  // Play the audio 
  
  for (int thisNote = 0; thisNote < NUMBER_OF_NOTES; thisNote ++)
    {
      int thisNoteTone = abc[thisNote]; //Replace helloThere with the "Filename" you wrote in the python program
      // If the frequency is below the acceptable range of the speaker, play the lowest note in the range
      if(thisNoteTone < 35)
      {
        thisNoteTone = 35;
      }
      Serial.println(thisNoteTone);

      tone(speakerPin, thisNoteTone, FREQUENCY_DURATION_MS); // Function that plays the songs

      // delay(FREQUENCY_DURATION_MS/2); // A small pause between tones to seperate them out
    
    }

delay(5000); // Play the file every second
 
}
