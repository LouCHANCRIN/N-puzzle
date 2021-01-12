/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcdup.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lchancri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/11/09 18:35:37 by lchancri          #+#    #+#             */
/*   Updated: 2018/05/09 18:46:21 by lchancri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/libft.h"

char	*ft_strcdup(const char *s, char c, int b)
{
	char	*cpy;
	int		a;

	a = 0;
	while (s[b + a] != c && s[b + a] != '\0')
		a++;
	cpy = (char*)malloc(sizeof(char) * (a + 1));
	if (cpy == NULL)
		return (NULL);
	a = 0;
	while (s[b + a] != c && s[b + a] != '\0')
	{
		cpy[a] = s[b + a];
		a++;
	}
	cpy[a] = '\0';
	return (cpy);
}
