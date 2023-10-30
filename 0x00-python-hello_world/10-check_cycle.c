#include "lists.h"
/**
 * check_cycle - finds the loop in a linked list
 * @list: head pointer
 * Return: 0
 */
int check_cycle(listint_t *list)
{
	listint_t *slow_point = list;
	listint_t *fast_point = list;

	while (slow_point && fast_point && fast_point->next)
	{
		slow_point = slow_point->next;       /* Move the tortoise one step */
		fast_point = fast_point->next->next;        /* Move the hare two steps */

		if (slow_point == fast_point)           /* If they meet, there is a loop */
		{
			/* Move one of the pointers to the head and start again */
			slow_point = list;
			while (slow_point != fast_point)
			{
				slow_point = slow_point->next;
				fast_point = fast_point->next;
			}
			return (1); /* Return the node where the loop starts */
		}
	}

	return (0); /* No loop found */
}
