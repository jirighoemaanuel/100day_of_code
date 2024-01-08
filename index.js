let url =
  'https://api.sheety.co/9e8f4da9e713d31f33c5798b7f6dff05/copyOfFlightDeals/users';
fetch(url)
  .then((response) => response.json())
  .then((json) => {
    // Do something with the data
    console.log(json.users);
  });
