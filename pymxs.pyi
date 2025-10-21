# flake8: noqa: E701
"""
 수작업으로 필요할때 추가하는 스텁파일
 - 독스티링 적용(독스트링은 상속이 안되기 때문에 여기서 적어야함)
    - 클래스 메소드 설명은 잘 따라옴.
"""
from __future__ import annotations
import enum
from contextlib import contextmanager
from typing import (
    Type, Any, overload, Literal, Iterable, TypeVar, TypeGuard, Sequence, Iterator,
    NoReturn, Optional, List, Protocol, Union, Tuple, Callable, TypeAlias,
    Dict
)
import warnings
from typing_extensions import Self

_T = TypeVar('_T')
_Iter = TypeVar('_Iter', bound=Iterable)
type MessageBoxIconType = Literal['warning', 'information', 'question', 'critical']
T = TypeVar('T')
ClassInfo: TypeAlias = Union[Type[T] , Tuple['ClassInfo[T]', ...]]
_Modifier = TypeVar('_Modifier', bound=runtime.modifier)


def attime(time: float):...
  
def animate(on_off: bool): ...

def mxsreference(obj: Any): ...

@contextmanager
def undo(on_off: bool, name): ...

class _Stub이동속성():
    pos: runtime.Point3
    scale: runtime.Point3
    position: runtime.Point3
    rotation: runtime.Quat
    scale: runtime.Point3

