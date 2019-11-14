from xlrd import open_workbook
from Node import Node

wb = open_workbook('book1.xlsx')
sheet = wb.sheet_by_name("Sheet1")
number_of_rows = sheet.nrows
number_of_columns = sheet.ncols


class Product:
    # Class product store product information
    def __init__(self, sku, width, length, height, frag, weight):
        self.sku = sku
        self.width = width
        self.length = length
        self.height = height
        self.frag = frag
        self.weight = weight


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, item):
        if self.head is None:
            self.head = item
            self.tail = item
        else:
            self.tail.next = item
            item.previous = self.tail
            self.tail = item

    def getitem_location(self, sku):
        not_found = 1
        # search sku on the list and return the address of the node that contains that sku
        cur_node = self.head
        while cur_node.next != None:

            if cur_node.data.sku == sku:
                return cur_node
            cur_node = cur_node.next
        else:
            if cur_node.data.sku == sku:
                return cur_node
        return not_found

    def delete(self, sku):

        item = self.getitem_location(sku)
        if item.next is not None:
            n1 = item.previous
            n2 = item.next
            n1.next = n2
            n2.previous = n1
            print('Deleted ', item.data.sku)
        else:
            self.tail=item.previous

            n1 = item.previous
            n2 = item.previous.next#idk if we need this
            n2.previous = None #maybe extra
            n1.next = None

            print('Deleted ', item.data.sku)

    def addSku(self, sku):

        # sku = input('Please enter the Sku:')
        wid = int(input('Please enter the width: '))
        height = int(input('Please enter the height: '))
        length = int(input('Please enter the length: '))
        weight = int(input('Please enter the weight: '))
        frag = input('Enter F for Fragile, N for non fragile: ')
        item = Product(sku, wid, length, height, frag, weight)
        self.add(Node(item))

        print('successfully added sku ', sku, ' to the inventory')
        print('-------------------------------------------------------')

    def shipping(self, sku):
        not_found = 1

        item = self.getitem_location(sku)

        if item is not_found:
            print(sku, 'is not on the list,do you want to add? ')
            ans = input('Y/N:')
            if ans == 'Y' or ans == 'y':
                self.addSku(sku)

                self.shipping(sku)
            else:
                print('invalid input.')
                
        else:

            print('SKU-', item.data.sku, 'LxWxH = ', item.data.length, 'x',
                  item.data.width, 'x', item.data.height, 'inches', item.data.weight, ' lbs')

            total_dim = item.data.width + item.data.length + item.data.height
            if item.data.frag == 'F':
                print("Fragile item. Bubbled wrapped needed")

            if item.data.weight < 3:
                print("First class Packing shipping")
            elif item.data.weight < 70 and total_dim <= 108:
                print("Flat rate medium box Shipping")
            else:
                print("Extra Large item. Wrap only")
                print("Truck delivery")
            print('Successfully shipped ',sku)
            print('-----------------------------------------')

    def print_inventory(self):
        print('---------------------------')
        print('Printing the inventory')
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            print('sku-', cur_node.data.sku, 'lxwxh=', cur_node.data.length, 'x', cur_node.data.width, 'x',
                  cur_node.data.height)

    def traversal_tail_to_head(self):
        print('----------------------------------------------------')
        print('Here is the inventory from newest to oldest:')
        cur_node = self.tail

        while cur_node.previous is not None:
            print('sku-', cur_node.data.sku)
            cur_node = cur_node.previous
        #print('sku-', cur_node.data.sku)


shelf = Queue()

product = []
product.append(Product(None, None, None, None, None, None))

for i in range(1, number_of_rows):
    product.append(Product(sheet.cell(i, 0).value,
                           sheet.cell(i, 1).value,
                           sheet.cell(i, 2).value,
                           sheet.cell(i, 3).value,
                           sheet.cell(i, 4).value,
                           sheet.cell(i, 5).value))
# print(product[3].sku)
for i in range(number_of_rows):
    shelf.add(Node(product[i]))

sku=input('What item do you want to ship?:')
shelf.shipping(sku)
shelf.delete(sku)



shelf.traversal_tail_to_head()
shelf.print_inventory()

# while cur.next != None:
# cur = cur.next
#  print(cur.data.sku)
