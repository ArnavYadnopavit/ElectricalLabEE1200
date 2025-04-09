#define Q1 2  // Input buttons
#define Q2 3
#define Q3 4
#define Q4 5
#define DOWN 8  // LED output
#define UP 9
#define TERMOWN 6
#define TERMP 7 
#define CLOCK 13
#define TEST A0
void setup() {
    pinMode(Q1, INPUT_PULLUP);
    pinMode(Q2, INPUT_PULLUP);
    pinMode(Q3, INPUT_PULLUP);
    pinMode(Q4, INPUT_PULLUP);
  pinMode(TERMOWN, INPUT);
  pinMode(TERMP, INPUT);
    pinMode(DOWN, OUTPUT);
    pinMode(UP, OUTPUT);
    pinMode(13, INPUT_PULLUP);
  pinMode(12, INPUT_PULLUP);
  pinMode(11, INPUT_PULLUP);
  pinMode(10, INPUT_PULLUP);
  pinMode(TEST,INPUT);// Set pin 13 as input
  pinMode(A1,INPUT);
  pinMode(A2,INPUT);
  pinMode(4,OUTPUT);
  Serial.begin(9600); 
}

void loop() {
    // Read input buttons (LOW when pressed)
    int q1 = digitalRead(10);  // NOT operation
    int q2 = digitalRead(11);
    int q3 = digitalRead(12);
    int q4 = digitalRead(13);
    int term1= digitalRead(TERMOWN);
    int term2= digitalRead(TERMP);    
    int test=analogRead(TEST);
    int a=analogRead(A1);
    int b=analogRead(A2);
    Serial.println();
    Serial.println(a);
    Serial.println(b);
    int a_st = (a > 200) ? 1 : 0;

  // Check if b > 100 and convert to 1 or 0
  int b_st = (b > 200) ? 1 : 0;
    int c=a_st&b_st;
    digitalWrite(4,c);
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
  int value2 = digitalRead(12);
  int value1 = digitalRead(11);
  int value0 = digitalRead(10);
  // Read value from pin 13
  Serial.print(value3);
  Serial.print(value2);
  Serial.print(value1);
  Serial.println(value0);
  Serial.println(test);
  Serial.println(and_result);
 Serial.println(ANDD);
   Serial.println(term1);// Print value (0 or 1)
  Serial.println(term2);// Print value (0 or 1)

  delay(500);  
 
    
}
