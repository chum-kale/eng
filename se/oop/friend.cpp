#include <iostream>
using namespace std;

class circle
{
    private:
    int r;
    public:
    circle () : r(0)
    {}
    friend int showrad(circle);
};

int showrad (circle c)
{
    c.r += 5;
    return c.r;
}

int main()
{
    circle c;
    cout << "Radius is:" << showrad(c) << endl;
    return 0;
}