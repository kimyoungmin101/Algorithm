
#include <iostream>
#include <queue>
#include <cstring>
#include <algorithm>
#include <math.h>
#include <queue>

using namespace std;

int main(){
    
    priority_queue< pair <int, int> > pq;

    pq.push(make_pair(-2,3));
    pq.push(make_pair(-5,4));
    pq.push(make_pair(-3,6));
    pq.push(make_pair(-8,5));
    pq.push(make_pair(-1,4));

    while(pq.empty()==0){
        cout << -pq.top().first << endl;
        pq.pop();
    }

    return 0;
}