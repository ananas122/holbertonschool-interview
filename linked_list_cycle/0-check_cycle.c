#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
* main: 
*
* Return: Always 0.
*/

int check_cycle(listint_t *list) {
    /* Déclaration et initialisation des pointeurs rapides */
    listint_t *slow = list;
    listint_t *fast = list;

    /* Parcours de la liste jusqu'à ce que fast atteigne la fin de la liste */
    while (fast != NULL && fast->next != NULL) {
        /* Déplacement du pointeur lent d'une étape */
        slow = slow->next;
        /* Déplacement du pointeur rapide de deux étapes */
        fast = fast->next->next;

        /* Si les pointeurs se rencontrent à un certain moment, il y a un cycle */
        if (slow == fast) {
            return 1; /* Cycle détecté */
        }
    }

    /* S'il n'y a pas de cycle, retourne 0 */
    return 0;
}



