#include "lists.h"
/**
 * dlistint_len - returns the number of elements in a list
 * @h: paramenter
 * Return: number of elements
 */
size_t dlistint_len(const dlistint_t *h)
{
	size_t size = 0;

	while (h != NULL)
	{
		h = h->next;
		size++;
	}
	return(size);
}
