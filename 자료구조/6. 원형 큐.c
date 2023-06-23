#include<stdio.h>
#include<stdlib.h>
#define N 5 

typedef int element;
element queue[N];

//처음 공백일때 0번지
int front=0;
int rear=0;

//삽입
void qinsert(element value){

	//포화 상태 확인
	//front :0 , rear: 8 => 큐에 insert만 해서 꽉 참. 0->1->----8->0->1, 여기서 front인 0번지는 비어있는 상태 
	if (front==(rear+1)%N){//front (한칸)비워놓음 
		printf("queue overflow");
		exit(1);
	}
	
	//++rear%N
	//=> rear = (rear + 1) % N
		// (8+1) % 9 = 0 
		//만약 +1을 안하고 rear = rear % N 이면, 8 % 9 = 8, 현재 rear 위치에 삽입하게 됨.
	queue[++rear%N] = value;
} 

element qdelete(){

	//큐 공백 검사
	if (front==rear){
		printf("큐에 값이 없습니다");
	}

	//++front%N
	//=> front = (front + 1) % N
		// (3+1) % 9 = 4번지로 front 이동 
		//만약 +1을 안하고 front = front % N 이면, 3 % 9 = 3, 현재 front 위치 그대로임.
	return queue[++front%N];
}

int main(void){
	//front: 0, rear:0

	qinsert(2); 					// front: 0, rear:1		(2) 
	qinsert(5); 					// front: 0, rear:2		(2 5)
	qinsert(1); 					// front: 0, rear:3		(2 5 1)
	printf("%d\n",qdelete()); 		// front: 1, rear:3		(5 1)
	qinsert(3); 					// front: 1, rear:4		(5 1 3)
	printf("%d\n",qdelete()); 		// front: 2, rear:4		(1 3)
	printf("%d\n",qdelete()); 		// front: 3, rear:4    	(3)
	qinsert(4);						// front: 3, rear:5   	(3 4)
	qinsert(7);						// front: 3, rear:6   	(3 4 7)
} 
