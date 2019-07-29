# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Definition

import flatbuffers

class proto_onReadCharacters(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsproto_onReadCharacters(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = proto_onReadCharacters()
        x.Init(buf, n + offset)
        return x

    # proto_onReadCharacters
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # proto_onReadCharacters
    def Characters(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 32
            from .proto_characterInfo import proto_characterInfo
            obj = proto_characterInfo()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # proto_onReadCharacters
    def CharactersLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def proto_onReadCharactersStart(builder): builder.StartObject(1)
def proto_onReadCharactersAddCharacters(builder, characters): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(characters), 0)
def proto_onReadCharactersStartCharactersVector(builder, numElems): return builder.StartVector(32, numElems, 4)
def proto_onReadCharactersEnd(builder): return builder.EndObject()