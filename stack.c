#include<stdio.h>
#define MAX_STACK_SIZE 100
 
int stack[MAX_STACK_SIZE];      //스택의 사이즈 100으로 지정 
int top=-1;     
 
int IsEmpty(){      
    if(top<0)       
        return true;
    else            
        return false;
    }


int IsFull(){       //스택이 꽉 차있나? 확인하는 함수임
    if(top>=MAX_STACK_SIZE-1)   
        return true;         
    else                
        return false;
}
 
void push(int value){       
    if(IsFull()==true)      
        printf("스택이 가득 찼습니다.");
    else                   
        stack[++top]=value; 
}
 
int pop(){                  //데이터 빼기
    if(IsEmpty()==true)     
        printf("스택이 비었습니다.");
    else                
        return stack[top--];  
}
 
int main(){
    
    push(3);
    push(5);
    push(12);
    printf("%d ",pop());
    printf("%d ",pop());
    printf("%d ",pop());
 
    return 0;
}
