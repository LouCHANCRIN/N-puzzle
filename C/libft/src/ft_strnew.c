/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnew.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lchancri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/11/09 14:29:43 by lchancri          #+#    #+#             */
/*   Updated: 2018/05/09 19:08:14 by lchancri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/libft.h"

char	*ft_strnew(size_t size)
{
	char	*a;

	a = (char*)malloc(sizeof(char) * (size + 1));
	if (a == NULL)
		return (NULL);
	ft_memset(a, '\0', size + 1);
	return (a);
}
