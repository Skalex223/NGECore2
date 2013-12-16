import sys
#issued necklace
def setup(core, actor):
	
	object = core.objectService.createObject('object/tangible/wearables/necklace/shared_necklace_s02.iff', actor.getPlanet())
	object.setStfFilename('static_item_n')
	object.setStfName('item_smuggler_pendant_01_02')
	object.setDetailFilename('static_item_d')
	object.setDetailName('item_smuggler_pendant_01_02')
	object.setStringAttribute('condition', '1000/1000')
	object.setStringAttribute('skill_required', 'Smuggler')
	object.setIntAttribute('cat_stat_mod_bonus.@stat_n:agility_modified', 12)
	object.setIntAttribute('cat_stat_mod_bonus.@stat_n:precision_modified', 12)
	
	inventory = actor.getSlottedObject('inventory')
	inventory.add(object)
		
	return