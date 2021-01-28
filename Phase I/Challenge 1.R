#------------------------------------------------------------------------------#
# Task --------------------------------------------------------------------
#------------------------------------------------------------------------------#


# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# 
# Find the sum of all the multiples of 3 or 5 below 1000


#------------------------------------------------------------------------------#
# Library -----------------------------------------------------------------
#------------------------------------------------------------------------------#

library(rbenchmark)

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
# Code -------------------------------------------------------------------
#------------------------------------------------------------------------------#

# a <- seq(1,9,1)
# sum(a[which(a %% 3 == 0 | a %% 5 ==0)])



A <- seq(1,999,1)

sum(A[which(A %% 3 == 0 | A %% 5 ==0)])


benchmark("algo 1" = {
  A <- seq(1,10^6,1)
  
  sum(A[which(A %% 3 == 0 | A %% 5 == 0)])
})
