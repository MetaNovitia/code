#include <iostream> 
#include <math.h> 
#include <iomanip>
#include <vector>
using namespace std; 

class Edge{  
public: 
    long s, d;
    long double w;  
};  

class Graph{  
public:
    int n, m;  
    Edge* e;  
};  

Graph* init(int n, int m){  
    Graph* g = new Graph;  
    g->n = n;  
    g->m = m;  
    g->e = new Edge[m];  
    return g;  
}  

int comp(const void* a, const void* b){
    return ((Edge*) a)->w > ((Edge*) b)->w;  
}

double kruskal(Graph* g){
    
    qsort(g->e, g->m, sizeof(g->e[0]), comp);
    int inside[g->n];
    vector<int> tree[g->n];
    for(int i=0; i<g->n; i++){
	inside[i] = i;
	tree[i].push_back(i);
    }
    double cost = 0;

    for(int i=0; i<g->m; i++){
        int x = g->e[i].s;
        int y = g->e[i].d;

        
        if(inside[x]!= inside[y]){
	    if(tree[inside[x]].size()>tree[inside[y]].size()){
		int temp=x;x=y;y=temp;
	    }
	    int nd = inside[x], st = inside[y];
	    for(int j=0; j<tree[nd].size(); j++){
		inside[tree[nd][j]] = st;
		tree[st].push_back(tree[nd][j]);
	    }
            cost += g->e[i].w;
        }
    }
            
    return cost;
}



int main()  
{
    int n,ct=0;
    cin >> n;

    Graph* g = init(n, n*(n-1)/2);

    long arr[n][3];
    cin >> arr[0][0] >> arr[0][1] >> arr[0][2];

    for(int i=1; i<n; i++){
        cin >> arr[i][0] >> arr[i][1] >> arr[i][2];
        for(int j=0; j<i; j++){
            g->e[ct].s = i;
            g->e[ct].d = j;
            g->e[ct].w = 
                sqrt(((arr[i][0]-arr[j][0])*(arr[i][0]-arr[j][0])) +
                     ((arr[i][1]-arr[j][1])*(arr[i][1]-arr[j][1])))
                - arr[i][2] - arr[j][2];
            ct++;
        }
    }

    cout << setprecision(8) << kruskal(g) << endl;
  
    return 0;  
}  