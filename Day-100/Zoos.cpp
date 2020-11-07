#include<iostream>
using namespace std;
int main(){
	string zoo;
	cin>>zoo;
	int x=0;
	int y=0;
	for(int i=0;i<zoo.length();i++){
		if(zoo[i]=='z'){
		   x=x+1;
		}
		if(zoo[i]=='o'){
			y=y+1;
		}
	}
	if (2*x==y){
		cout<<"Yes"<<endl;
	}else{
		cout<<"No"<<endl;
	}
}