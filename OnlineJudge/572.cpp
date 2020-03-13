/*********************************************
*   UVA #572 : Oil Deposits                   *
*   Labels   : bfs/dfs, connected components  *
**********************************************/

#include <iostream>

using namespace std;

void dfs(int i, int j, bool arr[102][102]){
  if(arr[i][j]){
    arr[i][j] = false;
    dfs(i-1,j-1,arr);
    dfs(i-1,j,arr);
    dfs(i-1,j+1,arr);
    dfs(i,j-1,arr);
    dfs(i,j+1,arr);
    dfs(i+1,j-1,arr);
    dfs(i+1,j,arr);
    dfs(i+1,j+1,arr);
  }
}

int main(){
  int m,n;
  string s;
  cin >> m >> n;
  while(m){
    bool arr[102][102]={};
    int ct=0;
    for(int i=0; i<m; i++){
      cin >> s;
      for(int j=0; j<n; j++){
	if(s[j]=='@'){
	  arr[i+1][j+1] = true;
	}
      }
    }

    for(int i=1; i<=m; i++){
      for(int j=1; j<=n; j++){
	if(arr[i][j]){
	  ct++;
	  dfs(i,j,arr);
	}
      }
    }
    cout << ct << endl;
    cin >> m >> n;
  }
  return 0;
}