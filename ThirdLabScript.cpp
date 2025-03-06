#include <iostream>
#include <new>
using namespace std;

class Node{
    public:
    int data;
    Node *next;
    Node(int x, Node *n){
        data = x, next = n;
    }
};

class   Queue{
    private:
    Node *first = nullptr;
    Node *last = nullptr;
    public:
     Queue() : first(nullptr), last(nullptr) {}
    
    void enqueue(){
        int exit = -1;
    
    do{
        cout<<"Enter a node value: (Enter '-1' to finish looping)"<<endl;
    cin>>exit;
     if(exit != -1){
        if(first == nullptr){
            first = new Node(exit, nullptr); last = first;
        }
        else{
            last ->next = new Node(exit, nullptr); last = last -> next;
        }
        }
    }
    while(exit != -1);
    }
    void print(){
         for(last = first; last != nullptr; last = last-> next  )
        cout<<last->data<<" ";
        cout<<endl;
    }
    void top(){
        cout<<first->data;
    }
    
    };


int main() {
  Queue queue;
  queue.enqueue();
  queue.print();
  queue.top();
   
    return 0;
}
