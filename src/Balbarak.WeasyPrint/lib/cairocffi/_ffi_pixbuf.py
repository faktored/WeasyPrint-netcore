# auto-generated file
import _cffi_backend
from cairocffi._ffi import ffi as _ffi0

ffi = _cffi_backend.FFI('cairocffi._ffi_pixbuf',
    _version = 0x2601,
    _types = b'\x00\x00\x7D\x0D\x00\x00\x7E\x03\x00\x00\x00\x0F\x00\x00\x42\x0D\x00\x00\x80\x03\x00\x00\x00\x0F\x00\x00\x3F\x0D\x00\x00\x04\x11\x00\x00\x00\x0F\x00\x00\x04\x0D\x00\x00\x00\x0F\x00\x00\xAE\x0D\x00\x00\x9A\x03\x00\x00\xC3\x03\x00\x00\x00\x0F\x00\x00\xAE\x0D\x00\x00\x0C\x11\x00\x00\x0D\x11\x00\x00\x9A\x03\x00\x00\x00\x0F\x00\x00\xAE\x0D\x00\x00\xA5\x03\x00\x00\xB6\x03\x00\x00\x88\x03\x00\x00\x00\x0F\x00\x00\xAE\x0D\x00\x00\x15\x11\x00\x00\xBD\x03\x00\x00\x07\x01\x00\x00\x8F\x03\x00\x00\x1C\x03\x00\x00\xB8\x03\x00\x00\x1E\x11\x00\x00\xB7\x03\x00\x00\x00\x0F\x00\x00\xAE\x0D\x00\x00\x15\x11\x00\x00\x0A\x01\x00\x00\x16\x11\x00\x00\xBA\x03\x00\x00\x00\x0F\x00\x00\xAE\x0D\x00\x00\x15\x11\x00\x00\x0A\x01\x00\x00\x25\x03\x00\x00\x00\x0F\x00\x00\xAE\x0D\x00\x00\x0D\x11\x00\x00\xBE\x03\x00\x00\x08\x01\x00\x00\x00\x0F\x00\x00\xAE\x0D\x00\x00\x0D\x11\x00\x00\xBE\x03\x00\x00\x08\x01\x00\x00\x00\x0F\x00\x00\x3B\x0D\x00\x00\x0C\x11\x00\x00\x0D\x11\x00\x00\xB2\x03\x00\x00\xA0\x03\x00\x00\x00\x0F\x00\x00\xBC\x0D\x00\x00\x7F\x03\x00\x00\x00\x0F\x00\x00\x1C\x0D\x00\x00\x7E\x03\x00\x00\xBC\x03\x00\x00\x2C\x11\x00\x00\x1B\x11\x00\x00\x5C\x03\x00\x00\x01\x0F\x00\x00\x1C\x0D\x00\x00\x01\x11\x00\x00\x00\x0F\x00\x00\x1C\x0D\x00\x00\x04\x11\x00\x00\x46\x11\x00\x00\x00\x0F\x00\x00\x1C\x0D\x00\x00\x04\x11\x00\x00\x35\x11\x00\x00\x0A\x01\x00\x00\x46\x11\x00\x00\x00\x0F\x00\x00\x30\x0D\x00\x00\x01\x11\x00\x00\x00\x0F\x00\x00\x25\x0D\x00\x00\x01\x11\x00\x00\x00\x0F\x00\x00\xC3\x0D\x00\x00\x7C\x03\x00\x00\x00\x0F\x00\x00\xC3\x0D\x00\x00\x04\x11\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x00\xC3\x0D\x00\x00\x0C\x11\x00\x00\x0D\x11\x00\x00\x00\x0F\x00\x00\xC3\x0D\x00\x00\x0C\x11\x00\x00\x0D\x11\x00\x00\x3B\x11\x00\x00\x00\x0F\x00\x00\xC3\x0D\x00\x00\x3B\x11\x00\x00\x3B\x11\x00\x00\x0D\x11\x00\x00\x00\x0F\x00\x00\xC3\x0D\x00\x00\x16\x11\x00\x00\x01\x11\x00\x00\x0E\x01\x00\x00\x0E\x01\x00\x00\x00\x0F\x00\x00\xC3\x0D\x00\x00\x0D\x11\x00\x00\x00\x0F\x00\x00\xC3\x0D\x00\x00\x00\x0F\x00\x00\x00\x09\x00\x00\x00\x0B\x00\x00\x01\x09\x00\x00\x02\x09\x00\x00\x03\x09\x00\x00\x02\x0B\x00\x00\x03\x0B\x00\x00\x09\x09\x00\x00\x04\x0B\x00\x00\x05\x0B\x00\x00\x06\x0B\x00\x00\x07\x0B\x00\x00\x04\x09\x00\x00\x0A\x09\x00\x00\x0B\x09\x00\x00\x08\x0B\x00\x00\x09\x0B\x00\x00\x0A\x0B\x00\x00\x0B\x0B\x00\x00\x90\x03\x00\x00\x05\x09\x00\x00\x0C\x0B\x00\x00\x0D\x0B\x00\x00\x0E\x0B\x00\x00\x0F\x0B\x00\x00\x0C\x09\x00\x00\x10\x0B\x00\x00\x0D\x09\x00\x00\x11\x0B\x00\x00\x16\x09\x00\x00\x0E\x09\x00\x00\x12\x0B\x00\x00\x13\x0B\x00\x00\x14\x0B\x00\x00\x15\x0B\x00\x00\x16\x0B\x00\x00\x10\x09\x00\x00\x11\x09\x00\x00\x0F\x09\x00\x00\x17\x0B\x00\x00\x12\x09\x00\x00\x13\x09\x00\x00\x0B\x03\x00\x00\x0F\x03\x00\x00\x14\x03\x00\x00\x19\x03\x00\x00\x23\x03\x00\x00\x29\x03\x00\x00\x2E\x03\x00\x00\x33\x03\x00\x00\x18\x0B\x00\x00\x19\x0B\x00\x00\x01\x0B\x00\x00\x38\x03\x00\x00\x14\x09\x00\x00\x1A\x0B\x00\x00\x1B\x0B\x00\x00\x1C\x0B\x00\x00\x08\x09\x00\x00\x1D\x0B\x00\x00\xB9\x03\x00\x00\x06\x09\x00\x00\x07\x09\x00\x00\x15\x09\x00\x00\xBD\x03\x00\x00\x02\x01\x00\x00\x04\x01\x00\x00\x63\x03\x00\x00\x67\x03\x00\x00\x6C\x03\x00\x00\x77\x03\x00\x00\x00\x01',
    _globals = (b'\xFF\xFF\xFF\x0BCAIRO_ANTIALIAS_BEST',6,b'\xFF\xFF\xFF\x0BCAIRO_ANTIALIAS_DEFAULT',0,b'\xFF\xFF\xFF\x0BCAIRO_ANTIALIAS_FAST',4,b'\xFF\xFF\xFF\x0BCAIRO_ANTIALIAS_GOOD',5,b'\xFF\xFF\xFF\x0BCAIRO_ANTIALIAS_GRAY',2,b'\xFF\xFF\xFF\x0BCAIRO_ANTIALIAS_NONE',1,b'\xFF\xFF\xFF\x0BCAIRO_ANTIALIAS_SUBPIXEL',3,b'\xFF\xFF\xFF\x0BCAIRO_CONTENT_ALPHA',8192,b'\xFF\xFF\xFF\x0BCAIRO_CONTENT_COLOR',4096,b'\xFF\xFF\xFF\x0BCAIRO_CONTENT_COLOR_ALPHA',12288,b'\xFF\xFF\xFF\x0BCAIRO_DEVICE_TYPE_COGL',6,b'\xFF\xFF\xFF\x0BCAIRO_DEVICE_TYPE_DRM',0,b'\xFF\xFF\xFF\x0BCAIRO_DEVICE_TYPE_GL',1,b'\xFF\xFF\xFF\x0BCAIRO_DEVICE_TYPE_INVALID',-1,b'\xFF\xFF\xFF\x0BCAIRO_DEVICE_TYPE_SCRIPT',2,b'\xFF\xFF\xFF\x0BCAIRO_DEVICE_TYPE_WIN32',7,b'\xFF\xFF\xFF\x0BCAIRO_DEVICE_TYPE_XCB',3,b'\xFF\xFF\xFF\x0BCAIRO_DEVICE_TYPE_XLIB',4,b'\xFF\xFF\xFF\x0BCAIRO_DEVICE_TYPE_XML',5,b'\xFF\xFF\xFF\x0BCAIRO_EXTEND_NONE',0,b'\xFF\xFF\xFF\x0BCAIRO_EXTEND_PAD',3,b'\xFF\xFF\xFF\x0BCAIRO_EXTEND_REFLECT',2,b'\xFF\xFF\xFF\x0BCAIRO_EXTEND_REPEAT',1,b'\xFF\xFF\xFF\x0BCAIRO_FILL_RULE_EVEN_ODD',1,b'\xFF\xFF\xFF\x0BCAIRO_FILL_RULE_WINDING',0,b'\xFF\xFF\xFF\x0BCAIRO_FILTER_BEST',2,b'\xFF\xFF\xFF\x0BCAIRO_FILTER_BILINEAR',4,b'\xFF\xFF\xFF\x0BCAIRO_FILTER_FAST',0,b'\xFF\xFF\xFF\x0BCAIRO_FILTER_GAUSSIAN',5,b'\xFF\xFF\xFF\x0BCAIRO_FILTER_GOOD',1,b'\xFF\xFF\xFF\x0BCAIRO_FILTER_NEAREST',3,b'\xFF\xFF\xFF\x0BCAIRO_FONT_SLANT_ITALIC',1,b'\xFF\xFF\xFF\x0BCAIRO_FONT_SLANT_NORMAL',0,b'\xFF\xFF\xFF\x0BCAIRO_FONT_SLANT_OBLIQUE',2,b'\xFF\xFF\xFF\x0BCAIRO_FONT_TYPE_FT',1,b'\xFF\xFF\xFF\x0BCAIRO_FONT_TYPE_QUARTZ',3,b'\xFF\xFF\xFF\x0BCAIRO_FONT_TYPE_TOY',0,b'\xFF\xFF\xFF\x0BCAIRO_FONT_TYPE_USER',4,b'\xFF\xFF\xFF\x0BCAIRO_FONT_TYPE_WIN32',2,b'\xFF\xFF\xFF\x0BCAIRO_FONT_WEIGHT_BOLD',1,b'\xFF\xFF\xFF\x0BCAIRO_FONT_WEIGHT_NORMAL',0,b'\xFF\xFF\xFF\x0BCAIRO_FORMAT_A1',3,b'\xFF\xFF\xFF\x0BCAIRO_FORMAT_A8',2,b'\xFF\xFF\xFF\x0BCAIRO_FORMAT_ARGB32',0,b'\xFF\xFF\xFF\x0BCAIRO_FORMAT_INVALID',-1,b'\xFF\xFF\xFF\x0BCAIRO_FORMAT_RGB16_565',4,b'\xFF\xFF\xFF\x0BCAIRO_FORMAT_RGB24',1,b'\xFF\xFF\xFF\x0BCAIRO_FORMAT_RGB30',5,b'\xFF\xFF\xFF\x0BCAIRO_HINT_METRICS_DEFAULT',0,b'\xFF\xFF\xFF\x0BCAIRO_HINT_METRICS_OFF',1,b'\xFF\xFF\xFF\x0BCAIRO_HINT_METRICS_ON',2,b'\xFF\xFF\xFF\x0BCAIRO_HINT_STYLE_DEFAULT',0,b'\xFF\xFF\xFF\x0BCAIRO_HINT_STYLE_FULL',4,b'\xFF\xFF\xFF\x0BCAIRO_HINT_STYLE_MEDIUM',3,b'\xFF\xFF\xFF\x0BCAIRO_HINT_STYLE_NONE',1,b'\xFF\xFF\xFF\x0BCAIRO_HINT_STYLE_SLIGHT',2,b'\xFF\xFF\xFF\x0BCAIRO_LINE_CAP_BUTT',0,b'\xFF\xFF\xFF\x0BCAIRO_LINE_CAP_ROUND',1,b'\xFF\xFF\xFF\x0BCAIRO_LINE_CAP_SQUARE',2,b'\xFF\xFF\xFF\x0BCAIRO_LINE_JOIN_BEVEL',2,b'\xFF\xFF\xFF\x0BCAIRO_LINE_JOIN_MITER',0,b'\xFF\xFF\xFF\x0BCAIRO_LINE_JOIN_ROUND',1,b'\xFF\xFF\xFF\x0BCAIRO_OPERATOR_ADD',12,b'\xFF\xFF\xFF\x0BCAIRO_OPERATOR_ATOP',5,b'\xFF\xFF\xFF\x0BCAIRO_OPERATOR_CLEAR',0,b'\xFF\xFF\xFF\x0BCAIRO_OPERATOR_COLOR_BURN',20,b'\xFF\xFF\xFF\x0BCAIRO_OPERATOR_COLOR_DODGE',19,b'\xFF\xFF\xFF\x0BCAIRO_OPERATOR_DARKEN',17,b'\xFF\xFF\xFF\x0BCAIRO_OPERATOR_DEST',6,b'\xFF\xFF\xFF\x0BCAIRO_OPERATOR_DEST_ATOP',10,b'\xFF\xFF\xFF\x0BCAIRO_OPERATOR_DEST_IN',8,b'\xFF\xFF\xFF\x0BCAIRO_OPERATOR_DEST_OUT',9,b'\xFF\xFF\xFF\x0BCAIRO_OPERATOR_DEST_OVER',7,b'\xFF\xFF\xFF\x0BCAIRO_OPERATOR_DIFFERENCE',23,b'\xFF\xFF\xFF\x0BCAIRO_OPERATOR_EXCLUSION',24,b'\xFF\xFF\xFF\x0BCAIRO_OPERATOR_HARD_LIGHT',21,b'\xFF\xFF\xFF\x0BCAIRO_OPERATOR_HSL_COLOR',27,b'\xFF\xFF\xFF\x0BCAIRO_OPERATOR_HSL_HUE',25,b'\xFF\xFF\xFF\x0BCAIRO_OPERATOR_HSL_LUMINOSITY',28,b'\xFF\xFF\xFF\x0BCAIRO_OPERATOR_HSL_SATURATION',26,b'\xFF\xFF\xFF\x0BCAIRO_OPERATOR_IN',3,b'\xFF\xFF\xFF\x0BCAIRO_OPERATOR_LIGHTEN',18,b'\xFF\xFF\xFF\x0BCAIRO_OPERATOR_MULTIPLY',14,b'\xFF\xFF\xFF\x0BCAIRO_OPERATOR_OUT',4,b'\xFF\xFF\xFF\x0BCAIRO_OPERATOR_OVER',2,b'\xFF\xFF\xFF\x0BCAIRO_OPERATOR_OVERLAY',16,b'\xFF\xFF\xFF\x0BCAIRO_OPERATOR_SATURATE',13,b'\xFF\xFF\xFF\x0BCAIRO_OPERATOR_SCREEN',15,b'\xFF\xFF\xFF\x0BCAIRO_OPERATOR_SOFT_LIGHT',22,b'\xFF\xFF\xFF\x0BCAIRO_OPERATOR_SOURCE',1,b'\xFF\xFF\xFF\x0BCAIRO_OPERATOR_XOR',11,b'\xFF\xFF\xFF\x0BCAIRO_PATH_CLOSE_PATH',3,b'\xFF\xFF\xFF\x0BCAIRO_PATH_CURVE_TO',2,b'\xFF\xFF\xFF\x0BCAIRO_PATH_LINE_TO',1,b'\xFF\xFF\xFF\x0BCAIRO_PATH_MOVE_TO',0,b'\xFF\xFF\xFF\x0BCAIRO_PATTERN_TYPE_LINEAR',2,b'\xFF\xFF\xFF\x0BCAIRO_PATTERN_TYPE_MESH',4,b'\xFF\xFF\xFF\x0BCAIRO_PATTERN_TYPE_RADIAL',3,b'\xFF\xFF\xFF\x0BCAIRO_PATTERN_TYPE_RASTER_SOURCE',5,b'\xFF\xFF\xFF\x0BCAIRO_PATTERN_TYPE_SOLID',0,b'\xFF\xFF\xFF\x0BCAIRO_PATTERN_TYPE_SURFACE',1,b'\xFF\xFF\xFF\x0BCAIRO_PDF_METADATA_AUTHOR',1,b'\xFF\xFF\xFF\x0BCAIRO_PDF_METADATA_CREATE_DATE',5,b'\xFF\xFF\xFF\x0BCAIRO_PDF_METADATA_CREATOR',4,b'\xFF\xFF\xFF\x0BCAIRO_PDF_METADATA_KEYWORDS',3,b'\xFF\xFF\xFF\x0BCAIRO_PDF_METADATA_MOD_DATE',6,b'\xFF\xFF\xFF\x0BCAIRO_PDF_METADATA_SUBJECT',2,b'\xFF\xFF\xFF\x0BCAIRO_PDF_METADATA_TITLE',0,b'\xFF\xFF\xFF\x0BCAIRO_PDF_OUTLINE_FLAG_BOLD',2,b'\xFF\xFF\xFF\x0BCAIRO_PDF_OUTLINE_FLAG_ITALIC',4,b'\xFF\xFF\xFF\x0BCAIRO_PDF_OUTLINE_FLAG_OPEN',1,b'\xFF\xFF\xFF\x0BCAIRO_PDF_VERSION_1_4',0,b'\xFF\xFF\xFF\x0BCAIRO_PDF_VERSION_1_5',1,b'\xFF\xFF\xFF\x0BCAIRO_PS_LEVEL_2',0,b'\xFF\xFF\xFF\x0BCAIRO_PS_LEVEL_3',1,b'\xFF\xFF\xFF\x0BCAIRO_REGION_OVERLAP_IN',0,b'\xFF\xFF\xFF\x0BCAIRO_REGION_OVERLAP_OUT',1,b'\xFF\xFF\xFF\x0BCAIRO_REGION_OVERLAP_PART',2,b'\xFF\xFF\xFF\x0BCAIRO_STATUS_CLIP_NOT_REPRESENTABLE',22,b'\xFF\xFF\xFF\x0BCAIRO_STATUS_DEVICE_ERROR',35,b'\xFF\xFF\xFF\x0BCAIRO_STATUS_DEVICE_FINISHED',37,b'\xFF\xFF\xFF\x0BCAIRO_STATUS_DEVICE_TYPE_MISMATCH',34,b'\xFF\xFF\xFF\x0BCAIRO_STATUS_FILE_NOT_FOUND',18,b'\xFF\xFF\xFF\x0BCAIRO_STATUS_FONT_TYPE_MISMATCH',25,b'\xFF\xFF\xFF\x0BCAIRO_STATUS_FREETYPE_ERROR',40,b'\xFF\xFF\xFF\x0BCAIRO_STATUS_INVALID_CLUSTERS',29,b'\xFF\xFF\xFF\x0BCAIRO_STATUS_INVALID_CONTENT',15,b'\xFF\xFF\xFF\x0BCAIRO_STATUS_INVALID_DASH',19,b'\xFF\xFF\xFF\x0BCAIRO_STATUS_INVALID_DSC_COMMENT',20,b'\xFF\xFF\xFF\x0BCAIRO_STATUS_INVALID_FORMAT',16,b'\xFF\xFF\xFF\x0BCAIRO_STATUS_INVALID_INDEX',21,b'\xFF\xFF\xFF\x0BCAIRO_STATUS_INVALID_MATRIX',5,b'\xFF\xFF\xFF\x0BCAIRO_STATUS_INVALID_MESH_CONSTRUCTION',36,b'\xFF\xFF\xFF\x0BCAIRO_STATUS_INVALID_PATH_DATA',9,b'\xFF\xFF\xFF\x0BCAIRO_STATUS_INVALID_POP_GROUP',3,b'\xFF\xFF\xFF\x0BCAIRO_STATUS_INVALID_RESTORE',2,b'\xFF\xFF\xFF\x0BCAIRO_STATUS_INVALID_SIZE',32,b'\xFF\xFF\xFF\x0BCAIRO_STATUS_INVALID_SLANT',30,b'\xFF\xFF\xFF\x0BCAIRO_STATUS_INVALID_STATUS',6,b'\xFF\xFF\xFF\x0BCAIRO_STATUS_INVALID_STRIDE',24,b'\xFF\xFF\xFF\x0BCAIRO_STATUS_INVALID_STRING',8,b'\xFF\xFF\xFF\x0BCAIRO_STATUS_INVALID_VISUAL',17,b'\xFF\xFF\xFF\x0BCAIRO_STATUS_INVALID_WEIGHT',31,b'\xFF\xFF\xFF\x0BCAIRO_STATUS_JBIG2_GLOBAL_MISSING',38,b'\xFF\xFF\xFF\x0BCAIRO_STATUS_LAST_STATUS',43,b'\xFF\xFF\xFF\x0BCAIRO_STATUS_NEGATIVE_COUNT',28,b'\xFF\xFF\xFF\x0BCAIRO_STATUS_NO_CURRENT_POINT',4,b'\xFF\xFF\xFF\x0BCAIRO_STATUS_NO_MEMORY',1,b'\xFF\xFF\xFF\x0BCAIRO_STATUS_NULL_POINTER',7,b'\xFF\xFF\xFF\x0BCAIRO_STATUS_PATTERN_TYPE_MISMATCH',14,b'\xFF\xFF\xFF\x0BCAIRO_STATUS_PNG_ERROR',39,b'\xFF\xFF\xFF\x0BCAIRO_STATUS_READ_ERROR',10,b'\xFF\xFF\xFF\x0BCAIRO_STATUS_SUCCESS',0,b'\xFF\xFF\xFF\x0BCAIRO_STATUS_SURFACE_FINISHED',12,b'\xFF\xFF\xFF\x0BCAIRO_STATUS_SURFACE_TYPE_MISMATCH',13,b'\xFF\xFF\xFF\x0BCAIRO_STATUS_TAG_ERROR',42,b'\xFF\xFF\xFF\x0BCAIRO_STATUS_TEMP_FILE_ERROR',23,b'\xFF\xFF\xFF\x0BCAIRO_STATUS_USER_FONT_ERROR',27,b'\xFF\xFF\xFF\x0BCAIRO_STATUS_USER_FONT_IMMUTABLE',26,b'\xFF\xFF\xFF\x0BCAIRO_STATUS_USER_FONT_NOT_IMPLEMENTED',33,b'\xFF\xFF\xFF\x0BCAIRO_STATUS_WIN32_GDI_ERROR',41,b'\xFF\xFF\xFF\x0BCAIRO_STATUS_WRITE_ERROR',11,b'\xFF\xFF\xFF\x0BCAIRO_SUBPIXEL_ORDER_BGR',2,b'\xFF\xFF\xFF\x0BCAIRO_SUBPIXEL_ORDER_DEFAULT',0,b'\xFF\xFF\xFF\x0BCAIRO_SUBPIXEL_ORDER_RGB',1,b'\xFF\xFF\xFF\x0BCAIRO_SUBPIXEL_ORDER_VBGR',4,b'\xFF\xFF\xFF\x0BCAIRO_SUBPIXEL_ORDER_VRGB',3,b'\xFF\xFF\xFF\x0BCAIRO_SURFACE_OBSERVER_NORMAL',0,b'\xFF\xFF\xFF\x0BCAIRO_SURFACE_OBSERVER_RECORD_OPERATIONS',1,b'\xFF\xFF\xFF\x0BCAIRO_SURFACE_TYPE_BEOS',8,b'\xFF\xFF\xFF\x0BCAIRO_SURFACE_TYPE_COGL',24,b'\xFF\xFF\xFF\x0BCAIRO_SURFACE_TYPE_DIRECTFB',9,b'\xFF\xFF\xFF\x0BCAIRO_SURFACE_TYPE_DRM',19,b'\xFF\xFF\xFF\x0BCAIRO_SURFACE_TYPE_GL',18,b'\xFF\xFF\xFF\x0BCAIRO_SURFACE_TYPE_GLITZ',5,b'\xFF\xFF\xFF\x0BCAIRO_SURFACE_TYPE_IMAGE',0,b'\xFF\xFF\xFF\x0BCAIRO_SURFACE_TYPE_OS2',11,b'\xFF\xFF\xFF\x0BCAIRO_SURFACE_TYPE_PDF',1,b'\xFF\xFF\xFF\x0BCAIRO_SURFACE_TYPE_PS',2,b'\xFF\xFF\xFF\x0BCAIRO_SURFACE_TYPE_QT',15,b'\xFF\xFF\xFF\x0BCAIRO_SURFACE_TYPE_QUARTZ',6,b'\xFF\xFF\xFF\x0BCAIRO_SURFACE_TYPE_QUARTZ_IMAGE',13,b'\xFF\xFF\xFF\x0BCAIRO_SURFACE_TYPE_RECORDING',16,b'\xFF\xFF\xFF\x0BCAIRO_SURFACE_TYPE_SCRIPT',14,b'\xFF\xFF\xFF\x0BCAIRO_SURFACE_TYPE_SKIA',22,b'\xFF\xFF\xFF\x0BCAIRO_SURFACE_TYPE_SUBSURFACE',23,b'\xFF\xFF\xFF\x0BCAIRO_SURFACE_TYPE_SVG',10,b'\xFF\xFF\xFF\x0BCAIRO_SURFACE_TYPE_TEE',20,b'\xFF\xFF\xFF\x0BCAIRO_SURFACE_TYPE_VG',17,b'\xFF\xFF\xFF\x0BCAIRO_SURFACE_TYPE_WIN32',7,b'\xFF\xFF\xFF\x0BCAIRO_SURFACE_TYPE_WIN32_PRINTING',12,b'\xFF\xFF\xFF\x0BCAIRO_SURFACE_TYPE_XCB',4,b'\xFF\xFF\xFF\x0BCAIRO_SURFACE_TYPE_XLIB',3,b'\xFF\xFF\xFF\x0BCAIRO_SURFACE_TYPE_XML',21,b'\xFF\xFF\xFF\x0BCAIRO_SVG_UNIT_CM',5,b'\xFF\xFF\xFF\x0BCAIRO_SVG_UNIT_EM',1,b'\xFF\xFF\xFF\x0BCAIRO_SVG_UNIT_EX',2,b'\xFF\xFF\xFF\x0BCAIRO_SVG_UNIT_IN',4,b'\xFF\xFF\xFF\x0BCAIRO_SVG_UNIT_MM',6,b'\xFF\xFF\xFF\x0BCAIRO_SVG_UNIT_PC',8,b'\xFF\xFF\xFF\x0BCAIRO_SVG_UNIT_PERCENT',9,b'\xFF\xFF\xFF\x0BCAIRO_SVG_UNIT_PT',7,b'\xFF\xFF\xFF\x0BCAIRO_SVG_UNIT_PX',3,b'\xFF\xFF\xFF\x0BCAIRO_SVG_UNIT_USER',0,b'\xFF\xFF\xFF\x0BCAIRO_SVG_VERSION_1_1',0,b'\xFF\xFF\xFF\x0BCAIRO_SVG_VERSION_1_2',1,b'\xFF\xFF\xFF\x0BCAIRO_TEXT_CLUSTER_FLAG_BACKWARD',1,b'\xFF\xFF\xFF\x0BGDK_COLORSPACE_RGB',0,b'\x00\x00\x5B\x23g_error_free',0,b'\x00\x00\x77\x23g_object_ref',0,b'\x00\x00\x77\x23g_object_unref',0,b'\x00\x00\x7A\x23g_type_init',0,b'\x00\x00\x71\x23gdk_cairo_set_source_pixbuf',0,b'\x00\x00\x3E\x23gdk_pixbuf_format_get_name',0,b'\x00\x00\x48\x23gdk_pixbuf_get_bits_per_sample',0,b'\x00\x00\x58\x23gdk_pixbuf_get_byte_length',0,b'\x00\x00\x00\x23gdk_pixbuf_get_colorspace',0,b'\x00\x00\x48\x23gdk_pixbuf_get_has_alpha',0,b'\x00\x00\x48\x23gdk_pixbuf_get_height',0,b'\x00\x00\x48\x23gdk_pixbuf_get_n_channels',0,b'\x00\x00\x55\x23gdk_pixbuf_get_pixels',0,b'\x00\x00\x48\x23gdk_pixbuf_get_rowstride',0,b'\x00\x00\x48\x23gdk_pixbuf_get_width',0,b'\x00\x00\x4B\x23gdk_pixbuf_loader_close',0,b'\x00\x00\x06\x23gdk_pixbuf_loader_get_format',0,b'\x00\x00\x03\x23gdk_pixbuf_loader_get_pixbuf',0,b'\x00\x00\x09\x23gdk_pixbuf_loader_new',0,b'\x00\x00\x5E\x23gdk_pixbuf_loader_set_size',0,b'\x00\x00\x4F\x23gdk_pixbuf_loader_write',0,b'\x00\x00\x41\x23gdk_pixbuf_save_to_buffer',0),
    _struct_unions = ((b'\x00\x00\x00\x7C\x00\x00\x00\x02$GError',b'\x00\x00\x31\x11domain',b'\x00\x00\x1C\x11code',b'\x00\x00\xBC\x11message'),(b'\x00\x00\x00\x7E\x00\x00\x00\x10$GdkPixbuf',),(b'\x00\x00\x00\x7F\x00\x00\x00\x10$GdkPixbufFormat',),(b'\x00\x00\x00\x80\x00\x00\x00\x10$GdkPixbufLoader',),(b'\x00\x00\x00\x88\x00\x00\x00\x08$cairo_font_extents_t',),(b'\x00\x00\x00\x90\x00\x00\x00\x08$cairo_glyph_t',),(b'\x00\x00\x00\xB9\x00\x00\x00\x08$cairo_text_cluster_t',),(b'\x00\x00\x00\xBA\x00\x00\x00\x08$cairo_text_extents_t',),(b'\x00\x00\x00\xB6\x00\x00\x00\x18_cairo',),(b'\x00\x00\x00\x83\x00\x00\x00\x18_cairo_device',),(b'\x00\x00\x00\x89\x00\x00\x00\x18_cairo_font_face',),(b'\x00\x00\x00\x8A\x00\x00\x00\x18_cairo_font_options',),(b'\x00\x00\x00\x95\x00\x00\x00\x08_cairo_matrix',),(b'\x00\x00\x00\x97\x00\x00\x00\x09_cairo_path_data_t',),(b'\x00\x00\x00\x9A\x00\x00\x00\x18_cairo_pattern',),(b'\x00\x00\x00\xA2\x00\x00\x00\x08_cairo_rectangle',),(b'\x00\x00\x00\xA0\x00\x00\x00\x08_cairo_rectangle_int',),(b'\x00\x00\x00\xA1\x00\x00\x00\x08_cairo_rectangle_list',),(b'\x00\x00\x00\xA4\x00\x00\x00\x18_cairo_region',),(b'\x00\x00\x00\xA5\x00\x00\x00\x18_cairo_scaled_font',),(b'\x00\x00\x00\xB2\x00\x00\x00\x18_cairo_surface',),(b'\x00\x00\x00\xBB\x00\x00\x00\x08_cairo_user_data_key',),(b'\x00\x00\x00\x99\x00\x00\x00\x08cairo_path',)),
    _enums = (b'\x00\x00\x00\x7D\x00\x00\x00\x16$GdkColorspace\x00GDK_COLORSPACE_RGB',b'\x00\x00\x00\xB0\x00\x00\x00\x16$cairo_surface_observer_mode_t\x00CAIRO_SURFACE_OBSERVER_NORMAL,CAIRO_SURFACE_OBSERVER_RECORD_OPERATIONS',b'\x00\x00\x00\x81\x00\x00\x00\x16_cairo_antialias\x00CAIRO_ANTIALIAS_DEFAULT,CAIRO_ANTIALIAS_NONE,CAIRO_ANTIALIAS_GRAY,CAIRO_ANTIALIAS_SUBPIXEL,CAIRO_ANTIALIAS_FAST,CAIRO_ANTIALIAS_GOOD,CAIRO_ANTIALIAS_BEST',b'\x00\x00\x00\x82\x00\x00\x00\x16_cairo_content\x00CAIRO_CONTENT_COLOR,CAIRO_CONTENT_ALPHA,CAIRO_CONTENT_COLOR_ALPHA',b'\x00\x00\x00\x84\x00\x00\x00\x15_cairo_device_type\x00CAIRO_DEVICE_TYPE_DRM,CAIRO_DEVICE_TYPE_GL,CAIRO_DEVICE_TYPE_SCRIPT,CAIRO_DEVICE_TYPE_XCB,CAIRO_DEVICE_TYPE_XLIB,CAIRO_DEVICE_TYPE_XML,CAIRO_DEVICE_TYPE_COGL,CAIRO_DEVICE_TYPE_WIN32,CAIRO_DEVICE_TYPE_INVALID',b'\x00\x00\x00\x85\x00\x00\x00\x16_cairo_extend\x00CAIRO_EXTEND_NONE,CAIRO_EXTEND_REPEAT,CAIRO_EXTEND_REFLECT,CAIRO_EXTEND_PAD',b'\x00\x00\x00\x86\x00\x00\x00\x16_cairo_fill_rule\x00CAIRO_FILL_RULE_WINDING,CAIRO_FILL_RULE_EVEN_ODD',b'\x00\x00\x00\x87\x00\x00\x00\x16_cairo_filter\x00CAIRO_FILTER_FAST,CAIRO_FILTER_GOOD,CAIRO_FILTER_BEST,CAIRO_FILTER_NEAREST,CAIRO_FILTER_BILINEAR,CAIRO_FILTER_GAUSSIAN',b'\x00\x00\x00\x8B\x00\x00\x00\x16_cairo_font_slant\x00CAIRO_FONT_SLANT_NORMAL,CAIRO_FONT_SLANT_ITALIC,CAIRO_FONT_SLANT_OBLIQUE',b'\x00\x00\x00\x8C\x00\x00\x00\x16_cairo_font_type\x00CAIRO_FONT_TYPE_TOY,CAIRO_FONT_TYPE_FT,CAIRO_FONT_TYPE_WIN32,CAIRO_FONT_TYPE_QUARTZ,CAIRO_FONT_TYPE_USER',b'\x00\x00\x00\x8D\x00\x00\x00\x16_cairo_font_weight\x00CAIRO_FONT_WEIGHT_NORMAL,CAIRO_FONT_WEIGHT_BOLD',b'\x00\x00\x00\x8E\x00\x00\x00\x15_cairo_format\x00CAIRO_FORMAT_INVALID,CAIRO_FORMAT_ARGB32,CAIRO_FORMAT_RGB24,CAIRO_FORMAT_A8,CAIRO_FORMAT_A1,CAIRO_FORMAT_RGB16_565,CAIRO_FORMAT_RGB30',b'\x00\x00\x00\x91\x00\x00\x00\x16_cairo_hint_metrics\x00CAIRO_HINT_METRICS_DEFAULT,CAIRO_HINT_METRICS_OFF,CAIRO_HINT_METRICS_ON',b'\x00\x00\x00\x92\x00\x00\x00\x16_cairo_hint_style\x00CAIRO_HINT_STYLE_DEFAULT,CAIRO_HINT_STYLE_NONE,CAIRO_HINT_STYLE_SLIGHT,CAIRO_HINT_STYLE_MEDIUM,CAIRO_HINT_STYLE_FULL',b'\x00\x00\x00\x93\x00\x00\x00\x16_cairo_line_cap\x00CAIRO_LINE_CAP_BUTT,CAIRO_LINE_CAP_ROUND,CAIRO_LINE_CAP_SQUARE',b'\x00\x00\x00\x94\x00\x00\x00\x16_cairo_line_join\x00CAIRO_LINE_JOIN_MITER,CAIRO_LINE_JOIN_ROUND,CAIRO_LINE_JOIN_BEVEL',b'\x00\x00\x00\x96\x00\x00\x00\x16_cairo_operator\x00CAIRO_OPERATOR_CLEAR,CAIRO_OPERATOR_SOURCE,CAIRO_OPERATOR_OVER,CAIRO_OPERATOR_IN,CAIRO_OPERATOR_OUT,CAIRO_OPERATOR_ATOP,CAIRO_OPERATOR_DEST,CAIRO_OPERATOR_DEST_OVER,CAIRO_OPERATOR_DEST_IN,CAIRO_OPERATOR_DEST_OUT,CAIRO_OPERATOR_DEST_ATOP,CAIRO_OPERATOR_XOR,CAIRO_OPERATOR_ADD,CAIRO_OPERATOR_SATURATE,CAIRO_OPERATOR_MULTIPLY,CAIRO_OPERATOR_SCREEN,CAIRO_OPERATOR_OVERLAY,CAIRO_OPERATOR_DARKEN,CAIRO_OPERATOR_LIGHTEN,CAIRO_OPERATOR_COLOR_DODGE,CAIRO_OPERATOR_COLOR_BURN,CAIRO_OPERATOR_HARD_LIGHT,CAIRO_OPERATOR_SOFT_LIGHT,CAIRO_OPERATOR_DIFFERENCE,CAIRO_OPERATOR_EXCLUSION,CAIRO_OPERATOR_HSL_HUE,CAIRO_OPERATOR_HSL_SATURATION,CAIRO_OPERATOR_HSL_COLOR,CAIRO_OPERATOR_HSL_LUMINOSITY',b'\x00\x00\x00\x98\x00\x00\x00\x16_cairo_path_data_type\x00CAIRO_PATH_MOVE_TO,CAIRO_PATH_LINE_TO,CAIRO_PATH_CURVE_TO,CAIRO_PATH_CLOSE_PATH',b'\x00\x00\x00\x9B\x00\x00\x00\x16_cairo_pattern_type\x00CAIRO_PATTERN_TYPE_SOLID,CAIRO_PATTERN_TYPE_SURFACE,CAIRO_PATTERN_TYPE_LINEAR,CAIRO_PATTERN_TYPE_RADIAL,CAIRO_PATTERN_TYPE_MESH,CAIRO_PATTERN_TYPE_RASTER_SOURCE',b'\x00\x00\x00\x9C\x00\x00\x00\x16_cairo_pdf_metadata\x00CAIRO_PDF_METADATA_TITLE,CAIRO_PDF_METADATA_AUTHOR,CAIRO_PDF_METADATA_SUBJECT,CAIRO_PDF_METADATA_KEYWORDS,CAIRO_PDF_METADATA_CREATOR,CAIRO_PDF_METADATA_CREATE_DATE,CAIRO_PDF_METADATA_MOD_DATE',b'\x00\x00\x00\x9D\x00\x00\x00\x16_cairo_pdf_outline_flags\x00CAIRO_PDF_OUTLINE_FLAG_OPEN,CAIRO_PDF_OUTLINE_FLAG_BOLD,CAIRO_PDF_OUTLINE_FLAG_ITALIC',b'\x00\x00\x00\x9E\x00\x00\x00\x16_cairo_pdf_version\x00CAIRO_PDF_VERSION_1_4,CAIRO_PDF_VERSION_1_5',b'\x00\x00\x00\x9F\x00\x00\x00\x16_cairo_ps_level\x00CAIRO_PS_LEVEL_2,CAIRO_PS_LEVEL_3',b'\x00\x00\x00\xA3\x00\x00\x00\x16_cairo_region_overlap\x00CAIRO_REGION_OVERLAP_IN,CAIRO_REGION_OVERLAP_OUT,CAIRO_REGION_OVERLAP_PART',b'\x00\x00\x00\xAE\x00\x00\x00\x16_cairo_status\x00CAIRO_STATUS_SUCCESS,CAIRO_STATUS_NO_MEMORY,CAIRO_STATUS_INVALID_RESTORE,CAIRO_STATUS_INVALID_POP_GROUP,CAIRO_STATUS_NO_CURRENT_POINT,CAIRO_STATUS_INVALID_MATRIX,CAIRO_STATUS_INVALID_STATUS,CAIRO_STATUS_NULL_POINTER,CAIRO_STATUS_INVALID_STRING,CAIRO_STATUS_INVALID_PATH_DATA,CAIRO_STATUS_READ_ERROR,CAIRO_STATUS_WRITE_ERROR,CAIRO_STATUS_SURFACE_FINISHED,CAIRO_STATUS_SURFACE_TYPE_MISMATCH,CAIRO_STATUS_PATTERN_TYPE_MISMATCH,CAIRO_STATUS_INVALID_CONTENT,CAIRO_STATUS_INVALID_FORMAT,CAIRO_STATUS_INVALID_VISUAL,CAIRO_STATUS_FILE_NOT_FOUND,CAIRO_STATUS_INVALID_DASH,CAIRO_STATUS_INVALID_DSC_COMMENT,CAIRO_STATUS_INVALID_INDEX,CAIRO_STATUS_CLIP_NOT_REPRESENTABLE,CAIRO_STATUS_TEMP_FILE_ERROR,CAIRO_STATUS_INVALID_STRIDE,CAIRO_STATUS_FONT_TYPE_MISMATCH,CAIRO_STATUS_USER_FONT_IMMUTABLE,CAIRO_STATUS_USER_FONT_ERROR,CAIRO_STATUS_NEGATIVE_COUNT,CAIRO_STATUS_INVALID_CLUSTERS,CAIRO_STATUS_INVALID_SLANT,CAIRO_STATUS_INVALID_WEIGHT,CAIRO_STATUS_INVALID_SIZE,CAIRO_STATUS_USER_FONT_NOT_IMPLEMENTED,CAIRO_STATUS_DEVICE_TYPE_MISMATCH,CAIRO_STATUS_DEVICE_ERROR,CAIRO_STATUS_INVALID_MESH_CONSTRUCTION,CAIRO_STATUS_DEVICE_FINISHED,CAIRO_STATUS_JBIG2_GLOBAL_MISSING,CAIRO_STATUS_PNG_ERROR,CAIRO_STATUS_FREETYPE_ERROR,CAIRO_STATUS_WIN32_GDI_ERROR,CAIRO_STATUS_TAG_ERROR,CAIRO_STATUS_LAST_STATUS',b'\x00\x00\x00\xAF\x00\x00\x00\x16_cairo_subpixel_order\x00CAIRO_SUBPIXEL_ORDER_DEFAULT,CAIRO_SUBPIXEL_ORDER_RGB,CAIRO_SUBPIXEL_ORDER_BGR,CAIRO_SUBPIXEL_ORDER_VRGB,CAIRO_SUBPIXEL_ORDER_VBGR',b'\x00\x00\x00\xB3\x00\x00\x00\x16_cairo_surface_type\x00CAIRO_SURFACE_TYPE_IMAGE,CAIRO_SURFACE_TYPE_PDF,CAIRO_SURFACE_TYPE_PS,CAIRO_SURFACE_TYPE_XLIB,CAIRO_SURFACE_TYPE_XCB,CAIRO_SURFACE_TYPE_GLITZ,CAIRO_SURFACE_TYPE_QUARTZ,CAIRO_SURFACE_TYPE_WIN32,CAIRO_SURFACE_TYPE_BEOS,CAIRO_SURFACE_TYPE_DIRECTFB,CAIRO_SURFACE_TYPE_SVG,CAIRO_SURFACE_TYPE_OS2,CAIRO_SURFACE_TYPE_WIN32_PRINTING,CAIRO_SURFACE_TYPE_QUARTZ_IMAGE,CAIRO_SURFACE_TYPE_SCRIPT,CAIRO_SURFACE_TYPE_QT,CAIRO_SURFACE_TYPE_RECORDING,CAIRO_SURFACE_TYPE_VG,CAIRO_SURFACE_TYPE_GL,CAIRO_SURFACE_TYPE_DRM,CAIRO_SURFACE_TYPE_TEE,CAIRO_SURFACE_TYPE_XML,CAIRO_SURFACE_TYPE_SKIA,CAIRO_SURFACE_TYPE_SUBSURFACE,CAIRO_SURFACE_TYPE_COGL',b'\x00\x00\x00\xB4\x00\x00\x00\x16_cairo_svg_unit\x00CAIRO_SVG_UNIT_USER,CAIRO_SVG_UNIT_EM,CAIRO_SVG_UNIT_EX,CAIRO_SVG_UNIT_PX,CAIRO_SVG_UNIT_IN,CAIRO_SVG_UNIT_CM,CAIRO_SVG_UNIT_MM,CAIRO_SVG_UNIT_PT,CAIRO_SVG_UNIT_PC,CAIRO_SVG_UNIT_PERCENT',b'\x00\x00\x00\xB5\x00\x00\x00\x16_cairo_svg_version\x00CAIRO_SVG_VERSION_1_1,CAIRO_SVG_VERSION_1_2',b'\x00\x00\x00\xB7\x00\x00\x00\x16_cairo_text_cluster_flags\x00CAIRO_TEXT_CLUSTER_FLAG_BACKWARD'),
    _typenames = (b'\x00\x00\x00\x0DATSUFontID',b'\x00\x00\x00\x0DCGContextRef',b'\x00\x00\x00\x0DCGFontRef',b'\x00\x00\x00\x7CGError',b'\x00\x00\x00\x31GQuark',b'\x00\x00\x00\x7DGdkColorspace',b'\x00\x00\x00\x7EGdkPixbuf',b'\x00\x00\x00\x7FGdkPixbufFormat',b'\x00\x00\x00\x80GdkPixbufLoader',b'\x00\x00\x00\x0DHDC',b'\x00\x00\x00\x0DHFONT',b'\x00\x00\x00\xC3LOGFONTW',b'\x00\x00\x00\x81cairo_antialias_t',b'\x00\x00\x00\x1Ccairo_bool_t',b'\x00\x00\x00\x82cairo_content_t',b'\x00\x00\x00\xC2cairo_destroy_func_t',b'\x00\x00\x00\x83cairo_device_t',b'\x00\x00\x00\x84cairo_device_type_t',b'\x00\x00\x00\x85cairo_extend_t',b'\x00\x00\x00\x86cairo_fill_rule_t',b'\x00\x00\x00\x87cairo_filter_t',b'\x00\x00\x00\x88cairo_font_extents_t',b'\x00\x00\x00\x89cairo_font_face_t',b'\x00\x00\x00\x8Acairo_font_options_t',b'\x00\x00\x00\x8Bcairo_font_slant_t',b'\x00\x00\x00\x8Ccairo_font_type_t',b'\x00\x00\x00\x8Dcairo_font_weight_t',b'\x00\x00\x00\x8Ecairo_format_t',b'\x00\x00\x00\x90cairo_glyph_t',b'\x00\x00\x00\x91cairo_hint_metrics_t',b'\x00\x00\x00\x92cairo_hint_style_t',b'\x00\x00\x00\x93cairo_line_cap_t',b'\x00\x00\x00\x94cairo_line_join_t',b'\x00\x00\x00\x95cairo_matrix_t',b'\x00\x00\x00\x96cairo_operator_t',b'\x00\x00\x00\x97cairo_path_data_t',b'\x00\x00\x00\x98cairo_path_data_type_t',b'\x00\x00\x00\x99cairo_path_t',b'\x00\x00\x00\x9Acairo_pattern_t',b'\x00\x00\x00\x9Bcairo_pattern_type_t',b'\x00\x00\x00\x9Ccairo_pdf_metadata_t',b'\x00\x00\x00\x9Dcairo_pdf_outline_flags_t',b'\x00\x00\x00\x9Ecairo_pdf_version_t',b'\x00\x00\x00\x9Fcairo_ps_level_t',b'\x00\x00\x00\xB1cairo_raster_source_acquire_func_t',b'\x00\x00\x00\xA7cairo_raster_source_copy_func_t',b'\x00\x00\x00\xBFcairo_raster_source_finish_func_t',b'\x00\x00\x00\xC0cairo_raster_source_release_func_t',b'\x00\x00\x00\xA6cairo_raster_source_snapshot_func_t',b'\x00\x00\x00\xACcairo_read_func_t',b'\x00\x00\x00\xA0cairo_rectangle_int_t',b'\x00\x00\x00\xA1cairo_rectangle_list_t',b'\x00\x00\x00\xA2cairo_rectangle_t',b'\x00\x00\x00\xA3cairo_region_overlap_t',b'\x00\x00\x00\xA4cairo_region_t',b'\x00\x00\x00\xA5cairo_scaled_font_t',b'\x00\x00\x00\xAEcairo_status_t',b'\x00\x00\x00\xAFcairo_subpixel_order_t',b'\x00\x00\x00\xC1cairo_surface_observer_callback_t',b'\x00\x00\x00\xB0cairo_surface_observer_mode_t',b'\x00\x00\x00\xB2cairo_surface_t',b'\x00\x00\x00\xB3cairo_surface_type_t',b'\x00\x00\x00\xB4cairo_svg_unit_t',b'\x00\x00\x00\xB5cairo_svg_version_t',b'\x00\x00\x00\xB6cairo_t',b'\x00\x00\x00\xB7cairo_text_cluster_flags_t',b'\x00\x00\x00\xB9cairo_text_cluster_t',b'\x00\x00\x00\xBAcairo_text_extents_t',b'\x00\x00\x00\xBBcairo_user_data_key_t',b'\x00\x00\x00\xA8cairo_user_scaled_font_init_func_t',b'\x00\x00\x00\xAAcairo_user_scaled_font_render_glyph_func_t',b'\x00\x00\x00\xA9cairo_user_scaled_font_text_to_glyphs_func_t',b'\x00\x00\x00\xABcairo_user_scaled_font_unicode_to_glyph_func_t',b'\x00\x00\x00\xADcairo_write_func_t',b'\x00\x00\x00\x1Cgboolean',b'\x00\x00\x00\xBDgchar',b'\x00\x00\x00\x1Cgint',b'\x00\x00\x00\x0Dgpointer',b'\x00\x00\x00\x25gsize',b'\x00\x00\x00\xBEguchar',b'\x00\x00\x00\x31guint',b'\x00\x00\x00\x31guint32'),
    _includes = (_ffi0,),
)