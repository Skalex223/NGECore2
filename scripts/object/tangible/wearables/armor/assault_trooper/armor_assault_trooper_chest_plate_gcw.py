import sys
#battle worn
def setup(core, object):
		object.setStringAttribute('condition', '40000/40000')
		object.setIntAttribute('volume', 1)
		object.setStringAttribute('armor_category', 'Assault')
		object.setStringAttribute('faction_restriction', 'Imperial')
		object.setIntAttribute('cat_armor_standard_protection.energy', 4608)
		object.setIntAttribute('cat_armor_standard_protection.kinetic', 6608)
		object.setIntAttribute('cat_armor_special_protection.elemental_acid', 5608)
		object.setIntAttribute('cat_armor_special_protection.elemental_cold', 5608)
		object.setIntAttribute('cat_armor_special_protection.elemental_electrical', 5608)
		object.setIntAttribute('cat_armor_special_protection.elemental_heat', 5608)	
		return
	
def equip(core, actor, target):
        core.skillModService.addSkillMod(actor, 'acid', 1123)
        core.skillModService.addSkillMod(actor, 'heat', 1123)         
        core.skillModService.addSkillMod(actor, 'cold', 1123)
        core.skillModService.addSkillMod(actor, 'electricity', 1123)
        core.skillModService.addSkillMod(actor, 'kinetic', 1323)
        core.skillModService.addSkillMod(actor, 'energy', 923)
        return
        
def unequip(core, actor, target):
        core.skillModService.deductSkillMod(actor, 'acid', 1123)
        core.skillModService.deductSkillMod(actor, 'heat', 1123)         
        core.skillModService.deductSkillMod(actor, 'cold', 1123)
        core.skillModService.deductSkillMod(actor, 'electricity', 1123)
        core.skillModService.deductSkillMod(actor, 'kinetic', 1323)
        core.skillModService.deductSkillMod(actor, 'energy', 923)
        return