/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strstr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lchancri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/11/08 13:01:30 by lchancri          #+#    #+#             */
/*   Updated: 2018/05/09 14:18:17 by lchancri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/libft.h"

char	*ft_strstr(const char *h, const char *n)
{
	size_t	a;
	size_t	b;

	a = 0;
	if (n[0] == '\0')
		return ((char*)h);
	while (h[a] != '\0')
	{
		b = 0;
		while (h[a + b] == n[b])
		{
			if (n[b + 1] == '\0')
				return ((char*)h + a);
			b++;
		}
		a++;
	}
	return (NULL);
}
