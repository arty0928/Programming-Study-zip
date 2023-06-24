#include <stdio.h>
#include <stdlib.h>
#define N 5

typedef struct {
    char name[50]; //이름
    int student_no; //학번
} element;

element queue[N];
int front = 0;
int rear = 0;

int isFull() {
    //rear로 넣을 그 다음 위치가 front와 같으면 포화
    if ((front == (rear + 1)%N)) //한칸 띄움
        return 1;
    else
        return 0;
}

int isEmpty() {
    if (front == rear)
        return 1;
    else
        return 0;
}

void qinsert(element value) {
    if (isFull()) {
        printf("queue overflow\n");
    } else {
        queue[++rear%N] = value;
        printf("Enqueued: %s\n", value.name);
    }
}

element qdelete() {
    element value;
    if (isEmpty()) {
        printf("Queue is empty. Cannot qdelete element.\n");
        return value;
    } else {
        value = queue[++front%N];
        printf("Dequeued: %s\n", value.name);
        return value;
    }
}

int main() {
    element e1 = {"John", 123};
    element e2 = {"Alice", 456};
    element e3 = {"Bob", 789};

    qinsert(e1);
    qinsert(e2);
    qinsert(e3);

    element dequeuedElement = qdelete();

    return 0;
}
