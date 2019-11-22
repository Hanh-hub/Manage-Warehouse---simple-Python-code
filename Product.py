class Node:
    def __init__(self, data, next=None, previous=None):
        self.data = data
        self.previous = previous
        self.next = next

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

    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False
    def getSize(self):
        count=1
        cur=self.head

        while cur.next is not None:

            count=count+1
            cur=cur.next
        return count

    def delete(self, sku):

        item = self.getitem_location(sku)
        if item.next is not None:
            n1 = item.previous
            n2 = item.next
            n1.next = n2
            n2.previous = n1
            print('Deleted ', item.data.sku)
            ('----------------------------------------------------')
        else:
            self.tail = item.previous

            n1 = item.previous
            n2 = item.previous.next
            n2.previous = None
            n1.next = None

            print('Deleted ', item.data.sku)

    def addSku(self, sku):
        wid = int(input('Please enter the width: '))
        height = int(input('Please enter the height: '))
        length = int(input('Please enter the length: '))
        weight = int(input('Please enter the weight: '))
        frag = input('Enter F for Fragile, N for non fragile: ')
        item = Product(sku, wid, length, height, frag, weight)
        self.add(Node(item))

        print('successfully added sku ', sku, ' to the inventory')
        print('----------------------------------------------------')

    def shipping(self, sku):
        if sku is '0':
            return
        else:
            not_found = 1
            item = self.getitem_location(sku)
            if item is not_found:
                print(sku, 'is not on the list,do you want to add? ')
                loop = True
                while loop:
                    ans = input('Y/N:')
                    if ans == 'Y' or ans == 'y':
                        self.addSku(sku)
                        self.shipping(sku)
                        loop = False
                    elif ans == 'N' or ans == 'n':
                        loop = False
                        return
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
                print('Successfully shipped ', sku)
                self.delete(sku)

    def print_inventory(self):
        print('----------------------------------------------------')
        print('Printing the inventory')
        print()
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            print('sku-', cur_node.data.sku, 'lxwxh=', cur_node.data.length, 'x', cur_node.data.width, 'x',
                  cur_node.data.height)

    def traversal_tail_to_head(self):
        print('----------------------------------------------------')
        print('Here is the inventory from newest to oldest:')
        print()
        cur_node = self.tail

        while cur_node.previous is not None:
            print('sku-', cur_node.data.sku, 'lxwxh=', cur_node.data.length, 'x', cur_node.data.width, 'x',
                  cur_node.data.height)
            cur_node = cur_node.previous