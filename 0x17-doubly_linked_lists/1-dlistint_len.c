#include "lists.h"
/**
 * dlistint_len - function that returns the number of elements
 * @h: head pointer
 * Return: number of nodes
 */
size_t dlistint_len(const dlistint_t *h)
{
	const dlistint_t *temp = h;
	size_t n = 0;

	while (temp != NULL)
	{
		temp = temp->next;
		n++;
	}
	return (n);
}
