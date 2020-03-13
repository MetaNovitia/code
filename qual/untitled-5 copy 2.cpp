#include <math.h> 
#include <iostream> 
#include <iomanip>
#include <vector>
using namespace std; 

class Edge  
{  
    public: 
    long src, dest;
    long double weight;  
};  

class Graph  
{  
    public: 
    int V, E;  
    Edge* edge;  
};  

Graph* createGraph(int V, int E)  
{  
    Graph* graph = new Graph;  
    graph->V = V;  
    graph->E = E;  
    graph->edge = new Edge[E];  
    return graph;  
}  

int comp(const void* a, const void* b)  
{  
    Edge* a1 = (Edge*)a;  
    Edge* b1 = (Edge*)b;  
    return a1->weight > b1->weight;  
}

double kruskal(Graph* graph){
    
    qsort(graph->edge, graph->E, sizeof(graph->edge[0]), comp);
    int inside[graph->V];
    vector<int> tree[graph->V];
    for(int i=0; i<graph->V; i++){
	inside[i] = i;
	tree[i].push_back(i);
    }
    double cost = 0;

    for(int i=0; i<graph->E; i++){
        int x = graph->edge[i].src;
        int y = graph->edge[i].dest;

        
        if(inside[x]!= inside[y]){
	    if(tree[inside[x]].size()>tree[inside[y]].size()){
		int temp=x;x=y;y=temp;
	    }
	    int nd = inside[x], st = inside[y];
	    for(int j=0; j<tree[nd].size(); j++){
		inside[tree[nd][j]] = st;
		tree[st].push_back(tree[nd][j]);
	    }
            cost += graph->edge[i].weight;
        }
    }
            
    return cost;
}



int main()  
{
    int n,ct=0;
    cin >> n;

    Graph* graph = createGraph(n, n*(n-1)/2);

    long arr[n][3];
    cin >> arr[0][0] >> arr[0][1] >> arr[0][2];

    for(int i=1; i<n; i++){
        cin >> arr[i][0] >> arr[i][1] >> arr[i][2];
        for(int j=0; j<i; j++){
            graph->edge[ct].src = i;
            graph->edge[ct].dest = j;
            graph->edge[ct].weight = 
                sqrt(((arr[i][0]-arr[j][0])*(arr[i][0]-arr[j][0])) +
                     ((arr[i][1]-arr[j][1])*(arr[i][1]-arr[j][1])))
                - arr[i][2] - arr[j][2];
            ct++;
        }
    }

    cout << setprecision(8) << kruskal(graph) << endl;
  
    return 0;  
}  