import sys
#light lightning
def setup(core, object):
	object.setStringAttribute('condition', '1000/1000')
	object.setIntAttribute('Volume', 1)
	
	object.setDamageType('@obj_attr_n:armor_eff_energy')
	object.setStringAttribute('cat_wpn_damage.wpn_category', 'Rifle')
	object.setStringAttribute('cat_wpn_damage.wpn_attack_speed', '0.8')
	object.setStringAttribute('cat_wpn_damage.damage', '0-0')
	object.setMinDamage(510)
	object.setMaxDamage(1045)
	object.setElementalType('@obj_attr_n:elemental_electrical')
	object.setElementalDamage(155)
	object.setIntAttribute('cat_wpn_damage.weapon_dps', testRifle.getDamagePerSecond())
	object.setStringAttribute('cat_wpn_other.wpn_range', '0-64m')
	
	return