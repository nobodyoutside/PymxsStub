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

    class Value: ...
    class BitArray(Value): ...
    class StructDef(Value): ...
    class windows: ...
    class Name(mxs.Name): ...

    class vertexColorType(mxs.Name):
        color: Type[mxs.Name]
        illum: Type[mxs.Name]
        alpha: Type[mxs.Name]
        color_plus_illum: Type[mxs.Name]
        ...

    class MAXWrapper(Value): ...

    class node(MAXWrapper):
        """[Node : MAXWrapper](https://help.autodesk.com/view/MAXDEV/2023/ENU/?guid=GUID-1C9953AA-4750-4147-91DC-127AF2F7BC87)
        [Interface : INode](https://help.autodesk.com/view/MAXDEV/2023/ENU/?guid=GUID-0BFEF796-5952-48B0-8929-88475F927649)
        """

        name: str
        ...

    class GeometryClass(node):
        mesh: runtime.TriMesh
        ...

    class Sphere(runtime.GeometryClass):
        radius: float
        ...

    class TriMesh(Value): ...
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

    class LayerManager(mxs.LayerManager):
        @staticmethod
        def getLayerFromName(*args, **kwargs) -> runtime.Layer: ...
        ...

    class NodeGeneric(Value): ...
    class Generic(Value): ...

    class getnumtverts(Generic):
        """-> int"""

        def __new__(cls, node) -> int: ...

    class convertToMesh(NodeGeneric):
        def __new__(cls, node) -> None: ...

    class Skin(mxs.Skin): ...

    class meshop(StructDef):
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
