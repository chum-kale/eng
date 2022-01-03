#include <iostream>
using namespace std;

//declaring template
template <typename T>
T Mmin (T x , T y)
{
   return (x < y) ? x : y; 
}

int main()
{
    cout << "For integer" << Mmin<int> (9 , 3) << endl;
    cout << "For float" << Mmin<float> (8.5 , 6.4) << endl;
    cout << "For chararcters" << Mmin<char> ('h' , 'y') << endl;
    return 0;
}