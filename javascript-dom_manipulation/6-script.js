const url = fetch('https://swapi-api.hbtn.io/api/people/5/?format=json').then(res =>{
    return res.json();
}).then(data =>{
    const character = document.getElementById('character');
    character.textContent = JSON.stringify(data);
})