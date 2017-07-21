import pymel.core as pc
import maya.cmds as mc
import re

class Scene:
    def __init__(self, parent):
        self.defaults = ['front', 'persp',
                         'side', 'top', 'lambert1']
        self.parent = parent

    def openScene(self, path, references):
        mc.file(path,
                f = True, options = "v=0", o = True, loadNoReferences=references)

    def objects(self, typ):
        objectsList = []
        if typ == 'shader': self.objs = self.shadingEngines()
        else: self.objs = [x.getParent() for x in pc.ls(type = typ)]
        for obj in self.objs:
            if obj in self.defaults:
                continue
            objectsList.append(obj)
        return objectsList
    
    def selectObjects(self, objects = []):
        pc.select(cl = True)
        if self.parent.objectType == 'Shader':
            for obj in objects:
                pc.select(self.shadingEngineHistoryChain(self.objs[obj]), add = True, ne = True)
            return
        pc.select(objects)
    
    def export(self, path):
        pc.exportSelected(path,
                          force=True,
                          expressions = True,
                          constructionHistory = True,
                          channels = True,
                          shader = True,
                          constraints = True,
                          options="v=0",
                          typ="mayaAscii",
                          pr = True)
    
    def shadingEngines(self):
        '''
        returns the materials and shading engines
        @param:
            selection: if True, returns the materials and shading engines of selected meshes else all
        @return: dictionary {material: [shadingEngine1, shadingEngine2, ...]}
        '''
        sgMtl = {}
        sg = set()
        sg.update(set(pc.ls(type = 'shadingEngine')))
        for x in sg:
            for inputs in map(lambda inp: getattr(x, inp).inputs(), ["vs", "ds", "ss"]):
                if not inputs: continue
                mtl = str(inputs[0])
                if sgMtl.has_key(mtl):
                    if x not in sgMtl[mtl]:
                        sgMtl[mtl].append(x)
                else:
                    sgMtl[mtl] = [x]
        return sgMtl
        
    def shadingEngineHistoryChain(self, shader):
        chain = []
        shader = shader[0]
        sets = mc.sets( str( shader ), q = True )
        for inputs in map(lambda inp: getattr(shader, inp).inputs(), ["vs", "ds", "ss"]):
            if inputs:
                chain.extend([x for x in pc.listHistory(inputs[0])
                if not isinstance( x, pc.nt.Reference )
                and ((not x in sets) if sets else True)
                and not isinstance(x, pc.nt.GroupId)])
        return chain + [str(shader)]
    
def purgeChar(string, pattern = r"\W", replace = ""):
        return re.sub(r"[%s]" %pattern, replace, str(string))
