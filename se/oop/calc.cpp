#include <iostream>

using namespace std;
// creation of class
class calci
{
    public:
    int n1 , n2;
    calci (int a, int b)
    {
        n1=a;
        n2=b;
    }
    void display()
    {
        cout<<"No 1:"<<n1<<endl;
        cout<<"No 2:"<<n2<<endl;
    }
    void addition();
    void subtraction();
    void division();
    void multiplication();
};
// functions of the calcuilator
void calci :: addition()
{
    int ans;
    ans = n1 + n2;
    cout<<"Sum is:"<<ans<<endl;
}
void calci :: subtraction()
{
    int ans;
    ans = n1- n2;
    cout<<"Difference is:"<<ans<<endl;
}
void calci :: division()
{
    int ans;
    ans = n1/n2;
    cout<<"Quotient is:"<<ans<<endl;
}
void calci :: multiplication()
{
    int ans;
    ans = n1 * n2;
    cout<<"Product is:"<<ans<<endl;
}
// Main working of calculator by taking input
int main()
{
    int a,b;
    char opt;
    char c;
    cout<<"Enter first number:"<<endl;
    cin>>a;
    cout<<"Enter second number:"<<endl;
    cin>>b;
    calci calc(a, b);
    calc.display();
    do
    {
        cout<<"Enter your choice \n '+' for addition \n '-' for subtraction \n '/' for division \n '*' for multiplication"<<endl;
        cin>>opt;
        switch (opt)
        {
            case '+' : calc.addition();
            break;
            case '-' : calc.subtraction();
            break;
            case '/' : calc.division();
            break;
            case '*' : calc.multiplication();
            break;
            default:
            cout<<"Please try again"<<endl;
        }
        cout<<"Press y to continue , or s to stop"<<endl;
        cin>>c;            
    } while(c=='y');
} 
    
    

