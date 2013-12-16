import sys

def setup():
        return
        
def run(core, actor, target, commandString):
        
        if not commandString.startswith('object/tangible') and not commandString.startswith('object/weapon'):
        	core.scriptService.callScript('scripts/object/tangible/generateditem/', 'setup', commandString, core, actor)
        	return 
                                
        object = core.objectService.createObject(commandString, actor.getPlanet())

        if not object:
                return
                
        inventory = actor.getSlottedObject('inventory')
        
        if inventory:
                inventory.add(object)
                
        return