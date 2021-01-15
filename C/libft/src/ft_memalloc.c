/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memalloc.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lchancri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/11/09 13:54:49 by lchancri          #+#    #+#             */
/*   Updated: 2018/05/09 18:44:33 by lchancri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/libft.h"

void	*ft_memalloc(size_t size)
{
	void	*a;

	a = (void*)malloc(sizeof(void) * size);
	if (a == NULL)
		return (NULL);
	ft_memset(a, 0, size);
	return (a);
}
