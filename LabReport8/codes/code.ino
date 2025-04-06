#define Q1 2  // Input buttons
#define Q2 3
#define Q3 4
#define Q4 5
#define DOWN 8  // LED output
#define UP 9
#define TERM1 6
#define TERM2 7 
#define CLOCK 13
void setup() {
    pinMode(Q1, INPUT_PULLUP);
    pinMode(Q2, INPUT_PULLUP);
    pinMode(Q3, INPUT_PULLUP);
    pinMode(Q4, INPUT_PULLUP);
  pinMode(TERM1, INPUT);
  pinMode(TERM2, INPUT);
    pinMode(DOWN, OUTPUT);
    pinMode(UP, OUTPUT);
    pinMode(13, INPUT_PULLUP);
  pinMode(12, INPUT_PULLUP);
  pinMode(11, INPUT_PULLUP);
  pinMode(10, INPUT_PULLUP);// Set pin 13 as input
  Serial.begin(9600); 
}

void loop() {
    // Read input buttons (LOW when pressed)
    int q1 = digitalRead(10);  // NOT operation
    int q2 = digitalRead(11);
    int q3 = digitalRead(12);
    int q4 = digitalRead(13);
    int term1= digitalRead(TERM1);
    int term2= digitalRead(TERM2);    

    // Apply De Morgan's theorem
    //int or_result = q1 | q2 | q3 | q4;  // OR operation
    int and_result = ((!q1)&(!q2)&(!q3)&!q4)&term1 ; // NOR gives AND result
    int ANDD=(q1&q4)&(term2);
    //int ter=term1&term2;
    
    // Output the AND operation result
    digitalWrite(DOWN, and_result);
    digitalWrite(UP, ANDD);
  //  digitalWrite(OUTERM, ter);
  int value3 = digitalRead(13);
  int value2 = digitalRead(11);
  int value1 = digitalRead(12);
  int value0 = digitalRead(10);
  // Read value from pin 13
  Serial.print(value3);
  Serial.print(value2);
  Serial.print(value1);
  Serial.println(value0);
  Serial.println(and_result);
 Serial.println(ANDD);// Print value (0 or 1)
   Serial.println(term1);// Print value (0 or 1)
  Serial.println(term2);// Print value (0 or 1)

  delay(500);  
 
    
}
