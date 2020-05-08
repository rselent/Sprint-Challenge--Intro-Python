# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


class Vehicle:			## BASE CLASS ##	(does this really need to be asked?)
	...

class FlightVehicle( Vehicle):
	...
class Starship( FlightVehicle):
	...
class Airplane( FlightVehicle):
	...

class GroundVehicle( Vehicle):
	...
class Car( GroundVehicle):
	...
class Motorcycle( GroundVehicle):
	...