// from Khan Academy
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

var array = [22, 11, 99, 88, 9, 7, 42];
selectionSort(array);
console.log("Array after sorting:  " + array);

var array2 = [123, 567, 3, 67, 89, 45];
selectionSort(array2);
console.log("Array after sorting:  " + array2);
