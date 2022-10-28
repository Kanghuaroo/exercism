#include "isogram.h"
#include <stddef.h>
#include <ctype.h>


bool is_isogram(const char phrase[]){
	if(phrase == NULL){return false;}

	for(int i = 0; phrase[i] != '\0'; i++){
		if(!isalpha(phrase[i])){ continue; }

		for(int j = i+1; phrase[j] != '\0'; j++){
			if(tolower(phrase[i]) == tolower(phrase[j])){
				return false;
			}
		}
	}
	return true;
}
