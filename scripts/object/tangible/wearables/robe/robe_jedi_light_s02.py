import sys

def setup(core, object):
	return
        
def equip(core, actor, target):
	core.skillModService.addSkillMod(actor, 'acid', 4000)
	core.skillModService.addSkillMod(actor, 'heat', 4000)
	core.skillModService.addSkillMod(actor, 'cold', 4000)
	core.skillModService.addSkillMod(actor, 'electricity', 4000)
	core.skillModService.addSkillMod(actor, 'kinetic', 4000)
	core.skillModService.addSkillMod(actor, 'energy', 4000)
	return
        
def unequip(core, actor, target):
	core.skillModService.deductSkillMod(actor, 'acid', 4000)
	core.skillModService.deductSkillMod(actor, 'heat', 4000)
	core.skillModService.deductSkillMod(actor, 'cold', 4000)
	core.skillModService.deductSkillMod(actor, 'electricity', 4000)
	core.skillModService.deductSkillMod(actor, 'kinetic', 4000)
	core.skillModService.deductSkillMod(actor, 'energy', 4000)
	return