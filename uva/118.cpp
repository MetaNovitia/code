/*******************************************
*   UVA #118   : Mutant Flatworld Explorers *
*   Labels     : Graph Traversal            *
********************************************/


#include <iostream>
#include <fstream>

using namespace std;

int main(){
  // VARIABLES
  int length, height, x, y, d;
  string instructions, dir="NESW";
  char direction;
  bool off[51][51]={};

  cin >> length >> height;
  while(cin >> x){
    cin >> y >> direction >> instructions;
    string l = "";

    // set direction
    d = 0;
    while(dir[d]!=direction){d++;}

    for(int i=0; i<instructions.length(); i++){
      if(instructions[i]=='L'){
	d = (((d-1) % 4) + 4) % 4;
      }else if(instructions[i]=='R'){
	d = (d+1) % 4;
      }else{
        int newX=x,newY=y;
	if(d%2==0){
	  if(d==0){
	    newY+=2;
	  }
	  newY--;
	}else{
	  if(d==1){
	    newX+=2;
	  }
	  newX--;
	}
	if(newX<0 || newX>length || newY<0 || newY>height){
	  if(!off[x][y]){
	    l = " LOST";
	    off[x][y]=true;
	    break;
	  }
	}else{
	  x = newX; y = newY;
	}
      }
      
    }
    cout << x << " " << y << " " << dir[d] << l << endl;
  }
  return 0;
}