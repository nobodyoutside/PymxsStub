# flake8: noqa: E302
"""
runtime에 적용할 베이스 클래스 정보 입력
"""
from __future__ import annotations
from typing import Type, Union, Optional

class Value: ...


class MXSWrapperBase:
    @staticmethod
    def getmxsprop(key: str): ...
    @staticmethod
    def setmxsprop(key: str, value): ...


class MXSWrapper(Value):
    @staticmethod
    def getmxsprop(key: str): ...
    @staticmethod
    def setmxsprop(key: str, value): ...


class Name:
    def __init__(self, string: str):
        self.string = string
    ...

class Quat(MXSWrapper):
    """
    [2022 api link](https://help.autodesk.com/view/MAXDEV/2022/ENU/?guid=GUID-C42F8CCE-CE31-49B4-9D5A-65C07D9F33FD)
    """

    ...

class Point3(MXSWrapper): ...

class Matrix3(MXSWrapper):
    rotation: Quat
    """ 회전값 """
    position: Point3
    row1: Point3
    row2: Point3
    row3: Point3
    row4: Point3
    translation: Point3
    ...

class bitArray(MXSWrapper): ...

class VertexSelection(MXSWrapper):
    """#verts(1 : $Editable_Mesh:Sphere002 @ [0.000000,0.000000,0.000000])"""

    ...

class Controller(MXSWrapper): ...
class TCB_Rotation(MXSWrapper): ...
class meshOp(MXSWrapper): ...
class Color(Point3): ...
class Box3(MXSWrapper): ...
class Material(MXSWrapper): ...
class TriMesh(MXSWrapper): ...

class Node(MXSWrapper):
    transform: Matrix3
    name: str
    baseObject: Node
    parent: Node
    material: Type[Material]
    children: list
    mesh: Type["TriMesh"]
    boundingBox: Type[Box3]
    displayByLayer: bool
    motionByLayer: bool
    renderByLayer: bool
    colorByLayer: bool
    globalIlluminationByLayer: bool
    isTarget: bool
    lookAt: Node
    target: Node
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
    wireColor: Color
    """  """
    showLinks: bool
    showLinksOnly: bool
    showVertexColors: bool
    vertexColorType: Type[Name]
    vertexColorsShaded: bool
    isDependent: bool
    visibility: bool
    controller: Type[Controller]
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
    motionBlurOnController: Type[Controller]
    motionBlur: Type[Name]
    generatecaustics: bool
    rcvcaustics: bool
    generateGlobalIllume: bool
    rcvGlobalIllum: bool
    ...

class CirCle(Node): ...

class Biped(Node):
    @staticmethod
    def getTransform(node: Node, name: Name) -> Union[Point3, Quat]:
        """
        name:
            - #pos -> :func:`Point3()`
            - #rot -> Quat
        """
        result = None
        if name == Name("pos"):
            result: Point3
        if name == Name("rot"):
            result: Quat
        return result
        ...
    @staticmethod
    def addNewKey(ctrl, time, type): ...

class LayerProperties(MXSWrapper): ...

class LayerManager(MXSWrapper):
    count: int
    current: LayerProperties
    ...

class Modifier(MXSWrapper): ...
class Editable_Mesh(Modifier): ...
class Skin(Modifier): ...

class skinOps:
    @staticmethod
    def GetNumberVertices(modifier: Type[Modifier]): ...
    @staticmethod
    def getSelectedVertices(wrapNodeIndex: int) -> bitArray: ...

class modPanel:
    @staticmethod
    def getCurrentObject() -> Modifier: ...
    ...

class logsystem:
    def getNetLogFileName() -> str:
        """현제 입력중인 로그 파일 경로를 출력."""
        ...
    def logEntry(message_text, type_name):
        """
        param:
            type_name: #error, #warning, #info, #debug

        api: https://help.autodesk.com/view/MAXDEV/2023/ENU/?guid=GUID-930627BF-AC41-4033-9768-64CC5A1CE684
        """
        ...

class BoneSys:
    def createBone(x: Point3, y: Point3, z: Point3) -> Node: ...
    ...
