import sys
#roadmap issued smuggler armor
def setup(core, actor):
	
	object = core.objectService.createObject('object/tangible/wearables/armor/tantel/shared_armor_tantel_skreej_helmet.iff', actor.getPlanet())
	object.setStfFilename('static_item_n')
	object.setStfName('armor_smuggler_roadmap_helmet_02_01')
	object.setDetailFilename('static_item_d')
	object.setDetailName('armor_smuggler_roadmap_helmet_02_01')
	object.setStringAttribute('condition', '1000/1000')
	object.setIntAttribute('volume', 1)
	object.setStringAttribute('skill_required', 'Smuggler')
	object.setIntAttribute('cat_stat_mod_bonus.@stat_n:constitution_modified', 3)
	object.setStringAttribute('armor_category', 'Reconnaissance')
	object.setIntAttribute('cat_armor_special_protection.elemental_acid', 1640)
	object.setIntAttribute('cat_armor_special_protection.elemental_cold', 1640)
	object.setIntAttribute('cat_armor_special_protection.elemental_electrical', 1640)
	object.setIntAttribute('cat_armor_special_protection.elemental_heat', 1640)
	object.setIntAttribute('cat_armor_standard_protection.energy', 2640)
	object.setIntAttribute('cat_armor_standard_protection.kinetic', 640)
	
	inventory = actor.getSlottedObject('inventory')
	inventory.add(object)
	
	return