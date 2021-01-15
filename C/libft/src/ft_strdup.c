/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lchancri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/11/07 17:33:49 by lchancri          #+#    #+#             */
/*   Updated: 2018/05/09 19:07:25 by lchancri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/libft.h"

char	*ft_strdup(const char *s)
{
	char			*cpy;
	unsigned int	a;
	unsigned int	b;

	a = 0;
	b = ft_strlen(s);
	cpy = (char*)malloc(sizeof(char) * (b + 1));
	if (cpy == NULL)
		return (NULL);
	while (a < b)
	{
		cpy[a] = s[a];
		a++;
	}
	cpy[a] = '\0';
	return (cpy);
}
