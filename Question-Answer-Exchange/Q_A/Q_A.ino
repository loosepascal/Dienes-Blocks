  //Atmega must check if question answered correctly/incorrectly and display the corresponding feedback on the screen
  //It sends the answer back to the teacher
  //Teacher prorgam sends the next question and records if it was answered incorrectly (in which case it would resend the same question)
  
   //Start
   //keep checking if question arrived
   //Question received-> send conf (don't have timeout for question not received- product may have been switched on and left a bit)
   //Display question for child (start timeout1 to limit time for child to answer)
   //keep checking if submit button has been pressed
   //if still checking and timeout1 is exceeded, send warning to teacher
   //if pressed, send answer to teacher
   //wait for confirmation, start timeout2 to limit time for confimation to come back, 
  //if timeout2 >t1  and no confirmation, resend answer
  //count number of resends (if not using timeout3)
 //if timeout2 >t2/number of resends exceeded without confirmation, display warning on child's screen
//if conf received, go to Start 

//need to set the 3 timeouts
     
#include <LiquidCrystal.h>

LiquidCrystal lcd(8, 9, 10, 11, 12 , 13);

int submit_timer = 0;
int submit_timeout = 1000;
int confirmation_timeout = 1000;
int resend_timeout = 5000;

int SubmitButton = 7;
int Q = 0;
int C = 0;
char Question[4];
char Answer[4];

int Thousands = 0;
int Hundreds = 1;
int Tens = 2;
int Units = 3;

void setup()
{
  Serial.begin(9600);
  pinMode(SubmitButton, OUTPUT);
  pinMode(Thousands, INPUT);
  pinMode(Hundreds, INPUT);
  pinMode(Tens, INPUT);
  pinMode(Units, INPUT);
  
   lcd.begin(20,4);
   lcd.clear(); 
}

void loop(void)
{
  
    while((Serial.available() > 0)  || (Q = 0)){ //if there Is data OR we have not yet read any data from a Question packet
         if(Serial.available() > 0){
           if(Serial.read() == 81) Q = 1;
         }
    } 
    //by here we know we have a Question available to read
    for(int i =0;i<4;i++){
    Question[i] = char(Serial.read());
    }
      
    //Display Question on screen 
    lcd.setCursor(0, 0); 
    for(int i =0;i<4;i++){
    lcd.print(Question[i]);
    }
      
    //keep checking if submit button has been pressed
    //if still checking and timeout1 is exceeded, send warning to teacher
     
    // sei(); //allow global interrupts
    
    unsigned long start = millis();
  
    while(digitalRead(SubmitButton) == 0){
     
    //if(submit_timer = 1)//set submit_timer to 1 in the ISR
    //call function to display warning on screen and halt program
       
       if((millis() - start)>submit_timeout) {
        while(1) {
          Serial.println("!!!!!!!!!!!!!!!submit_timeout!!!!!!!!!!!!!!!!!");//call function to display warning on screen and halt program
       } 
     }
    }
     
   
    //if pressed, read and send answer to teacher
    //read the 4 analogue inputs
    Answer[0] = analogRead(Thousands);
    Answer[1] = analogRead(Hundreds);
    Answer[2] = analogRead(Tens);
    Answer[3] = analogRead(Units);
        
    Serial.print("A"); Serial.print(Answer[0]); Serial.print(Answer[1]); Serial.print(Answer[2]); Serial.print(Answer[3]);
        
     //wait for confirmation, start timeout2 to limit time for confimation to come back, 
    //if timeout2 >t1  and no confirmation, resend answer
    start = millis();
    while((Serial.available() > 0)  || (C = 0)){ //if there Is data OR we have not yet read any data from a Question packet
       if(Serial.available() > 0){
         if(Serial.read() == 67) C = 1;
        }
        
       if((millis()-start)> confirmation_timeout){
         Serial.print("A"); Serial.print(Answer[0]); Serial.print(Answer[1]); Serial.print(Answer[2]); Serial.print(Answer[3]);
       }
       //count number of resends (if not using timeout3)
       //if timeout2 >t2/number of resends exceeded without confirmation, display warning on child's screen
       if((millis()-start)> resend_timeout){
         while(1) {
        Serial.println("!!!!!!!!!!!!!!!resend_timeout!!!!!!!!!!!!!!!!!");//call function to display warning on screen and halt program
         }            
       }
    } 

//if conf received, go to Start 
}


  
  
