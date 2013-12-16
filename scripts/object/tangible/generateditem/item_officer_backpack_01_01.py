import sys
#issued backpack
def setup(core, actor):
	
	object = core.objectService.createObject('object/tangible/wearables/backpack/shared_backpack_s03.iff', actor.getPlanet())
	object.setStfFilename('static_item_n')
	object.setStfName('item_officer_backpack_01_02')
	object.setDetailFilename('static_item_d')
	object.setDetailName('item_officer_backpack_01_02')
	object.setStringAttribute('condition', '1000/1000')
	object.setStringAttribute('skill_required', 'Officer')
	object.setIntAttribute('cat_stat_mod_bonus.@stat_n:agility_modified', 5)
	object.setIntAttribute('cat_stat_mod_bonus.@stat_n:precision_modified', 5)
	
	inventory = actor.getSlottedObject('inventory')
	inventory.add(object)
		
	return