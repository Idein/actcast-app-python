import enum


class V4L2_CTRL_CLASS(enum.IntEnum):
    USER = 0x00980000
    MPEG = 0x00990000
    CAMERA = 0x009a0000
    FM_TX = 0x009b0000
    FLASH = 0x009c0000
    JPEG = 0x009d0000
    IMAGE_SOURCE = 0x009e0000
    IMAGE_PROC = 0x009f0000
    DV = 0x00a00000
    FM_RX = 0x00a10000
    RF_TUNER = 0x00a20000
    DETECT = 0x00a30000


class V4L2_CID(enum.IntEnum):
    BASE = (V4L2_CTRL_CLASS.USER | 0x900)
    USER_BASE = BASE
    USER_CLASS = (V4L2_CTRL_CLASS.USER | 1)
    BRIGHTNESS = (BASE+0)
    CONTRAST = (BASE+1)
    SATURATION = (BASE+2)
    HUE = (BASE+3)

    AUDIO_VOLUME = (BASE+5)
    AUDIO_BALANCE = (BASE+6)
    AUDIO_BASS = (BASE+7)
    AUDIO_TREBLE = (BASE+8)
    AUDIO_MUTE = (BASE+9)
    AUDIO_LOUDNESS = (BASE+10)

    BLACK_LEVEL = (BASE+11)
    AUTO_WHITE_BALANCE = (BASE+12)
    DO_WHITE_BALANCE = (BASE+13)
    RED_BALANCE = (BASE+14)
    BLUE_BALANCE = (BASE+15)
    GAMMA = (BASE+16)
    WHITENESS = (GAMMA)
    EXPOSURE = (BASE+17)
    AUTOGAIN = (BASE+18)
    GAIN = (BASE+19)
    HFLIP = (BASE+20)
    VFLIP = (BASE+21)
    POWER_LINE_FREQUENCY = (BASE+24)
    HUE_AUTO = (BASE+25)
    WHITE_BALANCE_TEMPERATURE = (BASE+26)
    SHARPNESS = (BASE+27)
    BACKLIGHT_COMPENSATION = (BASE+28)
    CHROMA_AGC = (BASE+29)
    COLOR_KILLER = (BASE+30)
    COLORFX = (BASE+31)
    AUTOBRIGHTNESS = (BASE+32)
    BAND_STOP_FILTER = (BASE+33)
    ROTATE = (BASE+34)
    BG_COLOR = (BASE+35)
    CHROMA_GAIN = (BASE+36)
    ILLUMINATORS_1 = (BASE+37)
    ILLUMINATORS_2 = (BASE+38)
    MIN_BUFFERS_FOR_CAPTURE = (BASE+39)
    MIN_BUFFERS_FOR_OUTPUT = (BASE+40)
    ALPHA_COMPONENT = (BASE+41)
    COLORFX_CBCR = (BASE+42)
    LASTP1 = (BASE+43)

    USER_MEYE_BASE = (USER_BASE + 0x1000)
    USER_BTTV_BASE = (USER_BASE + 0x1010)
    USER_S2255_BASE = (USER_BASE + 0x1030)
    USER_SI476X_BASE = (USER_BASE + 0x1040)
    USER_TI_VPE_BASE = (USER_BASE + 0x1050)
    USER_SAA7134_BASE = (USER_BASE + 0x1060)
    USER_ADV7180_BASE = (USER_BASE + 0x1070)
    USER_TC358743_BASE = (USER_BASE + 0x1080)

    MPEG_BASE = (V4L2_CTRL_CLASS.MPEG | 0x900)
    MPEG_CLASS = (V4L2_CTRL_CLASS.MPEG | 1)

    MPEG_STREAM_TYPE = (MPEG_BASE+0)
    MPEG_STREAM_PID_PMT = (MPEG_BASE+1)
    MPEG_STREAM_PID_AUDIO = (MPEG_BASE+2)
    MPEG_STREAM_PID_VIDEO = (MPEG_BASE+3)
    MPEG_STREAM_PID_PCR = (MPEG_BASE+4)
    MPEG_STREAM_PES_ID_AUDIO = (MPEG_BASE+5)
    MPEG_STREAM_PES_ID_VIDEO = (MPEG_BASE+6)
    MPEG_STREAM_VBI_FMT = (MPEG_BASE+7)

    MPEG_AUDIO_SAMPLING_FREQ = (MPEG_BASE+100)
    MPEG_AUDIO_ENCODING = (MPEG_BASE+101)
    MPEG_AUDIO_L1_BITRATE = (MPEG_BASE+102)
    MPEG_AUDIO_L2_BITRATE = (MPEG_BASE+103)
    MPEG_AUDIO_L3_BITRATE = (MPEG_BASE+104)
    MPEG_AUDIO_MODE = (MPEG_BASE+105)
    MPEG_AUDIO_MODE_EXTENSION = (MPEG_BASE+106)
    MPEG_AUDIO_EMPHASIS = (MPEG_BASE+107)
    MPEG_AUDIO_CRC = (MPEG_BASE+108)
    MPEG_AUDIO_MUTE = (MPEG_BASE+109)
    MPEG_AUDIO_AAC_BITRATE = (MPEG_BASE+110)
    MPEG_AUDIO_AC3_BITRATE = (MPEG_BASE+111)
    MPEG_AUDIO_DEC_PLAYBACK = (MPEG_BASE+112)
    MPEG_AUDIO_DEC_MULTILINGUAL_PLAYBACK = (MPEG_BASE+113)

    MPEG_VIDEO_ENCODING = (MPEG_BASE+200)
    MPEG_VIDEO_ASPECT = (MPEG_BASE+201)
    MPEG_VIDEO_B_FRAMES = (MPEG_BASE+202)
    MPEG_VIDEO_GOP_SIZE = (MPEG_BASE+203)
    MPEG_VIDEO_GOP_CLOSURE = (MPEG_BASE+204)
    MPEG_VIDEO_PULLDOWN = (MPEG_BASE+205)
    MPEG_VIDEO_BITRATE_MODE = (MPEG_BASE+206)
    MPEG_VIDEO_BITRATE = (MPEG_BASE+207)
    MPEG_VIDEO_BITRATE_PEAK = (MPEG_BASE+208)
    MPEG_VIDEO_TEMPORAL_DECIMATION = (MPEG_BASE+209)
    MPEG_VIDEO_MUTE = (MPEG_BASE+210)
    MPEG_VIDEO_MUTE_YUV = (MPEG_BASE+211)
    MPEG_VIDEO_DECODER_SLICE_INTERFACE = (MPEG_BASE+212)
    MPEG_VIDEO_DECODER_MPEG4_DEBLOCK_FILTER = (MPEG_BASE+213)
    MPEG_VIDEO_CYCLIC_INTRA_REFRESH_MB = (MPEG_BASE+214)
    MPEG_VIDEO_FRAME_RC_ENABLE = (MPEG_BASE+215)
    MPEG_VIDEO_HEADER_MODE = (MPEG_BASE+216)
    MPEG_VIDEO_MAX_REF_PIC = (MPEG_BASE+217)
    MPEG_VIDEO_MB_RC_ENABLE = (MPEG_BASE+218)
    MPEG_VIDEO_MULTI_SLICE_MAX_BYTES = (MPEG_BASE+219)
    MPEG_VIDEO_MULTI_SLICE_MAX_MB = (MPEG_BASE+220)
    MPEG_VIDEO_MULTI_SLICE_MODE = (MPEG_BASE+221)
    MPEG_VIDEO_VBV_SIZE = (MPEG_BASE+222)
    MPEG_VIDEO_DEC_PTS = (MPEG_BASE+223)
    MPEG_VIDEO_DEC_FRAME = (MPEG_BASE+224)
    MPEG_VIDEO_VBV_DELAY = (MPEG_BASE+225)
    MPEG_VIDEO_REPEAT_SEQ_HEADER = (MPEG_BASE+226)
    MPEG_VIDEO_MV_H_SEARCH_RANGE = (MPEG_BASE+227)
    MPEG_VIDEO_MV_V_SEARCH_RANGE = (MPEG_BASE+228)

    MPEG_VIDEO_FORCE_KEY_FRAME = (MPEG_BASE+229)
    MPEG_VIDEO_H263_I_FRAME_QP = (MPEG_BASE+300)
    MPEG_VIDEO_H263_P_FRAME_QP = (MPEG_BASE+301)
    MPEG_VIDEO_H263_B_FRAME_QP = (MPEG_BASE+302)
    MPEG_VIDEO_H263_MIN_QP = (MPEG_BASE+303)
    MPEG_VIDEO_H263_MAX_QP = (MPEG_BASE+304)
    MPEG_VIDEO_H264_I_FRAME_QP = (MPEG_BASE+350)
    MPEG_VIDEO_H264_P_FRAME_QP = (MPEG_BASE+351)
    MPEG_VIDEO_H264_B_FRAME_QP = (MPEG_BASE+352)
    MPEG_VIDEO_H264_MIN_QP = (MPEG_BASE+353)
    MPEG_VIDEO_H264_MAX_QP = (MPEG_BASE+354)
    MPEG_VIDEO_H264_8X8_TRANSFORM = (MPEG_BASE+355)
    MPEG_VIDEO_H264_CPB_SIZE = (MPEG_BASE+356)
    MPEG_VIDEO_H264_ENTROPY_MODE = (MPEG_BASE+357)
    MPEG_VIDEO_H264_I_PERIOD = (MPEG_BASE+358)
    MPEG_VIDEO_H264_LEVEL = (MPEG_BASE+359)
    MPEG_VIDEO_H264_LOOP_FILTER_ALPHA = (MPEG_BASE+360)
    MPEG_VIDEO_H264_LOOP_FILTER_BETA = (MPEG_BASE+361)
    MPEG_VIDEO_H264_LOOP_FILTER_MODE = (MPEG_BASE+362)
    MPEG_VIDEO_H264_PROFILE = (MPEG_BASE+363)
    MPEG_VIDEO_H264_VUI_EXT_SAR_HEIGHT = (MPEG_BASE+364)
    MPEG_VIDEO_H264_VUI_EXT_SAR_WIDTH = (MPEG_BASE+365)
    MPEG_VIDEO_H264_VUI_SAR_ENABLE = (MPEG_BASE+366)
    MPEG_VIDEO_H264_VUI_SAR_IDC = (MPEG_BASE+367)
    MPEG_VIDEO_H264_SEI_FRAME_PACKING = (MPEG_BASE+368)
    MPEG_VIDEO_H264_SEI_FP_CURRENT_FRAME_0 = (MPEG_BASE+369)
    MPEG_VIDEO_H264_SEI_FP_ARRANGEMENT_TYPE = (MPEG_BASE+370)
    MPEG_VIDEO_H264_FMO = (MPEG_BASE+371)
    MPEG_VIDEO_H264_FMO_MAP_TYPE = (MPEG_BASE+372)
    MPEG_VIDEO_H264_FMO_SLICE_GROUP = (MPEG_BASE+373)
    MPEG_VIDEO_H264_FMO_CHANGE_DIRECTION = (MPEG_BASE+374)
    MPEG_VIDEO_H264_FMO_CHANGE_RATE = (MPEG_BASE+375)
    MPEG_VIDEO_H264_FMO_RUN_LENGTH = (MPEG_BASE+376)
    MPEG_VIDEO_H264_ASO = (MPEG_BASE+377)
    MPEG_VIDEO_H264_ASO_SLICE_ORDER = (MPEG_BASE+378)
    MPEG_VIDEO_H264_HIERARCHICAL_CODING = (MPEG_BASE+379)
    MPEG_VIDEO_H264_HIERARCHICAL_CODING_TYPE = (MPEG_BASE+380)
    MPEG_VIDEO_H264_HIERARCHICAL_CODING_LAYER = (MPEG_BASE+381)
    MPEG_VIDEO_H264_HIERARCHICAL_CODING_LAYER_QP = (MPEG_BASE+382)

    MPEG_VIDEO_MPEG4_I_FRAME_QP = (MPEG_BASE+400)
    MPEG_VIDEO_MPEG4_P_FRAME_QP = (MPEG_BASE+401)
    MPEG_VIDEO_MPEG4_B_FRAME_QP = (MPEG_BASE+402)
    MPEG_VIDEO_MPEG4_MIN_QP = (MPEG_BASE+403)
    MPEG_VIDEO_MPEG4_MAX_QP = (MPEG_BASE+404)
    MPEG_VIDEO_MPEG4_LEVEL = (MPEG_BASE+405)
    MPEG_VIDEO_MPEG4_PROFILE = (MPEG_BASE+406)
    MPEG_VIDEO_MPEG4_QPEL = (MPEG_BASE+407)

    MPEG_VIDEO_VPX_NUM_PARTITIONS = (MPEG_BASE+500)
    MPEG_VIDEO_VPX_IMD_DISABLE_4X4 = (MPEG_BASE+501)
    MPEG_VIDEO_VPX_NUM_REF_FRAMES = (MPEG_BASE+502)
    MPEG_VIDEO_VPX_FILTER_LEVEL = (MPEG_BASE+503)
    MPEG_VIDEO_VPX_FILTER_SHARPNESS = (MPEG_BASE+504)
    MPEG_VIDEO_VPX_GOLDEN_FRAME_REF_PERIOD = (MPEG_BASE+505)
    MPEG_VIDEO_VPX_GOLDEN_FRAME_SEL = (MPEG_BASE+506)
    MPEG_VIDEO_VPX_MIN_QP = (MPEG_BASE+507)
    MPEG_VIDEO_VPX_MAX_QP = (MPEG_BASE+508)
    MPEG_VIDEO_VPX_I_FRAME_QP = (MPEG_BASE+509)
    MPEG_VIDEO_VPX_P_FRAME_QP = (MPEG_BASE+510)
    MPEG_VIDEO_VPX_PROFILE = (MPEG_BASE+511)

    MPEG_CX2341X_BASE = (V4L2_CTRL_CLASS.MPEG | 0x1000)
    MPEG_CX2341X_VIDEO_SPATIAL_FILTER_MODE = (MPEG_CX2341X_BASE+0)
    MPEG_CX2341X_VIDEO_SPATIAL_FILTER = (MPEG_CX2341X_BASE+1)
    MPEG_CX2341X_VIDEO_LUMA_SPATIAL_FILTER_TYPE = (MPEG_CX2341X_BASE+2)
    MPEG_CX2341X_VIDEO_CHROMA_SPATIAL_FILTER_TYPE = (MPEG_CX2341X_BASE+3)
    MPEG_CX2341X_VIDEO_TEMPORAL_FILTER_MODE = (MPEG_CX2341X_BASE+4)
    MPEG_CX2341X_VIDEO_TEMPORAL_FILTER = (MPEG_CX2341X_BASE+5)
    MPEG_CX2341X_VIDEO_MEDIAN_FILTER_TYPE = (MPEG_CX2341X_BASE+6)
    MPEG_CX2341X_VIDEO_LUMA_MEDIAN_FILTER_BOTTOM = (MPEG_CX2341X_BASE+7)
    MPEG_CX2341X_VIDEO_LUMA_MEDIAN_FILTER_TOP = (MPEG_CX2341X_BASE+8)
    MPEG_CX2341X_VIDEO_CHROMA_MEDIAN_FILTER_BOTTOM = (MPEG_CX2341X_BASE+9)
    MPEG_CX2341X_VIDEO_CHROMA_MEDIAN_FILTER_TOP = (MPEG_CX2341X_BASE+10)
    MPEG_CX2341X_STREAM_INSERT_NAV_PACKETS = (MPEG_CX2341X_BASE+11)

    MPEG_MFC51_BASE = (V4L2_CTRL_CLASS.MPEG | 0x1100)
    MPEG_MFC51_VIDEO_DECODER_H264_DISPLAY_DELAY = (MPEG_MFC51_BASE+0)
    MPEG_MFC51_VIDEO_DECODER_H264_DISPLAY_DELAY_ENABLE = (MPEG_MFC51_BASE+1)
    MPEG_MFC51_VIDEO_FRAME_SKIP_MODE = (MPEG_MFC51_BASE+2)
    MPEG_MFC51_VIDEO_FORCE_FRAME_TYPE = (MPEG_MFC51_BASE+3)
    MPEG_MFC51_VIDEO_PADDING = (MPEG_MFC51_BASE+4)
    MPEG_MFC51_VIDEO_PADDING_YUV = (MPEG_MFC51_BASE+5)
    MPEG_MFC51_VIDEO_RC_FIXED_TARGET_BIT = (MPEG_MFC51_BASE+6)
    MPEG_MFC51_VIDEO_RC_REACTION_COEFF = (MPEG_MFC51_BASE+7)
    MPEG_MFC51_VIDEO_H264_ADAPTIVE_RC_ACTIVITY = (MPEG_MFC51_BASE+50)
    MPEG_MFC51_VIDEO_H264_ADAPTIVE_RC_DARK = (MPEG_MFC51_BASE+51)
    MPEG_MFC51_VIDEO_H264_ADAPTIVE_RC_SMOOTH = (MPEG_MFC51_BASE+52)
    MPEG_MFC51_VIDEO_H264_ADAPTIVE_RC_STATIC = (MPEG_MFC51_BASE+53)
    MPEG_MFC51_VIDEO_H264_NUM_REF_PIC_FOR_P = (MPEG_MFC51_BASE+54)

    CAMERA_CLASS_BASE = (V4L2_CTRL_CLASS.CAMERA | 0x900)
    CAMERA_CLASS = (V4L2_CTRL_CLASS.CAMERA | 1)

    EXPOSURE_AUTO = (CAMERA_CLASS_BASE+1)
    EXPOSURE_ABSOLUTE = (CAMERA_CLASS_BASE+2)
    EXPOSURE_AUTO_PRIORITY = (CAMERA_CLASS_BASE+3)

    PAN_RELATIVE = (CAMERA_CLASS_BASE+4)
    TILT_RELATIVE = (CAMERA_CLASS_BASE+5)
    PAN_RESET = (CAMERA_CLASS_BASE+6)
    TILT_RESET = (CAMERA_CLASS_BASE+7)
    PAN_ABSOLUTE = (CAMERA_CLASS_BASE+8)
    TILT_ABSOLUTE = (CAMERA_CLASS_BASE+9)

    FOCUS_ABSOLUTE = (CAMERA_CLASS_BASE+10)
    FOCUS_RELATIVE = (CAMERA_CLASS_BASE+11)
    FOCUS_AUTO = (CAMERA_CLASS_BASE+12)

    ZOOM_ABSOLUTE = (CAMERA_CLASS_BASE+13)
    ZOOM_RELATIVE = (CAMERA_CLASS_BASE+14)
    ZOOM_CONTINUOUS = (CAMERA_CLASS_BASE+15)

    PRIVACY = (CAMERA_CLASS_BASE+16)

    IRIS_ABSOLUTE = (CAMERA_CLASS_BASE+17)
    IRIS_RELATIVE = (CAMERA_CLASS_BASE+18)

    AUTO_EXPOSURE_BIAS = (CAMERA_CLASS_BASE+19)
    AUTO_N_PRESET_WHITE_BALANCE = (CAMERA_CLASS_BASE+20)

    WIDE_DYNAMIC_RANGE = (CAMERA_CLASS_BASE+21)
    IMAGE_STABILIZATION = (CAMERA_CLASS_BASE+22)

    ISO_SENSITIVITY = (CAMERA_CLASS_BASE+23)
    ISO_SENSITIVITY_AUTO = (CAMERA_CLASS_BASE+24)
    EXPOSURE_METERING = (CAMERA_CLASS_BASE+25)

    SCENE_MODE = (CAMERA_CLASS_BASE+26)

    BISMASK_3A_LOCK = (CAMERA_CLASS_BASE+27)

    AUTO_FOCUS_START = (CAMERA_CLASS_BASE+28)
    AUTO_FOCUS_STOP = (CAMERA_CLASS_BASE+29)
    AUTO_FOCUS_STATUS = (CAMERA_CLASS_BASE+30)

    AUTO_FOCUS_RANGE = (CAMERA_CLASS_BASE+31)

    PAN_SPEED = (CAMERA_CLASS_BASE+32)
    TILT_SPEED = (CAMERA_CLASS_BASE+33)

    FM_TX_CLASS_BASE = (V4L2_CTRL_CLASS.FM_TX | 0x900)
    FM_TX_CLASS = (V4L2_CTRL_CLASS.FM_TX | 1)

    RDS_TX_DEVIATION = (FM_TX_CLASS_BASE + 1)
    RDS_TX_PI = (FM_TX_CLASS_BASE + 2)
    RDS_TX_PTY = (FM_TX_CLASS_BASE + 3)
    RDS_TX_PS_NAME = (FM_TX_CLASS_BASE + 5)
    RDS_TX_RADIO_TEXT = (FM_TX_CLASS_BASE + 6)
    RDS_TX_MONO_STEREO = (FM_TX_CLASS_BASE + 7)
    RDS_TX_ARTIFICIAL_HEAD = (FM_TX_CLASS_BASE + 8)
    RDS_TX_COMPRESSED = (FM_TX_CLASS_BASE + 9)
    RDS_TX_DYNAMIC_PTY = (FM_TX_CLASS_BASE + 10)
    RDS_TX_TRAFFIC_ANNOUNCEMENT = (FM_TX_CLASS_BASE + 11)
    RDS_TX_TRAFFIC_PROGRAM = (FM_TX_CLASS_BASE + 12)
    RDS_TX_MUSIC_SPEECH = (FM_TX_CLASS_BASE + 13)
    RDS_TX_ALT_FREQS_ENABLE = (FM_TX_CLASS_BASE + 14)
    RDS_TX_ALT_FREQS = (FM_TX_CLASS_BASE + 15)

    AUDIO_LIMITER_ENABLED = (FM_TX_CLASS_BASE + 64)
    AUDIO_LIMITER_RELEASE_TIME = (FM_TX_CLASS_BASE + 65)
    AUDIO_LIMITER_DEVIATION = (FM_TX_CLASS_BASE + 66)

    AUDIO_COMPRESSION_ENABLED = (FM_TX_CLASS_BASE + 80)
    AUDIO_COMPRESSION_GAIN = (FM_TX_CLASS_BASE + 81)
    AUDIO_COMPRESSION_THRESHOLD = (FM_TX_CLASS_BASE + 82)
    AUDIO_COMPRESSION_ATTACK_TIME = (FM_TX_CLASS_BASE + 83)
    AUDIO_COMPRESSION_RELEASE_TIME = (FM_TX_CLASS_BASE + 84)

    PILOT_TONE_ENABLED = (FM_TX_CLASS_BASE + 96)
    PILOT_TONE_DEVIATION = (FM_TX_CLASS_BASE + 97)
    PILOT_TONE_FREQUENCY = (FM_TX_CLASS_BASE + 98)

    TUNE_PREEMPHASIS = (FM_TX_CLASS_BASE + 112)
    TUNE_POWER_LEVEL = (FM_TX_CLASS_BASE + 113)
    TUNE_ANTENNA_CAPACITOR = (FM_TX_CLASS_BASE + 114)

    FLASH_CLASS_BASE = (V4L2_CTRL_CLASS.FLASH | 0x900)
    FLASH_CLASS = (V4L2_CTRL_CLASS.FLASH | 1)

    FLASH_LED_MODE = (FLASH_CLASS_BASE + 1)
    FLASH_STROBE_SOURCE = (FLASH_CLASS_BASE + 2)

    FLASH_STROBE = (FLASH_CLASS_BASE + 3)
    FLASH_STROBE_STOP = (FLASH_CLASS_BASE + 4)
    FLASH_STROBE_STATUS = (FLASH_CLASS_BASE + 5)
    FLASH_TIMEOUT = (FLASH_CLASS_BASE + 6)
    FLASH_INTENSITY = (FLASH_CLASS_BASE + 7)
    FLASH_TORCH_INTENSITY = (FLASH_CLASS_BASE + 8)
    FLASH_INDICATOR_INTENSITY = (FLASH_CLASS_BASE + 9)
    FLASH_FAULT = (FLASH_CLASS_BASE + 10)
    FLASH_CHARGE = (FLASH_CLASS_BASE + 11)
    FLASH_READY = (FLASH_CLASS_BASE + 12)

    JPEG_CLASS_BASE = (V4L2_CTRL_CLASS.JPEG | 0x900)
    JPEG_CLASS = (V4L2_CTRL_CLASS.JPEG | 1)

    JPEG_CHROMA_SUBSAMPLING = (JPEG_CLASS_BASE + 1)
    JPEG_RESTART_INTERVAL = (JPEG_CLASS_BASE + 2)
    JPEG_COMPRESSION_QUALITY = (JPEG_CLASS_BASE + 3)

    JPEG_ACTIVE_MARKER = (JPEG_CLASS_BASE + 4)

    IMAGE_SOURCE_CLASS_BASE = (V4L2_CTRL_CLASS.IMAGE_SOURCE | 0x900)
    IMAGE_SOURCE_CLASS = (V4L2_CTRL_CLASS.IMAGE_SOURCE | 1)

    VBLANK = (IMAGE_SOURCE_CLASS_BASE + 1)
    HBLANK = (IMAGE_SOURCE_CLASS_BASE + 2)
    ANALOGUE_GAIN = (IMAGE_SOURCE_CLASS_BASE + 3)

    TEST_PATTERN_RED = (IMAGE_SOURCE_CLASS_BASE + 4)
    TEST_PATTERN_GREENR = (IMAGE_SOURCE_CLASS_BASE + 5)
    TEST_PATTERN_BLUE = (IMAGE_SOURCE_CLASS_BASE + 6)
    TEST_PATTERN_GREENB = (IMAGE_SOURCE_CLASS_BASE + 7)

    IMAGE_PROC_CLASS_BASE = (V4L2_CTRL_CLASS.IMAGE_PROC | 0x900)
    IMAGE_PROC_CLASS = (V4L2_CTRL_CLASS.IMAGE_PROC | 1)

    LINK_FREQ = (IMAGE_PROC_CLASS_BASE + 1)
    PIXEL_RATE = (IMAGE_PROC_CLASS_BASE + 2)
    TEST_PATTERN = (IMAGE_PROC_CLASS_BASE + 3)

    DV_CLASS_BASE = (V4L2_CTRL_CLASS.DV | 0x900)
    DV_CLASS = (V4L2_CTRL_CLASS.DV | 1)

    DV_TX_HOTPLUG = (DV_CLASS_BASE + 1)
    DV_TX_RXSENSE = (DV_CLASS_BASE + 2)
    DV_TX_EDID_PRESENT = (DV_CLASS_BASE + 3)
    DV_TX_MODE = (DV_CLASS_BASE + 4)
    DV_TX_RGB_RANGE = (DV_CLASS_BASE + 5)
    DV_TX_IT_CONTENT_TYPE = (DV_CLASS_BASE + 6)

    DV_RX_POWER_PRESENT = (DV_CLASS_BASE + 100)
    DV_RX_RGB_RANGE = (DV_CLASS_BASE + 101)
    DV_RX_IT_CONTENT_TYPE = (DV_CLASS_BASE + 102)

    FM_RX_CLASS_BASE = (V4L2_CTRL_CLASS.FM_RX | 0x900)
    FM_RX_CLASS = (V4L2_CTRL_CLASS.FM_RX | 1)

    TUNE_DEEMPHASIS = (FM_RX_CLASS_BASE + 1)

    RDS_RECEPTION = (FM_RX_CLASS_BASE + 2)
    RDS_RX_PTY = (FM_RX_CLASS_BASE + 3)
    RDS_RX_PS_NAME = (FM_RX_CLASS_BASE + 4)
    RDS_RX_RADIO_TEXT = (FM_RX_CLASS_BASE + 5)
    RDS_RX_TRAFFIC_ANNOUNCEMENT = (FM_RX_CLASS_BASE + 6)
    RDS_RX_TRAFFIC_PROGRAM = (FM_RX_CLASS_BASE + 7)
    RDS_RX_MUSIC_SPEECH = (FM_RX_CLASS_BASE + 8)

    RF_TUNER_CLASS_BASE = (V4L2_CTRL_CLASS.RF_TUNER | 0x900)
    RF_TUNER_CLASS = (V4L2_CTRL_CLASS.RF_TUNER | 1)

    RF_TUNER_BANDWIDTH_AUTO = (RF_TUNER_CLASS_BASE + 11)
    RF_TUNER_BANDWIDTH = (RF_TUNER_CLASS_BASE + 12)
    RF_TUNER_RF_GAIN = (RF_TUNER_CLASS_BASE + 32)
    RF_TUNER_LNA_GAIN_AUTO = (RF_TUNER_CLASS_BASE + 41)
    RF_TUNER_LNA_GAIN = (RF_TUNER_CLASS_BASE + 42)
    RF_TUNER_MIXER_GAIN_AUTO = (RF_TUNER_CLASS_BASE + 51)
    RF_TUNER_MIXER_GAIN = (RF_TUNER_CLASS_BASE + 52)
    RF_TUNER_IF_GAIN_AUTO = (RF_TUNER_CLASS_BASE + 61)
    RF_TUNER_IF_GAIN = (RF_TUNER_CLASS_BASE + 62)
    RF_TUNER_PLL_LOCK = (RF_TUNER_CLASS_BASE + 91)

    DETECT_CLASS_BASE = (V4L2_CTRL_CLASS.DETECT | 0x900)
    DETECT_CLASS = (V4L2_CTRL_CLASS.DETECT | 1)

    DETECT_MD_MODE = (DETECT_CLASS_BASE + 1)
    DETECT_MD_GLOBAL_THRESHOLD = (DETECT_CLASS_BASE + 2)
    DETECT_MD_THRESHOLD_GRID = (DETECT_CLASS_BASE + 3)
    DETECT_MD_REGION_GRID = (DETECT_CLASS_BASE + 4)


