import sys
def matrix_chain_multiplication(arr,i,j):
    minimum = sys.maxsize
    if i>=j:
        return 0
    for k in range(i,j):
        
        cost = (matrix_chain_multiplication(arr,i,k)+matrix_chain_multiplication(arr,k+1,j)+arr[i-1]*arr[k]*arr[j])
    if minimum>cost:
        minimum = cost
    return minimum

def matrix_chain_multiplication_dp(arr,i,j):
    minimum = sys.maxsize
    if i>=j:
        return 0
    if dp[i][j]!=-1:
        return dp[i][j]
    for k in range(i,j):
        
        cost = (matrix_chain_multiplication(arr,i,k)+matrix_chain_multiplication(arr,k+1,j)+arr[i-1]*arr[k]*arr[j])
    if minimum>cost:
        minimum = cost
    dp[i][j]=minimum
    return dp[i][j]
    
        
    



arr=[3,3,3]
n=len(arr)
dp=[[-1 for i in range(n+1)]for j in range(n+1)]
print(matrix_chain_multiplication(arr,1,n-1))
print(matrix_chain_multiplication_dp(arr,1,n-1))
