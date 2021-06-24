
val = 10

for i in primes:

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