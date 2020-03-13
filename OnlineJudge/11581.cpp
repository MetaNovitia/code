/*****************************************
*   UVA #10038 : Grid Successors          *
*   Labels     : Ad Hoc                   *
******************************************/

#include <string>
#include <iostream>

using namespace std;

int main()
{
  int n;
  cin >> n;

  for(int i=0; i<n; i++){
    string v[3];
    int l=-1;
    cin >> v[0] >> v[1] >> v[2];
    if(v[0]=="000" && v[1]==v[0] && v[2]==v[0]){
      l=-1;
    }else{
      int arr[3][3]={};
      for(int j=0; j<3; j++){
        for(int k=0; k<3; k++){
          if(v[j][k]=='1'){
            arr[j][k]=1;
          }
        }
      }

      bool cont=true;
      while(cont){
        cont=false;
        int a[3][3]={};
        if((arr[0][1]+arr[1][0])%2){
          cont=true;
          a[0][0]=1;
        }
        if((arr[0][0]+arr[1][1]+arr[0][2])%2){
          cont=true;
          a[0][1]=1;
        }
        if((arr[0][1]+arr[1][2])%2){
          cont=true;
          a[0][2]=1;
        }
        if((arr[0][0]+arr[1][1]+arr[2][0])%2){
          cont=true;
          a[1][0]=1;
        }
        if((arr[0][1]+arr[1][0]+arr[1][2]+arr[2][1])%2){
          cont=true;
          a[1][1]=1;
        }
        if((arr[0][2]+arr[1][1]+arr[2][2])%2){
          cont=true;
          a[1][2]=1;
        }
        if((arr[2][1]+arr[1][0])%2){
          cont=true;
          a[2][0]=1;
        }
        if((arr[2][0]+arr[1][1]+arr[2][2])%2){
          cont=true;
          a[2][1]=1;
        }
        if((arr[2][1]+arr[1][2])%2){
          cont=true;
          a[2][2]=1;
        }
        for(int j=0; j<3; j++){
          for(int k=0; k<3; k++){
            arr[j][k]=a[j][k];
          }
        }
        l++;
      }
    }
    
    cout << l << endl;
  }

  return 0;
}
