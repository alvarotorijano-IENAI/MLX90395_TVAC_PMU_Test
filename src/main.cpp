#include <Arduino.h>


const int DELAY_LED = 500;
const int LED_PIN_IENAI = 41;

void setup() {
  Serial.begin(9600);
  pinMode(LED_PIN_IENAI, OUTPUT);
  // put your setup code here, to run once:
}

void loop() {
  Serial.println("IENAI");
  digitalWrite(LED_PIN_IENAI, HIGH);
  delay(DELAY_LED);
  digitalWrite(LED_PIN_IENAI, LOW);
  delay(DELAY_LED);
  // put your main code here, to run repeatedly:
}
