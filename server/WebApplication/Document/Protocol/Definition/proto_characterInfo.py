# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Definition

import flatbuffers

class proto_characterInfo(object):
    __slots__ = ['_tab']

    # proto_characterInfo
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # proto_characterInfo
    def Chracteridx(self): return self._tab.Get(flatbuffers.number_types.Uint32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(0))
    # proto_characterInfo
    def Grade(self): return self._tab.Get(flatbuffers.number_types.Uint32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(4))
    # proto_characterInfo
    def Level(self): return self._tab.Get(flatbuffers.number_types.Uint32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(8))
    # proto_characterInfo
    def Exp(self): return self._tab.Get(flatbuffers.number_types.Uint32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(12))
    # proto_characterInfo
    def Awaken(self): return self._tab.Get(flatbuffers.number_types.Uint32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(16))
    # proto_characterInfo
    def SoulWeapon(self): return self._tab.Get(flatbuffers.number_types.Uint32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(20))
    # proto_characterInfo
    def SoulArmor(self): return self._tab.Get(flatbuffers.number_types.Uint32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(24))
    # proto_characterInfo
    def SoulTreasure(self): return self._tab.Get(flatbuffers.number_types.Uint32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(28))

def Createproto_characterInfo(builder, chracteridx, grade, level, exp, awaken, soulWeapon, soulArmor, soulTreasure):
    builder.Prep(4, 32)
    builder.PrependUint32(soulTreasure)
    builder.PrependUint32(soulArmor)
    builder.PrependUint32(soulWeapon)
    builder.PrependUint32(awaken)
    builder.PrependUint32(exp)
    builder.PrependUint32(level)
    builder.PrependUint32(grade)
    builder.PrependUint32(chracteridx)
    return builder.Offset()