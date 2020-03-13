#include <math.h> 
#include <iostream> 
#include <iomanip>
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

int myComp(const void* a, const void* b)  
{  
    Edge* a1 = (Edge*)a;  
    Edge* b1 = (Edge*)b;  
    return a1->weight > b1->weight;  
} 

double root(int x, int roots[]){
    while(roots[x] != x){
        roots[x] = roots[roots[x]];
        x = roots[x];
    }
    return x;
}

double KruskalMST(Graph* graph){
    
    qsort(graph->edge, graph->E, sizeof(graph->edge[0]), myComp);

    int roots[graph->V];
    for(int i=0; i<graph->V; i++) roots[i] = i;
    double cost = 0;
    
    for(int i=0; i<graph->E; i++){
        int x = root(graph->edge[i].src, roots);
        int y = root(graph->edge[i].dest, roots);
        
        if(x!=y){
            roots[x] = roots[y];
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

    cout << setprecision(8) << KruskalMST(graph) << endl;
  
    return 0;  
}  