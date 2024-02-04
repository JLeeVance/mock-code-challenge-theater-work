from role import Role
from audition import Audition


simba = Role("Simba")
nala = Role("Nala")
scar = Role("Scar")

print('\n')
john = Audition(simba, "John", "Pearl Studios", "3171123097")
bill = Audition(simba, "Bill", "Downtown", "7653542038")
print('\n')
print("-- Changing callback status --")
bill.call_back()
print(john.hired)
john.call_back()

# print(simba.auditions())

simba.actors()
print('\n')
simba.locations()
print("\n")
simba.lead()
print("\n")
simba.understudy()
print("\n")
Role.not_cast()

