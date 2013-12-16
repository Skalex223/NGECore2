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
package services.combat;

import java.util.List;
import java.util.Map;
import java.util.Random;
import java.util.Vector;
import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.ScheduledFuture;
import java.util.concurrent.TimeUnit;

import org.apache.mina.core.buffer.IoBuffer;
import org.apache.mina.core.session.IoSession;

import protocol.swg.ObjControllerMessage;
import protocol.swg.PlayClientEffectLocMessage;
import protocol.swg.UpdatePVPStatusMessage;
import protocol.swg.objectControllerObjects.CombatAction;
import protocol.swg.objectControllerObjects.CombatSpam;
import protocol.swg.objectControllerObjects.CommandEnqueueRemove;
import protocol.swg.objectControllerObjects.StartTask;
import resources.common.FileUtilities;
import resources.objects.Buff;
import resources.objects.DamageOverTime;
import resources.objects.creature.CreatureObject;
import resources.objects.player.PlayerObject;
import resources.objects.tangible.TangibleObject;
import resources.objects.waypoint.WaypointObject;
import resources.objects.weapon.WeaponObject;
import services.command.CombatCommand;
import services.sui.SUIService.MessageBoxType;
import services.sui.SUIWindow;
import services.sui.SUIWindow.SUICallback;
import services.sui.SUIWindow.Trigger;
import main.NGECore;
import engine.resources.common.CRC;
import engine.resources.objects.SWGObject;
import engine.resources.scene.Point3D;
import engine.resources.service.INetworkDispatch;
import engine.resources.service.INetworkRemoteEvent;

public class CombatService implements INetworkDispatch {
	
	private NGECore core;
    private final ScheduledExecutorService scheduler = Executors.newScheduledThreadPool(1);

	public CombatService(NGECore core) {
		this.core = core;
		CombatCommands.registerCommands(core);
	}

	@Override
	public void insertOpcodes(Map<Integer, INetworkRemoteEvent> arg0, Map<Integer, INetworkRemoteEvent> arg1) {
		
	}

	@Override
	public void shutdown() {
		// TODO Auto-generated method stub
		
	}
	
	public void doCombat(final CreatureObject attacker, final TangibleObject target, final WeaponObject weapon, final CombatCommand command, final int actionCounter) {
		
		boolean success = true;
		
		if((command.getAttackType() == 0 || command.getAttackType() == 1 || command.getAttackType() == 3) && !attemptCombat(attacker, target))
			success = false;
		
		if(!applySpecialCost(attacker, weapon, command))
			success = false;
		
		if(!success) {
			IoSession session = attacker.getClient().getSession();
			CommandEnqueueRemove commandRemove = new CommandEnqueueRemove(attacker.getObjectId(), actionCounter);
			session.write(new ObjControllerMessage(0x0B, commandRemove).serialize());
			StartTask startTask = new StartTask(actionCounter, attacker.getObjectID(), command.getCommandCRC(), CRC.StringtoCRC(command.getCooldownGroup()), -1);
			session.write(new ObjControllerMessage(0x0B, startTask).serialize());
			return;
		}

		final Point3D targetPos = target.getPosition();
		final SWGObject targetParent = target.getContainer();
		
		if(command.getDelayAttackParticle().length() > 0 || command.getInitialAttackDelay() > -1) {
			
			if(command.getInitialAttackDelay() > 0) {
				
				if(command.getDelayAttackParticle().length() > 0)
					target.notifyObservers(new PlayClientEffectLocMessage(command.getDelayAttackParticle(), target.getPlanet().getName(), target.getWorldPosition()), true);
				
				try {
					Thread.sleep((long) command.getInitialAttackDelay() * 1000);
				} catch (InterruptedException e) {
					e.printStackTrace();
				}
				
	
			} else if(command.getInitialAttackDelay() <= 0 && command.getDelayAttackInterval() > 0 && command.getDelayAttackLoops() <= 1) {
				
				try {
					Thread.sleep((long) command.getDelayAttackInterval() * 1000);
				} catch (InterruptedException e) {
					e.printStackTrace();
				}
				
				if(command.getDelayAttackParticle().length() > 0)
					target.notifyObservers(new PlayClientEffectLocMessage(command.getDelayAttackParticle(), target.getPlanet().getName(), target.getWorldPosition()), true);
				
			}
			
			if(command.getDelayAttackLoops() > 1) {
				final ScheduledFuture<?> task = scheduler.scheduleAtFixedRate(new Runnable() {

					@Override
					public void run() {
						
						if(command.getDelayAttackParticle().length() > 0)
							target.notifyObservers(new PlayClientEffectLocMessage(command.getDelayAttackParticle(), target.getPlanet().getName(), target.getWorldPosition()), true);

						if(command.getAttackType() == 1)
							doSingleTargetCombat(attacker, target, weapon, command, actionCounter);
						else if(command.getAttackType() == 0 || command.getAttackType() == 2 || command.getAttackType() == 3)
							doAreaCombat(attacker, targetPos, weapon, command, actionCounter, targetParent);
						
					}
					
				}, 0, (long) (command.getDelayAttackInterval() * 1000), TimeUnit.MILLISECONDS);
				
				scheduler.schedule(new Runnable() {

					@Override
					public void run() {
						task.cancel(true);
					}
					
				}, (long) ((command.getDelayAttackInterval() * 1000) * command.getDelayAttackLoops()), TimeUnit.MILLISECONDS);
				
				return;
				
			} else {
				if(command.getAttackType() == 1)
					doSingleTargetCombat(attacker, target, weapon, command, actionCounter);
				else if(command.getAttackType() == 0 || command.getAttackType() == 2 || command.getAttackType() == 3)
					doAreaCombat(attacker, targetPos, weapon, command, actionCounter, targetParent);
			}
			
		} else {
		
			if(command.getAttackType() == 1)
				doSingleTargetCombat(attacker, target, weapon, command, actionCounter);
			else if(command.getAttackType() == 0 || command.getAttackType() == 2 || command.getAttackType() == 3)
				doAreaCombat(attacker, target, weapon, command, actionCounter);
		
		}
		
		//core.buffService.addBuffToCreature(attacker, command.getBuffNameSelf());
		
	}

