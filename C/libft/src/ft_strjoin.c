/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lchancri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/11/09 15:59:58 by lchancri          #+#    #+#             */
/*   Updated: 2018/05/09 18:46:47 by lchancri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/libft.h"

char	*ft_strjoin(char const *s, char const *t)
{
	size_t	a;
	size_t	b;
	char	*c;

	if (s == NULL || t == NULL)
		return (NULL);
	if (!(c = (char*)malloc(sizeof(char) * (ft_strlen(s) + ft_strlen(t) + 1))))
		return (NULL);
	a = 0;
	b = 0;
	while (s[a] != '\0')
	{
		c[a] = s[a];
		a++;
	}
	while (t[b] != '\0')
	{
		c[a + b] = t[b];
		b++;
	}
	c[a + b] = '\0';
	return (c);
}
