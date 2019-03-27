var error = false

function setErrorState () {
  setOutput('ERROR')
  error = true
}

function getDisplay () {
  return document.getElementById('display')
}

function getOutput () {
  return getDisplay().innerText
}

function addToOutput (str) {
  getDisplay().innerText += str
}

function setOutput (str) {
  clearOutput()
  addToOutput(str)
}

function clearOutput () {
  error = false
  getDisplay().innerText = ''
}

function calculateCurrentOutput () {
  return eval(getDisplay().innerText)
}

function precisionRound (number, precision) {
  var factor = Math.pow(10, precision)
  return Math.round(number * factor) / factor
}

function setupNumberButtons () {
  for (let element of document.querySelectorAll('.number')) {
    element.addEventListener('click', function (event) {
      if (!error) { addToOutput(event.target.innerText) }
    })
  }
}

function setupOperatorButtons () {
  document.querySelectorAll('.operator').forEach(function (element) {
    element.addEventListener('click', function (event) {
      if (!error) { addToOutput(event.target.innerText) }
    }
    )
  })
}

function setupClearButton () {
  document.getElementById('clear').addEventListener('click', function (event) {
    clearOutput()
  })
}

function isOperator (str) {
  return (str === '+' || str === '-' || str === '*' || str === '/')
}

function setupDecimalButton () {
  document.getElementById('decimal').addEventListener('click', function (event) {
    if (!error) {
      var output = getOutput()

      if (output === '' || isOperator(output.charAt(output.length - 1))) {
        addToOutput('0.')
        return
      }

      var canAddDecimal = true

      for (var idx = output.length - 1; idx >= 0; idx--) {
        var char = output.charAt(idx)
        if (char === '.') {
          canAddDecimal = false
          break
        } else if (isOperator(char)) {
          break
        }
      }

      if (canAddDecimal) {
        addToOutput('.')
      }
    }
  })
}

function setupEqualsButton () {
  document.getElementById('operator-equals').addEventListener('click', function (event) {
    if (!error) {
      try {
        var result = calculateCurrentOutput()
        clearOutput()
        addToOutput(precisionRound(result, 5))
      } catch (ex) {
        setErrorState()
      }
    }
  })
}

document.addEventListener('DOMContentLoaded', function () {
  setupNumberButtons()
  setupOperatorButtons()
  setupClearButton()
  setupDecimalButton()
  setupEqualsButton()
})
