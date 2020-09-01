#include "lists.h"

/**
 * check_cycle -  function in C that checks if a singly linked list
 *                has a cycle in it.
 * @list: Data structure.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */

int check_cycle(listint_t *list)
{
	if (!list)
		return (0);
	else
	{
		listint_t *pointer = list;

		while (list->next)
			if (pointer == list->next)
				return (1);
			else
				list = list->next;
		return (0);
	}
}
