"""
runtime에 적용할 베이스 클래스 정보 입력
"""
from typing import Type, Union

class MXSWrapperBase:
    @staticmethod
    def getmxsprop(key: str): ...
    @staticmethod
    def setmxsprop(key: str, value): ...

class MXSWrapper(MXSWrapperBase): ...

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

class TCB_Rotation(MXSWrapper): ...
class meshOp(MXSWrapper): ...

class Node(MXSWrapper):
    baseObject: MXSWrapper
    transform: Matrix3
    controller: any
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
    def addNewKey(ctrl, time, type):
        ...

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
