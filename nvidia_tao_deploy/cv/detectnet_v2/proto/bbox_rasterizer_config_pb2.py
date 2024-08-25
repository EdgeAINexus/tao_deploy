# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nvidia_tao_deploy/cv/detectnet_v2/proto/bbox_rasterizer_config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='nvidia_tao_deploy/cv/detectnet_v2/proto/bbox_rasterizer_config.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nDnvidia_tao_deploy/cv/detectnet_v2/proto/bbox_rasterizer_config.proto\"\xe4\x02\n\x14\x42\x62oxRasterizerConfig\x12I\n\x13target_class_config\x18\x01 \x03(\x0b\x32,.BboxRasterizerConfig.TargetClassConfigEntry\x12\x17\n\x0f\x64\x65\x61\x64zone_radius\x18\x02 \x01(\x02\x1a\x84\x01\n\x11TargetClassConfig\x12\x14\n\x0c\x63ov_center_x\x18\x01 \x01(\x02\x12\x14\n\x0c\x63ov_center_y\x18\x02 \x01(\x02\x12\x14\n\x0c\x63ov_radius_x\x18\x03 \x01(\x02\x12\x14\n\x0c\x63ov_radius_y\x18\x04 \x01(\x02\x12\x17\n\x0f\x62\x62ox_min_radius\x18\x05 \x01(\x02\x1a\x61\n\x16TargetClassConfigEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x36\n\x05value\x18\x02 \x01(\x0b\x32\'.BboxRasterizerConfig.TargetClassConfig:\x02\x38\x01\x62\x06proto3')
)




_BBOXRASTERIZERCONFIG_TARGETCLASSCONFIG = _descriptor.Descriptor(
  name='TargetClassConfig',
  full_name='BboxRasterizerConfig.TargetClassConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cov_center_x', full_name='BboxRasterizerConfig.TargetClassConfig.cov_center_x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cov_center_y', full_name='BboxRasterizerConfig.TargetClassConfig.cov_center_y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cov_radius_x', full_name='BboxRasterizerConfig.TargetClassConfig.cov_radius_x', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cov_radius_y', full_name='BboxRasterizerConfig.TargetClassConfig.cov_radius_y', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bbox_min_radius', full_name='BboxRasterizerConfig.TargetClassConfig.bbox_min_radius', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=198,
  serialized_end=330,
)

_BBOXRASTERIZERCONFIG_TARGETCLASSCONFIGENTRY = _descriptor.Descriptor(
  name='TargetClassConfigEntry',
  full_name='BboxRasterizerConfig.TargetClassConfigEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='BboxRasterizerConfig.TargetClassConfigEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='BboxRasterizerConfig.TargetClassConfigEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=332,
  serialized_end=429,
)

_BBOXRASTERIZERCONFIG = _descriptor.Descriptor(
  name='BboxRasterizerConfig',
  full_name='BboxRasterizerConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target_class_config', full_name='BboxRasterizerConfig.target_class_config', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deadzone_radius', full_name='BboxRasterizerConfig.deadzone_radius', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_BBOXRASTERIZERCONFIG_TARGETCLASSCONFIG, _BBOXRASTERIZERCONFIG_TARGETCLASSCONFIGENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=73,
  serialized_end=429,
)

_BBOXRASTERIZERCONFIG_TARGETCLASSCONFIG.containing_type = _BBOXRASTERIZERCONFIG
_BBOXRASTERIZERCONFIG_TARGETCLASSCONFIGENTRY.fields_by_name['value'].message_type = _BBOXRASTERIZERCONFIG_TARGETCLASSCONFIG
_BBOXRASTERIZERCONFIG_TARGETCLASSCONFIGENTRY.containing_type = _BBOXRASTERIZERCONFIG
_BBOXRASTERIZERCONFIG.fields_by_name['target_class_config'].message_type = _BBOXRASTERIZERCONFIG_TARGETCLASSCONFIGENTRY
DESCRIPTOR.message_types_by_name['BboxRasterizerConfig'] = _BBOXRASTERIZERCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BboxRasterizerConfig = _reflection.GeneratedProtocolMessageType('BboxRasterizerConfig', (_message.Message,), dict(

  TargetClassConfig = _reflection.GeneratedProtocolMessageType('TargetClassConfig', (_message.Message,), dict(
    DESCRIPTOR = _BBOXRASTERIZERCONFIG_TARGETCLASSCONFIG,
    __module__ = 'nvidia_tao_deploy.cv.detectnet_v2.proto.bbox_rasterizer_config_pb2'
    # @@protoc_insertion_point(class_scope:BboxRasterizerConfig.TargetClassConfig)
    ))
  ,

  TargetClassConfigEntry = _reflection.GeneratedProtocolMessageType('TargetClassConfigEntry', (_message.Message,), dict(
    DESCRIPTOR = _BBOXRASTERIZERCONFIG_TARGETCLASSCONFIGENTRY,
    __module__ = 'nvidia_tao_deploy.cv.detectnet_v2.proto.bbox_rasterizer_config_pb2'
    # @@protoc_insertion_point(class_scope:BboxRasterizerConfig.TargetClassConfigEntry)
    ))
  ,
  DESCRIPTOR = _BBOXRASTERIZERCONFIG,
  __module__ = 'nvidia_tao_deploy.cv.detectnet_v2.proto.bbox_rasterizer_config_pb2'
  # @@protoc_insertion_point(class_scope:BboxRasterizerConfig)
  ))
_sym_db.RegisterMessage(BboxRasterizerConfig)
_sym_db.RegisterMessage(BboxRasterizerConfig.TargetClassConfig)
_sym_db.RegisterMessage(BboxRasterizerConfig.TargetClassConfigEntry)


_BBOXRASTERIZERCONFIG_TARGETCLASSCONFIGENTRY._options = None
# @@protoc_insertion_point(module_scope)
