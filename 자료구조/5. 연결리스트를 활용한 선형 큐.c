#include<stdio.h>
#include<stdlib.h>


typedef int element;
struct queue {
	element data;
	struct queue* link;
};

//구조체 queue를 가르키는 포인터
struct queue* front= NULL; //typedef struct queue_pointer* qpointer;
struct queue* rear= NULL;


void qinsert(element value){

	//queue 사이즈만큼 동적 할당-> 구조체 queue를 가르키는 포인터 타입으로 변환
	struct queue* newq = (struct queue*)malloc(sizeof(struct queue)); //(qpointer)malloc(sizeof(struct queue))
	newq -> data = value;
	newq ->link = NULL;
	if (rear==NULL) //들어올애가 NULL = queue가 비어있을 때
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



