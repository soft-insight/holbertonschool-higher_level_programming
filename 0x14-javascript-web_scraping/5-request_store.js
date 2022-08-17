#!/usr/bin/node

const axios = require('axios').default;
const fs = require('fs');

const url = process.argv[2];
const file = process.argv[3];

axios.get(url)
  .then(function (response) {
    fs.writeFile(file, response.data, 'utf8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  })
  .catch(function (error) {
    console.log(error);
  })
  .then(function () {
  });
