import sys
#roadmap issued ithorian battle armor
def setup(core, actor):
	
	object = core.objectService.createObject('object/tangible/wearables/armor/ithorian_defender/shared_ith_armor_s01_bracer_l.iff', actor.getPlanet())
	object.setStfFilename('static_item_n')
	object.setStfName('armor_ithorian_roadmap_bracer_l_02_02')
	object.setDetailFilename('static_item_d')
	object.setDetailName('armor_ithorian_roadmap_bracer_l_02_02')
	object.setStringAttribute('condition', '1000/1000')
	object.setIntAttribute('volume', 1)
	object.setStringAttribute('species_restriction', 'Ithorian')
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