	private void doAreaCombat(CreatureObject attacker, TangibleObject target, WeaponObject weapon, CombatCommand command, int actionCounter) {
		if(target instanceof CreatureObject) {
			doAreaCombat(attacker, (CreatureObject) target, weapon, command, actionCounter);
			return;
		}
	}
	
	private void doAreaCombat(CreatureObject attacker, Point3D targetPos, WeaponObject weapon, CombatCommand command, int actionCounter, SWGObject targetCell) {
		
		float x = attacker.getWorldPosition().x;
		float z = attacker.getWorldPosition().z;
		
		SWGObject fakeTargetObject = new WaypointObject(0, attacker.getPlanet(), targetPos);
		
		if(targetCell != null)
			targetCell._add(fakeTargetObject);
		
		float dirX = fakeTargetObject.getWorldPosition().x - x;
		float dirZ = fakeTargetObject.getWorldPosition().z - z;
		
		float range = command.getConeLength();
		
		List<SWGObject> inRangeObjects = core.simulationService.get(attacker.getPlanet(), fakeTargetObject.getWorldPosition().x, fakeTargetObject.getWorldPosition().z, (int) range);
		
		
		for(SWGObject obj : inRangeObjects) {
			
			if(!(obj instanceof TangibleObject) || obj == attacker)
				continue;
			
			if(obj instanceof CreatureObject && (((CreatureObject) obj).getPosture() == 13 || ((CreatureObject) obj).getPosture() == 14))
				continue;

			if(command.getAttackType() == 0 && !isInConeAngle(attacker, obj, (int) command.getConeLength(), (int) command.getConeWidth(), dirX, dirZ))
				continue;
			
			if(!core.simulationService.checkLineOfSight(fakeTargetObject, obj))
				continue;
			
			if(!attemptCombat(attacker, (TangibleObject) obj))
				continue;
						
			doSingleTargetCombat(attacker, (TangibleObject) obj, weapon, command, actionCounter);
			
		}

		if(targetCell != null)
			targetCell._remove(fakeTargetObject);
		
		core.objectService.destroyObject(fakeTargetObject);
		
	}


	private void doSingleTargetCombat(CreatureObject attacker, TangibleObject target, WeaponObject weapon, CombatCommand command, int actionCounter) {	
		if(target instanceof CreatureObject) {
			doSingleTargetCombat(attacker, (CreatureObject) target, weapon, command, actionCounter);
			return;
		}
		
		float damage = calculateDamage(attacker, target, weapon, command);
	}
	
	private void doAreaCombat(CreatureObject attacker, CreatureObject target, WeaponObject weapon, CombatCommand command, int actionCounter) {
		
		float x = attacker.getWorldPosition().x;
		float z = attacker.getWorldPosition().z;
		
		float dirX = target.getWorldPosition().x - x;
		float dirZ = target.getWorldPosition().z - z;
		
		float range = command.getConeLength();
		
		List<SWGObject> inRangeObjects = core.simulationService.get(attacker.getPlanet(), target.getWorldPosition().x, target.getWorldPosition().z, (int) range);
		
		for(SWGObject obj : inRangeObjects) {
			
			if(!(obj instanceof TangibleObject) || obj == attacker)
				continue;
			
			if(obj instanceof CreatureObject && (((CreatureObject) obj).getPosture() == 13 || ((CreatureObject) obj).getPosture() == 14))
				continue;

			if(command.getAttackType() == 0 && !isInConeAngle(attacker, obj, (int) command.getConeLength(), (int) command.getConeWidth(), dirX, dirZ))
				continue;
			
			if(!core.simulationService.checkLineOfSight(target, obj))
				continue;
			
			if(!attemptCombat(attacker, (TangibleObject) obj))
				continue;
						
			doSingleTargetCombat(attacker, (TangibleObject) obj, weapon, command, actionCounter);
			
		}
		
	}

