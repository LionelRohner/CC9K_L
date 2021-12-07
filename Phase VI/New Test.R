

primesUpTo = primeEvalErathostenes(11)

primesUpTo

n = 10

for (i in primesUpTo){
  if (n%%i == 0){
    print("yes")
    subDivision = n/i
    
    for (ii in subDivision){
      
    }
  } else {
    print("no")
  }
}



N <- 6
coins <- c(1,2)
# coins = 1
ways <- rep(0,N+1)
ways[1] <- 1


for (i in 1:length(coins)){
  for (j in 1:length(ways)){
    # cat("i = ", i, "j = ", j, "\n")
    if (coins[i] < j){
      # print(j)
      # print(coins[i])
      # cat("new idx = ", (j - coins[i]), "\n")
      ways[j] <- ways[j] + ways[(j - coins[i])]
      print(ways)
    }
  }
}; ways

