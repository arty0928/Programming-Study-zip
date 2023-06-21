#include<stdio.h>
#include<stdlib.h>
#define N 5 

typedef int element;
element queue[N];
int front=0;
int rear=0;

void qinsert(element value){
	if (front==(rear+1)%N){//한칸 비워놓는 작업 
		printf("queue overflow");
		exit(1);
	}
	
	queue[++rear%N] = value;
} 

element qdelete(){
	if (front==rear){
		printf("큐에 값이 없습니다");
	}
	
	return queue[++front%N];
}

int main(void){
	qinsert(2);
	qinsert(5);
	qinsert(1);
	printf("%d\n",qdelete());
	qinsert(3);
	printf("%d\n",qdelete());
	printf("%d\n",qdelete());
	qinsert(4);
	qinsert(7);
} 
