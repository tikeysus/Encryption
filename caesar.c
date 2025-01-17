//usage key, input_file, output_file

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

int main(int argc, char *argv[]){
	if (argc != 4){
		fprintf(stderr, "Usage: key input_file output_file\n");
		return 1; 
	}
	

	FILE *plaintext = fopen(argv[2], "r"); 
	FILE *ciphertext = fopen(argv[3], "w"); 

	if (plaintext == NULL || ciphertext == NULL){
		fprintf(stderr, "One of the files was null");
		return 1; 
	}


	int key = atoi(argv[1]); 

	char *line = NULL; 
	size_t linecap = 0; 
	ssize_t len; 
	while ((len = getline(&line, &linecap, plaintext)) > 0){
		for (int i = 0; i < len; i++){
			if (isalpha(line[i])){
				char base; 
				if (isupper(line[i])){
					base = 'A'; 
				}
				else{
					base = 'a';
				}
				line[i] = ((line[i] - base + key) % 26) + base;
			}
		}
		fwrite(line, len, 1, ciphertext);
	}

	free(line); 
	fclose(plaintext); 
	fclose(ciphertext); 

}