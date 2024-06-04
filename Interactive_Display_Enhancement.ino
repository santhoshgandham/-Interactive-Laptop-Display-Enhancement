int trigpin1 = 2;
int echopin1 = 15;
int trigpin2 = 14;
int echopin2 = 12;

int duration1;
long distance1;
int duration2;
long distance2;

void setup() {
pinMode(trigpin1, OUTPUT);
  pinMode(echopin1, INPUT);
  pinMode(trigpin2, OUTPUT);
  pinMode(echopin2, INPUT);

Serial.begin(9600);
}

void loop() {
  digitalWrite(trigpin1, LOW);
    delayMicroseconds(2); 

    digitalWrite(trigpin1,HIGH);
    delayMicroseconds(10);
    digitalWrite(trigpin1,LOW);
  duration1 = pulseIn(echopin1, HIGH);
    distance1= (duration1 * 0.0344 / 2);
  delay(100);

   digitalWrite(trigpin2, LOW);
    delayMicroseconds(2); 

    digitalWrite(trigpin2,HIGH);
    delayMicroseconds(10);
    digitalWrite(trigpin2,LOW);
  duration2 = pulseIn(echopin2, HIGH);
    distance2= (duration2 * 0.0344 / 2);
    delay(100);

      Serial.print(distance1);
  Serial.print(",");
  Serial.println(distance2);

 

}