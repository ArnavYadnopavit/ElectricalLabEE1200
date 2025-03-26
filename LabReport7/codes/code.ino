#define CLOCK_PIN 13
#define Q0_PIN 2
#define Q1_PIN 3
#define Q2_PIN 4
#define TEST 5

void setup() {
    pinMode(CLOCK_PIN, OUTPUT);
    pinMode(Q0_PIN, INPUT);
    pinMode(Q1_PIN, INPUT);
    pinMode(Q2_PIN, INPUT);
    pinMode(TEST, INPUT);
    Serial.begin(9600);
}

void loop() {
    // Generate clock signal
    digitalWrite(CLOCK_PIN, HIGH);
    delay(500);
    digitalWrite(CLOCK_PIN, LOW);
    delay(500);

    // Read flip-flop outputs
    int Q0 = digitalRead(Q0_PIN);
    int Q1 = digitalRead(Q1_PIN);
    int Q2 = digitalRead(Q2_PIN);
    int Test = digitalRead(TEST);

    // Send data to Serial Plotter
    Serial.print("Q0:"); Serial.print(Q0);
    Serial.print(" Q1:"); Serial.print(Q1);
    Serial.print(" Q2:"); Serial.print(Q2);
    Serial.print(" Test:"); Serial.println(Test);
}

