from random import choice
from estate import Apartment, House, Store
from user import User
from region import Region
from advertisement import ApartmentSell, HouseSell

FIRST_NAMES = ['Meysam', 'Kambiz', 'Jamshid']
LAST_NAMES = ['Ariaei', 'Alipour', 'Nazmi']
MOBILES = ['09123456789', '09123456788', '09123456787', '09123456786', '09123456786']

def create_samples():
    
    for mobile in MOBILES:
        User(choice(FIRST_NAMES), choice(LAST_NAMES), mobile)

    # for user in User.object_list:
    #     print(f"{user.id}\t {user.fullname}")

    reg1 = Region(name="R1")
    reg2 = Region(name="R2")
     
    # apt1 = Apartment(
    #     user=User.object_list[0], area=80, rooms_count=2, built_year=1393,
    #     has_elevator=True, has_parking=True, floor=2, region=reg1,
    #     address="Some text..."
    # )

    # house = House(
    #     has_yard=True, floor_count=1, user=User.object_list[2], area=400,
    #     rooms_count=6, built_year=1370, region=reg1, address="Some text..."
    # )

    # store = Store(
    #     user=User.object_list[-1], area=30,
    #     rooms_count=1, built_year=1390, region=reg1, address="Some text..."
    # )

    # apt1.show_description()
    # house.show_description()
    # store.show_description()


    apartment_sell = ApartmentSell(
        user=User.object_list[0], area=80, rooms_count=2, built_year=1393,
        has_elevator=True, has_parking=True, floor=2, region=reg1,
        address="Some text...", convertable=False, discountable=True,
        price_per_meter=10
    )
    apartment_sell.show_detail()


    # house_sell = HouseSell(
    #     has_yard=True, floor_count=1, user=User.object_list[2], area=400,
    #     rooms_count=6, built_year=1370, region=reg1, address="Some text...", 
    #     convertable=True, discountable=True, price_per_meter=20
    # )
    # house_sell.show_detail()

    search_result = ApartmentSell.manager.search(region=reg1, price_per_meter__min=6, price_per_meter__max=11)

    # print(search_result)

    # print(ApartmentSell.manager)
    # print(HouseSell.manager)

    print('Samples created')