const uut = require('./index')

describe('numberToString', () => {
  it('can handle numbers less than 10', () => {
    expect(uut.numberToString(0)).toEqual('zero')
    expect(uut.numberToString(1)).toEqual('one')
    expect(uut.numberToString(2)).toEqual('two')
    expect(uut.numberToString(3)).toEqual('three')
    expect(uut.numberToString(4)).toEqual('four')
    expect(uut.numberToString(5)).toEqual('five')
    expect(uut.numberToString(6)).toEqual('six')
    expect(uut.numberToString(7)).toEqual('seven')
    expect(uut.numberToString(8)).toEqual('eight')
    expect(uut.numberToString(9)).toEqual('nine')
  })

  it('can handle non-special case numbers less than 100', () => {
    expect(uut.numberToString(10)).toEqual('ten')
    expect(uut.numberToString(22)).toEqual('twenty two')
    expect(uut.numberToString(33)).toEqual('thirty three')
    expect(uut.numberToString(44)).toEqual('forty four')
    expect(uut.numberToString(55)).toEqual('fifty five')
    expect(uut.numberToString(66)).toEqual('sixty six')
    expect(uut.numberToString(77)).toEqual('seventy seven')
    expect(uut.numberToString(88)).toEqual('eighty eight')
    expect(uut.numberToString(99)).toEqual('ninety nine')
  })

  it('can handle special cases: teens', () => {
    expect(uut.numberToString(11)).toEqual('eleven')
    expect(uut.numberToString(12)).toEqual('twelve')
    expect(uut.numberToString(13)).toEqual('thirteen')
    expect(uut.numberToString(14)).toEqual('fourteen')
    expect(uut.numberToString(15)).toEqual('fifteen')
    expect(uut.numberToString(16)).toEqual('sixteen')
    expect(uut.numberToString(17)).toEqual('seventeen')
    expect(uut.numberToString(18)).toEqual('eighteen')
    expect(uut.numberToString(19)).toEqual('nineteen')
  })

  it('can handle numbers less than 1000', () => {
    expect(uut.numberToString(100)).toEqual('one hundred')
    expect(uut.numberToString(211)).toEqual('two hundred eleven')
    expect(uut.numberToString(322)).toEqual('three hundred twenty two')
  })

  it('can handle higher order magnitudes', () => {
    // thousands
    expect(uut.numberToString(2001)).toEqual('two thousand one')
    expect(uut.numberToString(16534)).toEqual('sixteen thousand five hundred thirty four')
    expect(uut.numberToString(123456)).toEqual('one hundred twenty three thousand four hundred fifty six')

    // millions
    expect(uut.numberToString(1000000)).toEqual('one million')

    // billions
    expect(uut.numberToString(314159265858)).toEqual('three hundred fourteen billion one hundred fifty nine million two hundred sixty five thousand eight hundred fifty eight')
  })
})