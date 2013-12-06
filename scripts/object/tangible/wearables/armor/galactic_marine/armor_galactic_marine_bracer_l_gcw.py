import sys

def setup(core, object):
		object.setStringAttribute('condition', '40000/40000')
		object.setIntAttribute('volume', 1)
		object.setStringAttribute('armor_category', 'Assault')
		object.setStringAttribute('faction_restriction', 'Imperial')
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
        return
        
def unequip(core, actor, target):
        core.skillModService.deductSkillMod(actor, 'acid', 544)
        core.skillModService.deductSkillMod(actor, 'heat', 544)         
        core.skillModService.deductSkillMod(actor, 'cold', 544)
        core.skillModService.deductSkillMod(actor, 'electricity', 544)
        core.skillModService.deductSkillMod(actor, 'kinetic', 644)
        core.skillModService.deductSkillMod(actor, 'energy', 444)
        return