class V4L2_POWER_LINE(enum.IntEnum):
    FREQUENCY_DISABLED = 0
    FREQUENCY_50HZ = 1
    FREQUENCY_60HZ = 2
    FREQUENCY_AUTO = 3


class V4L2_COLORFX(enum.IntEnum):
    NONE = 0
    BW = 1
    SEPIA = 2
    NEGATIVE = 3
    EMBOSS = 4
    SKETCH = 5
    SKY_BLUE = 6
    GRASS_GREEN = 7
    SKIN_WHITEN = 8
    VIVID = 9
    AQUA = 10
    ART_FREEZE = 11
    SILHOUETTE = 12
    SOLARIZATION = 13
    ANTIQUE = 14
    SET_CBCR = 15


class V4L2_MPEG_STREAM_TYPE(enum.IntEnum):
    MPEG2_PS = 0
    MPEG2_TS = 1
    MPEG1_SS = 2
    MPEG2_DVD = 3
    MPEG1_VCD = 4
    MPEG2_SVCD = 5


class V4L2_MPEG_STREAM_VBI_FMT(enum.IntEnum):
    NONE = 0
    IVTV = 1


class V4L2_MPEG_AUDIO_SAMPLING(enum.IntEnum):
    FREQ_44100 = 0
    FREQ_48000 = 1
    FREQ_32000 = 2


