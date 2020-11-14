const sortArrayOfObjects = function (array, key) {
  array.sort(function (value1, value2) {
    if (value1[key] > value2[key]) {
      return -1;
    }
    if (value1[key] < value2[key]) {
      return 1;
    }
    return 0;
  });
  return array;
};

export default sortArrayOfObjects;
