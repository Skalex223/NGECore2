import sys
#issued belt
def setup(core, actor):
	
	object = core.objectService.createObject('object/tangible/wearables/belt/shared_belt_s20.iff', actor.getPlanet())
	object.setStfFilename('static_item_n')
	object.setStfName('item_roadmap_belt_force_sensitive_01_02')
	object.setDetailFilename('static_item_d')
	object.setDetailName('item_roadmap_belt_force_sensitive_01_02')
	object.setStringAttribute('condition', '1000/1000')
	object.setIntAttribute('volume', 1)
	object.setStringAttribute('skill_required', 'Jedi')
	object.setIntAttribute('cat_stat_mod_bonus.@stat_n:agility_modified', 15)
	object.setIntAttribute('cat_stat_mod_bonus.@stat_n:constitution_modified', 20)
	object.setIntAttribute('cat_stat_mod_bonus.@stat_n:strength_modified', 15)
	
	inventory = actor.getSlottedObject('inventory')
	inventory.add(object)
		
	return