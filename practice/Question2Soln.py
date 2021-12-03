# Question 2
# Build a desktop 
class Item:
    def __init__(self, name='INVALID', price=0):
        self.name = name
        self.price = price
    
    # String contains this items information
    # Ex. Item name: Ryzen 9 5900x Item price: 450
    def __str__(self):
        return "Item name: " + self.name + " Item price: " + str(self.price)

    # Gets the price of this item
    def getPrice(self):
        return self.price

# Prints each item in the category.
# Starts at Motherboard and ends at SSD
def printCart(cart):
    for key in cart:
        if key == 'RAM' or key == 'SSD':
            for item in cart[key]:
                print(item)
        else:
            print(cart[key])

            
# Sums up the all the prices of the items in the cart
# Returns the sum of the cart
def sumCart(cart):
    res = 0
    for key in cart:
        if key == 'RAM' or key == 'SSD':
            for item in cart[key]:
                res += item.getPrice()
        else:
            res += cart[key].getPrice()
    return res 
    

def main():
    # You will be creating a list of parts for a desktop computer.
    # This desktop requires: 1 Motherboard, 1 CPU, 2 RAM, 1 GPU, 1 PSU, and 2 SSDs
    # The Category and the prices are listed below:
    
    # Category          Item Name                       Price
    # Motherboard       ASUS TUF GAMING X570-PLUS       $160
    # CPU               Ryzen 5 5600x                   $300
    # RAM               G.Skill Ripjaws V               $50     
    # GPU               NVIDIA Founders Edition         $400
    # PSU               Corsair CXM                     $55
    # SSD               Western Digital Blue            $53

    # Using the item class, add the items to the cart based on the desktop requirements
    # The cart will store ITEM(S) per category
    # If you are adding MULTIPLE ITEMS to a category, consider using a data structure to store the items

    # Part (1)
    cart = {}
    #Part 1:
    cart['Motherboard'] = Item("ASUS TUF GAMING X570-PLUS", 160)
    cart['CPU'] = Item("Ryzen 5 5600x", 300)
    cart['RAM'] = [Item("G.Skill Ripjaws V", 50), Item("G.Skill Ripjaws V", 50)]
    cart['GPU'] = Item("NVIDIA Founders Edition", 400)
    cart['PSU'] = Item("Corsair CXM", 55)
    cart['SSD'] = [Item("Western Digital Blue", 53), Item("Western Digital Blue", 53)]


    # Part (2) Write a print method
    printCart(cart)
    # Output should look like:
    """
    Item name: ASUS TUF GAMING X570-PLUS Item price: 160  
    Item name: Ryzen 5 5600x Item price: 300
    Item name: G.Skill Ripjaws V Item price: 50
    Item name: G.Skill Ripjaws V Item price: 50
    Item name: NVIDIA Founders Edition Item price: 400    
    Item name: Corsair CXM Item price: 55
    Item name: Western Digital Blue Item price: 53
    Item name: Western Digital Blue Item price: 53 
    """

    # Part (3) Make sure your print method works before working on the sumCart method
    print("Total Cost: ", sumCart(cart))
    # Total Cost: 1121
if __name__ == "__main__":
    main()


