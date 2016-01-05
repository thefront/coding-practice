// from Khan Academy
var insert = function(array, rightIndex, value) {
    for(var j = rightIndex; j >= 0 && array[j] > value; j--) {
        array[j + 1] = array[j];
    }   
    array[j + 1] = value; 
};

var insertionSort = function(array) {
    for (var i = 1; i < array.length; i++) {
        insert(array, i - 1, array[i]);
    }
};

var array = [22, 11, 99, 88, 9, 7, 42];
insertionSort(array);
println("Array after sorting:  " + array);
Program.assertEqual(array, [7, 9, 11, 22, 42, 88, 99]);
var array2 = [74, 45, 87, 1000, 101, -3, -45, 76];
insertionSort(array2);
println("Array after sorting:  " + array2);
Program.assertEqual(array2, [-45, -3, 45, 74, 76, 87, 101, 1000]);

