/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strrev.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lchancri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/11/09 19:50:17 by lchancri          #+#    #+#             */
/*   Updated: 2018/05/09 18:47:14 by lchancri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/libft.h"

char	*ft_strrev(char *str)
{
	int		a;
	int		b;
	char	c;

	b = 0;
	a = ft_strlen(str) - 1;
	while (a > b)
	{
		c = str[a];
		str[a] = str[b];
		str[b] = c;
		a--;
		b++;
	}
	return (str);
}
