#!/usr/bin/node

const axios = require('axios').default;

const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;

axios.get(url)
  .then(function (response) {
    console.log(response.data.title);
  })
  .catch(function (error) {
    console.log(error);
  })
  .then(function () {
  });
