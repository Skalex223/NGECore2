import sys

def setup(core, object):
		object.setStringAttribute('condition', '40000/40000')
		object.setIntAttribute('volume', 1)
		object.setStringAttribute('armor_category', 'Assault')
		object.setStringAttribute('faction_restriction', 'Imperial')
		object.setIntAttribute('cat_armor_standard_protection.energy', 5000)
		object.setIntAttribute('cat_armor_standard_protection.kinetic', 7000)
		object.setIntAttribute('cat_armor_special_protection.elemental_acid', 6000)
		object.setIntAttribute('cat_armor_special_protection.elemental_cold', 6000)
		object.setIntAttribute('cat_armor_special_protection.elemental_electrical', 6000)
		object.setIntAttribute('cat_armor_special_protection.elemental_heat', 6000)	
		return
	
def equip(core, actor, target):
        core.skillModService.addSkillMod(actor, 'acid', 600)
        core.skillModService.addSkillMod(actor, 'heat', 600)         
        core.skillModService.addSkillMod(actor, 'cold', 600)
        core.skillModService.addSkillMod(actor, 'electricity', 600)
        core.skillModService.addSkillMod(actor, 'kinetic', 700)
        core.skillModService.addSkillMod(actor, 'energy', 500)
        return
        
def unequip(core, actor, target):
        core.skillModService.deductSkillMod(actor, 'acid', 600)
        core.skillModService.deductSkillMod(actor, 'heat', 600)         
        core.skillModService.deductSkillMod(actor, 'cold', 600)
        core.skillModService.deductSkillMod(actor, 'electricity', 600)
        core.skillModService.deductSkillMod(actor, 'kinetic', 700)
        core.skillModService.deductSkillMod(actor, 'energy', 500)
        return