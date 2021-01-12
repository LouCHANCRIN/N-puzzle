/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strrchr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lchancri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/11/08 12:56:06 by lchancri          #+#    #+#             */
/*   Updated: 2018/05/09 14:17:48 by lchancri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/libft.h"

char	*ft_strrchr(const char *s, int c)
{
	char	*s1;
	char	a;
	size_t	b;

	a = (char)c;
	s1 = (char *)s;
	b = 0;
	while (s1[b] != '\0')
		b++;
	while (b > 0)
	{
		if (s1[b] == a)
			return (s1 + b);
		b--;
	}
	if (s1[b] == a)
		return (s1 + b);
	return (NULL);
}
