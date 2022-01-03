#include <iostream> 
#include <vector>

#define ll long long

#define endl "\n"

using namespace std;

int main() 
{
    vector<int> marks;
	int N;
	
	cout << "Enter Number of Students : ";
	
	cin >> N;
	
	cout << endl << "Enter Marks of Students : ";
	
	for(int i = 0; i < N; i++)
        {
	        int m;
	        cin >> m;
	        marks.push_back(m);
	    }
	
	cout << endl << "The marks are : ";
	for(int i = 0; i < N; i++)
        {
	        cout << marks[i] << " ";
	    }
	
	return 0;
}