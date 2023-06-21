#include<stdio.h>
#include<stdlib.h>


typedef int element;
struct queue {
	element data;
	struct queue* link;
};

//구조체 queue를 가르키는 포인터
struct queue* front= NULL; // = typedef struct queue_pointer* qpointer;
struct queue* rear= NULL;


void qinsert(element value){

	//queue 사이즈만큼 동적 할당-> 구조체 queue를 가르키는 포인터 타입으로 변환
	struct queue* newq = (struct queue*)malloc(sizeof(struct queue)); //(qpointer)malloc(sizeof(struct queue))
	newq -> data = value;
	newq ->link = NULL;
	if (rear==NULL) //들어올애가 NULL = queue가 비어있을 때
		front = newq; //뺄 때 얘부터 빼면 됨
	
	else
		//rear의 link가 새로운 newq의 주소값 가르킴
		rear ->link = newq; 
	
	//연결
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

	//처음 공백인 상태 : front = null, rear = null (null)

	qinsert(2); //front: 0번지, rear: 0번지 (2)
	qinsert(9); //front: 0번지, rear: 1번지 (2->9)
	printf("%d\n",qdelete()); // front: 1번지, rear: 1번지 (0번지 free) (9)
	printf("%d\n",qdelete()); // front: null, rear: null   (1번지 free) (null)
	qinsert(3); //front: 0'번지, rear: 0'번지 (3)
	qinsert(6); //front: 0'번지, rear: 1'번지 (3->6)
	printf("%d\n",qdelete());//front: 1'번지, rear: 1'번지 (6)
}



