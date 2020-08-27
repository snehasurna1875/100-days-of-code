#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
  int n;
    cin>>n;
    vector<int> a;
    int num;
    for(int i=0;i<n;i++){
        cin>>num;
        a.push_back(num);
    }  
    int pos;
    cin>>pos;
    pos=pos-1;
    a.erase(a.begin()+pos);
    int upper,lower;
    cin>>upper>>lower;
    upper=upper-1;
    lower=lower-1;
    a.erase(a.begin()+upper,a.begin()+lower);
    cout<<a.size()<<endl;
    int m=a.size();
     for(int i=0;i<m;i++){
       cout<<a[i]<<" ";
    }
    return 0;
}
