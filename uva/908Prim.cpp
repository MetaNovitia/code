/*********************************************
*   UVA #908 : Re-connecting Computer Sites   *
*   Labels   : MST (Prim's)		      *
**********************************************/

#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <queue>
#include <functional>
#include <utility>

using namespace std;

typedef pair<int, int> PII;

int main(){
  int n, k, m, sum, x, y, c;
  vector<int> v(3,0);
  bool notFirst=false;
  priority_queue< PII, vector<PII>, greater<PII> > Q;
  ofstream out("results.txt");  // for testing
  
  while(cin >> n){

    // formatting purposes
    if(notFirst){out << endl;}
    
    vector<PII> newT[n+1];
    bool vis[n+1];
    for(int i=0; i<=n; i++){
      vis[i]=false;
    }

    // original sum
    sum = 0;
    for(int i=0; i<n-1; i++){
      cin >> x >> y >> c;
      sum+=c;
    }
    out << sum << endl;
    sum = 0;
    for(int j=0; j<2; j++){
      cin >> k;
      for(long long i=0; i<k; i++){
        cin >> v[0] >> v[1] >> v[2];
	newT[v[0]].push_back(make_pair(v[2], v[1]));
        newT[v[1]].push_back(make_pair(v[2], v[0]));
      }
    }

    Q.push(make_pair(0, 1));
    while(!Q.empty()){
      int a = Q.top().second;
      int c = Q.top().first;
      Q.pop();
      if(!vis[a]){
        vis[a] = true;
        sum += c;
        for(int i = 0; i < newT[a].size(); i++){
          if(!vis[newT[a][i].second]){
            Q.push(newT[a][i]);
	  }
        }
      }
    }
    out << sum << endl;
    notFirst=true;
    
  }
  return 0;
}