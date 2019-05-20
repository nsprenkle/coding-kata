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
    expect(uut.numberToString(44)).toEqual('fourty four')
    expect(uut.numberToString(55)).toEqual('fifty five')
    expect(uut.numberToString(66)).toEqual('sixty six')
    expect(uut.numberToString(77)).toEqual('seventy seven')
    expect(uut.numberToString(88)).toEqual('eighty eight')
    expect(uut.numberToString(99)).toEqual('ninety nine')
  })
})