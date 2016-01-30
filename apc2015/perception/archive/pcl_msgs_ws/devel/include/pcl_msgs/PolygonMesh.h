/* Software License Agreement (BSD License)
 *
 * Copyright (c) 2011, Willow Garage, Inc.
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 *
 *  * Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 *  * Redistributions in binary form must reproduce the above
 *    copyright notice, this list of conditions and the following
 *    disclaimer in the documentation and/or other materials provided
 *    with the distribution.
 *  * Neither the name of Willow Garage, Inc. nor the names of its
 *    contributors may be used to endorse or promote products derived
 *    from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 * "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 * LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
 * FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 * COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
 * INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
 * BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 * LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
 * CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
 * ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
 *
 * Auto-generated by genmsg_cpp from file /home/motion/ece590-s2015/perception/pcl_msgs_ws/src/pcl_msgs/msg/PolygonMesh.msg
 *
 */


#ifndef PCL_MSGS_MESSAGE_POLYGONMESH_H
#define PCL_MSGS_MESSAGE_POLYGONMESH_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>
#include <sensor_msgs/PointCloud2.h>
#include <pcl_msgs/Vertices.h>

namespace pcl_msgs
{
template <class ContainerAllocator>
struct PolygonMesh_
{
  typedef PolygonMesh_<ContainerAllocator> Type;

  PolygonMesh_()
    : header()
    , cloud()
    , polygons()  {
    }
  PolygonMesh_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , cloud(_alloc)
    , polygons(_alloc)  {
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef  ::sensor_msgs::PointCloud2_<ContainerAllocator>  _cloud_type;
  _cloud_type cloud;

   typedef std::vector< ::pcl_msgs::Vertices_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::pcl_msgs::Vertices_<ContainerAllocator> >::other >  _polygons_type;
  _polygons_type polygons;




  typedef boost::shared_ptr< ::pcl_msgs::PolygonMesh_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::pcl_msgs::PolygonMesh_<ContainerAllocator> const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;

}; // struct PolygonMesh_

typedef ::pcl_msgs::PolygonMesh_<std::allocator<void> > PolygonMesh;

typedef boost::shared_ptr< ::pcl_msgs::PolygonMesh > PolygonMeshPtr;
typedef boost::shared_ptr< ::pcl_msgs::PolygonMesh const> PolygonMeshConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::pcl_msgs::PolygonMesh_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::pcl_msgs::PolygonMesh_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace pcl_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': True}
// {'std_msgs': ['/opt/ros/hydro/share/std_msgs/cmake/../msg'], 'pcl_msgs': ['/home/motion/ece590-s2015/perception/pcl_msgs_ws/src/pcl_msgs/msg'], 'sensor_msgs': ['/opt/ros/hydro/share/sensor_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/hydro/share/geometry_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::pcl_msgs::PolygonMesh_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::pcl_msgs::PolygonMesh_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::pcl_msgs::PolygonMesh_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::pcl_msgs::PolygonMesh_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pcl_msgs::PolygonMesh_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pcl_msgs::PolygonMesh_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::pcl_msgs::PolygonMesh_<ContainerAllocator> >
{
  static const char* value()
  {
    return "45a5fc6ad2cde8489600a790acc9a38a";
  }

  static const char* value(const ::pcl_msgs::PolygonMesh_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x45a5fc6ad2cde848ULL;
  static const uint64_t static_value2 = 0x9600a790acc9a38aULL;
};

template<class ContainerAllocator>
struct DataType< ::pcl_msgs::PolygonMesh_<ContainerAllocator> >
{
  static const char* value()
  {
    return "pcl_msgs/PolygonMesh";
  }

  static const char* value(const ::pcl_msgs::PolygonMesh_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::pcl_msgs::PolygonMesh_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# Separate header for the polygonal surface\n\
Header header\n\
# Vertices of the mesh as a point cloud\n\
sensor_msgs/PointCloud2 cloud\n\
# List of polygons\n\
Vertices[] polygons\n\
\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.secs: seconds (stamp_secs) since epoch\n\
# * stamp.nsecs: nanoseconds since stamp_secs\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
\n\
================================================================================\n\
MSG: sensor_msgs/PointCloud2\n\
# This message holds a collection of N-dimensional points, which may\n\
# contain additional information such as normals, intensity, etc. The\n\
# point data is stored as a binary blob, its layout described by the\n\
# contents of the \"fields\" array.\n\
\n\
# The point cloud data may be organized 2d (image-like) or 1d\n\
# (unordered). Point clouds organized as 2d images may be produced by\n\
# camera depth sensors such as stereo or time-of-flight.\n\
\n\
# Time of sensor data acquisition, and the coordinate frame ID (for 3d\n\
# points).\n\
Header header\n\
\n\
# 2D structure of the point cloud. If the cloud is unordered, height is\n\
# 1 and width is the length of the point cloud.\n\
uint32 height\n\
uint32 width\n\
\n\
# Describes the channels and their layout in the binary data blob.\n\
PointField[] fields\n\
\n\
bool    is_bigendian # Is this data bigendian?\n\
uint32  point_step   # Length of a point in bytes\n\
uint32  row_step     # Length of a row in bytes\n\
uint8[] data         # Actual point data, size is (row_step*height)\n\
\n\
bool is_dense        # True if there are no invalid points\n\
\n\
================================================================================\n\
MSG: sensor_msgs/PointField\n\
# This message holds the description of one point entry in the\n\
# PointCloud2 message format.\n\
uint8 INT8    = 1\n\
uint8 UINT8   = 2\n\
uint8 INT16   = 3\n\
uint8 UINT16  = 4\n\
uint8 INT32   = 5\n\
uint8 UINT32  = 6\n\
uint8 FLOAT32 = 7\n\
uint8 FLOAT64 = 8\n\
\n\
string name      # Name of field\n\
uint32 offset    # Offset from start of point struct\n\
uint8  datatype  # Datatype enumeration, see above\n\
uint32 count     # How many elements in the field\n\
\n\
================================================================================\n\
MSG: pcl_msgs/Vertices\n\
# List of point indices\n\
uint32[] vertices\n\
";
  }

  static const char* value(const ::pcl_msgs::PolygonMesh_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::pcl_msgs::PolygonMesh_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.cloud);
      stream.next(m.polygons);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER;
  }; // struct PolygonMesh_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::pcl_msgs::PolygonMesh_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::pcl_msgs::PolygonMesh_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "cloud: ";
    s << std::endl;
    Printer< ::sensor_msgs::PointCloud2_<ContainerAllocator> >::stream(s, indent + "  ", v.cloud);
    s << indent << "polygons[]" << std::endl;
    for (size_t i = 0; i < v.polygons.size(); ++i)
    {
      s << indent << "  polygons[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::pcl_msgs::Vertices_<ContainerAllocator> >::stream(s, indent + "    ", v.polygons[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // PCL_MSGS_MESSAGE_POLYGONMESH_H
