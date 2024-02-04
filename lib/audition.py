class Audition:

    all_auditions = []
    
    def __init__(self, role, actor, location, phone):
        self.role = role
        self.actor = actor
        self.location = location
        self.phone = phone
        self.hired = False
        Audition.all_auditions.append(self)
        role.all_auditions.append(self)
        print(f"{self.actor} has an audition for {self.role.character_name} at {self.location}")
    
    @property
    def role(self):
        return self._role
    
    @role.setter
    def role(self, new_role):
        from role import Role
        if isinstance(new_role, Role):
            self._role = new_role
        else:
            raise Exception("The role must be of instance class Role")

    @property
    def actor(self):
        return self._actor
    
    @actor.setter
    def actor(self, new_actor):
        if isinstance(new_actor, str) and len(new_actor) >= 3 and len(new_actor) <= 20:
            self._actor = new_actor
        else:
            raise Exception("The new Actor must be a name between 3 and 20 characters.")
    
    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self, new_location):
        if isinstance(new_location, str):
            self._location = new_location
        else:
            print(("The location need to a string!"))
    
    @property
    def phone(self):
        return self._phone
    
    @phone.setter
    def phone(self, new_number):
        if isinstance(new_number, str) and len(new_number) >5 and len(new_number) <=10:
            self._new_number = new_number
        else:
            print("the phone must be a number in string format!")
    
    def call_back(self):
        self.role.is_hired = True
        self.hired = True
    
