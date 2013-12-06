import sys

def setup(core, object):
		object.setStringAttribute('condition', '1000/1000')
		object.setIntAttribute('volume', 1)
		object.setIntAttribute('healing_combat_level_required', 40)
		object.setStringAttribute('skill_required', 'Jedi')
		object.setIntAttribute('cat_skill_mod.skill_mod_constitution_modified', 100)
		object.setIntAttribute('cat_skill_mod.skill_mod_precision_modified', 100)
		object.setStringAttribute('protection_level', 'Weak')
        return
        
def equip(core, actor, target):
        core.skillModService.addSkillMod(actor, 'constitution_modified', 100)
        core.skillModService.addSkillMod(actor, 'precision_modified', 100)
        core.skillModService.addSkillMod(actor, 'acid', 3000)
        core.skillModService.addSkillMod(actor, 'heat', 3000)
        core.skillModService.addSkillMod(actor, 'cold', 3000)
        core.skillModService.addSkillMod(actor, 'electricity', 3000)
        core.skillModService.addSkillMod(actor, 'kinetic', 3000)
        core.skillModService.addSkillMod(actor, 'energy', 3000)
        
        
        return
        
def unequip(core, actor, target):
        core.skillModService.deductSkillMod(actor, 'constitution_modified', 100)
        core.skillModService.deductSkillMod(actor, 'precision_modified', 100)
        core.skillModService.deductSkillMod(actor, 'acid', 3000)
        core.skillModService.deductSkillMod(actor, 'heat', 3000)
        core.skillModService.deductSkillMod(actor, 'cold', 3000)
        core.skillModService.deductSkillMod(actor, 'electricity', 3000)
        core.skillModService.deductSkillMod(actor, 'kinetic', 3000)
        core.skillModService.deductSkillMod(actor, 'energy', 3000)
        
        return