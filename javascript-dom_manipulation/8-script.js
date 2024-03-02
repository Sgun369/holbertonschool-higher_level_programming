document.addEventListener('DOMContentLoaded', function () {
  const url ='https://hellosalut.stefanbohacek.dev/?lang=fr';
  const helloElement = document.getElementById('ello');

  fetch(url)
  .then(response => response.json())
  .then(data => {
    const translatedHello = data.hello;
    helloElement.textContent = translatedHello;
  })
  .catch(error => console.error('Error fetching data:', error));
});
