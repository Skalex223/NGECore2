import sys
#roadmap issued officer armor
def setup(core, actor):
	
	object = core.objectService.createObject('object/tangible/wearables/armor/composite/shared_armor_composite_leggings.iff', actor.getPlanet())
	object.setStfFilename('static_item_n')
	object.setStfName('armor_officer_roadmap_leggings_02_01')
	object.setDetailFilename('static_item_d')
	object.setDetailName('armor_officer_roadmap_leggings_02_01')
	object.setStringAttribute('condition', '1000/1000')
	object.setIntAttribute('volume', 1)
	object.setStringAttribute('skill_required', 'Officer')
	object.setIntAttribute('cat_stat_mod_bonus.@stat_n:constitution_modified', 3)
	object.setStringAttribute('armor_category', 'Battle')
	object.setIntAttribute('cat_armor_special_protection.elemental_acid', 1640)
	object.setIntAttribute('cat_armor_special_protection.elemental_cold', 1640)
	object.setIntAttribute('cat_armor_special_protection.elemental_electrical', 1640)
	object.setIntAttribute('cat_armor_special_protection.elemental_heat', 1640)
	object.setIntAttribute('cat_armor_standard_protection.energy', 1640)
	object.setIntAttribute('cat_armor_standard_protection.kinetic', 1640)
	
	inventory = actor.getSlottedObject('inventory')
	inventory.add(object)
	
	return