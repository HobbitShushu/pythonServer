# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Definition

import flatbuffers

class proto_interest(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsproto_interest(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = proto_interest()
        x.Init(buf, n + offset)
        return x

    # proto_interest
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # proto_interest
    def Title(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # proto_interest
    def Value(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # proto_interest
    def ValueLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def proto_interestStart(builder): builder.StartObject(2)
def proto_interestAddTitle(builder, title): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(title), 0)
def proto_interestAddValue(builder, value): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(value), 0)
def proto_interestStartValueVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def proto_interestEnd(builder): return builder.EndObject()