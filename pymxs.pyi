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

    class BitArray(Value):
        def __iter__(self) -> runtime.BitArray: ...
        def __next__(self) -> int: ...

    class StructDef(Value): ...
    class windows: ...
    class Name(mxs.Name): ...
    class Primitive(runtime.Value): ...

    @staticmethod
    def resetMaxFile(noPrompt: runtime.Name) -> None: ...
    @staticmethod
    def clearListener() -> None: ...

    class vertexColorType(mxs.Name):
        color: Type[mxs.Name]
        illum: Type[mxs.Name]
        alpha: Type[mxs.Name]
        color_plus_illum: Type[mxs.Name]
        ...
    class setFaceSelection(NodeGeneric):
        def __new__(cls, *args, **kwargs) -> None: ...
    class getFaceSelection(NodeGeneric):
        def __new__(cls, *args, **kwargs) -> runtime.BitArray: ...
    class MAXWrapper(Value): ...
    class FaceSelection(Value): ...
    class node(MAXWrapper):
        """[Node : MAXWrapper](https://help.autodesk.com/view/MAXDEV/2023/ENU/?guid=GUID-1C9953AA-4750-4147-91DC-127AF2F7BC87)
        [Interface : INode](https://help.autodesk.com/view/MAXDEV/2023/ENU/?guid=GUID-0BFEF796-5952-48B0-8929-88475F927649)
        """

        name: str
        ...

    class GeometryClass(node):
        mesh: runtime.TriMesh
        numfaces: int
        ...

    class Sphere(runtime.GeometryClass):
        radius: float
        ...

    class TriMesh(Value):
        def selectedFaces(self) -> runtime.FaceSelection: ...
        ...

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

    subObjectLevel: int

    class convertToMesh(NodeGeneric):
        def __new__(cls, node) -> None: ...

    class Skin(mxs.Skin): ...

    class meshop(StructDef):
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


    class BoneSys(mxs.BoneSys): ...
    class controller: ...

    class Matrix3(mxs.Matrix3):
        """
        [2022 api link](https://help.autodesk.com/view/MAXDEV/2022/ENU/?guid=GUID-D77C780A-4E8A-4528-949F-CC09AAE048DA)
        """

        ...

    class modifier(MAXWrapper):
        """ """

        ...

    class Unwrap_UVW(modifier):
        """https://help.autodesk.com/view/MAXDEV/2023/ENU/?guid=GUID-17D700DC-1FDC-4713-8041-D9E3C3EB4789"""
        class unwrap:
            def __init__(self) -> None: ...
            @classmethod
            def setMapChannel(cls, index: int) -> None: ...
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
    def snapshot(Node) -> mxs.Node: ...
    @staticmethod
    def redrawViews(): ...
    @staticmethod
    def inverse(matrix3: "Matrix3"): ...
    @staticmethod
    def AttachObjects(
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
