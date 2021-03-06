# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Definition

import flatbuffers

class proto_onReadUserInfo(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsproto_onReadUserInfo(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = proto_onReadUserInfo()
        x.Init(buf, n + offset)
        return x

    # proto_onReadUserInfo
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # proto_onReadUserInfo
    def Username(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # proto_onReadUserInfo
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # proto_onReadUserInfo
    def RegistDate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def proto_onReadUserInfoStart(builder): builder.StartObject(3)
def proto_onReadUserInfoAddUsername(builder, username): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(username), 0)
def proto_onReadUserInfoAddName(builder, name): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)
def proto_onReadUserInfoAddRegistDate(builder, registDate): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(registDate), 0)
def proto_onReadUserInfoEnd(builder): return builder.EndObject()
