#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * Form_Recursive - Function that checks if it is a loop or not recursively.
 * @Element: an element of the data structure.
 * @Head: Pointer always in the lead.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */

int recursiva(listint_t *Tortuga, listint_t *Conejto)
{
  
        if (!Tortuga || !Conejto) // Element == NULL
		return (0);
        else if (Tortuga == Conejto)
		return (1);
        else
                return (recursiva(Tortuga->next, Conejto->next->next));
}
int check_cycle(listint_t *head)
{
	recursiva(head, head->next->next);
  
}
