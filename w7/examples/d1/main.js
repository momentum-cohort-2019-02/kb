const MAX = 1000

console.log("Let's play a game!")
console.log(`Please pick a number between 1 and ${MAX}.`)
console.log("When you're ready to start, type 'play()'!")

function play () {
  let low = 1
  let high = MAX
  while (true) {
    let guess = generateGuess(low, high)
    let input = window.prompt(`Is your number ${guess}? Type '>' if it's bigger than that, '<' if it's less, and '=' if it's equal.`)
    if (input === '>') {
      low = guess + 1
    } else if (input === '<') {
      high = guess - 1
    } else if (input === '=') {
      console.log('I guessed it!')
      break
    } else if (input === null) {
      break
    } else {
      console.log(`I don't know what to do with '${input}'.`)
    }
  }
}

function generateGuess (low, high) {
  return Math.floor((low + high) / 2)
}
