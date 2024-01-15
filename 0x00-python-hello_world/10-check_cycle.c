
#include "lists.h"

/**
 * check_cycle - check if you can make a cycle traversing the list
 * @list: head of the list
 * Description - check for the loop
 * Return: 1 if cycle and 0 otherwise
*/

int check_cycle(listint_t *list)
{
    listint_t *slow, *fast;
    
    slow = list;
    fast = list;

    while( fast && fast->next )
    {
        slow = slow->next;
        fast = fast->next->next;
        
        if( slow == fast )
        {
            return (1);
        }
        slow = slow->next;
        fast = fast->next->next;
    }
    return (0);
}