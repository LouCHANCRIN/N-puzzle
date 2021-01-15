/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_countcword.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lchancri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/11/10 11:24:02 by lchancri          #+#    #+#             */
/*   Updated: 2018/05/09 14:07:05 by lchancri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/libft.h"

int		ft_countcword(char const *str, char c)
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
