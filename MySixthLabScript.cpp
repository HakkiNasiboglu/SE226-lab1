// Online C++ compiler to run C++ program online
#include <iostream>
using namespace std;

double function(double n){
 
    if(n == 0){
        return 0.0;
   }
   else{
     
       return 1.0 /n + function(n-1);
    }
}
int main() {
    double a;
    cin>>a;
 
    cout<<function(a);
   
    return 0;
}
