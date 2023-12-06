#include "lists.h"
/**
 * is_palindrome - chackes if a singly list is a palindrome
 * @head: parameter
 * Return: 0 0r 1
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || head == NULL)
		return (1);
	return (pal(head, *head));
}
/**
 * pal - function
 * @head: parameter
 * @new: parameter
 */
int pal(listint_t **head, listint_t *new)
{
	if (new == NULL)
		return (1);
	if (pal(head, new->next) && (*head)->n == new->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
