#include "armstrong_numbers.h"
#include <math.h>

bool is_armstrong_number(int candidate){
	//get num digits
	int numDigits = 0;
	int temp = candidate;
	for(numDigits = 0; temp != 0; numDigits++){ temp = temp/10; }

	//sum products
	int sum = 0;
	temp = candidate;
	for(int i = 0; i < numDigits; i++){
		int digit = temp % 10;
		int product = (int)pow(digit, numDigits);
		
		sum += product;
		temp = temp/10;
	}
	return candidate == sum;
}