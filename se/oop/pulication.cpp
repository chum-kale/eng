#include <iostream>
using namespace std;
class publication
{
    public:
    string title;
    float price;
    publication()
    {
        title = " ";
        price = 0.0;
    }
    publication (string t, float p)
    {
        title = t;
        price = p;
    }
};
class book : public publication
{
    public:
    int pc;
    book(string t, float p, int c) : publication (t , p)
    {
        pc = c;
    }
    void display()
    {
        cout<<" Title :"<<title<<endl;
        cout<<" Price :"<<price<<endl;
        cout<<" No of pages :"<<pc<<endl;
    }
};
class tape : public publication
{
    public:
    int time;
    tape (string t, float p, int tt) : publication (t , p)
    {
        time = tt;
    }
    void display()
    {
        cout<<" Title: "<<title<<endl;
        cout<<" Price :"<<price<<endl;
        cout<<" Running time :"<<time<<endl;
    }
};
int main()
{
    string t;
    float p;
    int tt;
    int c;
    char choice;
    char opt;
    do
    {
        cout<<" WELCOME \n press B for book \n press T for tape"<<endl;
        cin>>choice;
        switch (choice)
        {   case 'B':  
            {
                cout<<" Enter title: "<<endl;
                cin>>t;
                cout<<" Enter Price:"<<endl;
                cin>>p;
                cout<<" Enter no of pages :"<<endl;
                cin>>c;
                book b (t, p ,c);
                b.display();
            }
            break;
            case 'T':
            {
                cout<<" Enter title: "<<endl;
                cin>>t;
                cout<<" Enter Price:"<<endl;
                cin>>p;
                cout<<" Enter runtime :"<<endl;
                cin>>c;
                tape T (t, p ,tt);
                T.display();
            }
            break;
            default:
            {
                cout<< "Invalid"<<endl;
            }
        }
        cout<<" Press Y to continue "<<endl;
        cin>>opt;
    }
    while (opt == 'Y');
    return 0;
}

      
    
    
