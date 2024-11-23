#include <iostream>
#include <vector>
#include <utility>
using namespace std;
int n,m,ans,cnt = 0;
vector<vector<int>> graph;
int dfs(int y,int x){
    int nx,ny,size = 1;
    vector<pair<int,int>> d = {{1,0},{-1,0},{0,1},{0,-1}};
    for (int k = 0; k < 4; k++){
        nx = x + d[k].first;
        ny = y + d[k].second;
        if (0 <= nx && nx < m && 0 <= ny && ny < n && graph[ny][nx] == 1){
            graph[ny][nx] = 2;
            size += dfs(ny,nx);
        }
    }
    return size;
}
int main() {
    cin >> n >> m;
    graph = vector<vector<int>>(n, vector<int>(m));
    for (int i = 0;i < n; i++){
        for (int j = 0; j < m; j++){
            cin >> graph[i][j];
        }
    }
    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            if (graph[i][j] == 1){
                cnt ++;
                graph[i][j] = 2;
                ans = max(ans,dfs(i,j));
            }
        }
    }
    cout << cnt << '\n' << ans;
}