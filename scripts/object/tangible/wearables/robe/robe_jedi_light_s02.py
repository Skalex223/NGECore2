import sys

def setup(core, object):
		object.setStringAttribute('condition', '1000/1000')
		object.setIntAttribute('volume', 1)
		object.setIntAttribute('healing_combat_level_required', 60)
		object.setStringAttribute('skill_required', 'Jedi')
		object.setIntAttribute('cat_skill_mod.skill_mod_constitution_modified', 145)
		object.setIntAttribute('cat_skill_mod.skill_mod_strength_modified', 145)
		object.setStringAttribute('protection_level', 'Lucent')
        return
        
def equip(core, actor, target):
        core.skillModService.addSkillMod(actor, 'constitution_modified', 145)
        core.skillModService.addSkillMod(actor, 'strength_modified', 145)
        core.skillModService.addSkillMod(actor, 'acid', 4000)
        core.skillModService.addSkillMod(actor, 'heat', 4000)
        core.skillModService.addSkillMod(actor, 'cold', 4000)
        core.skillModService.addSkillMod(actor, 'electricity', 4000)
        core.skillModService.addSkillMod(actor, 'kinetic', 4000)
        core.skillModService.addSkillMod(actor, 'energy', 4000)
        
        
        return
        
def unequip(core, actor, target):
        core.skillModService.deductSkillMod(actor, 'constitution_modified', 145)
        core.skillModService.deductSkillMod(actor, 'strength_modified', 145)
        core.skillModService.deductSkillMod(actor, 'acid', 4000)
        core.skillModService.deductSkillMod(actor, 'heat', 4000)
        core.skillModService.deductSkillMod(actor, 'cold', 4000)
        core.skillModService.deductSkillMod(actor, 'electricity', 4000)
        core.skillModService.deductSkillMod(actor, 'kinetic', 4000)
        core.skillModService.deductSkillMod(actor, 'energy', 4000)
        
        return