import sys

def setup(core, actor):
	
	object = core.objectService.createObject('object/tangible/wearables/robe/shared_robe_jedi_dark_s02.iff', actor.getPlanet())
	object.setStfFilename('static_item_n')
	object.setStfName('item_jedi_robe_dark_04_02')
	object.setDetailFilename('static_item_d')
	object.setDetailName('item_jedi_robe_dark_04_02')
	object.setStringAttribute('condition', '1000/1000')
	object.setIntAttribute('healing_combat_level_required', 60)
	object.setStringAttribute('skill_required', 'Jedi')
	object.setIntAttribute('cat_stat_mod_bonus.@stat_n:constitution_modified', 145)
	object.setIntAttribute('cat_stat_mod_bonus.@stat_n:precision_modified', 145)
	object.setStringAttribute('protection_level', 'Lucent')
	
	inventory = actor.getSlottedObject('inventory')
	inventory.add(object)
		
	return