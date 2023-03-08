#include "kf.hpp"

volatile long temp, encoderCounter =0; //This variable will increase or decreas depending on the rotation of encoder
//int PinA_1 = 18; //interrupt pin 2 
//int PinA_2 = 19;
//int PinA_3 = 2;
//int PinA_4 = 3;
int PinA[4] = {18, 19, 2, 3};
int PinA_1 = PinA[0];

//int PinB_1 = 6; //interrrupt pin 3
//int PinB_2 = 7;
//int PinB_3 = 8;
//int PinB_4 = 9;
int PinB[4] = {6, 7, 8, 9};
int PinB_1 = PinB[2];



//int PinZ = 3; 

float angle = 0.0;
double angleKF = 0.0; //kalman update Distance

int tmp_Z = LOW;
int count_Z = 0;
KalmanFilter encoderKF = KalmanFilter(1, 1);

void setup() {
Serial.begin (115200);
//pinMode (PinA_1, INPUT_PULLUP); 
for (int i = 0; i<4; i++)
{
  pinMode(PinA[i], INPUT_PULLUP);
  }
pinMode (PinB_1, INPUT_PULLUP); 

//Setting up interrupt
//attach an interrupt to pin PinA_1 & PinA_1 of the Arduino, and when the pulse is in the CHANGE edge called the function doEncoderA()/doEncoderB()
attachInterrupt (digitalPinToInterrupt(PinA_1), doEncoderA, FALLING);//B rising pulse from encodenren activated ai1(). AttachInterrupt 1 isDigitalPin nr 3 on moust Arduino.
//attachInterrupt (digitalPinToInterrupt(PinZ), doEncoderZ, RISING);
}

void loop() {
  // Send the value of counter
  angle = 1.0 * encoderCounter*360/1024;//ppr=172032
  
  if ( encoderCounter!= temp){
  Serial.print (angle);
  temp = encoderCounter;
  angleKF = encoderKF.update(angle);
  Serial.print(",");
  Serial.println(angleKF);
  
//  if (doEncoderZ() == true){
////    Serial.println("count++");
//    int turns = round(angle/360);
//    angle = 360 * turns;
//    encoderCounter = angle * 1024/360;
//    }
  }
}

void doEncoderA(){
//  encoderCounter ++;
    if (digitalRead(PinB_1) == HIGH) {   
      encoderCounter  += 1;          // CW
      
    } 
    else {
      encoderCounter -= 1;          // CCW
    }
  
  //Serial.println (encoder0Pos, DEC);          
  // use for debugging - remember to comment out
}

//boolean doEncoderZ(){  // when shaft back to 0'clock count +1
//    if(digitalRead(PinZ) == HIGH){
//    tmp_Z = HIGH;
//}
//    if((digitalRead(PinZ) == LOW) && (tmp_Z == HIGH)){
////      count_Z ++; 
////      Serial.println (count_Z);
//      tmp_Z = LOW;
//      return true;
//    }
//    return false;
//  }


//void doEncoderB(){
//
//  // look for a low-to-high on channel B
//  if (digitalRead(PinB_1) == HIGH) {   
//   // check channel A to see which way encoder is turning
//    if (digitalRead(PinA_1) == HIGH) {  
//      encoderCounter = encoderCounter + 1;         // CW
//    } 
//    else {
//      encoderCounter = encoderCounter - 1;         // CCW
//    }
//  }
//  // Look for a high-to-low on channel B
//  else { 
//    // check channel B to see which way encoder is turning  
//    if (digitalRead(PinA_1) == LOW) {   
//      encoderCounter = encoderCounter + 1;          // CW
//    } 
//    else {
//      encoderCounter = encoderCounter - 1;          // CCW
//    }
//  }
//}