class V4L2_MPEG_AUDIO_ENCODING(enum.IntEnum):
    LAYER_1 = 0
    LAYER_2 = 1
    LAYER_3 = 2
    AAC = 3
    AC3 = 4


class V4L2_MPEG_AUDIO_L1(enum.IntEnum):
    BITRATE_32K = 0
    BITRATE_64K = 1
    BITRATE_96K = 2
    BITRATE_128K = 3
    BITRATE_160K = 4
    BITRATE_192K = 5
    BITRATE_224K = 6
    BITRATE_256K = 7
    BITRATE_288K = 8
    BITRATE_320K = 9
    BITRATE_352K = 10
    BITRATE_384K = 11
    BITRATE_416K = 12
    BITRATE_448K = 13


class V4L2_MPEG_AUDIO_L2(enum.IntEnum):
    BITRATE_32K = 0
    BITRATE_48K = 1
    BITRATE_56K = 2
    BITRATE_64K = 3
    BITRATE_80K = 4
    BITRATE_96K = 5
    BITRATE_112K = 6
    BITRATE_128K = 7
    BITRATE_160K = 8
    BITRATE_192K = 9
    BITRATE_224K = 10
    BITRATE_256K = 11
    BITRATE_320K = 12
    BITRATE_384K = 13


class V4L2_MPEG_AUDIO_L3(enum.IntEnum):
    BITRATE_32K = 0
    BITRATE_40K = 1
    BITRATE_48K = 2
    BITRATE_56K = 3
    BITRATE_64K = 4
    BITRATE_80K = 5
    BITRATE_96K = 6
    BITRATE_112K = 7
    BITRATE_128K = 8
    BITRATE_160K = 9
    BITRATE_192K = 10
    BITRATE_224K = 11
    BITRATE_256K = 12
    BITRATE_320K = 13


