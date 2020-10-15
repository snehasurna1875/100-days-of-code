#include<iostream>
using namespace std;
int main(){
	int L;
	cin>>L;
	cout<<"\n"<<endl;
	int N;
	cin>>N;
	cout<<"\n"<<endl;
	int W,H;
	for (int i=0;i<N;i++)
	{
		cin>>W;
		cin>>H;
		if (W<L || H<L){
			cout<<"UPLOAD ANOTHER"<<endl;

		}
		if (W>=L && H>=L){
            if(H==W){
				cout<<"ACCEPTED"<<endl;
			}else{
				cout<<"CROP IT"<<endl;
			}
		}
	}

}