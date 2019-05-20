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
})