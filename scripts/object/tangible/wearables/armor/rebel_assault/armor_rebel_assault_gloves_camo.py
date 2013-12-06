import sys

def setup(core, object):
		object.setStringAttribute('condition', '40000/40000')
		object.setIntAttribute('volume', 1)
		object.setStringAttribute('armor_category', 'Assault')
		object.setStringAttribute('faction_restriction', 'Rebel')
		object.setIntAttribute('cat_skill_mod.skill_mod_constitution_modified', 15)
		object.setIntAttribute('cat_skill_mod.skill_mod_luck_modified', 10)
		object.setIntAttribute('cat_skill_mod.skill_mod_precision_modified', 20)
		return
