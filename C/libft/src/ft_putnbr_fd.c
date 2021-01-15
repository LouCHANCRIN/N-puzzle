/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_fd.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lchancri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/11/09 19:17:23 by lchancri          #+#    #+#             */
/*   Updated: 2018/05/09 18:45:58 by lchancri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/libft.h"

void		ft_putnbr_fd(int n, int fd)
{
	long	b;

	b = n;
	if (n < 0)
	{
		b = -b;
		ft_putchar_fd('-', fd);
	}
	if (b >= 10)
	{
		ft_putnbr_fd(b / 10, fd);
		ft_putchar_fd(b % 10 + 48, fd);
	}
	else
		ft_putchar_fd(b + 48, fd);
}
