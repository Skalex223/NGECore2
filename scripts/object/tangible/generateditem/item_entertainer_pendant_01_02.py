import sys
#issued necklace
def setup(core, actor):
	
	object = core.objectService.createObject('object/tangible/wearables/necklace/shared_necklace_s02.iff', actor.getPlanet())
	object.setStfFilename('static_item_n')
	object.setStfName('item_entertainer_pendant_01_02')
	object.setDetailFilename('static_item_d')
	object.setDetailName('item_entertainer_pendant_01_02')
	object.setStringAttribute('condition', '1000/1000')
	object.setStringAttribute('skill_required', 'Entertainer')
	object.setIntAttribute('cat_stat_mod_bonus.@stat_n:stamina_modified', 3)
	object.setIntAttribute('cat_skill_mod_bonus.@stat_n:dance_prop_assembly', 5)
	
	inventory = actor.getSlottedObject('inventory')
	inventory.add(object)
		
	return