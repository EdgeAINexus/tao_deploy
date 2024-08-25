# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nvidia_tao_deploy/cv/retinanet/proto/retinanet_config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='nvidia_tao_deploy/cv/retinanet/proto/retinanet_config.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n;nvidia_tao_deploy/cv/retinanet/proto/retinanet_config.proto\"\xfa\x03\n\x0fRetinaNetConfig\x12\x15\n\raspect_ratios\x18\x01 \x01(\t\x12\x1c\n\x14\x61spect_ratios_global\x18\x02 \x01(\t\x12\x0e\n\x06scales\x18\x03 \x01(\t\x12\x11\n\tmin_scale\x18\x04 \x01(\x02\x12\x11\n\tmax_scale\x18\x05 \x01(\x02\x12\x19\n\x11two_boxes_for_ar1\x18\x06 \x01(\x08\x12\r\n\x05steps\x18\x07 \x01(\t\x12\x12\n\nclip_boxes\x18\x08 \x01(\x08\x12\x11\n\tvariances\x18\t \x01(\t\x12\x0f\n\x07offsets\x18\n \x01(\t\x12\x12\n\nmean_color\x18\x0b \x01(\t\x12\x0c\n\x04\x61rch\x18\x0c \x01(\t\x12\x17\n\x0floss_loc_weight\x18\r \x01(\x02\x12\x18\n\x10\x66ocal_loss_alpha\x18\x0e \x01(\x02\x12\x18\n\x10\x66ocal_loss_gamma\x18\x0f \x01(\x02\x12\x15\n\rfreeze_blocks\x18\x10 \x03(\x02\x12\x11\n\tfreeze_bn\x18\x11 \x01(\x08\x12\x0f\n\x07nlayers\x18\x12 \x01(\r\x12\x11\n\tn_kernels\x18\x13 \x01(\r\x12\x14\n\x0c\x66\x65\x61ture_size\x18\x14 \x01(\r\x12\x16\n\x0epos_iou_thresh\x18\x15 \x01(\x02\x12\x16\n\x0eneg_iou_thresh\x18\x16 \x01(\x02\x12\x17\n\x0fn_anchor_levels\x18\x17 \x01(\rb\x06proto3')
)




_RETINANETCONFIG = _descriptor.Descriptor(
  name='RetinaNetConfig',
  full_name='RetinaNetConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='aspect_ratios', full_name='RetinaNetConfig.aspect_ratios', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='aspect_ratios_global', full_name='RetinaNetConfig.aspect_ratios_global', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scales', full_name='RetinaNetConfig.scales', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_scale', full_name='RetinaNetConfig.min_scale', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_scale', full_name='RetinaNetConfig.max_scale', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='two_boxes_for_ar1', full_name='RetinaNetConfig.two_boxes_for_ar1', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='steps', full_name='RetinaNetConfig.steps', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clip_boxes', full_name='RetinaNetConfig.clip_boxes', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='variances', full_name='RetinaNetConfig.variances', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offsets', full_name='RetinaNetConfig.offsets', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mean_color', full_name='RetinaNetConfig.mean_color', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='arch', full_name='RetinaNetConfig.arch', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='loss_loc_weight', full_name='RetinaNetConfig.loss_loc_weight', index=12,
      number=13, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='focal_loss_alpha', full_name='RetinaNetConfig.focal_loss_alpha', index=13,
      number=14, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='focal_loss_gamma', full_name='RetinaNetConfig.focal_loss_gamma', index=14,
      number=15, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='freeze_blocks', full_name='RetinaNetConfig.freeze_blocks', index=15,
      number=16, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='freeze_bn', full_name='RetinaNetConfig.freeze_bn', index=16,
      number=17, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nlayers', full_name='RetinaNetConfig.nlayers', index=17,
      number=18, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='n_kernels', full_name='RetinaNetConfig.n_kernels', index=18,
      number=19, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='feature_size', full_name='RetinaNetConfig.feature_size', index=19,
      number=20, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pos_iou_thresh', full_name='RetinaNetConfig.pos_iou_thresh', index=20,
      number=21, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='neg_iou_thresh', full_name='RetinaNetConfig.neg_iou_thresh', index=21,
      number=22, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='n_anchor_levels', full_name='RetinaNetConfig.n_anchor_levels', index=22,
      number=23, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=64,
  serialized_end=570,
)

DESCRIPTOR.message_types_by_name['RetinaNetConfig'] = _RETINANETCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RetinaNetConfig = _reflection.GeneratedProtocolMessageType('RetinaNetConfig', (_message.Message,), dict(
  DESCRIPTOR = _RETINANETCONFIG,
  __module__ = 'nvidia_tao_deploy.cv.retinanet.proto.retinanet_config_pb2'
  # @@protoc_insertion_point(class_scope:RetinaNetConfig)
  ))
_sym_db.RegisterMessage(RetinaNetConfig)


# @@protoc_insertion_point(module_scope)
