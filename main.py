from cgitb import handler
from sample import create_samples
from advertisement import ApartmentRent, ApartmentSell, HouseRent, HouseSell, StoreRent, StoreSell

class Handler:
    ADVERTISEMENT_TYPES = {
        1: ApartmentSell, 
        # 2:ApartmentRent,
        # 3: HouseSell, 4:HouseRent,
        # 5: StoreSell, 6:StoreRent,
    }

    SWITCHES = {
        'r': 'get_report',
        's': 'show_all',
    }

    def get_report(self):
        for adv in self.ADVERTISEMENT_TYPES.values():
            print(adv, adv.manager.count())

    def show_all(self):
        for adv in self.ADVERTISEMENT_TYPES.values():
            # print(adv, adv.manager.count())
            for obj in adv.object_list:
                print(obj.show_description())

    def run(self):
        print("Hello World")

        for key in self.SWITCHES:
            print(f"press {key} for {self.SWITCHES[key]}")

        user_input = input("Enter your choice:")
        switch = self.SWITCHES.get(user_input, None)
        if switch is None:
            print("Invalid input")
            self.run()
        choice = getattr(self, switch, None)
        choice()


if __name__ == "__main__":
    create_samples()

    handler = Handler()
    handler.run()