	private void doSingleTargetCombat(CreatureObject attacker, CreatureObject target, WeaponObject weapon, CombatCommand command, int actionCounter) {	
				
		float damage = calculateDamage(attacker, target, weapon, command);
		
		if(damage > 0) {
		
			byte hitType = getHitType(attacker, target, weapon, command);
			
			switch(hitType) {
			
				case HitType.MISS:
					damage = 0;
					break;
					
				case HitType.DODGE:
					damage = 0;
					break;
	
				case HitType.PARRY:
					damage = 0;
					break;
					
				case HitType.CRITICAL:
					damage *= 1.5f;
					break;
	
			}
			byte mitigationType = -1;
			if(hitType == HitType.CRITICAL || hitType == HitType.HIT || hitType == HitType.STRIKETHROUGH) {
				mitigationType = doMitigationRolls(attacker, target, weapon, command, hitType);
				
				if(mitigationType == HitType.GLANCE) {
					damage *= 0.4f;
				} else if(mitigationType == HitType.EVASION && attacker.getSkillMod("combat_evasion_value") != null) {
					float evasionValue = (attacker.getSkillMod("combat_evasion_value").getBase() / 4) / 100;
					damage *= (1 - evasionValue);
					
				}
				
			}
			int damageBeforeArmor = (int) damage;
			damage *= (1 - getArmorReduction(attacker, target, weapon, command, hitType));
			int armorAbsorbed = (int) (damageBeforeArmor - damage);
			if(mitigationType == HitType.BLOCK) {
					
				float blockValue = (attacker.getStrength() + attacker.getSkillMod("combat_block_value").getBase()) / 2 + 25;
				damage -= blockValue;
				
			}
			
			if(damage > 0)
				applyDamage(attacker, target, (int) damage);
			
			sendCombatPackets(attacker, target, weapon, command, actionCounter, damage, armorAbsorbed, hitType);
		
			if(hitType != HitType.MISS && hitType != HitType.DODGE && hitType != HitType.PARRY && command.getBuffNameTarget().length() > 0) {
				core.buffService.addBuffToCreature(target, command.getBuffNameTarget());
			}
			if(command.getDotIntensity() > 0) {
				addDotToCreature(attacker, target, command, target.getBuffByName(command.getBuffNameTarget()));
			}
	
			if(FileUtilities.doesFileExist("scripts/commands/combat/" + command.getCommandName() + ".py"))
				core.scriptService.callScript("scripts/commands/combat/", command.getCommandName(), "run", core, attacker, target, null);

			return;
			
		}
		
		if(command.getAddedDamage() == 0 && command.getPercentFromWeapon() == 0 && command.getBuffNameTarget().length() > 0)
			core.buffService.addBuffToCreature(target, command.getBuffNameTarget());
		
		sendCombatPackets(attacker, target, weapon, command, actionCounter, damage, 0, HitType.HIT);
		
	}

	private void sendCombatPackets(CreatureObject attacker, CreatureObject target, WeaponObject weapon, CombatCommand command, int actionCounter, float damage, int armorAbsorbed, int hitType) {
		
		String animationStr = command.getRandomAnimation(weapon);
		
		CombatAction combatAction = new CombatAction(CRC.StringtoCRC(animationStr), attacker.getObjectID(), weapon.getObjectID(), target.getObjectID(), command.getCommandCRC());
		ObjControllerMessage objController = new ObjControllerMessage(0x1B, combatAction);
		attacker.notifyObserversInRange(objController, true, 125);
		
		StartTask startTask = new StartTask(actionCounter, attacker.getObjectID(), command.getCommandCRC(), CRC.StringtoCRC(command.getCooldownGroup()), command.getCooldown());
		ObjControllerMessage objController2 = new ObjControllerMessage(0x0B, startTask);
		attacker.getClient().getSession().write(objController2.serialize());
		
		CommandEnqueueRemove commandRemove = new CommandEnqueueRemove(attacker.getObjectID(), actionCounter);
		ObjControllerMessage objController3 = new ObjControllerMessage(0x0B, commandRemove);
		attacker.getClient().getSession().write(objController3.serialize());
		
		CombatSpam combatSpam = new CombatSpam(attacker.getObjectID(), target.getObjectID(), weapon.getObjectID(), (int) damage, armorAbsorbed, hitType);
		ObjControllerMessage objController4 = new ObjControllerMessage(0x1B, combatSpam);
		IoBuffer spam = objController4.serialize();
		attacker.getClient().getSession().write(spam);
		
		if(target.getClient() != null)
			target.getClient().getSession().write(spam);


	}
	
	private void sendHealPackets(CreatureObject attacker, CreatureObject target, WeaponObject weapon, CombatCommand command, int actionCounter) {
		
		CombatAction combatAction = new CombatAction(CRC.StringtoCRC(command.getDefaultAnimations()[0]), attacker.getObjectID(), weapon.getObjectID(), target.getObjectID(), command.getCommandCRC());
		ObjControllerMessage objController = new ObjControllerMessage(0x1B, combatAction);
		attacker.notifyObserversInRange(objController, true, 125);
		
		StartTask startTask = new StartTask(actionCounter, attacker.getObjectID(), command.getCommandCRC(), CRC.StringtoCRC(command.getCooldownGroup()), command.getCooldown());
		ObjControllerMessage objController2 = new ObjControllerMessage(0x0B, startTask);
		attacker.getClient().getSession().write(objController2.serialize());
		
		CommandEnqueueRemove commandRemove = new CommandEnqueueRemove(attacker.getObjectID(), actionCounter);
		ObjControllerMessage objController3 = new ObjControllerMessage(0x0B, commandRemove);
		attacker.getClient().getSession().write(objController3.serialize());

	}

