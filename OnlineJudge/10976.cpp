/*****************************************
*   UVA #10976 : Fractions Again?!        *
*   Labels     : complete search          *
******************************************/

#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(){

    int n;
    cin >> n;
    while(!cin.eof()){


        vector<string> v;
        for(int i=n+1; i<n*2+1; i++){
            if((i*n/(i-n)) * (i-n) == i*n){
                v.push_back("1/" + to_string((i*n/(i-n))) + " + 1/" + to_string(i));
            }
        }

        cout << v.size() << endl;
        for(int i=0; i<v.size(); i++){
            cout << "1/" << to_string(n) << " = " << v[i] << endl;
        }

        cin >> n;
    }

    return 0;
}
