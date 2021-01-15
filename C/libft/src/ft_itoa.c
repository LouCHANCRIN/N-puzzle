/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lchancri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/11/09 19:20:36 by lchancri          #+#    #+#             */
/*   Updated: 2018/05/09 19:06:50 by lchancri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/libft.h"

static int	intlen(int a)
{
	int	b;

	b = 0;
	if (a <= 0)
		b++;
	while (a != 0)
	{
		a = a / 10;
		b++;
	}
	return (b);
}

char		*ft_itoa(int n)
{
	int		a;
	long	b;
	char	*str;

	b = n;
	a = intlen(b) - 1;
	str = (char*)malloc(sizeof(char) * (a + 1));
	if (str == NULL)
		return (NULL);
	if (n < 0)
	{
		b = -b;
		str[0] = 45;
	}
	str[a + 1] = '\0';
	while (b >= 10)
	{
		str[a] = b % 10 + 48;
		b = b / 10;
		a--;
	}
	str[a] = b + 48;
	return (str);
}
