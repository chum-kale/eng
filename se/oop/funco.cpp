#include <iostream>
using namespace std;

void print (int a)
{
    cout <<"This is integer type"<< a <<endl;
}

void print (float f)
{
    cout<< " Ths is float type"<< f <<endl;
}

void print (char const *c)
{
    cout << "This is character type"<< c <<endl;
}

int main()
{
    print(4);
    print(4.44);
    print('c');
    return 0;
}