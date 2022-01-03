#include <iostream>
using namespace std;

#define size 10
template <class T>

void sel (T A[size] , int n)
{
    int i,j,min;
    
    T temp;
    for (i=0; i<n-1; i++)
    {
        min = i;
        for (j=i+1; j<n; j++)
        {
            if (A[j] < A[min])
            {
                min = j;
            }
        }
        temp = A[i];
        A[i] = A[min];
        A[min] = temp;
    }
    cout<<"Sorted array:"<<endl;
    for (i=0; i<n; i++)
    {
        cout<<"  "<<A[i];
    }
}

int main()
{
    int A[size];
    float B[size];
    int i;
    
    cout<<"Enter total no of elements:"<<endl;
    cin>>n;
    cout<<"Enter int type elements:"<<endl;
    for (i=0; i<n; i++)
    {
        cin>>A[i];
    }
    sel(A , n);
    
    cout<<"Enter total no of float elements:"<<endl;
    cin>>n;
    cout<<"Enter float type elements:"<<endl;
    for (i=0; i<n; i++)
    {
        cin>>B[i];
    }
    sel(B , n);
}