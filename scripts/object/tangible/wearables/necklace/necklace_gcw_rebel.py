import sys

def setup(core, object):
	return
	
def equip(core, actor, target):
        core.skillModService.addSkillMod(actor, 'constitution_modified', 30)         
        core.skillModService.addSkillMod(actor, 'luck_modified', 30)
        core.skillModService.addSkillMod(actor, 'precision_modified', 24)
        core.skillModService.addSkillMod(actor, 'strength_modified', 24)
        return
        
def unequip(core, actor, target):
        core.skillModService.deductSkillMod(actor, 'constitution_modified', 30)         
        core.skillModService.deductSkillMod(actor, 'luck_modified', 30)
        core.skillModService.deductSkillMod(actor, 'precision_modified', 24)
        core.skillModService.deductSkillMod(actor, 'strength_modified', 24)
        return