import sys

def setup(core, object):
		object.setStringAttribute('condition', '1000/1000')
		object.setIntAttribute('volume', 1)
		object.setIntAttribute('healing_combat_level_required', 80)
		object.setStringAttribute('skill_required', 'Jedi')
		object.setIntAttribute('cat_skill_mod.skill_mod_luck_modified', 185)
		object.setIntAttribute('cat_skill_mod.skill_mod_constitution_modified', 185)
		object.setIntAttribute('cat_skill_mod.skill_mod_precision_modified', 185)
		object.setStringAttribute('protection_level', 'Luminous')
        return
        
def equip(core, actor, target):
        core.skillModService.addSkillMod(actor, 'constitution_modified', 185)
        core.skillModService.addSkillMod(actor, 'precision_modified', 185)
        core.skillModService.addSkillMod(actor, 'luck_modified', 185)
        core.skillModService.addSkillMod(actor, 'acid', 5000)
        core.skillModService.addSkillMod(actor, 'heat', 5000)
        core.skillModService.addSkillMod(actor, 'cold', 5000)
        core.skillModService.addSkillMod(actor, 'electricity', 5000)
        core.skillModService.addSkillMod(actor, 'kinetic', 5000)
        core.skillModService.addSkillMod(actor, 'energy', 5000)
        
        
        return
        
def unequip(core, actor, target):
        core.skillModService.deductSkillMod(actor, 'constitution_modified', 185)
        core.skillModService.deductSkillMod(actor, 'precision_modified', 185)
        core.skillModService.deductSkillMod(actor, 'luck_modified', 185)
        core.skillModService.deductSkillMod(actor, 'acid', 5000)
        core.skillModService.deductSkillMod(actor, 'heat', 5000)
        core.skillModService.deductSkillMod(actor, 'cold', 5000)
        core.skillModService.deductSkillMod(actor, 'electricity', 5000)
        core.skillModService.deductSkillMod(actor, 'kinetic', 5000)
        core.skillModService.deductSkillMod(actor, 'energy', 5000)
        
        return