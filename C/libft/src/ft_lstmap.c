/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstmap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lchancri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/11/10 18:03:59 by lchancri          #+#    #+#             */
/*   Updated: 2018/05/09 18:44:16 by lchancri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/libft.h"

t_list	*ft_lstmap(t_list *lst, t_list *(*f)(t_list *elem))
{
	t_list	*list;
	t_list	*beginlist;

	list = (t_list *)malloc(sizeof(t_list *));
	beginlist = NULL;
	if (lst != NULL)
	{
		list = f(lst);
		beginlist = list;
		lst = lst->next;
	}
	while (lst != NULL)
	{
		list->next = f(lst);
		lst = lst->next;
		list = list->next;
	}
	list = NULL;
	return (beginlist);
}
