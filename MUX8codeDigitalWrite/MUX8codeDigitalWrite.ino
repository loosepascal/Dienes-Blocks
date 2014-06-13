#include <LiquidCrystal.h>

LiquidCrystal lcd(8, 9, 10, 11, 12 , 13);

int S0 = 7;
int S1 = 6;
int S2 = 5;
int S3 = 4;

int muxValues[] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
int muxThresholds[] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};//= {310,250,400,370,340,380,360,310,295,430};

// digital values to control 8 inputs
int d_bin[]={LOW,LOW,LOW,LOW,LOW,LOW,LOW,LOW,HIGH,HIGH,HIGH,HIGH,HIGH,HIGH,HIGH,HIGH};
int c_bin[]={LOW,LOW,LOW,LOW,HIGH,HIGH,HIGH,HIGH,LOW,LOW,LOW,LOW,HIGH,HIGH,HIGH,HIGH};
int b_bin[]={LOW,LOW,HIGH,HIGH,LOW,LOW,HIGH,HIGH,LOW,LOW,HIGH,HIGH,LOW,LOW,HIGH,HIGH};
int a_bin[]={LOW,HIGH,LOW,HIGH,LOW,HIGH,LOW,HIGH,LOW,HIGH,LOW,HIGH,LOW,HIGH,LOW,HIGH};

int i=0;
int a=0;
int a_val=0;
int b_val=0;
int c_val=0;
int d_val=0;

  
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
  
  calibration();
 
}
 

void loop()
{
  
  for(i=0;i<=15;i++) {

    //select mux input
    a_val=a_bin[i];
    b_val=b_bin[i];
    c_val=c_bin[i];
    d_val=d_bin[i];

    digitalWrite(S0,a_val);
    digitalWrite(S1,b_val);
    digitalWrite(S2,c_val);
    digitalWrite(S3,d_val);
  
 
    muxValues[i] = analogRead(0);
    
  }

  
  a=0;
  if(muxValues[0] > muxThresholds[0]) a++;
  if(muxValues[1] > muxThresholds[1]) a++;
  if(muxValues[2] > muxThresholds[2]) a++;
  if(muxValues[3] > muxThresholds[3]) a++;
  if(muxValues[4] > muxThresholds[4]) a++;
  if(muxValues[5] > muxThresholds[5]) a++;
  if(muxValues[6] > muxThresholds[6]) a++;
  if(muxValues[7] > muxThresholds[7]) a++;
  if(muxValues[8] > muxThresholds[8]) a++;
  if(muxValues[9] > muxThresholds[9]) a++;
 
  lcd.clear(); 
  lcd.setCursor(0, 0); lcd.print("0"); lcd.setCursor(2, 0); lcd.print(" Units");

  lcd.setCursor(0, 1); lcd.print(a); lcd.setCursor(2, 1); lcd.print(" Tens");  
 
  lcd.setCursor(0, 2); lcd.print("0"); lcd.setCursor(2, 2);lcd.print(" Hundreds");  
  
  lcd.setCursor(0, 3); lcd.print("0"); lcd.setCursor(2, 3);lcd.print(" Thousands"); 
    
    Serial.print(" "); 
    Serial.print("0"); Serial.print(" "); 
    Serial.print(a); Serial.print(" "); 
    Serial.print("0"); Serial.print(" "); 
    Serial.println("0"); 
    
    
  //displayData();
  while((Serial.available() >0)){
    Serial.println(Serial.read());
  }
  Serial.println("-------------------------------------------------------------------");
delay(1000);
  
  
  //compare each input to threshold, if > increment counter  
  
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

 //calibration of sensors (compensate for temperature errors). PLatform needs to be empty
 void calibration() {
   
   for(i=0;i<=9;i++) {
    //select mux input
    a_val=a_bin[i];
    b_val=b_bin[i];
    c_val=c_bin[i];
    d_val=d_bin[i];
    digitalWrite(S0,a_val);
    digitalWrite(S1,b_val);
    digitalWrite(S2,c_val);
    digitalWrite(S3,d_val);
    muxThresholds[i] = analogRead(0);
    muxThresholds[i] = muxThresholds[i] + 15;
    Serial.println(muxThresholds[i]);

    delay(100);
   }
 }
