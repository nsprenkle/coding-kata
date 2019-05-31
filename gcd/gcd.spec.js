var gcd = require('./gcd')

describe('GCD', () => {
  it('should get the GCD of an array', () => {
    let arr = [2, 4, 6, 10]
    let N = arr.length

    expect(gcd(N, arr)).toEqual(2)
  })

  it('should get a GCD of 1 for items with no other GCD', () => {
    let arr = [3, 5, 7, 11]
    let N = arr.length

    expect(gcd(N, arr)).toEqual(1)
  })
})