#include "isogram.h"
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

bool is_isogram(const char phrase[])
{
	for(int i = 0; phrase[i] != '\0'; i++){
		for(int j = i; phrase[j] != '\0'; j++){
			if(phrase[i] == phrase[j]){
				return false;
			}
		}
	}
	return true;
}
