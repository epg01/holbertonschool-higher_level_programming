#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * Form_Recursive - Function that checks if it is a loop or not recursively.
 * @Element: an element of the data structure.
 * @Head: Pointer always in the lead.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */

int Form_Recursive(listint_t *Element, listint_t *Head)
{
	if (!(Element))
		return (0);
	else if (Element->next == Head)
		return (1);
	else
		return (Form_Recursive(Element->next, Head));
}


/**
 * check_cycle - check for a cycle lined list.
 * @head: Pointer data structure.
 * Return: integer.
 */

int check_cycle(listint_t *head)
{
	return (Form_Recursive(head, head));
}
