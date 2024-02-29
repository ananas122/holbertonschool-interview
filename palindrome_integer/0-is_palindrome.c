#include "palindrome.h"


/**
* is_palindrome - Check if a given unsigned integer is a palindrome
*
* Return: 1 if n is a palindrome 
*/

int is_palindrome(unsigned long n)
{
    unsigned long reversed = 0, digit = n;

    while (n != 0)
    {
        
        reversed = reversed * 10 + n % 10;
        n /= 10;
    }
    return (digit == reversed ? 1 : 0);
}
