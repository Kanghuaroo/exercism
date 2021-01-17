#include "armstrong_numbers.h"

int is_armstrong_number(int candidate){
	//get num digits
	int numDigits = 0;
	int temp = candidate;
	for(numDigits = 0; temp != 0; temp = temp/10){ numDigits++; }

	//sum products
	int sum = 0;
	temp = candidate;
	for(int i = 0; i < numDigits; i++){
		int digit = temp % 10;
		int product = digit;
		//power
		for(int j = 1; j < numDigits; j++){
			product = product * digit;
		}
		sum += product;
		temp = temp/10;
	}
	return candidate == sum;
}
