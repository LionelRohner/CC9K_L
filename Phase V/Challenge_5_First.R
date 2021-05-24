#------------------------------------------------------------------------------#
# Task --------------------------------------------------------------------
#------------------------------------------------------------------------------#

# How many, not necessarily distinct, values of choose(n,r) for 1 \leq n \leq
# 100$, are greater than one-million?\\[15pt]

# r \leq n

#------------------------------------------------------------------------------#
# Library -----------------------------------------------------------------
#------------------------------------------------------------------------------#

library(rbenchmark)

#------------------------------------------------------------------------------#
# Functions ---------------------------------------------------------------
#------------------------------------------------------------------------------#

# main
challenge_V <- function(countOnly = T, upperLim = 1e6, n, r){
  
  if(countOnly){
    
    # create an upper triangular matrix, because r should be smaller than n
    # Moreover, the diagonal can be excluded as choose(n,n) is always one
    A <- upper.tri(matrix(NA,nrow = n, ncol = r), diag = F)
    
    # Output array indeces (matrix of row and col indeces), where TRUE
    idx <- which(A == T, arr.ind = T)
    
    # vectorized binom coefficient calculation for all indeces of interest.
    return(length(which(choose(idx[,"col"],idx[,"row"]) > upperLim)))
  } else {
    
    # create an upper triangular matrix, because r should be smaller than n
    # Here diagonal is computed to avoid confusion of 0s on the diagonal
    A <- upper.tri(matrix(NA,nrow = n, ncol = r), diag = T)
    
    # Output array indeces (matrix of row and col indeces), where TRUE
    idx <- which(A == T, arr.ind = T)
    for (i in idx[,"row"]){
      for (j in idx[,"col"]){
        A[i,j] <- choose(j,i)
      }
    }
    return(A)
  } 
}

#------------------------------------------------------------------------------#
# Testing Area ------------------------------------------------------------
#------------------------------------------------------------------------------#

# Example 1
choose(5,3)

# Example 2
choose(23,10)

n = r = 10

# create an upper triangular matrix, because r should be smaller than n
# Moreover, the diagonal can be excluded as choose(n,n) is always one
A <- upper.tri(matrix(NA,nrow = n, ncol = r), diag = F)

# Output array indeces (matrix of row and col indeces), where TRUE
idx <- which(A == T, arr.ind = T)

for (i in idx[,1]){
  for (j in idx[,2]){
    A[i,j] <- choose(i,j)
  }
}

nrow(which(A > 1e6, arr.ind = T))


#------------------------------------------------------------------------------#
# Code -------------------------------------------------------------------
#------------------------------------------------------------------------------#

challenge_V(n = 100, r = 100, countOnly = F)

#------------------------------------------------------------------------------#
# Benchmark ---------------------------------------------------------------
#------------------------------------------------------------------------------#

test <- benchmark("Algo1" = {challenge_V(n = 100, r = 100)},
                  "Algo1_loops" = {challenge_V(n = 100, r = 100, countOnly = F)},
                  replications = 10)


test$meanTime <- test$elapsed/test$replications
test

