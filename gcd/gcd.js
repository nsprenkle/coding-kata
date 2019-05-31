function gcd(N, arr) {
  // the max possible number is the smallest entry in the array
  let max = Math.min(...arr)

  // using that as the maximum, let's test each for divisibility
  for (let i = max; i > 0; i--) {
    // we can use arr.every to see if all are divisible
    if (arr.every((number) => { return number % i === 0 })) {
      return i
    }
  }

  // if all else fails, the GCD is 1
  return 1
}

module.exports = gcd