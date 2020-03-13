#include <bits/stdc++.h>

using namespace std;

int main(){

    int n, k, xq, yq, x, y;
    int rise, run, ans, b_i;
    cin >> n >> k >> xq >> yq;

    // blocks are in clockwise order from top
    // assume origin is bottom left
    int blocks[8] = {n-yq, 0, n-xq, 0, yq-1, 0, xq-1, 0};
    for(int i=1; i<8; i+=2) 
        blocks[i] = min(blocks[i-1],blocks[(i+1)%8]);

    while(k--) {
        cin >> x >> y;
        rise = y - yq;
        run = x - xq;
        if (run == 0) {             // vertical case
            b_i = (rise < 0) ? 0 : 4;
            blocks[b_i] = min(blocks[b_i], abs(rise));
        } else if (rise == 0) {     // horizontal case
            b_i = (run < 0) ? 2 : 6;
            blocks[b_i] = min(blocks[b_i], abs(run));
        } else if (rise == run) {   // positive gradient
            b_i = (run < 0) ? 1 : 5;
        } else if (rise == -run) {  // negative gradient
            b_i = 
        }
    }

    return 0;
}