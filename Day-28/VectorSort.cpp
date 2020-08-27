#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n;
    cin>>n;
    int temp;
    vector<int> a;
    int num;
    for(int i=0;i<n;i++){
        cin>>num;
        a.push_back(num);
    }  
    sort(a.begin(), a.end()); 
    for(int i=0;i<n;i++){
       cout<<a[i]<<" ";
    }
    return 0;
}
