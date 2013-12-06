import sys

def setup(core, object):
	object.setIntAttribute(cat_skil_mod.skill_mod_constitution_modified', 25)
	object.setIntAttribute(cat_skil_mod.skill_mod_precision_modified', 25)
	return
	
def equip(core, actor, target):
        core.skillModService.addSkillMod(actor, 'constitution_modified', 25)         
        core.skillModService.addSkillMod(actor, 'precision_modified', 30)
        return
        
def unequip(core, actor, target):
        core.skillModService.deductSkillMod(actor, 'constitution_modified', 25)         
        core.skillModService.deductSkillMod(actor, 'precision_modified', 30)
        return