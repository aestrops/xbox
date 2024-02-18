int D8=15;
uint8_t close=0x42;
uint8_t open=0x41;
int a=0;
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(D8,OUTPUT);
}

void loop() {
uint8_t income=Serial.read();
if (income == close){
  digitalWrite(D8,HIGH);
}
if (income == open){
  digitalWrite(D8,LOW);
}
}