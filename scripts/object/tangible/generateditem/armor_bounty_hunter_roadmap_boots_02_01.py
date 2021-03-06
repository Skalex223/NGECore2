import sys
#roadmap issued bh armor
def setup(core, actor):
	
	object = core.objectService.createObject('object/tangible/wearables/armor/composite/shared_armor_composite_boots.iff', actor.getPlanet())
	object.setStfFilename('static_item_n')
	object.setStfName('armor_bounty_hunter_roadmap_boots_02_01')
	object.setDetailFilename('static_item_d')
	object.setDetailName('armor_bounty_hunter_roadmap_boots_02_01')
	object.setStringAttribute('condition', '1000/1000')
	object.setIntAttribute('volume', 1)
	object.setStringAttribute('skill_required', 'Bounty Hunter')
	object.setIntAttribute('cat_stat_mod_bonus.@stat_n:constitution_modified', 3)
	object.setStringAttribute('armor_category', 'Assault')
	
	inventory = actor.getSlottedObject('inventory')
	inventory.add(object)
	
	return