#include <iostream>
using namespace std;

//base class
class animals
{
    public:
    void describe()
    {
        cout<<"This class represents animals"<<endl;
    }
};

//derived class
class mammal : public animals
{
    public:
    void data()
    {
        cout<<"Mammals are a sub category of animals"<<endl;
    }
};

int main()
{
    mammal m1;
    m1.describe();
    m1.data();
    return 0;
}