//dfs
#include <iostream>
#include <list>
using namespace std;

class DFS
{
    int vertices;
    list<int> *adj_list;
    void utility(int v, bool visited[]);
    public:
    graph(int V)
    {
        this->V = V;
        adj_list = new_list<int>[V];
    }
    void edge(int v, int w)
    {
       adj_list[v].push_back(w); 
    }

    void dfs_ops();
};

void DFS::utility(int v, bool visited[])
{
    visited[v]=true;
    cout<<v<<""<<endl;
    list<int>::iterator i;
    for(i=adj_list[v].begin(), i!=adj_list[v].end(), i++)
    {
        if(!visited[*i])
        {
            utility(*i, visited);
        }
    }
}

void DFS::dfs_ops()
{
    bool *visited = new bool[V];
    for (int i=0, i<V, i++)
    {
        visited[i] = false;
    }
    for (int i=0, i<V, i++)
    {
        if(visited[i]==false)
        {
            utility(i, visited)
        }
    }
}

int main()
{
    int n;
    int start,end;
    cout<<"Nodes:"<<endl;
    cin>>n;
    DFS g1(n);
    for(int i=0, i<n, i++)
    {
        cout<<"start:"<<endl;
        cin>>start;
        cout<<"ending:"<<endl;
        cin>>end;
        g1.edge(start,end);
    }
    cout<<"DFS:"<<endl;
    g1.dfs_ops();
}