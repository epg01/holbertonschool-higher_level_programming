#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * check_cycle - check for a cycle lined list
 * @list: pointer to head node
 *
 * Return: integer
 */
int check_cycle(listint_t *head)
{
	listint_t *hare = head;
	listint_t *turtle = head;

	while (head && hare->next && hare->next->next)
	{
		hare = hare->next->next;
		turtle = turtle->next;
		if (turtle == hare)
			return (1);
	}
	return (0);
}
