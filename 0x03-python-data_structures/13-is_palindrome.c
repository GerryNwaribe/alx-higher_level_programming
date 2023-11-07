#include "lists.h"
/**
 * is_palindrome - function to check if list is palindrome
 * @head: pointer to head of list
 * Return: 0
 */
int is_palindrome(listint_t **head)
{

	listint_t *slow_point = *head;
	listint_t *fast_point = *head;
	listint_t *temp_ptr = NULL;
	listint_t *temp_ptr2 = NULL;
	listint_t *second_half_start = NULL;

	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}

	while (fast_point != NULL && fast_point->next != NULL)
	{
		slow_point = slow_point->next;
		fast_point = fast_point->next->next;
	}

	second_half_start = slow_point->next;
	slow_point->next = NULL;

	while (second_half_start != NULL)
	{
		temp_ptr = second_half_start->next;
		second_half_start->next = temp_ptr2;
		temp_ptr2 = second_half_start;
		second_half_start = temp_ptr;
	}
	second_half_start = temp_ptr2;

	while (*head != NULL && second_half_start != NULL)
	{
		if ((*head)->n != second_half_start->n)
			return (0);

		*head = (*head)->next;
		second_half_start = second_half_start->next;
	}
	return (1);
}
