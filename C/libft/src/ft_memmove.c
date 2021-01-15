/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memmove.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lchancri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/11/08 15:34:13 by lchancri          #+#    #+#             */
/*   Updated: 2018/05/09 14:12:00 by lchancri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/libft.h"

void	*ft_memmove(void *dest, const void *src, size_t n)
{
	size_t	a;

	a = 0;
	if (dest >= (void*)src)
		while (n)
		{
			((char*)dest)[n - 1] = ((char*)src)[n - 1];
			n--;
		}
	else
		while (a < n)
		{
			((char*)dest)[a] = ((char*)src)[a];
			a++;
		}
	return (dest);
}
