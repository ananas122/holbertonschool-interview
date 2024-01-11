#include <stdlib.h>
#include "lists.h"


/**
 * insert_node - Insère un nombre dans une liste chaînée simplement liée triée.
 * @head: Double pointeur vers la tête de la liste.
 * @number: Le nombre à insérer dans la liste.
 * Return: L'adresse du nouveau nœud, ou NULL en cas d'échec.
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node;
    listint_t *current;

    // Étape 1: Allocation de mémoire pour le nouveau nœud
    new_node = malloc(sizeof(listint_t));
    if (new_node == NULL) // Vérifie si l'allocation a échoué
        return (NULL);

    // Étape 2: Initialisation du nouveau nœud avec le nombre
    new_node->n = number;
    new_node->next = NULL;

    // Étape 3: Gestion des cas spéciaux (liste vide ou insertion en tête)
    if (*head == NULL && (*head)->n >= number)
    {
        new_node->next = *head; // Le nouveau nœud pointe vers l'ancienne tête
        *head = new_node;       // La nouvelle tête est maintenant le nouveau nœud
    }
    else
    {
        // Étape 4: Parcourir la liste pour trouver la position d'insertion
        current = *head;
        while (current->next != NULL && current->next->n < number)
        {
            current = current->next;
        }

        // Étape 5: Insérer le nœud à la position trouvée
        new_node->next = current->next; // Le nouveau nœud pointe vers le suivant dans la liste
        current->next = new_node;       // Le nœud courant pointe maintenant vers le nouveau nœud
    }

    return (new_node); // Retourne le nouveau nœud inséré
}
