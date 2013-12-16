import sys

def setup(core, object):
	return
        
def equip(core, actor, target):
 	core.skillModService.addSkillMod(actor, 'acid', 3000)
	core.skillModService.addSkillMod(actor, 'heat', 3000)
	core.skillModService.addSkillMod(actor, 'cold', 3000)
	core.skillModService.addSkillMod(actor, 'electricity', 3000)
	core.skillModService.addSkillMod(actor, 'kinetic', 3000)
	core.skillModService.addSkillMod(actor, 'energy', 3000)
	return
        
def unequip(core, actor, target):
	core.skillModService.deductSkillMod(actor, 'acid', 3000)
	core.skillModService.deductSkillMod(actor, 'heat', 3000)
	core.skillModService.deductSkillMod(actor, 'cold', 3000)
	core.skillModService.deductSkillMod(actor, 'electricity', 3000)
	core.skillModService.deductSkillMod(actor, 'kinetic', 3000)
	core.skillModService.deductSkillMod(actor, 'energy', 3000)
	return