	private float getArmorReduction(CreatureObject attacker, CreatureObject target, WeaponObject weapon, CombatCommand command, byte hitType) {
		
		int elementalType = 1;
		
		if(command.getPercentFromWeapon() > 0) {
			
			// TODO: elemental mitigation and damage
			
			if(weapon.getStringAttribute("cat_wpn_damage.wpn_damage_type").equals("@obj_attr_n:armor_eff_kinetic"))
				elementalType = ElementalType.KINETIC;
			else if(weapon.getStringAttribute("cat_wpn_damage.wpn_damage_type").equals("@obj_attr_n:armor_eff_energy"))
				elementalType = ElementalType.ENERGY;

		} else {
			
			elementalType = command.getElementalType();
			
		}
		
		int baseArmor = 0;
		
		switch(elementalType) {
		
			case ElementalType.KINETIC:
				baseArmor = target.getSkillMod("kinetic").getBase();
			case ElementalType.ENERGY:
				baseArmor = target.getSkillMod("energy").getBase();
			case ElementalType.HEAT:
				baseArmor = target.getSkillMod("heat").getBase();
			case ElementalType.COLD:
				baseArmor = target.getSkillMod("cold").getBase();
			case ElementalType.ACID:
				baseArmor = target.getSkillMod("acid").getBase();
			case ElementalType.ELECTRICITY:
				baseArmor = target.getSkillMod("electricity").getBase();

		}
			
		float mitigation = (float) (90 * (1 - Math.exp(-0.000125 * baseArmor)) + baseArmor / 9000);
		
		if(hitType == HitType.STRIKETHROUGH) {
			
			float stMaxValue = attacker.getSkillMod("combat_strikethrough_value").getBase() / 2 + attacker.getLuck() / 10;
			if(stMaxValue > 99)
				stMaxValue = 99;
			float stMinValue = stMaxValue / 2;

			float stValue = new Random().nextInt((int) (stMaxValue - stMinValue + 1)) + stMinValue;
			stValue /= 100;
			stValue = 1 - stValue;
			mitigation *= stValue;
		}
		
		return mitigation / 100;
		
	}

	private boolean attemptCombat(CreatureObject attacker, TangibleObject target) {
				
		if(target.getDefendersList().contains(attacker) && attacker.getDefendersList().contains(target))
			return true;
		
		if(attacker.getStateBitmask() == 0x8000000)
			return false;
		
		if(!target.isAttackableBy(attacker))
			return false;
		
		target.addDefender(attacker);
		attacker.addDefender(target);
		
		return true;
		
	}
	
	public boolean applySpecialCost(CreatureObject attacker, WeaponObject weapon, CombatCommand command) {
		
		float actionCost = command.getActionCost();
		float healthCost = command.getHealthCost();
		
		if(actionCost == 0 && healthCost == 0)
			return true;
		
		if(attacker.getSkillMod("expertise_action_all") != null)
			actionCost *= attacker.getSkillMod("expertise_action_all").getBase();
		
		float newAction = attacker.getAction() - actionCost;
		if(newAction <= 0)
			return false;
		
		float newHealth = attacker.getHealth() - healthCost;
		if(newHealth <= 0)
			return false;
		
		if(newAction != attacker.getAction())
			attacker.setAction((int) newAction);
		
		if(newHealth != attacker.getHealth())
			attacker.setHealth((int) newHealth);

		return true;
		
	}
	
	private float calculateDamage(CreatureObject attacker, CreatureObject target, WeaponObject weapon, CombatCommand command) {
		
		if(target.getBuffByName("me_stasis_self_1") != null || target.getBuffByName("me_stasis_1") != null)
			return 0;

		if(attacker.getBuffByName("me_stasis_self_1") != null || attacker.getBuffByName("me_stasis_1") != null)
			return 0;
		
		float rawDamage = command.getAddedDamage();
		
		if(command.getPercentFromWeapon() > 0 && weapon != attacker.getSlottedObject("default_weapon")) {
			
			float weaponMinDmg = weapon.getMinDamage();
			float weaponMaxDmg = weapon.getMaxDamage();
			
			if(attacker.getSlottedObject("ghost") != null) {
				PlayerObject ghost = (PlayerObject) attacker.getSlottedObject("ghost");
				if(ghost.getProfession().equals("commando_1a") && weapon.getWeaponType() == 12 && attacker.getSkillMod("expertise_devastation_bonus") != null) {
					
					if(new Random().nextFloat() <= attacker.getSkillMod("expertise_devastation_bonus").getBase() / 1000) {
						weaponMinDmg = weaponMaxDmg;
						weaponMaxDmg *= 1.1f;
					}
					
				}
			}
			
			float weaponDmg = new Random().nextInt((int) (weaponMaxDmg - weaponMinDmg + 1)) + weaponMinDmg;
			weaponDmg *= command.getPercentFromWeapon();
			rawDamage += weaponDmg;
			
			if(weapon.isMelee()) {
				
				if(attacker.getStrength() > 0) {
					rawDamage += ((attacker.getStrength() / 100) * 33);
				}
				
			}
			
		} else if(command.getPercentFromWeapon() > 0) {
			
			float weaponMinDmg = 50;
			float weaponMaxDmg = 100;
			
			float weaponDmg = new Random().nextInt((int) (weaponMaxDmg - weaponMinDmg + 1)) + weaponMinDmg;
			weaponDmg *= command.getPercentFromWeapon();
			rawDamage += weaponDmg;
			
			if(weapon.isMelee()) {
				
				if(attacker.getStrength() > 0) {
					rawDamage += ((attacker.getStrength() / 100) * 33);
				}
				
			}
			
		}
		
		if(target.getSkillMod("damage_decrease_percentage") != null) {
			rawDamage *= (1 - (target.getSkillMod("damage_decrease_percentage").getBase() / 100));
		}
		
		if(target.getSkillMod("combat_divide_damage_dealt") != null) {
			rawDamage *= (1 - (target.getSkillMod("combat_divide_damage_dealt").getBase() / 100));			
		}
		
		if(attacker.getSkillMod("expertise_damage_melee") != null) {
			rawDamage *= (1 + (attacker.getSkillMod("expertise_damage_melee").getBase() / 100));			
		}
		
		return rawDamage;
		
	}

	
	private float calculateDamage(CreatureObject attacker, TangibleObject target, WeaponObject weapon, CombatCommand command) {
		
		float rawDamage = command.getAddedDamage();
		
		if(command.getPercentFromWeapon() > 0 && weapon != attacker.getSlottedObject("default_weapon")) {
			
			float weaponMinDmg = weapon.getMinDamage();
			float weaponMaxDmg = weapon.getMaxDamage();
			
			if(attacker.getSlottedObject("ghost") != null) {
				PlayerObject ghost = (PlayerObject) attacker.getSlottedObject("ghost");
				if(ghost.getProfession().equals("commando_1a") && weapon.getWeaponType() == 12 && attacker.getSkillMod("expertise_devastation_bonus") != null) {
					
					if(new Random().nextFloat() <= attacker.getSkillMod("expertise_devastation_bonus").getBase() / 1000) {
						weaponMinDmg = weaponMaxDmg;
						weaponMaxDmg *= 1.1f;
					}
					
				}
			}
			
			float weaponDmg = new Random().nextInt((int) (weaponMaxDmg - weaponMinDmg + 1)) + weaponMinDmg;
			weaponDmg *= command.getPercentFromWeapon();
			rawDamage += weaponDmg;
			
			if(weapon.isMelee()) {
				
				if(attacker.getStrength() > 0) {
					rawDamage += ((attacker.getStrength() / 100) * 33);
				}
				
			}
			
		} else if(command.getPercentFromWeapon() > 0) {
			
			float weaponMinDmg = 50;
			float weaponMaxDmg = 100;
			
			float weaponDmg = new Random().nextInt((int) (weaponMaxDmg - weaponMinDmg + 1)) + weaponMinDmg;
			weaponDmg *= command.getPercentFromWeapon();
			rawDamage += weaponDmg;
			
			if(weapon.isMelee()) {
				
				if(attacker.getStrength() > 0) {
					rawDamage += ((attacker.getStrength() / 100) * 33);
				}
				
			}
			
		}
		
		return rawDamage;
		
	}
	
