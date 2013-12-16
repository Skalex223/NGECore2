import sys
#roadmap issued ithorian assault armor
def setup(core, actor):
	
	object = core.objectService.createObject('object/tangible/wearables/armor/ithorian_sentinel/shared_ith_armor_s03_boots.iff', actor.getPlanet())
	object.setStfFilename('static_item_n')
	object.setStfName('armor_ithorian_roadmap_boots_02_03')
	object.setDetailFilename('static_item_d')
	object.setDetailName('armor_ithorian_roadmap_boots_02_03')
	object.setStringAttribute('condition', '1000/1000')
	object.setIntAttribute('volume', 1)
	object.setStringAttribute('species_restriction', 'Ithorian')
	object.setIntAttribute('cat_stat_mod_bonus.@stat_n:constitution_modified', 3)
	object.setStringAttribute('armor_category', 'Assault')
	
	inventory = actor.getSlottedObject('inventory')
	inventory.add(object)
	
	return