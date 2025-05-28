# flake8: noqa: E701
"""
 수작업으로 필요할때 추가하는 스텁파일
 - 독스티링 적용(독스트링은 상속이 안되기 때문에 여기서 적어야함)
    - 클래스 메소드 설명은 잘 따라옴.
"""
from __future__ import annotations
import enum
from typing import Type, Any, overload, Literal
import MXSWrapperBase as mxs


def attime(time):...
  
def animate(on_off: bool): ...

class runtime:
    objects: list
    selection: list
    currentTime: int
    maxfilepath: str
    maxFilePath: str
    maxfilename: str
    maxFileName: str
    animationRange: runtime.Interval

    class Value:
        ...

    class Point3(Value):
        """[<expr>, <expr>, <expr>]

        [2022 api link](https://help.autodesk.com/view/MAXDEV/2022/ENU/?guid=GUID-1564BD35-50EA-4140-9150-1AECC89F713C)
        """
        x: int
        y: int
        z: int
        def __init__(self, *args, **kwargs) -> None: ...
        ...

    class Array(Value, list):
        ...

    class Interval(Value):
        start: runtime.Time
        end: runtime.Time
    class MixinInterface(Value):
        ...

    class BitArray(Value):
        def __iter__(self) -> runtime.BitArray: ...
        def __next__(self) -> int: ...

    class interface(Value):
        ...

    class skinUtils(interface):
        @staticmethod
        def ExtractSkinData(node) -> None: ...

        @staticmethod
        def ImportSkinData(target_node, source_node) -> None: ...

        @staticmethod
        def ImportSkinDataNoDialog(
            matchByName: bool,
            removeTargetPrefix: bool,
            removeTargetSuffix: bool,
            removeSourcePrefix: bool,
            removeSourceSuffix: bool,
            threshold: float,
            interpolationType: int
        ) -> None:
            '''
            - matchByName 매개 변수가 true로 설정되면 뼈가 이름으로 일치합니다(대화 상자의 Match By Name 버튼을 누르는 것과 동일). 거짓이면 뼈는 인덱스로 일치합니다.
            - 논쟁 2 ~ 5 개는 대화 상자의 수정 및 접미사 제거 체크 박스의 상태에 해당합니다.
            - threshold: 임계값 인수는 대화 상자의 임계값에 해당합니다.The threshold argument corresponds to the Threshold value in the dialog. 이것은 가장 가까운 이웃 임계 값입니다.
            - interpolationType: 마지막 인수는 `Interpolation Type` 드롭다운 목록의 선택에 해당합니다. 가능한 값은 다음과 같습니다.
                - 0 - Vertex에 의하여 일치
                -  1 - 얼굴별 경기
            '''
            ...

    class maxOps(interface):
        @staticmethod
        def getNodeByHandle(handle: int) -> runtime.node | None: ...

        @staticmethod
        def CollapseNodeTo(
            obj: runtime.GeometryClass,
            number: int,
            noWarning: bool
        ) -> runtime.node: ...

    class OkClass(Value):
        ...

    class StructDef(Value):
        ...
    class pluginPaths(StructDef):
        @staticmethod
        def count() -> int:
            ...
        @staticmethod
        def get(*args, **kwargs):
            ...
    class pathConfig(StructDef):
        xrefPaths: 'Any'  # systemGlobal
        @staticmethod
        def doesFileExist(*args, **kwargs) -> bool:
            ...
        @staticmethod
        def removePathLeaf(*args, **kwargs):
            ...
        @staticmethod
        def doSetProjectFolderSteps(*args, **kwargs):
            ...
        @staticmethod
        def SaveTo(*args, **kwargs):
            ...
        @staticmethod
        def isUncSharePath(*args, **kwargs):
            ...
        @staticmethod
        def getProjectSubDirectoryCount(*args, **kwargs):
            ...
        @staticmethod
        def resolvePathSymbols(*args, **kwargs):
            ...
        @staticmethod
        def doSetProjectFolderStepsUsingDirectory(*args, **kwargs):
            ...
        @staticmethod
        def isPathRootedAtBackslash(*args, **kwargs):
            ...
        @staticmethod
        def getProjectSubDirectory(*args, **kwargs):
            ...
        @staticmethod
        def normalizePath(*args, **kwargs):
            ...
        @staticmethod
        def isProjectFolder(*args, **kwargs) -> bool:
            ...
        mapPaths: 'Any'  # systemGlobal
        @staticmethod
        def isPathRootedAtDriveLetter(*args, **kwargs):
            ...
        @staticmethod
        def addProjectDirectoryCreateFilter(*args, **kwargs):
            ...
        @staticmethod
        def convertPathToLowerCase(*args, **kwargs):
            ...
        @staticmethod
        def getProjectFolderPath(*args, **kwargs):
            ...
        @staticmethod
        def pathsResolveEquivalent(*args, **kwargs):
            ...
        @staticmethod
        def removeProjectDirectoryCreateFilter(*args, **kwargs):
            ...
        @staticmethod
        def convertPathToRelativeTo(*args, **kwargs):
            ...
        @staticmethod
        def getCurrentProjectFolderPath(*args, **kwargs):
            ...
        pluginPaths: runtime.pluginPaths
        @staticmethod
        def load(*args, **kwargs):
            ...
        @staticmethod
        def appendPath(*args, **kwargs) -> str:
            ...
        @staticmethod
        def removeAllProjectDirectoryCreateFilters(*args, **kwargs):
            ...
        @staticmethod
        def convertPathToUnc(*args, **kwargs):
            ...
        @staticmethod
        def isAbsolutePath(*args, **kwargs):
            ...
        @staticmethod
        def SetDir(*args, **kwargs):
            ...
        @staticmethod
        def GetDir(*args, **kwargs):
            ...
        @staticmethod
        def stripPathToTopParent(*args, **kwargs):
            ...
        @staticmethod
        def getProjectDirectoryCreateFilters(*args, **kwargs):
            ...
        @staticmethod
        def convertPathToAbsolute(*args, **kwargs):
            ...
        @staticmethod
        def isLegalPath(*args, **kwargs):
            ...
        resolveUNC: 'Any'  # systemGlobal
        @staticmethod
        def merge(*args, **kwargs):
            ...
        @staticmethod
        def removePathTopParent(*args, **kwargs):
            ...
        @staticmethod
        def doProjectSetupSteps(*args, **kwargs):
            ...
        sessionPaths: 'Any'  # systemGlobal
        @staticmethod
        def isUsingProfileDirectories(*args, **kwargs):
            ...
        @staticmethod
        def isRootPath(*args, **kwargs):
            ...
        @staticmethod
        def getCurrentProjectFolder(*args, **kwargs):
            ...
        @staticmethod
        def stripPathToLeaf(*args, **kwargs):
            ...
        @staticmethod
        def doProjectSetupStepsUsingDirectory(*args, **kwargs):
            ...
        @staticmethod
        def isUsingRoamingProfiles(*args, **kwargs):
            ...
        @staticmethod
        def isUncPath(*args, **kwargs):
            ...
        @staticmethod
        def setCurrentProjectFolder(*args, **kwargs):
            ...
    class modPanel(StructDef):
        @staticmethod
        def addModToSelection(*args, **kwargs): ...
        @staticmethod
        def isPinStackEnabled(*args, **kwargs): ...
        @staticmethod
        def setPinStack(*args, **kwargs): ...
        @staticmethod
        def getPinStack(*args, **kwargs): ...
        @staticmethod
        def validModifier(*args, **kwargs) -> bool: ...
        @staticmethod
        def setCurrentObject(modifier: runtime.modifier) -> bool: ...
        @staticmethod
        def getCurrentObject() -> runtime.modifier: ...

        @staticmethod
        def getModifierIndex(
            obj: runtime.node, modifier: runtime.modifier
        ) -> int:
            '''
            최상단 상단 스택이 1로 부터 시작하는 위치숫자
            - 위치숫자1 == obj.modifiers[0]
            '''
            ...

    class refs(StructDef):
        @staticmethod
        def dependentNodes(*args, **kwargs) -> list: ...

    class skinOps(StructDef):
        '''
        - <https://help.autodesk.com/view/MAXDEV/2024/ENU/?guid=GUID-0820AA26-920F-434D-A6BC-E8B6B57F54AC>  # noqa: E501
        '''
        @staticmethod
        def GetBoneNode(skin, bone_index:int) -> runtime.GeometryClass: ...
        @staticmethod
        def GetNumberBones(skin) -> int: ...
        @staticmethod
        def GetListIDByBoneID(skin, bone_id: int) -> int: ...
        @staticmethod
        def GetBoneIDByListID(skin, list_id: int) -> int: ...
        @staticmethod
        def GetBoneNodes(skin) -> list: ...
        @staticmethod
        def GetBoneName(skin, bone_index: int, nameflag: Literal[0,1]) -> str:
            '''
            Args:
                - nameflag: Literal[0,1]
                    - 0: bone name
                    - 1: UI list name
            '''
            ...

        @overload
        @staticmethod
        def ReplaceVertexWeights(
            Skin: Any,
            vertex_integer: int,
            vertex_bone_integer: int,
            weight_float: float,
            node: runtime.node|None=None, name: str=""): ...

        @overload
        @staticmethod
        def ReplaceVertexWeights(
            Skin: Any,
            vertex_integer: int,
            vertex_bone_array: runtime.Array|list,
            weight_array: runtime.Array|list,
            node: runtime.node|None=None,
            name: str=""): ...

        @staticmethod
        def GetVertexWeight(
            skin,
            vertex_integer,
            vertex_bone_integer
        ) -> float:
            ...

        @staticmethod
        def GetVertexWeightBoneID(
            skin,
            vertex_integer,
            vertex_bone_intger
        ) -> int:
            '''
            skin 의 vertex_integer번째 정점의 vertex_bone_intger번째 본의 ID를 반환합니다.
            '''
            ...

        @staticmethod
        def GetVertexWeightCount(skin: runtime.modifier, vert_number: int)-> int: ...
        @staticmethod
        def AddBone(*args, **kwargs): ...
        @staticmethod
        def RemoveBone(*args, **kwargs):
            '''
            - `skinOps.removebone <Skin>`
            - `skinOps.removebone <Skin> <BoneID_integer> [(node:<node> | name:<string>)]`
            '''
            ...
    class windows:
        @staticmethod
        def getMAXHWND() -> int: ...
    class Name(runtime.Value):
        def __init__(self, string):
            ...
    class Primitive(runtime.Value):
        '''
        매소드임
        - https://help.autodesk.com/view/MAXDEV/2024/ENU/?guid=Max_Developer_Help_cpp_ref_class_primitive_html
        - https://help.autodesk.com/view/MAXDEV/2024/ENU/?guid=GUID-B28D7100-1F5F-4A0F-BFA3-17ABADD13580
            - Primitives클래스에 국한되지 않는 메서드입니다. 이 메서드는 인수의 타입(있는 경우)을 확인하고, 타입이 올바르지 않으면 오류를 발생시킵니다. Primitive의 정의는 하나뿐입니다.
        '''
        ...
    class Interface(runtime.Value): ...
    class menuMan(Interface):
        @staticmethod
        def getMainMenuBar(*args, **kwargs) -> runtime.menuMan: ...
        @staticmethod
        def addItem(*args, **kwargs) -> None: ...
        @staticmethod
        def removeItem(*args, **kwargs) -> None: ...
        @staticmethod
        def createActionItem(*args, **kwargs) -> None: ...
        @staticmethod
        def updateMenuBar(*args, **kwargs) -> None: ...
        @staticmethod
        def numMenus() -> int: ...
        @staticmethod
        def saveMenuFile(*args, **kwargs) -> None: ...
        @staticmethod
        def getMenuFile(*args, **kwargs) -> None: ...
        @staticmethod
        def findMenu(*args, **kwargs) -> None: ...
        @staticmethod
        def unRegisterMenu(*args, **kwargs) -> None: ...
        @staticmethod
        def createMenu(*args, **kwargs) -> runtime.menuMan: ...
        @staticmethod
        def createSubMenuItem(*args, **kwargs) -> runtime.menuMan: ...
        @staticmethod
        def addItem(*args, **kwargs) -> None: ...
        @staticmethod
        def numItems(*args, **kwargs) -> None: ...
        @staticmethod
        def registerMenuContext(contextId: int) -> bool: ...

    class macros(StructDef):

        @staticmethod
        def new(*args, **kwargs) -> None: ...

    @staticmethod
    def append(*args):
        ''' '''
        ...
    @staticmethod
    def completeRedraw() -> bool:
        ''' 화면 강재 갱신(씬 번경 업데이트시)'''
        ...
    @staticmethod
    def isValidObj(*args, **kwargs) -> bool:
        ''' 오브젝트 유효성 검사'''
        ...
    @staticmethod
    def rotateYPRMatrix(yaw: int|float, pitch: int|float, roll: int|float) -> runtime.Matrix3:
        '''
        parems:
        - yaw: int|float - y축
        - pitch: int|float - x축
        - roll: int|float - z축
        '''
        ...
    @staticmethod
    def preRotateX(matrix3: runtime.Matrix3, number: int|float) -> runtime.Matrix3: ...
    ''' maxtrix3는 참조값으로 업데이트됨, number는 회전값 '''
    @staticmethod
    def preRotateY(matrix3: runtime.Matrix3, number: int|float) -> runtime.Matrix3: ...
    ''' maxtrix3는 참조값으로 업데이트됨, number는 회전값 '''
    @staticmethod
    def preRotateZ(matrix3: runtime.Matrix3, number: int|float) -> runtime.Matrix3: ...
    ''' maxtrix3는 참조값으로 업데이트됨, number는 회전값 '''
    @staticmethod
    def delete(*args, **kwargs) -> Any: ...
    @staticmethod
    def isKindOf(*args, **kwargs) -> bool: ...
    @staticmethod
    def messageBox(*args, **kwargs) -> Any: ...
    @staticmethod
    def attachObjects(*args, **kwargs) -> Any: ...
    @staticmethod
    def quat(*args, **kwargs) -> Any: ...
    @staticmethod
    def getPropertyController(*args, **kwargs) -> Any: ...
    @staticmethod
    def hide(*args, **kwargs) -> Any: ...
    @staticmethod
    def setProperty(*args, **kwargs) -> Any: ...
    @staticmethod
    def getProperty(*args, **kwargs) -> Any: ...
    @staticmethod
    def getClassInstances(*args, **kwargs) -> type: ...
    @staticmethod
    def classof(*args, **kwargs) -> type: ...
    @staticmethod
    def cross(*args, **kwargs) -> None: ...
    @staticmethod
    def normalize(transform: Point3) -> Point3: ...
    @staticmethod
    def distance(a: Point3, b: Point3) -> float: ...
    @staticmethod
    def getCurrentSelection() -> Array: ...
    @staticmethod
    def isValidNode(obj: runtime.Value) -> bool: ...
    @staticmethod
    def GetNamedSelSetName(i: int) -> str:
        """ n번째 명명된 선택 세트의 이름을 반환합니다. """
        ...
    @staticmethod
    def GetNamedSelSetItem(i: int, n: int) -> mxs.Node:
        """ 특정 명명된 선택 세트에서 의 포인터를 검색합니다.INode """
        ...
    @staticmethod
    def GetNumNamedSelSets() -> int:
        """ 명명된 선택 세트의 수를 반환합니다. """
        ...
    @staticmethod
    def GetNamedSelSetItemCount(i: int) -> int:
        """ 명명된 선택 세트의 항목 수를 반환합니다. """
        ...
    @staticmethod
    def getNodeByName(name: str) -> mxs.Node: ...
    @staticmethod
    def setUserPropVal (obj, key_string, value_string, *args, **kwargs) -> None: ...
    @staticmethod
    def getUserPropVal(obj, key_string, *args, **kwargs) -> str: ...
    @staticmethod
    def ShellLaunch(*args, **kwargs) -> None: ...
    @staticmethod
    def saveMaxFile(*args, **kwargs) -> None: ...
    @staticmethod
    def getFiles(*args, **kwargs) -> list: ...
    @staticmethod
    def getFilenameType(*args, **kwargs) -> str: ...
    @staticmethod
    def getFilenameFile(*args, **kwargs) -> str: ...
    @staticmethod
    def filenameFromPath(*args, **kwargs) -> str: ...
    @staticmethod
    def getFilenamePath(*args, **kwargs) -> str: ...
    @staticmethod
    def GetDir(*args, **kwargs) -> str: ...
    @staticmethod
    def resetMaxFile(noPrompt: runtime.Name) -> None: ...
    @staticmethod
    def clearListener() -> None: ...


    class Object(Value):...
    class MAXWrapper(Value):...
    class MAXObject(Value):...
    class Time(Value, int, float):
        def __init__(self, *args, **kwargs) -> None: ...
    class rotationController(MAXWrapper): ...
    class Euler_XYZ(rotationController): ...
    class tcb_rotation(rotationController): ...
    class positionController(MAXWrapper): ...
    class Position_XYZ(MAXWrapper): ...
    class Matrix3Controller(MAXWrapper): ...
    class prs(Matrix3Controller): ...
    class transform_script(Matrix3Controller):
        class Type(enum.Enum):
            unknown = runtime.Name("unknown")
            target = runtime.Name("target")
            constant = runtime.Name("constant")
            object = runtime.Name("object")
            node = runtime.Name("node")
        ThrowOnError: bool
        def __init__(self, *args, **kwargs) -> None: ...
        def AddConstant(self, *args, **kwargs) -> bool: ...
        def SetConstant(self, which: str|int, *args, **kwargs) -> bool: ...
        def GetConstant(self, which: str|int, *args, **kwargs) -> Any: ...
        def AddTarget(
                self,
                value_name:str,
                target: runtime.node,
                Offset:int|float = runtime.Time(0),
                Owner:Any=None) -> bool: ...
        def SetTarget(self, which: str|int, target:runtime.Value, Owner:runtime.Value|None=None) -> bool: ...
        def GetTarget(self, which: str|int, asObject:bool=False) -> runtime.Value: ...
        # ObjectVariable
        def AddObject(self, *args, **kwargs) -> bool: ...
        def SetObject(self, which: str|int, object:runtime.Object) -> bool: ...
        def GetObject(self, which: str|int) -> runtime.MAXObject: ...
        def AddNode(self, name:str, node: runtime.node) -> bool: ...
        def SetNode(self, which: str|int, node: runtime.node) -> bool: ...
        def GetNode(self, which: str|int) -> runtime.node: ...
        def DeleteVariable(self, which: str|int) -> bool: ...
        # General Variable Access
        def NumVariables(self) -> int: ...
        def VariableExists(self, *args, **kwargs) -> bool: ...
        def GetType(self, *args, **kwargs) -> runtime.transform_script.Type: ...
        def GetName(self, *args, **kwargs) -> str: ...
        def RenameVariable(self, *args, **kwargs) -> bool: ...
        def GetIndex(self, name:str) -> int: ...
        def GetValue(self, *args, asObject:bool=False, **kwargs) -> runtime.Value: ...
        def GetVarValue(self, *args, **kwargs) -> runtime.Value: ...
        # Variable Time Offset
        def SetOffset(self, which: str|int, offset:runtime.Time, *args, **kwargs) -> bool: ...
        def GetOffset(self, which: str|int, *args, **kwargs) -> runtime.Time: ...
        ...
        def SetExpression(self, expression:str) -> bool: ...

    class Vertical_Horizontal_Turn(MAXWrapper): ...
    class node(runtime.MAXWrapper):
        """[Node : MAXWrapper](https://help.autodesk.com/view/MAXDEV/2023/ENU/?guid=GUID-1C9953AA-4750-4147-91DC-127AF2F7BC87)
        [Interface : INode](https://help.autodesk.com/view/MAXDEV/2023/ENU/?guid=GUID-0BFEF796-5952-48B0-8929-88475F927649)
        """

        name: str
        transform: runtime.Matrix3
        handle: int
        baseObject: runtime.node
        '''
        - [`<node>`.baseObject  A subclass of Node  default: varies](https://help.autodesk.com/view/MAXDEV/2024/ENU/?guid=GUID-00AB0CFA-3190-4A28-A185-4774B684F6D8)
        - The baseObject속성은 수정자 스택의 기본 개체에 대한 액세스를 제공합니다. 왜냐하면 classOf()장면 노드 객체의 함수는 세계 상태 객체(스택의 상단)의 클래스를 반환합니다. baseObject노드를 만드는 데 사용되는 원래 개체의 클래스를 결정하는 속성. 
        '''
        material: runtime.Material|None
        parent: runtime.node|None
        children: runtime.Array
        mesh: runtime.TriMesh
        boundingBox: runtime.Box3
        displayByLayer: bool
        motionByLayer: bool
        renderByLayer: bool
        colorByLayer: bool
        globalIlluminationByLayer: bool
        isTarget: bool
        lookAt: runtime.node|None
        target: runtime.node|None
        targetDistance: float
        isHidden: bool
        isNodeHidden: bool
        isHiddenInVpt: bool
        isFrozen: bool
        isNodeFrozen: bool
        isSelected: bool
        xray: bool
        boxMode: bool
        allEdges: bool
        vertexTicks: bool
        """ 노드의 모든 정점을 뷰포트에 눈금으로 표시할지 여부를 가져오거나 설정합니다. """
        backFaceCull: bool
        showTrajectory: bool
        ignoreExtents: bool
        showFrozenInGray: bool
        wireColor: runtime.Color
        """  """
        showLinks: bool
        showLinksOnly: bool
        showVertexColors: bool
        vertexColorType: runtime.Name
        vertexColorsShaded: bool
        isDependent: bool
        visibility: bool
        controller: runtime.Matrix3Controller
        renderable: bool
        inheritVisibility: bool
        primaryVisibility: bool
        secondaryVisibility: bool
        receiveShadows: bool
        castShadows: bool
        applyAtmospherics: bool
        renderOccluded: bool
        gbufferChannels: bool
        imageMotionBlurMultiplier: float
        motionBlurOn: bool
        motionBlurOnController: runtime.floatController
        motionBlur: runtime.Name
        ''' default: #none
        - #none
        - #object
        - #image
        '''
        generatecaustics: bool
        rcvcaustics: bool
        generateGlobalIllume: bool
        rcvGlobalIllum: bool
        ...

    class GeometryClass(node):
        name: str
        transform: runtime.Matrix3
        mesh: runtime.TriMesh
        numfaces: int
        wireColor: runtime.Color
        modifiers: dict[runtime.Name|int, runtime.modifier]|list[runtime.modifier]
        ...
    class Dummy(GeometryClass): ...
    class Point(GeometryClass): ...
    class Biped_Object(GeometryClass): ...

    class logsystem(StructDef):
        logDays: int
        logSize: int
        quietMode: bool
        enabled: bool
        longevity: runtime.Name
        ''' #days'''
        @staticmethod
        def loadState(*args, **kwargs) -> None: ...
        @staticmethod
        def getLogName(*args, **kwargs) -> str: ...
        @staticmethod
        def setLogLevel(*args, **kwargs) -> None: ...
        @staticmethod
        def getLogLevel(*args, **kwargs) -> None: ...
        @staticmethod
        def getNetLogFileName() -> str: ...
        @staticmethod
        def logEntry(*args, **kwargs) -> None: ...
        @staticmethod
        def logName(*args, **kwargs) -> None: ...
        @staticmethod
        def saveState(*args, **kwargs) -> None: ...

    class helper(node): ...

    class Bone(helper):
        length: int
        fronfin: bool
        frontfinsize: int
        sidefins: bool
        sidefinssize: int
        boneEnable: bool
        boneFreeaeLength: bool
        boneAutoAlign: bool
        boneScaleType: runtime.Name
        def __init__(self, *args, **kwargs) -> None:
            '''
            Args:
                - boneScaleType: runtime.Name('none')
            '''
            ...
        
    class vertexColorType(mxs.Name):
        color: Type[mxs.Name]
        illum: Type[mxs.Name]
        alpha: Type[mxs.Name]
        color_plus_illum: Type[mxs.Name]
        ...
    class NodeGeneric(Value): ...
    class setFaceSelection(NodeGeneric):
        def __new__(cls, *args, **kwargs) -> None: ...
    class getFaceSelection(NodeGeneric):
        def __new__(cls, *args, **kwargs) -> runtime.BitArray: ...
    class MAXWrapper(runtime.Value):
        '''
        https://help.autodesk.com/view/MAXDEV/2024/ENU/?guid=GUID-025B6C97-8601-4FEF-ACB8-E47EE0929300
        '''
        category: runtime.Name
        categories: runtime.Array
        classes: runtime.Array
        classID: runtime.Array
        creatabl: bool
        localizedName: str
        ''' 읽기 전용'''
        nonLocalizedNam: str
        ''' 읽기 전용'''
        dllName: str
        ''' 읽기 전용'''
        dllIsLoaded: bool
        ''' 2012이상 - 읽기 전용'''
        isMSPluginClass: bool
        ''' 2012이상 - 읽기 전용'''
        ...
    class FaceSelection(Value): ...
    class node(runtime.MAXWrapper):
        """[Node : MAXWrapper](https://help.autodesk.com/view/MAXDEV/2023/ENU/?guid=GUID-1C9953AA-4750-4147-91DC-127AF2F7BC87)
        [Interface : INode](https://help.autodesk.com/view/MAXDEV/2023/ENU/?guid=GUID-0BFEF796-5952-48B0-8929-88475F927649)
        """

        name: str
        transform: runtime.Matrix3
        handle: int
        baseObject: runtime.node
        '''
        - [`<node>`.baseObject  A subclass of Node  default: varies](https://help.autodesk.com/view/MAXDEV/2024/ENU/?guid=GUID-00AB0CFA-3190-4A28-A185-4774B684F6D8)
        - The baseObject속성은 수정자 스택의 기본 개체에 대한 액세스를 제공합니다. 왜냐하면 classOf()장면 노드 객체의 함수는 세계 상태 객체(스택의 상단)의 클래스를 반환합니다. baseObject노드를 만드는 데 사용되는 원래 개체의 클래스를 결정하는 속성. 
        '''
        material: runtime.Material|None
        parent: runtime.node|None
        children: runtime.Array
        mesh: runtime.TriMesh
        boundingBox: runtime.Box3
        displayByLayer: bool
        motionByLayer: bool
        renderByLayer: bool
        colorByLayer: bool
        globalIlluminationByLayer: bool
        isTarget: bool
        lookAt: runtime.node|None
        target: runtime.node|None
        targetDistance: float
        isHidden: bool
        isNodeHidden: bool
        isHiddenInVpt: bool
        isFrozen: bool
        isNodeFrozen: bool
        isSelected: bool
        xray: bool
        boxMode: bool
        allEdges: bool
        vertexTicks: bool
        """ 노드의 모든 정점을 뷰포트에 눈금으로 표시할지 여부를 가져오거나 설정합니다. """
        backFaceCull: bool
        showTrajectory: bool
        ignoreExtents: bool
        showFrozenInGray: bool
        wireColor: runtime.Color
        """  """
        showLinks: bool
        showLinksOnly: bool
        showVertexColors: bool
        vertexColorType: runtime.Name
        vertexColorsShaded: bool
        isDependent: bool
        visibility: bool
        controller: runtime.Matrix3Controller
        renderable: bool
        inheritVisibility: bool
        primaryVisibility: bool
        secondaryVisibility: bool
        receiveShadows: bool
        castShadows: bool
        applyAtmospherics: bool
        renderOccluded: bool
        gbufferChannels: bool
        imageMotionBlurMultiplier: float
        motionBlurOn: bool
        motionBlurOnController: runtime.floatController
        motionBlur: runtime.Name
        ''' default: #none
        - #none
        - #object
        - #image
        '''
        generatecaustics: bool
        rcvcaustics: bool
        generateGlobalIllume: bool
        rcvGlobalIllum: bool
        ...

    class floatController(MAXWrapper):...
    class Editable_mesh(GeometryClass):...
    class Editable_Poly(GeometryClass):...
    class PolyMeshObject(GeometryClass):...

    class biped(runtime.StructDef):
        @staticmethod
        def createXtraOpposite(*args, **kwargs): ...
        @staticmethod
        def numTwistPoses(*args, **kwargs): ...
        @staticmethod
        def getParentNodePos(*args, **kwargs): ...
        @staticmethod
        def getIKActive(*args, **kwargs): ...
        @staticmethod
        def setCopyName(*args, **kwargs): ...
        @staticmethod
        def getClipAtTime(*args, **kwargs): ...
        @staticmethod
        def numLayers(*args, **kwargs): ...
        @staticmethod
        def saveTalentPoseFile(*args, **kwargs): ...
        @staticmethod
        def saveBipFileDlg(*args, **kwargs): ...
        @staticmethod
        def getTwistPoseTwist(*args, **kwargs): ...
        @staticmethod
        def clearAllAnimation(*args, **kwargs): ...
        @staticmethod
        def scaleFootprints(*args, **kwargs): ...
        @staticmethod
        def copyBipPose(*args, **kwargs): ...
        @staticmethod
        def collapsePosSubAnims(*args, **kwargs): ...
        @staticmethod
        def clearPrefClips(*args, **kwargs): ...
        @staticmethod
        def setCurrentLayer(*args, **kwargs): ...
        @staticmethod
        def getTwistStartId(*args, **kwargs): ...
        @staticmethod
        def saveStpFile(*args, **kwargs): ...
        @staticmethod
        def addNewKey(*args, **kwargs): ...
        @staticmethod
        def getXtraOpposite(*args, **kwargs): ...
        @staticmethod
        def createTwistPose(*args, **kwargs): ...
        @staticmethod
        def getClavicleVals(*args, **kwargs): ...
        @staticmethod
        def setKey(*args, **kwargs): ...
        @staticmethod
        def loadCopyPasteFile(*args, **kwargs): ...
        @staticmethod
        def createPosSubAnims(*args, **kwargs): ...
        @staticmethod
        def createLayer(*args, **kwargs): ...
        @staticmethod
        def multipleFSDlg(*args, **kwargs): ...
        @staticmethod
        def loadBipFile(*args, **kwargs): ...
        @staticmethod
        def getTwistPoseBias(*args, **kwargs): ...
        @staticmethod
        def clearSelectedAnimation(*args, **kwargs): ...
        @staticmethod
        def convertFromBuffer(*args, **kwargs): ...
        @staticmethod
        def copyBipTrack(*args, **kwargs): ...
        @staticmethod
        def collapseRotSubAnims(*args, **kwargs): ...
        @staticmethod
        def addPrefClip(*args, **kwargs): ...
        @staticmethod
        def getLimbRetargetState(*args, **kwargs): ...
        @staticmethod
        def maxTwistNodes(*args, **kwargs): ...
        @staticmethod
        def saveBipedAnimationLayer(*args, **kwargs): ...
        @staticmethod
        def createNew(*args, **kwargs): ...
        @staticmethod
        def deleteXtra(*args, **kwargs): ...
        @staticmethod
        def setTwistPose(*args, **kwargs): ...
        @staticmethod
        def getHingeVal(*args, **kwargs): ...
        @staticmethod
        def setSelectedKey(*args, **kwargs): ...
        @staticmethod
        def saveCopyPasteFile(*args, **kwargs): ...
        @staticmethod
        def createRotSubAnims(*args, **kwargs): ...
        @staticmethod
        def deleteLayer(*args, **kwargs): ...
        @staticmethod
        def addFootprint(*args, **kwargs): ...
        @staticmethod
        def loadStpFile(*args, **kwargs): ...
        @staticmethod
        def getXtraName(*args, **kwargs): ...
        @staticmethod
        def getEulerActive(*args, **kwargs): ...
        @staticmethod
        def mirror(*args, **kwargs): ...
        @staticmethod
        def pasteFromBuffer(*args, **kwargs): ...
        @staticmethod
        def pasteBipPosture(*args, **kwargs): ...
        @staticmethod
        def copyPosture(*args, **kwargs): ...
        @staticmethod
        def deletePrefClip(*args, **kwargs): ...
        @staticmethod
        def setTransform(
            obj: runtime.Biped_Object,
            target: runtime.Name,
            value: runtime.Point3|runtime.Quat,
            set_key: bool,
            limb: runtime.Biped_Object|None = None,
        ): ...
        @staticmethod
        def getTransform(
            obj: runtime.Biped_Object,
            target: runtime.Name,
            limb: runtime.Biped_Object|None = None,
        ): ...
        @staticmethod
        def setLimbRetargetState(*args, **kwargs): ...
        @staticmethod
        def maxTwistLinks(*args, **kwargs): ...
        @staticmethod
        def saveBipedBaseAnimationLayer(*args, **kwargs): ...
        @staticmethod
        def deleteKeys(*args, **kwargs): ...
        @staticmethod
        def attachXtra(*args, **kwargs): ...
        @staticmethod
        def deleteTwistPose(*args, **kwargs): ...
        @staticmethod
        def getHorseAnkleVal(*args, **kwargs): ...
        @staticmethod
        def setPlantedKey(*args, **kwargs): ...
        @staticmethod
        def numCopyCollections(*args, **kwargs): ...
        @staticmethod
        def createScaleSubAnims(*args, **kwargs): ...
        @staticmethod
        def collapseAtLayer(*args, **kwargs): ...
        @staticmethod
        def addMultipleFootprints(*args, **kwargs): ...
        @staticmethod
        def loadFigFile(*args, **kwargs): ...
        @staticmethod
        def getEulerOrder(*args, **kwargs): ...
        @staticmethod
        def mirrorInPlace(*args, **kwargs): ...
        @staticmethod
        def getCurrentRange(*args, **kwargs): ...
        @staticmethod
        def pasteBipPose(*args, **kwargs): ...
        @staticmethod
        def pastePosture(*args, **kwargs): ...
        @staticmethod
        def isPrefClip(*args, **kwargs): ...
        @staticmethod
        def getRetargetRefBip(*args, **kwargs): ...
        @staticmethod
        def setMultipleKeys(*args, **kwargs): ...
        @staticmethod
        def loadBipedAnimationLayer(*args, **kwargs): ...
        @staticmethod
        def selectKeys(*args, **kwargs): ...
        @staticmethod
        def setXtraName(*args, **kwargs): ...
        @staticmethod
        def setDefaultTwistPoses(*args, **kwargs): ...
        @staticmethod
        def getPelvisVal(*args, **kwargs): ...
        @staticmethod
        def setSlidingKey(*args, **kwargs): ...
        @staticmethod
        def getCopyCollection(*args, **kwargs): ...
        @staticmethod
        def setPosSubAnim(*args, **kwargs): ...
        @staticmethod
        def getLayerActive(*args, **kwargs): ...
        @staticmethod
        def getMultipleFSParams(*args, **kwargs): ...
        @staticmethod
        def loadFigNoTwists(*args, **kwargs): ...
        @staticmethod
        def setEulerActive(*args, **kwargs): ...
        @staticmethod
        def setSnapKey(*args, **kwargs): ...
        @staticmethod
        def getIdLink(*args, **kwargs): ...
        @staticmethod
        def pasteBipTrack(*args, **kwargs): ...
        @staticmethod
        def deleteAllCopies(*args, **kwargs): ...
        @staticmethod
        def getCurrentClip(*args, **kwargs): ...
        @staticmethod
        def setRetargetRefBip(*args, **kwargs): ...
        @staticmethod
        def doSetMultipleKeysDlg(*args, **kwargs): ...
        @staticmethod
        def loadBipedBaseAnimationLayer(*args, **kwargs): ...
        @staticmethod
        def deselectKeys(*args, **kwargs): ...
        @staticmethod
        def setTwistPoseName(*args, **kwargs): ...
        @staticmethod
        def getFingerVal(*args, **kwargs): ...
        @staticmethod
        def setFreeKey(*args, **kwargs): ...
        @staticmethod
        def createCopyCollection(*args, **kwargs): ...
        @staticmethod
        def setRotSubAnim(*args, **kwargs): ...
        @staticmethod
        def setLayerActive(*args, **kwargs): ...
        @staticmethod
        def newFootprintKeys(*args, **kwargs): ...
        @staticmethod
        def loadFigJustTwists(*args, **kwargs): ...
        @staticmethod
        def setQuaternionActive(*args, **kwargs): ...
        @staticmethod
        def zeroTwist(*args, **kwargs): ...
        @staticmethod
        def getRotParentNode(*args, **kwargs): ...
        @staticmethod
        def pastePostureToXtras(*args, **kwargs): ...
        @staticmethod
        def numCopies(*args, **kwargs): ...
        @staticmethod
        def numPrefClips(*args, **kwargs): ...
        @staticmethod
        def RetargetToBaseLayer(*args, **kwargs): ...
        @staticmethod
        def convertToFreeForm(*args, **kwargs): ...
        @staticmethod
        def loadMocapFile(*args, **kwargs): ...
        @staticmethod
        def moveKeys(*args, **kwargs): ...
        @staticmethod
        def setTwistPoseTwist(*args, **kwargs): ...
        @staticmethod
        def getHorizontalControl(*args, **kwargs): ...
        @staticmethod
        def resetAllLimbKeys(*args, **kwargs): ...
        @staticmethod
        def deleteCopyCollection(*args, **kwargs): ...
        @staticmethod
        def setScaleSubAnim(*args, **kwargs): ...
        @staticmethod
        def getLayerName(*args, **kwargs): ...
        @staticmethod
        def getNode(*args, **kwargs): ...
        @staticmethod
        def saveBipFileSegment(*args, **kwargs): ...
        @staticmethod
        def fsAddSide(*args, **kwargs): ...
        @staticmethod
        def setEulerOrder(*args, **kwargs): ...
        @staticmethod
        def zeroAll(*args, **kwargs): ...
        @staticmethod
        def getPosParentNode(*args, **kwargs): ...
        @staticmethod
        def pasteTrackToXtras(*args, **kwargs): ...
        @staticmethod
        def deleteCopy(*args, **kwargs): ...
        @staticmethod
        def getPrefClip(*args, **kwargs): ...
        @staticmethod
        def RetargetToReferenceBiped(*args, **kwargs): ...
        @staticmethod
        def convertToFootSteps(*args, **kwargs): ...
        @staticmethod
        def adjustTalentPose(*args, **kwargs): ...
        @staticmethod
        def displayPrefsDlg(*args, **kwargs): ...
        @staticmethod
        def setTwistPoseBias(*args, **kwargs): ...
        @staticmethod
        def getVerticalControl(*args, **kwargs): ...
        @staticmethod
        def collapseMoveAllMode(*args, **kwargs): ...
        @staticmethod
        def deleteAllCopyCollections(*args, **kwargs): ...
        @staticmethod
        def collapseAllPosSubAnims(*args, **kwargs): ...
        @staticmethod
        def setLayerName(*args, **kwargs): ...
        @staticmethod
        def maxNumNodes(*args, **kwargs): ...
        @staticmethod
        def saveBipFile(*args, **kwargs): ...
        @staticmethod
        def createXtra(*args, **kwargs): ...
        @staticmethod
        def smoothTwist(*args, **kwargs): ...
        @staticmethod
        def getParentNodeRot(*args, **kwargs): ...
        @staticmethod
        def setCurrentCopyCollection(*args, **kwargs): ...
        @staticmethod
        def getCopyName(*args, **kwargs): ...
        @staticmethod
        def getPrefClipProb(*args, **kwargs): ...
        @staticmethod
        def unifyMotion(*args, **kwargs): ...
        @staticmethod
        def saveTalentFigFile(*args, **kwargs): ...
        @staticmethod
        def loadBipFileDlg(*args, **kwargs): ...
        @staticmethod
        def getTwistPoseName(*args, **kwargs): ...
        @staticmethod
        def getTurnControl(*args, **kwargs): ...
        @staticmethod
        def bendFootprints(*args, **kwargs): ...
        @staticmethod
        def copyBipPosture(*args, **kwargs): ...
        @staticmethod
        def collapseAllRotSubAnims(*args, **kwargs): ...
        @staticmethod
        def getCurrentLayer(*args, **kwargs): ...
        @staticmethod
        def maxNumLinks(*args, **kwargs): ...
        @staticmethod
        def saveFigFile(*args, **kwargs): ...
        @staticmethod
        def getKey(*args, **kwargs): ...
        ...

    class Sphere(runtime.GeometryClass):
        radius: float
        ...

    class TriMesh(Value):
        def selectedFaces(self) -> runtime.FaceSelection: ...
        ...

    class Box3: ...
    class Material: ...
    class setPropertyController(Primitive):
        def __new__(cls, contrller, target_name:str, new_controller) -> None: ...
    class SetCommandPanelTaskMode(Primitive):
        def __new__(cls, name: runtime.Name) -> None:
            """ name
            - create
            - modify
            - hierarchy 
            - motion 
            - display 
            - utility 
            """
            ...
        ...
    class Point3(Point3):
        """[<expr>, <expr>, <expr>]

        [2022 api link](https://help.autodesk.com/view/MAXDEV/2022/ENU/?guid=GUID-1564BD35-50EA-4140-9150-1AECC89F713C)
        """
        x: int
        y: int
        z: int
        def __init__(self, *args, **kwargs) -> None: ...
        ...

    class Color(mxs.Color):
        def __init__(self, *args, **kwargs) -> None: ...

    class Biped(mxs.Biped): ...

    class LayerManager(mxs.LayerManager):
        @staticmethod
        def getLayerFromName(*args, **kwargs): ...
        ...
    class Generic(Value): ...

    class getnumtverts(Generic):
        """-> int"""

        def __new__(cls, node) -> int: ...

    subObjectLevel: int

    class convertToMesh(NodeGeneric):
        def __new__(cls, node) -> None: ...

    class Skin(runtime.modifier):
        always_deform: bool
        enabledInViews: bool
        enable: bool

    class meshop(StructDef):
        @staticmethod
        def getNumVerts(*args, **kwargs) -> int:
            """ 버텍스"""
            ...
        @staticmethod
        def getNumMapFaces(*args, **kwargs) -> int:
            """getNumMapFaces <Mesh mesh> <Integer mapChannel>
            -> integer"""
            ...
        @staticmethod
        def getMapSupport(*args, **kwargs) -> bool:
            """getMapSupport <Mesh mesh> <Integer mapChannel>"""
            ...

        @staticmethod
        def setMapSupport(*args, **kwargs) -> bool:
            """setMapSupport <Mesh mesh> <Integer mapChannel> <Boolean support>"""
            ...

        @staticmethod
        def setNumMaps(*args, **kwargs) -> None:
            """meshop.setNumMaps <Mesh mesh> <int count> keep:<bool1ean=false>"""
            ...

        @staticmethod
        def getNumMaps(Any) -> int:
            """-> int(카운트를 반환)
            setNumMaps <Mesh mesh> <int count> keep:<bool1ean=false>"""
            ...

        @staticmethod
        def setNumMapVerts(*args, **kwargs) -> None:
            """setNumMapVerts <Mesh mesh> <Integer mapChannel> <Integer count> keep:<boolean=FALSE>"""
            ...

        @staticmethod
        def getMapVertsUsingMapFace(*args, **kwargs) -> runtime.BitArray:
            """meshop.getMapVertsUsingMapFace <Mesh mesh> <int mapChannel> <mapFacelist>"""
            ...

        @staticmethod
        def getFaceCenter(*args, **kwargs) -> runtime.Point3:
            """<point3>meshop.getFaceCenter <Mesh mesh> <int faceIndex> node:<node=unsupplied>"""
            ...
    class getNumFaces(Generic):
        def __new__(cls, node) -> int: ...
    class polyop(StructDef):
        """
        getNumVDataChannels:<fn>; Public,
        getNumMaps:<fn>; Public,
        weldEdgesByThreshold:<fn>; Public,
        createPolygon:<fn>; Public,
        createVert:<fn>; Public,
        collapseDeadStructs:<fn>; Public,
        getVertsByMatId:<fn>; Public,
        setFaceFlags:<fn>; Public,
        setFaceSelection:<fn>; Public,
        setEDataChannelSupport:<fn>; Public,
        setMapFace:<fn>; Public,
        capHolesByEdge:<fn>; Public,
        cutFace:<fn>; Public,
        makeVertsPlanar:<fn>; Public,
        inSlicePlaneMode:<fn>; Public,
        getFacesEdges:<fn>; Public,
        getFacesUsingVert:<fn>; Public,
        getVertsByFlag:<fn>; Public,
        setVDataChannelSupport:<fn>; Public,
        setMapSupport:<fn>; Public,
        weldEdges:<fn>; Public,
        unHideAllFaces:<fn>; Public,
        unHideAllVerts:<fn>; Public,
        attach:<fn>; Public,
        getBorderFromEdge:<fn>; Public,
        getDeadVerts:<fn>; Public,
        getNumVerts:<fn>; Public,
        getEDataChannelSupport:<fn>; Public,
        getMapFace:<fn>; Public,
        makeEdgesPlanar:<fn>; Public,
        capHolesByFace:<fn>; Public,
        moveVertsToPlane:<fn>; Public,
        getVert:<fn>; Public,
        getFaceDeg:<fn>; Public,
        getVertsUsingEdge:<fn>; Public,
        getVertFlags:<fn>; Public,
        getVDataChannelSupport:<fn>; Public,
        getMapSupport:<fn>; Public,
        divideEdge:<fn>; Public,
        setFaceSmoothGroup:<fn>; Public,
        autosmooth:<fn>; Public,
        breakVerts:<fn>; Public,
        deleteIsoVerts:<fn>; Public,
        getEdgeVerts:<fn>; Public,
        getDeadEdges:<fn>; Public,
        getNumEdges:<fn>; Public,
        getEDataValue:<fn>; Public,
        defaultMapFaces:<fn>; Public,
        moveEdgesToPlane:<fn>; Public,
        makeFacesPlanar:<fn>; Public,
        chamferVerts:<fn>; Public,
        getVerts:<fn>; Public,
        getFaceCenter:<fn>; Public,
        getFacesUsingEdge:<fn>; Public,
        setVertFlags:<fn>; Public,
        getVDataValue:<fn>; Public,
        setNumMapVerts:<fn>; Public,
        collapseEdges:<fn>; Public,
        getFaceSmoothGroup:<fn>; Public,
        collapseVerts:<fn>; Public,
        forceSubdivision:<fn>; Public,
        getEdgeFaces:<fn>; Public,
        getDeadFaces:<fn>; Public,
        getNumFaces:<fn>; Public,
        setEDataValue:<fn>; Public,
        applyUVWMap:<fn>; Public,
        createShape:<fn>; Public,
        moveFacesToPlane:<fn>; Public,
        getFaceMatID:<fn>; Public,
        setVert:<fn>; Public,
        getSafeFaceCenter:<fn>; Public,
        getVertsUsingFace:<fn>; Public,
        getEdgesByFlag:<fn>; Public,
        getVertSelection:<fn>; Public,
        checkTriangulation:<fn>; Public,
        setVDataValue:<fn>; Public,
        getNumMapVerts:<fn>; Public,
        splitEdges:<fn>; Public,
        divideFace:<fn>; Public,
        meshSmoothByVert:<fn>; Public,
        propagateFlags:<fn>; Public,
        getEdgesVerts:<fn>; Public,
        getHasDeadStructs:<fn>; Public,
        getHiddenVerts:<fn>; Public,
        freeEData:<fn>; Public,
        getVertsByColor:<fn>; Public,
        getEdgeVis:<fn>; Public,
        extrudeFaces:<fn>; Public,
        getFacesMatID:<fn>; Public,
        moveVert:<fn>; Public,
        getFaceNormal:<fn>; Public,
        getEdgesUsingFace:<fn>; Public,
        getEdgeFlags:<fn>; Public,
        setVertSelection:<fn>; Public,
        freeVData:<fn>; Public,
        setNumMapFaces:<fn>; Public,
        meshSmoothByEdge:<fn>; Public,
        slice:<fn>; Public,
        collapseFaces:<fn>; Public,
        tessellateByVert:<fn>; Public,
        fillInMesh:<fn>; Public,
        getEdgesFaces:<fn>; Public,
        isFaceDead:<fn>; Public,
        setHiddenVerts:<fn>; Public,
        resetEData:<fn>; Public,
        setFaceColor:<fn>; Public,
        setEdgeVis:<fn>; Public,
        bevelFaces:<fn>; Public,
        setFaceMatID:<fn>; Public,
        deleteVerts:<fn>; Public,
        getFaceArea:<fn>; Public,
        getElementsUsingFace:<fn>; Public,
        setEdgeFlags:<fn>; Public,
        getEdgeSelection:<fn>; Public,
        resetVData:<fn>; Public,
        getNumMapFaces:<fn>; Public,
        tessellateByEdge:<fn>; Public,
        meshSmoothByFace:<fn>; Public,
        detachVerts:<fn>; Public,
        resetSlicePlane:<fn>; Public,
        getFaceVerts:<fn>; Public,
        isEdgeDead:<fn>; Public,
        getHiddenFaces:<fn>; Public,
        setVertColor:<fn>; Public,
        chamferEdges:<fn>; Public,
        deleteEdges:<fn>; Public,
        retriangulate:<fn>; Public,
        deleteFaces:<fn>; Public,
        weldVertsByThreshold:<fn>; Public,
        getFacesByMatId:<fn>; Public,
        getVertsUsedOnlyByFaces:<fn>; Public,
        getFacesByFlag:<fn>; Public,
        setEdgeSelection:<fn>; Public,
        setNumEDataChannels:<fn>; Public,
        setMapVert:<fn>; Public,
        detachEdges:<fn>; Public,
        tessellateByFace:<fn>; Public,
        cutVert:<fn>; Public,
        getSlicePlane:<fn>; Public,
        getFaceEdges:<fn>; Public,
        isVertDead:<fn>; Public,
        setHiddenFaces:<fn>; Public,
        setNumVDataChannels:<fn>; Public,
        setNumMaps:<fn>; Public,
        createEdge:<fn>; Public,
        setDiagonal:<fn>; Public,
        flipNormals:<fn>; Public,
        weldVerts:<fn>; Public,
        getAllFaces:<fn>; Public,
        isMeshFilledIn:<fn>; Public,
        getFaceFlags:<fn>; Public,
        getFaceSelection:<fn>; Public,
        getNumEDataChannels:<fn>; Public,
        getMapVert:<fn>; Public,
        cutEdge:<fn>; Public,
        detachFaces:<fn>; Public,
        capHolesByVert:<fn>; Public,
        setSlicePlane:<fn>; Public,
        getFacesVerts:<fn>; Public,
        getEdgesUsingVert:<fn>; Public,
        getOpenEdges:<fn>; Public)
        """
        @staticmethod
        def getFaceCenter(*args, **kwargs) -> runtime.Point3:
            """<point3>polyop.getFaceCenter <Mesh mesh> <int faceIndex> node:<node=unsupplied>"""
            ...

        @staticmethod
        def getFaceVerts(*args, **kwargs) -> runtime.BitArray:
            """<bitArray>polyop.getFaceVerts <Mesh mesh> <int faceIndex>"""
            ...

        @staticmethod
        def setFaceSelection(*args, **kwargs) -> None: ...
        @staticmethod
        def getFacesUsingMapFace(*args, **kwargs) -> runtime.BitArray: ...


    class BoneSys(runtime.Interface):
        @staticmethod
        def createBone(startPos:runtime.Point3,
                       endPos: runtime.Point3,
                       zAxis: runtime.Point3) -> runtime.Bone: ...
    class controller: ...
    class Quat: ...

    class Matrix3(Value):
        """
        [2022 api link](https://help.autodesk.com/view/MAXDEV/2022/ENU/?guid=GUID-D77C780A-4E8A-4528-949F-CC09AAE048DA)
        """
        rotation: runtime.Quat
        """ 회전값 """
        position: runtime.Point3
        row1: runtime.Point3
        row2: runtime.Point3
        row3: runtime.Point3
        row4: runtime.Point3
        translation: runtime.Point3
        @overload
        def __init__(self, flag: Literal[0, 1]) -> None: ...

        @overload
        def __init__(self,
                     row1:runtime.Point3,
                     row2:runtime.Point3,
                     row3:runtime.Point3,
                     row4:runtime.Point3,
                     ) -> None: ...
        ...
        def __mul__(self, other: runtime.Matrix3) -> runtime.Matrix3: ...
        def __rmul__(self, other: runtime.Matrix3) -> runtime.Matrix3: ...

    class modifier(MAXWrapper):
        """ """
        name: str
        """ 모디파이어 이름 """

        ...

    class Skin_Wrap(modifier):
        class meshDeformOps():
            @staticmethod
            def ConvertToSkin(*args, **kwargs) -> None: ...
        engine: int
        falloff: float
        weightAllVerts: bool
        blend: bool
        meshList: runtime.Array
        ...
    class Unwrap_UVW(modifier):
        """https://help.autodesk.com/view/MAXDEV/2023/ENU/?guid=GUID-17D700DC-1FDC-4713-8041-D9E3C3EB4789"""
        class unwrap:
            def __init__(self) -> None: ...
            @classmethod
            def setMapChannel(cls, index: int) -> None: ...
        class unwrap2:
            @staticmethod
            def flattenMapNoParams() -> None: ...
        def __init__(self) -> None: ...
        def setFaceVertex(
            self,
            point3: runtime.Point3,
            face_index: int,
            vertex_index: int,
            sel: bool,
        ) -> None:
            """
            setFaceVertex <point3>pos <integer>faceIndex <integer>ithVertex <boolean>sel
            """
            ...

        def numberPointsInFace(self, index: int) -> int:
            """<integer><Unwrap_UVW>.numberPointsInFace <integer>index
                    면에 포함된 정점 수를 검색합니다.

            면은 Unwrap이 작업 중인 토폴로지 유형에 따라 3~N개의 점을 포함할 수 있습니다. 트라이 메시의 경우 이는 항상 3입니다. 패치의 경우 3 또는 4일 수 있습니다. 다각형의 경우 이는 3 이상이 될 수 있습니다. Unwrap은 세 가지 객체 유형을 모두 하나의 일반 형식으로 추상화합니다.

            <integer> index- 검사 중인 얼굴의 인덱스입니다.
            numberPointsInFace(1) -> 0
            """
            ...

        def getVertexIndexFromFace(
            self, fase_index: int, target_index: int
        ) -> int:
            """<integer><Unwrap_UVW>.getVertexIndexFromFace <integer>faceIndex <integer>ithVertex
            - ithVertex: faceIndex에서 몇 번째 정점을 찾을지 지정
            - 면에서 정점의 인덱스를 검색
            - 면 인덱스와 검사하려는 i번째 정점을 제공
            """
            ...

        def getVertexGeomIndexFromFace(
            self, face_index: int, target_index: int
        ) -> int:
            """<integer><Unwrap_UVW>.getVertexGeomIndexFromFace <integer>faceIndex <integer>ithVertex
            - ithVertex: faceIndex에서 몇 번째 정점을 찾을지 지정
            - 면에서 **메쉬**의 정점의 인덱스를 검색

            """
            ...
        def flattenMap(self, angleThreshold, normalList, spacing, normalize, layOutType, rotateClusters, fillHoles) -> None:
            """flattenMap <float>angleThreshold <point3 array>normalList <float>spacing <boolean>normalize <integer>layOutType <boolean>rotateClusters <boolean>fillHoles
            - 매핑 평탄화 대화상자를 사용하지 않고 제공된 파라미터에 따라 UVW 좌표를 평탄화합니다.
            - 이 메서드는 동일한 기능을 MAXScript에 직접 노출하며 UVW 플로터 편집을 열지 않아도 됩니다.
            """
            ...

    @staticmethod
    def maxVersion(*args, **kwargs) -> list:
        """#(25000, 62, 0, 25, 2, 2, 3312, 2023, ".2.2 Update")"""
        ...

    @staticmethod
    def addModifier(*args, **kwargs) -> None: ...
    @staticmethod
    def getSubAnim(*args, **kwargs) -> None: ...
    @staticmethod
    def select(*args, **kwargs) -> None: ...
    @staticmethod
    def importFile(*args, **kwargs) -> None: ...
    @staticmethod
    def FBXExporterSetParam(*args, **kwargs) -> None: ...
    @staticmethod
    def execute(*args, **kwargs) -> None: ...
    @staticmethod
    def doesFileExist(*args, **kwargs) -> bool: ...
    @staticmethod
    def rotateZ(*args, **kwargs) -> Matrix3: ...
    @staticmethod
    def snapshot(Node: runtime.GeometryClass) -> runtime.Editable_mesh: ...
    @staticmethod
    def redrawViews(): ...
    @staticmethod
    def inverse(matrix3: Matrix3) -> Matrix3: ...
    @staticmethod
    def AttachObjects(
        pNode: runtime.node, node: runtime.node, move=True
    ): ...
    @staticmethod
    def classOf(obj: Value): ...
    @staticmethod
    def setSelectionLevel(obj: runtime.node, level: Name):
        """
        parm:
            level: vertex
        """