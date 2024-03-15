#include <SoftwareSerial.h>

const int triggerPin = 9; // Broche du capteur ultrason (à la fois pour le déclenchement et la réception)

const int greenLedPin = 7; // Broche de la LED verte
const int redLedPin = 8; // Broche de la LED rouge

SoftwareSerial bluetooth(2, 3); // Broches RX, TX pour le module Bluetooth

void setup() {
  pinMode(greenLedPin, OUTPUT);
  pinMode(redLedPin, OUTPUT);

  bluetooth.begin(9600);
}

void loop() {
  if (bluetooth.available()) {
    char command = bluetooth.read();

    if (command == 'S') { // Commande de démarrage (Start)
      while (true) {
        int distance = getDistance();

        if (distance < 10) {
          digitalWrite(greenLedPin, HIGH); // Allumer la LED verte
          digitalWrite(redLedPin, LOW); // Éteindre la LED rouge
        } else {
          digitalWrite(greenLedPin, LOW); // Éteindre la LED verte
          digitalWrite(redLedPin, HIGH); // Allumer la LED rouge
        }

        // Envoyer la distance via Bluetooth
        bluetooth.print(distance);
        bluetooth.print('\n');

        delay(200); // Attente pour éviter une boucle trop rapide
      }
    } else if (command == 'E') { // Commande d'arrêt (End)
      digitalWrite(greenLedPin, LOW); // Éteindre la LED verte
      digitalWrite(redLedPin, LOW); // Éteindre la LED rouge
    }
  }
}

int getDistance() {
  pinMode(triggerPin, OUTPUT);  // Clear the trigger
  digitalWrite(triggerPin, LOW);
  delayMicroseconds(2);
  digitalWrite(triggerPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(triggerPin, LOW);
  pinMode(triggerPin, INPUT);
  return pulseIn(triggerPin, HIGH);
  // Mesurer la durée de l'écho
  long duration = pulseIn(triggerPin, HIGH);

  // Calculer la distance en fonction de la durée de l'écho
  int distance = duration * 0.034 / 2;

  return distance;
}
