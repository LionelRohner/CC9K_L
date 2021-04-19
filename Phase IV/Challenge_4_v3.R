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


getPrimes <- function(from, to){
  
  # variables
  vecNat = from:to; vecNat
  primes = c(2) # add 2 already here, because hes an ass
  
  # remove corner cases 0, 1, and 2 from the list
  if(length(which(vecNat < 3)) != 0){
    
    # get indices of 0, 1, and 2 if present in the vec and remove em
    cornerCases = which(vecNat < 3)
    vecNat <-vecNat[-cornerCases]
  }
  
  # reduce search space to only uneven numbers
  vecCheck = vecNat%%2; vecCheck
  vecNat <- vecNat[which(vecCheck > 0)]; vecNat
  
  # whoop the loop
  for (natural in vecNat){
    
    # upper limit of the dividents (the highest divident can be half of the prime at most)
    end = natural%/%2
    
    # dammmm youuuu first primmemeeeee - Extra conds for first prime
    # if the only divident is 1 it should be a prime, this is the case for 2 and 3.
    if(end == 1){
      # message(natural, " is a Prime")
      primes <- append(primes,natural)
      next
    }
    
    # Vec with repeated query natural numb, length = # of potential divisors
    vecQueryNat = rep(natural, length(3:end))
    
    # Vec with all divisors from 3 (search space reduced) to half of natural 
    vecDiv = c(3:end)
    
    # add to primes or not
    if(min(vecQueryNat%%vecDiv) != 0){
      # message(natural, " is a Prime")
      primes <- append(primes,natural)
    } #else {
      # message(natural, " is not a Prime")
    # }
  }
  return(primes)
}



getCyclicPrimes <- function(from,to){
  
  # getPrimes
  primes <- getPrimes(from, to)
  cyclicPrimes <- c()
  singleDigits <- X
}

primes <- getPrimes(1,120)

primes

# TO DO: get number of rotations (ONELINE THAT ISH)
# nDigits <- floor(log10(primes)) + 1
nDigits <- as.data.frame(table(floor(log10(primes)) + 1))
colnames(nDigits) <- c("Rotations (i.e. # of digits)","# of primes with that rotation number")

# decompose nDigits - the # of rotation is the number of rows
maxRotation <- nrow(nDigits)

# Cache vector for primes - reduces the number of iteration if primes are already in
# this vectior. E.g. a cyclic prime with 3 digits will appear 3 times and should only
# be evaluated once.
rotVecCache <- c()

for(rotation in 1:maxRotation){
  print(c("rotation: ", rotation))
  # get the indices of the start index
  # if rotation is 1; the first index is 1
  # if rotation is > 1; the starting index is found in col 2 of nDigits
  if(rotation == 1){
    start = 1
  } else if(rotation > 1){
    print(c("start: ",start))
    start = nDigits[rotation,2]
  }
  
  # define the last index of the primes with a given rotation
  if(rotation == maxRotation){
    end = length(primes)
  } else {
    end = nDigits[rotation,2]
    print(c("end: ", end))
  }
   
  # the prime slice with a specific rotation number (used in next loop) 
  primesRot <- primes[start:end]
  print(primesRot)
  
  # go through all rotations in all primes of the slice primesRot
  for(potCyclicPrimes in primesRot){
    
    # transform prime to character vector to evaluate rotation
    rot <- as.character(potCyclicPrimes); rot
    rotVec <- unlist(strsplit(rot,"")); rotVec
    
    # check whether character prime vector has already been evaluated in some other rotation
    if(as.numeric(paste(sort(rotVec),collapse = "")) %in% rotVecCache){
      # print("duplicate")
      next
    } 
  
    # else add character prime to cache
    rotVecCache <- append(rotVecCache, as.numeric(paste(sort(rotVec),collapse = "")))
  
    # rotation
    check = 0
    
    # evaluate if all rotations are also primes 
    for (i in 1:rotation){
      
      lastIdx <- length(rotVec); lastIdx
      rotVec <- rotVec[c(lastIdx,1:lastIdx-1)]
      
      rotVecNum <- as.numeric(paste(rotVec, collapse = "",sep = ""))
      
      # check if rotation is prime
      if(rotVecNum %in% primes){
          
        check = check + 1
      } else {
        break
      }
    }
    if (check == rotation){
      cyclicPrimes <- append(cyclicPrimes, potCyclicPrimes)
    }
  }
}
primes[]
nDigits
# TO DO: ALL ROTATIONS APPEAR!!! Append all rots and remove rots from iterating list
cyclicPrimes
unique(cyclicPrimes)



cyclicPrimeTest = 197

rot <- as.character(cP); rot
rotVec <- unlist(strsplit(rot,"")); rotVec

# rotation
for (rotation in 1:3){
  
  check = 0
  
  lastIdx <- length(rotVec); lastIdx
  rotVec <- rotVec[c(lastIdx,1:lastIdx-1)]
  
  # check if rotation is prime
  if(as.numeric(paste(rotVec, collapse = "",sep = "")) %in% primes){
    print("Prime")
    check = check + 1
  } else {
    break
  }
}
if (check == maxRot){
  cyclicPrimes <- append(cyclicPrimes, cyclicPrimeTest)
}

rotVec = c("4","2","3")

rotVecCache <- append(rotVecCache,as.numeric(paste(sort(rotVec),collapse = "")))

if(as.numeric(paste(sort(rotVec),collapse = "")) %in% rotVecCache){
  print("duplicate")
} 



### option 2

for (natural in 2:10){
  end = natural%/%2
  
  vecNat = rep(natural, length(2:end))
  vecDiv = c(2:end)
  
  if(min(vecNat%%vecDiv) != 0){
    message(natural, " is a Prime")
  } else {
    message(natural, " is not a Prime")
  }
}

natural = 3

end = natural%/%2; end

vecNat = rep(natural, length(1:end)); vecNat
vecDiv = c(1:end); vecDiv

min(vecNat%%vecDiv)

if(min(vecNat%%vecDiv) != 0){
  message(natural, " is a Prime")
} else {
  message(natural, " is not a Prime")
}

#------------------------------------------------------------------------------#
# Benchmark ---------------------------------------------------------------
#------------------------------------------------------------------------------#

test <- benchmark("Algo 1" = {
  A <- seq(1,10^6,1)
  
  sum(A[which(A %% 3 == 0 | A %% 5 == 0)])
},

"Algo 2" = {
  A <- 1:10^6
  
  sum(A[which(A %% 3 == 0 | A %% 5 == 0)])
  
},

"Algo 3" = {
  A <- 1:10^6
  
  sum(A[setdiff(union(which(A %% 3 == 0), which(A %% 5 == 0)),
                intersect(which(A %% 3 == 0), which(A %% 5 == 0)))])
},

"Algo 4" = {
  A <- 1:10^6
  
  B <- A[which(A %% 3 == 0)]
  
  C <- setdiff(A,B)
  
  C <- C[which(C %% 5 == 0)]
  
  sum(B) + sum (C)
},
replications = 10)

test$meanTime <- test$elapsed/test$replications
test
