function double(arr) {
  return arr.map(function(val) {
    return val * 2;
  });
}

/* Write an ES2015 Version */
const double = (arr) => arr.map((val) => val * 2);