/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memccpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lchancri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/11/08 15:26:40 by lchancri          #+#    #+#             */
/*   Updated: 2018/05/09 14:11:22 by lchancri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/libft.h"

void	*ft_memccpy(void *dest, const void *src, int c, size_t n)
{
	size_t	a;
	char	*d;
	char	*s;

	a = 0;
	d = (char*)dest;
	s = (char*)src;
	while (n--)
	{
		d[a] = s[a];
		if (s[a] == (char)c)
		{
			a++;
			return (dest + a);
		}
		a++;
	}
	return (NULL);
}
