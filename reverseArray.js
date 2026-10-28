
function arrayReverse (array) {

    for (let number = 0; number < array.length; number++) {

        let start = 0;
        let end = array[number].length - 1;

        while (start < end) {

            let temporaryArray = array[number][start];
            array[number][start] = array[number][end];
            array[number][end] = temporaryArray;

            start++;
            end--;
        }
    }
}

let array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];

reverseArray(array);

console.log(array);
