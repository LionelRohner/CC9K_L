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

n = 10

A <- upper.tri(matrix(NA,nrow = n, ncol = r), diag = F)

idx <- which(A == T, arr.ind = T)

class(idx)

# main
challenge_V <- function(countOnly = T, upperLim = 1e6, n, r){
  
  # ONLY COUNT THE NUMBER OF BINOM COEF THAT ARE BIGGER THAN 1e6  
  if(countOnly){
    
    # create an upper triangular matrix, because r should be smaller than n
    # Moreover, the diagonal can be excluded as choose(n,n) is always one
    A <- upper.tri(matrix(NA,nrow = n, ncol = r), diag = F)
    
    # Output array indeces (matrix of row and col indeces), where TRUE
    idx <- which(A == T, arr.ind = T)
    
    # vectorized binom coefficient calculation for all indeces of interest.
    return(length(which(choose(idx[,"col"],idx[,"row"]) > upperLim)))
  
  # DISPLAY RESULTS  
  } else {
    
    # Here diagonal is computed to avoid confusion of 0s on the diagonal
    A <- upper.tri(matrix(NA,nrow = n, ncol = r), diag = T)
    idx <- which(A == T, arr.ind = T)
    
    # pre-allocate results into a vector
    res <- choose(idx[,"col"],idx[,"row"])
    
    # loop through indeces pairs. Didnt find a way to drop the loop
    # DOES NOT WORK : A[idx[,"row"],idx[,"col"]] <- res[]
    for (i in 1:nrow(idx)){
      A[idx[i,"row"],idx[i,"col"]] <- res[i]
    }
    return(t(A))
  } 
}


challenge_V_v2 <- function(countOnly = T, upperLim = 1e6, n, r){
  
  # ONLY COUNT THE NUMBER OF BINOM COEF THAT ARE BIGGER THAN 1e6  
  if(countOnly){
    
    # create an upper triangular matrix, because r should be smaller than n
    # Moreover, the diagonal can be excluded as choose(n,n) is always one
    A <- upper.tri(matrix(NA,nrow = n, ncol = r), diag = F)
    
    # Output array indeces (matrix of row and col indeces), where TRUE
    idx <- which(A == T, arr.ind = T)
    
    # vectorized binom coefficient calculation for all indeces of interest.
    return(length(which(choose(idx[,"col"],idx[,"row"]) > upperLim)))
    
    # DISPLAY RESULTS  
  } else {
    
    # Here diagonal is computed to avoid confusion of 0s on the diagonal
    A <- upper.tri(matrix(NA,nrow = n, ncol = r), diag = T)
    idx <- which(A == T, arr.ind = T)
    
    # pre-allocate results into a vector
    res <- choose(idx[,"col"],idx[,"row"])
    
    # loop through indeces pairs. Didnt find a way to drop the loop
    # DOES NOT WORK : A[idx[,"row"],idx[,"col"]] <- res[]
    for (i in 1:nrow(idx)){
      A[idx[i,"row"],idx[i,"col"]] <- res[i]
    }
    return(t(A))
  } 
}

#------------------------------------------------------------------------------#
# Testing Area ------------------------------------------------------------
#------------------------------------------------------------------------------#

# Example 1
choose(5,3)
challenge_V(n = 100, r = 100, countOnly = F)[5,3]

# Example 2
choose(23,10)
challenge_V(n = 100, r = 100, countOnly = F)[23,10]


#------------------------------------------------------------------------------#
# Code -------------------------------------------------------------------
#------------------------------------------------------------------------------#

challenge_V(n = 100, r = 100, countOnly = T)

#------------------------------------------------------------------------------#
# Benchmark ---------------------------------------------------------------
#------------------------------------------------------------------------------#

test <- benchmark("Algo1" = {challenge_V(n = 100, r = 100)},
                  "Algo1_Display" = {challenge_V(n = 100, r = 100, countOnly = F)},
                  replications = 10)


test$meanTime <- test$elapsed/test$replications
test

