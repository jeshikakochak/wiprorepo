class College:
    def __init__(self,ccode,cname,ccity):
        self.ccode = ccode;
        self.cname = cname;
        self.ccity = ccity;

    def welcome_message(self):
        print('Welcome to College !!')

    def display_clg_details(self):
        print(f"College code: {self.ccode}")
        print(f"College name: {self.cname}")
        print(f"City: {self.ccity}")