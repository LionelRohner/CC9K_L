#------------------------------------------------------------------------------#
# Task --------------------------------------------------------------------
#------------------------------------------------------------------------------#


# The number, 197, is called a circular prime because all rotations of the 
# digits: 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 
# 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

# How many circular primes are there below one million?


#------------------------------------------------------------------------------#
# Library -----------------------------------------------------------------
#------------------------------------------------------------------------------#

library(rbenchmark)
library(Rcpp)

#------------------------------------------------------------------------------#
# Functions ---------------------------------------------------------------
#------------------------------------------------------------------------------#


#------------------------------------------------------------------------------#
# Code -------------------------------------------------------------------
#------------------------------------------------------------------------------#

checkPrime <- function(numb){
  upperBound <- sqrt(numb)
  if(numb == 2){
    return(TRUE)
  } else if (any(numb %% 2:upperBound == 0)){
    return(FALSE)
  } else {
    return(TRUE)
  }
}

checkPrimeRedux <- function(numb){
  upperBound <- sqrt(numb)
  if (any(numb %% 2:upperBound == 0)){
    return(FALSE)
  } else {
    return(TRUE)
  }
}

checkPrimeRedux2 <- function(numb){
  upperBound <- sqrt(numb)
  if (any(numb %% 10:upperBound == 0)){
    return(FALSE)
  } else {
    return(TRUE)
  }
}


primeEvalFast <- function(from = 0, to, countOnly = TRUE){
  
  # generate range vec for prime search
  vecNat = from:to
  outputPrimes = c()
  
  # extract search space reducing primes
  exceptions <- which(vecNat == 2 | vecNat == 3 | vecNat == 5 | vecNat == 7)
  outputPrimes <- vecNat[exceptions]
  
  # reduce search space
  rmIdx <- c()
  for (i in c(2,3,5,7)){
    # rmIdx <- append(rmIdx, which(vecNat%%i == 0))
    vecNat <- vecNat[-which(vecNat%%i == 0)]
  }
  message("Search space reduced by ", round(100-(length(vecNat)/length(from:to))*100, digits = 3), "%")
  
  # iterate through vec
  if(countOnly == TRUE){
    cnt = length(outputPrimes)
    for(numb in vecNat){
      if(checkPrimeRedux(numb)){
        cnt = cnt + 1
      }
    }
    return(cnt)
  
  } else {
    for(numb in vecNat){
      if(checkPrimeRedux(numb)){
        outputPrimes <- append(outputPrimes, numb)
      }
    }
    return(outputPrimes)
  }
}

primeEvalFaster <- function(from = 0, to, countOnly = TRUE){
  
  # generate range vec for prime search
  vecNat = from:to
  outputPrimes = c()
  
  # extract search space reducing primes
  exceptions <- which(vecNat == 2 | vecNat == 3 | vecNat == 5 | vecNat == 7)
  outputPrimes <- vecNat[exceptions]
  
  # reduce search space
  rmIdx <- c()
  for (i in c(2,3,5,7)){
    # rmIdx <- append(rmIdx, which(vecNat%%i == 0))
    vecNat <- vecNat[-which(vecNat%%i == 0)]
  }
  message("Search space reduced by ", round(100-(length(vecNat)/length(from:to))*100, digits = 3), "%")
  
  # iterate through vec
  if(countOnly == TRUE){
    cnt = length(outputPrimes)
    for(numb in vecNat){
      if(checkPrimeRedux2(numb)){
        cnt = cnt + 1
      }
    }
    return(cnt)
    
  } else {
    for(numb in vecNat){
      if(checkPrimeRedux2(numb)){
        outputPrimes <- append(outputPrimes, numb)
      }
    }
    return(outputPrimes)
  }
}

getCyclicPrimes <- function(primes){
  
  # Cache vector for primes - reduces the number of iteration if primes are already in
  # this vectior. E.g. a cyclic prime with 3 digits will appear 3 times and should only
  # be evaluated once.
  rotVecCache <- c()
  
  # empty vector for output$
  cyclicPrimes <- c()
  
  cnt = 0
  
  # go through all rotations in all primes of the slice primesRot
  for(potCyclicPrimes in primes){
    
    # transform prime to character vector to evaluate rotation
    rot <- as.character(potCyclicPrimes)
    rotVec <- unlist(strsplit(rot,""))
    
    # # check whether character prime vector has already been evaluated in some other rotation
    # redundancyChecker <- as.numeric(paste(sort(rotVec),collapse = ""))
    # 
    # if(redundancyChecker %in% rotVecCache){
    #   next
    # } else {
    #   # else add character prime to cache
    #   rotVecCache <- append(rotVecCache, redundancyChecker)
    # }
    # 
    
    # rotation
    check = 0
    
    rotation = length(rotVec)
    
    # evaluate if all rotations are also primes 
    for (i in 1:rotation){
      
      lastIdx <- length(rotVec)
      
      # puts the last index at the first position and pushes the OG-vec to position 2
      rotVec <- rotVec[c(lastIdx,1:lastIdx-1)]
      
      
      # if rotVec not in cache check whether rotations are primes
      rotVecNum <- as.numeric(paste(rotVec, collapse = "",sep = ""))
      cnt = cnt + 1
      
      # check if rotation is prime
      if(rotVecNum %in% primes){
        # if rotation is in primes, add +1 to check counter  
        check = check + 1
      } else {
        break
      }
    }
    # if the number of checks is equal to the number of rotation all rotation are primes
    if (check == rotation){
      cyclicPrimes <- append(cyclicPrimes, potCyclicPrimes)
    }
  }
  return(cyclicPrimes)
}





length(getCyclicPrimes(primeEvalFast(0,1e6,countOnly = F)))

#------------------------------------------------------------------------------#
# Benchmark ---------------------------------------------------------------
#------------------------------------------------------------------------------#
library(rbenchmark)

test <- benchmark("Algo 1" = {length(getCyclicPrimes(primeEvalFast(0,1e6,countOnly = F)))},
                  "Algo 2" = {length(getCyclicPrimes(primeEvalFaster(0,1e6,countOnly = F)))},
                  replications = 10)

test$meanTime <- test$elapsed/test$replications
test

