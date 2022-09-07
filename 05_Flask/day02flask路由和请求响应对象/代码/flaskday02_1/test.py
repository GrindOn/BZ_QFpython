import uuid

uid = uuid.uuid4()
print(uid)
print(type(uid))

uid1 = str(uid)
print(type(uid1))
uid1 = uid1.replace('-','')
print(uid1)
