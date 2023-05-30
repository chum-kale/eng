#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <stack>
using namespace std;

class graph
{
    int V;
    vector<list<int> > adj;
    public:
    graph (int V);
    void edge(int v, int w);
    void BFS (int s);
    void DFS(int s);
};

graph :: graph(int V)
{
    this -> V;
    adj.resize(V);
}

void graph :: edge(int v, int w)
{
    adj[v].push_back(w);
}

void graph :: BFS(int s)
{
    vector<bool> visited;
    visited.resize(V, false);
    list<int> queue;
    visited[s] = true;
    queue.push_back(s);
    while (!queue.empty())
    {
        s = queue.front();
        cout <<s<<" "<<endl;
        queue.pop_front();
        for (auto adjacent : adj[s])
        {
            if (!visited[adjacent])
            {
                visited[adjacent] = true;
                queue.push_back(adjacent);
            }
        }
    }
}

void graph :: DFS(int s)
{
    vector<bool> visited(V, false);
    visited[s] = true;
    cout << s <<" "<<endl;
    list<int>::iterator i;
    for (i = adj[s].begin(); i != adj[s].end(); ++i)
        if (!visited[*i])
            DFS(*i);
}

int main()
{
    graph g(5); // Total 5 vertices in graph
    g.edge(1, 0);
    g.edge(0, 2);
    g.edge(2, 1);
    g.edge(0, 3);
    g.edge(1, 4);
 
    cout << "Following is Depth First Traversal\n";
    g.DFS(2);

    cout << "BFS is: \n";
    g.BFS(0);
 
    return 0;
}