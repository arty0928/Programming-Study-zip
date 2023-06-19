#include<stdio.h>
#include<stdlib.h>

typedef int element;
typedef struct stack_node* stack_pointer;
typedef struct stack_node{
	element data;
	stack_pointer link;
	
}snode;

stack_pointer top = NULL;
void push (element value){
	stack_pointer news=(stack_pointer)malloc(sizeof(snode));
	news->data = value;
	news -> link = top;
	top = news;

} 

element pop(){
	if(!top){
	  printf("스택에 값이 없습니다");
	  exit(1);
	  }//NULL일때 참 
	stack_pointer del = top;
	element tmp = top->data ;
	top = top->link;
	free(del);
	return tmp;
}

int main(void){
	push(5);
	push(1);
	printf("%d/n", pop());
	push(3);
	printf("%d/n", pop());
	printf("%d/n", pop());	
}
