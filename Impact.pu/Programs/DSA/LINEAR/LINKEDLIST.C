#include <stdio.h>
#include <stdlib.h>
struct node{
    int val;
    struct node *next;
};
typedef struct node NODE;
NODE *temp = NULL, *head = NULL;
void dispList(NODE *);
void insertAtEnd();
void insertAtBeggining();
int findVal(NODE *, int );
int main(){
    int opt = 1;
    int value;
    while (opt){
        printf("\n1.Insert At Beggining\n2.Insert At End\n3.Display\n4.Find Value");
        scanf("%d", &opt);
        switch (opt){
        case 1:
            insertAtBeggining();
            break;
        case 2:
            insertAtEnd();
            break;
        case 3:
            dispList(head);
            break;
        case 4:
            printf("Enter the value you want to find: ");
            scanf("%d", &value);
            printf("%d",findVal(head, value));
            break;
        case 0:
            break;
        }
    }
    return 0;
}
void dispList(NODE *t){
    while (t!=NULL){
        printf("(%d)-->", t->val);
        t = t->next;
    }
    printf("NULL");
}
void insertAtEnd(){
    NODE * newNode;
    newNode = (NODE *)malloc(sizeof(NODE));
    printf("Enter the value of New Node: ");
    scanf("%d", &newNode->val);
    newNode->next = NULL;
    if (head == NULL){
        head = newNode;
        temp = head;
    }
    else{
        while (temp->next!=NULL){
            temp = temp->next;
        }
        temp->next = newNode;
    }
}
void insertAtBeggining(){
    NODE * newNode;
    newNode = (NODE *)malloc(sizeof(NODE));
    printf("Enter the value of New Node: ");
    scanf("%d", &newNode->val);
    newNode->next = NULL;
    if(head==NULL){
        head=newNode;
        temp=head;
    }
    else{
        newNode->next=head;
        head=newNode;
    }
}
int findVal(NODE *t, int value){
    int flag=0;
    while(t){
        if(t->val==value){
            return 1;
        }
        t=t->next;
    }
    return 0;
}