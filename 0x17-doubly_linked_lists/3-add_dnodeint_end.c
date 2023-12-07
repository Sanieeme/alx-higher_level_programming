#include "lists.h"
/**
 * add_dnodeint_end - function that add a new node at the end of the list
 * @head: paramenter
 * @n: parmeter
 * Return: newnode
 */
dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
	dlistint_t *newnode;

	newnode = malloc(sizeof(dlistint_t));
	if (newnode == NULL)
	{
		return (newnode);
	}
	newnode->n = n;
	newnode->next = NULL;
	newnode->prev = *head;
	if (head->next != NULL)
	{
		(*head)->next = newnode;
	}
	*head = newnode;
	return (*head);
}
