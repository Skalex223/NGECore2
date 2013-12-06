import sys

def setup(core, object):
		object.setStringAttribute('condition', '40000/40000')
		object.setIntAttribute('volume', 1)
		object.setStringAttribute('armor_category', 'Assault')
		object.setStringAttribute('faction_restriction', 'Rebel')
		object.setIntAttribute('cat_skill_mod.skill_mod_constitution_modified', 23)
		object.setIntAttribute('cat_skill_mod.skill_mod_luck_modified', 11)
		object.setIntAttribute('cat_skill_mod.skill_mod_precision_modified', 17)
		object.setIntAttribute('cat_armor_standard_protection.energy', 4664)
		object.setIntAttribute('cat_armor_standard_protection.kinetic', 6664)
		object.setIntAttribute('cat_armor_special_protection.elemental_acid', 5664)
		object.setIntAttribute('cat_armor_special_protection.elemental_cold', 5664)
		object.setIntAttribute('cat_armor_special_protection.elemental_electrical', 5664)
		object.setIntAttribute('cat_armor_special_protection.elemental_heat', 5664)	
		return
	
def equip(core, actor, target):
        core.skillModService.addSkillMod(actor, 'acid', 567)
        core.skillModService.addSkillMod(actor, 'heat', 567)         
        core.skillModService.addSkillMod(actor, 'cold', 567)
        core.skillModService.addSkillMod(actor, 'electricity', 567)
        core.skillModService.addSkillMod(actor, 'kinetic', 667)
        core.skillModService.addSkillMod(actor, 'energy', 467)
        core.skillModService.addSkillMod(actor, 'constitution_modified', 23)
        core.skillModService.addSkillMod(actor, 'luck_modified', 11)
        core.skillModService.addSkillMod(actor, 'precision_modified', 17)
        return
        
def unequip(core, actor, target):
        core.skillModService.deductSkillMod(actor, 'acid', 567)
        core.skillModService.deductSkillMod(actor, 'heat', 567)         
        core.skillModService.deductSkillMod(actor, 'cold', 567)
        core.skillModService.deductSkillMod(actor, 'electricity', 567)
        core.skillModService.deductSkillMod(actor, 'kinetic', 667)
        core.skillModService.deductSkillMod(actor, 'energy', 467)
        core.skillModService.deductSkillMod(actor, 'constitution_modified', 23)
        core.skillModService.deductSkillMod(actor, 'luck_modified', 11)
        core.skillModService.deductSkillMod(actor, 'precision_modified', 27)       
        return