// Khan Academy

var factorial = function(n) {
	// base case: 
    if (n === 0) {
        return 1;
    }	
	// recursive case:
	return n * factorial(n - 1);
}; 

println("The value of 0! is " + factorial(0) + ".");
println("The value of 5! is " + factorial(5) + ".");

#Program.assertEqual(factorial(0), 1);
#Program.assertEqual(factorial(5), 120);
#Program.assertEqual(factorial(6), 720);
#Program.assertEqual(factorial(3), 6);

// sample #2 resursive powers x to power n
var isEven = function(n) {
    return n % 2 === 0;
};

var isOdd = function(n) {
    return !isEven(n);
};

var power = function(x, n) {
    println("Computing " + x + " raised to power " + n + ".");
    // base case
    if (n === 0) {
        return 1;
    }
    // recursive case: n is negative
    if (n < 0) {
        return 1 / (power(x, -n));
    }
    // recursive case: n is odd
    if (isOdd(n)) {
        return x * power(x, n - 1); 
    }
    // recursive case: n is even
    if (isEven(n)) {
        var y = power(x, (n / 2));
        return y * y;
    }
};

var displayPower = function(x, n) {
    println(x + " to the " + n + " is " + power(x, n));
};

displayPower(3, 0);
Program.assertEqual(power(3, 0), 1);
displayPower(3, 1);
Program.assertEqual(power(3, 1), 3);
displayPower(3, 2);
Program.assertEqual(power(3, 2), 9);
displayPower(3, -1);
Program.assertEqual(power(3, -1), 1/3);
displayPower(4, 2);
Program.assertEqual(power(4, 2), 16);
displayPower(6, 3);
Program.assertEqual(power(6, 3), 216);

