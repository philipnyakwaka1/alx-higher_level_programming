#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: address of pointer to head node
 * @number: number to be inserted
 * Return: pointer to new node or NULL if fail
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *ptr;
	unsigned int count;

	count = 0;
	ptr = *head;
	if (ptr == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		free(new);
		return (NULL);
	}
	new->n = number;
	new->next = NULL;
	while (ptr != NULL)
	{
		if (ptr->n > number)
			break;
		count++;
		ptr = ptr->next;
	}
	ptr = *head;
	while (count != 1)
	{
		ptr = ptr->next;
		count--;
	}
	new->next = ptr->next;
	ptr->next = new;
	return (new);
}
