#------------------------------------------------------------------------------#
# Task --------------------------------------------------------------------
#------------------------------------------------------------------------------#

# How many, not necessarily distinct, values of $\binom{n}{r}$ for $1\leq n \leq
# 100$, are greater than one-million?\\[15pt]

# r \leq n

#------------------------------------------------------------------------------#
# Library -----------------------------------------------------------------
#------------------------------------------------------------------------------#

library(rbenchmark)
library(comprehenr)

#------------------------------------------------------------------------------#
# Functions ---------------------------------------------------------------
#------------------------------------------------------------------------------#

list_comp_2d <- function(row, col, x = NULL, cond = NULL){
  
  if (require(comprehenr) == F){
    message("Install \"comprehener\" \n")
    return(NULL)
  }
  
  if (is.null(x) & is.null(cond)){
    return(t(matrix(to_vec(for (i in 1:(row*col)) i), nrow = col))) 
    
  } else if (!is.null(x) & is.null(cond)) {
    return(t(matrix(to_vec(for (i in 1:(row*col)) eval(parse(text=x))), nrow = col)))
    
  } else if (!is.null(cond) & is.null(x)){
    
    # counting elements that are required of matrix of dim(row,col)
    elements = row*col
    
    # count how many iterations are required given the condition
    
    cnt = 0
    for (i in 1:10^6){
      if(eval(parse(text=cond))){
        cnt = cnt + 1
      }
      if (cnt == elements){
        maxElements = i
        break
      }
    }
    
    # use upper limit (maxElements) for iteration 
    return(t(matrix(to_vec(for (i in 1:maxElements) if(eval(parse(text=cond))) i ), nrow = row)))
  }
}


#------------------------------------------------------------------------------#
# Testing Area ------------------------------------------------------------
#------------------------------------------------------------------------------#

choose(5,3)
choose(23,10)

binomCoef <- function(n,r){
  return(factorial(n)/(factorial(r)*factorial(n-r)))
}

binomCoef(5,3)

list_comp_2d(row = 23, col = 10,cond = )

list_comp_2d(row = 23,col = 10, x = "choose(n,r)")

n = 10
r = 10

# diag = F as all of these entries are 1
A <- upper.tri(matrix(NA,nrow = n, ncol = r), diag = F)
idx <- which(A == T, arr.ind = T)


choose(idx[,1],idx[,2])



for (i in idx[,1]){
  for (j in idx[,2]){
    A[i,j] <- choose(i,j)
  }
}

nrow(which(A > 1e6, arr.ind = T))

#------------------------------------------------------------------------------#
# Code -------------------------------------------------------------------
#------------------------------------------------------------------------------#


#------------------------------------------------------------------------------#
# Benchmark ---------------------------------------------------------------
#------------------------------------------------------------------------------#

test <- benchmark("Algo1" = {},
                  replications = 10)



test$meanTime <- test$elapsed/test$replications
test

