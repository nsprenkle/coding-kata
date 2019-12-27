const ONES = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
const TENS = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
const TEENS = ['', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
const MAGNITUEDS = ['', 'thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion', 'sextillion', 'septilion', 'octillion', 'nonillion', 'decillion', 'undecillion', 'duodecillion', 'tredecillion', 'quattuordecillion', 'quindecillion', 'sexdecillion', 'septdecillion', 'septendecillion', 'octodecillion', 'novemdecillion', 'vigintillion']

function numberToString(number) {
  let stringElements = []
  let magnitudeIndex = 0
  let partialNumber = 0

  // handle zero
  if (number === 0) {
    return 'zero'
  }

  // process the next order of magnitude
  while (number > 0) {
    partialNumber = number % 1000

    if (partialNumber !== 0) {
      stringElements.unshift(MAGNITUEDS[magnitudeIndex])
      stringElements.unshift(...handleMagnitude(partialNumber))
    }

    number = Math.floor(number / 1000)
    magnitudeIndex++
  }

  // post-process
  return stringElements.filter(val => { return val && val.length > 0 }).join(' ').trim()
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