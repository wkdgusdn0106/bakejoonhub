#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n,total = 2;
    cin >> n;
    if (n < 2){
        cout << 0;
        return 0;
    }
    vector<int> dp(n, 0);
    dp[1] = 3;
    for (int i = 2; i < n; i++){
        if (i % 2 == 0){
            continue;
        }
        dp[i] = dp[i-2]*3+total;
        total = dp[i] - dp[i-2];
    }
    cout << dp[n-1];
}