#include<stdio.h>
#include<stdio.h>

typedef int element;
struct tree{
	struct tree* llink;
	element data;
	struct tree* rlink;
};

struct tree n3={NULL,1,NULL};
struct tree n2={&n3, 3,NULL};
struct tree n1={&n2, 5,NULL};

struct tree* search1(struct tree* root, element key){//재귀함수 
	if(root==NULL){
		printf("트리에 찾는 값이 없습니다.");
		return NULL; 
	}
	
	if(root->data==key) return root; 
	else if(root->data<key) search1(root->rlink, key);
	else search1(root->llink, key);
} 

struct tree* search2(struct tree* root, element key){//반복문 
	while(root!=NULL){
		if(root->data==key)return root;
		else if(root->data<key) root=root->rlink;
		else root=root->llink; 
	}
	printf("트리에 찾는 값이 없습니다.");
	return NULL; 
}

int main(void){
	struct tree* a=search1(&n1,3);
	printf("%d", a->data);	
} 


