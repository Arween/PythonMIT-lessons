list_flavors = {}


class Restaurant():

    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):

        print ("Restaurant name - " + self.restaurant_name.title())
        print ("Cuisine type: " + self.cuisine_type.title())
        print ("Number served: " + str(self.number_served))

    def open_restaurant(self):

        print ('Restaurant ' + self.restaurant_name.title() + ' open!!')

    def set_number_served(self):

        self.number_served = input("\nNumber served: ")

    def increment_number_served(self):

        self.increment_number_served = input("\nIncrement number served: ")
        self.number_served += self.increment_number_served

       # if self.number_served == 'q':
        #    print ("Number served: " + str(self.number_served))


my_restaurant = Restaurant('LiLO', 'French')
favorite_restaurant = Restaurant('kiko', 'Chinese')


my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
favorite_restaurant.describe_restaurant()
favorite_restaurant.open_restaurant()

# change number_served
#print(my_restaurant.number_served)
#my_restaurant.number_served = 6
#print (my_restaurant.number_served)

# change number_served (method)

#favorite_restaurant.set_number_served()
#favorite_restaurant.describe_restaurant()
#favorite_restaurant.increment_number_served()
#favorite_restaurant.describe_restaurant()


class IceCreamStand(Restaurant, object):
    def __init__(self, restaurant_name, cuisine_type, number_served=0):

        super(IceCreamStand, self).__init__(self, restaurant_name, cuisine_type, number_served=0)

            self.flavors = input("\nFlavors: ")

            list_flavors.append(self.flavors)


            #self.flavors = 'chocolate'

            def describe_ice_cream(self):

               print ("Flavors: " + list_flavors)

my_ice = IceCreamStand('iCE','USA')
my_ice.describe_restaurant()
my_ice.describe_ice_cream()