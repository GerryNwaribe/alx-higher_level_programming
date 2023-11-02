#include "lists.h"
/**
 * insert_node - function to insert node in singly list
 * @head: head pointer
 * @number: number node to be inserted
 * Return: pointer to new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node_ptr = *head;
	listint_t *new = NULL;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node_ptr == NULL || node_ptr->n >= number)
	{
		new->next = node_ptr;
		*head = new;
		return (new);
	}

	while (node_ptr && node_ptr->next && node_ptr->next->n < number)
		node_ptr = node_ptr->next;

	new->next = node_ptr->next;
	node_ptr->next = new;

	return (new);
}
