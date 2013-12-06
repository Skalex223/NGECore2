import sys

def setup(core, object):
		object.setStringAttribute('condition', '1000/1000')
		object.setIntAttribute('volume', 1)
		object.setIntAttribute('healing_combat_level_required', 20)
		object.setStringAttribute('skill_required', 'Jedi')
		object.setIntAttribute('cat_skill_mod.skill_mod_constitution_modified', 21)
		object.setStringAttribute('protection_level', 'Faint')
        return
        
def equip(core, actor, target):
        core.skillModService.addSkillMod(actor, 'constitution_modified', 21)
        core.skillModService.addSkillMod(actor, 'acid', 1400)
        core.skillModService.addSkillMod(actor, 'heat', 1400)
        core.skillModService.addSkillMod(actor, 'cold', 1400)
        core.skillModService.addSkillMod(actor, 'electricity', 1400)
        core.skillModService.addSkillMod(actor, 'kinetic', 1400)
        core.skillModService.addSkillMod(actor, 'energy', 1400)
        
        
        return
        
def unequip(core, actor, target):
        core.skillModService.deductSkillMod(actor, 'constitution_modified', 21)
        core.skillModService.deductSkillMod(actor, 'acid', 1400)
        core.skillModService.deductSkillMod(actor, 'heat', 1400)
        core.skillModService.deductSkillMod(actor, 'cold', 1400)
        core.skillModService.deductSkillMod(actor, 'electricity', 1400)
        core.skillModService.deductSkillMod(actor, 'kinetic', 1400)
        core.skillModService.deductSkillMod(actor, 'energy', 1400)
        
        return