class runtime:

    rootNode: runtime.MAXRootNode
    objects: runtime.ObjectSet
    selection: runtime.ObjectSet
    currentTime: runtime.Time
    maxfilepath: str
    maxFilePath: str
    maxfilename: str
    maxFileName: str
    animationRange: runtime.Interval
    animateMode: bool
    sliderTime: runtime.Time
    SelectionSets: runtime.SelectionSetArray
    selectionSets: runtime.SelectionSetArray

    class Value:
        def __init__(self, *args, **kwargs) -> None: ...
        @classmethod
        def getmxsprop(cls, arg1: str) -> Any:
            """ runtime 속성값을 가져옵니다.
            :param arg1: runtime 속성 이름으로 None은 에러
            """
            ...
        ...
    class MAXWrapperNonRefTarg(Value): ...
    class ExporterPlugin(MAXWrapperNonRefTarg): ...
    class FBXEXP(ExporterPlugin):
        """ fbx 익스포트 플러그인 """
        ...
    FbxExporter = FBXEXP
    class ImporterPlugin(Value): ...
    class FBXIMP(ImporterPlugin):...
    FbxImporter = FBXIMP
    class BitMap(Value):
        filename: str
    class MAXKey(Value):
        # tension: Any
        # continuity: Any
        # bias: Any
        ...
    class SelectionSetArray(Value):
        @overload
        def __getitem__(self, name: str):...
        @overload
        def __getitem__(self, index: int):
            """ 선택셋 배열에서 인덱스에 해당하는 선택셋을 반환합니다.
            :param index: 선택셋 인덱스 (0부터 시작)
            """
        @overload
        def __setitem__(self, name: int, value) -> None:...
        @overload
        def __setitem__(self, index: str, value) -> None:
            """ 선택셋 배열에서 인덱스에 해당하는 선택셋을 설정합니다.
            :param index: 선택셋 인덱스 (0부터 시작)
            :param value: 설정할 선택셋
            """
    class MaxObject(Value):
        ...
    class MAXRootNode(Value):
        children: runtime.Array[runtime.node]
    class Set(Sequence[_T], Value):
        def __iter__(self) -> Iterator[_T]: ...
        def __next__(self) -> _T: ...
        def __len__(self) -> int: ...
    class ObjectSet(Set):...

    # class Point3(Value):
    #     """[<expr>, <expr>, <expr>]

    #     [2022 api link](https://help.autodesk.com/view/MAXDEV/2022/ENU/?guid=GUID-1564BD35-50EA-4140-9150-1AECC89F713C)
    #     """
    #     x: int
    #     y: int
    #     z: int
    #     def __init__(self, *args, **kwargs) -> None: ...
    #     ...

    class Array(Sequence[_T], Value):
        def __iter__(self) -> Iterator[_T]: ...
        def __next__(self) -> _T: ...
        def __len__(self) -> int: ...
        @overload
        def __getitem__(self, index: int) -> _T: ...
        
        @overload
        def __getitem__(self, index: slice) -> Self: ...
    class Interval(Value):
        start: runtime.Time
        end: runtime.Time


    class BitArray(Value):
        def __iter__(self) -> runtime.BitArray: ...
        def __next__(self) -> int: ...

    class interface(Value):
        ...

    class SkinUtils(interface):
        """ 스킨 유틸리티 클래스
        [helper]<https://help.autodesk.com/view/MAXDEV/2024/ENU/?guid=GUID-226B4FEA-9707-4582-A7FE-34BF142F345F>
        """
        ...
        @staticmethod
        def ImportSkinData(target_obj, source_obj) -> None:
            """ 스킨 데이터를 가져옵니다.
            """
            ...

    class pluginManager(interface):
        """플러그인 관리 클래스
        https://help.autodesk.com/view/MAXDEV/2024/ENU/?guid=GUID-2846E2E6-8D13-43A6-AD1D-3BB83A38FDD6
        """

        @staticmethod
        def loadClass(arg1) -> bool:
            """플러그인 클래스를 로드합니다.
            `<void>pluginManager.loadClass <class>class`
            """
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
            :param matchByName: 매개 변수가 true로 설정되면 뼈가 이름으로 일치합니다(대화 상자의 Match By Name 버튼을 누르는 것과 동일). 거짓이면 뼈는 인덱스로 일치합니다.\n
                - 논쟁 2 ~ 5 개는 대화 상자의 수정 및 접미사 제거 체크 박스의 상태에 해당합니다.
            :param threshold: 임계값 인수는 대화 상자의 임계값에 해당합니다.The threshold argument corresponds to the Threshold value in the dialog. 이것은 가장 가까운 이웃 임계 값입니다.
            :param interpolationType: 마지막 인수는 `Interpolation Type` 드롭다운 목록의 선택에 해당합니다. 가능한 값은 다음과 같습니다.\n
                - 0 - Vertex에 의하여 일치\n
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
    class renderers(StructDef):
        medit_locked: 'Any'  # systemGlobal
        renderDialogMode: 'Any'  # systemGlobal
        target: 'Any'  # systemGlobal
        current: 'Any'  # systemGlobal
        renderButtonText: 'Any'  # systemGlobal
        @staticmethod
        def ClearDraftRenderer(*args, **kwargs):
            ...
        activeShade: 'Any'  # systemGlobal
        production: 'Any'  # systemGlobal
        medit: 'Any'  # systemGlobal
        @staticmethod
        def GetDraftRenderer(*args, **kwargs):
            ...
    class viewport(StructDef):
        @staticmethod
        def getType() -> runtime.Name: ...
        @staticmethod
        def setType(name: runtime.Name) -> None: ...
        @staticmethod
        def getTM() -> runtime.Matrix3:
            """
            현재 뷰포트의 변환 행렬을 반환합니다.
            :return: 변환 행렬
            """
            ...
    class TCBDefaultParams(StructDef):
        easeFrom: Any
        easeTo: Any
        continuity: Any
        bias: Any
        tension: Any
    class callbacks(StructDef):
        @staticmethod
        def addScript(
            arg1:runtime.Name,
            arg2:str,
            id:runtime.Name=runtime.Name('')
        ):
            """
            :param arg1: 콜벡타입이름
            :param arg2: 실행 코드 문자열
            """;...
        @staticmethod
        def show(arg1:runtime.Name, asArray:bool=False) -> list[list]|None:
            """
            :param arg1: 콜백타입이름
            :param asArray: 콜백함수들을 배열로 반환할지 여부, 아니면 리스터 창에 출력만함
            :return: 콜백함수들 정보
                #(#(#filePreOpen, #PhysXPlugin, false, false, "px_filePreOpen()", false),
            """
            ...
        @staticmethod
        def notificationParam(*args, **kwargs):
            ...
        @staticmethod
        def removeScripts(id:runtime.Name|None=None):
            """ 콜백함수 제거 """
            ...
        @staticmethod
        def broadcastCallback(*args, **kwargs):
            ...
    class custAttributes(StructDef):
        @staticmethod
        def unRegisterDefLoadCallback(*args, **kwargs):
            ...
        @staticmethod
        def getDef(*args, **kwargs):
            ...
        @staticmethod
        def delete(*args, **kwargs):
            ...
        @staticmethod
        def getDefClass(*args, **kwargs):
            ...
        @staticmethod
        def unRegisterAllDefLoadCallbacks(*args, **kwargs):
            ...
        @staticmethod
        def getDefSource(*args, **kwargs):
            ...
        @staticmethod
        def getDefInstances(*args, **kwargs):
            ...
        @staticmethod
        def getDefData(*args, **kwargs):
            ...
        @staticmethod
        def get(*args, **kwargs):
            ...
        @staticmethod
        def getSceneLoadVersionHandlingBehavior(*args, **kwargs):
            ...
        @staticmethod
        def setDefData(*args, **kwargs):
            ...
        @staticmethod
        def setSceneLoadVersionHandlingBehavior(*args, **kwargs):
            ...
        @staticmethod
        def redefine(*args, **kwargs):
            ...
        @staticmethod
        def getPBlockDefs(*args, **kwargs):
            ...
        @staticmethod
        def getSceneMergeVersionHandlingBehavior(*args, **kwargs):
            ...
        @staticmethod
        def getSceneDefs(*args, **kwargs):
            ...
        @staticmethod
        def setSceneMergeVersionHandlingBehavior(*args, **kwargs):
            ...
        @staticmethod
        def deleteDef(*args, **kwargs):
            ...
        @staticmethod
        def setLimits(*args, **kwargs):
            ...
        @staticmethod
        def showRegisteredDefLoadCallbacks(*args, **kwargs):
            ...
        @staticmethod
        def getDefs(*args, **kwargs):
            ...
        @staticmethod
        def add(*args, **kwargs):
            ...
        @staticmethod
        def registerDefLoadCallback(*args, **kwargs):
            ...
        @staticmethod
        def makeUnique(*args, **kwargs):
            ...
        @staticmethod
        def getOwner(*args, **kwargs):
            ...
        @staticmethod
        def count(*args, **kwargs):
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
            :return: 최상단 상단 스택이 1로 부터 시작하는 위치숫자
            - 위치숫자1 == obj.modifiers[0]
            '''
            ...

    class refs(StructDef):
        @staticmethod
        def dependentNodes(*args, **kwargs) -> list: ...
        
        @staticmethod
        def replaceReference(object, index: int, newTarget) -> None:
            """ 오브젝트의 index번째 레퍼런스를 newTarget으로 교체합니다.
            타입체크를 해주지는 않으니 검증후 적용이 필요함.

            :param object: 레퍼런스를 교체할 오브젝트
            :param index: 교체할 레퍼런스의 인덱스 (1부터 시작)
            :param newTarget: 새로 설정할 레퍼런스 대상
            
            예)
            오브젝티의 인덱스1은 트렌스폼 컨트롤러. 이걸 다른 컨트롤러로 교체.
            rt.refs.replaceReference(obj, 1, new_controller)

            트렌스폼의 하위 컨트롤러 교체도 가능
            rt.refs.replaceReference(obj.transform, 2, rt.euler_XYZ())
            """
            ...


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
            :param nameflag:
                - 0: bone name\n
                - 1: UI list name
            :type nameflag: Literal[0,1]
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
    class IScriptCtrl(runtime.Interface):
        """Script Controller Interface
        스크립트 컨트롤러의 인터페이스를 제공합니다.
        """
        
        # Properties
        ThrowOnError: bool
        """스크립트 오류 발생 시 예외를 던질지 여부를 설정합니다."""
        
        # Methods
        def SetExpression(self, expression: str) -> bool:
            """스크립트 표현식을 설정합니다.
            
            :param expression: 설정할 스크립트 표현식
            :return: 설정 성공 여부
            """
            ...
        
        def GetExpression(self) -> str:
            """현재 스크립트 표현식을 반환합니다.
            
            :return: 현재 설정된 스크립트 표현식
            """
            ...
        
        def GetDescription(self) -> str:
            """스크립트 컨트롤러의 설명을 반환합니다.
            
            :return: 컨트롤러 설명
            """
            ...
        
        def SetDescription(self, description: str) -> bool:
            """스크립트 컨트롤러의 설명을 설정합니다.
            
            :param description: 설정할 설명
            :return: 설정 성공 여부
            """
            ...
        
        def NumVariables(self) -> int:
            """스크립트에서 사용되는 변수의 개수를 반환합니다.
            
            :return: 변수 개수
            """
            ...
        
        def AddConstant(self, name: str, constant: Any) -> bool:
            """상수 변수를 추가합니다.
            
            :param name: 변수 이름
            :param constant: 상수 값
            :return: 추가 성공 여부
            """
            ...
        
        def AddTarget(self, name: str, target: Any, offset: runtime.Time = runtime.Time(0), owner: Any = None) -> bool:
            """타겟 변수를 추가합니다.
            
            :param name: 변수 이름
            :param target: 타겟 값
            :param offset: 시간 오프셋 (기본값: 0f)
            :param owner: 소유자 (기본값: undefined)
            :return: 추가 성공 여부
            """
            ...
        
        def AddObject(self, name: str, obj: Any) -> bool:
            """오브젝트 변수를 추가합니다.
            
            :param name: 변수 이름
            :param obj: 오브젝트 값
            :return: 추가 성공 여부
            """
            ...
        
        def AddNode(self, name: str, node: runtime.node) -> bool:
            """노드 변수를 추가합니다.
            
            :param name: 변수 이름
            :param node: 노드
            :return: 추가 성공 여부
            """
            ...
        
        def SetConstant(self, which: Union[str, int], constant: Any) -> bool:
            """상수 변수의 값을 설정합니다.
            
            :param which: 변수 식별자 (이름 또는 인덱스)
            :param constant: 새로운 상수 값
            :return: 설정 성공 여부
            """
            ...
        
        def SetTarget(self, which: Union[str, int], target: Any, owner: Any = None) -> bool:
            """타겟 변수의 값을 설정합니다.
            
            :param which: 변수 식별자 (이름 또는 인덱스)
            :param target: 새로운 타겟 값
            :param owner: 소유자 (기본값: undefined)
            :return: 설정 성공 여부
            """
            ...
        
        def SetObject(self, which: Union[str, int], obj: Any) -> bool:
            """오브젝트 변수의 값을 설정합니다.
            
            :param which: 변수 식별자 (이름 또는 인덱스)
            :param obj: 새로운 오브젝트 값
            :return: 설정 성공 여부
            """
            ...
        
        def SetNode(self, which: Union[str, int], node: runtime.node) -> bool:
            """노드 변수의 값을 설정합니다.
            
            :param which: 변수 식별자 (이름 또는 인덱스)
            :param node: 새로운 노드
            :return: 설정 성공 여부
            """
            ...
        
        def DeleteVariable(self, which: Union[str, int]) -> bool:
            """변수를 삭제합니다.
            
            :param which: 변수 식별자 (이름 또는 인덱스)
            :return: 삭제 성공 여부
            """
            ...
        
        def RenameVariable(self, which: Union[str, int], name: str) -> bool:
            """변수의 이름을 변경합니다.
            
            :param which: 변수 식별자 (이름 또는 인덱스)
            :param name: 새로운 변수 이름
            :return: 이름 변경 성공 여부
            """
            ...
        
        def GetOffset(self, which: Union[str, int]) -> runtime.Time:
            """변수의 시간 오프셋을 반환합니다.
            
            :param which: 변수 식별자 (이름 또는 인덱스)
            :return: 시간 오프셋
            """
            ...
        
        def SetOffset(self, which: Union[str, int], offset: runtime.Time) -> bool:
            """변수의 시간 오프셋을 설정합니다.
            
            :param which: 변수 식별자 (이름 또는 인덱스)
            :param offset: 새로운 시간 오프셋
            :return: 설정 성공 여부
            """
            ...
        
        def VariableExists(self, name: str) -> bool:
            """지정된 이름의 변수가 존재하는지 확인합니다.
            
            :param name: 확인할 변수 이름
            :return: 변수 존재 여부
            """
            ...
        
        def GetConstant(self, which: Union[str, int]) -> Any:
            """상수 변수의 값을 반환합니다.
            
            :param which: 변수 식별자 (이름 또는 인덱스)
            :return: 상수 값
            """
            ...
        
        def GetTarget(self, which: Union[str, int], asObject: bool = False) -> Any:
            """타겟 변수의 값을 반환합니다.
            
            :param which: 변수 식별자 (이름 또는 인덱스)
            :param asObject: 오브젝트로 반환할지 여부 (기본값: False)
            :return: 타겟 값
            """
            ...
        
        def GetObject(self, which: Union[str, int]) -> runtime.MaxObject:
            """오브젝트 변수의 값을 반환합니다.
            
            :param which: 변수 식별자 (이름 또는 인덱스)
            :return: 오브젝트 값
            """
            ...
        
        def GetNode(self, which: Union[str, int]) -> runtime.node:
            """노드 변수의 값을 반환합니다.
            
            :param which: 변수 식별자 (이름 또는 인덱스)
            :return: 노드
            """
            ...
        
        def GetValue(self, which: Union[str, int], asObject: bool = False) -> Any:
            """변수의 값을 반환합니다.
            
            :param which: 변수 식별자 (이름 또는 인덱스)
            :param asObject: 오브젝트로 반환할지 여부 (기본값: False)
            :return: 변수 값
            """
            ...
        
        def GetVarValue(self, which: Union[str, int]) -> Any:
            """변수의 값을 반환합니다.
            
            :param which: 변수 식별자 (이름 또는 인덱스)
            :return: 변수 값
            """
            ...
        
        def GetType(self, which: Union[str, int]) -> Literal['unknown', 'target', 'constant', 'object', 'node']:
            """변수의 타입을 반환합니다.
            
            :param which: 변수 식별자 (이름 또는 인덱스)
            :return: 변수 타입 (#unknown|#target|#constant|#object|#node)
            """
            ...
        
        def GetName(self, index: int) -> str:
            """지정된 인덱스의 변수 이름을 반환합니다.
            
            :param index: 변수 인덱스
            :return: 변수 이름
            """
            ...
        
        def GetIndex(self, name: str) -> int:
            """지정된 이름의 변수 인덱스를 반환합니다.
            
            :param name: 변수 이름
            :return: 변수 인덱스
            """
            ...
        
        def Update(self) -> None:
            """스크립트 컨트롤러를 업데이트합니다."""
            ...
        
        def PrintDetails(self) -> str:
            """스크립트 컨트롤러의 상세 정보를 문자열로 반환합니다.
            
            :return: 상세 정보 문자열
            """
            ...
       
    class renderMessageManager(runtime.Interface):
        """ """
        ShowInfoMessage: bool = ...
        LogFilename: str = ...
        OpenOnWarning: bool = ...
        autoScroll: bool = ...
        ShowProgressMessage: bool = ...
        LogFileON: bool = ...
        OpenOnError: bool = ...
        LogDebugMessage: bool = ...
        LogFileAppend: bool = ...
        @staticmethod
        def HideWindow():
            ...
        @staticmethod
        def OpenWindow():
            ...
        @staticmethod
        def ClearWindow():
            ...
    class NamedSelectionSetManager(runtime.Interface):
        @staticmethod
        def AddNewNamedSelSet(nodes: Iterable[runtime.node], name: str) -> None:
            """
            새로운 이름이 지정된 선택 집합을 추가합니다.
            :param nodes: 노드들의 iterable
            :param name: 선택 집합의 이름
            """
            ...
        @staticmethod
        def RemoveNamedSelSet(name: str) -> None:
            """ 이름이 지정된 선택 집합을 제거합니다. """
            ...
        @staticmethod
        def GetNamedSelSetNames() -> List[str]:
            """ 현재 존재하는 이름이 지정된 선택 집합의 이름들을 반환합니다. """
            ...
        @staticmethod
        def GetNumNamedSelSets() -> int:
            """ 현재 존재하는 이름이 지정된 선택 집합의 개수를 반환합니다. """
            ...
        @staticmethod
        def GetNamedSelSetName(index: int) -> str:
            """
            주어진 인덱스에 해당하는 이름이 지정된 선택 집합의 이름을 반환합니다.
            :param index: 선택 집합의 인덱스 (0부터 시작)
            :return: 선택 집합의 이름
            """
            ...
        @staticmethod
        def GetNamedSelSetItemCount(set_index: int) -> int:
            """
            주어진 선택 집합 인덱스에 해당하는 아이템의 개수를 반환합니다.
            :param set_index: 선택 집합의 인덱스 (0부터 시작)
            :return: 선택 집합의 아이템 개수
            """
        @staticmethod
        def GetNamedSelSetItem(set_index: int, item_index: int) -> runtime.node:
            """
            주어진 선택 집합 인덱스와 아이템 인덱스에 해당하는 노드를 반환합니다.
            :param set_index: 선택 집합의 인덱스 (0부터 시작)
            :param item_index: 아이템의 인덱스 (0부터 시작)
            :return: 선택 집합에서 해당 아이템의 노드
            """
            ...
        @staticmethod
        def RemoveNamedSelSetByIndex(set_index: int) -> bool:
            """
            주어진 인덱스에 해당하는 이름이 지정된 선택 집합을 제거합니다.
            :param set_index: 선택 집합의 인덱스 (0부터 시작)
            :return: 제거 성공 여부
            """
            ...
        @staticmethod
        def RemoveNamedSelSetByName(set_name: str) -> bool:
            """
            주어진 이름에 해당하는 이름이 지정된 선택 집합을 제거합니다.
            RemoveNamedSelSetByName - no automatic redraw after invoked
            :param set_name: 선택 집합의 이름
            :return: 제거 성공 여부
            """
            ...
    class LayerProperties(Interface):
        # --- Properties ---
        on: bool
        lock: bool
        current: bool
        wireColor: runtime.Color
        isGIExcluded: bool
        renderable: bool
        inheritVisibility: bool
        primaryVisibility: bool
        secondaryVisibility: bool
        receiveshadows: bool
        castShadows: bool
        applyAtmospherics: bool
        renderOccluded: bool
        ishidden: bool
        isfrozen: bool
        boxmode: bool
        backfacecull: bool
        alledges: bool
        vertexTicks: bool
        showTrajectory: bool
        xray: bool
        ignoreExtents: bool
        showFrozenInGray: bool
        showVertexColors: bool
        vertexColorsShaded: bool
        visibility: float
        imageMotionBlurMultiplier: float
        motionBlurOn: bool
        motionblur: Literal["none", "object", "image"]
        display: Literal["viewport", "boundingbox", "wireframe", "shaded"]

        # --- Read-only Properties ---
        @property
        def name(self) -> str: ...
        @property
        def INodeGIProperties(self) -> Any: ... # 실제 GIProperties 인터페이스 타입으로 대체 가능
        @property
        def layerAsRefTarg(self) -> runtime.MaxObject: ...

        # --- Methods ---
        def addnode(self, node: runtime.node) -> None: ...
        def addnodes(self, nodes: List[runtime.node]) -> None: ...
        def select(self, OnOff: bool) -> None: ...
        def setname(self, name: str) -> bool: ...
        def nodes(self) -> List[runtime.node]:
            """
            이 메서드는 MAXScript에서 out 파라미터를 사용하지만,
            Python에서는 반환 값으로 노드 리스트를 받는 것이 일반적입니다.
            """
            ...
        def getParent(self) -> Optional[runtime.LayerProperties]: ...
        def setParent(self, parent: runtime.LayerProperties) -> bool: ...
        def getChild(self, index: int) -> Optional[runtime.LayerProperties]: ...
        def getNumChildren(self) -> int: ...
        def canDelete(self) -> bool: ...
        def getNumNodes(self) -> int: ...
        def hasSceneXRefNodesInHierarchy(self) -> bool: ...
    class INode(Interface):
        boneEnable: bool
        posTaskWeight: float
        rotTaskWeight: float
        boneAutoAlign: bool
        boneFreezeLength: bool
        boneScaleType: runtime.Name
        """ [#scale, #squash, #none] """
        stretchTM: runtime.Matrix3
        boneAxis: runtime.Name
        """ [#x, #y, #z] """
        boneAxisFlip: bool
        primaryVisibility: bool
        secondaryVisibility: bool
        applyAtmospherics: bool
        vertexColorType: runtime.Name
        """ [#color, #illum, #alpha. #color_plus_illum, #soft_select, #map_channel] """
        showVertexColors: int
        shadeVertexColors: int
        vertexColorMapChannel: int
        handle: int
        isSceneXRefNode: bool
        posInParent: runtime.Point3
        rotInParent: runtime.Point3
        scaleInParent: runtime.Point3
        scaleOrientInParent: runtime.Quat
        wasLoadedByLastMerge: bool
        OverrideMaterialEnabled: bool
        def setBoneEnable(self, value: bool, time: runtime.Time) -> None: ...
        def realignBoneToChild(self) -> None: ...
        def resetBoneStretch(self) -> None: ...


    class menuMan(Interface):
        @staticmethod
        def loadMenuFile(file:str) -> bool:
            """
            :param file: filename
            """
            ...
        @staticmethod
        def saveMenuFile(file:str) -> bool:
            """
            :param file: filename
            """
            ...
        @staticmethod
        def getMenuFile() -> str:
            """
            :return: filename
            """
            ...
        @staticmethod
        def updateMenuBar() -> None: ...
        @staticmethod
        def registerMenuContext(contextId: int) -> bool: ...
        @staticmethod
        def findMenu(menuName:str) -> runtime.MixinInterface.menu: ...
        @staticmethod
        def findQuadMenu(menuName:str) -> runtime.MixinInterface.menu: ...
        @staticmethod
        def unRegisterMenu(menu:runtime.MixinInterface.menu) -> bool: ...
        @staticmethod
        def unRegisterQuadMenu(menu:runtime.MixinInterface.quadMenu) -> bool: ...
        @staticmethod
        def createMenu(name:str) -> runtime.MixinInterface.menu: ...
        @staticmethod
        def createQuadMenu(name:str, quad1Name:str, quad2Name:str, quad3Name:str, quad4Name:str) -> runtime.MixinInterface.quadMenu: ...
        @staticmethod
        def createSubMenuItem(name:str, subMenu:runtime.MixinInterface.menu) -> runtime.MixinInterface.menuItem:
            """
            :param name: 메뉴 이름
            :param subMenu: 생성될 메뉴
            :return: 생성된 아이템
            """
            ...
        @staticmethod
        def createSeparatorItem() -> runtime.MixinInterface.menuItem: ...
        @staticmethod
        def createActionItem(macroScriptName:str, macroScriptCategory:str) -> runtime.MixinInterface.menuItem: ...
        @staticmethod
        def setViewportRightClickMenu(which: runtime.Name, menu) -> bool:
            """
            :param which: which enums: {#nonePressed|#shiftPressed|#altPressed|#controlPressed|#shiftAndAltPressed|#shiftAndControlPressed|#controlAndAltPressed|#shiftAndAltAndControlPressed}
            """
            ...
        @staticmethod
        def getViewportRightClickMenu(which: runtime.Name):
            """
            :param which: which enums: {#nonePressed|#shiftPressed|#altPressed|#controlPressed|#shiftAndAltPressed|#shiftAndControlPressed|#controlAndAltPressed|#shiftAndAltAndControlPressed}
            :return: runtime.MixinInterface.menu
            """
            ...
        @staticmethod
        def getMainMenuBar() -> runtime.MixinInterface.menu: ...
        @staticmethod
        def getMainMsetMainMenuBarenuBar(menu:runtime.MixinInterface.menu) -> bool: ...
        @staticmethod
        def getShowAllQuads(quadMenu:runtime.MixinInterface.quadMenu) -> bool: ...
        @staticmethod
        def setShowAllQuads(quadMenu:runtime.MixinInterface.quadMenu, value:bool) -> None: ...
        @staticmethod
        def getQuadMenuName(quadMenu:runtime.MixinInterface.quadMenu) -> str: ...
        @staticmethod
        def setQuadMenuName(quadMenu:runtime.MixinInterface.quadMenu, name:str) -> None: ...
        @staticmethod
        def numMenus() -> int: ...
        @staticmethod
        def getMenu(index: int) -> runtime.MixinInterface.menu:
            """:param index: 메뉴 인덱스 (1부터 시작)""";...
        @staticmethod
        def numQuadMenus() -> int: ...
        @staticmethod
        def getQuadMenu(index: int) -> runtime.MixinInterface.quadMenu:
            """:param index: 메뉴 인덱스 (1부터 시작)""";...
        @staticmethod
        def createMenuItemFromAction(group:str, action: str, categroy:str|None=None) -> runtime.MixinInterface.menuItem: ...
    
    class MixinInterface(Value):
        """ 타입 체킹용 클래스로 하위클래스를 직접 사용금지 """
        class menu(runtime.Interface):
            def setTitle(self, title:str) -> None: ...
            def getTitle(self) -> str: ...
            def numItems(self) -> int: ...
            def getItem(self, position: int) -> runtime.MixinInterface.menu:
                """:param position: 메뉴 아이템 위치 (1부터 시작)""";...
            def addItem(self, item: runtime.MixinInterface.menu, position: int) -> None:
                """:param position: 1부터 시작""";...
            def removeItemByPosition(self, position: int) -> None: ...
            def removeItem(self, item: runtime.MixinInterface.menu) -> None:
                """ 메뉴에서 item을 제거 것(삭제 아님)""";...

        class menuItem(runtime.Interface):
            def setTitle(self, title:str) -> None: ...
            def getTitle(self) -> str: ...
            def setUseCustomTitle(self, value:bool) -> bool: ...
            def getUseCustomTitle(self) -> str: ...
            def setDisplayFlat(self, value:bool) -> bool: ...
            def getDisplayFlat(self) -> bool: ...
            def getIsSeparator(self) -> bool: ...
            def getSubMenu(self) -> runtime.MixinInterface.menu: ...

        class quadMenu(runtime.Interface):
            def getMenu(self, position:int) -> runtime.MixinInterface.menu: ...
            def trackMenu(self, showAllQuads:bool) -> None: ...

    class list(MixinInterface):
        """ https://help.autodesk.com/view/MAXDEV/2024/ENU/?guid=Max_Developer_Help_cpp_ref_class_i_list_control_html"""
        count: int
        def getCount(self) -> int: ...
        def setActive(self, arg1: int) -> None:
            """:param arg1: 1부터 시작, 활성화할 대상""";...
        def getActive(self) -> int:
            """:retrun: 활성화 인덱스 1 부터""";...
        def delete(self, arg1: int) -> None:
            """:param arg1: 1부터 시작, 삭제할 대상""";...
        def cut(self, arg1: int) -> None:...
        def paste(self, arg1: int) -> None:...
        def getName(self, arg1: int) -> str:...
        def setName(self, arg1: int, arg2:str) -> None:
            """
            :param arg1: <index>listIndex: 항목의 인덱스입니다.
            :param arg2:  <string>name: 설정할 이름입니다.""";...

    class constraints(MixinInterface):
            def getNumTargets(self) -> int: ...
            def getNode(self, nodeNumber: int) -> runtime.node: ...
            def getWeight(self, targetNumber: int) -> float: ...
            def setWeight(self, targetNumber: int, weight: float) -> bool: ...
            #  공통요소 아님
            # def appendTarget(self, target:runtime.node, weight:float) -> bool: ...
            def deleteTarget(self, targetNumber: int) -> bool: ...

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
    def RotateX(matrix3: runtime.Matrix3, number: int|float):
        ''' maxtrix3는 참조값으로 업데이트됨, number는 회전값 '''
        ...
    @staticmethod
    def RotateY(matrix3: runtime.Matrix3, number: int|float):
        ''' maxtrix3는 참조값으로 업데이트됨, number는 회전값 '''
        ...
    @staticmethod
    def RotateZ (matrix3: runtime.Matrix3, number: int|float):
        ''' maxtrix3는 참조값으로 업데이트됨, number는 회전값 '''
        ...
    @staticmethod
    def rotate(matrix3: runtime.Matrix3, number: runtime.Quat):
        ''' maxtrix3는 참조값으로 업데이트됨, number는 회전값 '''
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
    def isKindOf(arg1: Any, arg2:ClassInfo[_T]) -> TypeGuard[_T]:
        return isinstance(arg1, arg2)
    @staticmethod
    def messageBox(*args, **kwargs) -> Any: ...
    @staticmethod
    def attachObjects(node1, node2, move:bool=True) -> None:
        """링크 걸기

        :param node1:부모가 될 노드
        :param node2:부모가 될 노드의 자식이 될 노드
        :param move: True이면 node2가 node1의 위치로 이동됩니다.
        """
        ...
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
    def cross(arg1: Point3, arg2: Point3) -> Point3:
        """ [help2024](https://help.autodesk.com/view/MAXDEV/2024/ENU/?guid=GUID-1564BD35-50EA-4140-9150-1AECC89F713C)
        :return: 두 벡터로 정의된 평면에 항상 수직인 세 번째 벡터이며, 방향은 오른손 법칙에 의해 결정되는 백터를 반환 """
        ...
    @staticmethod
    def normalize(transform: Point3) -> Point3:
        """ [help2024](https://help.autodesk.com/view/MAXDEV/2024/ENU/?guid=GUID-1564BD35-50EA-4140-9150-1AECC89F713C) """
        ...
    @staticmethod
    def distance(a: Point3, b: Point3) -> float: ...
    @staticmethod
    def getCurrentSelection() -> Array: ...
    @staticmethod
    def isValidNode(obj: _T|None) -> TypeGuard[_T]: ...
    @staticmethod
    def GetNamedSelSetName(i: int) -> str:
        """ n번째 명명된 선택 세트의 이름을 반환합니다. """
        ...
    @staticmethod
    def GetNamedSelSetItem(i: int, n: int) -> runtime.node:
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
    def getNodeByName(name: str) -> runtime.node | None: ...
    @staticmethod
    def setUserPropVal (
        arg1, arg2:str, arg3:str|int|bool,
        quoteString:bool=False, encodeCRLF: bool=False
    ) -> None:
        r"""
        :param arg1: 노드
        :param arg2: 키 문자열
        :param arg3: 입력할 값
        :param quoteString: 값을 문자열로 저장할지 여부
        :param encodeCRLF:   encodeCRLF가 지정되지 않았거나 true로 지정된 경우
            속성 값의 문자열에 있는 캐리지 리턴 또는 줄 바꿈 문자는 16진수
            표현으로 변환되고, 그렇지 않으면 16진수 표현으로 변환되지 않습니다.
            즉, '\r\n'은 '\xd\xa'로 변환됩니다.
        """;...
    @staticmethod
    def getUserPropVal(obj, key_string, *args, **kwargs) -> str: ...
    @staticmethod
    def ShellLaunch(*args, **kwargs) -> None: ...
    @staticmethod
    def loadMaxFile(*args, **kwargs) -> None: ...
    @staticmethod
    def mergeMAXFile(*args, **kwargs) -> None: ...
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
    def GetDir(name: runtime.Name) -> str:
        """:param name: #userMacros 같은 예약어 네임 """;...
    @staticmethod
    def resetMaxFile(noPrompt: runtime.Name) -> None: ...
    @staticmethod
    def clearListener() -> None: ...
    @staticmethod
    def copy(arg1: _T) -> _T: ...


    class Object(Value):...
    class MAXObject(Value):...
    class Time(Value, int, float):
        frame: float
        def __init__(self, *args, **kwargs) -> None: ...
    class RendererClass(MAXWrapper): ...
    class Default_Scanline_Renderer(RendererClass): ...
    class rotationController(MAXWrapper): ...
    class Euler_XYZ(rotationController): ...
    class LookAt_Constraint(rotationController):
        """[Helper AIP](<https://help.autodesk.com/view/MAXDEV/2024/ENU/?guid=GUID-5ACA7739-C848-40F4-BFCD-D0863BA300F4>)
        """
        target_axis: int
        upnode_axis: int
        upnode_world: bool
        pickUpNode: runtime.node|None
        ...
    class tcb_rotation(rotationController): ...
    class rotation_list(runtime.list,rotationController):
        available: runtime.Quat
        average: bool
        weight: runtime.Array[float]
        list: runtime.list
    class Orientation_Constraint(constraints, rotationController):
        def appendTarget(self, target:runtime.node, weight:float) -> bool: ...
    class positionController(MAXWrapper):
        """ """;...
    class Position_Constraint(constraints, positionController):
        def appendTarget(self, target:runtime.node, weight:float) -> bool: ...
    class position_list(positionController):
        weight: runtime.Array[float]
        average: bool
        index: int
        indexMode: bool
        count: int
        active: int
        """ index"""
        Available : runtime.Point3
        
        def getCount(self) -> int:...
        def setActive(self, arg1: int) -> None:...

    class Position_XYZ(MAXWrapper): ...
    class Matrix3Controller(MAXWrapper, _Stub이동속성): ...
    class prs(Matrix3Controller): ...
    class transform_list(Matrix3Controller, runtime.list):
        list: runtime.list
        """ list 인터페이스 """
        ...
    class Link_Constraint(runtime.constraints, Matrix3Controller):
        def addTarget(self, target:runtime.node, frameNo:int) -> bool: ...
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

    class GeometryClass(node):
        boxmode: bool
        name: str
        transform: runtime.Matrix3
        mesh: runtime.TriMesh
        numfaces: int
        wireColor: runtime.Color
        modifiers: Dict[Union[type[runtime.modifier], runtime.Name, int], runtime.modifier]
        def __init__(self, name:str='', **kwargs) -> None: ...

    class Dummy(helper, _Stub이동속성): ...
    class Point(GeometryClass, _Stub이동속성): ...
    class Biped_Object(GeometryClass):...

    class logsystem(StructDef):
        logDays: int
        logSize: int
        quietMode: bool
        enabled: bool
        longevity: runtime.Name
        ''' Literal[#days] '''
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

    class helper(node, _Stub이동속성):
        modifiers: Dict[Union[Type[runtime.modifier], runtime.Name, int], runtime.modifier]
        ...

    class Bone(helper):
        """
        :ivar boneScaleType: runtime.Name('none')
        """
        length: int
        fronfin: bool
        frontfinsize: int
        sidefins: bool
        sidefinssize: int
        boneEnable: bool
        boneFreeaeLength: bool
        boneAutoAlign: bool
        boneScaleType: runtime.Name = runtime.Name('none')
        def __init__(self, *args, **kwargs) -> None:
            ...
        
    class vertexColorType(runtime.Name):
        color: Type[runtime.Name]
        illum: Type[runtime.Name]
        alpha: Type[runtime.Name]
        color_plus_illum: Type[runtime.Name]
        ...
    class NodeGeneric(Value): ...
    class setFaceSelection(NodeGeneric):
        def __new__(cls, *args, **kwargs) -> None: ...
    class getFaceSelection(NodeGeneric):
        def __new__(cls, *args, **kwargs) -> runtime.BitArray: ...
    class getUserProp(NodeGeneric):
        """
        :param arg1: 값을 가져올 노드 
        :type arg1: runtime.node
        :param arg2: key용 문자열
        :type arg2: str
        :return: 값을 int, bool, str 중 하나로 반환합니다. 없으면 None.
        :rtype: int | bool | str | None
        """
        def __new__(cls, arg1, arg2:str) -> int|bool|str|None: ...
    class setUserProp(NodeGeneric):
        """
        :param arg1: 값을 가져올 노드 
        :type arg1: runtime.node
        :param arg2: key용 문자열
        :type arg2: str
        :return: 값을 int, bool, str 중 하나로 반환합니다. 없으면 None.
        :rtype: int | bool | str | None
        """
        def __new__(cls, arg1, arg2:str, arg3:int|bool|str) -> int|bool|str|None: ...
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
    class node(INode, runtime.MAXWrapper):
        """[Node : MAXWrapper](https://help.autodesk.com/view/MAXDEV/2023/ENU/?guid=GUID-1C9953AA-4750-4147-91DC-127AF2F7BC87)
        [Interface : INode](https://help.autodesk.com/view/MAXDEV/2023/ENU/?guid=GUID-0BFEF796-5952-48B0-8929-88475F927649)
        """
        position: ...
        rotation: ...
        scale: ...
        pivot: ...
        min: ...
        max: ...
        center: ...
        dir: ...
        objectoffsetpos: ...
        objectoffsetrot: ...
        objectoffsetscale: ...
        objecttransform: ...
        modifiers: ...
        isDeleted: ...
        custAttributes: ...
        lookat: ...
        ishidden: ...
        boxmode: ...
        alledges: ...
        backfacecull: ...
        receiveshadows: ...
        isdependent: ...
        istarget: ...
        gbufferchannel: ...
        motionblur: ...
        isfrozen: ...
        showVertexColors: ...
        rcvCaustics: ...
        generateCaustics: ...
        generateGlobalIllum: ...
        isnodehidden: ...
        isnodefrozen: ...
        ishiddenInVpt: ...
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
        children: runtime.Array[Self]
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
        :rtype: Literal["#none", "#object", "#image"]
        '''
        generatecaustics: bool
        rcvcaustics: bool
        generateGlobalIllume: bool
        rcvGlobalIllum: bool
        ...
    class camera(node, _Stub이동속성):
        fov: float
        """ default: 45.0 """
        curFOV: float
        """ default: 45.0 """
        fovType: Literal[1,2,3]
        """ 1: horizontal, 2: vertical, 3: diagonal
        default: 1 """
        orthoProjection: bool
        """ default: False """
        type: runtime.Name
        """ literal["free", "target"]
        default: runtime.Name("free")
        """
        showCone: bool
        """ default: True """
        showHorizeon: bool
        """ default: True """
        nearrange: float
        """ default: 0.0 """
        farrange: float
        """ default: 1000.0 """
        clipManually: bool
        """ default: False """
        nearClip: float
        """ default: 1.0 """
        farclip: float
        """ default: 1000.0 """
        showRanges: bool
        """ default: false """
        targetDistance: float
        """ default: 16.0 """
        mpassEnable: bool
        """ default: False """
        mpassRenderPerPass: bool
        """ default: False """
    class Freecamera(camera): ...
    class floatController(MAXWrapper):
        keys: runtime.Array[runtime.MAXKey]
        def __init__(self) -> None: ...
        ...
    class float_script(floatController, IScriptCtrl):
        IScriptCtrl: runtime.IScriptCtrl
        ...
    class Linear_Float(floatController): ...
    class bezier_float(floatController):
        def __init__(self) -> None: ...
        ...
    class Editable_mesh(GeometryClass):...
    class BoneGeometry(GeometryClass):
        sidefins: bool
        fronfin: bool
        ...
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
        def setCopyName(biped_ctrl, name: runtime.Name, int_which:int, String_newName:str):
            """
            :param biped_ctrl: Biped 컨트롤러
            :param name: Literal["posture", "pose", "track"]
            :param int_which: ?부터 시작하는 인덱스
            :param String_newName: 새 이름
            """
            ...
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
        def numCopyCollections(biped_ctrl) -> int:
            """
            :param biped_ctrl: Biped 컨트롤러
            :return: 컬렉션의 수,  없으면 0
            """
            ...
        @staticmethod
        def createScaleSubAnims(*args, **kwargs): ...
        @staticmethod
        def collapseAtLayer(ctrl, index: int) -> None: ...
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
        def getCopyCollection(ctrl, index):
            """
            :param ctrl: Biped 컨트롤러
            :param index: 1부터 시작하는 인덱스
            :return: CopyCollection 객체 없으면 False
            """
            ...
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
    # class GetDir(Primitive):
    #     """
    #     :arg name:
    #     - #userMacros
    #     """
    #     def __new__(cls, name: runtime.Name) -> str:
    #         ...
    #     ...
    class getINISetting(Primitive):
        """[api](https://help.autodesk.com/view/MAXDEV/2024/ENU/?guid=GUID-CF408D64-D4E2-4C39-90DB-62E525D7B45A)
        
        :arg file_name: "c:/temp/test.ini"
        :arg section: "Directories"
        :arg key: "Scenes"
        """
        def __new__(cls, file_name: str, section:str, key:str, defaultValue: str="") -> str:
            ...
    class Point3(Value):
        """[x, y, z]

        [2022 api link](https://help.autodesk.com/view/MAXDEV/2022/ENU/?guid=GUID-1564BD35-50EA-4140-9150-1AECC89F713C)
        """
        x: int
        y: int
        z: int
        def __init__(self, *args, **kwargs) -> None: ...
        ...
        def __add__(self, other): ...
        def __mul__(self, other): ...

    class Color(runtime.Value):
        def __init__(self, *args, **kwargs) -> None: ...

    class Biped(runtime.Value): ...

    class LayerManager(runtime.Value):
        count: int
        current : runtime.LayerProperties

        @staticmethod
        def getLayerFromName(*args, **kwargs): ...
        ...
        @staticmethod
        def getLayer(index: int) -> runtime.LayerProperties:...
        @staticmethod
        def newLayerFromName(name: str) -> runtime.LayerProperties:...
    class Generic(Value): ...

    class getnumtverts(Generic):
        """-> int"""

        def __new__(cls, node) -> int: ...
    class sort(Generic):
        """:arg items: iterable"""

        def __new__(cls, items:Iterable[_T]) -> Iterable[_T]: ...

    subObjectLevel: int

    class convertToMesh(NodeGeneric):
        def __new__(cls, node) -> None: ...

    class Skin(runtime.modifier):
        bone_Limit: int
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
        """ """
        @staticmethod
        def getNumVDataChannels(*args, **kwargs):...
        @staticmethod
        def getNumMaps(*args, **kwargs):...
        @staticmethod
        def weldEdgesByThreshold(*args, **kwargs):...
        @staticmethod
        def createPolygon(*args, **kwargs):...
        @staticmethod
        def createVert(*args, **kwargs):...
        @staticmethod
        def collapseDeadStructs(*args, **kwargs):...
        @staticmethod
        def getVertsByMatId(*args, **kwargs):...
        @staticmethod
        def setFaceFlags(*args, **kwargs):...
        @staticmethod
        def setEDataChannelSupport(*args, **kwargs):...
        @staticmethod
        def setMapFace(*args, **kwargs):...
        @staticmethod
        def capHolesByEdge(*args, **kwargs):...
        @staticmethod
        def cutFace(*args, **kwargs):...
        @staticmethod
        def makeVertsPlanar(*args, **kwargs):...
        @staticmethod
        def inSlicePlaneMode(*args, **kwargs):...
        @staticmethod
        def getFacesEdges(*args, **kwargs):...
        @staticmethod
        def getFacesUsingVert(*args, **kwargs):...
        @staticmethod
        def getVertsByFlag(*args, **kwargs):...
        @staticmethod
        def setVDataChannelSupport(*args, **kwargs):...
        @staticmethod
        def setMapSupport(*args, **kwargs):...
        @staticmethod
        def weldEdges(*args, **kwargs):...
        @staticmethod
        def unHideAllFaces(*args, **kwargs):...
        @staticmethod
        def unHideAllVerts(*args, **kwargs):...
        @staticmethod
        def attach(*args, **kwargs):...
        @staticmethod
        def getBorderFromEdge(*args, **kwargs):...
        @staticmethod
        def getDeadVerts(*args, **kwargs):...
        @staticmethod
        def getNumVerts(*args, **kwargs):...
        @staticmethod
        def getEDataChannelSupport(*args, **kwargs):...
        @staticmethod
        def getMapFace(*args, **kwargs):...
        @staticmethod
        def makeEdgesPlanar(*args, **kwargs):...
        @staticmethod
        def capHolesByFace(*args, **kwargs):...
        @staticmethod
        def moveVertsToPlane(*args, **kwargs):...
        @staticmethod
        def getVert(*args, **kwargs):...
        @staticmethod
        def getFaceDeg(*args, **kwargs):...
        @staticmethod
        def getVertsUsingEdge(*args, **kwargs):...
        @staticmethod
        def getVertFlags(*args, **kwargs):...
        @staticmethod
        def getVDataChannelSupport(*args, **kwargs):...
        @staticmethod
        def getMapSupport(*args, **kwargs):...
        @staticmethod
        def divideEdge(*args, **kwargs):...
        @staticmethod
        def setFaceSmoothGroup(*args, **kwargs):...
        @staticmethod
        def autosmooth(*args, **kwargs):...
        @staticmethod
        def breakVerts(*args, **kwargs):...
        @staticmethod
        def deleteIsoVerts(*args, **kwargs):...
        @staticmethod
        def getEdgeVerts(*args, **kwargs):...
        @staticmethod
        def getDeadEdges(*args, **kwargs):...
        @staticmethod
        def getNumEdges(*args, **kwargs):...
        @staticmethod
        def getEDataValue(*args, **kwargs):...
        @staticmethod
        def defaultMapFaces(*args, **kwargs):...
        @staticmethod
        def moveEdgesToPlane(*args, **kwargs):...
        @staticmethod
        def makeFacesPlanar(*args, **kwargs):...
        @staticmethod
        def chamferVerts(*args, **kwargs):...
        @staticmethod
        def getVerts(*args, **kwargs):...
        @staticmethod
        def getFacesUsingEdge(*args, **kwargs):...
        @staticmethod
        def setVertFlags(*args, **kwargs):...
        @staticmethod
        def getVDataValue(*args, **kwargs):...
        @staticmethod
        def setNumMapVerts(*args, **kwargs):...
        @staticmethod
        def collapseEdges(*args, **kwargs):...
        @staticmethod
        def getFaceSmoothGroup(*args, **kwargs):...
        @staticmethod
        def collapseVerts(*args, **kwargs):...
        @staticmethod
        def forceSubdivision(*args, **kwargs):...
        @staticmethod
        def getEdgeFaces(*args, **kwargs):...
        @staticmethod
        def getDeadFaces(*args, **kwargs):...
        @staticmethod
        def getNumFaces(*args, **kwargs):...
        @staticmethod
        def setEDataValue(*args, **kwargs):...
        @staticmethod
        def applyUVWMap(*args, **kwargs):...
        @staticmethod
        def createShape(*args, **kwargs):...
        @staticmethod
        def moveFacesToPlane(*args, **kwargs):...
        @staticmethod
        def getFaceMatID(*args, **kwargs):...
        @staticmethod
        def setVert(*args, **kwargs):...
        @staticmethod
        def getSafeFaceCenter(*args, **kwargs):...
        @staticmethod
        def getVertsUsingFace(*args, **kwargs):...
        @staticmethod
        def getEdgesByFlag(*args, **kwargs):...
        @staticmethod
        def getVertSelection(*args, **kwargs):...
        @staticmethod
        def checkTriangulation(*args, **kwargs):...
        @staticmethod
        def setVDataValue(*args, **kwargs):...
        @staticmethod
        def getNumMapVerts(*args, **kwargs):...
        @staticmethod
        def splitEdges(*args, **kwargs):...
        @staticmethod
        def divideFace(*args, **kwargs):...
        @staticmethod
        def meshSmoothByVert(*args, **kwargs):...
        @staticmethod
        def propagateFlags(*args, **kwargs):...
        @staticmethod
        def getEdgesVerts(*args, **kwargs):...
        @staticmethod
        def getHasDeadStructs(*args, **kwargs):...
        @staticmethod
        def getHiddenVerts(*args, **kwargs):...
        @staticmethod
        def freeEData(*args, **kwargs):...
        @staticmethod
        def getVertsByColor(*args, **kwargs):...
        @staticmethod
        def getEdgeVis(*args, **kwargs):...
        @staticmethod
        def extrudeFaces(*args, **kwargs):...
        @staticmethod
        def getFacesMatID(*args, **kwargs):...
        @staticmethod
        def moveVert(*args, **kwargs):...
        @staticmethod
        def getFaceNormal(*args, **kwargs):...
        @staticmethod
        def getEdgesUsingFace(*args, **kwargs):...
        @staticmethod
        def getEdgeFlags(*args, **kwargs):...
        @staticmethod
        def setVertSelection(*args, **kwargs):...
        @staticmethod
        def freeVData(*args, **kwargs):...
        @staticmethod
        def setNumMapFaces(*args, **kwargs):...
        @staticmethod
        def meshSmoothByEdge(*args, **kwargs):...
        @staticmethod
        def slice(*args, **kwargs):...
        @staticmethod
        def collapseFaces(*args, **kwargs):...
        @staticmethod
        def tessellateByVert(*args, **kwargs):...
        @staticmethod
        def fillInMesh(*args, **kwargs):...
        @staticmethod
        def getEdgesFaces(*args, **kwargs):...
        @staticmethod
        def isFaceDead(*args, **kwargs):...
        @staticmethod
        def setHiddenVerts(*args, **kwargs):...
        @staticmethod
        def resetEData(*args, **kwargs):...
        @staticmethod
        def setFaceColor(*args, **kwargs):...
        @staticmethod
        def setEdgeVis(*args, **kwargs):...
        @staticmethod
        def bevelFaces(*args, **kwargs):...
        @staticmethod
        def setFaceMatID(*args, **kwargs):...
        @staticmethod
        def deleteVerts(*args, **kwargs):...
        @staticmethod
        def getFaceArea(*args, **kwargs):...
        @staticmethod
        def getElementsUsingFace(*args, **kwargs):...
        @staticmethod
        def setEdgeFlags(*args, **kwargs):...
        @staticmethod
        def getEdgeSelection(*args, **kwargs):...
        @staticmethod
        def resetVData(*args, **kwargs):...
        @staticmethod
        def getNumMapFaces(*args, **kwargs):...
        @staticmethod
        def tessellateByEdge(*args, **kwargs):...
        @staticmethod
        def meshSmoothByFace(*args, **kwargs):...
        @staticmethod
        def detachVerts(*args, **kwargs):...
        @staticmethod
        def resetSlicePlane(*args, **kwargs):...
        @staticmethod
        def isEdgeDead(*args, **kwargs):...
        @staticmethod
        def getHiddenFaces(*args, **kwargs):...
        @staticmethod
        def setVertColor(*args, **kwargs):...
        @staticmethod
        def chamferEdges(*args, **kwargs):...
        @staticmethod
        def deleteEdges(*args, **kwargs):...
        @staticmethod
        def retriangulate(*args, **kwargs):...
        @staticmethod
        def deleteFaces(*args, **kwargs):...
        @staticmethod
        def weldVertsByThreshold(*args, **kwargs):...
        @staticmethod
        def getFacesByMatId(*args, **kwargs):...
        @staticmethod
        def getVertsUsedOnlyByFaces(*args, **kwargs):...
        @staticmethod
        def getFacesByFlag(*args, **kwargs):...
        @staticmethod
        def setEdgeSelection(*args, **kwargs):...
        @staticmethod
        def setNumEDataChannels(*args, **kwargs):...
        @staticmethod
        def setMapVert(*args, **kwargs):...
        @staticmethod
        def detachEdges(*args, **kwargs):...
        @staticmethod
        def tessellateByFace(*args, **kwargs):...
        @staticmethod
        def cutVert(*args, **kwargs):...
        @staticmethod
        def getSlicePlane(*args, **kwargs):...
        @staticmethod
        def getFaceEdges(*args, **kwargs):...
        @staticmethod
        def isVertDead(*args, **kwargs):...
        @staticmethod
        def setHiddenFaces(*args, **kwargs):...
        @staticmethod
        def setNumVDataChannels(*args, **kwargs):...
        @staticmethod
        def setNumMaps(*args, **kwargs):...
        @staticmethod
        def createEdge(*args, **kwargs):...
        @staticmethod
        def setDiagonal(*args, **kwargs):...
        @staticmethod
        def flipNormals(*args, **kwargs):...
        @staticmethod
        def weldVerts(*args, **kwargs):...
        @staticmethod
        def getAllFaces(*args, **kwargs):...
        @staticmethod
        def isMeshFilledIn(*args, **kwargs):...
        @staticmethod
        def getFaceFlags(*args, **kwargs):...
        @staticmethod
        def getFaceSelection(*args, **kwargs):...
        @staticmethod
        def getNumEDataChannels(*args, **kwargs):...
        @staticmethod
        def getMapVert(*args, **kwargs):...
        @staticmethod
        def cutEdge(*args, **kwargs):...
        @staticmethod
        def detachFaces(*args, **kwargs):...
        @staticmethod
        def capHolesByVert(*args, **kwargs):...
        @staticmethod
        def setSlicePlane(*args, **kwargs):...
        @staticmethod
        def getFacesVerts(*args, **kwargs):...
        @staticmethod
        def getEdgesUsingVert(*args, **kwargs):...
        @staticmethod
        def getOpenEdges(*args, **kwargs):...
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
                       zAxis: runtime.Point3) -> runtime.BoneGeometry: ...
    class controller: ...
    
    class Quat: ...

    class Matrix3(Value):
        """
        [2022 api link](https://help.autodesk.com/view/MAXDEV/2022/ENU/?guid=GUID-D77C780A-4E8A-4528-949F-CC09AAE048DA)
        """
        rotationpart: runtime.Quat
        """ read-only """
        translationpart: runtime.Point3
        """ read-only """
        scalerotationpart: runtime.Point3
        """ read-only 이동을 제외한 회전과 크기값 """
        scalepart: runtime.Point3
        """ read-only """

        rotation: runtime.Quat
        """ 회전값 """
        position: runtime.Point3

        row1: runtime.Point3
        row2: runtime.Point3
        row3: runtime.Point3
        row4: runtime.Point3
        translation: runtime.Point3
        determinantsign: int
        """ 행렬의 행렬식의 부호를 반환합니다. 기본1 이네,"""
        @overload
        def __init__(self) -> None: ...
        
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
        @overload
        def __init__(self,
                     row1:list[float|int],
                     row2:list[float|int],
                     row3:list[float|int],
                     row4:list[float|int],
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
    def maxVersion() -> list[int| str]:
        """:return: #(25000, 62, 0, 25, 2, 2, 3312, 2023, ".2.2 Update")
            - 25000: 릴리스 번호
            - 62: API버전
            - 0: SDK 개정판
            - 25: 주요 버전
            - 업데이트 버전
            - 핫픽스 번호
            - 빌드 번호
            - 연도
            - 버전 설명
        :rtype: list[int]
        [wep api](https://help.autodesk.com/view/MAXDEV/2024/ENU/?guid=GUID-53F8D6CE-A5A6-4353-BE48-4298BBE107DE)
        """;...

    @staticmethod
    def addModifier(*args, **kwargs) -> None: ...
    @staticmethod
    def getSubAnim(*args, **kwargs) -> Any: ...
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
    def classOf(obj: _T) -> type[_T]: ...
    @staticmethod
    def setSelectionLevel(obj: runtime.node, level: Name):
        """
        :type level: literal[#object, #vertex, #edge, #face]
        """
    @staticmethod
    def close_enough(arg1: float, arg2: float, arg3:int):
        """
        :param arg1: 비교대상1
        :param arg2: 비교대상2
        :param arg3: 오차 보간기준, 기본10을 추천
        :return: bool
        """
        ...
    @staticmethod
    def MatchPattern(arg1: str, pattern: str , ignoreCase:bool=False) -> bool:
        """ [help](https://help.autodesk.com/view/MAXDEV/2024/ENU/?guid=GUID-A6A60FC7-6206-4FFC-80E2-0EF8544BE2C4)
        :param arg1: 검사할 문자열
        :param pattern: 패턴
        :param ignoreCase: 대소문자 구분 여부, 기본값은 False
        :return: 매칭됨
        """
        ...
    @staticmethod
    def queryBox(arg1: str, title="MAXScript", beep=True,
        icon: runtime.Name = ...,
        defaultButton: int=1, dontShowAgain: Any=..., helpID: int=...,
        showHoldButton=..., parent: int=..., extraFlags:int=...
    ):
        """[help](https://help.autodesk.com/view/MAXDEV/2024/ENU/?guid=GUID-7A4AA91A-0DEB-470B-AD6B-2E7A3A105BD0)
        :param icon: #question|#information|#warning|#critical
        :param parent: parent HWND, 기본값 3ds Max window임 -1은 임의
        :param extraFlags: 추가 플래그, 
            0x00002000L - MB_TASKMODAL
            0x00001000L - MB_SYSTEMMODAL
            0x00008000L - MB_NOFOCUS
            0x00010000L - MB_SETFOREGROUND
            0x00040000L - MB_TOPMOST
            0x00080000L - MB_RIGHT
            0x00100000L - MB_RTLREADING
            0x10000000L - show dialog using win32 MessageBox()
            0x40000000L - show dialog using MaxMessageBox hwnd parent version

        """
    @staticmethod
    def setINISetting(arg1: str, arg2: str, arg3: str, arg4: str) -> None:
        """[api](https://help.autodesk.com/view/MAXDEV/2024/ENU/)
        :param arg1: file_path
        :param arg2: section
        :param arg3: key
        :param arg4: value
        """
        ...
    @staticmethod
    def DisableSceneRedraw() -> None:...
    @staticmethod
    def EnableSceneRedraw() -> None:...
    @staticmethod
    def substituteString(arg1: str, arg2:str, arg3:str) -> str:
        """[help](https://help.autodesk.com/view/MAXDEV/2024/ENU/?guid=GUID-A6A60FC7-6206-4FFC-80E2-0EF8544BE2C4)
        :param arg1: 원본 문자열
        :param arg2: 찾을 문자열
        :param arg3: 대체할 문자열
        :return: 대체된 원본 문자열
        """
        ...
    @staticmethod
    @overload
    def setTransformLockFlags(arg1: Sequence[_T], arg2: runtime.Name):
        """
        :param arg1: node or list of nodes
        :param arg2: transform lock flags, [#none, #all]
        """
        ...
    @staticmethod
    @overload
    def setTransformLockFlags(arg1: node, arg2: runtime.Name):
        """
        :param arg1: node or list of nodes
        :param arg2: transform lock flags, [#none, #all]
        """
        ...
    @staticmethod
    def ForceCompleteRedraw(doDisabled: bool) -> None:
        """[3dsMaxHelp](https://help.autodesk.com/view/MAXDEV/2024/ENU/?guid=GUID-52E2EA19-D42C-4240-A061-CB0DC364267E)
        이 방법을 모두 사용하면 모든 뷰포트가 완전히 다시 그려집니다. 이 방법은 문자 그대로 모든 것 (모든 개체, 모든 화면 직사각형, 모든보기)이 유효하지 않은 것으로 표시되고 전체 장면이 재생되도록합니다. 그러나 개별 개체 파이프라인 캐시는 플러시되지 않습니다. 이 루틴은 느리다는 보장이 있습니다.

        :param doDisabled: true이면 비활성화된 뷰포트도 다시 그려집니다.
        """
        ...
    @staticmethod
    def selectmore(nodes: Any) -> None:...
    @staticmethod
    def selectMore(nodes: Any) -> None:...
    @staticmethod
    def deselect(nodes: Any) -> None:...
    @staticmethod
    def getKey(*args: Any, **kwargs: Any) -> runtime.MAXKey:
        """ [help](https://help.autodesk.com/view/MAXDEV/2024/ENU/?guid=GUID-3DEAA5D4-FEF9-40B8-99C0-C92A8769A117)"""
        ...
    @staticmethod
    def addNewKey(*args: Any, **kwargs: Any) -> runtime.MAXKey:
        """ [help](https://help.autodesk.com/view/MAXDEV/2024/ENU/?guid=GUID-3DEAA5D4-FEF9-40B8-99C0-C92A8769A117)"""
    @staticmethod
    def isProperty(obj:Any, prop: str) -> TypeGuard[bool]:
        """[help](https://help.autodesk.com/view/MAXDEV/2024/ENU/?guid=GUID-879ECFAD-7928-44B3-BCD7-276D53C89B52#isproperty)
        :param obj: object
        :param prop: property name
        :return: True if the object has the property, False otherwise
        """
        ...
    @staticmethod
    def ScaleMatrix(scale: runtime.Point3) -> runtime.Matrix3:
        """[help](https://help.autodesk.com/view/MAXDEV/2024/ENU/?guid=GUID-D77C780A-4E8A-4528-949F-CC09AAE048DA)
        :param scale: scaling factors for x, y, z axes
        :return: scaling matrix
        """
        ...
    @staticmethod
    def save(arg1):...
    @staticmethod
    def getNumNamedSelSets() -> int:...
    @staticmethod
    def getNamedSelSetName(index: int) -> str:...
    @staticmethod
    def clearSelection() -> None:...
    @staticmethod
    def normTime(arg1: float) -> runtime.Time:
        """animationRange의 범위를 1.0으로 정규화했을때 프레임값"""
        ...
    @staticmethod
    def exportFile(
        fileName: str,
        prompt: runtime.Name = runtime.Name("Prompt"),
        selectedOnly: bool = False,
        using: type[runtime.ExporterPlugin] = ...,
    ) -> None:
        """[help](https://help.autodesk.com/view/MAXDEV/2024/ENU/?guid=GUID-3DEAA5D4-FEF9-40B8-99C0-C92A8769A117)
        :param fileName: 파일 이름
        :param prompt: Literal["#Prompt", "#noPrompt"] - 사용자에게 파일 이름을 묻는지 여부
        :type prompt: runtime.Name
        :param selected: 선택된 객체만 내보낼지 여부
        :param using: 익스포트 종류
        """
        ...
    @staticmethod
    def nodeLocalBoundingBox(obj, asBox3: bool = ...) -> tuple[runtime.Point3, runtime.Point3]:
        """[help](https://help.autodesk.com/view/MAXDEV/2024/ENU/?guid=GUID-A8BF79D1-FAEE-413E-B552-3E486DA21EC3)
        :param obj: node
        :param asBox3: ????차이가 없는데
        :return: (Point3, Point3)
        """
        ...
    @staticmethod
    def fetchMaxFile(quiet: bool = False) -> None:
        """[help](...)
        holde로 임시저장된 Max 파일을 불러옵니다.

        :param quiet: True이면 사용자에게 알리지 않습니다.
        """
        ...
    @staticmethod
    def holdMaxFile():
        """[help](...)
        현재 열려 있는 Max 파일을 임시로 저장합니다.
        """
        ...
    @staticmethod
    def selectKeys(ctrl: runtime.controller) -> None:
        """[help](...)
        :param ctrl: 컨트롤러
        컨트롤러의 키들을 선택합니다.
        """
        ...
    @staticmethod
    def deselectKeys(ctrl: runtime.controller, range: runtime.Interval) -> None:
        """[help](...)
        :param ctrl: 컨트롤러
        :param range: 범위
        범위의 키들을 선택에서 제외합니다.
        """
        ...
    @staticmethod
    def deleteKeys(ctrl: runtime.controller, target: runtime.Name) -> None:
        """[help](https://help.autodesk.com/view/MAXDEV/2024/ENU/?guid=GUID-B1700B1D-B1EA-4A6C-B4A3-A29DB26C8C02)
        :param ctrl: 컨트롤러
        :param target: 키 타입 Literal[#allKeys | #selection]
        범위의 키들을 삭제합니다.
        """
        ...
    @staticmethod
    def deleteFile(fileName: str) -> None:
        """[help](...)
        :param fileName: 파일 이름
        파일을 삭제합니다.
        """
        ...
    @staticmethod
    def FBXImporterSetParam(
        param: str,
        value: str | int | float | bool | None = None,
    ) -> None:
        """[help]()
        fbx임포트 설정
        :param param: 파라미터 이름
        :param value: 파라미터 값
        """
        ...

    @staticmethod
    def SetQuietMode(bool):
        """조용한 모드 설정
        :param bool: True이면 조용한 모드로 설정
        """
        ...

    @staticmethod
    def getLastMergedNodes() -> list[runtime.node]:
        """ (열려 있는 신에서) 최근 병합된 노드 가져오기
        """
        ...
    @staticmethod
    def render(*args, **kwargs):
        """ 렌더링 실행
        https://help.autodesk.com/view/MAXDEV/2024/ENU/?guid=GUID-5984208E-B730-44F2-8D15-D4BB350F5877
        """
        ...
    @staticmethod
    def formattedPrint(*args, **kwargs):
        """ 포맷된 출력
        https://help.autodesk.com/view/MAXDEV/2024/ENU/?guid=GUID-19874C74-DEE5-4BCD-A5FD-4F0F51EB3451
        """
        ...
    @staticmethod
    def unRegisterTimeCallback(fn):
        """시간 콜백 등록 해제
        :param fn: 콜백 함수
        """
        ...
    @staticmethod
    def registerTimeCallback(fn):
        """시간 콜백 등록
        :param fn: 콜백 함수
        """
        ...