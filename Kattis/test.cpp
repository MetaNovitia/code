#include <iostream>
#include <string>

using namespace std;

long long npr(int n, int r){
  long long ans=1;
  for(int i=n-r+1; i<=n; i++){
    ans*=i;
  }
  return ans;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  cin >> n >> k;
  
  int
  
  string target, words[n];
  int notTaken[n+1];
  int order[k];

  for(int i=0; i<n; i++){
    notTaken[i+1] = i;
    cin >> words[i];
  }
  cin >> target;

  int i,start, end, ct = 0, pos = 0;
  string t;

  while(pos<target.length()){
    
    start = 0;
    end = n;
    i = (start+end)/2;
    
    t = target.substr(pos,words[i].length());
               
    while(words[i] != t){
        if(t<words[i]){
            end = i-1;
        }else{
            start = i+1;
        }
        i = (start+end)/2;
        t = target.substr(pos,words[i].length());
    }
    order[ct] = i+1;
    ct++;
    pos += len(t);
  }
    

  long long ans = 1;

  for(int i=0; i<k; i++){
    ans += (notTaken[order[i]])*npr(n-i-1,k-i-1);
    ans %= 1000000007;
    for(int j=order[i]+1; j<=n; j++){
        notTaken[j]--;
    }
  }
        

  cout << ans << endl;
  return 0;
}