class V4L2_MPEG_AUDIO_MODE(enum.IntEnum):
    STEREO = 0
    JOINT_STEREO = 1
    DUAL = 2
    MONO = 3


class V4L2_MPEG_AUDIO_MODE_EXTENSION(enum.IntEnum):
    BOUND_4 = 0
    BOUND_8 = 1
    BOUND_12 = 2
    BOUND_16 = 3


class V4L2_MPEG_AUDIO(enum.IntEnum):
    EMPHASIS_NONE = 0
    EMPHASIS_50_DIV_15_uS = 1
    EMPHASIS_CCITT_J17 = 2


class V4L2_MPEG_AUDIO_CRC(enum.IntEnum):
    NONE = 0
    CRC16 = 1


class V4L2_MPEG_AUDIO_AC3(enum.IntEnum):
    BITRATE_32K = 0
    BITRATE_40K = 1
    BITRATE_48K = 2
    BITRATE_56K = 3
    BITRATE_64K = 4
    BITRATE_80K = 5
    BITRATE_96K = 6
    BITRATE_112K = 7
    BITRATE_128K = 8
    BITRATE_160K = 9
    BITRATE_192K = 10
    BITRATE_224K = 11
    BITRATE_256K = 12
    BITRATE_320K = 13
    BITRATE_384K = 14
    BITRATE_448K = 15
    BITRATE_512K = 16
    BITRATE_576K = 17
    BITRATE_640K = 18


