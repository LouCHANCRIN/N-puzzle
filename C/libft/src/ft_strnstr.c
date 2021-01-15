/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnstr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lchancri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/11/08 13:30:57 by lchancri          #+#    #+#             */
/*   Updated: 2018/05/09 14:17:39 by lchancri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/libft.h"

char	*ft_strnstr(const char *h, const char *n, size_t len)
{
	size_t	a;
	size_t	b;

	a = 0;
	if (n[0] == '\0')
		return ((char*)h);
	while (h[a] != '\0' && len > a)
	{
		b = 0;
		while (h[a + b] == n[b] && a + b < len)
		{
			if (n[b + 1] == '\0' && a < len)
				return ((char*)h + a);
			b++;
		}
		a++;
	}
	return (NULL);
}
