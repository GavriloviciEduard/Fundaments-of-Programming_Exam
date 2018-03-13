from infrastracturre.repo import CarRepo
from application.controller import CarController
from user_interface.ui import CarUI

r=CarRepo()
c=CarController(r)
u=CarUI(c)

u.menu()