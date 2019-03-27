/* globals fetch */

function query (selector) {
  return document.querySelector(selector)
}

function queryAll (selector) {
  return document.querySelectorAll(selector)
}

function getWeather (zip) {
  const promise = fetch(
    `http://api.openweathermap.org/data/2.5/weather?zip=${zip},us&appid=dcd19d748f9a4da76524de8ec2bac3f8`
  ).then(function (response) {
    if (!response.ok) {
      throw Error(response.statusText)
    }
    return response.json()
  })
  return promise
}

function updateWeather (zip) {
  getWeather(zip)
    .then(function (weatherData) {
      console.log(weatherData)
      const tempK = weatherData.main.temp
      const tempF = Math.round((tempK - 273.15) * (9 / 5) + 32)
      query('#temperature').innerHTML = `${tempF}&deg; F`

      const weatherDescr = weatherData.weather[0].description
      query('#weather').innerText = weatherDescr

      query('#location').innerText = weatherData.name

      const iconName = weatherData.weather[0].icon
      const iconURL = `http://openweathermap.org/img/w/${iconName}.png`
      const iconHolder = query('#icon-holder')

      // const icon = document.createElement('img')
      // icon.src = iconURL
      // icon.alt = weatherDescr
      // icon.classList.add('icon')

      // const currentIcon = iconHolder.querySelector('.icon')
      // if (currentIcon) {
      //   iconHolder.replaceChild(icon, currentIcon)
      // } else {
      //   iconHolder.appendChild(icon)
      // }
      iconHolder.innerHTML = `<img class="icon" src="${iconURL}" alt="${weatherDescr}">`
    })
}

document.addEventListener('DOMContentLoaded', function () {
  // const updateOverAndOver = function () {
  //   updateWeather()
  //   console.log('update')
  //   setTimeout(updateOverAndOver, 6000)
  // }

  // updateWeather()

  query('#zip').addEventListener('change', function (event) {
    updateWeather(event.target.value)
  })
})
