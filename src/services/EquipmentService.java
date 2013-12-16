/*******************************************************************************
 * Copyright (c) 2013 <Project SWG>
 * 
 * This File is part of NGECore2.
 * 
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Lesser General Public License for more details.
 * 
 * You should have received a copy of the GNU Lesser General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 * 
 * Using NGEngine to work with NGECore2 is making a combined work based on NGEngine. 
 * Therefore all terms and conditions of the GNU Lesser General Public License cover the combination.
 ******************************************************************************/
package services;

import java.util.Map;
import java.util.Map.Entry;
import java.util.TreeMap;
import org.python.core.Py;
import org.python.core.PyObject;
import resources.objects.creature.CreatureObject;
import main.NGECore;
import engine.resources.objects.SWGObject;
import engine.resources.service.INetworkDispatch;
import engine.resources.service.INetworkRemoteEvent;

public class EquipmentService implements INetworkDispatch {
	
	private NGECore core;

	public EquipmentService(NGECore core) {
		this.core = core;
	}

	@Override
	public void insertOpcodes(Map<Integer, INetworkRemoteEvent> arg0, Map<Integer, INetworkRemoteEvent> arg1) {
		
	}

	@Override
	public void shutdown() {
		
	}
	
	public void equip(CreatureObject actor, SWGObject item, SWGObject replacedItem) {

		if(replacedItem != null)
			unequip(actor, replacedItem);
		
		String template = item.getTemplate();
		String serverTemplate = template.replace(".iff", "");
		PyObject func = core.scriptService.getMethod("scripts/" + serverTemplate.split("shared_" , 2)[0].replace("shared_", ""), serverTemplate.split("shared_" , 2)[1], "equip");
		if(func != null)
			func.__call__(Py.java2py(core), Py.java2py(actor), Py.java2py(item));
		
		// TODO: add health/action bonus from crafted weapon with augmentations
		
		Map<String, Object> attributes = new TreeMap<String, Object>(item.getAttributes());
		
		for(Entry<String, Object> e : attributes.entrySet()) {
			
			if(e.getKey().startsWith("cat_skill_mod_bonus.@stat_n:")) {
				core.skillModService.addSkillMod(actor, e.getKey().replace("cat_skill_mod_bonus.@stat_n:", ""), Integer.parseInt((String) e.getValue()));
			}
			if(e.getKey().startsWith("cat_stat_mod_bonus.@stat_n:")) {
				core.skillModService.addSkillMod(actor, e.getKey().replace("cat_stat_mod_bonus.@stat_n:", ""), Integer.parseInt((String) e.getValue()));
			}
			//if(e.getKey().startsWith("cat_special_protection.elemental_")){
			//	if(template.contains("helmet") || template.contains("chest") || template.contains("leggings")){
			//		core.skillModService.addSkillMod(actor, e.getKey().replace("cat_special_protection.elemental_", ""), Integer.parseInt((String) e.getValue()));	
			//}	 if(template.contains("bicep") || template.contains("bracer")){
			//		core.skillModService.addSkillMod(actor, e.getKey().replace("cat_special_protection.elemental_", ""), Integer.parseInt((String) e.getValue()));
			//}}
			//if(e.getKey().startsWith("cat_standard_protection.")){
			//	if(template.contains("helmet") || template.contains("chest") || template.contains("leggings")){
			//		core.skillModService.addSkillMod(actor, e.getKey().replace("cat_standard_protection.", ""), Integer.parseInt((String) e.getValue()));	
			//}	 if(template.contains("bicep") || template.contains("bracer")){
			//		core.skillModService.addSkillMod(actor, e.getKey().replace("cat_standard_protection.", ""), Integer.parseInt((String) e.getValue()));
			//}}
		}
	}
	
	public void unequip(CreatureObject actor, SWGObject item) {
		
		String template = item.getTemplate();
		String serverTemplate = template.replace(".iff", "");
		PyObject func = core.scriptService.getMethod("scripts/" + serverTemplate.split("shared_" , 2)[0].replace("shared_", ""), serverTemplate.split("shared_" , 2)[1], "unequip");
		if(func != null)
			func.__call__(Py.java2py(core), Py.java2py(actor), Py.java2py(item));

		// TODO: remove health/action bonus from crafted weapon with augmentations
		
		Map<String, Object> attributes = new TreeMap<String, Object>(item.getAttributes());
		
		for(Entry<String, Object> e : attributes.entrySet()) {
			
			if(e.getKey().startsWith("cat_skill_mod_bonus.@stat_n:")) {
				core.skillModService.deductSkillMod(actor, e.getKey().replace("cat_skill_mod_bonus.@stat_n:", ""), Integer.parseInt((String) e.getValue()));
			}
			if(e.getKey().startsWith("cat_stat_mod_bonus.@stat_n:")) {
				core.skillModService.deductSkillMod(actor, e.getKey().replace("cat_stat_mod_bonus.@stat_n:", ""), Integer.parseInt((String) e.getValue()));
			}
			//if(e.getKey().startsWith("cat_special_protection.elemental_")){
			//	if(template.contains("helmet") || template.contains("chest") || template.contains("leggings")){
			//		core.skillModService.deductSkillMod(actor, e.getKey().replace("cat_special_protection.elemental_", ""), Integer.parseInt((String) e.getValue()));	
			//}	 if(template.contains("bicep") || template.contains("bracer")){
			//		core.skillModService.deductSkillMod(actor, e.getKey().replace("cat_special_protection.elemental_", ""), Integer.parseInt((String) e.getValue()));
			//}}	
			//if(e.getKey().startsWith("cat_standard_protection.")){
			//	if(template.contains("helmet") || template.contains("chest") || template.contains("leggings")){
			//		core.skillModService.deductSkillMod(actor, e.getKey().replace("cat_standard_protection.", ""), Integer.parseInt((String) e.getValue()));	
			//} 	if(template.contains("bicep") || template.contains("bracer")){
			//		core.skillModService.deductSkillMod(actor, e.getKey().replace("cat_standard_protection.", ""), Integer.parseInt((String) e.getValue()));
			//}}

		}

	}


}
