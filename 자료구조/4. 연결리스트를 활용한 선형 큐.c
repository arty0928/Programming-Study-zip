#include<stdio.h>
#include<stdlib.h>


typedef int element;
struct queue {
	element data;
	struct queue* link;
};

struct queue* front= NULL; 
struct queue* rear= NULL;

void qinsert(element value){
	struct queue* newq = (struct queue*)malloc(sizeof(struct queue));
	newq -> data = value;
	newq ->link = NULL;
	if (rear==NULL)
		front = newq;
	
	else
		rear ->link = newq;
	
	rear = newq;
} 

element qdelete(){
	if(front == NULL){
		printf("큐에 값이 없습니다");
		exit(1); 
	}
	element tmp = front->data;
	struct queue* del = front;
	front = front->link;
	if(front==NULL) rear = NULL; 
	free(del);
	return tmp;
	}
	
int main(void){
	qinsert(2);
	qinsert(9);
	printf("%d\n",qdelete());
	printf("%d\n",qdelete());
	qinsert(3);
	qinsert(6);
	printf("%d\n",qdelete());
}



