#include<iostream>
#include<cstring>
#include<string>
#include<stack>
using namespace std;

//precedence order
int pre(char ch)
{
    switch (ch)
    {
        case '/':
	    case '*': return 2;
	    case '+':
	    case '-': return 1;
	    default : return 0;
    }
}

// function to convert infix to postfix
void itop (char ifx[] , char pfx[] , int size)
{
    stack <char> s;
    int w;
    int i = 0;
    int k = 0;
    char ch;
    while (i < size)
    {
        ch = ifx[i];
        if (ch == '(')
        {
            s.push(ch);
            i++;
            continue;
        }
        if (ch == ')')
        {
            while (!s.empty() && s.top() != '(')
            {
                pfx[k++] = s.top();
                s.pop();
            }
            if (!s.empty())
            {
                s.pop();
            }
            i++;
            continue;
        }
        w = pre(ch);
        if (w == 0)
        {
            pfx[k++] = ch;
        }
        else
        {
            if (s.empty())
            {
                s.push(ch);
            }
            else
            {
                while (!s.empty() && s.top() != '(' && w <= pre(s.top()))
                {
                    pfx[k++] = s.top();
                    s.pop();
                }
                s.push(ch);
            }
        }
        i++;
    }
    while (!s.empty())
    {
        pfx[k++] = s.top();
        s.pop();
    }
    pfx[k] = 0;
}

// Main function
int main()
{
    char ifx[100];
    cout<<"Enter infix operatiion:"<<endl;
    cin>>ifx;
    int size = strlen(ifx);
    char pfx[size];
    itop(ifx,pfx,size);
    cout<<"Infix expression:"<<ifx<<endl;
    cout<<"Postfix expression:"<<pfx<<endl;
    return 0;
}