/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_uitoabase.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lchancri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/12/09 15:07:14 by lchancri          #+#    #+#             */
/*   Updated: 2018/05/09 14:19:15 by lchancri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/libft.h"

char	*ft_uitoabase(unsigned long long nb, char *base)
{
	int		a;
	int		b;
	char	*str;

	a = 0;
	b = 0;
	if (!(str = (char*)malloc(sizeof(char) * 64)))
		return (NULL);
	while (base[a] != '\0')
		a++;
	while (nb != 0 || b == 0)
	{
		str[b] = base[nb % a];
		b++;
		nb = nb / a;
	}
	str[b] = '\0';
	return (ft_strrev(str));
}
