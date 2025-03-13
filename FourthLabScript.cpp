#include <iostream>
#include <new>
using namespace std;

class Node {
public:
    int data;
    Node* next;
};

class Stack {
private:
    Node* head;     // Points to top element of stack.
    int num;        // Number of elements (index-style tracking).
    int capacity;   // Fixed size limit (resized when full).

public:
    Stack(int initialCapacity) {  // You can set any initial size.
        head = nullptr;
        num = -1;
        capacity = initialCapacity;
    }
    void push(int x) {
        Node *pushed = new Node();
        pushed->data = x;
        pushed->next = head;
        head=pushed;
        num++;
        cout<< pushed->data<< " is added"<<endl;
        
        if(head == nullptr){
            head = pushed;
        }
        
    }

    int pop() {
        Node *popped = new Node();
        popped = head;
        head = head->next;
        cout<<popped->data<<" is popped"<<endl;
        delete popped;
       
        return 0;
    }
    int peek() {
        cout<<head->data;
        return 0;
    }

    bool isEmpty() {
        if(head==nullptr){
            return true;
        }
        else{
            return false;
        }
    }

    void increaseCapacity() {
       capacity++;
    }

    bool deleteElement(int val) {
        // To be implemented.
        return false;
    }
};

int main() {
    Stack stack1(5);
    stack1.push(6);
    stack1.push(10);
    stack1.push(12);
    stack1.pop();
    stack1.peek();

    return 0;
}
