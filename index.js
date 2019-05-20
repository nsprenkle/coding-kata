function numberToString(number) {
  let string = ''

  if (number === 0) { return 'zero' }

  switch (Math.floor(number / 10)) {
    case 0:
      break
    case 1:
      string += 'ten'
      break
    case 2:
      string += 'twenty'
      break;
    case 3:
      string += 'thirty'
      break
    case 4:
      string += 'fourty'
      break
    case 5:
      string += 'fifty'
      break
    case 6:
      string += 'sixty'
      break
    case 7:
      string += 'seventy'
      break
    case 8:
      string += 'eighty'
      break
    case 9:
      string += 'ninety'
      break
  }

  switch (number % 10) {
    case 0:
      break
    case 1:
      string += ' one'
      break
    case 2:
      string += ' two'
      break
    case 3:
      string += ' three'
      break
    case 4:
      string += ' four'
      break
    case 5:
      string += ' five'
      break
    case 6:
      string += ' six'
      break
    case 7:
      string += ' seven'
      break
    case 8:
      string += ' eight'
      break
    case 9:
      string += ' nine'
      break
  }

  return string.trim()
}

module.exports = { numberToString } 