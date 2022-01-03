#include <iostream>
#include<algorithm>
#include <vector>
using namespace std;
class Person
{
	public:
		char name[10];
		int marks;
		int rollno;
		bool operator==(const Person& i1)
		{
			if (rollno==i1.rollno)
			return 1;
			return 0;
		}
		bool operator<(const Person& i1)
		{
			if(rollno<i1.rollno)
			return 1;
			return 0;
		}
};

vector<Person>o1;
void print(Person& i1);
void display();
void insert();
void search();
void dlt();

bool compare(const Person &i1,const Person &i2)
{
	//if(i1.name!=i2.name) return i1.marks<i2.marks;
	return i1.marks<i2.marks;
}

int main()
{
	int ch;
	do
	{
	  cout<<"\n**MENU**";
      cout<<"\n1.Insert";
      cout<<"\n2.Display";
      cout<<"\n3.Sort";
      cout<<"\n4.Search";
      cout<<"\n5.Exit";
      cout<<"\nEnter your choice: ";
      cin>>ch;
	
	switch(ch){
		case 1: insert();
		         break;
		case 2: display();
		         break;
		case 3: search();
		         break;
		case 4: sort(o1.begin(),o1.end(),compare);
		        cout<<"\n Sorted on marks";
		        display();
		        break;
		case 5: dlt();
		        break;
		case 6: exit(0);
	}
	}while(ch!=7);
	return 0;
}

void insert()
{
	Person i1;
	cout<<"\nEnter person name: ";
	cin>>i1.name;
	cout<<"\nEnter person marks: ";
	cin>>i1.marks;
	cout<<"\n Enter person roll no.: ";
	cin>>i1.rollno;
	o1.push_back(i1);
}

void display()
{
	for_each(o1.begin(),o1.end(),print);
}

void print(Person& i1)
{
	cout<<"\n";
	cout<<"\nPerson name: "<<i1.name;
	cout<<"\nPerson marks: "<<i1.marks;
	cout<<"\nPerson roll no.: "<<i1.rollno;
}

void search()
{
	vector<Person>::iterator p;
	Person i1;
	cout<<"\nEnter Person rollno to search";
	cin>>i1.rollno;
	p=find(o1.begin(),o1.end(),i1);
	if(p==o1.end())
	{
		cout<<"\nNot Found";
	}
	else
	{
		cout<<"\nFound";
	}
}

void dlt()
{
	vector<Person>::iterator p;
	Person i1;
	cout<<"\nEnter person roll no. to delete: ";
	cin>>i1.rollno;
	p=find(o1.begin(),o1.end(),i1);
	if(p==o1.end())
	{
		cout<<"\nNot Found";
	}
	else
	{
		o1.erase(p);
		cout<<"\nDeleted";
	}
}