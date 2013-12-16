import sys

def setup(core, actor):
	
	object = core.objectService.createObject('object/tangible/wearables/helmet/shared_helmet_fighter_blacksun_ace.iff', actor.getPlanet())
	object.setStringAttribute('condition', '100/100')
	object.setIntAttribute('volume', 1)
	
	inventory = actor.getSlottedObject('inventory')
	inventory.add(object)
		
	return