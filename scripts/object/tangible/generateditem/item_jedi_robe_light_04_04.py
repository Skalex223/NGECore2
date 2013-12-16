import sys
#elder light jedi robe
def setup(core, actor):
	
	object = core.objectService.createObject('object/tangible/wearables/robe/shared_robe_jedi_light_s04.iff', actor.getPlanet())
	object.setStfFilename('static_item_n')
	object.setStfName('item_jedi_robe_light_04_04')
	object.setDetailFilename('static_item_d')
	object.setDetailName('item_jedi_robe_light_04_04')
	object.setStringAttribute('condition', '1000/1000')
	object.setIntAttribute('healing_combat_level_required', 80)
	object.setStringAttribute('skill_required', 'Jedi')
	object.setIntAttribute('cat_stat_mod_bonus.@stat_n:constitution_modified', 250)
	object.setIntAttribute('cat_stat_mod_bonus.@stat_n:strength_modified', 250)
	object.setIntAttribute('cat_stat_mod_bonus.@stat_n:agility_modified', 250)
	object.setStringAttribute('effect', 'Gift of the Light Side')
	object.setStringAttribute('protection_level', 'Radiant')
	
	inventory = actor.getSlottedObject('inventory')
	inventory.add(object)
		
	return