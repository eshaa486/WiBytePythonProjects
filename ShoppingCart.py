
import random

print('Welcome to Flower Boutique!')
print()
inventory = []

menu = ['Daisies', 'Roses', 'Sunflowers', 'Lilies', 'Tulips']
price = [18.99, 12.99, 10.99, 14.99, 19.99]

special_items = ['Boutique Bouquet ', 'Dried Mini-Bouquet ', 'Mystery Box ', 'Glass Vase ', 'Press-Flower Card ', 'Scented Candle ', 'Plant Care Kit ', 'Seed Packet ', 'Potted Succulent '  ]

special_items_prc = [34.99, 21.50, 29.99, 24.00, 20.00, 26.50, 31.99, 22.75, 28.00]

spcl_idx = random.randint(0,len(special_items_prc) - 1)
menu.append(special_items[spcl_idx])
price.append(special_items_prc[spcl_idx])
inventory.append(20)



print('Today\'s special is: ', special_items[spcl_idx] )
print()

print('ITEM', 'PRICE (USD), excl Tax', sep= '\t\t\t')

for kk in range(len(menu)):
    print(str(kk+1) + '.' + menu[kk], price[kk], sep= '\t\t')

print()

shopping_complete = 0

shopping_cart = []
shopping_quant = []

while shopping_complete == 0:
    order = int(input(f'Enter 1 to {len(menu)} to select a type of flower, or {len(menu) + 1} to proceed to checkout:\n')) 

    if order <= len(menu) and order > 0:
    
        print('You selected', menu[order-1])
        quant = int(input('How many of these do you wish to purchase?\n'))


        if menu[order-1] in shopping_cart:
            print('Repeated Selection')
            idx = shopping_cart.index(menu[order-1])
            #shopping_quant[idx] = shopping_quant[idx]+quant
            shopping_quant[idx] += quant
        else:
            print('New selection')
            shopping_cart.append(menu[order-1])
            shopping_quant.append(quant)
        

    elif order == len(menu) + 1:
        print('Proceeding to checkout')
        shopping_complete = 1
    else:
        print('Invalid Input')


print()

print('Shopping is complete, displaying shopping cart...')
print('ITEM', 'QUANT', 'UNIT PRICE', '\b\b\b\b\b\b\b\bTOTAL', sep='\t\t\t')

grand_tot = 0.0

#print('Shopping is complete, displaying shopping cart...')




for kk in range(len(shopping_cart)):
    idx = menu.index(shopping_cart[kk])
    unit_price = float(price[idx])
    tot_price = round(int(shopping_quant[kk]) * unit_price, 2)
    grand_tot = grand_tot + tot_price
    print(shopping_cart[kk], shopping_quant[kk], unit_price, tot_price, sep='\t\t\t')



print()

print('The grand total is', round(grand_tot, 2))
