const ONES = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
const TENS = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
const TEENS = ['', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
const MAGNITUEDS = ['', 'thousand']

function numberToString(number) {
  let stringElements = []
  let magnitude = 1000
  let partialNumber = 0

  // handle zero
  if (number === 0) {
    return 'zero'
  }

  // get the partial (within 1000) for processing
  partialNumber = number % 1000
  stringElements.unshift(...handleMagnitude(partialNumber))

  // process the next order of magnitude
  number = Math.floor(number / 1000)
  if(number > 0) {
    partialNumber = number % 1000
    stringElements.unshift('thousand')
    stringElements.unshift(...handleMagnitude(partialNumber))
  }

  // post-process
  return stringElements.filter(val => { return val.length > 0 }).join(' ').trim()
}

function handleMagnitude(number) {
  let stringElements = []
  // handle teens independently
  if (number % 100 > 10 && number % 100 < 20) {
    stringElements.unshift(TEENS[number % 10])
    number = Math.floor(number / 10)
  } else {
    // handle ones
    stringElements.unshift(ONES[number % 10])

    // handle tens
    number = Math.floor(number / 10)
    stringElements.unshift(TENS[number % 10])
  }

  // handle hundreds
  number = Math.floor(number / 10)

  if (number > 0) {
    stringElements.unshift('hundred')
    stringElements.unshift(ONES[number % 10])
  }

  return stringElements
}

module.exports = { numberToString } 