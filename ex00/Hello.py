ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# Lists are changeable
ft_list[1] = "World"

# tuples are unchangeable
tuple_to_list = list(ft_tuple)
tuple_to_list[1] = "Morocco"
ft_tuple = tuple(tuple_to_list)

# sets are unchangeable
set_to_list = list(ft_set)
set_to_list[1] = "Ben Guerrir"
ft_set = set(set_to_list)

# dicts are changeable
ft_dict["Hello"] = "1337"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)