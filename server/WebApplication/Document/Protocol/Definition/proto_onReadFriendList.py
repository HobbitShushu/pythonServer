# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Definition

import flatbuffers

class proto_onReadFriendList(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsproto_onReadFriendList(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = proto_onReadFriendList()
        x.Init(buf, n + offset)
        return x

    # proto_onReadFriendList
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # proto_onReadFriendList
    def FriendList(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .proto_userInfo import proto_userInfo
            obj = proto_userInfo()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # proto_onReadFriendList
    def FriendListLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def proto_onReadFriendListStart(builder): builder.StartObject(1)
def proto_onReadFriendListAddFriendList(builder, friendList): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(friendList), 0)
def proto_onReadFriendListStartFriendListVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def proto_onReadFriendListEnd(builder): return builder.EndObject()
