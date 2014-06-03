#include <LiquidCrystal.h>

LiquidCrystal lcd(8, 9, 10, 11, 12 , 13);

int S0 = 7;
int S1 = 6;
int S2 = 5;
int S3 = 4;

int muxValues[] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};

void setup()
{
 Serial.begin(9600);
 for (int a=4; a<8; a++)
  {
    pinMode(a, OUTPUT);
  }
  analogReference(EXTERNAL);
  
  lcd.begin(20,4);
  lcd.setCursor(4,1);  lcd.print("Welcome to");
  lcd.setCursor(4,2); lcd.print("Dienes Blocks!");
  delay(2000);
  lcd.clear();
}
 
 void displayData()
// dumps captured data from array to serial monitor
{
  Serial.println();
  Serial.println("Values from multiplexer:");
  Serial.println("========================");
  for (int i = 0; i < 10; i++)
  {
    Serial.print("input I");
    Serial.print(i);
    Serial.print(" = ");
    Serial.println(muxValues[i]);
  }
  Serial.println("========================");  
}



// digital values to control 8 inputs
int d_bin[]={LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,HIGH,HIGH,HIGH,HIGH,HIGH,HIGH,HIGH,HIGH};
int c_bin[]={LOW,LOW,LOW,LOW,HIGH,HIGH,HIGH,HIGH,LOW,LOW,LOW,LOW,HIGH,HIGH,HIGH,HIGH};
int b_bin[]={LOW,LOW,HIGH,HIGH,LOW,LOW,HIGH,HIGH,LOW,LOW,HIGH,HIGH,LOW,LOW,HIGH,HIGH};
int a_bin[]={LOW,HIGH,LOW,HIGH,LOW,HIGH,LOW,HIGH,LOW,HIGH,LOW,HIGH,LOW,HIGH,LOW,HIGH};

int entrada=0;
int a_val=0;
int b_val=0;
int c_val=0;
int d_val=0;

void loop()
{
  
  for(entrada=0;entrada<=15;entrada++) {

    //select mux input
    a_val=a_bin[entrada];
    b_val=b_bin[entrada];
    c_val=c_bin[entrada];
    d_val=d_bin[entrada];

    digitalWrite(S0,a_val);
    digitalWrite(S1,b_val);
    digitalWrite(S2,c_val);
    digitalWrite(S3,d_val);
  
  
//  for (int i = 0; i < 16; i++)
  //{ digitalWrite(S0, LOW); digitalWrite(S1, LOW);digitalWrite(S2, LOW);  digitalWrite(S3, LOW);  
    muxValues[entrada] = analogRead(0);
    
  }
  displayData();
 // delay(250);
  
  int a=0;
  if(muxValues[0] > 420) a++;
  if(muxValues[1] > 300) a++;
  if(muxValues[2] > 450) a++;
  if(muxValues[3] > 420) a++;
  if(muxValues[4] > 400) a++;
  if(muxValues[5] > 450) a++;
  if(muxValues[6] > 400) a++;
  if(muxValues[7] > 370) a++;
  if(muxValues[8] > 300) a++;
  if(muxValues[9] > 445) a++;
 
   Serial.print(a);
    Serial.println(" Tens");
  lcd.setCursor(0, 0); lcd.print("0"); lcd.setCursor(1, 0); lcd.print(" Units");

  lcd.setCursor(0, 1); lcd.print(a); lcd.setCursor(1, 1); lcd.print(" Tens");  
 
  lcd.setCursor(0, 2); lcd.print("0"); lcd.setCursor(1, 2);lcd.print(" Hundreds");  
  
  lcd.setCursor(0, 3); lcd.print("0"); lcd.setCursor(1, 3);lcd.print(" Thousands"); 
    
   
  

  
  
  //compare each input to threshold, if > increment counter  
  
}
