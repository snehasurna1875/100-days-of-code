def count_substring(string, sub_string):
    count=0
    s=""
    if string=="" or sub_string=="":
        return count
    for i in range(1,len(string)-(len(sub_string)-2))  :
        for j in range(0,len(sub_string)):
            s=s+ string[-(i+j)]
        d=s[::-1]
        
        
        if s.lower()==sub_string or s.upper()==sub_string or d==sub_string :
            count=count+1
        s=""
         
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
