from audition import Audition


class Role:

    all_roles = []
    
    def __init__(self, character_name):
        self.character_name = character_name
        self.all_auditions = []
        Role.all_roles.append(self)
        self.is_hired = False
        print(f"{self.character_name} is ready to cast!")
    
    @property
    def character_name(self):
        return self._character_name
    
    @character_name.setter
    def character_name(self, new_name):
        if isinstance(new_name, str) and len(new_name) > 0:
            self._character_name = new_name
        else:
            raise Exception("the new character_name must be a string!")
    
    def auditions(self):
        return self.all_auditions
    
    def actors(self):
        role_actors = []
        for obj in self.all_auditions:
            role_actors.append(obj.actor)
        print(role_actors)
        return role_actors

    def locations(self):
        audition_locations = []
        for obj in self.all_auditions:
            audition_locations.append(obj.location)
        print(audition_locations)
        return audition_locations

    def lead(self):
        for obj in self.all_auditions:
            if obj.hired == True:
                print(obj.actor)
                return obj
            else:
                return("no actor has been hired for this role")
    
    def understudy(self):
        i = 1
        callbacks = []
        while i <= 2:
            for obj in self.all_auditions:
                if obj.hired == True:
                    callbacks.append(obj)
                    i += 1
        print(callbacks[1].actor)
        return callbacks[1]

    @classmethod
    def not_cast(cls):
        notcast = []
        for role in cls.all_roles:
            if role.is_hired == False:
                notcast.append(role)
        print([role.character_name for role in notcast])
        return notcast

