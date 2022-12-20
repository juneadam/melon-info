"""Print out all the melons in our inventory."""


from melons import melons_register

for melon in melons_register:

    """Print each melon with corresponding attribute information."""

    # have_or_have_not = 'have'
    # if melons_register[melon]['seedless']:
    #     have_or_have_not = 'do not have'

    print(f'{melon.upper()}:')
    print(f'price:  ${melons_register[melon]["price"]}')
    print(f'seedless: {melons_register[melon]["seedless"]}')
    print(f'flesh color: {melons_register[melon]["flesh"]}')
    print(f'rind color: {melons_register[melon]["rind"]}')
    print(f'average weight: {melons_register[melon]["weight"]}\n')


# for i in melon_names:
#     print_melon(melon_names[i], melon_prices[i], melon_seedlessness[i])
