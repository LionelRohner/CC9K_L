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

#------------------------------------------------------------------------------#
# Primes Function ---------------------------------------------------------
#------------------------------------------------------------------------------#


primeEvalErathostenes <- function(to){
  
  # vars
  upperBound = round(sqrt(to))
  vecNat = rep(T, to)
  
  # expection from 1
  vecNat[1] <- F
  
  # sieve of erathostenes
  lastPrime = 2
  
  for (i in lastPrime:upperBound){
    
    # skip indeces that are already F
    if (vecNat[i] == F){
      lastPrime = lastPrime + 1
      next
    }

    # find all multiples of primes as these must be composite
    multiples <- seq(lastPrime*2, to, lastPrime)
    vecNat[multiples] <- F

    # redefine new prime
    lastPrime = lastPrime + 1

  }
  
  # return primes, i.e. those that are still TRUE
  return(which(vecNat))
}

#------------------------------------------------------------------------------#
# Cyclic Primes Function --------------------------------------------------
#------------------------------------------------------------------------------#

getCyclicPrimes <- function(primes){
  
  # Cache vector for primes - reduces the number of iteration if primes are already in
  # this vectior. E.g. a cyclic prime with 3 digits will appear 3 times and should only
  # be evaluated once.
  rotVecCache <- c()
  
  # empty vector for output$
  cyclicPrimes <- c()
  
  cnt = 0
  
  # nenad'sche Heuristik
  primes = primes[!grepl("0|[0-9]+2|4|6|8", primes)]
  
  # go through all rotations in all primes of the slice primesRot
  for(potCyclicPrimes in primes){
    
    # transform prime to character vector to evaluate rotation
    rot <- as.character(potCyclicPrimes)
    rotVec <- unlist(strsplit(rot,""))
    
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

#------------------------------------------------------------------------------#
# Testing Area ------------------------------------------------------------
#------------------------------------------------------------------------------#

primes2 <- primeEvalErathostenes(1e3); primes2

#------------------------------------------------------------------------------#
# Code -------------------------------------------------------------------
#------------------------------------------------------------------------------#

length(getCyclicPrimes(primeEvalErathostenes(1e6)))

#------------------------------------------------------------------------------#
# Benchmark ---------------------------------------------------------------
#------------------------------------------------------------------------------#

test <- benchmark("FastnFurious" = {length(getCyclicPrimes(primeEvalErathostenes(1e6)))},
                  replications = 10)

# test <- benchmark("Algo 1" = {primeEvalFast(0,1e6,countOnly = F)},
#                   "Algo 2" = {primeEvalErathostenes(1e6)},
#                   replications = 5)

test$meanTime <- test$elapsed/test$replications
test

