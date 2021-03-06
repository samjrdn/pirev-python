from .type import A, A_PLUS, A_3_PLUS, ALPHA, B, B_PLUS, B_2, B_3, B_3_PLUS, CM_1, CM_3, CM_3_PLUS, ZERO, ZERO_W
from .memory import GB_1, MB_256, MB_512
from .processor import BCM_2835, BCM_2836, BCM_2837
from .manufacturer import EGOMAN, EMBEST, SONY_JAPAN, SONY_UK, STADIUM

UNKNOWN = 'unknown'

MEMORY_CODE = {
  0x0: MB_256,
  0x1: MB_512,
  0x2: GB_1,
}

def getMemory(code):
  memory = (code >> 20) & 0b111

  if memory in MEMORY_CODE:
    return MEMORY_CODE[memory]
  else:
    return UNKNOWN

MANUFACTURER_CODE = {
  0x0: SONY_UK,
  0x1: EGOMAN,
  0x2: EMBEST,
  0x3: SONY_JAPAN,
  0x4: EMBEST,
  0x5: STADIUM,
}

def getManufacturer(code):
  manufacturer = (code >> 16) & 0b1111

  if manufacturer in MANUFACTURER_CODE:
    return MANUFACTURER_CODE[manufacturer]
  else:
    return UNKNOWN

PROCESSOR_CODE = {
  0x0: BCM_2835,
  0x1: BCM_2836,
  0x2: BCM_2837,
}

def getProcessor(code):
  processor = (code >> 12) & 0b1111

  if processor in PROCESSOR_CODE:
    return PROCESSOR_CODE[processor]
  else:
    return UNKNOWN

TYPE_CODE = {
  0x0: A,
  0x1: B,
  0x2: A_PLUS,
  0x3: B_PLUS,
  0x4: B_2,
  0x5: ALPHA,
  0x6: CM_1,
  0x8: B_3,
  0x9: ZERO,
  0xa: CM_3,
  0xc: ZERO_W,
  0xd: B_3_PLUS,
  0xe: A_3_PLUS,
  0x10: CM_3_PLUS
}

def getType(code):
  type = (code >> 4) & 0b11111111

  if type in TYPE_CODE:
    return TYPE_CODE[type]
  else:
    return UNKNOWN

def getRevision(code):
  return 1 + (code & 0b1111)/10

def newrev(code):
  if isinstance(code, str):
    code = int(code, 16)

  flag = (code >> 23) & 0b1

  if flag != 1:
    return None

  return {
    'type': getType(code),
    'memory': getMemory(code),
    'processor': getProcessor(code),
    'revision': getRevision(code),
    'manufacturer': getManufacturer(code),
  }