class V4L2_MPEG_AUDIO_DEC_PLAYBACK(enum.IntEnum):
    AUTO = 0
    STEREO = 1
    LEFT = 2
    RIGHT = 3
    MONO = 4
    SWAPPED_STEREO = 5


class V4L2_MPEG_VIDEO_ENCODING(enum.IntEnum):
    MPEG_1 = 0
    MPEG_2 = 1
    MPEG_4_AVC = 2


class V4L2_MPEG_VIDEO(enum.IntEnum):
    ASPECT_1x1 = 0
    ASPECT_4x3 = 1
    ASPECT_16x9 = 2
    ASPECT_221x100 = 3


class V4L2_MPEG_VIDEO_BITRATE_MODE(enum.IntEnum):
    VBR = 0
    CBR = 1


class V4L2_MPEG_VIDEO_HEADER_MODE(enum.IntEnum):
    SEPARATE = 0
    JOINED_WITH_1ST_FRAME = 1


class V4L2_MPEG_VIDEO_MULTI_SLICE_MODE(enum.IntEnum):
    SINGLE = 0
    MAX_MB = 1
    MAX_BYTES = 2


class V4L2_MPEG_VIDEO_H264_ENTROPY_MODE(enum.IntEnum):
    CAVLC = 0
    CABAC = 1


