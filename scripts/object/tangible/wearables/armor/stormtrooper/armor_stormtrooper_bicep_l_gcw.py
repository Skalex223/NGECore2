import sys

def setup(core, object):
		object.setStringAttribute('condition', '40000/40000')
		object.setIntAttribute('volume', 1)
		object.setStringAttribute('armor_category', 'Battle')
		object.setStringAttribute('faction_restriction', 'Imperial')
		object.setIntAttribute('cat_armor_standard_protection.energy', 5608)
		object.setIntAttribute('cat_armor_standard_protection.kinetic', 5608)
		object.setIntAttribute('cat_armor_special_protection.elemental_acid', 5608)
		object.setIntAttribute('cat_armor_special_protection.elemental_cold', 5608)
		object.setIntAttribute('cat_armor_special_protection.elemental_electrical', 5608)
		object.setIntAttribute('cat_armor_special_protection.elemental_heat', 5608)	
		return
	
def equip(core, actor, target):
        core.skillModService.addSkillMod(actor, 'acid', 561)
        core.skillModService.addSkillMod(actor, 'heat', 561)         
        core.skillModService.addSkillMod(actor, 'cold', 561)
        core.skillModService.addSkillMod(actor, 'electricity', 561)
        core.skillModService.addSkillMod(actor, 'kinetic', 561)
        core.skillModService.addSkillMod(actor, 'energy', 561)
        return
        
def unequip(core, actor, target):
        core.skillModService.deductSkillMod(actor, 'acid', 561)
        core.skillModService.deductSkillMod(actor, 'heat', 561)         
        core.skillModService.deductSkillMod(actor, 'cold', 561)
        core.skillModService.deductSkillMod(actor, 'electricity', 561)
        core.skillModService.deductSkillMod(actor, 'kinetic', 561)
        core.skillModService.deductSkillMod(actor, 'energy', 561)
        return