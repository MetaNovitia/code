/*********************************************
*   UVA #908 : Re-connecting Computer Sites   *
*   Labels   : MST (Kruskal's)		      *
**********************************************/

#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;

bool vectComp (vector<int> i,vector<int> j) { return (i[2]<j[2]); }

int root(int x, int id[]){
    while(id[x] != x){
        id[x] = id[id[x]];
        x = id[x];
    }
    return x;
}

int main(){
  long long n, k, m, sum, x, y, c;
  vector<int> v(3,0);
  bool notFirst=false;
  ofstream out("results.txt");  // for testing
  
  while(cin >> n){

    // formatting purposes
    if(notFirst){cout << endl;}

    vector<vector<int> > newT;
    int id[n+1];
    for(int i = 0;i < n+1;i++){
      id[i] = i;
    }

    // original sum
    sum = 0;
    for(long long i=0; i<n-1; i++){
      cin >> x >> y >> c;
      sum+=c;
    }
    cout << sum << endl;

    for(int j=0; j<2; j++){
      cin >> k;
      for(long long i=0; i<k; i++){
        cin >> v[0] >> v[1] >> v[2];
        newT.push_back(v);
      }
    }

    sort(newT.begin(), newT.end(), vectComp);
    
    sum=0;
    for(int i=0; i<newT.size(); i++){
      x = root(newT[i][0], id);
      y = root(newT[i][1], id);
      if(x!=y){
	id[x]=id[y];
        sum+=newT[i][2];
      }
    }
    cout << sum << endl;
    notFirst=true;
    
  }
  return 0;
}