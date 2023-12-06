#include "lists.h"
/**
 * insert_node - inserts a number
 * @head: pararmeter
 * @number: parameter
 * Return: new node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *node = NULL, *temp = NULL;

	new = *head;

	if (head == NULL)
		return (NULL);
	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);
