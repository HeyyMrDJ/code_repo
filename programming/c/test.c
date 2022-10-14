#include <stdio.h>
#include <stdlib.h>

int generaterandomnumber(int range){
    //Seed Random Number Generator with time
    srand(time(0));
    //Generate and return a random number
    int randomrange = 10;
    int randomnumber = rand()%randomrange;
    return randomnumber;
}

int checkguess(int *tries, int randomnumber, int guess){
    *tries -= 1;
    printf("Please enter a number between 1 and 10: ");
    scanf("%d", &guess);

    while (tries > 0){
        if (guess == randomnumber){
            printf("Congrats! You have correctly guessed the number");
            return 0;
        }
        else {
            printf("Sorry, the number you guessed is not correct.\n");
            
        }
    }

    if (tries == 0){
        printf("Sorry you have failed. The correct number was %d\n", randomnumber);
        printf("GAME OVER!!!");
    }
    return 0;    
}

int main()
{
    int tries = 3;
    int guess = 0;
    int randomnumber = generaterandomnumber(10);

    printf("Welcome to a guessing game.\n");
 
    checkguess(&tries, randomnumber, guess);
           
    return 0;
}