	public byte getHitType(CreatureObject attacker, CreatureObject target, WeaponObject weapon, CombatCommand command) {
		
		float r;
		Random random = new Random();
		// negation rolls(parry, miss and dodge) can only roll on single target attacks, strikethrough also only rolls on single target attacks
		if(command.getAttackType() == 1) {
		
			if(weapon.isRanged()) {
				float missChance = 0.05f;
				if(attacker.getStrength() > 0) {
					float missNegation = (float) ((attacker.getStrength() / 100) * 0.1);
					if(missNegation > 0.04f)
						missNegation = 0.04f;
					missChance -= missNegation;
				}
				r = random.nextFloat();
				if(r <= missChance)
					return HitType.MISS;
			}
			if(target.getSkillMod("display_only_dodge") != null) {
				float dodgeChance = (float) target.getSkillMod("display_only_dodge").getBase() / 10000;
		
				r = random.nextFloat();
				if(r <= dodgeChance)
					return HitType.DODGE;
			}
				
			WeaponObject weapon2 = (WeaponObject) core.objectService.getObject(((CreatureObject) target).getWeaponId());
			if(weapon2 != null && weapon2.isMelee() && target.getSkillMod("display_only_parry") != null) {
				
				float parryChance = (float) target.getSkillMod("display_only_parry").getBase() / 10000;
	
				r = random.nextFloat();
				if(r <= parryChance)
					return HitType.PARRY;
					
			}
			
			float stChance = (float) attacker.getSkillMod("display_only_strikethrough").getBase() / 10000;
			
			r = random.nextFloat();
			if(r <= stChance)
				return HitType.STRIKETHROUGH;

		}

		float critChance = (float) attacker.getSkillMod("display_only_critical").getBase() / 10000;
		r = random.nextFloat();
		if(r <= critChance)
			return HitType.CRITICAL;
		
		// TODO: Punishing blow once AI is implemented
		
		return HitType.HIT;
		
	}
	
	public byte doMitigationRolls(CreatureObject attacker, CreatureObject target, WeaponObject weapon, CombatCommand command, byte hitType) {
		
		float r;
		Random random = new Random();
					
		float blockChance = (float) target.getSkillMod("display_only_block").getBase() / 10000;
			
		r = random.nextFloat();
		if(r <= blockChance)
			return HitType.BLOCK;
			
		if(command.getAttackType() == 0 || command.getAttackType() == 2 || command.getAttackType() == 3) {
				
			float evasionChance = (float) target.getSkillMod("display_only_evasion").getBase() / 10000;
				
			r = random.nextFloat();
			if(r <= evasionChance)
				return HitType.EVASION;

		}
		
		if(hitType == HitType.HIT && target.getSkillMod("display_only_glancing_blow") != null) {
			
			float glanceChance = (float) target.getSkillMod("display_only_glancing_blow").getBase() / 10000;
			
			r = random.nextFloat();
			if(r <= glanceChance)
				return HitType.GLANCE;

		}

		return -1;
		
	}
	
