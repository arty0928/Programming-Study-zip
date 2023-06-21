#include<stdio.h>
#include<stdio.h>

typedef int element;
struct tree{
	struct tree* llink;
	element data;
	struct tree* rlink;
};

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

void insert(struct tree** root,element value){
	struct tree* newn=(struct tree*)malloc(sizeof(struct tree));
	newn -> data= value;
	newn -> rlink=NULL;
	newn ->llink=NULL;
	if(root==NULL) *root=newn;	
	 
}





