/*****************************************
*   UVA #572 : Mapping the Route          *
*   Labels   : dfs, implementation        *
******************************************/


#include <iostream>

using namespace std;

bool dfs(int i, int j, int ct, int rows, int cols, int arr[12][12], int res[12][12], int end_row, int end_col){

  // only check those unvisited
  if(res[i][j]==0){

    res[i][j] = ct;

    // reached goal
    if(i==end_row && j==end_col){
      return true;
    }

    // west
    if(j>0 && !(arr[i][j-1]%2) && dfs(i, j-1, ct+1, rows, cols, arr, res, end_row, end_col)){
      return true;
    }

    // north
    if(i>0 && arr[i-1][j]<2 && dfs(i-1, j, ct+1, rows, cols, arr, res, end_row, end_col)){
      return true;
    }

    // east
    if(!(arr[i][j]%2) && j<cols-1 && dfs(i, j+1, ct+1, rows, cols, arr, res, end_row, end_col)){
      return true;
    }

    // south
    if(arr[i][j]<2 && i<rows-1 && dfs(i+1, j, ct+1, rows, cols, arr, res, end_row, end_col)){
      return true;
    }

    // visited but not in path
    res[i][j] = -1;
  }
  return false;
}

int main(){

  int rows, cols, start_row, start_col, end_row, end_col, maze=0;

  cin >> rows >> cols >> start_row >> start_col >> end_row >> end_col;

  while(rows){
    maze++;
    end_row--;
    end_col--;
    start_row--;
    start_col--;

    int arr[12][12], res[12][12]={};

    for(int i=0; i<rows; i++){
      for(int j=0; j<cols; j++){
        cin >> arr[i][j];
      }
    }

    dfs(start_row, start_col, 1, rows, cols, arr, res, end_row, end_col);

    
    // print

    cout << "Maze " << maze << endl << endl;

    cout << "+";
    for(int j=0; j<cols; j++){
      cout << "---+";
    }cout << endl;

    for(int i=0; i<rows; i++){
      cout << "|";
      for(int j=0; j<cols; j++){
	if(res[i][j]==-1){
	  cout << "???";
	}else if(!res[i][j]){
	  cout << "   ";
        }else{
	  if(res[i][j]<100){
	    cout << " ";
	    if(res[i][j]<10){
	      cout << " ";
	    }
          }
          cout << res[i][j];
	}
	if(arr[i][j]%2 || j==cols-1){
	  cout << "|";
	}else{
          cout << " ";
	}
      }cout << endl << "+";
      for(int j=0; j<cols; j++){
	if(arr[i][j]>1 || i==rows-1){
	  cout << "---";
	}else{
          cout << "   ";
	}
	cout << "+";
      }cout << endl;
    }
    cout << endl << endl;

    cin >> rows >> cols >> start_row >> start_col >> end_row >> end_col;
  }
  return 0;
}