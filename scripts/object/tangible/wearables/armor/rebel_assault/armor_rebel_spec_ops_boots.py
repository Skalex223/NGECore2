import sys

def setup(core, object):
		object.setStringAttribute('condition', '40000/40000')
		object.setIntAttribute('volume', 1)
		object.setStringAttribute('armor_category', 'Assault')
		object.setStringAttribute('faction_restriction', 'Rebel')
		object.setIntAttribute('cat_skill_mod.skill_mod_constitution_modified', 23)
		object.setIntAttribute('cat_skill_mod.skill_mod_luck_modified', 11)
		object.setIntAttribute('cat_skill_mod.skill_mod_precision_modified', 17)
		return
	
def equip(core, actor, target):
        core.skillModService.addSkillMod(actor, 'constitution_modified', 23)
        core.skillModService.addSkillMod(actor, 'luck_modified', 11)
        core.skillModService.addSkillMod(actor, 'precision_modified', 17)
        return
        
def unequip(core, actor, target):
        core.skillModService.deductSkillMod(actor, 'constitution_modified', 23)
        core.skillModService.deductSkillMod(actor, 'luck_modified', 11)
        core.skillModService.deductSkillMod(actor, 'precision_modified', 27)       
        return