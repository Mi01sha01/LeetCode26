class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
      m = len(mat)
      n = len(mat[0])
      special = 0
      
      row_count = [0] * m
      col_count = [0] * n
      for r in range(m):
          for c in range(n):
              if mat[r][c] == 1:
                  row_count[r] += 1
                  col_count[c] +=1
                  
      for r in range(m):
          for c in range(n):
              if mat[r][c] == 1:
                  if row_count[r] == 1 and col_count[c] == 1:
                      special += 1
      return special                
                              
                  
          
               
          
  
       
  
        