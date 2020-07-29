
vector<int> dynamicArray(int n, vector<vector<int>> queries) {


vector<vector<int>> seq(n);
vector<int> value;
int lastanswer=0;
int k;
int j=0;
int m =queries.size();
for(int i=0;i<m;i++){
    if(queries[i][0]==1){
         j= (queries[i][1]^lastanswer)%n;
        seq[j].push_back(queries[i][2]);
        
    }
    else{
         j= (queries[i][1]^lastanswer)%n;
        k= (queries[i][2])%seq[j].size();
        lastanswer=seq[j][k];
        value.push_back(lastanswer);
    }
}
return value; 

}
