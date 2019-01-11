def numofneighbour(mat, i, j): 
    count = 0;   
    if (i > 0 and mat[i - 1][j]): 
        count+= 1; 
    if (j > 0 and mat[i][j - 1]): 
        count+= 1; 
    if (i < R-1 and mat[i + 1][j]): 
        count+= 1
    if (j < C-1 and mat[i][j + 1]): 
        count+= 1; 
  
    return count; 
