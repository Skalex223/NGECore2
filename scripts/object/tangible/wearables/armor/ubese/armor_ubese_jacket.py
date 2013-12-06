import sys

def setup(core, object):
		object.setStringAttribute('condition', '40000/40000')
		object.setIntAttribute('volume', 1)
		object.setStringAttribute('armor_category', 'Reconnaissance')
		object.setIntAttribute('sockets', 1)
		object.setIntAttribute('cat_armor_standard_protection.energy', 7000)
		object.setIntAttribute('cat_armor_standard_protection.kinetic', 5000)
		object.setIntAttribute('cat_armor_special_protection.elemental_acid', 6000)
		object.setIntAttribute('cat_armor_special_protection.elemental_cold', 6000)
		object.setIntAttribute('cat_armor_special_protection.elemental_electrical', 6000)
		object.setIntAttribute('cat_armor_special_protection.elemental_heat', 6000)	
		return
	
def equip(core, actor, target):
        core.skillModService.addSkillMod(actor, 'acid', 2400)
        core.skillModService.addSkillMod(actor, 'heat', 2400)         
        core.skillModService.addSkillMod(actor, 'cold', 2400)
        core.skillModService.addSkillMod(actor, 'electricity', 2400)
        core.skillModService.addSkillMod(actor, 'kinetic', 2000)
        core.skillModService.addSkillMod(actor, 'energy', 2800)
        return
        
def unequip(core, actor, target):
        core.skillModService.deductSkillMod(actor, 'acid', 2400)
        core.skillModService.deductSkillMod(actor, 'heat', 2400)         
        core.skillModService.deductSkillMod(actor, 'cold', 2400)
        core.skillModService.deductSkillMod(actor, 'electricity', 2400)
        core.skillModService.deductSkillMod(actor, 'kinetic', 2000)
        core.skillModService.deductSkillMod(actor, 'energy', 2800)
        return