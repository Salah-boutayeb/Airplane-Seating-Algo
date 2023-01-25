# Time complexity of this code is O(n²) 
# Space complexity is O(n)
def seats(mat):
    
    i=0
    while i < len(mat):
        if len(mat[i]) == 0:
            i=i+1 
            print("       ", end='\t')
            continue
        print(mat[i][0], end='  ')
        mat[i].pop(0)
        
        if i == len(mat)-1:
            print('\n')
            i=0
        else:
            i=i+1    



def airplane(arr,pas):
    n=0
    s=0
    mat=[]


    for i in range(len(arr)):
        mat.append([[' ']*arr[i][0] for j in range(arr[i][1])])
    


    i=0
    # This while loop used to fill the aisle seats
    while n<len(arr):
        if n==0:
            if i < arr[n][1]:
                s=s+1
                if(s<=pas):
                    mat[n][i][arr[n][0]-1]=s
                    
                    n=n+1
                else:
                    break    
            else:
                n=n+1
            
        elif n==len(mat)-1:
            if i < arr[n][1]:
                s=s+1
                if(s<=pas):
                    mat[n][i][0]=s
                    i=i+1  
                    n=0
                else:
                    break        
            else:
                n=n+1
                
        else :
            if i < arr[n][1]:
                s=s+1
                if(s<=pas):
                    mat[n][i][0]=s
                else:
                    break        
                s=s+1
                if(s<=pas):
                    mat[n][i][arr[n][0]-1]=s
                    n=n+1
                else:
                    break        
            else:
                n=n+1



    i=0
    n=0
    # This while loop used to fill the window seats
    while n<len(arr):
        if n==0:
            if i < arr[n][1]:
                s=s+1
                if(s<=pas):
                    mat[n][i][0]=s
                    n=n+1
                else:
                    break        
            else:
                n=n+1
            
        elif n==len(mat)-1:
            if i < arr[n][1]:
                s=s+1
                if(s<=pas):
                    mat[n][i][arr[n][0]-1]=s
                    i=i+1
                    n=0
                else:
                    break        
            else:
                n=n+1
        else:
            n=n+1



    i=0
    n=0
    # This while loop used to fill the middel seats
    while n<len(arr) :
        if i < arr[n][1]:
            for k in range(1,arr[n][0]-1):
                s=s+1
                if(s<=pas):
                    mat[n][i][k]=s
                else:
                    break    
            if(n==len(mat)-1)  :
                n=0
                i=i+1
            else:
                n=n+1      
       
        else:
            n=n+1
    seats(mat)            

airplane([[3,2],[4,3],[2,3],[3,4]],30)