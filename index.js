const ONES = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
const TENS = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
const TEENS = ['', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

function numberToString(number) {
  let stringElements = []

  // handle zero
  if (number === 0) {
    return 'zero'
  }

  // handle teens independently
  if (number % 100 > 10 && number % 100 < 20) {
    stringElements.unshift(TEENS[number % 10])
  } else {
    // handle ones
    stringElements.unshift(ONES[number % 10])

    // handle tens
    number = Math.floor(number / 10)
    stringElements.unshift(TENS[number % 10])
  }

  // post-process
  return stringElements.join(' ').trim()
}

module.exports = { numberToString } 