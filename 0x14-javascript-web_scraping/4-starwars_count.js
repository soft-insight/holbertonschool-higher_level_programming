#!/usr/bin/node

const axios = require('axios').default;

const antilles = 'https://swapi-api.hbtn.io/api/people/18/';
const url = process.argv[2];

axios.get(url)
  .then(function (response) {
    let movie = 0;
    for (let i = 0; i < response.data.results.length; i++) {
      if (response.data.results[i].characters.includes(antilles)) {
        movie += 1;
      }
    }
    console.log(movie);
  })
  .catch(function (error) {
    console.log(error);
  })
  .then(function () {
  });