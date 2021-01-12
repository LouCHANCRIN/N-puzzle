/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strsplit.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lchancri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/11/09 18:05:34 by lchancri          #+#    #+#             */
/*   Updated: 2018/05/09 18:47:41 by lchancri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/libft.h"

static char	*strcdup(const char *s, char c, int b)
{
	char	*cpy;
	int		a;

	a = 0;
	while (s[b + a] != c && s[b + a] != '\0')
		a++;
	if (!(cpy = (char*)malloc(sizeof(char) * (a + 2))))
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

static int	countcword(char const *str, char c)
{
	int	a;
	int	b;

	a = 0;
	b = 1;
	while (str[a] != '\0')
	{
		if (str[a] == c && str[a + 1] != c)
			b++;
		a++;
	}
	return (b);
}

char		**ft_strsplit(char const *s, char c)
{
	int		a;
	int		b;
	char	**tab;

	if (s == NULL)
		return (NULL);
	a = 0;
	b = 0;
	tab = (char **)malloc(sizeof(char **) * (countcword(s, c) + 1));
	if (tab == NULL)
		return (NULL);
	while (s[a] != '\0')
	{
		if (s[a] != c)
		{
			tab[b] = strcdup(s, c, a);
			while (s[a] != c && s[a] != '\0')
				a++;
			b++;
		}
		if (s[a] != '\0')
			a++;
	}
	tab[b] = 0;
	return (tab);
}
