#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
bool Sort(const pair<int,int>& a, const pair<int,int>& b){
    if (a.second == b.second){
        return a.first < b.first;
    }
    return a.second < b.second;
}
int main() {
    int n,start,end,time = 0,cnt = 0;
    cin >> n;
    vector<pair<int,int>> meet(n);
    for (int i = 0; i < n; i++){
        cin >> meet[i].first >> meet[i].second;
    }
    sort(meet.begin(),meet.end(),Sort);
    for (int i = 0; i < n; i++){
        if (meet[i].first >= time){
            time = meet[i].second;
            cnt ++;
        }
    }
    cout << cnt;
}