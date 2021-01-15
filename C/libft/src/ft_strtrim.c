/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lchancri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/11/09 16:22:42 by lchancri          #+#    #+#             */
/*   Updated: 2018/05/09 18:48:22 by lchancri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/libft.h"

static int	firstwordindex(const char *s)
{
	int	a;

	a = 0;
	while (s[a] == '\t' || s[a] == '\n' || s[a] == ' ')
		a++;
	return (a);
}

static int	lastcharindex(const char *s)
{
	int	a;

	a = 0;
	while (s[a] != '\0')
		a++;
	a--;
	while ((s[a] == '\t' || s[a] == '\n' || s[a] == ' ') && a > 0)
		a--;
	return (a);
}

char		*ft_strtrim(char const *s)
{
	size_t	a;
	size_t	b;
	size_t	c;
	char	*str;

	if (s == NULL)
		return (NULL);
	a = firstwordindex(s);
	b = lastcharindex(s);
	c = 0;
	str = (char*)malloc(sizeof(char) * (ft_strlen(s) + 1));
	if (str == NULL)
		return (NULL);
	if (s[a] == '\0')
	{
		str[0] = '\0';
		return (str);
	}
	if (b <= a)
		return (str);
	while (a <= b)
		str[c++] = s[a++];
	str[c] = s[a];
	str[c] = '\0';
	return (str);
}
