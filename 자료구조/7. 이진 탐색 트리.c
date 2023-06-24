#include<stdio.h>
#include<stdio.h>

typedef int element;
struct tree{
	struct tree* llink;
	element data;
	struct tree* rlink;
};

//n1 -> n2 -> n3
struct tree n3={NULL,1,NULL};
struct tree n2={&n3, 3,NULL};
struct tree n1={&n2, 5,NULL};

//key가 있는지 확인
struct tree* search1(struct tree* root, element key){//재귀함수 

	//트리가 비어있음
	if(root==NULL){
		printf("트리에 찾는 값이 없습니다.");
		return NULL; 
	}
	
	//root에 data가 있는 경우
	if(root->data==key) return root; 

	// data < key 오른쪽 
	else if(root->data<key) search1(root->rlink, key);

	// data > key 왼쪽
	else search1(root->llink, key);
} 


struct tree* search2(struct tree* root, element key){//반복문 
	//root가 null이면 끝남 (마지막 노드까지)
	while(root!=NULL){
		if(root->data==key)return root;

		//data < key면 root->rlink가 새로운 root가 됨
		else if(root->data<key) root=root->rlink;

		//data > key면 root->llink가 새로운 root가 됨
		else root=root->llink; 
		
	}
	printf("트리에 찾는 값이 없습니다.");
	return NULL; 
}

int main(void){

	//root노드부터 3이 있는지 탐색
	struct tree* a=search1(&n1,3);
	printf("%d", a->data);	
} 


