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

# not in
`%notin%` <- Negate(`%in%`)

# find primes
primeEvalErathostenes <- function(to){
  
  # vars
  upperBound = round(sqrt(to))
  # print(upperBound)
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

primeEvalErathostenes(11)


# INIT

result <- data.frame(val = c(2,3), combCnt = c(1,1))

# while(result[val,2] < 5000){
#   
# }

for (val in 4:10){
  combCnt = 0
  
  primes <- primeEvalErathostenes(val)
  
  is <- c()
  
  for (i in primes){
    
    is <- c(is,i)
    
    
    if (i > val-2){
      next
    }
    
    mudolo <- val%%i
    times <- val%/%i
    
    # if (times == 1 & mudolo == 0){
    #   next
    # }
    
    message("val: ", val," || ", "i: ",i)
    
    # this catches all single primes sums, e.g. 2+2+2 or 3+3
    if(mudolo==0){
      # times <- val%/%i
      if(i*times == val)
        print("without %")
        print(rep(i,times))
        combCnt <- combCnt + 1
        next
      
    } else if (mudolo %in% result[,1]){
      # times <- val%/%i
      if(i*times + mudolo == val)
        print("with %")
        print(c(rep(i,times),mudolo))
        combCnt = combCnt + result[which(result[,1]==mudolo),2]
        # print("yes")
        
    } else if (mudolo == 1 & times > 1){
      mudoloPlus <- mudolo + i
      if(mudoloPlus %in% primes & mudoloPlus %notin% is){
        if(i*times-1 + mudoloPlus == val){
          print("with %+")
          print(c(rep(i,times),mudoloPlus))
          combCnt = combCnt + result[which(result[,1]==mudoloPlus),2]
        }
          
      }
    } 
    
    

  }
  result <- rbind(result, c(val,combCnt))
}


result

2*5 == 2+2+2+2+2

# use expand grid: use number of primes as the number of arguments
expand.grid()

# Test Area ---------------------------------------------------------------

val <- 10

primes <- primeEvalErathostenes(10); primes

lastIndex <- primes[max(which(primes <= sqrt(val)))]
upperLim <- primes[1]*lastIndex

all <- rep(primes,upperLim)

DF <- c()
for (i in 1:upperLim){
  DF <- cbind(DF,all)
}

expand.grid(replicate(upperLim,all,simplify = F))



 # Garbage Code ------------------------------------------------------------


for (val in 4:10){
  combCnt = 0
  
  primes <- primeEvalErathostenes(val)
  
  for (i in primes){
    
    if (i > val-2){
      next
    }
    
    mudolo <- val%%i
    times <- val%/%i
    
    if (times == 1 & mudolo == 0){
      next
    }
    
    message("val: ", val," || ", "i: ",i)
    
    # this catches all single primes sums, e.g. 2+2+2 or 3+3
    if(mudolo==0){
      # times <- val%/%i
      if(i*times == val)
        print("without %")
      print(rep(i,times))
      combCnt <- combCnt + 1
      next
      
    } else if (mudolo %in% result[,1]){
      # times <- val%/%i
      if(i*times + mudolo == val)
        print("with %")
      print(c(rep(i,times),mudolo))
      combCnt = combCnt + result[which(result[,1]==mudolo),2]
      # print("yes")
      
    } else if (mudolo == 1){
      next
    } 
    
    
    
  }
  result <- rbind(result, c(val,combCnt))
}
