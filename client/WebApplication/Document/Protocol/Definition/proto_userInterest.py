# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Definition

import flatbuffers

class proto_userInterest(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsproto_userInterest(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = proto_userInterest()
        x.Init(buf, n + offset)
        return x

    # proto_userInterest
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # proto_userInterest
    def Useridx(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # proto_userInterest
    def Username(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # proto_userInterest
    def Interest(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .proto_interest import proto_interest
            obj = proto_interest()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # proto_userInterest
    def InterestLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def proto_userInterestStart(builder): builder.StartObject(3)
def proto_userInterestAddUseridx(builder, useridx): builder.PrependUint32Slot(0, useridx, 0)
def proto_userInterestAddUsername(builder, username): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(username), 0)
def proto_userInterestAddInterest(builder, interest): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(interest), 0)
def proto_userInterestStartInterestVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def proto_userInterestEnd(builder): return builder.EndObject()