class V4L2_MPEG_VIDEO_H264(enum.IntEnum):
    LEVEL_1_0 = 0
    LEVEL_1B = 1
    LEVEL_1_1 = 2
    LEVEL_1_2 = 3
    LEVEL_1_3 = 4
    LEVEL_2_0 = 5
    LEVEL_2_1 = 6
    LEVEL_2_2 = 7
    LEVEL_3_0 = 8
    LEVEL_3_1 = 9
    LEVEL_3_2 = 10
    LEVEL_4_0 = 11
    LEVEL_4_1 = 12
    LEVEL_4_2 = 13
    LEVEL_5_0 = 14
    LEVEL_5_1 = 15


class V4L2_MPEG_VIDEO_H264_LOOP_FILTER_MODE(enum.IntEnum):
    ENABLED = 0
    DISABLED = 1
    DISABLED_AT_SLICE_BOUNDARY = 2


class V4L2_MPEG_VIDEO_H264_PROFILE(enum.IntEnum):
    BASELINE = 0
    CONSTRAINED_BASELINE = 1
    MAIN = 2
    EXTENDED = 3
    HIGH = 4
    HIGH_10 = 5
    HIGH_422 = 6
    HIGH_444_PREDICTIVE = 7
    HIGH_10_INTRA = 8
    HIGH_422_INTRA = 9
    HIGH_444_INTRA = 10
    CAVLC_444_INTRA = 11
    SCALABLE_BASELINE = 12
    SCALABLE_HIGH = 13
    SCALABLE_HIGH_INTRA = 14
    STEREO_HIGH = 15
    MULTIVIEW_HIGH = 16


