# include <iostream>
using namespace std;
class student
{
    public:
    string bg;
    string name;
    string db;
    int rn;
    static int counter;
    student()
    {
        rn=0;
        counter++;
    }
    student (int rn)
    {
        this ->rn = rn;
        counter++;
    }
    student (student &obj)
    {
        rn = obj.rn;
        name = obj.name;
        bg = obj.bg;
        cls = obj.cls;
        div = obj.div;
        tel = obj.tel;
        counter++;
    }
    ~ student()
    {
        cout<<"Object Deleted"<<endl;
        counter--;
    }
    static void dis_counter()
    {
        cout<<"No of objects in the program are:"<<counter<<endl;
    }
    void add();
    friend void display(student &obj);
};
void student :: add()
{
    cout<<"Enter roll number:"<<endl;
    cin>>rn;
    cout<<"Enter name:"<<endl;
    cin>>name;
    cout<<"Enter Blood group:"<<endl;
    cin>>bg;
}
void display (student &obj)
{
    cout<<"Roll No:"<<obj.rn<<endl;
    cout<<"Name:"<<obj.name<<endl;
    cout<<"Blood Group:"<<obj.bg<<endl;
}
int student :: counter=0;
int main()
{
    student s1;
    student s2(101);
    s2.add();
    student s3(s2);
    display(s2);
    display(s3);
    student :: dis_counter();
    int n,i;
    student *s[50];
    cout<<"Enter number of students in class:"<<endl;
    cin>>n;
    for (i=0; i<n; i++)
    {
        s[i] = new student();
    }
    for (i=0; i<n; i++)
    {
        s[i] -> add();
    }
    for (i=0; i<n; i++)
    {
        display (*s[i]);
    }
    student :: dis_counter();
    for (i=0; i<n; i++)
    {
        delete s[i];
    }
    return 0;
}
    
