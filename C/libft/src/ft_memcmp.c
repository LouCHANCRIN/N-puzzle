/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcmp.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lchancri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/11/08 16:27:37 by lchancri          #+#    #+#             */
/*   Updated: 2018/05/09 14:11:37 by lchancri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/libft.h"

int		ft_memcmp(const void *s1, const void *s2, size_t n)
{
	size_t	a;
	char	*d;
	char	*e;

	a = 0;
	d = (char*)s1;
	e = (char*)s2;
	while (n--)
	{
		if (d[a] != e[a])
			return ((unsigned char)d[a] - (unsigned char)e[a]);
		a++;
	}
	return (0);
}
