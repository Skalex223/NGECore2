import sys

def setup(core, object):
		object.setStringAttribute('condition', '40000/40000')
		object.setIntAttribute('volume', 1)
		object.setStringAttribute('armor_category', 'Battle')
		object.setStringAttribute('faction_restriction', 'Rebel')
		object.setIntAttribute('cat_skill_mod.skill_mod_constitution_modified', 18)
		object.setIntAttribute('cat_skill_mod.skill_mod_luck_modified', 6)
		object.setIntAttribute('cat_skill_mod.skill_mod_precision_modified', 12)
		object.setIntAttribute('cat_skill_mod.skill_mod_strength_modified', 12)
		return
	
def equip(core, actor, target):
        core.skillModService.addSkillMod(actor, 'constitution_modified', 18)
        core.skillModService.addSkillMod(actor, 'luck_modified', 6)
        core.skillModService.addSkillMod(actor, 'precision_modified', 12)
        core.skillModService.addSkillMod(actor, 'strength_modified', 12)
        return
        
def unequip(core, actor, target):
        core.skillModService.deductSkillMod(actor, 'constitution_modified', 18)
        core.skillModService.deductSkillMod(actor, 'luck_modified', 6)
        core.skillModService.deductSkillMod(actor, 'precision_modified', 12)
        core.skillModService.deductSkillMod(actor, 'strength_modified', 12)
        return