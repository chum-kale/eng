#include <iostream>
using namespace std;
class pr //personal record
{
    public:
    string name;
    string adr;
    string g;
    void getpr()
    {
        cout<<"Enter name:"<<endl;
        cin>>name;
        cout<<"Enter address:"<<endl;
        cin>>adr;
        cout<<"Enter Gender:"<<endl;
        cin>>g;
    }
    
};
class pd //professional details
{
    public:
    int exp;
    void getpd()
    {
        cout<<"Total Expirience:"<<endl;
        cin>>exp;
    }
   
};
class ed //education details
{
    public:
    float cbse;
    float hsc;
    float be;
    void geted()
    {
        cout<<"Enter CBSE marks:"<<endl;
        cin>>cbse;
        cout<<"Enter HSC marks:"<<endl;
        cin>>hsc;
        cout<<"Enter BE marks:"<<endl;
        cin>>be;
    }
    
};
class biodata : public pr , public pd , public ed
{
    public:
    void displaybd()
    {
        cout<<"**********BIODATA**********"<<endl;
        cout<<"Personal data"<<endl;
        cout<<"Name:"<<name<<endl;
        cout<<"Address:"<<adr<<endl;
        cout<<"Gender:"<<g<<endl;

        cout<<"Professional data:"<<endl;
        cout<<"Total Expirience:"<<exp<<endl;
        
        cout<<"Educational data:"<<endl;
        cout<<"CBSE Marks:"<<cbse<<endl;
        cout<<"HSC marks:"<<hsc<<endl;
        cout<<"Graduation marks:"<<be<<endl;
    }
};
int main()
{
    biodata b;
    b.getpr();
    b.getpd();
    b.geted();
    b.displaybd();

    return 0; 
}