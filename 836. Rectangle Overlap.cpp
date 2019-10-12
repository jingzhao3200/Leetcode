#include <vector>
#include <iostream>
using namespace std;

bool is1DOverlap(int x11, int x12, int x21, int x22){
  cout << x11 << endl;
  cout << x12 << endl;
  cout << x21 << endl;
  cout << x22 << endl;
  if ((x11<=x21 && x12>x21) || (x11>=x21 && x11<x22))
  {cout << "p1" << endl;
    return true;}
  else
  {cout << "p2" << endl;
    return false;}
}

bool isRectangleOverlap(vector<int>& rec1, vector<int>& rec2){
  if (!is1DOverlap(rec1[0], rec1[2], rec2[0], rec2[2]) ||
      !is1DOverlap(rec1[1], rec1[3], rec2[1], rec2[3]) )
    return false;
  else
    return true;
}



int main(){
  vector<int> rec1 = {7,8,13,15};
  vector<int> rec2 = {10,8,12,20};
  if (isRectangleOverlap(rec1, rec2)) 
    cout << "true" << endl;
  else
    cout << "false" << endl;
  return 0;
}
