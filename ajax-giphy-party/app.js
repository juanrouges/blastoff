console.log("Let's get this party started!");

const form = document.querySelector('#form');
const giphy = document.querySelector('#giphy');
const submit = document.querySelector('#submit');
const clear = document.querySelector('#clear');
const results = document.querySelector('#results');

async function formSubmit(evt, query) {
  evt.preventDefault();

  if (!query) {
    return alert('Please enter a value');
  }

  try {
    const res = await axios.get(`http://api.giphy.com/v1/gifs/search?q=${query}&api_key=MhAodEJIJxQMxW9XqxKjyXfNYdLoOIym`);

    const img = document.createElement('img');
    img.src = res.data.data[0].images.original.url;

    giphy.value = '';

    results.append(img);
  } catch (err) {
    console.log(err)
  }
}

submit.addEventListener('click', function(evt) {
  formSubmit(evt, giphy.value);
})

clear.addEventListener('click', function(evt) {
  evt.preventDefault();
  results.innerHTML = '';
})