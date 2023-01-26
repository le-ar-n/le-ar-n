'''
. . . . . . . . . . . . . . . . . . . . . 
.                                       .
.    <<      ><      ><       >< <<     .
.    < ><   ><<     ><<<    ><    ><<   .
.    << >< > ><    ><  ><     ><        .  
.    <<  ><  ><   ><<<<<><      ><      .
.    <<      >< ><<     ><< ><    ><<   .
.    <<      ><><<       ><<  >< <<     .
.                                       .
.             DFAB 2016/17              .
. . . . . . . . . . . . . . . . . . . . . 

Created on 14.09.2016

@authors: rust & dorf
'''


# =================================================================================    
# this import is only necessary if you execute the file outside of Rhino or Grasshopper
# =================================================================================    
import sys
import clr
import System
import copy

sys.path.append(r"C:\Program Files\Rhinoceros 5 (64-bit)\System")
clr.AddReference('RhinoCommon') 
# ================================================================================= 

import Rhino.Geometry as rg
import math  


class Frame():
    
    def __init__(self, plane = None, draw_geo = False):
        '''
        The class "Frame" is initialized with a Rhino plane.
        It is a generic class, that allows to derive the euler angles (Kuka), axis angle (UR), or quaternions (ABB) from this plane,
        the transformation matrix to and from another plane, and also contains some transformation methods.
        If no plane is given as an input, the origin of the plane is in world XY.
        If draw_geo is set to true: the axes can be visualized as lines (length = 100)
        
        quaternion definition: [qw, qx, qy, qz]
        angle_axis definition: [ax,ay,az] (angle = length of the vector, axis = vector)
        '''       
        self.draw_geo = draw_geo
        if plane:
            self.set_to_plane(plane)
        else:
            self.set_to_worldXY()
                
    def update_geo(self, plane):
        '''
        updates geometry for the axes if draw_geo == True 
        '''
        if self.draw_geo:
            self.x_axis = rg.Line(plane.Origin, plane.XAxis*100)
            self.y_axis = rg.Line(plane.Origin, plane.YAxis*100)
            self.z_axis = rg.Line(plane.Origin, plane.ZAxis*100)     
            self.frame_geo = [self.x_axis, self.y_axis, self.z_axis]
    
    def get_axes_as_lines(self, length = 100):
        '''
        returns the axes of the plane as lines for visualization
        '''
        return [rg.Line(self.plane.Origin, self.plane.XAxis*length), rg.Line(self.plane.Origin, self.plane.YAxis*length), rg.Line(self.plane.Origin, self.plane.ZAxis*length)]
        
    def set_to_worldXY(self):
        '''
        sets the plane with the origin in world XY
        '''
        self.plane = rg.Plane.WorldXY
        self.update_geo(self.plane)
    
    def set_to_plane(self, plane):
        ''' 
        sets the plane of the frame
        '''
        self.plane = rg.Plane(plane)
        self.update_geo(self.plane)
    
    def set_to_tmatrix(self, T):
        '''
        sets the plane of the frame with a transformation matrix from world XY
        '''
        self.plane = rg.Plane.WorldXY
        self.plane.Transform(T)
        self.update_geo(self.plane)
            
    def set_to_pose_quaternion(self, pose_quaternion):
        '''
        sets the plane of the frame with the input of a pose_quaternion
        '''
        x, y, z, qw, qx, qy, qz = pose_quaternion
        self.set_rotation_from_quaternion([qw, qx, qy, qz])
        self.set_to_point3d(rg.Point3d(x, y, z))
    
    def set_to_pose_angle_axis(self, pose_angle_axis):
        '''
        sets the plane of the frame with the input of a pose_angle_axis
        '''
        #TODO: Romana: please fill in according to your conventions. 
        
        x, y, z, ax, ay, az = pose_angle_axis
        self.set_rotation_from_angle_axis(ax, ay, az)
        self.set_to_point3d(rg.Point3d(x, y, z))
    
    def set_to_pose_euler_angles(self, pose_euler_angles):
        '''
        sets the plane of the frame with the input of a pose_euler_angles
        '''
        x, y, z, a, b, c = pose_euler_angles
        self.set_rotation_from_euler_angles(a, b, c)
        self.set_to_point3d(rg.Point3d(x, y, z))
 
    def set_to_point3d(self, point3d):
        '''
        sets the origin of the plane to the point coordinate
        '''
        self.plane.Origin = point3d
        self.update_geo(self.plane)
        
    def get_plane(self):
        '''
        returns the copy of the plane of the frame
        '''
        return rg.Plane(self.plane)
        
    def set_rotation_from_quaternion(self, quaternion):
        '''
        sets the plane's orientation according to the quaternion values, origin is set back to World XY
        '''
        if type(quaternion) <> type(rg.Quaternion()):
            a,b,c,d = quaternion
            quaternion = rg.Quaternion(a,b,c,d)        
        qplane = quaternion.GetRotation()[1]
        self.set_to_plane(qplane)
        
    def set_rotation_from_angle_axis(self, ax, ay, az):
        '''
        sets the plane's orientation according to the angle axis values, origin is set back to World XY
        TODO: Romana: please fill in according to your conventions.
        '''
        
        ex = rg.Vector3d(ax, ay, az)
        R = self.rotation_from_angle_axis(ex)
        self.set_to_tmatrix(R)

    
    def set_rotation_from_euler_angles(self, a, b, c):
        ''' 
        sets the plane's orientation according to the angle axis values, origin is set back to World XY
        TODO: Kathrin or Romana :) '''
        pass
        
    def get_quaternion(self):
        '''
        returns rotation from plane as quaternion (as Rhino quaternion)
        '''     
        # info: unfortunately this does not work, returns None:
        # q = rg.Quaternion.Rotation(rg.Plane.WorldZX, self.plane) / q.SetRotation(plane1, plane2)
        # therefore calculate from Rotation        
        T = rg.Transform.Rotation(rg.Vector3d.XAxis, rg.Vector3d.YAxis, rg.Vector3d.ZAxis, self.plane.XAxis, self.plane.YAxis, self.plane.ZAxis) 
        a, b, c, d = self.rotation_to_quaternion(T)     
        quaternion = rg.Quaternion(a, b, c, d)        
        return quaternion
    
    def get_quaternion_as_list(self):
        '''
        returns rotation from plane as quaternion (as list)
        '''     
        # info: unfortunately this does not work, returns None:
        # q = rg.Quaternion.Rotation(rg.Plane.WorldZX, self.plane) / q.SetRotation(plane1, plane2)
        # therefore calculate from Rotation        
        T = rg.Transform.Rotation(rg.Vector3d.XAxis, rg.Vector3d.YAxis, rg.Vector3d.ZAxis, self.plane.XAxis, self.plane.YAxis, self.plane.ZAxis) 
        return self.rotation_to_quaternion(T)
    
    def get_angle_axis(self):
        '''
        returns rotation from plane as angle axis (as Rhino Vector3d)
        '''
        T = rg.Transform.Rotation(rg.Vector3d.XAxis, rg.Vector3d.YAxis, rg.Vector3d.ZAxis, self.plane.XAxis, self.plane.YAxis, self.plane.ZAxis) 
        angle, axis = self.rotation_to_angle_axis(T)  
        return rg.Vector3d.Multiply(angle, rg.Vector3d(axis[0], axis[1], axis[2])) 
    
    def get_angle_axis_as_list(self):
        '''
        returns rotation from plane as angle axis (as list) 
        '''
        T = rg.Transform.Rotation(rg.Vector3d.XAxis, rg.Vector3d.YAxis, rg.Vector3d.ZAxis, self.plane.XAxis, self.plane.YAxis, self.plane.ZAxis) 
        angle, axis = self.rotation_to_angle_axis(T)
        vec = rg.Vector3d.Multiply(angle, rg.Vector3d(axis[0], axis[1], axis[2]))
        return [vec.X, vec.Y, vec.Z]
    
    def get_euler_angles(self):
        '''
        returns rotation from plane as euler angles (as Rhino Vector3d)
        '''
        T = rg.Transform.Rotation(rg.Vector3d.XAxis, rg.Vector3d.YAxis, rg.Vector3d.ZAxis, self.plane.XAxis, self.plane.YAxis, self.plane.ZAxis) 
        ex, ey, ez = self.rotation_to_euler_angles(T)  
        return rg.Vector3d(ex, ey, ez)
    
    def get_euler_angles_as_list(self):
        '''
        returns rotation from plane as euler angles (as list)
        '''
        T = rg.Transform.Rotation(rg.Vector3d.XAxis, rg.Vector3d.YAxis, rg.Vector3d.ZAxis, self.plane.XAxis, self.plane.YAxis, self.plane.ZAxis) 
        return self.rotation_to_euler_angles(T)
    
    def get_pose_quaternion(self):
        '''
        returns a pose with quaternions as [x,y,z,qw,qx,qy,qz]
        '''
        quaternion = self.get_quaternion()
        point = self.plane.Origin
        return [point.X, point.Y, point.Z, quaternion.A, quaternion.B, quaternion.C, quaternion.D]
    
    def get_pose_angle_axis(self):
        '''
        returns a pose with angle_axis as [x,y,z,ax,ay,az]
        '''
        angle_axis = self.get_angle_axis()
        point = self.plane.Origin
        return [point.X, point.Y, point.Z, angle_axis.X, angle_axis.Y, angle_axis.Z]
    
    def get_pose_euler_angles(self):
        '''
        returns a pose with euler angles as [x,y,z,ex,ey,ez]
        '''
        euler_angles = self.get_euler_angles()
        point = self.plane.Origin
        return [point.X, point.Y, point.Z, euler_angles.X, euler_angles.Y, euler_angles.Z]
    
    def rotation_to_angle_axis(self, T):
        '''
        create angle and axis from matrix,
        references Martin Baker's implementation of matrix to axis angle function at
        http://www.euclideanspace.com/maths/geometry/rotations/conversions/matrixToAngle/index.htm
        ''' 
        
        epsilon = 0.01 # margin to allow for rounding errors
        epsilon2 = 0.1 # margin to distinguish between 0 and 180 degrees
        
        if ((math.fabs(T.M01-T.M10)< epsilon) and \
            (math.fabs(T.M02-T.M20)< epsilon) and \
            (math.fabs(T.M12-T.M21)< epsilon)):
        #singularity found
        #first check for identity matrix which must have +1 for all terms in leading diagonal and zero in other terms
            if ((math.fabs(T.M01+T.M10) < epsilon2) and \
                (math.fabs(T.M02+T.M20) < epsilon2) and \
                (math.fabs(T.M12+T.M21) < epsilon2) and \
                (math.fabs(T.M00+T.M11+T.M22-3) < epsilon2)) :
                # this singularity is identity matrix so angle = 0
                    return 0, (1,0,0) # zero angle, arbitrary axis
            else:
                # otherwise this singularity is angle = 180
                angle = math.pi
                xx = (T.M00+1)/2
                yy = (T.M11+1)/2
                zz = (T.M22+1)/2
                xy = (T.M01+T.M10)/4
                xz = (T.M02+T.M20)/4
                yz = (T.M12+T.M21)/4
                root_half = math.sqrt(0.5)
                if ((xx > yy) and (xx > zz)) : # T.M00 is the largest diagonal term
                    if (xx< epsilon) :
                        axis = (0,root_half,root_half)
                    else:
                        x = math.sqrt(xx)
                        axis = (x,xy/x,xz/x)                    
                elif (yy > zz) : # T.M11 is the largest diagonal term
                    if (yy< epsilon):
                        axis = (root_half,0,root_half)
                    else :
                        y = math.sqrt(yy)
                        axis = (xy/y,y,yz/y)                        
                else : # T.M22 is the largest diagonal term so base result on this
                    if (zz< epsilon) :
                        axis = (root_half,root_half,0)
                    else :
                        z = math.sqrt(zz)
                        axis = (xz/z,yz/z,z)
                                    
                return angle, axis # return 180 degree rotation
    
        # as we have reached here there are no singularities so we can handle normally
        s = math.sqrt(\
            (T.M21 - T.M12)*(T.M21 - T.M12)+
            (T.M02 - T.M20)*(T.M02 - T.M20)+
            (T.M10 - T.M01)*(T.M10 - T.M01)) # used to normalize
        
        # prevent divide by zero, should not happen if matrix is orthogonal and should be
        # caught by singularity test above, but I've left it in just in case
        if (math.fabs(s) < 0.001): s=1
        angle = math.acos((T.M00 + T.M11 + T.M22 - 1)/2)
        
        x = (T.M21 - T.M12)/s
        y = (T.M02 - T.M20)/s
        z = (T.M10 - T.M01)/s
        return angle, (x,y,z)
    
    def rotation_to_quaternion(self, T):
        '''
        create a unit quaternion from matrix as qw, qx, qy, qz,
        references Martin Baker's implementation of matrix to quaternion: 
        http://www.euclideanspace.com/maths/geometry/rotations/conversions/matrixToQuaternion/ 
        '''
        
        qw, qx, qy, qz = 0,0,0,0
        trace = T.M00 + T.M11 + T.M22 # m[0][0] + m[1][1] + m[2][2]
        
        if trace > 0.0:
            # print "case 1"
            s = (0.5 / math.sqrt(trace+1.0)) # s = 0.5f / sqrtf(trace+ 1.0f);
            qw = 0.25 / s # 0.25f / s;
            qx = (T.M21 - T.M12) * s #( a[2][1] - a[1][2] ) * s;
            qy = (T.M02 - T.M20) * s #( a[0][2] - a[2][0] ) * s;
            qz = (T.M10 - T.M01) * s #( a[1][0] - a[0][1] ) * s;
            
        elif ( (T.M00 > T.M11) and (T.M00 > T.M22) ): # ( a[0][0] > a[1][1] && a[0][0] > a[2][2] )
            # print "case 2"
            s = 2.0 * math.sqrt(1.0 + T.M00 - T.M11 - T.M22) # s = 2.0f * sqrtf( 1.0f + a[0][0] - a[1][1] - a[2][2]);
            qw = (T.M21 - T.M12) / s #(a[2][1] - a[1][2] ) / s;
            qx = 0.25 * s #0.25f * s;
            qy = (T.M01 + T.M10) / s #(a[0][1] + a[1][0] ) / s;
            qz = (T.M02 + T.M20) / s #(a[0][2] + a[2][0] ) / s;
            
        elif (T.M11 > T.M22 ): #(a[1][1] > a[2][2]) {
            # print "case 3"
            s = 2.0 * math.sqrt(1.0 + T.M11 - T.M00 - T.M22) #float s = 2.0f * sqrtf( 1.0f + a[1][1] - a[0][0] - a[2][2]);
            qw = (T.M02 - T.M20) / s #q.w = (a[0][2] - a[2][0] ) / s;
            qx = (T.M01 + T.M10) / s #q.x = (a[0][1] + a[1][0] ) / s;
            qy = 0.25 * s #q.y = 0.25f * s;
            qz = (T.M12 + T.M21) / s #q.z = (a[1][2] + a[2][1] ) / s;
        else:
            # print "case 4"
            s = 2.0 * math.sqrt(1.0 + T.M22 - T.M00 - T.M11) # float s = 2.0f * sqrtf( 1.0f + a[2][2] - a[0][0] - a[1][1] );
            qw = (T.M10 - T.M01) / s  # q.w = (a[1][0] - a[0][1] ) / s;
            qx = (T.M02 + T.M20) / s # q.x = (a[0][2] + a[2][0] ) / s;
            qy = (T.M12 + T.M21) / s # q.y = (a[1][2] + a[2][1] ) / s;
            qz = 0.25 * s  # q.z = 0.25f * s;
            
        return [qw, qx, qy, qz]
    
    def rotation_to_euler_angles(self, T):
        '''
        create euler angles from matrix
        TODO: Kathrin or Romana :) 
        '''
        ex, ey, ez = [0, 0, 0]
        return [ex, ey, ez]
    

    def rotation_from_angle_axis(self, angle_axis):
        ax = rg.Vector3d(angle_axis)
        ax.Unitize()
        R = rg.Transform.Rotation(angle_axis.Length, ax, rg.Point3d(0,0,0)) 
        return R
    
    def get_transformation_from(self, other = None):
        '''
        returns the transformation matrix either from the world xy to self, or from another plane to self,
        other can be a frame or a plane
        '''
        if other == None:
            return rg.Transform.PlaneToPlane(rg.Plane.WorldXY, self.plane)
        else:
            if type(other) == rg.Plane: 
                return rg.Transform.PlaneToPlane(other, self.plane)
            else:
                return rg.Transform.PlaneToPlane(other.plane, self.plane)
    
    def get_transformation_to(self, other = None):
        '''
        returns the transformation matrix either from self to the world xy, or from self to another plane,
        other can be a frame or a plane
        '''
        if other == None:
            return rg.Transform.PlaneToPlane(self.plane, rg.Plane.WorldXY)
        else:            
            if type(other) == rg.Plane: 
                return rg.Transform.PlaneToPlane(self.plane, other)
            else:
                return rg.Transform.PlaneToPlane(self.plane, other.plane)
            
    def transform(self, T):
        '''
        transform the frame with a Rhino transformation matrix
        '''
        self.plane.Transform(T)
        self.update_geo(self.plane)
    
    def rotate(self, angle, axis, centerpt):
        '''
        rotate the frame with angle, axis and centerpoint
        '''
        self.plane.Rotate(math.radians(angle), axis, centerpt)
        self.update_geo(self.plane)
    
    def translate(self, vector):
        '''
        translate the frame by a vector
        '''
        self.plane.Translate(vector)
        self.update_geo(self.plane)  
    
    def copy(self):
        '''
        return a deepcopy of the frame
        '''
        return copy.deepcopy(self)


if __name__ == '__main__':
    
    plane = rg.Plane(rg.Point3d(6,9,5), rg.Vector3d(8,4,7))
    frame = Frame(plane)
    print frame.plane
    
    print frame.get_pose_quaternion()
    print frame.get_pose_angle_axis()