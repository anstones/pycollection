# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import lwz_model_pb2 as lwz__model__pb2


class modelStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.lwz_show = channel.unary_unary(
        '/lwz_example.model/lwz_show',
        request_serializer=lwz__model__pb2.lwz_Request.SerializeToString,
        response_deserializer=lwz__model__pb2.lwz_Response.FromString,
        )


class modelServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def lwz_show(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_modelServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'lwz_show': grpc.unary_unary_rpc_method_handler(
          servicer.lwz_show,
          request_deserializer=lwz__model__pb2.lwz_Request.FromString,
          response_serializer=lwz__model__pb2.lwz_Response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'lwz_example.model', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
