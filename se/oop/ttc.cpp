#include <iostream>
using namespace std;

int main()
{
    int x = -1;
    cout << "x is less than 0" << endl;
    try
    {
        cout << "This is inside try" << endl;
        if (x < 0)
        {
            throw x;
            cout << "This sttatement will never be printed" << endl;
        }
    }
    catch (int x)
    {
        cout << "The exception is caught" << endl;
    }
    cout << "After the catch , this statement will be printed" << endl;
    return 0;
}