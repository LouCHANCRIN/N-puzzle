/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstdel.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lchancri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/11/10 17:05:12 by lchancri          #+#    #+#             */
/*   Updated: 2018/05/09 14:10:17 by lchancri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/libft.h"

void	ft_lstdel(t_list **alst, void (*del)(void *, size_t))
{
	t_list	*list;
	t_list	*list2;

	list = *alst;
	while (list != NULL)
	{
		list2 = list;
		list = list->next;
		del(list2->content, list2->content_size);
		free(list2);
	}
	*alst = NULL;
}
