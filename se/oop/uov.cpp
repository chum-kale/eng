#include <iostream>
using namespace std;

class test
{
    private:
    int a;

    public:
    test() : a(10)
    {} 

    //overload -- as prefix
    void operator -- ()
    {
        --a;
    }
    void display()
    {
        cout <<"value is:"<<a<<endl;
    }
};

int main()
{
    test t;
    --t;
    t.display();
    return 0;
}