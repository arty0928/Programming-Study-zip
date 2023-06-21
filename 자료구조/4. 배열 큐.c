#include<stdio.h>
#include<stdlib.h>
#define N 5 

typedef int element;
element queue[N];
int front=-1; //여기서부터 빠지면 됨
int rear=-1; //받을차례

void qinsert(element value){
	if (rear>=N-1){ //4
		printf("queue overflow");
		exit(1);
	}
	rear++;
	queue[rear] = value;
} 

element qdelete(){
	if (front==rear){ //여기까지 넣음(front) == 여기까지 뺌(rear) 즉, 넣은거 다 뺌 = 공백
		printf("큐에 값이 없습니다");
	}
	front++;
	return queue[front];
}

int main(void){
	qinsert(2); //front: -1, rear: 0
	qinsert(5); //front: -1, rear: 1
	qinsert(1); //front: -1, rear: 2
	printf("%d\n",qdelete()); //front: 0, rear: 2
	qinsert(3); //front: 0, rear: 3
	printf("%d\n",qdelete()); //front: 1, rear: 3
	qinsert(4); //front: 1, rear: 4
	qinsert(7); //front: 1, rear: 5
} 
