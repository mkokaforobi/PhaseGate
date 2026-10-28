
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
	return array;
    }
}

let array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];

arrayReverse(array);

console.log(array);
