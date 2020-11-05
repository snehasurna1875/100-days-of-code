#include <bits/stdc++.h> 
using namespace std; 
int main() 
{ 
    string str;
	cin>>str;
    
    string dtr;
	dtr=str;
    reverse(str.begin(), str.end()); 
	if(dtr==str){
		cout<<"YES"<<endl;
	}else{
        cout<<"NO"<<endl;
	}
  
    return 0; 
} 