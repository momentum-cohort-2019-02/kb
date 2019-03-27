'use strict'

const MAX = 100
let low = 1
let high = MAX
let guess

function newGuess () {
  guess = generateGuess(low, high)
  document.querySelector('#output').innerText = `Is your number ${guess}?`
}

function makeOptions () {
  const optionsDiv = document.querySelector('#options')
  const buttonClasses = 'f6 link dim br3 ba bw2 ph3 pv2 mb2 dib navy'.split(' ')

  const greaterButton = document.createElement('button')
  greaterButton.innerText = 'My number is bigger'
  greaterButton.addEventListener('click', function () {
    low = guess + 1
    newGuess()
  })

  const lesserButton = document.createElement('button')
  lesserButton.innerText = 'My number is smaller'
  lesserButton.addEventListener('click', function () {
    high = guess - 1
    newGuess()
  })

  const equalButton = document.createElement('button')
  equalButton.innerText = "That's my number!"
  equalButton.addEventListener('click', function () {
    optionsDiv.innerHTML = '<h3>I guessed it!</h3>'
  })

  optionsDiv.appendChild(greaterButton)
  optionsDiv.appendChild(lesserButton)
  optionsDiv.appendChild(equalButton)

  for (let button of optionsDiv.querySelectorAll('button')) {
    for (let cssClass of buttonClasses) {
      button.classList.add(cssClass)
    }
  }
  console.log('option buttons', optionsDiv.querySelectorAll('button'))
}

function generateGuess (low, high) {
  return Math.floor((low + high) / 2)
}

function main () {
  document.querySelector('#max-num').innerText = MAX
  makeOptions()
  newGuess()
}

document.addEventListener('DOMContentLoaded', main)
