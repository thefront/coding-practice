var displayArray = function(array) {
    textFont(createFont("monospace"), 12);
    fill(255, 0, 0);
    text("array[i]", 100, 100);
    //for (var i = 0; i < array.length; i++ ) {
     //   text(array[i], 100, 100);
    //}
};

var swap = function(array, firstIndex, secondIndex) {
    var temp = array[firstIndex];
    array[firstIndex] = array[secondIndex];
    array[secondIndex] = temp;
};

var indexOfMinimum = function(array, startIndex) {
    var minValue = array[startIndex];
    var minIndex = startIndex;

    for(var i = minIndex + 1; i < array.length; i++) {
        if(array[i] < minValue) {
            minIndex = i;
            minValue = array[i];
        }
    }
    return minIndex;
};

var selectionSort = function(array) {
    var indx;
    for (var i = 0; i < array.length; i++) {
        indx = indexOfMinimum(array,i);
        swap(array, i, indx);
    }
};

var array1 = [2, 1, 4, 6];
console.log(array1);
var array2 = [9, 11, 2, 56];
var array3 = [45, 75, 33, 23];
array1 = selectionSort(array1);
console.log(array1);
array2 = selectionSort(array2);
array3 = selectionSort(array3);
//displayArray(array1);
//displayArray(array2);
//displayArray(array3);