	public void applyDamage(CreatureObject attacker, final CreatureObject target, int damage) {
		
		if(target.getHealth() - damage <= 0) {
			
			if(target.hasBuff("incapWeaken")) {
				deathblowPlayer(attacker, target);
				return;
			}
			
			synchronized(target.getMutex()) {
				target.setHealth(1);
				target.setPosture((byte) 13);
				target.setTurnRadius(0);
				target.setSpeedMultiplierBase(0);
			}
			ScheduledFuture<?> incapTask = scheduler.schedule(new Runnable() {

				@Override
				public void run() {
					
					synchronized(target.getMutex()) {

						if(target.getPosture() != 13)
							return;
						
						target.setPosture((byte) 0);
						target.setTurnRadius(1);
						target.setSpeedMultiplierBase(1);
					
					}

				}
				
			}, target.getIncapTimer(), TimeUnit.SECONDS);
			target.setIncapTask(incapTask);
			core.buffService.addBuffToCreature(target, "incapWeaken");
			if(target.getSlottedObject("ghost") != null)
				attacker.sendSystemMessage("You incapacitate " + target.getCustomName() + ".", (byte) 0);
			return;
		}
		synchronized(target.getMutex()) {
			target.setHealth(target.getHealth() - damage);
		}
		
	}
	
	private boolean isInConeAngle(CreatureObject attacker, SWGObject target, int coneLength, int coneWidth, float directionX, float directionZ) {
		
		float radius = coneWidth / 2;
		float angle = (float) (2 * Math.atan(coneLength / radius));
		
		float targetX = target.getWorldPosition().x - attacker.getWorldPosition().x;
		float targetZ = target.getWorldPosition().z - attacker.getWorldPosition().z;
		
		float targetAngle = (float) (Math.atan2(targetZ, targetX) -  Math.atan2(directionZ, directionX));
		
		float degrees = (float) (targetAngle * 180 / Math.PI);
		float coneAngle = angle / 2;
		
		if(degrees > coneAngle || degrees < -coneAngle)
			return false;
		
		return true;
				
	}
	
	public boolean attemptHeal(CreatureObject healer, CreatureObject target) {
		
		if(healer == target)
			return true;
		
		if(healer.getFaction().equals(target.getFaction())) {
			
			if(healer.getFactionStatus() < target.getFactionStatus())
				return false;
			
			return true;
			
		} else {
			
			if(target.getFactionStatus() == 0)
				return true;
			
			return false;
			
		}
		
	}
	
	public void doHeal(CreatureObject healer, CreatureObject target, WeaponObject weapon, CombatCommand command, int actionCounter) {
		
		boolean success = true;
		
		if(target.getMaxHealth() == target.getHealth())
			success = command.getAttackType() != 1;
		
		if(!applySpecialCost(healer, weapon, command))
			success = false;
		
		if((command.getAttackType() == 0 || command.getAttackType() == 1 || command.getAttackType() == 3) && !attemptHeal(healer, target))	
			target = healer;

		if(!success) {
			IoSession session = healer.getClient().getSession();
			CommandEnqueueRemove commandRemove = new CommandEnqueueRemove(healer.getObjectId(), actionCounter);
			session.write(new ObjControllerMessage(0x0B, commandRemove).serialize());
			StartTask startTask = new StartTask(actionCounter, healer.getObjectID(), command.getCommandCRC(), CRC.StringtoCRC(command.getCooldownGroup()), -1);
			session.write(new ObjControllerMessage(0x0B, startTask).serialize());
			return;
		}
		
		if(command.getAttackType() == 1)
			doSingleTargetHeal(healer, target, weapon, command, actionCounter);
		else if(command.getAttackType() == 0 || command.getAttackType() == 2 || command.getAttackType() == 3)
			doAreaHeal(healer, target, weapon, command, actionCounter);
		
		sendHealPackets(healer, target, weapon, command, actionCounter);
		
	}
	
	private void doSingleTargetHeal(CreatureObject healer, CreatureObject target, WeaponObject weapon, CombatCommand command, int actionCounter) {
		
		int healAmount = command.getAddedDamage();
		int healPotency = 0;
		
		if(healer.getSkillMod("expertise_healing_all") != null)
			healPotency += healer.getSkillMod("expertise_healing_all").getBase();
		if(healer.getSkillMod("expertise_healing_line_me_heal") != null)
			healPotency += healer.getSkillMod("expertise_healing_line_me_heal").getBase();
		if(healer.getSkillMod("expertise_healing_line_of_heal") != null)
			healPotency += healer.getSkillMod("expertise_healing_line_of_heal").getBase();
		if(healer.getSkillMod("expertise_healing_line_sm_heal") != null)
			healPotency += healer.getSkillMod("expertise_healing_line_sm_heal").getBase();
		if(healer.getSkillMod("expertise_healing_line_sp_heal") != null)
			healPotency += healer.getSkillMod("expertise_healing_line_sp_heal").getBase();
		if(healPotency > 0)
			healAmount += (healAmount * (healPotency / 100));
		if(target.getSkillMod("expertise_healing_reduction") != null)
			healAmount *= (1 - target.getSkillMod("expertise_healing_reduction").getBase() / 100);
		
		synchronized(target.getMutex()) {
			target.setHealth(target.getHealth() + healAmount);
		}
		
		if(FileUtilities.doesFileExist("scripts/commands/combat" + command.getCommandName() + ".py"))
			core.scriptService.callScript("scripts/commands/combat", command.getCommandName(), "run", core, healer, target, null);
		
	}
	
