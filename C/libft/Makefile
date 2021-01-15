# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lchancri <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/11/08 16:01:58 by lchancri          #+#    #+#              #
#    Updated: 2018/05/09 19:22:17 by lchancri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME		=	libft.a

FLAG		=	-Wall -Wextra -Werror

#------------------------------------------------------------------------------#
#----------------------------------INCLUDE-------------------------------------#
#------------------------------------------------------------------------------#

I_FILE		=	libft.h\

I_PATH		=	include

I_SRC		=	$(addprefix $(I_PATH)/, $(I_FILE))

#------------------------------------------------------------------------------#
#----------------------------------C_FILE--------------------------------------#
#------------------------------------------------------------------------------#

C_FILE		=	ft_bzero.c\
				ft_isnumber.c\
				ft_memccpy.c\
				ft_strclen.c\
				ft_strnequ.c\
				ft_countcword.c\
				ft_memchr.c\
				ft_strclr.c\
				ft_strnew.c\
				ft_firstwordindex.c\
				ft_memcmp.c\
				ft_strcmp.c\
				ft_strnstr.c\
				ft_intlen.c\
				ft_memcpy.c\
				ft_strcpy.c\
				ft_strrchr.c\
				ft_isalnum.c\
				ft_memdel.c\
				ft_strdel.c\
				ft_strrev.c\
				ft_isalpha.c\
				ft_memmove.c\
				ft_strdup.c\
				ft_strsplit.c\
				ft_isascii.c\
				ft_memset.c\
				ft_strequ.c\
				ft_strstr.c\
				ft_isdigit.c\
				ft_putchar.c\
				ft_striter.c\
				ft_strsub.c\
				ft_isprint.c\
				ft_putchar_fd.c\
				ft_striteri.c\
				ft_strtrim.c\
				ft_itoa.c\
				ft_putendl.c\
				ft_strjoin.c\
				ft_tolower.c\
				ft_lastcharindex.c\
				ft_putendl_fd.c\
				ft_strlcat.c\
				ft_toupper.c\
				ft_lstadd.c\
				ft_putnbr.c\
				ft_strlen.c\
				ft_lstdel.c\
				ft_putnbr_fd.c\
				ft_lstdelone.c\
				ft_putstr.c\
				ft_strmap.c\
				ft_lstiter.c\
				ft_putstr_fd.c\
				ft_strmapi.c\
				ft_lstnew.c\
				ft_strcdup.c\
				ft_strncmp.c\
				ft_strncat.c\
				ft_strcat.c\
				ft_lstmap.c\
				ft_strchr.c\
				ft_atoi.c\
				ft_atoll.c\
				ft_memalloc.c\
				ft_strncpy.c\
				ft_printbit.c\
				ft_swap.c\
				ft_recursive_factorial.c\
				ft_sqrt.c\
				ft_uitoabase.c\
				ft_itoabase.c\

C_PATH		=	src

C_SRC		=	$(addprefix $(C_PATH)/, $(C_FILE))

#------------------------------------------------------------------------------#
#----------------------------------O_FILE--------------------------------------#
#------------------------------------------------------------------------------#

O_FILE		=	$(C_FILE:.c=.o)

O_PATH		=	libft_obj

O_SRC		=	$(addprefix $(O_PATH)/, $(O_FILE))

#------------------------------------------------------------------------------#
#--------------------------------REGLE-----------------------------------------#
#------------------------------------------------------------------------------#

all: $(NAME)

$(NAME): $(O_PATH) $(O_SRC)
	@ar -rc $(NAME) $(O_SRC)

$(O_PATH):
	@mkdir -p $(O_PATH)

$(addprefix $(O_PATH)/, %.o): $(addprefix $(C_PATH)/, %.c) $(I_PATH)
	gcc $(FLAG) -Iinclude -o $@ -c $<

clean:
	@rm -Rf $(O_SRC)
	@rm -Rf $(O_PATH) 2>/dev/null || true

fclean: clean
	@rm -Rf $(NAME)

re: fclean all

.PHONY: clean fclean re all
