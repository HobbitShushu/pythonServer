# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Definition

import flatbuffers

class proto_userInfo(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsproto_userInfo(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = proto_userInfo()
        x.Init(buf, n + offset)
        return x

    # proto_userInfo
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # proto_userInfo
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # proto_userInfo
    def RegistDate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def proto_userInfoStart(builder): builder.StartObject(2)
def proto_userInfoAddName(builder, name): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)
def proto_userInfoAddRegistDate(builder, registDate): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(registDate), 0)
def proto_userInfoEnd(builder): return builder.EndObject()