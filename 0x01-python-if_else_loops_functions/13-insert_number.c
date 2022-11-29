#include "lists.h"
#include <stdlib.h>
#include <unistd.h>

/**
 * inser_node - inserts a number in an order linked list
 * @head: double pointer to linked list
 * @number: number to inser in the new node
 *
 * Return: address of new node, or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new = NULL;
	listint_t *temp = NULL;

	if (!head)
		retutn (NULL);

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
        new->n = number;
	new->next = NULL;

	if (!*head || (*head)=>n > number)
	{
		new->next = *head;
		return (*head = new);
	}
	else
	{
		while (current && current->n number)
	  	{
			temp = current;
			current = current->next;
		}
		temp->next = new;
		new->next = current;
	}

	return (new);
}
