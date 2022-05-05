#define _USE_MATH_DEFINES
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define final_t 10000
#define stepsize 0.001
const double G =1;//暂设为引力常数
//三个星体的质量
const double m1 =10;
const double m2 =1000;
const double m3 =10;

//三个星体的初始位置
const double ix1=0;
const double iy1=500;
const double ix2=0;
const double iy2=0;
const double ix3=0;
const double iy3=1000;

//三个星体的初始速度
const double iv1_x=1.5;
const double iv1_y=0;
const double iv2_x=0;
const double iv2_y=0;
const double iv3_x=0.8;
const double iv3_y=0;
//定义运动状态
typedef struct{
  double x1, x2, x3, y1, y2, y3, v1_x, v1_y, v2_x, v2_y, v3_x, v3_y;
}SS;
//定义运动方程
SS eom(SS s){
    SS sdot;
    double dis12 = sqrt((s.x1-s.x2)*(s.x1-s.x2)+(s.y1-s.y2)*(s.y1-s.y2));
    double dis13 = sqrt((s.x1-s.x3)*(s.x1-s.x3)+(s.y1-s.y3)*(s.y1-s.y3));
    double dis23 = sqrt((s.x2-s.x3)*(s.x2-s.x3)+(s.y2-s.y3)*(s.y2-s.y3));
    double a12 = G*m2/(dis12*dis12);
    double a13 = G*m3/(dis13*dis13);
    double a21 = G*m1/(dis12*dis12);
    double a23 = G*m3/(dis23*dis23);
    double a31 = G*m1/(dis13*dis13);
    double a32 = G*m2/(dis23*dis23);
    double a1_x = a12*(s.x2-s.x1)/dis12+a13*(s.x3-s.x1)/dis13;
    double a1_y = a12*(s.y2-s.y1)/dis12+a13*(s.y3-s.y1)/dis13;
    double a2_x = a21*(s.x1-s.x2)/dis12+a23*(s.x3-s.x2)/dis23;
    double a2_y = a21*(s.y1-s.y2)/dis12+a23*(s.y3-s.y2)/dis23;
    double a3_x = a31*(s.x1-s.x3)/dis13+a32*(s.x2-s.x3)/dis23;
    double a3_y = a31*(s.y1-s.y3)/dis13+a32*(s.y2-s.y3)/dis23;
    //得到六个速度和六个加速度
    sdot.x1 = s.v1_x;
    sdot.x2 = s.v2_x;
    sdot.x3 = s.v3_x;
    sdot.y1 = s.v1_y;
    sdot.y2 = s.v2_y;
    sdot.y3 = s.v3_y;
    sdot.v1_x = a1_x;
    sdot.v2_x = a2_x;
    sdot.v3_x = a3_x;
    sdot.v1_y = a1_y;
    sdot.v2_y = a2_y;
    sdot.v3_y = a3_y;
    return sdot;
}
SS SS_add(SS a, SS b){
  SS c;
  c.x1 = a.x1 + b.x1;
  c.x2 = a.x2 + b.x2;
  c.x3 = a.x3 + b.x3;
  c.y1 = a.y1 + b.y1;
  c.y2 = a.y2 + b.y2;
  c.y3 = a.y3 + b.y3;
  c.v1_x = a.v1_x + b.v1_x;
  c.v2_x = a.v2_x + b.v2_x;
  c.v3_x = a.v3_x + b.v3_x;
  c.v1_y = a.v1_y + b.v1_y;
  c.v2_y = a.v2_y + b.v2_y;
  c.v3_y = a.v3_y + b.v3_y;
  return c;
}
SS SS_grow(double c, SS a){
  SS f;
  f.x1 = c*a.x1;
  f.x2 = c*a.x2;
  f.x3 = c*a.x3;
  f.y1 = c*a.y1;
  f.y2 = c*a.y2;
  f.y3 = c*a.y3;
  f.v1_x = c*a.v1_x;
  f.v2_x = c*a.v2_x;
  f.v3_x = c*a.v3_x;
  f.v1_y = c*a.v1_y;
  f.v2_y = c*a.v2_y;
  f.v3_y = c*a.v3_y;
  return f;
}
SS rk4(SS s, double h){
  SS k1 = eom(s);
  SS k2 = eom(SS_add(s, SS_grow(h/2., k1)));
  SS k3 = eom(SS_add(s, SS_grow(h/2., k2)));
  SS k4 = eom(SS_add(s, SS_grow(h, k3)));
  SS sf = SS_add(s, SS_grow(h/6., k1));
  sf = SS_add(sf, SS_grow(h/3., k2));
  sf = SS_add(sf, SS_grow(h/3., k3));
  sf = SS_add(sf, SS_grow(h/6., k4));
  return sf;
}
int main(){
   double t=0;
   double h =stepsize;
   double tf = final_t;
   SS s;
   s.x1 = ix1;
   s.x2 = ix2;
   s.x3 = ix3;
   s.y1 = iy1;
   s.y2 = iy2;
   s.y3 = iy3;
   s.v1_x=iv1_x;
   s.v2_x=iv2_x;
   s.v3_x=iv3_x;
   s.v1_y=iv1_y;
   s.v2_y=iv2_y;
   s.v3_y=iv3_y;
   int count = 1;
   FILE* fp = fopen("threebody2drk4.txt", "a");
    while(t <= tf){
    s = rk4(s, h);
    t += h;
    //每50秒记录一次
    if(count%50000==0){
        fprintf(fp, "%.15le %.15le %.15le %.15le %.15le %.15le %.15le %.15le %.15le %.15le %.15le %.15le %.15le \n", t, s.x1, s.y1, s.x2, s.y2, s.x3, s.y3, s.v1_x, s.v1_y, s.v2_x, s.v2_y, s.v3_x, s.v3_y);
    }
    count ++;
  }
  
  fclose(fp);
  
  return 0;

}
    
