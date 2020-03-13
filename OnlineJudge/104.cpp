/****************************************
*   UVA #104 : Arbitrage                *
*   Labels   : graph traversals, bfs    *
*****************************************/


#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main(){

    int n;
    double x;
    cin >> n;
    while(!cin.eof()){

        vector<double> graph[n];
        queue<vector<int> > q;
        queue<double> curr;
        vector<int> ans;
        bool cont = true;

        /// input  ///
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                if(i==j){
                    graph[i].push_back(1);
                }else{
                    cin >> x;
                    graph[i].push_back(x);
                    if(x>=1){
                        vector<int> v(1,i);
                        v.push_back(j);
                        q.push(v);
                        curr.push(x);
                    }
                }
            }
        }

        while(q.size()>0 && cont){
            vector<int> sequence = q.front(); q.pop();
            double current = curr.front(); curr.pop();
            int i = sequence.back();
            int start = sequence[0];

            if(sequence.size()>=20){
                break;
            }

            for(int j=0; j<n; j++){
                double mul = graph[i][j]*current;
                if(i!=j && mul>=1){
                    if(start==j && mul>=1.01){
                        ans = sequence;
                        ans.push_back(j);
                        cont=false;
                        break;
                    }
                    vector<int> seq(sequence.begin(), sequence.end());
                    seq.push_back(j);
                    q.push(seq);
                    curr.push(mul);
                }
            }

        }

        if(ans.size()!=0){
            cout << ans[0]+1;
            for(int i=1; i<ans.size(); i++){
                cout << " " << ans[i]+1;
            }
            cout << endl;
        }else{
            cout << "no arbitrage sequence exists" << endl;
        }


        cin >> n;
    }

    return 0;
}
