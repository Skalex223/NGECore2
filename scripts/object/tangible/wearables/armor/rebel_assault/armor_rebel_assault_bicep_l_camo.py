import sys

def setup(core, object):
		object.setStringAttribute('condition', '40000/40000')
		object.setIntAttribute('volume', 1)
		object.setStringAttribute('armor_category', 'Assault')
		object.setStringAttribute('faction_restriction', 'Rebel')
		object.setIntAttribute('cat_skill_mod.skill_mod_constitution_modified', 15)
		object.setIntAttribute('cat_skill_mod.skill_mod_luck_modified', 10)
		object.setIntAttribute('cat_skill_mod.skill_mod_precision_modified', 20)
		object.setIntAttribute('cat_armor_standard_protection.energy', 4440)
		object.setIntAttribute('cat_armor_standard_protection.kinetic', 6440)
		object.setIntAttribute('cat_armor_special_protection.elemental_acid', 5440)
		object.setIntAttribute('cat_armor_special_protection.elemental_cold', 5440)
		object.setIntAttribute('cat_armor_special_protection.elemental_electrical', 5440)
		object.setIntAttribute('cat_armor_special_protection.elemental_heat', 5440)	
		return
			
def equip(core, actor, target):
        core.skillModService.addSkillMod(actor, 'acid', 544)
        core.skillModService.addSkillMod(actor, 'heat', 544)         
        core.skillModService.addSkillMod(actor, 'cold', 544)
        core.skillModService.addSkillMod(actor, 'electricity', 544)
        core.skillModService.addSkillMod(actor, 'kinetic', 644)
        core.skillModService.addSkillMod(actor, 'energy', 444)
        core.skillModService.addSkillMod(actor, 'constitution_modified', 15)
        core.skillModService.addSkillMod(actor, 'luck_modified', 10)
        core.skillModService.addSkillMod(actor, 'precision_modified', 20)
        return
        
def unequip(core, actor, target):
        core.skillModService.deductSkillMod(actor, 'acid', 544)
        core.skillModService.deductSkillMod(actor, 'heat', 544)         
        core.skillModService.deductSkillMod(actor, 'cold', 544)
        core.skillModService.deductSkillMod(actor, 'electricity', 544)
        core.skillModService.deductSkillMod(actor, 'kinetic', 644)
        core.skillModService.deductSkillMod(actor, 'energy', 444)
        core.skillModService.deductSkillMod(actor, 'constitution_modified', 15)
        core.skillModService.deductSkillMod(actor, 'luck_modified', 10)
        core.skillModService.deductSkillMod(actor, 'precision_modified', 20)       
        return