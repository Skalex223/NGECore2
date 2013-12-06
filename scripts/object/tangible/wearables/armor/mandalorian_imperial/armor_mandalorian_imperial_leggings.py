import sys

def setup(core, object):
		object.setStringAttribute('condition', '40000/40000')
		object.setIntAttribute('volume', 1)
		object.setStringAttribute('armor_category', 'Battle')
		object.setStringAttribute('faction_restriction', 'Imperial')
		object.setIntAttribute('cat_skill_mod.skill_mod_constitution_modified', 18)
		object.setIntAttribute('cat_skill_mod.skill_mod_luck_modified', 6)
		object.setIntAttribute('cat_skill_mod.skill_mod_precision_modified', 12)
		object.setIntAttribute('cat_skill_mod.skill_mod_strength_modified', 12)
		object.setIntAttribute('cat_armor_standard_protection.energy', 5496)
		object.setIntAttribute('cat_armor_standard_protection.kinetic', 5496)
		object.setIntAttribute('cat_armor_special_protection.elemental_acid', 5496)
		object.setIntAttribute('cat_armor_special_protection.elemental_cold', 5496)
		object.setIntAttribute('cat_armor_special_protection.elemental_electrical', 5496)
		object.setIntAttribute('cat_armor_special_protection.elemental_heat', 5496)	
		return
	
def equip(core, actor, target):
        core.skillModService.addSkillMod(actor, 'acid', 1100)
        core.skillModService.addSkillMod(actor, 'heat', 1100)         
        core.skillModService.addSkillMod(actor, 'cold', 1100)
        core.skillModService.addSkillMod(actor, 'electricity', 1100)
        core.skillModService.addSkillMod(actor, 'kinetic', 1100)
        core.skillModService.addSkillMod(actor, 'energy', 1100)
        core.skillModService.addSkillMod(actor, 'constitution_modified', 18)
        core.skillModService.addSkillMod(actor, 'luck_modified', 6)
        core.skillModService.addSkillMod(actor, 'precision_modified', 12)
        core.skillModService.addSkillMod(actor, 'strength_modified', 12)
        return
        
def unequip(core, actor, target):
        core.skillModService.deductSkillMod(actor, 'acid', 1100)
        core.skillModService.deductSkillMod(actor, 'heat', 1100)         
        core.skillModService.deductSkillMod(actor, 'cold', 1100)
        core.skillModService.deductSkillMod(actor, 'electricity', 1100)
        core.skillModService.deductSkillMod(actor, 'kinetic', 1100)
        core.skillModService.deductSkillMod(actor, 'energy', 1100)
        core.skillModService.deductSkillMod(actor, 'constitution_modified', 18)
        core.skillModService.deductSkillMod(actor, 'luck_modified', 6)
        core.skillModService.deductSkillMod(actor, 'precision_modified', 12)
        core.skillModService.deductSkillMod(actor, 'strength_modified', 12)
        return