	private void doAreaHeal(CreatureObject healer, CreatureObject target, WeaponObject weapon, CombatCommand command, int actionCounter) {
		
		float range = command.getConeLength();
		
		List<SWGObject> inRangeObjects = core.simulationService.get(healer.getPlanet(), target.getWorldPosition().x, target.getWorldPosition().z, (int) range);
		
		for(SWGObject obj : inRangeObjects) {
			
			if(!(obj instanceof CreatureObject))
				continue;
			
			if(obj instanceof CreatureObject && (((CreatureObject) obj).getPosture() == 14))
				continue;
			
			if(!core.simulationService.checkLineOfSight(target, obj))
				continue;
			
			if(!attemptHeal(healer, (CreatureObject) obj))
				continue;
			
			doSingleTargetHeal(healer, (CreatureObject) obj, weapon, command, actionCounter);
			
		}

	}

	public void deathblowPlayer(CreatureObject attacker, CreatureObject target) {
		
		target.stopIncapTask();
		target.setIncapTask(null);
		target.setPosture((byte) 14);
		attacker.sendSystemMessage("You have killed " + target.getCustomName() + ".", (byte) 0);
		target.sendSystemMessage("@base_player:victim_dead", (byte) 0);
		attacker.removeDefender(target);
		target.removeDefender(attacker);
		
		core.playerService.sendCloningWindow(target, attacker.getSlottedObject("ghost") != null);
		
	}
	
	public boolean areInDuel(CreatureObject creature1, CreatureObject creature2) {
		
		if(creature1.getDuelList().contains(creature2) && creature2.getDuelList().contains(creature1))
			return true;
		
		return false;
		
	}
	
	public void handleDuel(CreatureObject requester, CreatureObject target) {
		
		if(!target.getDuelList().contains(requester)) {
			
			requester.getDuelList().add(target);
			requester.sendSystemMessage("You challenge " + target.getCustomName() + " to a duel.", (byte) 0);
			target.sendSystemMessage(requester.getCustomName() + " challenges you to a duel.", (byte) 0);
			return;
			
		} else {
			
			requester.getDuelList().add(target);
			requester.sendSystemMessage("You accept " + target.getCustomName() + "'s challenge.", (byte) 0);
			target.sendSystemMessage(requester.getCustomName() + " accepts your challenge.", (byte) 0);
			target.getClient().getSession().write(new UpdatePVPStatusMessage(requester.getObjectID(), 55, requester.getFaction()).serialize());
			requester.getClient().getSession().write(new UpdatePVPStatusMessage(target.getObjectID(), 55, target.getFaction()).serialize());
			
		}
		
		
	}
	
	public void handleEndDuel(CreatureObject requester, CreatureObject target) {
		
		requester.getDuelList().remove(target);
		target.getDuelList().remove(requester);
		
		target.removeDefender(requester);
		requester.removeDefender(target);
		
		target.getClient().getSession().write(new UpdatePVPStatusMessage(requester.getObjectID(), 0x16, requester.getFaction()).serialize());
		requester.getClient().getSession().write(new UpdatePVPStatusMessage(target.getObjectID(), 0x16, target.getFaction()).serialize());
		
		requester.sendSystemMessage("You end your duel with " + target.getCustomName() + ".", (byte) 0);
		target.sendSystemMessage(requester.getCustomName() + " ends your duel.", (byte) 0);

	}

	public void doRevive(CreatureObject medic, CreatureObject target, WeaponObject weapon, CombatCommand command, int actionCounter) {

		boolean success = true;
				
		if(!applySpecialCost(medic, weapon, command))
			success = false;
		
		if((command.getAttackType() == 0 || command.getAttackType() == 1 || command.getAttackType() == 3) && !attemptHeal(medic, target))	
			target = medic;

		if(!success) {
			IoSession session = medic.getClient().getSession();
			CommandEnqueueRemove commandRemove = new CommandEnqueueRemove(medic.getObjectId(), actionCounter);
			session.write(new ObjControllerMessage(0x0B, commandRemove).serialize());
			StartTask startTask = new StartTask(actionCounter, medic.getObjectID(), command.getCommandCRC(), CRC.StringtoCRC(command.getCooldownGroup()), -1);
			session.write(new ObjControllerMessage(0x0B, startTask).serialize());
			return;
		}

		if(command.getAttackType() == 1)
			doSingleTargetRevive(medic, target, weapon, command, actionCounter);
		else if(command.getAttackType() == 0 || command.getAttackType() == 2 || command.getAttackType() == 3)
			doAreaRevive(medic, target, weapon, command, actionCounter);
		
		sendHealPackets(medic, target, weapon, command, actionCounter);
		
	}
	
	private void doSingleTargetRevive(CreatureObject medic, CreatureObject target, WeaponObject weapon, CombatCommand command, int actionCounter) {
		
		SUIWindow rezWindow = core.suiService.createMessageBox(MessageBoxType.MESSAGE_BOX_YES_NO, "@spam:revive_sui_title", medic.getCustomName() + " has offered to Revive you. Click YES to revive immediately at this location without cloning.", target, null, 0);
		Vector<String> returnParams = new Vector<String>();
		returnParams.add("btnOk:Text");		
		rezWindow.addHandler(0, "", Trigger.TRIGGER_OK, returnParams, new SUICallback() {

			@Override
			public void process(SWGObject owner, int eventType, Vector<String> returnList) {
				
				CreatureObject creature = (CreatureObject) owner;
				
				if(eventType != 0 || creature.getPosture() != 14)
					return;
				
				synchronized(creature.getMutex()) {
					creature.setPosture((byte) 0);
					creature.setTurnRadius(1);
					creature.setSpeedMultiplierBase(1);
					creature.setHealth(creature.getHealth() + 4000);
				}
				
			}
			
		});
		
		core.suiService.openSUIWindow(rezWindow);
		
	}

