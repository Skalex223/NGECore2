import sys
#issued ring gleaming
def setup(core, actor):
	
	object = core.objectService.createObject('object/tangible/wearables/ring/shared_ring_s02.iff', actor.getPlanet())
	object.setStfFilename('static_item_n')
	object.setStfName('item_force_sensitive_ring_02_01')
	object.setDetailFilename('static_item_d')
	object.setDetailName('item_force_sensitive_ring_02_01')
	object.setStringAttribute('condition', '1000/1000')
	object.setStringAttribute('skill_required', 'Jedi')
	object.setIntAttribute('cat_stat_mod_bonus.@stat_n:agility_modified', 5)
	object.setIntAttribute('cat_stat_mod_bonus.@stat_n:strength_modified', 5)
	
	inventory = actor.getSlottedObject('inventory')
	inventory.add(object)
		
	return