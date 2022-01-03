#include <iostream>
using namespace std;

struct Node
{
	int data;
	Node *next;

};

void insertion(Node *head)
{
	Node *newnode = new Node();
	newnode->data = rollno;
	newnode-> next = NULL;
	Node *temp = head;
	while(temp->next!=NULL)
	{
		temp = temp->next;

	}
	temp->next = newnode;

}

void display(Node *head)
{
	Node *temp = head;
	while(temp != NULL)
	{
		cout << temp->data <<"";
		temp = temp->next;
	}
}
void deletion_node(Node *&head)
{
	cout<< " Enter the position of element to be deleted";
	int position;
	cin>>position;
	Node *temp = head;
	int counter = 0;
	while(counter !=position-1)
	{
		temp =temp->next;

	}
	temp->next= temp->next->next;
	delete temp->next:
}

int main() {
	Node *head1 = new Node();
	cout<<"enter the head value of the first list";
	cin>> head1->data;
	head1->next= NULL;

	Node *head2 = new Node();
	cout<<"enter the head value of the first list";
		cin>> head2->data;
		head2->next= NULL;

		int vanilla;
		cout<< " Enter the number of students who like vanilla";
		cin>> vanilla;
		for(int i = 0;i< vanilla;i++)
		{
			insertion(head1);

		}
		cout << "First list is ";
		display(head1);
		cout << "Second  list is ";
		display(head2);

		int butterscotch;
				cout<< " Enter the number of students who like butterscotch";
				cin>> vanilla;
				for(int i = 0;i< butterscotch;i++)
				{
					insertion(head1);

				}
				cout << "First list is ";
				display(head1);
				cout << "Second  list is ";
				display(head2);

};