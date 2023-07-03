#include <stdio.h>
#include <stdlib.h>
#define N 10
 
typedef int element; //나중에 int만 char 로 바꿔주면 됨

element stack[N];// 배열의 크기도 나중에 바꿀 수도 있으니까
int top = -1;

// 노드 삽입
void push(int value){
	if(top>=N -1){
		printf("stack overflow");
		exit(1);
	}
    top++;
	stack[top] = value;
} //값을 삽입하는 함수 

// 노드 삭제
element pop(){
	if (top<=-1){ //top = -1 : stack 공백
		printf("stack underflow");
		exit(1);
	}
	
	element tmp;
	tmp = stack[top];
	top--; 
	return tmp;
}

int main(){
	push(5); //stack: 5
 	push(3); //stack: 5 3
	printf("%d\n", pop()); //stack: 5 , 3출력
	push(7);  //stack: 5 7
	printf("%d\n",pop()); //stack: 5, 7출력
	printf("%d\n",pop()); //stack:  , 5출력
	
}