class V4L2_MPEG_VIDEO_H264_VUI_SAR(enum.IntEnum):
    IDC_UNSPECIFIED = 0
    IDC_1x1 = 1
    IDC_12x11 = 2
    IDC_10x11 = 3
    IDC_16x11 = 4
    IDC_40x33 = 5
    IDC_24x11 = 6
    IDC_20x11 = 7
    IDC_32x11 = 8
    IDC_80x33 = 9
    IDC_18x11 = 10
    IDC_15x11 = 11
    IDC_64x33 = 12
    IDC_160x99 = 13
    IDC_4x3 = 14
    IDC_3x2 = 15
    IDC_2x1 = 16
    IDC_EXTENDED = 17


class V4L2_MPEG_VIDEO_H264_SEI_FP_ARRANGEMENT_TYPE(enum.IntEnum):
    CHECKERBOARD = 0
    COLUMN = 1
    ROW = 2
    SIDE_BY_SIDE = 3
    TOP_BOTTOM = 4
    TEMPORAL = 5


class V4L2_MPEG_VIDEO_H264_FMO_MAP_TYPE(enum.IntEnum):
    INTERLEAVED_SLICES = 0
    SCATTERED_SLICES = 1
    FOREGROUND_WITH_LEFT_OVER = 2
    BOX_OUT = 3
    RASTER_SCAN = 4
    WIPE_SCAN = 5
    EXPLICIT = 6


class V4L2_MPEG_VIDEO_H264_FMO_CHANGE_DIR(enum.IntEnum):
    RIGHT = 0
    LEFT = 1


class V4L2_MPEG_VIDEO_H264_HIERARCHICAL_CODING(enum.IntEnum):
    B = 0
    P = 1


class V4L2_MPEG_VIDEO_MPEG4(enum.IntEnum):
    LEVEL_0 = 0
    LEVEL_0B = 1
    LEVEL_1 = 2
    LEVEL_2 = 3
    LEVEL_3 = 4
    LEVEL_3B = 5
    LEVEL_4 = 6
    LEVEL_5 = 7


class V4L2_MPEG_VIDEO_MPEG4_PROFILE(enum.IntEnum):
    SIMPLE = 0
    ADVANCED_SIMPLE = 1
    CORE = 2
    SIMPLE_SCALABLE = 3
    ADVANCED_CODING_EFFICIENCY = 4


class V4L2_MPEG_VIDEO_VPX_PARTITIONS(enum.IntEnum):
    NUM_1 = 0
    NUM_2 = 1
    NUM_4 = 2
    NUM_8 = 3


class V4L2_MPEG_VIDEO_VPX_REF_FRAME(enum.IntEnum):
    NUM_1 = 0
    NUM_2 = 1
    NUM_3 = 2


class V4L2_MPEG_VIDEO_VPX_GOLDEN_FRAME_USE(enum.IntEnum):
    PREV = 0
    REF_PERIOD = 1


class V4L2_MPEG_CX2341X_VIDEO_SPATIAL_FILTER_MODE(enum.IntEnum):
    MANUAL = 0
    AUTO = 1


class V4L2_MPEG_CX2341X_VIDEO_LUMA_SPATIAL_FILTER(enum.IntEnum):
    TYPE_OFF = 0
    TYPE_1D_HOR = 1
    TYPE_1D_VERT = 2
    TYPE_2D_HV_SEPARABLE = 3
    TYPE_2D_SYM_NON_SEPARABLE = 4


