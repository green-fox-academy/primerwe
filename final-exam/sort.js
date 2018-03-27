function returnSecondBiggestItem(arr) {
  function sortArray() {
    const len = arr.length;
    for (let i = 0; i < len; i++) {
      let maxIndex = i;
      for (let j = i + 1; j < len; j++) {
        if (arr[j] > arr[maxIndex]) {
          maxIndex = j;
        }
      }
      const temp = arr[i];
      arr[i] = arr[maxIndex];
      arr[maxIndex] = temp;
    }
    return arr;
  }
  return sortArray(arr)[1];
}

console.log(returnSecondBiggestItem([4, 2, 1, 5, 3]));

module.exports = {
  returnSecondBiggestItem,
};
