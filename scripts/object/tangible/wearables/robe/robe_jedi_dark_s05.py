import sys
#elder dark council
def setup(core, object):
	return
        
def equip(core, actor, target):
	core.skillModService.addSkillMod(actor, 'acid', 6500)
	core.skillModService.addSkillMod(actor, 'heat', 6500)
	core.skillModService.addSkillMod(actor, 'cold', 6500)
	core.skillModService.addSkillMod(actor, 'electricity', 6500)
	core.skillModService.addSkillMod(actor, 'kinetic', 6500)
	core.skillModService.addSkillMod(actor, 'energy', 6500)
        
	Buff = actor.getBuffByName('proc_old_dark_jedi_gift')
	if actor.getBuffList().contains(Buff):
		core.buffService.removeBuffFromCreature(actor, Buff)
		return
                
	if actor:
		core.buffService.addBuffToCreature(actor, 'proc_old_dark_jedi_gift')
		return
	return
        
def unequip(core, actor, target):
	core.skillModService.deductSkillMod(actor, 'acid', 6500)
	core.skillModService.deductSkillMod(actor, 'heat', 6500)
	core.skillModService.deductSkillMod(actor, 'cold', 6500)
	core.skillModService.deductSkillMod(actor, 'electricity', 6500)
	core.skillModService.deductSkillMod(actor, 'kinetic', 6500)
	core.skillModService.deductSkillMod(actor, 'energy', 6500)
        
	Buff = actor.getBuffByName('proc_old_dark_jedi_gift')
	if actor.getBuffList().contains(Buff):
		core.buffService.removeBuffFromCreature(actor, Buff)
		return
	return