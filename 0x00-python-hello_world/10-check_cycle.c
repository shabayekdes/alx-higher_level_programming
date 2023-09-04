#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: If there is no cycle - 0.
 *         If there is a cycle - 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *temp, *l;

	if (list == NULL || list->next == NULL)
		return (0);

	temp = list->next;
	l = list->next->next;

	while (temp && l && l->next)
	{
		if (temp == l)
			return (1);

		temp = temp->next;
		l = l->next->next;
	}

	return (0);
}
