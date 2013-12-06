import sys
#elder light
def setup(core, object):
		object.setStringAttribute('condition', '1000/1000')
		object.setIntAttribute('volume', 1)
		object.setIntAttribute('healing_combat_level_required', 80)
		object.setStringAttribute('skill_required', 'Jedi')
		object.setIntAttribute('cat_skill_mod.skill_mod_agility_modified', 250)
		object.setIntAttribute('cat_skill_mod.skill_mod_constitution_modified', 250)
		object.setIntAttribute('cat_skill_mod.skill_mod_strength_modified', 250)
		object.setStringAttribute('effect', 'Gift of the Light Side')
		object.setStringAttribute('protection_level', 'Radiant')
        return
        
def equip(core, actor, target):
        core.skillModService.addSkillMod(actor, 'constitution_modified', 250)
        core.skillModService.addSkillMod(actor, 'agility_modified', 250)
        core.skillModService.addSkillMod(actor, 'strength_modified', 250)
        core.skillModService.addSkillMod(actor, 'acid', 6500)
        core.skillModService.addSkillMod(actor, 'heat', 6500)
        core.skillModService.addSkillMod(actor, 'cold', 6500)
        core.skillModService.addSkillMod(actor, 'electricity', 6500)
        core.skillModService.addSkillMod(actor, 'kinetic', 6500)
        core.skillModService.addSkillMod(actor, 'energy', 6500)
        
        
        Buff = actor.getBuffByName('proc_old_light_jedi_gift')
        if actor.getBuffList().contains(Buff):
                core.buffService.removeBuffFromCreature(actor, Buff)
                return
                
        if actor:
                core.buffService.addBuffToCreature(actor, 'proc_old_light_jedi_gift')
                return
        return
        
def unequip(core, actor, target):
        core.skillModService.deductSkillMod(actor, 'constitution_modified', 250)
        core.skillModService.deductSkillMod(actor, 'agility_modified', 250)
        core.skillModService.deductSkillMod(actor, 'strength_modified', 250)
        core.skillModService.deductSkillMod(actor, 'acid', 6500)
        core.skillModService.deductSkillMod(actor, 'heat', 6500)
        core.skillModService.deductSkillMod(actor, 'cold', 6500)
        core.skillModService.deductSkillMod(actor, 'electricity', 6500)
        core.skillModService.deductSkillMod(actor, 'kinetic', 6500)
        core.skillModService.deductSkillMod(actor, 'energy', 6500)
        
        Buff = actor.getBuffByName('proc_old_light_jedi_gift')
        if actor.getBuffList().contains(Buff):
                core.buffService.removeBuffFromCreature(actor, Buff)
                return
        return