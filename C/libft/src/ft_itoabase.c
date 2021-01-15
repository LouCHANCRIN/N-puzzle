/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoabase.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lchancri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/11/30 11:54:33 by lchancri          #+#    #+#             */
/*   Updated: 2018/05/09 19:06:59 by lchancri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/libft.h"

char	*ft_itoabase(long long nb, char *base)
{
	unsigned long long	a;
	unsigned long long	b;
	int					c;
	char				*str;

	a = ft_strlen(base);
	b = 0;
	c = 0;
	if (!(str = (char*)malloc(sizeof(char) * 64)))
		return (NULL);
	if (nb < 0)
		c = -1;
	if (nb < 0)
		nb = -nb;
	while (nb != 0 || b == 0)
	{
		str[b] = base[nb % a];
		b++;
		nb = nb / a;
	}
	if (c < 0)
		str[b++] = '-';
	str[b] = '\0';
	return (ft_strrev(str));
}
