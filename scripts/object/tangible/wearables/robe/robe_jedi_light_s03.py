import sys

def setup(core, object):
		return
        
def equip(core, actor, target):
	core.skillModService.addSkillMod(actor, 'acid', 5000)
	core.skillModService.addSkillMod(actor, 'heat', 5000)
	core.skillModService.addSkillMod(actor, 'cold', 5000)
	core.skillModService.addSkillMod(actor, 'electricity', 5000)
	core.skillModService.addSkillMod(actor, 'kinetic', 5000)
	core.skillModService.addSkillMod(actor, 'energy', 5000)
	return
        
def unequip(core, actor, target):
	core.skillModService.deductSkillMod(actor, 'acid', 5000)
	core.skillModService.deductSkillMod(actor, 'heat', 5000)
	core.skillModService.deductSkillMod(actor, 'cold', 5000)
	core.skillModService.deductSkillMod(actor, 'electricity', 5000)
	core.skillModService.deductSkillMod(actor, 'kinetic', 5000)
	core.skillModService.deductSkillMod(actor, 'energy', 5000)
	return