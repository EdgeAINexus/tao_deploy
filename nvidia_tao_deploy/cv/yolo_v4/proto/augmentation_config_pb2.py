# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nvidia_tao_deploy/cv/yolo_v4/proto/augmentation_config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='nvidia_tao_deploy/cv/yolo_v4/proto/augmentation_config.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n<nvidia_tao_deploy/cv/yolo_v4/proto/augmentation_config.proto\"\xa1\x03\n\x12\x41ugmentationConfig\x12\x0b\n\x03hue\x18\x01 \x01(\x02\x12\x12\n\nsaturation\x18\x02 \x01(\x02\x12\x10\n\x08\x65xposure\x18\x03 \x01(\x02\x12\x15\n\rvertical_flip\x18\x04 \x01(\x02\x12\x17\n\x0fhorizontal_flip\x18\x05 \x01(\x02\x12\x0e\n\x06jitter\x18\x06 \x01(\x02\x12\x14\n\x0coutput_width\x18\x07 \x01(\x05\x12\x15\n\routput_height\x18\x08 \x01(\x05\x12\x16\n\x0eoutput_channel\x18\t \x01(\x05\x12\x14\n\x0coutput_depth\x18\x0e \x01(\r\x12$\n\x1crandomize_input_shape_period\x18\n \x01(\x05\x12\x13\n\x0bmosaic_prob\x18\x0b \x01(\x02\x12\x18\n\x10mosaic_min_ratio\x18\x0c \x01(\x02\x12\x36\n\nimage_mean\x18\r \x03(\x0b\x32\".AugmentationConfig.ImageMeanEntry\x1a\x30\n\x0eImageMeanEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02:\x02\x38\x01\x62\x06proto3')
)




_AUGMENTATIONCONFIG_IMAGEMEANENTRY = _descriptor.Descriptor(
  name='ImageMeanEntry',
  full_name='AugmentationConfig.ImageMeanEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='AugmentationConfig.ImageMeanEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='AugmentationConfig.ImageMeanEntry.value', index=1,
      number=2, type=2, cpp_type=6, label=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=434,
  serialized_end=482,
)

_AUGMENTATIONCONFIG = _descriptor.Descriptor(
  name='AugmentationConfig',
  full_name='AugmentationConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hue', full_name='AugmentationConfig.hue', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='saturation', full_name='AugmentationConfig.saturation', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exposure', full_name='AugmentationConfig.exposure', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vertical_flip', full_name='AugmentationConfig.vertical_flip', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='horizontal_flip', full_name='AugmentationConfig.horizontal_flip', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='jitter', full_name='AugmentationConfig.jitter', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output_width', full_name='AugmentationConfig.output_width', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output_height', full_name='AugmentationConfig.output_height', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output_channel', full_name='AugmentationConfig.output_channel', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output_depth', full_name='AugmentationConfig.output_depth', index=9,
      number=14, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='randomize_input_shape_period', full_name='AugmentationConfig.randomize_input_shape_period', index=10,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mosaic_prob', full_name='AugmentationConfig.mosaic_prob', index=11,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mosaic_min_ratio', full_name='AugmentationConfig.mosaic_min_ratio', index=12,
      number=12, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='image_mean', full_name='AugmentationConfig.image_mean', index=13,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_AUGMENTATIONCONFIG_IMAGEMEANENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=65,
  serialized_end=482,
)

_AUGMENTATIONCONFIG_IMAGEMEANENTRY.containing_type = _AUGMENTATIONCONFIG
_AUGMENTATIONCONFIG.fields_by_name['image_mean'].message_type = _AUGMENTATIONCONFIG_IMAGEMEANENTRY
DESCRIPTOR.message_types_by_name['AugmentationConfig'] = _AUGMENTATIONCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AugmentationConfig = _reflection.GeneratedProtocolMessageType('AugmentationConfig', (_message.Message,), dict(

  ImageMeanEntry = _reflection.GeneratedProtocolMessageType('ImageMeanEntry', (_message.Message,), dict(
    DESCRIPTOR = _AUGMENTATIONCONFIG_IMAGEMEANENTRY,
    __module__ = 'nvidia_tao_deploy.cv.yolo_v4.proto.augmentation_config_pb2'
    # @@protoc_insertion_point(class_scope:AugmentationConfig.ImageMeanEntry)
    ))
  ,
  DESCRIPTOR = _AUGMENTATIONCONFIG,
  __module__ = 'nvidia_tao_deploy.cv.yolo_v4.proto.augmentation_config_pb2'
  # @@protoc_insertion_point(class_scope:AugmentationConfig)
  ))
_sym_db.RegisterMessage(AugmentationConfig)
_sym_db.RegisterMessage(AugmentationConfig.ImageMeanEntry)


_AUGMENTATIONCONFIG_IMAGEMEANENTRY._options = None
# @@protoc_insertion_point(module_scope)
