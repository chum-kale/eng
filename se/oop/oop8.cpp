# include <iostream>
# include <string.h>
using namespace std;
class user
{
	public:
	  char vehicle;
	  int salary, age;
	  string city;
		
	  user()
	  {
		  age=0;
		  vehicle=0;
		  salary=0;
	  }
	  void getdata();
};

void user::getdata()
{
	cout<<"Enter age of person: ";
	cin>>age;
	if(age<18||age>55)
	{
		throw 1;
	}
	
	cout<<"Enter salary for per month: ";
	cin>>salary;
	if(salary<50000||salary>100000)
	{
		throw 2;
	}
	
	cout<<"Do you have 4 wheeler (y/n): ";
	cin>>vehicle;
	if(vehicle=='n'||vehicle=='N')
	{
		throw 3;
	}
	
	cout<<"Enter name of city where user stays: ";
	cin>>city;
	if(city=="pune"||city=="mumbai"||city=="bangalore"||city=="chennai")
	{	
	}
	
	else
	{
		throw 4;
	}
}

int main()
{
	user u;
	try
	{
		u.getdata();
	}
	catch(int i)
	{
		switch(i)
		{
			case 1: cout<<"\n Invalid...please enter age between (18-55)";
			        break;
			case 2: cout<<"\n Invalid... please enter salary between (50000-100000)";
			        break;
			case 3: cout<<"\n User does not have four vehicle";
			        break;
			case 4: cout<<"\n Invalid city";
			        break;
		}
	}
	return 0;
}