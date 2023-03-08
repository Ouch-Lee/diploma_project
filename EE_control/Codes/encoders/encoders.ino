#include "kf.hpp"
volatile long temps[4];
volatile long encoderCounter[4];
//int PinA_1 = 18; //interrupt pin 2 
//int PinA_2 = 19;
//int PinA_3 = 2;
//int PinA_4 = 3;
int PinA[4] = {18, 19, 2, 3};


//int PinB_1 = 6; //interrrupt pin 3
//int PinB_2 = 7;
//int PinB_3 = 8;
//int PinB_4 = 9;
int PinB[4] = {6, 7, 8, 9};

int analogPin = A0;
// Pin_Z:

//

// output angle
float angles[4];
double angleKF[4];
double angleKF0;
double angleKF1;
double angleKF2;
double angleKF3;
double angle_anlog = 0.0;
int iVal = 0;
KalmanFilter encoderKF = KalmanFilter(1, 1);


void setup() {
  // put your setup code here, to run once:
  Serial.begin (115200);
  for (int i = 0; i<4; i++)
  {
  pinMode(PinA[i], INPUT_PULLUP);
  pinMode(PinB[i], INPUT_PULLUP);
  }
  // interrupt
  
  attachInterrupt (digitalPinToInterrupt(PinA[0]), doEncoderA_0, FALLING);
  attachInterrupt (digitalPinToInterrupt(PinA[1]), doEncoderA_1, FALLING);
  attachInterrupt (digitalPinToInterrupt(PinA[2]), doEncoderA_2, FALLING);
  attachInterrupt (digitalPinToInterrupt(PinA[3]), doEncoderA_3, FALLING);

}

void loop() {
  // put your main code here, to run repeatedly:

  iVal = analogRead(analogPin);
  angle_anlog =iVal * 360.0 / 1018;
  
  for (int i=0; i<4; i++)
  {
    angles[i] = 1.0 * encoderCounter[i]*360/1024;
    }

  for (int q = 0; q<4; q++){
    if(temps[q] != encoderCounter[q])
    {
      angleKF[q] = encoderKF.update(angles[q]);
      temps[q] = encoderCounter[q];
//      Serial.print("the encoder ");
//      Serial.print(q);
//      Serial.print("angle : ");
//      Serial.println(angleKF[q]);
      }
    }

    Serial.print(angle_anlog);
    Serial.print(" ");
    for(int p =0; p<3; p++){
      Serial.print(angleKF[p]);
      Serial.print(" ");
      }
     Serial.println(angleKF[3]);
    

//   if(temps[0] != encoderCounter[0])
//   {
//    angleKF0 = encoderKF.update(angles[0]);
//    temps[0] = encoderCounter[0];
//    Serial.print(",");
//    Serial.println(angleKF0);
//    }
//   if(temps[1] != encoderCounter[1])
//   {
//    angleKF1 = encoderKF.update(angles[1]);
//    temps[1] = encoderCounter[1];
//    Serial.print(",");
//    Serial.println(angleKF1);
//    }
//   if(temps[2] != encoderCounter[2])
//   {
//    angleKF2 = encoderKF.update(angles[2]);
//    temps[2] = encoderCounter[2];
//    Serial.print(",");
//    Serial.println(angleKF2);
//    }
//   if(temps[3] != encoderCounter[3])
//   {
//    angleKF3 = encoderKF.update(angles[3]);
//    temps[3] = encoderCounter[3];
//    Serial.print(",");
//    Serial.println(angleKF3);
//    }
//   

    
      

}

void doEncoderA_0(){
      if (digitalRead(PinB[0]) == HIGH) {   
      encoderCounter[0]  += 1;          // CW
      
    } 
    else {
      encoderCounter[0] -= 1;          // CCW
    }
  }

void doEncoderA_1(){
      if (digitalRead(PinB[1]) == HIGH) {   
      encoderCounter[1]  += 1;          // CW
      
    } 
    else {
      encoderCounter[1] -= 1;          // CCW
    }
  }
  
void doEncoderA_2(){
      if (digitalRead(PinB[2]) == HIGH) {   
      encoderCounter[2]  += 1;          // CW
      
    } 
    else {
      encoderCounter[2] -= 1;          // CCW
    }
  }
void doEncoderA_3(){
      if (digitalRead(PinB[3]) == HIGH) {   
      encoderCounter[3]  += 1;          // CW
      
    } 
    else {
      encoderCounter[3] -= 1;          // CCW
    }
  }
