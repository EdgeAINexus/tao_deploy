# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nvidia_tao_deploy/cv/yolo_v4/proto/experiment.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from nvidia_tao_deploy.cv.yolo_v4.proto import augmentation_config_pb2 as nvidia__tao__deploy_dot_cv_dot_yolo__v4_dot_proto_dot_augmentation__config__pb2
from nvidia_tao_deploy.cv.yolo_v3.proto import dataset_config_pb2 as nvidia__tao__deploy_dot_cv_dot_yolo__v3_dot_proto_dot_dataset__config__pb2
from nvidia_tao_deploy.cv.common.proto import training_config_pb2 as nvidia__tao__deploy_dot_cv_dot_common_dot_proto_dot_training__config__pb2
from nvidia_tao_deploy.cv.common.proto import eval_config_pb2 as nvidia__tao__deploy_dot_cv_dot_common_dot_proto_dot_eval__config__pb2
from nvidia_tao_deploy.cv.common.proto import nms_config_pb2 as nvidia__tao__deploy_dot_cv_dot_common_dot_proto_dot_nms__config__pb2
from nvidia_tao_deploy.cv.common.proto import class_weighting_config_pb2 as nvidia__tao__deploy_dot_cv_dot_common_dot_proto_dot_class__weighting__config__pb2
from nvidia_tao_deploy.cv.yolo_v4.proto import yolov4_config_pb2 as nvidia__tao__deploy_dot_cv_dot_yolo__v4_dot_proto_dot_yolov4__config__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='nvidia_tao_deploy/cv/yolo_v4/proto/experiment.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n3nvidia_tao_deploy/cv/yolo_v4/proto/experiment.proto\x1a<nvidia_tao_deploy/cv/yolo_v4/proto/augmentation_config.proto\x1a\x37nvidia_tao_deploy/cv/yolo_v3/proto/dataset_config.proto\x1a\x37nvidia_tao_deploy/cv/common/proto/training_config.proto\x1a\x33nvidia_tao_deploy/cv/common/proto/eval_config.proto\x1a\x32nvidia_tao_deploy/cv/common/proto/nms_config.proto\x1a>nvidia_tao_deploy/cv/common/proto/class_weighting_config.proto\x1a\x36nvidia_tao_deploy/cv/yolo_v4/proto/yolov4_config.proto\"\xca\x02\n\nExperiment\x12,\n\x0e\x64\x61taset_config\x18\x01 \x01(\x0b\x32\x14.YOLOv3DatasetConfig\x12\x30\n\x13\x61ugmentation_config\x18\x02 \x01(\x0b\x32\x13.AugmentationConfig\x12(\n\x0ftraining_config\x18\x03 \x01(\x0b\x32\x0f.TrainingConfig\x12 \n\x0b\x65val_config\x18\x04 \x01(\x0b\x32\x0b.EvalConfig\x12\x1e\n\nnms_config\x18\x05 \x01(\x0b\x32\n.NMSConfig\x12$\n\ryolov4_config\x18\x06 \x01(\x0b\x32\r.YOLOv4Config\x12\x35\n\x16\x63lass_weighting_config\x18\x08 \x01(\x0b\x32\x15.ClassWeightingConfig\x12\x13\n\x0brandom_seed\x18\x07 \x01(\rb\x06proto3')
  ,
  dependencies=[nvidia__tao__deploy_dot_cv_dot_yolo__v4_dot_proto_dot_augmentation__config__pb2.DESCRIPTOR,nvidia__tao__deploy_dot_cv_dot_yolo__v3_dot_proto_dot_dataset__config__pb2.DESCRIPTOR,nvidia__tao__deploy_dot_cv_dot_common_dot_proto_dot_training__config__pb2.DESCRIPTOR,nvidia__tao__deploy_dot_cv_dot_common_dot_proto_dot_eval__config__pb2.DESCRIPTOR,nvidia__tao__deploy_dot_cv_dot_common_dot_proto_dot_nms__config__pb2.DESCRIPTOR,nvidia__tao__deploy_dot_cv_dot_common_dot_proto_dot_class__weighting__config__pb2.DESCRIPTOR,nvidia__tao__deploy_dot_cv_dot_yolo__v4_dot_proto_dot_yolov4__config__pb2.DESCRIPTOR,])




_EXPERIMENT = _descriptor.Descriptor(
  name='Experiment',
  full_name='Experiment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dataset_config', full_name='Experiment.dataset_config', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='augmentation_config', full_name='Experiment.augmentation_config', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='training_config', full_name='Experiment.training_config', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='eval_config', full_name='Experiment.eval_config', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nms_config', full_name='Experiment.nms_config', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='yolov4_config', full_name='Experiment.yolov4_config', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='class_weighting_config', full_name='Experiment.class_weighting_config', index=6,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='random_seed', full_name='Experiment.random_seed', index=7,
      number=7, type=13, cpp_type=3, label=1,
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
  serialized_start=457,
  serialized_end=787,
)

_EXPERIMENT.fields_by_name['dataset_config'].message_type = nvidia__tao__deploy_dot_cv_dot_yolo__v3_dot_proto_dot_dataset__config__pb2._YOLOV3DATASETCONFIG
_EXPERIMENT.fields_by_name['augmentation_config'].message_type = nvidia__tao__deploy_dot_cv_dot_yolo__v4_dot_proto_dot_augmentation__config__pb2._AUGMENTATIONCONFIG
_EXPERIMENT.fields_by_name['training_config'].message_type = nvidia__tao__deploy_dot_cv_dot_common_dot_proto_dot_training__config__pb2._TRAININGCONFIG
_EXPERIMENT.fields_by_name['eval_config'].message_type = nvidia__tao__deploy_dot_cv_dot_common_dot_proto_dot_eval__config__pb2._EVALCONFIG
_EXPERIMENT.fields_by_name['nms_config'].message_type = nvidia__tao__deploy_dot_cv_dot_common_dot_proto_dot_nms__config__pb2._NMSCONFIG
_EXPERIMENT.fields_by_name['yolov4_config'].message_type = nvidia__tao__deploy_dot_cv_dot_yolo__v4_dot_proto_dot_yolov4__config__pb2._YOLOV4CONFIG
_EXPERIMENT.fields_by_name['class_weighting_config'].message_type = nvidia__tao__deploy_dot_cv_dot_common_dot_proto_dot_class__weighting__config__pb2._CLASSWEIGHTINGCONFIG
DESCRIPTOR.message_types_by_name['Experiment'] = _EXPERIMENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Experiment = _reflection.GeneratedProtocolMessageType('Experiment', (_message.Message,), dict(
  DESCRIPTOR = _EXPERIMENT,
  __module__ = 'nvidia_tao_deploy.cv.yolo_v4.proto.experiment_pb2'
  # @@protoc_insertion_point(class_scope:Experiment)
  ))
_sym_db.RegisterMessage(Experiment)


# @@protoc_insertion_point(module_scope)
