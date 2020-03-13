/*****************************************
*   UVA #11857 : Driving Range            *
*   Labels     : MST (Kruskal's)          *
******************************************/


#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;

bool compareRoad(vector<int> i, vector<int> j){return i[2]<j[2];}

int root(int x, int id[]){
    while(id[x] != x){
        id[x] = id[id[x]];
        x = id[x];
    }
    return x;
}


int main(){
  int n,m;
  ofstream out("results.txt");  // For Testing
  vector<int> v(3,0);
  cin >> n >> m;

  while(n){

    vector<vector <int> > roads;  // holds road (edge) data
    int id[n];			  // holds root data
    for(int i = 0;i < n;i++){
      id[i] = i;
    }
    
    for(int i=0; i<m ; i++){
      cin >> v[0] >> v[1] >> v[2];
      roads.push_back(v);
    }

    // greedy, takes cheapest roads first
    sort(roads.begin(), roads.end(), compareRoad);

    int pt = 0, ct = 0;
    while(pt<m){
      
      // get the root of each city
      int x = root(roads[pt][0], id);
      int y = root(roads[pt][1], id);

      // not equal root (no cycle)
      if(x!=y){
	id[x] = id[y];
	ct++;
      }

      // when all cities taken into account
      if(ct==n-1){
        cout << roads[pt][2] << endl;
	break;
      }

      pt++;
    }

    if(ct!=n-1){
      cout << "IMPOSSIBLE" << endl;
    }
    cin >> n >> m;
  }
  return 0;
}
