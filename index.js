const ONES = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
const TENS = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

function numberToString(number) {
  let stringElements = []

  // handle zero
  if(number === 0) {
    return 'zero'
  }

  // handle ones
  stringElements.unshift(ONES[number % 10])

  // handle tens
  number = Math.floor(number / 10)
  stringElements.unshift(TENS[number %10])

  // post-process
  return stringElements.join(' ').trim()
}

module.exports = { numberToString } 