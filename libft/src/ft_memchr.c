/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lchancri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/11/08 16:23:44 by lchancri          #+#    #+#             */
/*   Updated: 2018/05/09 14:11:31 by lchancri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/libft.h"

void	*ft_memchr(const void *s, int c, size_t n)
{
	char			*s1;

	s1 = (char*)s;
	while (n--)
	{
		if (*s1 == (char)c)
			return (s1);
		s1++;
	}
	return (NULL);
}
