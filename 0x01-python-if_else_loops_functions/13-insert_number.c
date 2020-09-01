#include "lists.h"

listint_t *insert_node(listint_t **head, int Number)
{
	if (!(*head))
		return (NULL);
	else if (!((*head)->next) || ((*head)->next->n > Number))
	{
		listint_t *New_Nodo;

		New_Nodo = (listint_t *)malloc(sizeof(listint_t));

		if (!(New_Nodo))
			return (NULL);

		New_Nodo->n    = Number;

		New_Nodo->next = (*head)->next;
		(*head)->next  = New_Nodo;
		return (New_Nodo);
	}
	else
		return (insert_node(&(*head)->next, Number));
}
