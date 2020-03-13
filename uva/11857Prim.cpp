/*****************************************
*   UVA #11857 : Driving Range            *
*   Labels     : MST (Prim's)             *
******************************************/

/*
THIS CODE IS COPIED FROM https://www.hackerearth.com/practice/algorithms/graphs/minimum-spanning-tree/tutorial/ AND IS ONLY SLIGHTLY MODIFIED
*/

#include <iostream>
#include <vector>
#include <queue>
#include <functional>
#include <utility>
#include <fstream>

using namespace std;
typedef pair<long long, int> PII;

long long prim(int n, int x, vector <PII> adj[], bool marked[])
{
    priority_queue<PII, vector<PII>, greater<PII> > Q;
    int y;
    int ct=0;
    long long maxCost = 0;
    PII p;
    Q.push(make_pair(0, x));
    while(!Q.empty())
    {
        // Select the edge with minimum weight
        p = Q.top();
        Q.pop();
        x = p.second;
        // Checking for cycle
        if(marked[x] == true)
            continue;
        maxCost = max(maxCost, p.first);
        marked[x] = true;
        ct++;
        for(int i = 0;i < adj[x].size();++i)
        {
            y = adj[x][i].second;
            if(marked[y] == false){
                Q.push(adj[x][i]);
	    }
        }
    }
    if(ct==n){return maxCost;}
    return -1;
}

int main()
{
    ofstream out("results.txt");
    int nodes, edges, x, y;
    long long weight, maxCost;
    cin >> nodes >> edges;
    while(nodes){
      bool marked[nodes];
      for(int i=0; i<nodes; i++){
	marked[i]=false;
      }
      vector <PII> adj[nodes];
      for(int i = 0;i < edges;i++)
      {
          cin >> x >> y >> weight;
          adj[x].push_back(make_pair(weight, y));
          adj[y].push_back(make_pair(weight, x));
      }
      // Selecting 1 as the starting node
      int res = prim(nodes, 1, adj, marked);
      if(res!=-1)
      {cout << res << endl;}
      else{cout << "IMPOSSIBLE" << endl;}
      cin >> nodes >> edges;
    }
    return 0;
}