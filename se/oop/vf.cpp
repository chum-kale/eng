#include <iostream>
using namespace std;

class parent
{
    public:
    virtual void show()
    {
        cout << "This is parent class"<< endl;
    }
    void test()
    {
        cout << "This is a test function(parent class)" << endl;
    }
};

class child : public parent
{
    public:
    void show()
    {
        cout << "This is child class" << endl;
    }
    void test()
    {
        cout << "This is a test function(child class)" << endl;
    }
};

int main()
{
    parent *pptr;
    child c;
    pptr = &c;

    //virtual function
    pptr -> show();
    //non-virtual function
    pptr -> test();
    return 0;
}