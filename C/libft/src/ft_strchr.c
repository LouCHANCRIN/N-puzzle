/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lchancri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/11/08 11:51:13 by lchancri          #+#    #+#             */
/*   Updated: 2018/05/09 14:14:39 by lchancri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/libft.h"

char	*ft_strchr(const char *s, int c)
{
	char	a;
	char	*s1;

	a = (char)c;
	s1 = (char*)s;
	while (*s1 != '\0')
	{
		if (*s1 == a)
			return (s1);
		s1++;
	}
	if (*s1 == a)
		return (s1);
	return (NULL);
}
