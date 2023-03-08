#ifndef KF_H
#define KF_H

//#include <iostream>
using namespace std;

/*
system model:
    x_(k+1) = x_k + w_k   w_k ~ N(0, Q_k)
    y_k = x_k + v_k    v_k ~ N(0, R_k)
*/
class KalmanFilter{
  private:
    double pre_err; // Q
    double mea_err; // R

    // x_0,P_0 is arbitrary
    double x = 0.0;
    double P = 1;
    double _x ;
    double _P; 
    double K; 

public:


    KalmanFilter():pre_err(2),mea_err(16){
    }

    KalmanFilter(double pre_err, double mea_err):pre_err(pre_err),mea_err(mea_err){
    }

    double update(double measure){
        track_slow();
        _x = x;
        _P = P + pre_err;
        
        K = _P / (_P + mea_err);
        x = _x + K * (measure - _x);
        P = (1 - K) * _P ;
        return x;
    }

    void track_fast(void){
        pre_err = 16;
        mea_err = 0.1;
    }
    void track_slow(void){
        pre_err = 0.3;
        
        mea_err = 16;
    }
};

#endif
