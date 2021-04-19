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
  
  # remove corner cases 0, 1, and 2
  if(length(which(vecNat < 3)) != 0){
    
    # could make a oneliner here
    cornerCases = which(vecNat < 3)
    vecNat <-vecNat[-cornerCases]
  }
  
  # reduce search space to only uneven numbers
  vecCheck = vecNat%%2; vecCheck
  vecNat <- vecNat[which(vecCheck > 0)]; vecNat
  
  
  # whoop the loop
  for (natural in vecNat){
    end = natural%/%2
    
    # dammmm youuuu first primmemeeeee
    if(end == 1){
      # message(natural, " is a Prime")
      primes <- append(primes,natural)
      next
    }
    
    # Vec with repeated query natural #, length = # of potential divisors
    # Other Vec has all divisors from 3 (search space reduced) to half of natural 
    vecQueryNat = rep(natural, length(3:end))
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
# nDigits$Var1 <- as.character(nDigits$Var1)
# nDigits <- rbind(c("Start",1),nDigits,c("End",length(primes)))

# add all single Digits (col 1 = # of rotations, col 2 = number of primes with
# a given number of rotation)
# cyclicPrimes <- primes[1:nDigits[1,2]]

# decompose nDigits
maxRotation = nrow(nDigits)


for(rotation in 1:maxRotation){
  
  if(rotation == 1){
    start = 1
  } else {
    start = nDigits[rotations,2]
  }
  if(rotation == maxRotation){
    end = length(primes)
  } else {
    end = nDigits[rotation,2]
  }
   
  primesRot <- primes[start:end]
  
  for(potCyclicPrimes in primesRot){
    rot <- as.character(potCyclicPrimes); rot
    rotVec <- unlist(strsplit(rot,"")); rotVec
    
    # rotation
    check = 0
    
    for (i in 1:rotation){
      
      lastIdx <- length(rotVec); lastIdx
      rotVec <- rotVec[c(lastIdx,1:lastIdx-1)]
      
      # check if rotation is prime
      if(as.numeric(paste(rotVec, collapse = "",sep = "")) %in% primes){
        
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

# TO DO: ALL ROTATIONS APPEAR!!! Append all rots and remove rots from iterating list

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
