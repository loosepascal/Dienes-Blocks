void setup() 
{ Serial.begin(9600); 
} 

void loop() 
{ int a = 2;
int b = 5 ;
int c = 10;
int d = 11;

  while(1)
  {
    Serial.print(" "); 
    Serial.print(a); Serial.print(" "); 
    Serial.print(b); Serial.print(" "); 
    Serial.print(c); Serial.print(" "); 
    Serial.print(d); 
    
    delay(1000);
    
  }

}
