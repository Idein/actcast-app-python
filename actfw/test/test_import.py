from nose2.tools import params


@params(
    # generated from the following program:
    #
    # ```python
    # import actfw
    # import inspect
    # import pkgutil
    #
    # builtin_modules = [m.name for m in pkgutil.iter_modules()]
    # visited_modules = {}
    #
    # def print_constants_in_module(module):
    #     visited_modules[module] = True
    #     for sub_name, sub in module.__dict__.items():
    #         if not sub_name.startswith('_') and sub_name not in builtin_modules:
    #             print(f'''    {{ 'from': '{module.__name__}', 'import': '{sub_name}' }}''')
    #             if inspect.ismodule(sub) and not visited_modules.get(sub) and sub.__name__.startswith('actfw'):
    #                 print_constants_in_module(sub)
    #
    # print_constants_in_module(actfw)
    # ```
    {'from': 'actfw', 'import': 'Application'},
    {'from': 'actfw', 'import': 'CommandServer'},
    {'from': 'actfw', 'import': 'Display'},
    {'from': 'actfw', 'import': 'Path'},
    {'from': 'actfw', 'import': 'application'},
    {'from': 'actfw', 'import': 'capture'},
    {'from': 'actfw', 'import': 'command_server'},
    {'from': 'actfw', 'import': 'display'},
    {'from': 'actfw', 'import': 'edid'},
    {'from': 'actfw', 'import': 'heartbeat'},
    {'from': 'actfw', 'import': 'notify'},
    {'from': 'actfw', 'import': 'set_heartbeat_function'},
    {'from': 'actfw', 'import': 'task'},
    {'from': 'actfw', 'import': 'v4l2'},
    {'from': 'actfw.application', 'import': 'Application'},
    {'from': 'actfw.application', 'import': 'Task'},
    {'from': 'actfw.application', 'import': 'time'},
    {'from': 'actfw.capture', 'import': 'Frame'},
    {'from': 'actfw.capture', 'import': 'Full'},
    {'from': 'actfw.capture', 'import': 'PiCameraCapture'},
    {'from': 'actfw.capture', 'import': 'Producer'},
    {'from': 'actfw.capture', 'import': 'V4L2_PIX_FMT'},
    {'from': 'actfw.capture', 'import': 'V4LCameraCapture'},
    {'from': 'actfw.capture', 'import': 'Video'},
    {'from': 'actfw.capture', 'import': 'VideoPort'},
    {'from': 'actfw.command_server', 'import': 'CommandServer'},
    {'from': 'actfw.command_server', 'import': 'Isolated'},
    {'from': 'actfw.command_server', 'import': 'Lock'},
    {'from': 'actfw.display', 'import': 'Display'},
    {'from': 'actfw.display', 'import': 'EDID'},
    {'from': 'actfw.edid', 'import': 'EDID'},
    {'from': 'actfw.task', 'import': 'Consumer'},
    {'from': 'actfw.task', 'import': 'Isolated'},
    {'from': 'actfw.task', 'import': 'Pipe'},
    {'from': 'actfw.task', 'import': 'Producer'},
    {'from': 'actfw.task', 'import': 'Task'},
    {'from': 'actfw.task', 'import': 'consumer'},
    {'from': 'actfw.task', 'import': 'isolated'},
    {'from': 'actfw.task', 'import': 'pipe'},
    {'from': 'actfw.task', 'import': 'producer'},
    {'from': 'actfw.task', 'import': 'task'},
    {'from': 'actfw.task.consumer', 'import': 'Consumer'},
    {'from': 'actfw.task.consumer', 'import': 'Pipe'},
    {'from': 'actfw.task.isolated', 'import': 'Isolated'},
    {'from': 'actfw.task.isolated', 'import': 'Task'},
    {'from': 'actfw.task.pipe', 'import': 'Empty'},
    {'from': 'actfw.task.pipe', 'import': 'Full'},
    {'from': 'actfw.task.pipe', 'import': 'Pipe'},
    {'from': 'actfw.task.pipe', 'import': 'Queue'},
    {'from': 'actfw.task.pipe', 'import': 'Task'},
    {'from': 'actfw.task.pipe', 'import': 'Thread'},
    {'from': 'actfw.task.producer', 'import': 'Pipe'},
    {'from': 'actfw.task.producer', 'import': 'Producer'},
    {'from': 'actfw.task.task', 'import': 'Task'},
    {'from': 'actfw.task.task', 'import': 'Thread'},
    {'from': 'actfw.v4l2', 'import': 'control'},
    {'from': 'actfw.v4l2', 'import': 'video'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_AUTO_FOCUS_RANGE'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_AUTO_FOCUS_STATUS_BUSY'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_AUTO_FOCUS_STATUS_FAILED'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_AUTO_FOCUS_STATUS_IDLE'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_AUTO_FOCUS_STATUS_REACHED'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_CID'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_COLORFX'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_CTRL_CLASS'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_CTRL_FLAG_DISABLED'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_CTRL_FLAG_EXECUTE_ON_WRITE'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_CTRL_FLAG_GRABBED'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_CTRL_FLAG_HAS_PAYLOAD'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_CTRL_FLAG_INACTIVE'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_CTRL_FLAG_MODIFY_LAYOUT'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_CTRL_FLAG_READ_ONLY'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_CTRL_FLAG_SLIDER'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_CTRL_FLAG_UPDATE'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_CTRL_FLAG_VOLATILE'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_CTRL_FLAG_WRITE_ONLY'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_CTRL_TYPE'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_DEEMPHASIS'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_DETECT_MD_MODE'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_DV_IT_CONTENT_TYPE'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_DV_RGB_RANGE'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_DV_TX_MODE'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_EXPOSURE'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_EXPOSURE_METERING'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_FLASH_FAULT_INDICATOR'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_FLASH_FAULT_INPUT_VOLTAGE'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_FLASH_FAULT_LED_OVER_TEMPERATURE'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_FLASH_FAULT_OVER_CURRENT'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_FLASH_FAULT_OVER_TEMPERATURE'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_FLASH_FAULT_OVER_VOLTAGE'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_FLASH_FAULT_SHORT_CIRCUIT'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_FLASH_FAULT_TIMEOUT'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_FLASH_FAULT_UNDER_VOLTAGE'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_FLASH_LED_MODE'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_FLASH_STROBE_SOURCE'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_ISO_SENSITIVITY'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_JPEG_ACTIVE_MARKER_APP0'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_JPEG_ACTIVE_MARKER_APP1'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_JPEG_ACTIVE_MARKER_COM'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_JPEG_ACTIVE_MARKER_DHT'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_JPEG_ACTIVE_MARKER_DQT'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_JPEG_CHROMA'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_LOCK_EXPOSURE'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_LOCK_FOCUS'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_LOCK_WHITE_BALANCE'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_MPEG_AUDIO'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_MPEG_AUDIO_AC3'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_MPEG_AUDIO_CRC'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_MPEG_AUDIO_DEC_PLAYBACK'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_MPEG_AUDIO_ENCODING'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_MPEG_AUDIO_L1'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_MPEG_AUDIO_L2'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_MPEG_AUDIO_L3'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_MPEG_AUDIO_MODE'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_MPEG_AUDIO_MODE_EXTENSION'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_MPEG_AUDIO_SAMPLING'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_MPEG_CX2341X_VIDEO_CHROMA_SPATIAL_FILTER'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_MPEG_CX2341X_VIDEO_LUMA_SPATIAL_FILTER'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_MPEG_CX2341X_VIDEO_MEDIAN_FILTER_TYPE'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_MPEG_CX2341X_VIDEO_SPATIAL_FILTER_MODE'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_MPEG_CX2341X_VIDEO_TEMPORAL_FILTER_MODE'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_MPEG_MFC51_VIDEO_FORCE_FRAME_TYPE'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_MPEG_MFC51_VIDEO_FRAME_SKIP_MODE'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_MPEG_STREAM_TYPE'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_MPEG_STREAM_VBI_FMT'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_MPEG_VIDEO'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_MPEG_VIDEO_BITRATE_MODE'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_MPEG_VIDEO_ENCODING'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_MPEG_VIDEO_H264'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_MPEG_VIDEO_H264_ENTROPY_MODE'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_MPEG_VIDEO_H264_FMO_CHANGE_DIR'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_MPEG_VIDEO_H264_FMO_MAP_TYPE'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_MPEG_VIDEO_H264_HIERARCHICAL_CODING'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_MPEG_VIDEO_H264_LOOP_FILTER_MODE'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_MPEG_VIDEO_H264_PROFILE'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_MPEG_VIDEO_H264_SEI_FP_ARRANGEMENT_TYPE'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_MPEG_VIDEO_H264_VUI_SAR'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_MPEG_VIDEO_HEADER_MODE'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_MPEG_VIDEO_MPEG4'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_MPEG_VIDEO_MPEG4_PROFILE'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_MPEG_VIDEO_MULTI_SLICE_MODE'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_MPEG_VIDEO_VPX_GOLDEN_FRAME_USE'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_MPEG_VIDEO_VPX_PARTITIONS'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_MPEG_VIDEO_VPX_REF_FRAME'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_POWER_LINE'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_PREEMPHASIS'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_SCENE_MODE'},
    {'from': 'actfw.v4l2.control', 'import': 'V4L2_WHITE_BALANCE'},
    {'from': 'actfw.v4l2.video', 'import': 'V4L2_BUF_TYPE'},
    {'from': 'actfw.v4l2.video', 'import': 'V4L2_CAP_TIMEPERFRAME'},
    {'from': 'actfw.v4l2.video', 'import': 'V4L2_FIELD'},
    {'from': 'actfw.v4l2.video', 'import': 'V4L2_FRMIVAL_TYPE'},
    {'from': 'actfw.v4l2.video', 'import': 'V4L2_FRMSIZE_TYPE'},
    {'from': 'actfw.v4l2.video', 'import': 'V4L2_MEMORY'},
    {'from': 'actfw.v4l2.video', 'import': 'V4L2_MODE_HIGHQUALITY'},
    {'from': 'actfw.v4l2.video', 'import': 'V4L2_PIX_FMT'},
    {'from': 'actfw.v4l2.video', 'import': 'Video'},
    {'from': 'actfw.v4l2.video', 'import': 'VideoBuffer'},
    {'from': 'actfw.v4l2.video', 'import': 'VideoConfig'},
    {'from': 'actfw.v4l2.video', 'import': 'VideoPort'},
    {'from': 'actfw.v4l2.video', 'import': 'VideoStream'},
)
def test_import_actfw_forward_compatibility(param):
    exec(f'''from {param['from']} import {param['import']}''')
