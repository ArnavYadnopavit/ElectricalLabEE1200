const int clockPin = 12;
const int xPin = 13;
const int xNotPin = 11;
#define TEST A0


// You can change this array for different input sequences
int x_array[] = {1, 1, 0, 1, 1,1, 0, 1, 1};  // Example: 11011011 (overlapping pattern)

const int arrayLength = sizeof(x_array) / sizeof(x_array[0]);

void setup() {
    Serial.begin(9600);

  pinMode(clockPin, OUTPUT);
  pinMode(xPin, OUTPUT);
  pinMode(xNotPin, OUTPUT);
  pinMode(TEST,INPUT);
}
int index = 0;
void loop() {
  int q0=digitalRead(2),q1=digitalRead(3),q2=digitalRead(4);
    

    Serial.print(q2);
  Serial.print(q1);
  Serial.println(q0);
      // 1 for HIGH, 0 for LOW
delay(1000);
  if (index < arrayLength) {
    // Rising edge of clock
    

    int x = x_array[index];
    
  Serial.println(x);
    Serial.println();
    digitalWrite(xPin, x);
    digitalWrite(xNotPin, !x);
    int bitValue = analogRead(TEST);
Serial.println(bitValue);
    digitalWrite(clockPin, HIGH);
    delay(500); // Keep clock HIGH for 500 ms

    // Falling edge of clock
    digitalWrite(clockPin, LOW);
    delay(500); // Keep clock LOW for 500 ms

    index++;
  } //else {
    // Hold last state after array is done
    //digitalWrite(clockPin, LOW);
    //digitalWrite(xPin, LOW);
    //digitalWrite(xNotPin, HIGH);
  //}
}