	private void doAreaRevive(CreatureObject medic, CreatureObject target, WeaponObject weapon, CombatCommand command, int actionCounter) {
		
		float range = command.getConeLength();
		
		List<SWGObject> inRangeObjects = core.simulationService.get(medic.getPlanet(), target.getWorldPosition().x, target.getWorldPosition().z, (int) range);
		
		for(SWGObject obj : inRangeObjects) {
			
			if(!(obj instanceof CreatureObject))
				continue;
			
			if(obj instanceof CreatureObject && (((CreatureObject) obj).getPosture() != 14))
				continue;
			
			if(!attemptHeal(medic, (CreatureObject) obj))
				continue;
			
			if(!core.simulationService.checkLineOfSight(target, obj))
				continue;
			
			doSingleTargetRevive(medic, (CreatureObject) obj, weapon, command, actionCounter);
			
		}
		
	}
	
	public void addDotToCreature(final CreatureObject attacker, final CreatureObject target, final CombatCommand command, Buff debuff) {
		
		//if(debuff == null)
		//	return;
		
		if(target.getDotByName(command.getCommandName()) != null) {
			
			DamageOverTime oldDot = target.getDotByName(command.getCommandName());
			if(debuff != null && debuff.getMaxStacks() > 1)
				return;
			else {
				oldDot.getTask().cancel(true);
				target.removeDot(oldDot);
			}
			
		}
		
		final DamageOverTime dot = new DamageOverTime(command.getCommandName(), debuff, command.getDotType(), command.getDotDuration(), command.getDotIntensity());
		target.addDot(dot);
		dot.setStartTime(System.currentTimeMillis());
		
		final ScheduledFuture<?> task = scheduler.scheduleAtFixedRate(new Runnable() {

			@Override
			public void run() {

				if(dot.getRemainingDuration() <= 0) {
					target.removeDot(dot);
					dot.getTask().cancel(true);
				}
				
				doDotDamageTick(attacker, target, command, dot);
				
			}
			
		}, 10, 2000, TimeUnit.MILLISECONDS);
		
		dot.setTask(task);
		
	}
	
	public void doDotDamageTick(CreatureObject attacker, CreatureObject target, CombatCommand command, DamageOverTime dot) {
		
		int damage = dot.getIntensity();
		if(dot.getBuff() != null)
			damage *= dot.getBuff().getStacks();
		int baseArmor = 0;
		
		float innateDotResist = 0.05f;	// TODO: add armor dot resists chances
		
		if(new Random().nextFloat() <= innateDotResist)
			return;
		
		if(target.getSkillMod("expertise_dot_absorption_all") != null)
			damage *= (1 - target.getSkillMod("expertise_dot_absorption_all").getBase() / 100);
		
		switch(dot.getType()) {
		
			case "acid":
				baseArmor = target.getSkillMod("acid").getBase();
			case "heat":
				baseArmor = target.getSkillMod("heat").getBase();
			case "cold":
				baseArmor = target.getSkillMod("cold").getBase();
			case "electricity":
				baseArmor = target.getSkillMod("electricity").getBase();
			case "energy":
				baseArmor = target.getSkillMod("energy").getBase();
			case "kinetic":
				baseArmor = target.getSkillMod("electricity").getBase();
			case "poison":
				baseArmor = target.getSkillMod("acid").getBase();
			case "disease":	// disease damages action in nge, cold armor per swg wiki
				baseArmor = target.getSkillMod("cold").getBase();
			case "bleeding": // bleeding, cold armor per swg wiki
				baseArmor = target.getSkillMod("cold").getBase();
			case "fire":
				baseArmor = target.getSkillMod("heat").getBase();
				
		}
		
		if(baseArmor > 0) {
			float mitigation = (float) (90 * (1 - Math.exp(-0.000125 * baseArmor)) + baseArmor / 9000);
            mitigation /= 100;
            damage *= (1 - mitigation / 2);
		}
				
		if(dot.getType().equals("disease")) {
			target.setAction(target.getAction() - damage);
			return;
		}	
		applyDamage(attacker, target, damage);
		
	}

	public enum HitType{; 
	
		public static final byte MISS = 0;
		public static final byte DODGE = 1;
		public static final byte PARRY = 2;
		public static final byte STRIKETHROUGH = 3;
		public static final byte CRITICAL = 4;
		public static final byte PUNISHING = 5;
		public static final byte HIT = 6;
		public static final byte BLOCK = 7;
		public static final byte EVASION = 8;
		public static final byte GLANCE = 9;
	
	}
	
	public enum ElementalType {;
	
		public static final int KINETIC = 1;
		public static final int ENERGY = 2;
		public static final int BLAST = 4;
		public static final int STUN = 8;
		public static final int HEAT = 32;
		public static final int COLD = 64;
		public static final int ACID = 128;
		public static final int ELECTRICITY = 256;

	}

}
