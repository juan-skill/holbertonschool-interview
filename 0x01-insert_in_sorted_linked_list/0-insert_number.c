#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 *
 * @head: pointer to pointer of first element of listint_t list
 * @number: integer to be sort
¨*
 * Return: address of the new element or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL, *current = NULL;

	current = *head;

	new = (listint_t *) malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
	}
	else if (current->n > new->n)
	{
		new->next = current;
		*head = new;
	}
	else
	{
		while (current->next != NULL && current->next->n < new->n)
			current = current->next;

		new->next = current->next;
		current->next = new;
	}

	return (new);
}