class V4L2_MPEG_CX2341X_VIDEO_CHROMA_SPATIAL_FILTER(enum.IntEnum):
    TYPE_OFF = 0
    TYPE_1D_HOR = 1


class V4L2_MPEG_CX2341X_VIDEO_TEMPORAL_FILTER_MODE(enum.IntEnum):
    MANUAL = 0
    AUTO = 1


class V4L2_MPEG_CX2341X_VIDEO_MEDIAN_FILTER_TYPE(enum.IntEnum):
    OFF = 0
    HOR = 1
    VERT = 2
    HOR_VERT = 3
    DIAG = 4


class V4L2_MPEG_MFC51_VIDEO_FRAME_SKIP_MODE(enum.IntEnum):
    DISABLED = 0
    LEVEL_LIMIT = 1
    BUF_LIMIT = 2


class V4L2_MPEG_MFC51_VIDEO_FORCE_FRAME_TYPE(enum.IntEnum):
    DISABLED = 0
    I_FRAME = 1
    NOT_CODED = 2


class V4L2_EXPOSURE(enum.IntEnum):
    AUTO = 0
    MANUAL = 1
    SHUTTER_PRIORITY = 2
    APERTURE_PRIORITY = 3


class V4L2_WHITE_BALANCE(enum.IntEnum):
    MANUAL = 0
    AUTO = 1
    INCANDESCENT = 2
    FLUORESCENT = 3
    FLUORESCENT_H = 4
    HORIZON = 5
    DAYLIGHT = 6
    FLASH = 7
    CLOUDY = 8
    SHADE = 9


class V4L2_ISO_SENSITIVITY(enum.IntEnum):
    MANUAL = 0
    AUTO = 1


class V4L2_EXPOSURE_METERING(enum.IntEnum):
    AVERAGE = 0
    CENTER_WEIGHTED = 1
    SPOT = 2
    MATRIX = 3


class V4L2_SCENE_MODE(enum.IntEnum):
    NONE = 0
    BACKLIGHT = 1
    BEACH_SNOW = 2
    CANDLE_LIGHT = 3
    DAWN_DUSK = 4
    FALL_COLORS = 5
    FIREWORKS = 6
    LANDSCAPE = 7
    NIGHT = 8
    PARTY_INDOOR = 9
    PORTRAIT = 10
    SPORTS = 11
    SUNSET = 12
    TEXT = 13


class V4L2_AUTO_FOCUS_RANGE(enum.IntEnum):
    AUTO = 0
    NORMAL = 1
    MACRO = 2
    INFINITY = 3


class V4L2_PREEMPHASIS(enum.IntEnum):
    DISABLED = 0
    TUNE_50_uS = 1
    TUNE_75_uS = 2


class V4L2_FLASH_LED_MODE(enum.IntEnum):
    NONE = 0
    FLASH = 1
    TORCH = 2


class V4L2_FLASH_STROBE_SOURCE(enum.IntEnum):
    SOFTWARE = 0
    EXTERNAL = 1


class V4L2_JPEG_CHROMA(enum.IntEnum):
    SUBSAMPLING_444 = 0
    SUBSAMPLING_422 = 1
    SUBSAMPLING_420 = 2
    SUBSAMPLING_411 = 3
    SUBSAMPLING_410 = 4
    SUBSAMPLING_GRAY = 5


class V4L2_DV_TX_MODE(enum.IntEnum):
    DVI_D = 0
    HDMI = 1


class V4L2_DV_RGB_RANGE(enum.IntEnum):
    AUTO = 0
    LIMITED = 1
    FULL = 2


class V4L2_DV_IT_CONTENT_TYPE(enum.IntEnum):
    GRAPHICS = 0
    PHOTO = 1
    CINEMA = 2
    GAME = 3
    NO_ITC = 4


class V4L2_DEEMPHASIS(enum.IntEnum):
    DISABLED = V4L2_PREEMPHASIS.DISABLED
    TUNE_50_uS = V4L2_PREEMPHASIS.TUNE_50_uS
    TUNE_75_uS = V4L2_PREEMPHASIS.TUNE_75_uS


class V4L2_DETECT_MD_MODE(enum.IntEnum):
    DISABLED = 0
    GLOBAL = 1
    THRESHOLD_GRID = 2
    REGION_GRID = 3


V4L2_LOCK_EXPOSURE = (1 << 0)
V4L2_LOCK_WHITE_BALANCE = (1 << 1)
V4L2_LOCK_FOCUS = (1 << 2)

V4L2_AUTO_FOCUS_STATUS_IDLE = (0 << 0)
V4L2_AUTO_FOCUS_STATUS_BUSY = (1 << 0)
V4L2_AUTO_FOCUS_STATUS_REACHED = (1 << 1)
V4L2_AUTO_FOCUS_STATUS_FAILED = (1 << 2)

V4L2_FLASH_FAULT_OVER_VOLTAGE = (1 << 0)
V4L2_FLASH_FAULT_TIMEOUT = (1 << 1)
V4L2_FLASH_FAULT_OVER_TEMPERATURE = (1 << 2)
V4L2_FLASH_FAULT_SHORT_CIRCUIT = (1 << 3)
V4L2_FLASH_FAULT_OVER_CURRENT = (1 << 4)
V4L2_FLASH_FAULT_INDICATOR = (1 << 5)
V4L2_FLASH_FAULT_UNDER_VOLTAGE = (1 << 6)
V4L2_FLASH_FAULT_INPUT_VOLTAGE = (1 << 7)
V4L2_FLASH_FAULT_LED_OVER_TEMPERATURE = (1 << 8)

V4L2_JPEG_ACTIVE_MARKER_APP0 = (1 << 0)
V4L2_JPEG_ACTIVE_MARKER_APP1 = (1 << 1)
V4L2_JPEG_ACTIVE_MARKER_COM = (1 << 16)
V4L2_JPEG_ACTIVE_MARKER_DQT = (1 << 17)
V4L2_JPEG_ACTIVE_MARKER_DHT = (1 << 18)
