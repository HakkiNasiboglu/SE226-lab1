// Online C++ compiler to run C++ program online
#include <iostream>
using namespace std;

int main() {
    string name;
    string id;
    cout<<"Enter your name:";
    cin>>name;
    cout<<"Hello " + name + "."<<endl;
    cout<<"What is your ID?";
    cin>>id;
    cout<<"Your ID is " + id + "."<<endl;
    
    int var1;
    int var2;
    cout<<"Enter var1 and var2"<<endl;
    cin>>var1;
    cin>>var2;
    int sum;
    int diff;
    int prod;
    sum = var1 + var2;
    diff = var1 / var2;
    prod = var1 * var2;
    
    cout<<var1<<endl;
    cout<<var2<<endl;
    cout<<sum<<endl;
    cout<<diff<<endl;
    cout<<prod<<endl;
    
    string studentname;
    int lab;
    int midterm;
    int final;
    int lastscore;
    cout<<"Enter student's name:"<<endl;
    cin>>studentname;
    cout<<"Enter lab midterm and final grades:"<<endl;
    cin>>lab;
    cin>>midterm;
    cin>>final;

    
    
    
    cout<<"Name: " << studentname<<endl;
    cout<<"Lab: " << lab<<endl;
    cout<<"Midterm: " << midterm<<endl;
    cout<<"Final: " << final<<endl;
    lastscore = (lab * 25/100) + (midterm * 35/100) + (final * 45/100);
    cout<<"Last Score: " << lastscore<<endl;
    
    cout<<"*\n**\n***\n**\n*";
    
    return 0;
}
