#!/usr/bin/node

const axios = require('axios').default;
const url = 'https://jsonplaceholder.typicode.com/todos';

axios.get(url)
  .then(function (response) {
    const lgth = response.data.length;
    // console.log(response.data[0].id);
    // console.log(response.data[1]);

    const complJob = {};

    for (let j = 1; j < 11; j++) {
      let idx = 0;
      for (let i = 0; i < lgth; i++) {
        if (response.data[i].userId === j && response.data[i].completed === true) {
          idx += 1;
        }
      }
      complJob[j] = idx;
      // console.log(complJob);
    }
    console.log(complJob);
  })
  .catch(function (error) {
    console.log(error);
  })
  .then(function () {
  });
