import sys
#bluefrog composite armor
def setup(core, actor):
	object = core.objectService.createObject('object/tangible/wearables/armor/composite/shared_armor_composite_chest_plate.iff', actor.getPlanet())
	object.setStringAttribute('Condition', '40000/40000')
	object.setIntAttribute('volume', 1)
	object.setStringAttribute('armor_category', 'Assault')
	object.setIntAttribute('sockets', 1)
	object.setIntAttribute('cat_armor_standard_protection.energy', 5000)
	object.setIntAttribute('cat_armor_standard_protection.kinetic', 7000)
	object.setIntAttribute('cat_armor_special_protection.elemental_acid', 6000)
	object.setIntAttribute('cat_armor_special_protection.elemental_cold', 6000)
	object.setIntAttribute('cat_armor_special_protection.elemental_electrical', 6000)
	object.setIntAttribute('cat_armor_special_protection.elemental_heat', 6000)	
	
	inventory = actor.getSlottedObject('inventory')
	inventory.add(object)
	
	return