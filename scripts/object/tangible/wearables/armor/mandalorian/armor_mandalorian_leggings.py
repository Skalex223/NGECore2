import sys

def setup(core, object):
		display.setStringAttribute('Condition', '40000/40000')
		display.setIntAttribute('volume', 1)
		display.setStringAttribute('armor_category', 'Assault')
		display.setIntAttribute('sockets', 1)
		display.setIntAttribute('cat_armor_standard_protection.energy', 5000)
		display.setIntAttribute('cat_armor_standard_protection.kinetic', 7000)
		display.setIntAttribute('cat_armor_special_protection.elemental_acid', 6000)
		display.setIntAttribute('cat_armor_special_protection.elemental_cold', 6000)
		display.setIntAttribute('cat_armor_special_protection.elemental_electrical', 6000)
		display.setIntAttribute('cat_armor_special_protection.elemental_heat', 6000)	
		return
	
def equip(core, actor, target):
        core.skillModService.addSkillMod(actor, 'acid', 1200)
        core.skillModService.addSkillMod(actor, 'heat', 1200)         
        core.skillModService.addSkillMod(actor, 'cold', 1200)
        core.skillModService.addSkillMod(actor, 'electricity', 1200)
        core.skillModService.addSkillMod(actor, 'kinetic', 1400)
        core.skillModService.addSkillMod(actor, 'energy', 1000)
        return
        
def unequip(core, actor, target):
        core.skillModService.deductSkillMod(actor, 'acid', 1200)
        core.skillModService.deductSkillMod(actor, 'heat', 1200)         
        core.skillModService.deductSkillMod(actor, 'cold', 1200)
        core.skillModService.deductSkillMod(actor, 'electricity', 1200)
        core.skillModService.deductSkillMod(actor, 'kinetic', 1400)
        core.skillModService.deductSkillMod(actor, 'energy', 1000)
        return