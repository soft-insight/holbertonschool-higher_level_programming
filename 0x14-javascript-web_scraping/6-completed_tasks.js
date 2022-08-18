#!/usr/bin/node

const axios = require('axios').default;
const url = 'https://jsonplaceholder.typicode.com/todos';

axios.get(url)
  .then(function (response) {
    const lgth = response.data.length;
    // console.log(response.data[0].id);
    // console.log(response.data[1]);

    const complJob = {};

    const usId = [];
    for (let i = 0; i < lgth; i++) {
      usId.push(response.data[i].userId);
    }

    const unique = (value, index, self) => {
      return self.indexOf(value) === index;
    };
    const usIdUnique = usId.filter(unique);

    for (let j = 0; j < usIdUnique.length; j++) {
      let idx = 0;
      for (let i = 0; i < lgth; i++) {
        if (response.data[i].userId === usIdUnique[j] && response.data[i].completed === true) {
          idx += 1;
        }
      }
      complJob[j + 1] = idx;
      // console.log(complJob);
    }
    console.log(complJob);
  })
  .catch(function (error) {
    console.log(error.response);
  })
  .then(function () {
  });
