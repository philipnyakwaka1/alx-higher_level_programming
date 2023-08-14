#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
#include <stddef.h>
/**
 * list_len - returns the number elements of a list
 * @h: pointer to the first element of the linked list
 * Return: number of elements
 */
int list_len(listint_t *h)
{
	int count;

	count = 0;
	while (h != NULL)
	{
		count++;
		h = h->next;
	}
	return (count);
}
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head pointer
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *ptr;
	int *array1, *array2;
	int len, i, j;

	ptr = *head;
	len = list_len(ptr);
	if (len == 0)
		return (1);
	array1 = malloc(sizeof(int) * len);
	i = 0;
	while (ptr != NULL)
	{
		array1[i] = ptr->n;
		ptr = ptr->next;
		i++;
	}
	array2 = malloc(sizeof(int) * len);
	for (j = 0; j < len; j++)
		array2[j] = array1[j];
	i = len - 1;
	j = 0;
	while (j < len)
	{
		if (array1[j] != array2[i])
			return (0);
		j++;
		i--;
	}
	free(array1);
	free(array2);
	return (1);
}
