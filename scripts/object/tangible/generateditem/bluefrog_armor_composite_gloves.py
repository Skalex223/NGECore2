import sys
#bluefrog composite armor
def setup(core, actor):
	object = core.objectService.createObject('object/tangible/wearables/armor/composite/shared_armor_composite_gloves.iff', actor.getPlanet())
	object.setStringAttribute('Condition', '40000/40000')
	object.setIntAttribute('volume', 1)
	object.setStringAttribute('armor_category', 'Assault')
	object.setIntAttribute('sockets', 1)
	
	inventory = actor.getSlottedObject('inventory')
	inventory.add(object)
	
	return