#include<stdio.h>
#include<stdlib.h>
#define N 5 



typedef int element;
element queue[N];
int front=-1;
int rear=-1;

void qinsert(element value){
	if (rear>N-1){
		printf("queue overflow");
		exit(1);
	}
	rear++;
	queue[rear] = value;
} 

element qdelete(){
	if (front==rear){
		printf("큐에 값이 없습니다");
	}
	front++;
	return queue[front];
}

int main(void){
	qinsert(2);
	qinsert(5);
	qinsert(1);
	printf("%d\n",qdelete());
	qinsert(3);
	printf("%d\n",qdelete());
	qinsert(4);
	qinsert(7);
} 
