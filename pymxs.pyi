# flake8: noqa: E701
"""
 수작업으로 필요할때 추가하는 스텁파일
 - 독스티링 적용(독스트링은 상속이 안되기 때문에 여기서 적어야함)
    - 클래스 메소드 설명은 잘 따라옴.
"""
from __future__ import annotations
from typing import Type

import MXSWrapperBase as mxs

class runtime:
    currentTime: int

    class windows: ...
    class Name(mxs.Name): ...

    class vertexColorType(mxs.Name):
        color: Type[mxs.Name]
        illum: Type[mxs.Name]
        alpha: Type[mxs.Name]
        color_plus_illum: Type[mxs.Name]
        ...

    class Node(mxs.Node):
        """
        [2022 api link](https://help.autodesk.com/view/MAXDEV/2022/ENU/?guid=GUID-0BFEF796-5952-48B0-8929-88475F927649)
        """

        ...

    class TriMesh: ...
    class Box3: ...
    class Material: ...

    class Point3(mxs.Point3):
        """[<expr>, <expr>, <expr>]

        [2022 api link](https://help.autodesk.com/view/MAXDEV/2022/ENU/?guid=GUID-1564BD35-50EA-4140-9150-1AECC89F713C)
        """

        def __init__(self, *args, **kwargs) -> None: ...
        ...

    class Color(mxs.Color):
        def __init__(self, *args, **kwargs) -> None: ...

    class Biped(mxs.Biped): ...
    class LayerManager(mxs.LayerManager): ...
    class Skin(mxs.Skin): ...
    class meshOp(mxs.meshOp): ...
    class BoneSys(mxs.BoneSys): ...
    class controller: ...

    class Matrix3(mxs.Matrix3):
        """
        [2022 api link](https://help.autodesk.com/view/MAXDEV/2022/ENU/?guid=GUID-D77C780A-4E8A-4528-949F-CC09AAE048DA)
        """

        ...
    @staticmethod
    def maxVersion(*args, **kwargs) -> list:
        """#(25000, 62, 0, 25, 2, 2, 3312, 2023, ".2.2 Update")"""
        ...
    @staticmethod
    def rotateZ(*args, **kwargs) -> Matrix3: ...
    @staticmethod
    def snapshot(Node) -> mxs.Node: ...
    @staticmethod
    def redrawViews(): ...
    @staticmethod
    def inverse(matrix3: "Matrix3"): ...
    @staticmethod
    def attachObjects(
        pNode: Type[mxs.Node], node: Type[mxs.Node], move=True
    ): ...
    @staticmethod
    def classOf(obj: "mxs.MXSWrapper"): ...
    @staticmethod
    def setSelectionLevel(obj: Node, level: Name):
        """
        parm:
            level: vertex
        """
