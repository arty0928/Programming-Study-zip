#include<stdio.h>
#include<stdlib.h>

typedef int element; //4 bytes

//stack_node 구조체를 가리키는 포인터
//=구조체 stack_node의 주소를 가지는 변수 stack_pointer
typedef struct stack_node* stack_pointer; 

typedef struct stack_node{
	element data;
	stack_pointer link; //stack_node의 주소를 가지는 변수
	
}snode;

//헤더 포인터 생성, 초기에는 스택에 아무것도 없으니까 NULL
stack_pointer top = NULL; 

// linked stack 삽입
void push (element value){

	//구조체 stack_node 사이즈만큼 동적할당
		//malloc(sizeof(snode)): 구조체 snode의 사이즈만큼 메모리를 동적할당해서 void*(타입이 없는 일반 포인터 반환)
		//(stack_pointer)malloc(sizeof(snode)): 동적할당한 포인터를 stack_pointer타입으로 전환 
	stack_pointer news=(stack_pointer)malloc(sizeof(snode));
	news->data = value;
	news -> link = top; //top=NULL
	top = news;
} 