/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lchancri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/11/08 10:30:31 by lchancri          #+#    #+#             */
/*   Updated: 2018/05/09 14:16:11 by lchancri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/libft.h"

size_t	ft_strlcat(char *dest, const char *src, size_t size)
{
	size_t	a;

	a = ft_strlen(dest);
	if (a >= size)
		return (size + ft_strlen(src));
	dest = ft_strncat(dest, src, size - a - 1);
	return (a + ft_strlen(src));
}
