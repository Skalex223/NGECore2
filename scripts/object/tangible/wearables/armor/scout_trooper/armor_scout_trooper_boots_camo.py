import sys

def setup(core, object):
		object.setStringAttribute('condition', '40000/40000')
		object.setIntAttribute('volume', 1)
		object.setStringAttribute('armor_category', 'Battle')
		object.setStringAttribute('faction_restriction', 'Imperial')
		object.setIntAttribute('cat_skill_mod.skill_mod_constitution_modified', 15)
		object.setIntAttribute('cat_skill_mod.skill_mod_luck_modified', 10)
		object.setIntAttribute('cat_skill_mod.skill_mod_precision_modified', 20)
		return
			
def equip(core, actor, target):
        core.skillModService.addSkillMod(actor, 'constitution_modified', 15)
        core.skillModService.addSkillMod(actor, 'luck_modified', 10)
        core.skillModService.addSkillMod(actor, 'precision_modified', 20)
        return
        
def unequip(core, actor, target):
        core.skillModService.deductSkillMod(actor, 'constitution_modified', 15)
        core.skillModService.deductSkillMod(actor, 'luck_modified', 10)
        core.skillModService.deductSkillMod(actor, 'precision_modified', 20)       
        return