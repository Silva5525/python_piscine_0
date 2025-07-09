# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Hello.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wdegraf <wdegraf@student.42heilbronn.de    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/07/07 11:34:07 by wdegraf           #+#    #+#              #
#    Updated: 2025/07/07 11:42:58 by wdegraf          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# List: An ordered, mutable (changeable) collection of items.
# Lists can contain duplicate values, and you can add, remove, or change elements.
ft_list = ["Hello", "World!"]

# Tuple: An ordered, immutable (unchangeable) collection of items.
# Tuples can also contain duplicates, but once created, their contents cannot be modified.
ft_tuple = ("Hello", "Deutschland!")

# Set: An unordered collection of unique elements.
# Sets do not allow duplicates, and the order is not preserved.
# Useful for storing distinct items and performing set operations like union or intersection.
ft_set = {"Hello", "Heilbronn!"}

# Dictionary: A collection of key-value pairs.
# Keys must be unique; values can be anything (even duplicates).
# Dictionaries are mutable and provide fast lookups by key.
ft_dict = {"Hello": "42Heilbronn!"}

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)