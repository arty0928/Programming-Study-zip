#include<stdio.h>
#include<stdlib.h>

typedef int element;
typedef struct stack_node* stack_pointer;

typedef struct stack_node{
	element data;
	stack_pointer link;
	
}snode;

//stack의 top 현재 비어있음
stack_pointer top = NULL;

//삽입
void push (element value){
	stack_pointer news=(stack_pointer)malloc(sizeof(snode));
	news->data = value;
	news -> link = top;
	top = news;

} 

element pop(){

	// stack =NULL
	// top = NULL
	// NULL == FALSE == 0
	// !NULL == TRUE == 1
	if(!top){ //true일때
	  printf("스택에 값이 없습니다");
	  exit(1);
	  }//NULL일때 거짓

	stack_pointer del = top;
	element tmp = top->data ; //삭제한 노드의 데이터 값
	top = top->link;
	free(del); //동적할당한 메모리 free
	return tmp;

}

int main(void){
	push(5); //stack: top -> 5
	push(1); //stack: top -> 1 5 
	printf("%d\n", pop()); //stack: top -> 5, 1출력
	push(3); //stack: top -> 3 -> 5
	printf("%d\n", pop()); //stack: top -> 5, 3 출력
	printf("%d\n", pop()); //stack: top -> NULL, 5출력
}
