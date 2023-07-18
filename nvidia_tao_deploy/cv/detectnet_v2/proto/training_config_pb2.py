# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nvidia_tao_deploy/cv/detectnet_v2/proto/training_config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from nvidia_tao_deploy.cv.detectnet_v2.proto import cost_scaling_config_pb2 as nvidia__tao__deploy_dot_cv_dot_detectnet__v2_dot_proto_dot_cost__scaling__config__pb2
from nvidia_tao_deploy.cv.detectnet_v2.proto import learning_rate_config_pb2 as nvidia__tao__deploy_dot_cv_dot_detectnet__v2_dot_proto_dot_learning__rate__config__pb2
from nvidia_tao_deploy.cv.detectnet_v2.proto import optimizer_config_pb2 as nvidia__tao__deploy_dot_cv_dot_detectnet__v2_dot_proto_dot_optimizer__config__pb2
from nvidia_tao_deploy.cv.detectnet_v2.proto import regularizer_config_pb2 as nvidia__tao__deploy_dot_cv_dot_detectnet__v2_dot_proto_dot_regularizer__config__pb2
from nvidia_tao_deploy.cv.detectnet_v2.proto import visualizer_config_pb2 as nvidia__tao__deploy_dot_cv_dot_detectnet__v2_dot_proto_dot_visualizer__config__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='nvidia_tao_deploy/cv/detectnet_v2/proto/training_config.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n=nvidia_tao_deploy/cv/detectnet_v2/proto/training_config.proto\x1a\x41nvidia_tao_deploy/cv/detectnet_v2/proto/cost_scaling_config.proto\x1a\x42nvidia_tao_deploy/cv/detectnet_v2/proto/learning_rate_config.proto\x1a>nvidia_tao_deploy/cv/detectnet_v2/proto/optimizer_config.proto\x1a@nvidia_tao_deploy/cv/detectnet_v2/proto/regularizer_config.proto\x1a?nvidia_tao_deploy/cv/detectnet_v2/proto/visualizer_config.proto\"\xbc\x02\n\x0eTrainingConfig\x12\x1a\n\x12\x62\x61tch_size_per_gpu\x18\x01 \x01(\r\x12\x12\n\nnum_epochs\x18\x02 \x01(\r\x12*\n\rlearning_rate\x18\x03 \x01(\x0b\x32\x13.LearningRateConfig\x12\'\n\x0bregularizer\x18\x04 \x01(\x0b\x32\x12.RegularizerConfig\x12#\n\toptimizer\x18\x05 \x01(\x0b\x32\x10.OptimizerConfig\x12(\n\x0c\x63ost_scaling\x18\x06 \x01(\x0b\x32\x12.CostScalingConfig\x12\x1b\n\x13\x63heckpoint_interval\x18\x07 \x01(\r\x12\x12\n\nenable_qat\x18\x08 \x01(\x08\x12%\n\nvisualizer\x18\t \x01(\x0b\x32\x11.VisualizerConfigb\x06proto3')
  ,
  dependencies=[nvidia__tao__deploy_dot_cv_dot_detectnet__v2_dot_proto_dot_cost__scaling__config__pb2.DESCRIPTOR,nvidia__tao__deploy_dot_cv_dot_detectnet__v2_dot_proto_dot_learning__rate__config__pb2.DESCRIPTOR,nvidia__tao__deploy_dot_cv_dot_detectnet__v2_dot_proto_dot_optimizer__config__pb2.DESCRIPTOR,nvidia__tao__deploy_dot_cv_dot_detectnet__v2_dot_proto_dot_regularizer__config__pb2.DESCRIPTOR,nvidia__tao__deploy_dot_cv_dot_detectnet__v2_dot_proto_dot_visualizer__config__pb2.DESCRIPTOR,])




_TRAININGCONFIG = _descriptor.Descriptor(
  name='TrainingConfig',
  full_name='TrainingConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='batch_size_per_gpu', full_name='TrainingConfig.batch_size_per_gpu', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_epochs', full_name='TrainingConfig.num_epochs', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='learning_rate', full_name='TrainingConfig.learning_rate', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='regularizer', full_name='TrainingConfig.regularizer', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='optimizer', full_name='TrainingConfig.optimizer', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cost_scaling', full_name='TrainingConfig.cost_scaling', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='checkpoint_interval', full_name='TrainingConfig.checkpoint_interval', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enable_qat', full_name='TrainingConfig.enable_qat', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='visualizer', full_name='TrainingConfig.visualizer', index=8,
      number=9, type=11, cpp_type=10, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=396,
  serialized_end=712,
)

_TRAININGCONFIG.fields_by_name['learning_rate'].message_type = nvidia__tao__deploy_dot_cv_dot_detectnet__v2_dot_proto_dot_learning__rate__config__pb2._LEARNINGRATECONFIG
_TRAININGCONFIG.fields_by_name['regularizer'].message_type = nvidia__tao__deploy_dot_cv_dot_detectnet__v2_dot_proto_dot_regularizer__config__pb2._REGULARIZERCONFIG
_TRAININGCONFIG.fields_by_name['optimizer'].message_type = nvidia__tao__deploy_dot_cv_dot_detectnet__v2_dot_proto_dot_optimizer__config__pb2._OPTIMIZERCONFIG
_TRAININGCONFIG.fields_by_name['cost_scaling'].message_type = nvidia__tao__deploy_dot_cv_dot_detectnet__v2_dot_proto_dot_cost__scaling__config__pb2._COSTSCALINGCONFIG
_TRAININGCONFIG.fields_by_name['visualizer'].message_type = nvidia__tao__deploy_dot_cv_dot_detectnet__v2_dot_proto_dot_visualizer__config__pb2._VISUALIZERCONFIG
DESCRIPTOR.message_types_by_name['TrainingConfig'] = _TRAININGCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TrainingConfig = _reflection.GeneratedProtocolMessageType('TrainingConfig', (_message.Message,), dict(
  DESCRIPTOR = _TRAININGCONFIG,
  __module__ = 'nvidia_tao_deploy.cv.detectnet_v2.proto.training_config_pb2'
  # @@protoc_insertion_point(class_scope:TrainingConfig)
  ))
_sym_db.RegisterMessage(TrainingConfig)


# @@protoc_insertion_point(module_scope)