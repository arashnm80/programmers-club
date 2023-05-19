#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int n;
    cin >> n;

    int a[300'000];
    for(int i = 0; i < n; i++){
        cin >> a[i];
    }

    sort(a, a + n);
    int hIndex = 0;

    for(int i = 0; i < n; i++){
        if(a[i] >= n - i){
            hIndex = n - i;
            break;
        }
    }

    cout << hIndex << endl;
}