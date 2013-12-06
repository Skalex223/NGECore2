import sys

def setup(core, object):
		object.setStringAttribute('condition', '1000/1000')
		object.setIntAttribute('volume', 1)
		object.setIntAttribute('healing_combat_level_required', 1)
		object.setStringAttribute('skill_required', 'Jedi')
		object.setIntAttribute('cat_skill_mod.skill_mod_agility_modified', 10)
        return

def equip(core, actor, target):
        core.skillModService.addSkillMod(actor, 'agility_modified', 10)        
        
        return
        
def unequip(core, actor, target):
        core.skillModService.deductSkillMod(actor, 'agility_modified', 10)
        
        return