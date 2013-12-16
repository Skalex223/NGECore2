import sys
#issued ring
def setup(core, actor):
	
	object = core.objectService.createObject('object/tangible/wearables/ring/shared_ring_s02.iff', actor.getPlanet())
	object.setStfFilename('static_item_n')
	object.setStfName('item_bounty_hunter_ring_01_02')
	object.setDetailFilename('static_item_d')
	object.setDetailName('item_bounty_hunter_ring_01_02')
	object.setStringAttribute('condition', '1000/1000')
	object.setStringAttribute('skill_required', 'Bounty Hunter')
	object.setIntAttribute('cat_stat_mod_bonus.@stat_n:constitution_modified', 6)
	object.setIntAttribute('cat_stat_mod_bonus.@stat_n:precision_modified', 6)
	
	inventory = actor.getSlottedObject('inventory')
	inventory.add(object)
		
	return