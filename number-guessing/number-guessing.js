const readline = require('readline')
const rl = readline.createInterface(process.stdin, process.stdout)

let testCases, lowerBound, upperBound, numberOfGuesses, guess

let step = 'start'
let testNumber = 0

rl.on('line', (line) => {
  switch (step) {
    case 'start':
      testCases = Number(line)
      step = 'bounds'
      break
    case 'bounds':
      lowerBound = Number(line.split(' ')[0])
      upperBound = Number(line.split(' ')[1])
      step = 'numberOfGuesses'
      break
    case 'numberOfGuesses':
      numberOfGuesses = Number(line)
      generateGuess(lowerBound, upperBound)
      step = 'guess'
      break
    case 'guess':
      if (line === 'TOO_SMALL') {
        lowerBound = guess
        generateGuess(lowerBound, upperBound)
      } else if (line === 'TOO_BIG') {
        upperBound = guess
        generateGuess(lowerBound, upperBound)
      } else if (line === 'CORRECT') {
        testNumber++
        if (testNumber >= testCases) { rl.close() }
        step = 'bounds'
      } else {
        rl.close()
      }
      break
  }
}).on('close', () => {
  process.exit()
})

function generateGuess (low, high) {
  guess = Math.ceil(low + (high - low) / 2)
  console.log(guess)
}
