#------------------------------------------------------------------------------#
# Task --------------------------------------------------------------------
#------------------------------------------------------------------------------#

# What is the first value which can be written as the sum of primes in over 
# five thousand different ways?

#------------------------------------------------------------------------------#
# Library -----------------------------------------------------------------
#------------------------------------------------------------------------------#

library(rbenchmark)

#------------------------------------------------------------------------------#
# Functions ---------------------------------------------------------------
#------------------------------------------------------------------------------#

# find primes
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

primes <- primeEvalErathostenes(10)

combCnt = 0
val = 10

10%/%2

10%%2

for (i in primes){
  
  # this catches all single primes sums, e.g. 2+2+2 or 3+3
  if(val%%i==0){
    times <- val%/%i
    if(sum(rep(i,times))==val)
      print(rep(i,times))
      combCnt <- combCnt + 1
  }
  
  # this catches sums of two primes, e.g. 2+2+2+2+5, or 7+3
  mudolo <- val%%i
  if(mudolo %in% primes){
    times <- floor(val%/%i)
    if(sum(c(rep(i,times),mudolo))==val)
      print(c(rep(i,times),mudolo))
      combCnt <- combCnt +1
  }
  
  # now the combinations of more than 2 primes is required.
  # An idea, would be to save all combinations to avoid recalculating all combos
  # if val is 5, save 5+3 and when 10 is next, just double it 3+2+3+2
}

combCnt

