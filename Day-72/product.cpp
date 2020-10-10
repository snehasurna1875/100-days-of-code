

#include <iostream>
#include <bits/stdc++.h> 
using namespace std;

int main() {
	int num;
	cin >> num;	
	
	int a;
	long long pro=1;
	

    for (int i=0 ;i<num;i++){
		cin>>a;
	
		pro=(pro*a)%(1000000007);
	}
    cout<<pro<<endl;
}


